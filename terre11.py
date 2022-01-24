#24 to 12
#Exercice 12 : terre11.py

import sys
from datetime import datetime

if (len(sys.argv)==2):
    heure_str=sys.argv[1]
    heure_obj = datetime.strptime(heure_str,"%H:%M")
    resultat = heure_obj.strftime("%I:%M%p")
    print(resultat)
else:
    print("Erreur.")
