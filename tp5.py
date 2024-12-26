from math import *
print("On resoud les equations du format ax^2+bx+c=0")
a = int(input("Donnez le premier scalaire a:"))
b = int(input("Donnez le deuxieme scalaire b:"))
c = int(input("Donnez le troisieme scalaire c:"))
delta = b**2 -4 *a *c
if(delta > 0):
    x1 = (-b-sqrt(delta))/2*a
    x2 = (-b+sqrt(delta))/2*a
    print("Les solutions de l'equation sont: x1 = {0} et x2 = {1}".format(x1,x2))
elif delta == 0:
    x = (-b/2*a)
    print("La solution de l'equation est: x = {0}".format(x))
else:
    print("L'equation n'admit pas des solutions reelles")
