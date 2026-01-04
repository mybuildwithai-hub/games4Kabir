import streamlit as st
import time

st.set_page_config(page_title="Toddler Fun", page_icon="🐾")

# 1. Initialize "Memory": If this is the first time opening the app, 
# tell Python we aren't showing a big animal yet.
if 'showing_animal' not in st.session_state:
    st.session_state.showing_animal = None

# 2. SCREEN A: Show the Big Animal
if st.session_state.showing_animal:
    animal = st.session_state.showing_animal
    
    st.title(f"LOOK! A {animal['name'].upper()}!")
    
    # Show the big image
    st.image(animal['image_url'], use_container_width=True)
    
    # Play the sound
    st.audio(animal['sound_url'], autoplay=True)
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Clear the memory and refresh to go back to the main menu
    st.session_state.showing_animal = None
    st.rerun()

# 3. SCREEN B: The Main Menu (The grid of animals)
else:
    st.title("Tap an animal! 🐾")
    
    col1, col2 = st.columns(2)

    with col1:
        # We store the animal data in a "Dictionary" (a Python list of labels)
        lion_data = {
            "name": "Lion",
            "image_url": "https://img.freepik.com/free-vector/cute-lion-cartoon-vector-icon-illustration-animal-nature-icon-concept-isolated-flat-vector_138676-1335.jpg",
            "sound_url": "https://www.w3schools.com/html/horse.ogg" # Swap with real Lion MP3 later!
        }
        if st.button('🦁 Tap the Lion', use_container_width=True):
            st.session_state.showing_animal = lion_data
            st.rerun()

    with col2:
        dog_data = {
            "name": "Dog",
            "image_url": "https://img.freepik.com/free-vector/cute-dog-sitting-cartoon-vector-icon-illustration-animal-nature-icon-concept-isolated-flat-vector_138676-1336.jpg",
            "sound_url": "https://www.soundjay.com/nature/dog-bark-1.mp3"
        }
        if st.button('🐶 Tap the Dog', use_container_width=True):
            st.session_state.showing_animal = dog_data
            st.rerun()
