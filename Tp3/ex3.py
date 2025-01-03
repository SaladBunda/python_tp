import math

class Cercle:
    def __init__(self, rayon):
        self.__rayon = rayon if rayon > 0 else 0

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter
    def rayon(self, valeur):
        if valeur > 0:
            self.__rayon = valeur
        else:
            print("Le rayon doit être positif.")

    def calculer_surface(self):
        return math.pi * self.__rayon ** 2


cercle = Cercle(5)
print(f"Rayon initial : {cercle.rayon}")  

cercle.rayon = 10  
print(f"Nouveau rayon : {cercle.rayon}")

cercle.rayon = -3  
print(f"Rayon après tentative de modification : {cercle.rayon}")

surface = cercle.calculer_surface()  
print(f"Surface du cercle : {surface:.2f}")
