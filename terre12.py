#12 to 24
#Exercice 13 : terre12.py

import sys
from datetime import datetime

if (len(sys.argv)==2):
    heure_str=sys.argv[1]
    heure_obj = datetime.strptime(heure_str,"%I:%M%p")
    resultat = heure_obj.strftime("%H:%M")
    print(resultat)
else:
    print("Erreur.")
