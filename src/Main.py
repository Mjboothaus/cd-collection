from pathlib import Path

import streamlit as st

from helper_functions import read_render_markdown_file, read_toml_file
from sidebar import create_sidebar

APP_TITLE = "CD-Collection"

# Note this must be the first function call in the Streamlit app code

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.databooth.com.au/help',
        'Report a bug': "https://www.databooth.com.au/bug",
        "About": "Created with love & care at DataBooth - www.databooth.com.au"
    },
)

config = read_toml_file()

SUB_TITLE = config["st-app"]["SUB_TITLE"]

def create_app_header(app_title, subtitle=SUB_TITLE):
    st.header(app_title)
    if subtitle is not None:
        st.subheader(subtitle)
    return None


create_app_header(APP_TITLE, SUB_TITLE)
# create_sidebar()
read_render_markdown_file("docs/app_main.md", output="streamlit")
