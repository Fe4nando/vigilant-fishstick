import streamlit as st
from streamlit.components.v1 import html
import os

# Get path to current directory
BASE_DIR = os.path.dirname(__file__)

# Load CSS
with open(os.path.join(BASE_DIR, "home.css"), "r", encoding="utf-8") as f:
    css = f"<style>{f.read()}</style>"

# Load HTML
with open(os.path.join(BASE_DIR, "Home.html"), "r", encoding="utf-8") as f:
    html_content = f.read()

st.markdown("""
    <style>
        .stApp {
            background-color: black;
            color: white;
        }
        .title-text {
            text-align: center;
            font-size: 4em;
            color: white;
            margin-top: 1em;
            font-family: Arial, sans-serif;
        }
    </style>
    <div class="title-text">IM SORRY</div>
""", unsafe_allow_html=True)


# Combine and render
st.set_page_config(page_title="im sorry", layout="wide")
html(css + html_content, height=1000, scrolling=False)
