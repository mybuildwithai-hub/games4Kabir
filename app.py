import streamlit as st

# --- 1. SETTINGS ---
st.set_page_config(page_title="Toddler Play Box", page_icon="🎮", layout="centered")

# --- 2. THE APP "BRAIN" (Navigation Logic) ---
# We use 'page' to remember which game we are currently playing
if 'page' not in st.session_state:
    st.session_state.page = "main_menu"

# --- 3. PAGE: MASTER MENU ---
if st.session_state.page == "main_menu":
    st.title("Choose a Game! 👶")
    
    # Large buttons for the master menu
    if st.button("🐾 TAP AN ANIMAL", use_container_width=True):
        st.session_state.page = "animal_game"
        st.rerun()
        
    if st.button("🎨 COLOR LEARNING", use_container_width=True):
        st.session_state.page = "color_game"
        st.rerun()
        
    if st.button("🎈 POP THE BALLOON", use_container_width=True):
        st.session_state.page = "balloon_game"
        st.rerun()

# --- 4. PAGE: ANIMAL GAME ---
elif st.session_state.page == "animal_game":
    st.title("Animal Sounds 🦁")
    
    col1, col2 = st.columns(2)
    with col1:
        # Using the Link Button approach for better iPad playback
        st.link_button("🦁 LION", "https://www.youtube.com/embed/zgxUh6RYo7Y?autoplay=1&mute=1", use_container_width=True)
        st.link_button("🐶 DOG", "https://www.youtube.com/embed/Hy-cFpg2e30?autoplay=1&mute=1", use_container_width=True)
    with col2:
        st.link_button("🦆 DUCK", "https://www.youtube.com/embed/raF08RDQrhI?autoplay=1&mute=1", use_container_width=True)
        st.link_button("🐘 ELEPHANT", "https://www.youtube.com/embed/J8O9_ugpDjE?autoplay=1&mute=1", use_container_width=True)
    
    st.write("---")
    if st.button("🏠 BACK TO MENU", use_container_width=True):
        st.session_state.page = "main_menu"
        st.rerun()

# --- 5. PAGE: COLOR GAME (Placeholder) ---
elif st.session_state.page == "color_game":
    st.title("What Color is This? 🎨")
    st.info("We will build the color logic here next!")
    if st.button("🏠 BACK TO MENU", use_container_width=True):
        st.session_state.page = "main_menu"
        st.rerun()

# --- 6. PAGE: BALLOON GAME (Placeholder) ---
elif st.session_state.page == "balloon_game":
    st.title("Pop the Balloon! 🎈")
    if st.button("🎈 CLICK TO POP!", use_container_width=True):
        st.balloons()
    if st.button("🏠 BACK TO MENU", use_container_width=True):
        st.session_state.page = "main_menu"
        st.rerun()
