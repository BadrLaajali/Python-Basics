import csv, os


def check_file(file_name):
    """Vérifiez si le fichier CSV existe, sinon créez-le""" #Voici comment déclarer un doc-string(help) pour une fonction
    if not os.path.exists(file_name):
        with open(file_name, mode="w", newline="") as file:
            pass


def get_list_value(file_name):
    list_value = []
    try:
        with open(file_name, mode="r") as file: 
            reader = csv.reader(file)
            next(reader) #Sauter la premiere ligne du fichier csv
            for row in reader:
                if row and row[0] not in list_value: #Vérifier si pas de ligne vide ET pas de doublons
                    try:
                        list_value.append(float(row[0])) #Convertir la valeur dans le fichier texte vers un float
                    except ValueError:
                        print(f"Ignoré : '{row[0]}' n'est pas convertible en float.")
                        continue
    except StopIteration:
        print("Votre fichier est vide")
    return list_value


def get_average(list_value):
    try:
        average = 0
        sum_value = sum(list_value)
        average = sum_value / len(list_value) #Average = Total / sur le nombre
    except ZeroDivisionError:
        print ("Division par Zero n'est pas autoriser")
    return average


def add_todo(user_action, file_name):
    todo = user_action.strip() 
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([todo])


def get_todo(file_name):
    todos = [] 
    with open(file_name, mode="r") as file: 
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] not in todos:  
                todos.append(row[0])
    # A Améliorer pour retourner une liste avec un numéro avant chaque ligne
    '''
    for index, item in enumerate(todos, start=1): 
        item = item.title() 
        message = f"{index}- {item.capitalize()}" 
    '''
    return todos


def edit_todo(file_name, index, new_todo):
    todos = []
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0]: 
                todos.append(row[0])
    todos[index] = new_todo 
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        for task in todos:
            writer.writerow([task])


def complete_todo(file_name, index):
    todo_founded = False 
    todos = []
    todo_deleted = []
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i != index:  
                todos.append(row[0]) 
            else:
                todo_deleted.append(row[0])
                todo_founded = True
    if todo_founded:
        # Réécrivez tout le contenu de la liste dans le fichier CSV
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            for task in todos:
                writer.writerow([task])
        print("You completed this todo", todo_deleted[0].title())
    else:
        print("This todo does not exist")
