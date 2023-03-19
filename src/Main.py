from pathlib import Path

import streamlit as st

from helper_functions import read_render_markdown_file, read_toml_file
from sidebar import create_sidebar

config = read_toml_file()

APP_TITLE = config["st-app"]["APP_TITLE"]
SUB_TITLE = config["st-app"]["SUB_TITLE"]

st.set_page_config(
    page_title=APP_TITLE,
    layout="wide",
    menu_items={
        "About": "Created with love & care at DataBooth - www.databooth.com.au"
    },
)


def create_app_header(app_title, subtitle=None):
    st.header(app_title)
    if subtitle is not None:
        st.subheader(subtitle)
    return None


create_app_header(APP_TITLE, SUB_TITLE)
# create_sidebar()
read_render_markdown_file("docs/app_main.md", output="streamlit")
