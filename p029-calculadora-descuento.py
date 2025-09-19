# p029-calculadora-descuento.py
## Simula una calculadora de descuentos basada en el monto de la compra

compra = descuento = porcentaje = total = 0

print("\033[2J\033[H")
print("Calculadora de Descuentos \n")
compra = float(input("Ingresa el total de tu compra: $"))

if compra > 2000:
    porcentaje = 0.20
else:
    if compra > 1000:
        porcentaje = 0.10 
    else:
        if compra > 500:
            porcentaje = 0.05
        else:
            porcentaje = 0
    
descuento = compra = porcentaje
total = compra - descuento


print("\n--- Resumen de la Compra ---")
print(f"Total de la compra: ${compra:,.2f}")
print(f"Porcentaje de descuento: {int(porcentaje * 100)}%")
print(f"Ahorro por descuento: ${descuento:,.2f}")
print(f"Total a pagar: ${total:,.2f}")

print("\n¡Gracias por tu compra!")
