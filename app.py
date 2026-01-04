import streamlit as st

# 1. Setup the Page Title and Icon
st.set_page_config(page_title="Toddler Fun", page_icon="👶")

# 2. The Header
st.title("Tap an Animal! 🐾")
st.write("A simple game for my little one.")

# 3. Create a layout with 2 columns
col1, col2 = st.columns(2)

# 4. Logic for the first animal (Cow)
with col1:
    if st.button('🐮 MOO', use_container_width=True):
        st.balloons() # This makes balloons fly up the screen!
        st.success("THE COW SAYS MOOOO!")
        # Tip: Later, we can add st.audio() here for real sounds

# 5. Logic for the second animal (Duck)
with col2:
    if st.button('🦆 QUACK', use_container_width=True):
        st.snow() # This makes snowflakes fall!
        st.info("THE DUCK SAYS QUACK!")
