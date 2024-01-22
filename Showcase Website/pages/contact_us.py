import streamlit as st

st.header ("Contact Me")

with st.form(key="contact"):
    user_email = st.text_input(label="Your Email Address :", placeholder="Put Your email her")
    user_text = st.text_area(label="Your Message :", placeholder="Put your text her")
    button_submit = st.form_submit_button(label="Submit")
    if button_submit:
        print()
