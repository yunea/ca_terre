#Afficheur d'arguments
#Exercice 3 : terre02.py

import sys

for arg in sys.argv:
    if (arg == "terre02.py"):
        continue
    else :
        print (arg)
