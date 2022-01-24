#Racine carrée d'un nombre
#Exercice 10 : terre09.py

import sys

if (len(sys.argv)==2):
    try :
        nombre = int(sys.argv[1])
        if (int(nombre)<0):
            print("Erreur.")
        else:
            resultat = int(nombre)**(0.5) #équivalent à math.sqrt(int(nombre))
            print(resultat)
    except:
        print("Erreur.")
else :
    print("Erreur.")
