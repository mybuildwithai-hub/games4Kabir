import streamlit as st
import time

# --- 4 & 5. COMBINED SCREEN: ANIMAL SELECTION WITH GIF POP-UP ---
elif st.session_state.page == "animal_game":
    st.title("Tap an Animal! 🦁")
    
    # This creates a "placeholder" that we can fill with a GIF later
    placeholder = st.empty()

    # If no animal is being "watched" right now, show the menu
    if st.session_state.current_video is None:
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🦁 LION", use_container_width=True):
                # We store a list: [GIF_FILENAME, SOUND_URL]
                st.session_state.current_video = ["lion.gif", "https://www.w3schools.com/html/horse.ogg"] 
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

    # --- THE MAGIC POP-UP LOGIC ---
    else:
        gif_file, sound_url = st.session_state.current_video
        
        with placeholder.container():
            st.markdown("### LOOK!")
            # 1. Show the GIF
            st.image(gif_file, use_container_width=True)
            # 2. Play the Sound
            st.audio(sound_url, autoplay=True)
            
            # 3. Wait for 5 seconds
            time.sleep(5)
            
            # 4. Clear the state and refresh
            st.session_state.current_video = None
            st.rerun()
