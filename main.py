import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])


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

with st.container():
    df = pd.read_csv("data.csv", sep=";")
    with col3:
        for i, row in df[:10].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Cooming Soon]({row['url']})")

    with empty_col:
        st.empty()

    with col4:
        for i, row in df[10:].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Cooming Soon]{row['url']}")