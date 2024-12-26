fruits = ["banane", "pomme", "poire", "kiwi", "fraise"]

fruits += ["abricot", "cerise"]

del fruits[2]
fruits.sort()

for fruit in fruits:
	print(fruit)