# p022-resistencia-equivalente-paralelo.py
# calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo

R1 = float(input("Ingresa el valor de la resistencia R1 : "))
R2 = float(input("Ingresa el valor de la resistencia R2 : "))
R3 = float(input("Ingresa el valor de la resistencia R3 : "))
R4 = float(input("Ingresa el valor de la resistencia R4 : "))


inversa_total = (1/R1) + (1/R2) + (1/R3) + (1/R4)
resistencia_total = 1 / inversa_total


print(f"La resistencia total del circuito en paralelo es: {resistencia_total:.2f} ohmios")
