# p041-aceptar-estudiante-V2.py
# Solicita los datos del aspirante

nombre = input("Nombre: ")
sexo = input("Sexo (h/m): ").lower()
edad = int(input("Edad: "))

calificaciones = []
for i in range(3):
    nota = float(input(f"Calificacion #{i+1}: "))
    calificaciones.append(nota)

promedio = sum(calificaciones) / len(calificaciones)

if sexo != "m":
    print(f"Lo sentimos, {nombre}. La universidad solo acepta mujeres.")
elif edad <= 21:
    print(f"Lo sentimos, {nombre}. No cumples con la edad requerida (mayores de 21 años).")
elif not (8 <= promedio <= 9.5):
    print(f"Lo sentimos, {nombre}. Tu promedio de {promedio:.2f} no alcanza el mínimo requerido de 8.")
else:
    print(f"¡Felicidades, {nombre}! Has sido aceptada. Cumples con la edad y tu promedio de {promedio:.2f} está dentro del rango permitido.")

print("\nPrograma terminado")
