#Taille d'une chaine
#Exercice 8 : terre07.py

import sys

nb_ch=0
nb_arg=0

for arg in sys.argv:
    nb_arg=int(nb_arg)+1

if (int(nb_arg)==2):
    x=""
    ch = sys.argv[1]
    try:
        ch = int(ch)
        x=isinstance(ch, int)
        if (x==True):
            print("Erreur.")
    except:
        for car in ch :
            nb_ch = nb_ch+1
        print(nb_ch)
else :
    print("Erreur.")
