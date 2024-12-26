n = int(input("Entrer le nombre de depart: "))

fact = 1
for num in range(1,n+1):
    fact*=num
print("Le factorielle de {0} est {1}".format(n,fact))

i = 1
fact2= 1
while(i <= n):
    fact2*=i
    i+=1

print("Le factorielle de {0} est {1}".format(n,fact2))
