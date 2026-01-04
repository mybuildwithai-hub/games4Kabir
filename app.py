import streamlit as st

# --- 1. SETTINGS ---
st.set_page_config(page_title="Toddler Play Box", page_icon="🎮", layout="wide")

# --- 2. THE APP BRAIN ---
if 'page' not in st.session_state:
    st.session_state.page = "main_menu"
if 'current_video' not in st.session_state:
    st.session_state.current_video = None

# --- 3. SCREEN: MASTER MENU ---
if st.session_state.page == "main_menu":
    st.title("Choose a Game! 👶")
    
    # Large navigation buttons
    if st.button("🐾 TAP AN ANIMAL", use_container_width=True):
        st.session_state.page = "animal_game"
        st.rerun()
        
    if st.button("🎨 COLOR LEARNING", use_container_width=True):
        st.session_state.page = "color_game"
        st.rerun()

# --- 4. SCREEN: ANIMAL SELECTION ---
elif st.session_state.page == "animal_game" and st.session_state.current_video is None:
    st.title("Tap an Animal! 🦁")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🦁 LION", use_container_width=True):
            st.session_state.current_video = "https://www.youtube.com/embed/zgxUh6RYo7Y?autoplay=1&mute=1"
            st.rerun()
        if st.button("🐶 DOG", use_container_width=True):
            st.session_state.current_video = "https://www.youtube.com/embed/Hy-cFpg2e30?autoplay=1&mute=1"
            st.rerun()
    with col2:
        if st.button("🦆 DUCK", use_container_width=True):
            st.session_state.current_video = "https://www.youtube.com/embed/raF08RDQrhI?autoplay=1&mute=1"
            st.rerun()
        if st.button("🐘 ELEPHANT", use_container_width=True):
            st.session_state.current_video = "https://www.youtube.com/embed/J8O9_ugpDjE?autoplay=1&mute=1"
            st.rerun()
    
    st.write("---")
    if st.button("🏠 BACK TO MASTER MENU", use_container_width=True):
        st.session_state.page = "main_menu"
        st.rerun()

# --- 5. SCREEN: EMBEDDED VIDEO PLAYER ---
elif st.session_state.current_video:
    st.title("Watch!")
    
    # This displays the video inside the app
    st.video(st.session_state.current_video)
    
    st.write("---")
    if st.button("⬅️ CHOOSE ANOTHER ANIMAL", use_container_width=True):
        st.session_state.current_video = None
        st.rerun()

# --- 6. SCREEN: COLOR GAME ---
elif st.session_state.page == "color_game":
    st.title("Color Game 🎨")
    st.write("Coming Soon!")
    if st.button("🏠 BACK", use_container_width=True):
        st.session_state.page = "main_menu"
        st.rerun()
