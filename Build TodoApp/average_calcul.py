'''
Il est possible d'avoir deux méthode pour importer des fonctions
from X import Y, Z, W...
Avec cette méthode on appel directement Y, Z et W

On a aussi une autre méthode
import X
Mais pour appeler Y, Z et W il faut ajouter X avant
X.Y X.Z X.W ect
'''
from functions import get_list_value, get_average
import functions

file_name = "./files/average.csv"

functions.check_file() #function declared with default argument so we dont need to pass it again

list_value = get_list_value("./files/average.csv") #In the function declaration we used default argument but we can also change it when we call the function if it's different
#print(list_value)

average_value = get_average(list_value)

#print(round(average_value))
print(round(average_value, 1)) #On va arrandir vers 1 valeur decimale