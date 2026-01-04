import streamlit as st
import time

st.set_page_config(page_title="Toddler TV", page_icon="📺")

# 1. Memory Check
if 'playing_video' not in st.session_state:
    st.session_state.playing_video = None

# 2. SCREEN A: Show the Video
if st.session_state.playing_video:
    video_url = st.session_state.playing_video
    
    st.title("Watch!")
    
    # This displays the video. 
    # Note: 'autoplay' on iPads is often restricted by Apple for web browsers, 
    # so the toddler might need to tap the play button once.
    st.video(video_url)
    
    # "Back" button for the parent or toddler to return early
    if st.button("Go Back"):
        st.session_state.playing_video = None
        st.rerun()

# 3. SCREEN B: The Main Menu
else:
    st.title("Tap to watch! 🐾")
    
    col1, col2 = st.columns(2)

    with col1:
        if st.button('🦁 Lion Video', use_container_width=True):
            # Using a kid-friendly National Geographic Lion clip
            st.session_state.playing_video = "https://www.youtube.com/shorts/x6FeFwnOT-Q"
            st.rerun()

    with col2:
        if st.button('🦆 Duck Video', use_container_width=True):
            # Using a simple duckling video
            st.session_state.playing_video = "https://www.youtube.com/watch?v=u6_f6OshL90"
            st.rerun()
