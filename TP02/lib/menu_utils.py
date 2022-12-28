from art import *  # pip install art before using this
from lib.ferme import bovin, ferme, Animal

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
        ferme.ajouter_bovin(nom, age, poids)
    # elif choix == "chat":
    #     nom = input("Nom du chat ? ")
    #     age = input("Age du chat ? ")
    #     ferme.ajouter_animal(ferme.ajouter_chat(nom, age))
    else:
        return 


def tuer_animal(nom):
    if nom == "q":
        return
    try:
        ferme.tuer_animal(nom)
    except KeyError:
        print("Cet animal n'existe pas")


def ferme_vide():
    if ferme.animaux == {}:
        print_separator()
        print("La ferme est vide")
        return True
    return False
