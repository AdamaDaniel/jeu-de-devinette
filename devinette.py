# Jeu de devinette
#La commande randint(a,b) permet d'obtenir un entier aléatoire dans l'intervalle [a ; b]
#importer random
from numpy import random
x = random.randint(0,1000)
n=0
chance=5
print("Jeu de devinette")
print("Vous avez cinq (5) chances pour tenter de deviner le nombre")
while x!=n and chance!=0:
    #demander a l'utilisateur d'entrer un nombre
    n=int(input("Devinez un nombre:"))
    if n<x:
        print(f"le nombre que vous avez saisie est inferieur il vous reste {chance-1} tentatives")
    elif n==x:
       print('Bravo vous avez reuissi, a seulement ')
    else:
        print(f"le nombre est superieur  il vous reste {chance-1} tentatives.")

        break
    # decrementer chance a chaque tentative echoué
    chance -= 1
# Afficher le nombre toutes les tentatives sont voué a l'echec
if chance == 0:
    print(f"Vous avez utilisé toutes vos chances. Le nombre correct était {x}.")
