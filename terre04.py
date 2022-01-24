#Pair ou impair
#Exercice 5 : terre04.py

import sys

nb = 0
for arg in sys.argv:
    if (arg == 'terre04.py'):
        continue
    else:
        try :
            nb = int(arg)
            x=isinstance(nb, int)

            if (x==True):
                mod = int(nb) % 2
                if (mod==0):
                    print("pair")

                else:
                    print("impair")
            else:
                print("Tu ne me la mettras pas à l'envers.")
        except:
            print("Tu ne me la mettras pas à l'envers.")
