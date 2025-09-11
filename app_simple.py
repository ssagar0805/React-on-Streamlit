#!/usr/bin/env python3
"""
Simplified Streamlit app focused on React component integration
This version removes complex dependencies to focus on getting the React frontend working
"""

import streamlit as st
import sys
from pathlib import Path

# Configure Streamlit page (must be first Streamlit command)
st.set_page_config(
    page_title="TruthLens - AI-Powered Fact Checking",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit branding and UI elements
st.markdown("""
    <style>
        /* Hide top header (logo + menu) */
        header[data-testid="stHeader"] {
            display: none;
        }
        /* Hide the "Deploy" toolbar */
        div[data-testid="stToolbar"] {
            display: none;
        }
        /* Hide the hamburger menu and "About" menu */
        #MainMenu {
            visibility: hidden;
        }
        /* Hide the default footer ("Made with Streamlit") */
        footer {
            visibility: hidden;
        }
        /* Remove padding from main container */
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            max-width: none;
        }
    </style>
""", unsafe_allow_html=True)

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Import React component
try:
    from tl_frontend import render_landing
    REACT_COMPONENT_AVAILABLE = True
except Exception as e:
    st.error(f"Failed to import React component: {e}")
    REACT_COMPONENT_AVAILABLE = False

def main():
    """Main application function"""
    
    # Check authentication
    if not check_authentication():
        return
    
    # Navigation
    show_navigation()
    
    # Get current page from session state
    current_page = st.session_state.get('page', 'Home')
    
    # Route to appropriate page
    if current_page == 'Home':
        show_home_page()
    elif current_page == 'Archive':
        show_archive_page()
    elif current_page == 'Learn':
        show_learn_page()
    elif current_page == 'Authority':
        show_authority_page()

def check_authentication():
    """Simple authentication system"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h1>🔐 TruthLens Access Portal</h1>
            <p style="font-size: 1.2rem;">🚀 Advanced AI-Powered Misinformation Detection System</p>
            <p style="color: #666;">🛡️ Powered by Google Cloud & Gemini AI</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            access_type = st.radio(
                "🎯 Select Access Type:",
                ["🔍 Public Access", "👮 Authority Login"],
                help="Public users get analysis tools. Authority users get monitoring tools."
            )
            
            if access_type == "🔍 Public Access":
                if st.button("🚀 Enter as Public User", type="primary", use_container_width=True):
                    st.session_state.authenticated = True
                    st.session_state.user_type = "public"
                    st.success("✅ Logged in as Public User")
                    st.rerun()
            
            else:
                username = st.text_input("👤 Username", placeholder="Enter your username")
                password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")
                
                if st.button("🔐 Authority Login", type="primary", use_container_width=True):
                    # Simple demo credentials
                    if username == "admin" and password == "demo123":
                        st.session_state.authenticated = True
                        st.session_state.user_type = "authority"
                        st.session_state.authority_username = username
                        st.success(f"✅ Logged in as {username}")
                        st.rerun()
                    else:
                        st.error("❌ Invalid credentials (try: admin/demo123)")
        
        return False
    
    return True

def show_navigation():
    """Show navigation header"""
    header_left, header_center, header_right = st.columns([1.4, 2.2, 1.4])
    
    with header_left:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <h3 style="margin: 0;">🔎 TruthLens</h3>
            <p style="margin: 0; font-size: 0.9rem; color: #666;">AI Misinformation Detection</p>
        </div>
        """, unsafe_allow_html=True)
    
    with header_center:
        # Navigation Buttons
        cols = st.columns(4)
        pages = ["Home", "Archive", "Learn", "Authority"]
        emojis = ["🏠", "📰", "📚", "👮"]
        
        for i, (page, icon) in enumerate(zip(pages, emojis)):
            if cols[i].button(f"{icon} {page}", key=f"nav_{page}"):
                st.session_state.page = page
                st.rerun()
        
        # Default page
        if "page" not in st.session_state:
            st.session_state.page = "Home"
    
    with header_right:
        user_type = st.session_state.get('user_type', 'unknown')
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem;">
            <p style="margin: 0; font-size: 0.9rem;">User: <strong>{user_type.title()}</strong></p>
        </div>
        """, unsafe_allow_html=True)

def show_home_page():
    """Home page with React component"""
    st.markdown("---")
    
    # React Landing Page Component
    if REACT_COMPONENT_AVAILABLE:
        try:
            st.markdown("### 🚀 React Frontend Component")
            st.info("Loading React landing page component...")
            
            # Render the React component
            render_landing()
            
            st.success("✅ React component loaded successfully!")
            
        except Exception as e:
            st.error(f"❌ Error rendering React component: {e}")
            show_fallback_home()
    else:
        st.warning("⚠️ React component not available, showing fallback")
        show_fallback_home()

def show_fallback_home():
    """Fallback home page if React component fails"""
    st.markdown("""
    ### 🏠 Welcome to TruthLens
    
    **AI-Powered Misinformation Detection System**
    
    This application integrates a React frontend with Streamlit backend for advanced fact-checking capabilities.
    
    #### 🔧 Technical Status:
    - ✅ Streamlit backend running
    - ❓ React frontend component status varies
    - 🎯 Focus: Getting React-Streamlit integration working
    
    #### 📝 Quick Analysis Tools:
    """)
    
    # Simple text analysis
    with st.expander("📝 Quick Text Analysis", expanded=True):
        user_input = st.text_area(
            "Enter text to analyze:",
            placeholder="Paste news articles, social media posts, or claims here...",
            height=100
        )
        
        if st.button("🔍 Analyze Text", type="primary"):
            if user_input.strip():
                analyze_text_simple(user_input)
            else:
                st.warning("⚠️ Please enter some text to analyze")

def analyze_text_simple(text):
    """Simple text analysis without external APIs"""
    st.subheader("📊 Analysis Results")
    
    # Simple risk scoring based on keywords
    risk_keywords = [
        'breaking', 'urgent', 'shocking', 'unbelievable', 'secret', 'hidden',
        'they don\'t want', 'conspiracy', 'cover-up', 'fake news', 'lie'
    ]
    
    manipulation_keywords = [
        'share immediately', 'forward this', 'spread the word', 'tell everyone',
        'before it\'s deleted', 'going viral', 'must see'
    ]
    
    text_lower = text.lower()
    risk_count = sum(1 for keyword in risk_keywords if keyword in text_lower)
    manip_count = sum(1 for keyword in manipulation_keywords if keyword in text_lower)
    
    # Calculate risk score
    risk_score = min(100, (risk_count * 15) + (manip_count * 20) + len([c for c in text if c in '!?']) * 2)
    credibility_score = max(0, 100 - risk_score)
    
    # Display results
    col1, col2, col3 = st.columns(3)
    
    with col1:
        color = "#ff4444" if risk_score > 70 else "#ff8800" if risk_score > 40 else "#44ff44"
        st.markdown(f"""
        <div style="background-color: {color}; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Risk Score</h3>
            <h1>{risk_score}/100</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        color = "#44ff44" if credibility_score > 70 else "#ff8800" if credibility_score > 40 else "#ff4444"
        st.markdown(f"""
        <div style="background-color: {color}; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Credibility</h3>
            <h1>{credibility_score}/100</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        threat_level = "HIGH" if risk_score > 70 else "MEDIUM" if risk_score > 40 else "LOW"
        color = "#ff4444" if threat_level == "HIGH" else "#ff8800" if threat_level == "MEDIUM" else "#44ff44"
        st.markdown(f"""
        <div style="background-color: {color}; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Threat Level</h3>
            <h1>{threat_level}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    # Simple analysis
    st.markdown("### 🔍 Analysis Details")
    
    if risk_count > 0:
        st.warning(f"⚠️ Found {risk_count} potential risk indicator(s)")
    
    if manip_count > 0:
        st.warning(f"🎯 Found {manip_count} manipulation tactic(s)")
    
    if risk_score < 30:
        st.success("✅ Content appears relatively low-risk")
    elif risk_score < 70:
        st.warning("⚠️ Content shows some concerning patterns")
    else:
        st.error("🚨 Content shows high-risk patterns")

def show_archive_page():
    """Archive page placeholder"""
    st.markdown("---")
    st.markdown("### 📰 Analysis Archive")
    st.info("Archive functionality will store and display previous analyses")
    
    # Placeholder content
    st.markdown("""
    **Recent Analyses:**
    - 📝 Text Analysis #1 - Risk: 45/100
    - 🔗 URL Investigation #1 - Status: Verified
    - 🖼️ Image Forensics #1 - Authenticity: 87/100
    """)

def show_learn_page():
    """Learn page placeholder"""
    st.markdown("---")
    st.markdown("### 📚 Learn About Misinformation")
    st.info("Educational content about identifying and combating misinformation")
    
    st.markdown("""
    #### 🎯 Common Misinformation Tactics:
    1. **Emotional Manipulation** - Using fear, anger, or outrage
    2. **False Urgency** - "Share before it's deleted!"
    3. **Authority Undermining** - "Experts don't want you to know"
    4. **Conspiracy Language** - "Hidden truth" narratives
    5. **Selective Evidence** - Cherry-picking data points
    """)

def show_authority_page():
    """Authority dashboard placeholder"""
    st.markdown("---")
    st.markdown("### 👮 Authority Dashboard")
    
    user_type = st.session_state.get('user_type', 'public')
    if user_type != 'authority':
        st.warning("⚠️ Authority access required")
        return
    
    st.info("Authority monitoring tools and reporting dashboard")
    
    # Placeholder metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Reports Today", "23", "↑ 5")
    
    with col2:
        st.metric("High Risk Content", "8", "↓ 2")
    
    with col3:
        st.metric("Verified Claims", "156", "↑ 12")
    
    with col4:
        st.metric("Active Users", "1,234", "↑ 45")

if __name__ == "__main__":
    main()