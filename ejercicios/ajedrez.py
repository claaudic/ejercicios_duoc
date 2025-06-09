fila_alfil = int(input("Fila alfil "))
columna_alfil= int (input("Columna alfil "))
fila_torre = int(input("Fila torre "))
columna_torre = int(input("Columna torre "))

if (fila_alfil >= 1 and fila_alfil <= 1000) and (columna_alfil >= 1 and columna_alfil <= 1000):
    if (fila_torre >= 1 and fila_torre <= 1000) and (columna_torre >= 1 and columna_torre <= 1000):
        if columna_alfil == columna_torre:
            print("Torre captura a alfil")
        elif fila_alfil == fila_torre:
            print("Torre captura a alfil ")
             
        elif columna_alfil - columna_torre == fila_alfil - fila_torre:
            print("Alfil captura a torre")
        else:
            print("Ninguna pieza captura")
else:
    print("Invalido")


