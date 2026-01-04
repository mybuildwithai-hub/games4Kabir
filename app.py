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
        
    if st.button("🎨 BALLOON GAME", use_container_width=True):
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
    
    # This displays the video inside the app
    st.video(st.session_state.current_video)
    
    st.write("---")
    if st.button("⬅️ CHOOSE ANOTHER ANIMAL", use_container_width=True):
        st.session_state.current_video = None
        st.rerun()

# --- 6. SCREEN: POP THE BALLOON ---
elif st.session_state.page == "balloon_game":
    st.title("Pop the Balloons! 🎈")
    st.subheader("Tap a color to hear it!")

    # Create 3 columns for big, colorful buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔴 RED", use_container_width=True):
            st.balloons()
            # Voice over: "Red"
            st.audio("https://ssl.gstatic.com/dictionary/static/sounds/oxford/red--_gb_1.mp3", autoplay=True)
            st.success("That is RED!")

    with col2:
        if st.button("🔵 BLUE", use_container_width=True):
            st.balloons()
            # Voice over: "Blue"
            st.audio("https://ssl.gstatic.com/dictionary/static/sounds/oxford/blue--_gb_1.mp3", autoplay=True)
            st.info("That is BLUE!")

    with col3:
        if st.button("🟢 GREEN", use_container_width=True):
            st.balloons()
            # Voice over: "Green"
            st.audio("https://ssl.gstatic.com/dictionary/static/sounds/oxford/green--_gb_1.mp3", autoplay=True)
            st.warning("That is GREEN!")

    st.write("---")
    
    # A special "Great Job" button
    if st.button("🥳 TAP FOR A SURPRISE", use_container_width=True):
        st.snow()
        # Voice over: "Great Job" (Using a generic cheering sound)
        st.audio("https://www.myinstants.com/media/sounds/kids_cheering.mp3", autoplay=True)
        st.balloons()

    if st.button("🏠 BACK TO MENU", use_container_width=True):
        st.session_state.page = "main_menu"
        st.rerun()
