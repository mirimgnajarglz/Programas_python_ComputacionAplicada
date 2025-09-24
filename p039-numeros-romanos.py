# p039-numeros-romanos.py
# Solicita un numero entre 1 y 10 y mostrarlo en numeros romanos

numero = int(input("Ingresa un numero entre 1 y 10: "))

romanos = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X"
}

if numero in romanos:
    print(romanos[numero])
else:
    print("Error: Numero inválido.")

print("\nPrograma terminado")
