import streamlit as st

st.set_page_config(page_title="Toddler Sounds", page_icon="🔊")

st.title("Touch the Animals! 🔊")

# Create three columns for more choices
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('🦁 Lion', use_container_width=True):
        st.write("ROAR!")
        # A link to a short lion roar sound
        st.audio("https://www.w3schools.com/html/horse.ogg") # Placeholder: Replace with Lion URL
        st.balloons()

with col2:
    if st.button('🐶 Dog', use_container_width=True):
        st.write("WOOF!")
        st.audio("https://www.soundjay.com/nature/dog-bark-1.mp3")
        st.snow()

with col3:
    if st.button('🐱 Cat', use_container_width=True):
        st.write("MEOW!")
        st.audio("https://www.soundjay.com/condition/sounds/cat-meow-1.mp3")
        st.toast("Meow!") # This pops up a tiny notification at the bottom
