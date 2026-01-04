import streamlit as st
import time
import random
import os
import base64

# --- 1. SETTINGS ---
st.set_page_config(page_title="Kabir Play Box", page_icon="🎮", layout="wide")

# This CSS hides the audio player globally so the screen stays clean
st.markdown("<style>audio {display: none;}</style>", unsafe_allow_html=True)

# --- 2. THE APP BRAIN ---
if 'current_animal' not in st.session_state:
    st.session_state.current_animal = None

# --- 3. MAIN SCREEN: ANIMAL SELECTION ---
if st.session_state.current_animal is None:
    st.title("Tap an Animal! 🦁")
    
    # Grid layout for 8 animals
    col1, col2, col3, col4 = st.columns(4)
    
    # List of animals: (Label, GIF Path, Sound Path, Column)
    animals = [
        ("🦁 LION", "animations/lion.gif", "sounds/lion.mp3", col1),
        ("🐶 DOG", "animations/dog.gif", "sounds/dog.mp3", col1),
        ("🦆 DUCK", "animations/duck.gif", "sounds/duck.mp3", col2),
        ("🐘 ELEPHANT", "animations/elephant.gif", "sounds/elephant.mp3", col2),
        ("🐱 CAT", "animations/cat.gif", "sounds/cat.mp3", col3),
        ("🐮 COW", "animations/cow.gif", "sounds/cow.mp3", col3),
        ("🐒 MONKEY", "animations/monkey.gif", "sounds/monkey.mp3", col4),
        ("🐑 SHEEP", "animations/sheep.gif", "sounds/sheep.mp3", col4)
    ]

    for label, gif, sound, col in animals:
        with col:
            if st.button(label, use_container_width=True):
                st.session_state.current_animal = [gif, sound]
                st.rerun()

# --- 4. POP-UP SCREEN: GIF + SOUND ---
else:
    gif_path, sound_path = st.session_state.current_animal
    
    # Double check files exist to prevent the app from crashing
    if os.path.exists(gif_path) and os.path.exists(sound_path):
                
        # Prepare the GIF
        with open(gif_path, "rb") as f:
            gif_bytes = f.read()
            base64_gif = base64.b64encode(gif_bytes).decode()
        
        # Prepare the Sound
        with open(sound_path, "rb") as f:
            sound_bytes = f.read()

        # Display the GIF (Centered for iPad)
        st.markdown(
            f'''
            <div style="display: flex; justify-content: center;">
                <img src="data:image/gif;base64,{base64_gif}" 
                     style="width: 85%; max-height: 550px; object-fit: contain; border-radius: 20px; border: 8px solid #FFD700;">
            </div>
            ''',
            unsafe_allow_html=True
        )
        
        # Play the Sound
        st.audio(sound_bytes, format="audio/mpeg", autoplay=True)
        
        # Wait 5 seconds so the toddler can enjoy the animation
        time.sleep(5)
        
        # Reset and go back to menu
        st.session_state.current_animal = None
        st.rerun()
    else:
        # Error handling if a file is missing in GitHub
        st.error(f"Missing File! Check if these are in your folders: {gif_path} or {sound_path}")
        if st.button("⬅️ Back to Menu"):
            st.session_state.current_animal = None
            st.rerun()
