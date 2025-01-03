class Vehicule:
    def __init__(self, marque):
        self.marque = marque

    def rouler(self):
        print(f"Le véhicule de marque {self.marque} roule.")

class Voiture(Vehicule):
    def __init__(self, marque, nombre_de_portes):
        super().__init__(marque)
        self.nombre_de_portes = nombre_de_portes

voiture = Voiture("Toyota", 4)
voiture.rouler()
print(f"Marque : {voiture.marque}, Nombre de portes : {voiture.nombre_de_portes}")



class Animal:
    def parler(self):
        return "L'animal fait un bruit."

class Oiseau(Animal):
    def parler(self):
        return "L'oiseau chante."

class Poisson(Animal):
    def parler(self):
        return "Le poisson ne fait pas de bruit."

animaux = [Animal(), Oiseau(), Poisson()]
for animal in animaux:
    print(animal.parler())


class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

class Triangle:
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def calculer_surface(self):
        return 0.5 * self.base * self.hauteur

formes = [
    Rectangle(5, 10),
    Triangle(6, 8),
    Rectangle(7, 3)
]

for forme in formes:
    print(f"Surface : {forme.calculer_surface()}")


from abc import ABC, abstractmethod

class Employe(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def calculer_salaire(self):
        pass

class EmployeHoraire(Employe):
    def __init__(self, nom, taux_horaire, heures_travail):
        super().__init__(nom)
        self.taux_horaire = taux_horaire
        self.heures_travail = heures_travail

    def calculer_salaire(self):
        return self.taux_horaire * self.heures_travail

class EmployeMensuel(Employe):
    def __init__(self, nom, salaire_mensuel):
        super().__init__(nom)
        self.salaire_mensuel = salaire_mensuel

    def calculer_salaire(self):
        return self.salaire_mensuel

# Exemple d'utilisation
employes = [
    EmployeHoraire("Alice", 20, 120),
    EmployeMensuel("Bob", 3000)
]

for employe in employes:
    print(f"Employé : {employe.nom}, Salaire : {employe.calculer_salaire()} €")
