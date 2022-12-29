from art import *  # pip install art before using this
from lib.ferme import ferme
def choix_animal():
    print_separator()
    print("1. Bovin")
    print("2. Caprin")
    print("3. Ovin")
    print("4. Porcin")
    print("5. Volaille")
    choix = input("Votre choix ? ")
    if choix == "1":
        return "Bovin"
    elif choix == "2":
        return "Caprin"
    elif choix == "3":
        return "Ovin"
    elif choix == "4":
        return "Porcin"
    elif choix == "5":
        return "Volaille"
    elif choix == "6":
        return print_menu()
    else:
        print("Choix invalide")
        return None


def print_separator():
    print("====================================")


def print_menu_asciiart():
    tprint("La ferme", font="random-small")


def print_menu():
    print_separator()
    print_menu_asciiart()
    print_separator()
    print("Menu")
    print("1. Ajouter un animal")
    print("2. Crier")
    print("3. Tuer un animal")
    print("4. Afficher la ferme")
    print("5. Quitter")


def ajouter_animal():
    choix = choix_animal()
    if choix == "Bovin":
        nom = input("Nom du bovin ? ")
        age = input("Age du bovin ? ")
        poids = input("Poids du bovin ? ")
        ferme.ajouter_bovin(ferme, nom, age, poids)
    elif choix == "Caprin":
        nom = input("Nom du caprin ? ")
        age = input("Age du caprin ? ")
        poids = input("Poids du caprin ? ")
        ferme.ajouter_caprin(ferme, nom, age, poids)
    elif choix == "Ovin":
        nom = input("Nom de l'ovin ? ")
        age = input("Age de l'ovin ? ")
        poids = input("Poids de l'ovin ? ")
        ferme.ajouter_ovin(ferme, nom, age, poids)
    elif choix == "Porcin":
        nom = input("Nom du porcin ? ")
        age = input("Age du porcin ? ")
        poids = input("Poids du porcin ? ")
        ferme.ajouter_porcin(ferme, nom, age, poids)
    elif choix == "Volaille":
        nom = input("Nom de la volaille ? ")
        age = input("Age de la volaille ? ")
        poids = input("Poids de la volaille ? ")
        ferme.ajouter_volaille(ferme, nom, age, poids)
    else:
        return 


def tuer_animal():
    nom = input("Nom de l'animal à tuer ? ")    
    for animal in ferme.animaux.values():
        if nom == animal:
            print("Animal trouvé")
        else:
            print("Cet animal n'existe pas")
            nom = input("Nom de l'animal à tuer ? ")
            continue

def ferme_vide():
    if ferme.afficher_ferme(ferme) == 0:
        return True
    return False
