import sys
import base64
from pathlib import Path

import streamlit as st

# ==========================================================
# PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND)
# ==========================================================

st.set_page_config(
    page_title="StoreScope | Retail Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# PROJECT ROOT
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# ==========================================================
# IMPORTS
# ==========================================================

from src.data_loader import load_data
from src import components

# ==========================================================
# ASSETS
# ==========================================================

ASSET_DIR = Path(__file__).parent / "assets"

CSS_FILE = ASSET_DIR / "style.css"

# Change if your image is png
BACKGROUND_IMAGE = ASSET_DIR / "background.jpg"

# ==========================================================
# LOAD CSS
# ==========================================================

def get_base64(path: Path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


if CSS_FILE.exists():

    css = CSS_FILE.read_text(encoding="utf-8")

    if BACKGROUND_IMAGE.exists():

        css = css.replace(
            "__BACKGROUND__",
            get_base64(BACKGROUND_IMAGE)
        )

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )

else:

    st.warning("style.css not found.")

# ==========================================================
# LOAD DATA
# ==========================================================

try:

    df = load_data()

except Exception as e:

    st.error(f"Unable to load dataset.\n\n{e}")

    st.stop()

# ==========================================================
# HEADER
# ==========================================================

st.title("📊 StoreScope")

st.markdown(
    """
### Retail Intelligence Dashboard

Analyze sales, profit, customers, products and business
performance using interactive visual analytics.

Use the filters on the left to explore the Global Superstore dataset.
"""
)

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

filtered_df = components.dashboard_filters(df)

# ==========================================================
# DASHBOARD
# ==========================================================

components.dashboard_view(filtered_df)

# ==========================================================
# EXPORT
# ==========================================================

st.divider()

st.subheader("Export Filtered Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download CSV",
    data=csv,
    file_name="storescope_filtered_data.csv",
    mime="text/csv",
    use_container_width=True,
)