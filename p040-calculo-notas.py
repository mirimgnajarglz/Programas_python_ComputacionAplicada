# p040-calculo-notas.py
# Calcular el promedio de 5 calificaciones ingresadas por el usuario.
calificaciones = []


for i in range(5):
    nota = float(input(f"Ingrese la calificacion #{i+1}: "))
    calificaciones.append(nota)

promedio = sum(calificaciones) / len(calificaciones)

print(f"Tu promedio es {promedio:.1f}.", end=" ")

if promedio < 6:
    print("Quedas reprobado.")
elif promedio < 7:
    print("Pasas de panzazo.")
elif promedio < 8:
    print("Muy bien, puedes mejorar.")
elif promedio < 9:
    print("Excelente, sigue así.")
elif promedio <= 10:
    print("Perfecto, tu esfuerzo valio la pena.")
else:
    print("Error: Promedio fuera de rango.")

print("\nPrograma terminado")
