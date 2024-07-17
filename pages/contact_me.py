import streamlit as st
from send_email import send_email

st.header('Contact Me')


with st.container():
    with st.form(key='contact_form'):
        user_email = st.text_input('Your email address')
        user_message = st.text_area('Your Message')
        submit_button = st.form_submit_button('Submit')
        if submit_button:
            send_email(user_email, user_message)