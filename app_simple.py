# app_simple.py - Simplified version for React component testing

import streamlit as st
import sys
from pathlib import Path

# IMPORTANT: set_page_config must be the first Streamlit command
st.set_page_config(
    page_title="TruthLens - AI-Powered Fact Checking",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- Hide Streamlit header, toolbar, menu, and footer ---
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
        /* Custom styling */
        .stApp {
            background-color: #f8f9fa;
        }
    </style>
""", unsafe_allow_html=True)

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Import the React component wrapper
try:
    from tl_frontend import render_landing
    react_component_available = True
except ImportError as e:
    st.error(f"Failed to import React component: {e}")
    react_component_available = False

def main():
    """Simplified main function for testing React component integration"""
    
    # --- Authentication (simplified) ---
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        # --- React Landing Page Component ---
        if react_component_available:
            st.markdown("### 🎯 React Landing Page Component Test")
            st.info("The React component should render below this message:")
            
            # Render the React landing page component
            try:
                render_landing()
                st.success("✅ React component rendered successfully!")
            except Exception as e:
                st.error(f"❌ Failed to render React component: {e}")
        else:
            st.error("❌ React component is not available")
        
        # Simple authentication
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### 🔐 Authentication")
            if st.button("🚀 Enter App (Test Mode)", type="primary", use_container_width=True):
                st.session_state.authenticated = True
                st.rerun()
        return

    # --- Main App (after authentication) ---
    st.markdown("### 🎉 Welcome to TruthLens!")
    st.info("You have successfully authenticated. The React landing page component integration is working!")
    
    # Simple tabs to show the app is working
    tab1, tab2 = st.tabs(["📝 Text Analysis", "ℹ️ About"])
    
    with tab1:
        st.subheader("📝 Text Analysis")
        text_input = st.text_area("Enter text to analyze:", placeholder="Paste your content here...")
        if st.button("🔍 Analyze", type="primary"):
            if text_input.strip():
                st.success(f"✅ Analysis completed for {len(text_input)} characters!")
            else:
                st.warning("⚠️ Please enter some text to analyze")
    
    with tab2:
        st.subheader("ℹ️ About TruthLens")
        st.write("""
        **TruthLens** is an AI-powered misinformation detection platform.
        
        **Key Features:**
        - 🔍 Text forensics and fact-checking
        - 🖼️ Image analysis and manipulation detection
        - 🔗 URL investigation and source verification
        - 🛡️ Real-time threat assessment
        
        **Technology Stack:**
        - **Frontend:** React + TypeScript + Vite + Tailwind CSS
        - **Backend:** Streamlit + Python
        - **Integration:** Streamlit Components for React embedding
        """)
    
    # Logout button
    if st.sidebar.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()

if __name__ == "__main__":
    main()