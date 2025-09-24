# p034-tipo-angulo.py
# Mostrar el tipo de angulo
# <90 Agudo, =90 Recto, <180 Obtuso, =180 llano, <360 concavo, =360 completo

print("\033[2J\033[H")
print("--- clasificador de angulos de acuerdo a su magnitud")

angulo = int(input('Dame un ángulo en grados: '))

if angulo < 0 or angulo > 360:
    print(" Tu angulo de {angulo} grados, no esta en el rango de 0 a 360, por lo tanto es invalido ")
else:
    if angulo < 90:
        print(f"  El ángulo de {angulo} grados es angulo AGUDO ")
    elif angulo == 90:
        print(f' El ángulo de {angulo} grados es un ángulo RECTO.')
    elif angulo < 180:
        print(f' El ángulo de {angulo} grados es un ángulo OBTUSO.')
    elif angulo == 180:
        print(f' El ángulo de {angulo} grados es un ángulo LLANO.')
    elif angulo < 360:
        print(f' El ángulo de {angulo} grados es un ángulo CÓNCAVO.')
    else:
        print(f" El ángulo de {angulo} grados es un ángulo COMPLETO o Cerrado ")

print("\nPROCESO TERMINADO")