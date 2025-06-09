fruta = "frutilla"
#len -> te dice el largo de una palabra o una lista
print(len(fruta))

for i in range (len(fruta)-1):
    print(f"LA FRUTA ES {fruta} {i}")
#for i in fruta
#print (f"la fruta es {fruta}")




palabra = input("Ingrese una palabra \n")

for i in range(10) :
    print(f"La palabra es {palabra}")


edad = int (input("Cuantos años tiene?"))

for i in range (edad):
    if i + 1 == 1:
        print(f"Has cumplido 1 año")
    else:
        print(f"has cumplido  {i+1} años")
        
num = 0
while num != 100:
    num = num + 1
    print(num)