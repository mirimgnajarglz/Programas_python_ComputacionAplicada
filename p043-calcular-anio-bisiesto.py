# p043-calcular-anio-bisiesto.py
# Solicita el año al usuario para determinar si es bisiesto

print("Verificador de Años Bisiestos")

an = int(input("Ingrese un año: "))

#Divisible por 4 y no por 100
#Divisible por 400

if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
    print(f"El año {an} es bisiesto ")
else:
    print(f"El año {an} no es bisiesto ")

print("\nPrograma terminado")