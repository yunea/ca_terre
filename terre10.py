#Nombre premier
#Exercice 11 : terre10.py

import sys

if (len(sys.argv)==2):
    try :
        nombre = int(sys.argv[1])
        if (nombre == 0 or nombre == 1):
            print("Non, "+str(nombre)+" n'est pas un nombre premier")
        else:
            i=2
            while (int(i)<int(nombre) and (int(nombre)%int(i))!=0):
                i = i+1
            if( i==nombre):
                print("Oui, "+str(nombre)+" est un nombre premier")
            else :
                print("Non, "+str(nombre)+" n'est pas un nombre premier")
    except:
        print("Erreur.")
else :
    print("Erreur.")
