import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("The Best Company")
content1 = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
    It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. 
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
    and more recently with desktop publishing software like Aldus PageMaker 
    including versions of Lorem Ipsum.
"""
st.write(content1)

st.header("Our Team")

col3, empyt_col_1, col4, empty_col_2, col5 = st.columns([1.5,0.5,1.5,0.5,1.5])

team_df = pd.read_csv("data.csv", sep=",")

with col3:
    for index, row in team_df[:4].iterrows():
        st.header(row["first name"].title() + "" + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col4:
    for index, row in team_df[4:8].iterrows():
        st.header(row["first name"].title() + "" + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])
        

with col5:
    for index, row in team_df[8:].iterrows():
        st.header(row["first name"].title() + "" + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])
        
