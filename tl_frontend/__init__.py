import streamlit.components.v1 as components
from pathlib import Path

# Locate the build folder (to be created next)
_build_dir = Path(__file__).parent / "frontend" / "dist"


# Declare the component, pointing at the build directory
tl_frontend = components.declare_component(
    name="tl_frontend",
    path=str(_build_dir)
)

def render_landing(**kwargs):
    """
    Render the custom TruthLens landing page component.
    Any kwargs passed here will be forwarded to the React component.
    """
    return tl_frontend(**kwargs)
