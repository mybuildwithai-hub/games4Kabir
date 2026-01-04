import streamlit as st
import random

# --- 1. SETTINGS ---
st.set_page_config(page_title="Toddler Play Box", page_icon="🎮", layout="wide")

# --- 2. THE APP BRAIN (Session State) ---
if 'page' not in st.session_state:
    st.session_state.page = "main_menu"
if 'current_video' not in st.session_state:
    st.session_state.current_video = None
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'balloon_order' not in st.session_state:
    # This keeps track of which column each balloon is in
    st.session_state.balloon_order = [0, 1, 2]

# Logic to shuffle balloons
def shuffle_balloons():
    random.shuffle(st.session_state.balloon_order)

# --- 3. SCREEN: MASTER MENU ---
if st.session_state.page == "main_menu":
    st.title("Choose a Game! 👶")
    
    if st.button("🐾 TAP AN ANIMAL", use_container_width=True):
        st.session_state.page = "animal_game"
        st.rerun()
        
    if st.button("🎈 BALLOON POP GAME", use_container_width=True):
        st.session_state.page = "balloon_game"
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
    st.video(st.session_state.current_video)
    if st.button("⬅️ CHOOSE ANOTHER ANIMAL", use_container_width=True):
        st.session_state.current_video = None
        st.rerun()

# --- 6. SCREEN: POP THE BALLOON (Updated Game Logic) ---
elif st.session_state.page == "balloon_game":
    # Top header with Score
    head_col1, head_col2 = st.columns([3, 1])
    with head_col1:
        st.title("Pop the Balloons! 🎈")
    with head_col2:
        st.metric("SCORE", st.session_state.score)

    # Create 3 columns for the game area
    game_cols = st.columns(3)

    # We use the balloon_order list to decide which balloon goes in which column
    
    # RED BALLOON
    with game_cols[st.session_state.balloon_order[0]]:
        if st.button("🎈 RED", key="red", use_container_width=True):
            st.session_state.score += 1
            st.audio("https://ssl.gstatic.com/dictionary/static/sounds/oxford/red--_gb_1.mp3", autoplay=True)
            st.balloons()
            shuffle_balloons()
            st.rerun()

    # BLUE BALLOON
    with game_cols[st.session_state.balloon_order[1]]:
        if st.button("🎈 BLUE", key="blue", use_container_width=True):
            st.session_state.score += 1
            st.audio("https://ssl.gstatic.com/dictionary/static/sounds/oxford/blue--_gb_1.mp3", autoplay=True)
            st.balloons()
            shuffle_balloons()
            st.rerun()

    # GREEN BALLOON
    with game_cols[st.session_state.balloon_order[2]]:
        if st.button("🎈 GREEN", key="green", use_container_width=True):
            st.session_state.score += 1
            st.audio("https://ssl.gstatic.com/dictionary/static/sounds/oxford/green--_gb_1.mp3", autoplay=True)
            st.balloons()
            shuffle_balloons()
            st.rerun()

    st.write("---")
    if st.button("🏠 BACK TO MENU", use_container_width=True):
        st.session_state.page = "main_menu"
        st.rerun()
