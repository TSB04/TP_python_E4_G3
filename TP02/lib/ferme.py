class ferme:
    def __init__(self):
        self.animaux = {}

    # def ajouter_animal(self, animal):
    #     self.animaux[animal] = animal
    #     print("L'animal", animal, "a été ajouté")

    def tuer_animal(self, nom):
        del self.animaux[nom]
        print("L'animal", nom, "a été tué")

    def get_animal(self, nom, age, poids):
        return self.animaux[nom]+self.animaux[age]+self.animaux[poids]

    def ajouter_bovin(nom, age, poids):
        return bovin(nom, age, poids)    

    # def ajouter_chien(nom, age):
    #     return chien(nom, age)

    # def ajouter_chat(nom, age):
    #     return chat(nom, age)

    # def crier(self):
    #     for animal in self.animaux.values():
    #         animal.crier()

    # def __del__(self):
    #     for animal in self.animaux.values():
    #         del animal

    def afficher_ferme(self):
        print("La ferme contient les animaux suivants :")
        for animal in ferme.animaux:
            print(animal)


class Animal ():
    def __init__(self, nom, age, poids):
        self.nom = nom
        self.age = age
        self.poids = poids



class bovin(Animal):
    def __init__(self, nom, age, poids):
        super().__init__(nom, age, poids)
        print("Le bovin s'appelle", self.nom, "il a", self.age, "ans", "et il pèse", self.poids, "kg")

    def crier(self):
        print("Mbeuhhhh")



class ovin(Animal):
    def __init__(self, nom, age, poids):
        super().__init__(nom, age, poids)
        print("L'ovin s'appelle", self.nom, " il a", self.age, "ans", "et il pèse", self.poids, "kg")

    def crier(self):
        print("béh, béhhh")

    def __del__(self):
        print("L'ovin", self.nom, "est mort")

class caprin(Animal):
    def __init__(self, nom, age, poids):
        super().__init__(nom, age, poids)
        print("Le caprin s'appelle", self.nom, " il a", self.age, "ans", "et il pèse", self.poids, "kg")

    def crier(self):
        print("Wouaf")

    def __del__(self):
        print("Le caprin", self.nom, "est mort")

class porcin(Animal):
    def __init__(self, nom, age, poids):
        super().__init__(nom, age, poids)
        print("Le chien s'appelle", self.nom, "et il a", self.age, "ans")

    def crier(self):
        print("groin-groin")

    def __del__(self):
        print("porcin", self.nom, "est mort")

class volaille(Animal):
    def __init__(self, nom, age, poids):
        super().__init__(nom, age, poids)
        print("La s'appelle", self.nom, "et il a", self.age, "ans")

    def crier(self):
        print("Wouaf")

    def __del__(self):
        print("Le chien", self.nom, "est mort")