import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import os
import threading
import time
import requests

# Global variable to track if assets server is running
_assets_server_running = False
_assets_server_thread = None

def start_assets_server():
    """Start the assets server if not already running"""
    global _assets_server_running, _assets_server_thread
    
    if _assets_server_running:
        return True
    
    try:
        # Import and start the assets server
        import sys
        sys.path.append(str(Path(__file__).parent.parent))
        from serve_assets import start_assets_server as start_server
        
        _assets_server_thread = start_server(8081)
        _assets_server_running = True
        
        # Test if server is responding
        time.sleep(3)
        try:
            response = requests.get("http://localhost:8081/", timeout=5)
            return response.status_code == 200
        except:
            return False
            
    except Exception as e:
        st.error(f"Failed to start assets server: {e}")
        return False

def render_landing(**kwargs):
    """
    Render the TruthLens React landing page component.
    Uses an assets server to properly serve React files with correct MIME types.
    """
    
    # Get the build directory
    build_dir = Path(__file__).parent / "frontend" / "dist"
    index_html_path = build_dir / "index.html"
    
    # Check if files exist
    if not build_dir.exists():
        st.error("❌ React build directory not found. Run 'npm run build' in tl_frontend/frontend/")
        render_landing_fallback()
        return None
        
    if not index_html_path.exists():
        st.error("❌ index.html not found in build directory")
        render_landing_fallback()
        return None
    
    # Start assets server
    st.info("🚀 Starting assets server for React component...")
    server_started = start_assets_server()
    
    if not server_started:
        st.warning("⚠️ Assets server failed to start, trying direct embedding...")
        return render_landing_direct()
    
    try:
        # Read the HTML file and modify it to use the assets server
        with open(index_html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Replace relative asset paths with absolute URLs to our assets server
        html_content = html_content.replace(
            './assets/', 'http://localhost:8081/assets/'
        ).replace(
            'src="./assets/', 'src="http://localhost:8081/assets/'
        ).replace(
            'href="./assets/', 'href="http://localhost:8081/assets/'
        )
        
        # Add meta tags for proper rendering
        enhanced_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>TruthLens React Component</title>
            <style>
                body {{ margin: 0; padding: 0; }}
                #root {{ width: 100%; min-height: 600px; }}
            </style>
        </head>
        <body>
            <div id="root"></div>
            {html_content[html_content.find('<script'):html_content.rfind('</body>')]}
        </body>
        </html>
        """
        
        # Display the component
        st.success("✅ Assets server running - Loading React component...")
        components.html(enhanced_html, height=700, scrolling=False)
        
        return "assets_server"
        
    except Exception as e:
        st.error(f"❌ Error loading React component with assets server: {e}")
        return render_landing_direct()

def render_landing_direct():
    """
    Direct embedding approach (fallback method)
    """
    build_dir = Path(__file__).parent / "frontend" / "dist"
    index_html_path = build_dir / "index.html"
    
    try:
        with open(index_html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        st.info("🔄 Trying direct HTML embedding...")
        
        # Try to inline the CSS and JS content
        assets_dir = build_dir / "assets"
        if assets_dir.exists():
            # Find CSS and JS files
            css_files = list(assets_dir.glob("*.css"))
            js_files = list(assets_dir.glob("*.js"))
            
            # Inline CSS
            css_content = ""
            for css_file in css_files:
                try:
                    with open(css_file, 'r', encoding='utf-8') as f:
                        css_content += f.read()
                except Exception as e:
                    st.warning(f"Could not read CSS file {css_file.name}: {e}")
            
            # Create inlined HTML
            inlined_html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>TruthLens Component</title>
                <style>{css_content}</style>
            </head>
            <body>
                <div id="root"></div>
                <div id="react-info">
                    <h2>🚀 TruthLens React Component</h2>
                    <p>React frontend is being loaded...</p>
                    <p><strong>Note:</strong> This is a direct embedding approach.</p>
                </div>
                
                <script>
                    console.log("TruthLens React component container loaded");
                    // Note: React JS cannot be safely inlined due to module imports
                    // This serves as a fallback display
                </script>
            </body>
            </html>
            """
            
            components.html(inlined_html, height=400)
            st.warning("⚠️ Showing React container with CSS - JavaScript modules cannot be inlined")
            return "direct_css_only"
        
        else:
            st.error("❌ Assets directory not found")
            render_landing_fallback()
            return None
            
    except Exception as e:
        st.error(f"❌ Direct embedding failed: {e}")
        render_landing_fallback()
        return None

def render_landing_fallback():
    """
    Fallback rendering when React component is not available.
    """
    st.markdown("""
    ### 🚀 TruthLens Landing Page (Fallback Mode)
    
    **AI-Powered Misinformation Detection System**
    
    *The React component is currently unavailable. Using Streamlit fallback interface.*
    
    #### 🎯 Key Features:
    - 🔍 **Advanced Text Analysis** - AI-powered fact checking
    - 🖼️ **Image Forensics** - Detect manipulated images  
    - 🔗 **URL Investigation** - Verify article sources
    - 📊 **Risk Assessment** - Comprehensive credibility scoring
    - 🛡️ **Real-time Protection** - Immediate misinformation alerts
    
    ---
    """)
    
    # Hero section with gradient background
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 2rem 0;
    ">
        <h1 style="font-size: 3rem; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            🔍 TruthLens
        </h1>
        <h2 style="font-size: 1.5rem; margin-bottom: 2rem; opacity: 0.9;">
            AI-Powered Misinformation Detection
        </h2>
        <p style="font-size: 1.1rem; max-width: 600px; margin: 0 auto; line-height: 1.6;">
            Detect, verify, and report misinformation with advanced AI technology. 
            Protecting truth in the digital age.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; border: 1px solid #ddd; border-radius: 8px;">
            <h3>🧠</h3>
            <h4>AI Analysis</h4>
            <p>Advanced machine learning algorithms</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; border: 1px solid #ddd; border-radius: 8px;">
            <h3>⚡</h3>
            <h4>Real-time</h4>
            <p>Instant fact-checking results</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; border: 1px solid #ddd; border-radius: 8px;">
            <h3>🛡️</h3>
            <h4>Secure</h4>
            <p>Privacy-focused analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; border: 1px solid #ddd; border-radius: 8px;">
            <h3>📊</h3>
            <h4>Detailed</h4>
            <p>Comprehensive reports</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick analysis demo
    with st.expander("🧪 Try Quick Analysis", expanded=False):
        sample_text = st.text_area(
            "Enter text to analyze:",
            value="Scientists discover breakthrough that could change everything! Doctors hate this simple trick. Share before it's banned!",
            help="This is a demo analysis using pattern recognition"
        )
        
        if st.button("🔍 Analyze Content", type="primary"):
            # Simple pattern-based analysis for demo
            risk_indicators = ["breakthrough", "doctors hate", "banned", "secret", "shocking", "urgent", "share"]
            risk_count = sum(1 for indicator in risk_indicators if indicator in sample_text.lower())
            risk_score = min(100, risk_count * 15)
            credibility = 100 - risk_score
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Risk Score", f"{risk_score}/100", delta=f"{risk_count} indicators")
            with col2:
                st.metric("Credibility", f"{credibility}/100")
            with col3:
                threat_level = "HIGH" if risk_score > 60 else "MEDIUM" if risk_score > 30 else "LOW"
                st.metric("Threat Level", threat_level)
            
            if risk_score > 60:
                st.error("🚨 HIGH RISK: Multiple manipulation indicators detected!")
            elif risk_score > 30:
                st.warning("⚠️ MEDIUM RISK: Some concerning patterns found")
            else:
                st.success("✅ LOW RISK: Content appears relatively credible")

# For backward compatibility
tl_frontend = render_landing