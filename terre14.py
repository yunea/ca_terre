#Trié ou pas
#Exercice 15 : terre14.py

import sys


b=False
try:
    x=int(sys.argv[1])
    for arg in sys.argv :

        if (arg == 'terre14.py'):
            continue
        else:
            arg = int(arg)
            if (x<=arg):
                x=arg
                b=True
            else:
                b=False
                break
    if(b):
        print("Triée !")
    else:
        print("Pas triée !")

except:
    print("Erreur.")
