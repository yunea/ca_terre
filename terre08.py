#Puissance d'un nombre
#Exercice 9 : terre08.py

import sys

if (len(sys.argv)==3):
    try :
        nombre = int(sys.argv[1])
        exposant = int(sys.argv[2])
        if (exposant<0):
            print("L'exposant ne peut pas être négatif")
        else:
            resultat = int(nombre) ** int(exposant)
            print(resultat)
    except:
        print("Erreur.")
else :
    print("Erreur.")
