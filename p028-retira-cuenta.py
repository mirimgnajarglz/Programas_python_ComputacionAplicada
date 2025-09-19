# p028-retira-cuenta.py
#Simula un retiro de dinero de una cuenta con validaciones anidadas


saldo_actual = 1500.50
print("Simulacro de retiro")
print("\033[2J\033[H")
print(f"Tu saldo inicial es de {saldo_actual:.2f}")

cantidad_retiro = float(input("Ingresa la cantidad a retirar: $"))

if cantidad_retiro > 0:
    if cantidad_retiro <= saldo_actual:
        print("Iniciando con el retiro...")
        saldo_actual -= cantidad_retiro
        print("\n Retiro exitoso.")
        print(f"Tu nuevo saldo es: ${saldo_actual:,.2f}")
    else:
        print("\n Fondos insuficientes. No se puede completar la transacción.")

else:
    print("\n La cantidad a retirar debe ser un número positivo.")

print("\nProceso terminado.")