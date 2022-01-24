#Trouver la Suisse (lol)
#Exercice 14 : terre13.py

import sys

if (len(sys.argv)==4):
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
        x=0
        if((a>b and a<c) or (a<b and a>c)):
            print(a)
        elif((b>a and b<c) or (b<a and b>c)):
            print(b)
        elif ((c>a and c<b) or (c<a and c>b)):
            print(c)
        else :
            print("Erreur.")
    except:
        print("Erreur.")
else :
    print("Erreur.")
    
