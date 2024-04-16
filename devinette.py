# Jeu de devinette
#La commande randint(a,b) permet d'obtenir un entier aléatoire dans l'intervalle [a ; b]
#importer random
from numpy import random
x = random.randint(0,1000)
n=0
while x!=n:
    #demander a l'utilisateur d'entrer un nombre
    n=int(input("Devinez un nombre:"))
    if n<x:
        print('le nombre que vous avez saisie est inferieur')
    elif n==x:
       print('Bravo vous avez reuissi')
    else:
        print('le nombre est superieur.')
