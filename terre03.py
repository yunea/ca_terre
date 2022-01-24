#L'alphabet à partir de
#Exercice 4 : terre03.py

import sys

alphabet_list=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lettre=''
for arg in sys.argv:
    if (arg == 'terre03.py'):
        continue
    else:
        lettre = arg

i=0
resultat=""
for l in alphabet_list :
    #print('i :'+ str(i))
    #print(alphabet_list[i])
    if (l == lettre):
        resultat=str(resultat)+str(l)
        if ((i+1)<len(alphabet_list)):
            lettre=alphabet_list[i+1]
    i=i+1
print(str(resultat))
