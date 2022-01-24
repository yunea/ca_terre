#Divisions
#Exercice 6 : terre05.py

import sys

quotient = sys.argv[1]
diviseur = sys.argv[2]

if (int(diviseur)==0):
    print("Erreur.")
elif (int(quotient)<int(diviseur)):
    print("Erreur.")
else :
    resultat = int(quotient) / int(diviseur)
    res = int(resultat)
    print("Résultat: "+str(res))
    reste = int(quotient) % int(diviseur)
    print("Reste: "+str(reste))
