from lib.ferme import ferme
from lib.menu_utils import *

while True:
    print_menu()
    choix = input("Votre choix ? ")
    if choix == "1":
        ajouter_animal()
    elif choix == "2":
        ferme.crier()
    elif choix == "3":
        if ferme_vide():
            continue
        print_separator()
        nom = input("Nom de l'animal à tuer ? ")
        while nom not in ferme.animaux and nom != "q":
            print("Cet animal n'existe pas")
            nom = input("Nom de l'animal à tuer ? ")
        tuer_animal(nom)
    elif choix == "4":
        ferme.afficher_ferme(ferme)
    elif choix == "5":
        break
    else:
        print("Choix invalide")
