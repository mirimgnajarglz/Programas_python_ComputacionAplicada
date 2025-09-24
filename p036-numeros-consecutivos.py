# p036-numeros-consecutivos.py
# Solicita tres numeros al usuario

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))


numeros = sorted([num1, num2, num3])

if numeros[1] == numeros[0] + 1 and numeros[2] == numeros[1] + 1:
    print("Los numeros son consecutivos.")
else:
    print("Los numeros no son consecutivos.")

print("\nPrograma terminado")