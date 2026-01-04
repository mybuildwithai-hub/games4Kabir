import streamlit as st
import time
import random
import os
import base64

# --- 1. SETTINGS ---
st.set_page_config(page_title="Kabir Play Box", page_icon="🎮", layout="wide")

# CSS to hide the standard audio player and style the "Finish" button
st.markdown("""
    <style>
    audio { display: none; }
    .stButton>button { border-radius: 20px; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE APP BRAIN ---
if 'current_animal' not in st.session_state:
    st.session_state.current_animal = None

# --- 3. MAIN SCREEN: ANIMAL SELECTION ---
if st.session_state.current_animal is None:
    st.title("Tap an Animal! 🦁")
    
    col1, col2, col3, col4 = st.columns(4)
    
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

# --- 4. POP-UP SCREEN: GIF + LOOPING SOUND ---
else:
    gif_path, sound_path = st.session_state.current_animal
    
    if os.path.exists(gif_path) and os.path.exists(sound_path):
        # 1. Prepare GIF
        with open(gif_path, "rb") as f:
            gif_bytes = f.read()
            base64_gif = base64.b64encode(gif_bytes).decode()
        
        # 2. Prepare Sound
        with open(sound_path, "rb") as f:
            sound_bytes = f.read()
            base64_sound = base64.b64encode(sound_bytes).decode()

        # 3. Show GIF
        st.markdown(
            f'''
            <div style="display: flex; justify-content: center;">
                <img src="data:image/gif;base64,{base64_gif}" 
                     style="width: 85%; max-height: 500px; object-fit: contain; border-radius: 20px; border: 8px solid #FFD700;">
            </div>
            ''',
            unsafe_allow_html=True
        )
        
        # 4. Loop Sound using HTML (Better for iPad/iPhone)
        st.markdown(
            f'''
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{base64_sound}" type="audio/mp3">
            </audio>
            ''',
            unsafe_allow_html=True
        )

        st.write("") # Spacer
        
        # 5. The Skip/Finish Button
        # This allows you to go back before the 15 seconds are up
        if st.button("⬅️ DONE / NEXT ANIMAL", use_container_width=True):
            st.session_state.current_animal = None
            st.rerun()
            
        # 6. The 15 Second Timer
        time.sleep(15)
        
        # Auto-reset after timer finishes
        st.session_state.current_animal = None
        st.rerun()

    else:
        st.error(f"Missing File! Check: {gif_path} or {sound_path}")
        if st.button("⬅️ Back to Menu"):
            st.session_state.current_animal = None
            st.rerun()
