#p084-cuadro-hueco-caracter.py
# Dibujar un cuadrado hueco con el caracter indicado

lado = int(input("¿De que tamaño sera el lado del cuadrado? "))
caracter = input("¿Que caracter quieres usar? ")

for fila in range(1, lado + 1):
    for columna in range(1, lado + 1):
        if fila == 1 or fila == lado or columna == 1 or columna == lado:
            print(caracter, end=" ")
        else:
            print(" ", end=" ")
    print() 

print("\nPrograma terminado")