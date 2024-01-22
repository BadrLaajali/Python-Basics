import streamlit as st
import pandas as pd

user_topics_df = pd.read_csv("topics.csv")

with st.form(key="submit"):
    user_email = st.text_input(label="Your Email Address :")  
    user_list = st.selectbox(label="What topic you want to discuss ?", options=user_topics_df)
    user_text = st.text_area(label="Text :")
    button_submit = st.form_submit_button(label="Submit")

