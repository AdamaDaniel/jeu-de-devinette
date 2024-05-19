import tkinter as tk
from tkinter import messagebox
import random

# Fonction pour initialiser ou réinitialiser le jeu
def initialiser_jeu():
    global choix_de_nombre, nombre, chance
    choix_de_nombre = random.randint(0, 1000)
    nombre = 0
    chance = 5
    label_instruction.config(text="Vous avez cinq (5) chances pour tenter de deviner le nombre.\nLe nombre à deviner est " + ("pair." if choix_de_nombre % 2 == 0 else "impair."))
    label_resultat.config(text="")
    entry_nombre.delete(0, tk.END)

# Fonction pour gérer les tentatives de l'utilisateur
def deviner_nombre():
    global chance
    try:
        nombre = int(entry_nombre.get())
        if nombre < 0 or nombre > 1000:
            messagebox.showerror("Erreur", "Nombre invalide. Veuillez saisir un nombre compris entre 0 et 1000.")
            return

        if nombre < choix_de_nombre:
            label_resultat.config(text=f"Oups! Le nombre que vous avez saisi est inférieur. Il vous reste {chance - 1} tentatives.")
        elif nombre == choix_de_nombre:
            label_resultat.config(text=f"Bravo! Vous avez réussi en {5 - (chance - 1)} tentatives.",fg="green")
            return
        else:
            label_resultat.config(fg="red",text=f"Oups! Le nombre que vous avez saisi est supérieur. Il vous reste {chance - 1} tentatives.")
        
        chance -= 1
        
        if chance == 0 and nombre != choix_de_nombre:
            label_resultat.config(text=f"Vous avez utilisé toutes vos chances. Le nombre correct était {choix_de_nombre}. ", fg="green")
        
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

# Fonction pour gérer le clic sur le bouton "Recommencer"
def recommencer_jeu():
    initialiser_jeu()

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Jeu de devinette")
root.geometry("400x200")

label_instruction = tk.Label(root, text="Jeu de devinette")
label_instruction.pack()

label_resultat = tk.Label(root, text="")
label_resultat.pack()

entry_nombre = tk.Entry(root)
entry_nombre.pack()

bouton_deviner = tk.Button(root, text="Deviner", command=deviner_nombre)
bouton_deviner.pack()

bouton_recommencer = tk.Button(root, text="Recommencer", command=recommencer_jeu)
bouton_recommencer.pack()

# Initialiser le jeu pour la première fois
initialiser_jeu()

# Lancer la boucle principale de l'interface
root.mainloop()
