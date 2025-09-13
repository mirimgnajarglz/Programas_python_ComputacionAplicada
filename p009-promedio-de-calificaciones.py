# p009-promedio-de-calificaciones.py 
# Calcuar el promedio de tres calificaciones ingresadas por el usuario

print("Calculando el promedio de tres calificaciones:\n")

# Solicitar 3 calificaciones separadas por espacio
cal1, cal2, cal3 = input ().split() # Se almacena cada valor por separado en base al espacio (como cadena)
print(type(cal1), type(cal2), type(cal3))

cal1, cal2, cal3 = int(cal1), int(cal2), int(cal3) # Convertir cada variable de cadena a entero
print(type(cal1), type(cal2), type(cal3)) 

# Calcular promedio
suma = ( cal1 + cal2 + cal3 ) 
promedio = suma / 3


# mostrar el resultado 
print(f"Las calificaciones son: {cal1}, {cal2}, {cal3}") 
print(f"La suma es : {suma}")
print(f"El promedio es : {promedio}")

