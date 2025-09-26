# p049-sumar-consecutivos.py
# Suma números hasta alcanzar 100

print(" 🤑 Rifa entre amigos para recaudar 100, cuantos boletos necesito? ")

c = 0
suma = 0
meta = 200

while c < 200:
    c += 1
    suma += c
    print(f" (+{c})", end="")

    if suma >= meta:
        print("\n\n🏆 ¡Meta alcanzada!")
        print(f"Boletos: {c}")
        break

print(f"Se necesitaron los primeros {c} números para llegar a una suma de ${suma}.")