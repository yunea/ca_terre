#Inverser une chaine
#Exercice 7 : terre06.py

import sys

ch = sys.argv[1]

l = len(ch)
i=int(l)-1
res=""

while (i>=0):
    res=res+str(ch[i])
    i=i-1
print(str(res))
