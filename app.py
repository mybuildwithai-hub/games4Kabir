import streamlit as st
import time
import random
import os
import base64

# --- 1. SETTINGS & STYLING ---
st.set_page_config(page_title="Kabir Play Box", page_icon="🎮", layout="wide")

st.markdown("""
    <style>
    /* 1. Hide the audio bars to keep the screen clean */
    audio { display: none; }

    /* 2. Standardize button size for Kabir's fingers */
    .stButton>button { 
        border-radius: 20px; 
        height: 4em; 
        font-weight: bold; 
        font-size: 22px; 
        background-color: #f0f2f6;
        border: 2px solid #dfe1e5;
    }

    /* 3. Visual feedback ONLY when the button is actually pressed */
    .stButton>button:active { 
        background-color: #FFD700 !important; 
        color: black !important;
        border: 2px solid #FFA500;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE APP BRAIN ---
if 'page' not in st.session_state:
    st.session_state.page = "main_menu"
if 'current_item' not in st.session_state:
    st.session_state.current_item = None

# --- 3. HELPER FUNCTION: THE POP-UP ---
# This function handles the 15-second show for BOTH games
def show_surprise(file_path, sound_path):
    if os.path.exists(file_path) and os.path.exists(sound_path):
        # Prepare Image/GIF
        with open(file_path, "rb") as f:
            base64_img = base64.b64encode(f.read()).decode()
        
        # Prepare Sound
        with open(sound_path, "rb") as f:
            base64_sound = base64.b64encode(f.read()).decode()

        # Display Content
        st.markdown(f'''
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
                <img src="data:image/{"gif" if file_path.endswith("gif") else "jpeg"};base64,{base64_img}" 
                     style="width: 80%; max-height: 500px; object-fit: contain; border-radius: 30px; border: 10px solid #FFD700;">
                <audio autoplay loop><source src="data:audio/mp3;base64,{base64_sound}" type="audio/mp3"></audio>
            </div>
            ''', unsafe_allow_html=True)

        st.write("") 
        if st.button("⬅️ DONE / NEXT", use_container_width=True):
            st.session_state.current_item = None
            st.rerun()
            
        time.sleep(15)
        st.session_state.current_item = None
        st.rerun()
    else:
        st.error(f"Missing File! Check: {file_path}")
        if st.button("Back"):
            st.session_state.current_item = None
            st.rerun()

# --- 4. MASTER MENU ---
if st.session_state.page == "main_menu":
    st.title("Hi Kabir! Pick a Game 🌟")
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🦁 ANIMAL FRIENDS", use_container_width=True):
            st.session_state.page = "animal_game"
            st.rerun()
    with col_b:
        if st.button("✈️ TOY BOX SURPRISE", use_container_width=True):
            st.session_state.page = "toy_game"
            st.rerun()

# --- 5. GAME 1: ANIMAL FRIENDS ---
elif st.session_state.page == "animal_game":
    if st.session_state.current_item is None:
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
        for label, path, sound, col in animals:
            with col:
                if st.button(label, use_container_width=True):
                    st.session_state.current_item = [path, sound]
                    st.rerun()
        if st.button("🏠 MAIN MENU", use_container_width=True):
            st.session_state.page = "main_menu"
            st.rerun()
    else:
        show_surprise(st.session_state.current_item[0], st.session_state.current_item[1])

# --- 6. GAME 2: TOY BOX SURPRISE ---
elif st.session_state.page == "toy_game":
    if st.session_state.current_item is None:
        st.title("What's in the Box? 🎁")
        t_col1, t_col2 = st.columns(2)
        
        toys = [
            ("✈️ PLANE", "toys/plane.jpg", "sounds/plane.mp3", t_col1),
            ("🚗 CAR", "toys/car.jpg", "sounds/car.mp3", t_col1),
            ("🚂 TRAIN", "toys/train.jpg", "sounds/train.mp3", t_col2),
            ("⚽ BALL", "toys/ball.jpg", "sounds/bounce.mp3", t_col2)
        ]
        
        for label, path, sound, col in toys:
            with col:
                if st.button(label, use_container_width=True):
                    st.session_state.current_item = [path, sound]
                    st.rerun()
        if st.button("🏠 MAIN MENU", use_container_width=True):
            st.session_state.page = "main_menu"
            st.rerun()
    else:
        show_surprise(st.session_state.current_item[0], st.session_state.current_item[1])
