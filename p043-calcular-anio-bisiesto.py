# p043-calcular-anio-bisiesto.py
# Solicita el año al usuario para determinar si es bisiesto

anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")

print("\nPrograma terminado")
