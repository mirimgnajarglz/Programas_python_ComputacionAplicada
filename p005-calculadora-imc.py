# p005-calculadora-imc.py
# Calcula el indice de masa corporal

print("Calculando el indice de masa corporal (IMC):\n")

# Entrada 
peso_kg = float(input("Ingresa tu peso en kilogramos: "))
altura_m = float(input("Ingresa tu altura en metros: "))

# Proceso
imc = peso_kg / (altura_m ** 2) # Divide el peso entre la altura al cuadrado (** eleva a la potencia)

# Salida
print("El peso es {0:.2f}kg y la altura {1:.2f}m y resulta en un IMC de {2:.2f}".format (peso_kg,altura_m,imc))
