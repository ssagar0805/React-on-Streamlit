import streamlit as st

# Ensure sidebar doesn’t render the default multipage list
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Define pages by file path (relative to this file)
pages = [
    st.Page("app.py", title="App", icon=":material/home:", url_path="app", default=True),
    st.Page("pages/admin.py", title="Admin", icon=":material/admin_panel_settings:", url_path="admin"),
    st.Page("pages/authority.py", title="Authority", icon=":material/shield_person:", url_path="authority"),
    st.Page("pages/analytics.py", title="Analytics", icon=":material/insights:", url_path="analytics"),
    st.Page("pages/education.py", title="Education", icon=":material/school:", url_path="education"),
]

# Top navigation
current = st.navigation(pages=pages, position="top")

# Run selected page
current.run()
