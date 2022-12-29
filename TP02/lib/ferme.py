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
        print("Mbéh, Mbéhhh")

    def __del__(self):
        print("L'ovin", self.nom, "est mort")

class caprin(Animal):
    def __init__(self, nom, age, poids):
        super().__init__(nom, age, poids)
        print("Le caprin s'appelle", self.nom, " il a", self.age, "ans", "et il pèse", self.poids, "kg")

    def crier(self):
        print("béh, béhhh")

    def __del__(self):
        print("Le caprin", self.nom, "est mort")

class porcin(Animal):
    def __init__(self, nom, age, poids):
        super().__init__(nom, age, poids)
        print("Le porcin s'appelle", self.nom, "et il a", self.age, "ans")

    def crier(self):
        print("groin-groin")

    def __del__(self):
        print("porcin", self.nom, "est mort")

class volaille(Animal):
    def __init__(self, nom, age, poids):
        super().__init__(nom, age, poids)
        print("La volaille s'appelle", self.nom, "et il a", self.age, "ans")

    def crier(self):
        print("cocorico")

    def __del__(self):
        print("La volaille", self.nom, "est mort")

class ferme:
    animaux = {
        bovin: {},
        ovin: {},
        caprin: {},
        porcin: {},
        volaille: {}
    }
    def __init__(self, animaux):
        self.animaux = animaux

# le code actuel ecrase la derniere valeur de l'animal.bovin pour enregistré la nouvelle valeur
    def ajouter_bovin(self, nom, age, poids):
        self.animaux.update({bovin:{ "nom": nom, "age": age, "poids": poids}})
        print("Le bovin", nom, "a été ajouté")
    def ajouter_ovin(self, nom, age, poids):
        #insert ne fonctionne pas
        self.animaux.insert(ovin, {"nom": nom, "age": age, "poids": poids})
        print("L'ovin", nom, "a été ajouté")

    #forme de base mais fonctionne de la meme maniere que ajouter_bovin
    def ajouter_caprin(self, nom, age, poids):
        self.animaux[caprin]["nom"] = nom
        self.animaux[caprin]["age"] = age
        self.animaux[caprin]["poids"] = poids
        print("Le caprin", nom, "a été ajouté")
    def ajouter_porcin(self, nom, age, poids):
        self.animaux[porcin]["nom"] = nom
        self.animaux[porcin]["age"] = age
        self.animaux[porcin]["poids"] = poids
        print("Le porcin", nom, "a été ajouté")
    def ajouter_volaille(self, nom, age, poids):
        self.animaux[volaille]["nom"] = nom
        self.animaux[volaille]["age"] = age
        self.animaux[volaille]["poids"] = poids
        print("La volaille", nom, "a été ajouté")

    def tuer_bovin(self, nom):
        del self.animaux[bovin][nom]
        print("Le bovin", nom, "a été tué")
    def tuer_ovin(self, nom):
        del self.animaux[ovin][nom]
        print("L'ovin", nom, "a été tué")
    def tuer_caprin(self, nom):
        del self.animaux[caprin][nom]
        print("Le caprin", nom, "a été tué")
    def tuer_porcin(self, nom):
        del self.animaux[porcin][nom]
        print("Le porcin", nom, "a été tué")
    def tuer_volaille(self, nom):
        del self.animaux[volaille][nom]
        print("La volaille", nom, "a été tué")

    def get_bovin(self, nom):
        return self.animaux[bovin][nom]
        

#     def tuer_animal(self, nom):
#         del self.animaux[nom]
#         print("L'animal", nom, "a été tué")

#     def get_animal(self, nom, age, poids):
#         return self.animaux[nom]+self.animaux[age]+self.animaux[poids]

#     # def crier(self):
#     #     for animal in self.animaux.values():
#     #         animal.crier()

#     # def __del__(self):
#     #     for animal in self.animaux.values():
#     #         del animal

    def afficher_ferme(self):
        if (self.animaux == { bovin: {},ovin: {},caprin: {},porcin: {},volaille: {}}):
            print("La ferme est vide")
            return 0
        else:
            print("La ferme contient les animaux suivants :")
            for animal in self.animaux.items():
                key=animal[0]
                value=animal[1]
                print(key, value)
            return 1