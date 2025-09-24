# p037-numero-mayor.py
# Solicita tres números al usuario para saber cual es mayor

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

mayor = max(num1, num2, num3)

print(f"El numero mayor es {mayor}.")

print("\nPrograma terminado")