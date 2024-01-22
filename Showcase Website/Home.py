import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

#Create two column
col1, col2 = st.columns(2) 

#Create content inside the first column
with col1:
    st.image("images/photo.png", width=300)
#Create content inside the second column
with col2:
    st.title("Badr LAAJALI")
    content = """
    Badr Laajali vous apporte des astuces et des outils pratiques en IA et productivité pour enrichir votre parcours d'apprentissage. Cliquez pour en savoir plus ➡️ 
Actif sur YouTube depuis 2023, ma passion pour l'intelligence artificielle et le machine learning anime chaque vidéo. Mon expertise en analyse d'affaires et fonctionnelle, la collecte de besoins, ainsi que la modélisation de flux et processus enrichissent mes projets, que je partage sur www.digitgrow.com pour aider les petites entreprises à se digitaliser et s'automatiser. 
Sur ma chaîne, découvrez mes aventures dans l'IA, avec des conseils pratiques pour ceux souhaitant intégrer ces technologies dans leur vie professionnelle. 
Bon visionnage et bienvenue dans notre cercle des passionnés d'IA et de productivité !
    """
    st.info(content)

st.text("Below you can find some of the apps I have built in Python. Feel free to contact me!")

#We can pass to column a list with the dimension of the column
col3, compty_col, col4 = st.columns([1.5,0.5,1.5])

#Read the CSV file as a dataframe with panda and give the separation used inside the csv (;)
projects_data = pd.read_csv("data.csv", sep=";")

with col3:
    #We use iterrows to get access to the rows inside the dataframe
    for index, row in projects_data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        #We can use simple concatenatin (see col4) or use f to add variable with text
        st.write(f"[Source Code]({row['url']})")

with col4:
    #We use iterrows to get access to the rows inside the dataframe
    for index, row in projects_data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](" + row["url"] + ")")
