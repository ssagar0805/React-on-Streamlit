#!/usr/bin/env python3
"""
Test script to verify React component integration
"""

import streamlit as st
import sys
from pathlib import Path

# Configure Streamlit
st.set_page_config(
    page_title="React Component Test",
    page_icon="🧪",
    layout="wide"
)

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

st.title("🧪 React Component Integration Test")

# Test 1: Import test
st.header("1. Import Test")
try:
    from tl_frontend import render_landing
    st.success("✅ Successfully imported `render_landing` from `tl_frontend`")
    component_imported = True
except ImportError as e:
    st.error(f"❌ Failed to import component: {e}")
    component_imported = False
except Exception as e:
    st.error(f"❌ Unexpected error importing component: {e}")
    component_imported = False

# Test 2: Component path test
st.header("2. Component Path Test")
try:
    build_dir = Path(__file__).parent / "tl_frontend" / "frontend" / "dist"
    st.write(f"**Build directory:** `{build_dir}`")
    st.write(f"**Directory exists:** {build_dir.exists()}")
    
    if build_dir.exists():
        index_html = build_dir / "index.html"
        st.write(f"**index.html exists:** {index_html.exists()}")
        
        if index_html.exists():
            # Show first few lines of index.html
            with open(index_html, 'r') as f:
                content = f.read()
                st.code(content[:500] + "..." if len(content) > 500 else content, language="html")
        
        # List assets
        assets_dir = build_dir / "assets"
        if assets_dir.exists():
            assets = list(assets_dir.glob("*"))
            st.write(f"**Assets found:** {len(assets)} files")
            for asset in assets[:10]:  # Show first 10
                st.write(f"- {asset.name}")
    
except Exception as e:
    st.error(f"❌ Error checking component path: {e}")

# Test 3: Component rendering test
st.header("3. Component Rendering Test")
if component_imported:
    try:
        st.info("Attempting to render React component...")
        
        # Create a container for the component
        component_container = st.container()
        
        with component_container:
            result = render_landing()
            
        st.success("✅ React component rendered successfully!")
        st.write(f"**Component return value:** {result}")
        
    except Exception as e:
        st.error(f"❌ Error rendering component: {e}")
        st.write("**Error details:**")
        st.exception(e)
else:
    st.warning("⚠️ Skipping render test - component not imported")

# Test 4: Browser console check
st.header("4. Browser Console Check")
st.info("""
🔍 **Manual Check Required:**
1. Open browser developer tools (F12)
2. Check the Console tab for JavaScript errors
3. Look for any MIME type errors or 404s
4. Verify that React component assets are loading

**Common issues to look for:**
- `net::ERR_ABORTED 404` - Asset not found
- `Refused to execute script... MIME type ('text/html')` - MIME type mismatch
- React errors related to component initialization
""")

# Test 5: Debug info
st.header("5. Debug Information")
st.write("**Python version:**", sys.version)
st.write("**Streamlit version:**", st.__version__)

# Show environment
import os
st.write("**Current working directory:**", os.getcwd())
st.write("**Script location:**", __file__)

# Check for dev/prod mode detection
dev_mode_env = os.getenv('TL_USE_DEV', '0')
st.write(f"**TL_USE_DEV environment variable:** {dev_mode_env}")

st.markdown("---")
st.markdown("**💡 Next Steps:**")
st.markdown("""
1. If import test ✅ and component path test ✅ but rendering fails ❌:
   - Check browser console for JavaScript/MIME errors
   - Verify asset paths in built index.html are relative (`./assets/...`)

2. If all tests pass ✅ but component appears blank:
   - Check browser console for React errors
   - Verify component JavaScript is executing

3. If MIME type errors occur:
   - Ensure Vite build uses `base: "./"` for relative paths
   - Check Streamlit is serving assets correctly
""")