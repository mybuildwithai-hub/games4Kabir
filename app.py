import streamlit as st
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Toddler Fun & Sounds", 
    page_icon="👶", 
    layout="centered"
)

# --- 2. SESSION STATE (The App's Memory) ---
# This checks if we are currently playing a video or looking at the menu
if 'playing_video' not in st.session_state:
    st.session_state.playing_video = None

# --- 3. THE VIDEO PLAYER (SCREEN A) ---
if st.session_state.playing_video:
    # Use a container to make it look organized
    with st.container():
        st.title("Watch! 📺")
        
        # Display the video
        # We use the ?autoplay=1&mute=1 trick for iPad compatibility
        st.video(st.session_state.playing_video)
        
        st.write("---")
        # Big button to go back to the menu
        if st.button("⬅️ BACK TO GAMES", use_container_width=True):
            st.session_state.playing_video = None
            st.rerun()

# --- 4. THE MAIN MENU (SCREEN B) ---
else:
    st.title("Tap an Animal! 🐾")
    st.subheader("Choose one for your toddler:")

    # Create two columns for the buttons
    col1, col2 = st.columns(2)

    with col1:
        # LION BUTTON
        # Link: A roaring lion (Shorts converted to embed)
        if st.button("🦁 LION", use_container_width=True):
            st.session_state.playing_video = "https://www.youtube.com/embed/zgxUh6RYo7Y?autoplay=1&mute=1"
            st.rerun()

        # DUCK BUTTON
        if st.button("🦆 DUCK", use_container_width=True):
            st.session_state.playing_video = "https://www.youtube.com/embed/u6_f6OshL90?autoplay=1&mute=1"
            st.rerun()

    with col2:
        # DOG BUTTON
        if st.button("🐶 DOG", use_container_width=True):
            st.session_state.playing_video = "https://www.youtube.com/embed/j_S_9_193mY?autoplay=1&mute=1"
            st.rerun()

        # ELEPHANT BUTTON
        if st.button("🐘 ELEPHANT", use_container_width=True):
            st.session_state.playing_video = "https://www.youtube.com/embed/Gn8S_C_uXmY?autoplay=1&mute=1"
            st.rerun()

    # --- 5. CATEGORY SECTION (For Future Growth) ---
    st.write("---")
    st.caption("Tip: Add this page to your iPad Home Screen for a full-screen experience.")
