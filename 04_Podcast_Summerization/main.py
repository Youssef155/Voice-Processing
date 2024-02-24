from api_communication import *
import streamlit as st

st.title('Welcome to Listen Notes Podcast Summerizer')
episode_Id = st.sidebar.text_input("Enter Podcast ID")
button = st.sidebar.button("Get Summary!", on_click=save_transcript, args=(episode_Id,))

def get_clean_time(start_ms):
    seconds = int((start_ms / 1000) % 60)
    minutes = int((start_ms / (1000 * 60)) % 60)
    hours = int((start_ms / (1000 * 60 * 60)) % 24)

    if hours > 0:
        st_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        st_time = f"{minutes:02d}:{seconds:02d}"

    return st_time

if button:
    filename = episode_Id + "_Chapters.json"
    with open(filename, 'r') as f:
        data = json.load(f)

        chapters = data['chapters']
        podcast_title = data['podcast_title']
        episode_title = data['episode_title']
        thumbnail = data['episode_thumbnail']

    st.header(f"{podcast_title} - {episode_title}")
    st.image(thumbnail)
    for chp in chapters:
        with st.expander(chp['gist'] + ' - ' + get_clean_time(chp['start'])):
            chp['summary']