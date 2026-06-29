from pathlib import Path
import streamlit as st
from PIL import Image

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume Arrnav Dutta - updated.pdf"
profile_pic = current_dir / "assets" / "profile-pic-ai.png"

# --- General Settings ---
PAGE_TITLE = "Arrnav Dutta | Online Resume"
PAGE_ICON = ":wave:"
NAME = "Arrnav Dutta"
DESCRIPTION = """
Aspiring Actuary | Avid Gamer | Problem Solver And Determined Learner
"""
EMAIL = "arrnav18.2002@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ard18/",
    "GitHub": "https://github.com/ard18"
}
PROJECTS = {
    "🏆 Actuarial Ratemaking & Reserving Project": "https://ratemaking-with-python.streamlit.app/"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello There!!")

