from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

CD_INFO_FILE = "data/cd_info.parquet"  # created in notebooks/process-apple-music-urls.ipynb


def create_embed_apple_music_iframe(album_info):
    embed_html = """
    <html>
        <iframe allow="autoplay *; encrypted-media *;" frameborder="0" height="450"
            style="width:100%;max-width:660px;overflow:hidden;background:transparent;"
            sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-top-navigation-by-user-activation"
            src="https://embed.music.apple.com/au/album/APPLE_ALBUM_INFO">
        </iframe>
    </html>
    """
    embed_html = embed_html.replace("APPLE_ALBUM_INFO", album_info)
    return embed_html


@st.cache
def get_cd_info():
    if Path(CD_INFO_FILE).exists():
        cd_info_df = pd.read_parquet("data/cd_info.parquet")
        return cd_info_df
    else:
        raise FileNotFoundError
    

# Load album data, cache and sort by title
 
cd_info_df = get_cd_info().sort_values(by="Album Title")

# Create UI

album_title = st.sidebar.selectbox(
    label="Select CD (Album):", options=cd_info_df["Album Title"]
)

artist = cd_info_df[cd_info_df["Album Title"] == album_title]["Artist"].iloc[0]
album_url = cd_info_df[cd_info_df["Album Title"] == album_title]["Apple Music URL"].iloc[0]
album_info = album_url.replace("https://music.apple.com/au/album/", "")

st.write(f"**{album_title}** by *{artist}*")

embed_html = create_embed_apple_music_iframe(album_info)
components.html(embed_html, height=600)