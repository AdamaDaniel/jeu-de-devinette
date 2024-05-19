# Jeu de devinette
#La commande randint(a,b) permet d'obtenir un entier aléatoire dans l'intervalle [a ; b]
import random

choix_de_nombre = random.randint(0, 1000)
nombre = 0
chance = 5
print("Jeu de devinette")
print("Vous avez cinq (5) chances pour tenter de deviner le nombre")

#Preciser si le nombre a choisir est pair ou impair.
if choix_de_nombre % 2 == 0:
    print("Le nombre à deviner est un nombre pair.")
else:
    print("Le nombre à deviner est un nombre impair.")


while choix_de_nombre != nombre and chance > 0:
    try:
        # demander à l'utilisateur d'entrer un nombre
        nombre = int(input("Devinez un nombre: "))
        
        if nombre < 0 or nombre > 1000:
            print("Nombre invalide. Veuillez saisir un nombre compris entre 0 et 1000.")
            continue
        
        if nombre < choix_de_nombre:
            print(f"Oups! Le nombre que vous avez saisi est inférieur. Il vous reste {chance - 1} tentatives.")
        elif nombre == choix_de_nombre:
            print(f"Bravo! Vous avez réussi en {5 - (chance - 1)} tentatives.")
        else:
            print(f"Oups! Le nombre que vous avez saisi est supérieur. Il vous reste {chance - 1} tentatives.")
        
        # décrémenter chance à chaque tentative échouée
        chance -= 1
    
    except ValueError:
        print("Veuillez entrer un nombre valide.")

# Afficher le nombre correct lorsque toutes les tentatives sont épuisées
if choix_de_nombre != nombre:
    print(f"Vous avez utilisé toutes vos chances. Le nombre correct était {choix_de_nombre}.")

