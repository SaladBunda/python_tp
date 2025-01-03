dict = {
	"yassin": 20,
	"mohamed": 21,
	"ahmed": 20,
	"ali": 22,
	"oussama": 60
}

dict["hatim"] = 23

del dict["yassin"]
dict.pop("mohamed")

for key in dict:
	print(key)

for age in dict.values():
	print(age)