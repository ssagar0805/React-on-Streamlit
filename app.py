# app.py

import streamlit as st
import sys
from pathlib import Path

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# --- Hide Streamlit header, toolbar, menu, and footer ---
st.markdown("""
    <style>
        /* Hide top header (logo + menu) */
        header[data-testid="stHeader"] {
            display: none;
        }
        /* Hide the “Deploy” toolbar */
        div[data-testid="stToolbar"] {
            display: none;
        }
        /* Hide the hamburger menu and “About” menu */
        #MainMenu {
            visibility: hidden;
        }
        /* Hide the default footer (“Made with Streamlit”) */
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from config import Config, setup_page_config
from utils.ai_services import GeminiService, FactCheckService
from utils.news_services import NewsAggregator
from utils.security import SecurityService
from utils.database import FirebaseService

# Import page interfaces (RENAMED/UPDATED)
from pages.home import show_home
from pages.archive import show_archive
from pages.learn import show_learn
from pages.authority import show_authority

# ======================
# Initialize Services
# ======================
config = Config()
gemini_service = GeminiService()
fact_check_service = FactCheckService()
news_aggregator = NewsAggregator()
security_service = SecurityService()
firebase_service = FirebaseService()


st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# ======================
# Utility: Service Status Badges
# ======================
# def display_status_badges():
#     """Show compact service status inline in the header."""
#     services_status = {
#         "Gemini": gemini_service.test_connection(),
#         "FactCheck": fact_check_service.test_connection(),
#         "News": news_aggregator.test_connection(),
#         "Security": security_service.test_connection(),
#         "DB": firebase_service.test_connection(),
#     }
#     parts = []
#     for name, ok in services_status.items():
#         emoji = "✅" if ok else "❌"
#         parts.append(f"{emoji} {name}")
#     st.markdown(" | ".join(parts))

# ======================
# Main Function
# ======================
def main():
    setup_page_config()
    load_custom_css()

    # Authentication
    if not check_authentication():
        return

    # --- Top Header Layout ---
    header_left, header_center, header_right = st.columns([1.4, 2.2, 1.4])

    with header_left:
        st.markdown(
            '<div class="tl-header"><h3>🔎 TruthLens</h3><p style="margin:0">AI Misinformation Detection</p></div>',
            unsafe_allow_html=True
        )

    with header_center:
        # Navigation Buttons
        cols = st.columns(4)
        pages = ["Home", "Archive", "Learn", "Authority"]
        emojis = ["🏠", "📰", "📚", "👮"]

        for i, (page, icon) in enumerate(zip(pages, emojis)):
            if cols[i].button(f"{icon} {page}", key=f"nav_{page}"):
                st.session_state.page = page

        # Default page (first load = Home)
        if "page" not in st.session_state:
            st.session_state.page = "Home"

    # with header_right:
    #     st.markdown('<div class="tl-badges">', unsafe_allow_html=True)
    #     display_status_badges()
    #     st.markdown('</div>', unsafe_allow_html=True)

    # --- Routing ---
    page = st.session_state.page
    if page == "Home":
        show_home()
    elif page == "Archive":
        show_archive()
    elif page == "Learn":
        show_learn()
    elif page == "Authority":
        show_authority()

# ======================
# Custom CSS Loader
# ======================
def load_custom_css():
    """Load custom CSS for better UI"""
    try:
        with open('assets/styles.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ styles.css not found – using default styling")

# ======================
# Authentication
# ======================
def check_authentication():
    """Simple authentication with public/authority flows"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.markdown("""
        <div class="hero-section">
            <h1>🔐 TruthLens Access Portal</h1>
            <p>🚀 Advanced AI-Powered Misinformation Detection System</p>
            <p>🛡️ Powered by Google Cloud & Gemini AI</p>
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
                    if security_service.verify_authority_credentials(username, password):
                        st.session_state.authenticated = True
                        st.session_state.user_type = "authority"
                        st.session_state.authority_username = username
                        st.success(f"✅ Logged in as {username}")
                        st.rerun()
                    else:
                        st.error("❌ Invalid credentials")

        return False

    return True

if __name__ == "__main__":
    main()
