# p042-precio-entrada-cine.py
# Determinar el precio de una entrada segun la edad del cliente para el cine

edad = int(input("Ingresa tu edad: "))

if edad < 5:
    print("Tu entrada es gratis.")
elif edad <= 12:
    print("El precio de tu entrada es de $5.")
elif edad <= 64:
    print("El precio de tu entrada es de $10.")
else:
    print("El precio de tu entrada es de $7.")

print("\nPrograma terminado")
