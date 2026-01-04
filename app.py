import streamlit as st
import time
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
    st.session_state.balloon_order = [0, 1, 2]

def shuffle_balloons():
    random.shuffle(st.session_state.balloon_order)

# --- 3. SCREEN: MASTER MENU ---
# Every logic chain MUST start with an "if"
if st.session_state.page == "main_menu":
    st.title("Choose a Game! 👶")
    
    if st.button("🐾 TAP AN ANIMAL", use_container_width=True):
        st.session_state.page = "animal_game"
        st.rerun()
        
    if st.button("🎈 BALLOON POP GAME", use_container_width=True):
        st.session_state.page = "balloon_game"
        st.rerun()

# --- 4. SCREEN: ANIMAL SELECTION (The GIF + Sound Version) ---
elif st.session_state.page == "animal_game":
    # If we aren't showing a GIF right now, show the menu
    if st.session_state.current_video is None:
        st.title("Tap an Animal! 🦁")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🦁 LION", use_container_width=True):
                # Format: ["gif_filename", "audio_url"]
                st.session_state.current_video = ["lion.gif", "https://www.myinstants.com/media/sounds/lion_roar.mp3"]
                st.rerun()
            if st.button("🐶 DOG", use_container_width=True):
                st.session_state.current_video = ["dog.gif", "https://www.soundjay.com/nature/dog-bark-1.mp3"]
                st.rerun()
        with col2:
            if st.button("🦆 DUCK", use_container_width=True):
                st.session_state.current_video = ["duck.gif", "https://www.soundjay.com/nature/sounds/duck-quack-1.mp3"]
                st.rerun()
            if st.button("🐘 ELEPHANT", use_container_width=True):
                st.session_state.current_video = ["elephant.gif", "https://www.soundjay.com/nature/sounds/elephant-trumpets-1.mp3"]
                st.rerun()
        
        st.write("---")
        if st.button("🏠 BACK TO MASTER MENU", use_container_width=True):
            st.session_state.page = "main_menu"
            st.rerun()

    # THE POP-UP LOGIC: Shows when an animal is clicked
    else:
        gif_file, sound_url = st.session_state.current_video
        st.title("LOOK!")
        
        # Display the GIF (must be uploaded to GitHub)
        st.image(gif_file, use_container_width=True)
        # Play Sound
        st.audio(sound_url, autoplay=True)
        
        # Wait 5 seconds, then go back to the animal menu
        time.sleep(5)
        st.session_state.current_video = None
        st.rerun()

# --- 5. SCREEN: BALLOON POP GAME ---
elif st.session_state.page == "balloon_game":
    head_col1, head_col2 = st.columns([3, 1])
    with head_col1:
        st.title("Pop the Balloons! 🎈")
    with head_col2:
        st.metric("SCORE", st.session_state.score)

    game_cols = st.columns(3)
    
    # RED
    with game_cols[st.session_state.balloon_order[0]]:
        if st.button("🎈 RED", key="red", use_container_width=True):
            st.session_state.score += 1
            st.audio("https://ssl.gstatic.com/dictionary/static/sounds/oxford/red--_gb_1.mp3", autoplay=True)
            st.balloons()
            shuffle_balloons()
            st.rerun()

    # BLUE
    with game_cols[st.session_state.balloon_order[1]]:
        if st.button("🎈 BLUE", key="blue", use_container_width=True):
            st.session_state.score += 1
            st.audio("https://ssl.gstatic.com/dictionary/static/sounds/oxford/blue--_gb_1.mp3", autoplay=True)
            st.balloons()
            shuffle_balloons()
            st.rerun()

    # GREEN
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
