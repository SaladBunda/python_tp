villes = ("tetouan", "tanger", "rabat", "casablanca", "marrakech")
print(villes[1])
print(villes[-1])
villes2 = ("fes", "meknes")

villes = villes + villes2

str = input("Donnez une ville: ")
if str in villes:
	print("La ville existe")
