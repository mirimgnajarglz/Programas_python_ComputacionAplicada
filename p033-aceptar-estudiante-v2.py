# p033-aceptar-estudiante-v2.py
# Aceptar a un estudiante en base a la edad y 2 calificaciones 
# Usaremos and

print("\033[2J\033[H")
print('--- Admision de estudiantes a la Universidad Sierra Madre ---')

nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))


if edad >= 18:
    print("El proceso continua...")
    print('Ingresa 2 calificaciones separadas por Enter')
    calificacion1 = float(input())
    calificacion2 = float(input())
    if calificacion1 >= 8 and calificacion2 >= 8:
        print(f" ¡Bienvenido, {nombre}! tu edad {edad} y tus {calificacion1}, {calificacion2} te permiten ingresar")
    else:
        print(f' Lo sentimos, se requieren 2 calificaciones de 8 como minimo, y tu tienes {calificacion1}, {calificacion2}')
else:
    print(f' Lo sentimos, {nombre}. Solo aceptamos a mayores de edad y tu tienes tan solo {edad} años')
print("\nProceso terminado...")