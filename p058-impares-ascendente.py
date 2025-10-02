# p058-impares-ascendente.py
# Programa para imprimir números impares y su suma total

while True:
    n = int(input("Ingresa un número límite: "))

    i = 1
    suma = 0

    while i <= n:
        if i % 2 != 0:  # Si es impar
            print(i)
            suma += i
        else:
            suma = suma
        i += 1

    print("La suma total de los impares es:", suma)

    if input('\n¿Deseas continuar (S/N)? ').upper() == 'N':
        break

print("Programa Terminado.")