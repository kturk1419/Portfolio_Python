import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with st.container():
    with col1:
        st.image("images/photo.png")

    with col2:
        st.title("Khaled Turkestani")
        content = """
        Hi, I am Khaled! I am a Software Developer graduated from King Fahd University of Petroleum and Minerals. This website is didecated to show my projects developed using Python.
    I am currently working in King Fahd University of Petroleum and Minerals as a Developer, and a Banner AR Consultant.
        """
        st.info(content)

with st.container():
    st.text("<b>Below you can find some of the apps i have built using Python. Feel free to contact me anytime.</b>")
