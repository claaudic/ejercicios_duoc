asci_caracter = int (input("ingrese un carácter "))

if asci_caracter >= 65 and asci_caracter <= 90:
    print("es letra mayu")
elif asci_caracter >= 97 and asci_caracter <= 122:
    print("es letra mini")
else:
    print("simbolo")