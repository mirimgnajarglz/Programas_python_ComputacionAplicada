# p038-dia-semana.py
# Solicitar un numero del 1 al 7 y mostrar el dia de la semana 

numero = int(input("Ingresa un numero del 1 al 7: "))

dias = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]

if 1 <= numero <= 7:
    print(dias[numero - 1])
else:
    print("Error: Dia invalido")

print("\nPrograma terminado")
