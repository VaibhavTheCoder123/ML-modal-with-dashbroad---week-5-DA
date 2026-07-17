import base64
from pathlib import Path
import streamlit as st


def load_css():

    assets = Path(__file__).resolve().parent.parent / "dashboard" / "assets"

    css_file = assets / "style.css"

    background = assets / "background.jpg"      # change if png

    if not css_file.exists():
        return

    css = css_file.read_text(encoding="utf-8")

    if background.exists():

        with open(background, "rb") as img:

            encoded = base64.b64encode(
                img.read()
            ).decode()

        css = css.replace(
            "__BACKGROUND__",
            encoded
        )

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )