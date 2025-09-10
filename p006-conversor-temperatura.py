# p006-conversor-temperatura.py
# Convierte temperaturas de Celsius a Fahrenheit

print("Conversor de Temperatura (Celsius - Fahrenheit):\n")

celsius = float(input("Ingresa la temperatura en Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"\n {celsius:.2f} grados celsius equivale a {fahrenheit:.2f} fahrenheit")

