import functions, datetime, os
import PySimpleGUI as sg

# Obtenir le répertoire actuel du fichier de code
current_directory = os.path.dirname(os.path.abspath(__file__))
# Concaténer le nom du fichier pour obtenir le chemin complet
file_name = os.path.join(current_directory, "todos.csv")

functions.check_file(file_name)
# Obtenir la date et l'heure actuelles
now = datetime.datetime.now() # 2023-12-23 22:09:52.633851
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

sg.theme("DarkTeal12")

layout = [
    [sg.Text(formatted_date_time)],
    [sg.Text("Type your todo :")], 
    [sg.InputText(tooltip="Type your text here", key='-user_todo-'), 
     sg.Button("Add")],
    [sg.Listbox(values=functions.get_todo(file_name), key='-list_todos-',
                enable_events=True, size=[45,10]), sg.Button("Edit")],
    [sg.Button("Complete"), sg.Button("Exit")]
]

window = sg.Window('My To-Do App', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Add":
        functions.add_todo(values['-user_todo-'], file_name)
        todos_list = functions.get_todo(file_name) 
        window["-user_todo-"].update("")
        window['-list_todos-'].update(values=todos_list)
    elif event == "Edit":
        try:
            todo_to_edit = values['-list_todos-'][0]
            new_todo = values['-user_todo-']
            #Get the list of all the todos, we need it to find the index of the todo that we need to edit
            todos_list = functions.get_todo(file_name) 
            #Get the index of the value inside the list
            index = todos_list.index(todo_to_edit) 
            functions.edit_todo(file_name, index, new_todo)
            todos_list[index] = new_todo
            window['-list_todos-'].update(values=todos_list)
        except IndexError:
            sg.popup("Please select an item first")
    elif event == "-list_todos-":
        window["-user_todo-"].update(value=values['-list_todos-'][0])
    elif event == "Complete":
        try:
            todo_to_complete = values['-list_todos-'][0]
            todos_list = functions.get_todo(file_name) 
            index = todos_list.index(todo_to_complete) 
            functions.complete_todo(file_name, index)
            del todos_list[index]
            window['-list_todos-'].update(values=todos_list)
            window["-user_todo-"].update("")
        except IndexError:
            sg.popup("Please select an item first")
    elif event == "Exit":
        break

window.close()