# p051-adivina-numero.py
# Simula un juego de azar donde el usuario adivina un numero entre 1 y 50

import random

print("\033[2J\033[H")
print("🎲 ¡Bienvenido al juego 'Adivina el Número'! 🎲")
print("Yo te doy un número entre 1 y 50. ¿Podrás adivinarlo?")

numero_secreto = random.randint(1, 50) 
intento_usuario = 0
contador_intentos = 0

while True:
    intento_usuario = int(input("Tu número: "))
    contador_intentos += 1
    if intento_usuario < numero_secreto:
        print(" ¡Demasiado bajo! Intenta con un número más alto.")
    elif intento_usuario > numero_secreto:
        print(" ¡Demasiado alto! Intenta con un número más bajo.")
    else:
        print(f"\n ¡Felicidades! ¡Adivinaste el número secreto que era {numero_secreto}!")
        print(f"Lo lograste en {contador_intentos} intentos.")
        break
print("\n Programa terminado")