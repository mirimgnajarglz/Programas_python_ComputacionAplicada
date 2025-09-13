# p016-tercer-angulo.py
# Solicitar al usuario los dos ángulos conocidos

angulo1 = float(input("Ingresa el primer ángulo del triángulo  : "))
angulo2 = float(input("Ingresa el segundo ángulo del triángulo : "))


angulo3 = 180 - (angulo1 + angulo2)

print(f"El tercer ángulo del triangulo es: {angulo3:.2f} grados")
