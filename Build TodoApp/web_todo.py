import streamlit as st
import functions, datetime, os

st.title("My Todo Web-App")
st.subheader("This is my todo app")
st.write("This app is to increase productivity")



#Initialise variables and file
# Obtenir le répertoire actuel du fichier de code
current_directory = os.path.dirname(os.path.abspath(__file__))
# Concaténer le nom du fichier pour obtenir le chemin complet
file_name = os.path.join(current_directory, "todos.csv")

functions.check_file(file_name)

# Obtenir la date et l'heure actuelles
now = datetime.datetime.now() # 2023-12-23 22:09:52.633851
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

#Function called with event
def add_todo():
    new_todo = st.session_state["new_todo"] #Get the value from the key new_todo stored inside the session
    functions.add_todo(new_todo, file_name)
    st.session_state["new_todo"] = ""

def todo_complete():
    print('')
    #

#Build the interace
todos_list = functions.get_todo(file_name) 
for index, todo in enumerate(todos_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        functions.complete_todo(file_name, index)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

st.write(st.session_state)