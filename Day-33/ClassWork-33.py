len ითვლის თითოუელ ელემნტს
new_goa = ""
goa = "Goa Is The Best"
i იღებს თითოუელ ინდექსს goa -ში
for i in range(len(goa)):
    print("fisrt loop")
    print(goa[i])
------------------------------
i იღებს თითოეული ასოს მნიშველობას goa -ში
goa = "Goa Is The Best"
for i in goa:
    if i != " ":
        new_goa += i
print(new_goa)
------------------------------
arr = ["goa",2,3,3,4,4,4,4,5,5,5,6,6,6,7,7,78,8]
i იღებს თოთეული ელემენტის მნიშვნელობას arr-ში
for i in arr:
    print(i)