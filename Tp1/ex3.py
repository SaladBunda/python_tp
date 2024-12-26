HT = float(input("Entrer le prix Hors Taxes: "))
NA = int(input("Entrer le nombre d'article: "))
TVA = float(input("Entrer le taux de TVA en pourcentage: "))
print("Le prix total TTC est: {0:0.2f}".format(HT*NA*(1+TVA/100)))
