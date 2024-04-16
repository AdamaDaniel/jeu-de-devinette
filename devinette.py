# Jeu de devinette
#La commande randint(a,b) permet d'obtenir un entier aléatoire dans l'intervalle [a ; b]
from numpy import random
x = random.randint(0,1000)
n=0
while x!=n:
    n=int(input("Devinez un nombre:"))
    if n<x:
        print('le nombre que vous avez saisi est inferieur')
    elif n==x:
       print('Bravo')
    else:
        print('le nombre est superieur')