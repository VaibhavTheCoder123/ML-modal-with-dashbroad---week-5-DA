import sys
from pathlib import Path
from pathlib import Path

# =================================
# ADD PROJECT ROOT TO PYTHON PATH
# =================================

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))



import streamlit as st


from src.data_loader import load_data
from src import components



# =================================
# PAGE CONFIG
# =================================

st.set_page_config(
    page_title="StoreScope | Retail Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)



# =================================
# LOAD DATA
# =================================

try:

    df = load_data()

except Exception as e:

    st.error(
        f"Data loading failed:\n\n{e}"
    )

    st.stop()



# =================================
# HEADER
# =================================

st.title(
    "📊 StoreScope: Retail Analytics Dashboard"
)


st.markdown(
    """
    Interactive dashboard for Global Superstore
    sales, profit, customer and product analysis.
    """
)



# =================================
# FILTERS
# =================================

filtered_df = components.dashboard_filters(df)



# =================================
# DASHBOARD
# =================================

components.dashboard_view(filtered_df)



# =================================
# EXPORT
# =================================

st.divider()

st.subheader(
    "Export Filtered Data"
)


csv = filtered_df.to_csv(
    index=False
).encode("utf-8")



st.download_button(
    label="⬇️ Download CSV",
    data=csv,
    file_name="storescope_filtered_data.csv",
    mime="text/csv"
)

# Load Custom CSS

css_path = Path(__file__).parent / "assets" / "style.css"

with open(css_path) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )