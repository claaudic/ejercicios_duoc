año = int (input ("ingrese un año"))
if año % 4 == 0: 
    if año % 100 != 0:
        # no es divisible
        print("es")
    else:
        # es divisible
        if año % 400 == 0:
            print("es")
        else:
            print("no")
else:
    print("no")