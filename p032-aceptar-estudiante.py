# p032-aceptar-estudiante.py
# Aceptar a un estudiante en base a la edad y 2 calificaciones.
# Usaremos or

print("\033[2J\033[H")
print('--- Admision de estudiantes a la Universidad Sierra Madre ---')

nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))

if edad < 18:
   print(f' Lo sentimos, {nombre}. Solo aceptamos a mayores de edad, y tu tienes tan solo {edad} !')
else:
   print('Ingresa 2 calificaciones separados po Enter:')
   calificacion1 = float(input())
   calificacion2 = float(input())
   if calificacion1 < 8 or calificacion2 < 8:
       print(' Lo sentimos, se requiere una calificación mínima de 8 y tu tienes {calificacion1}, {calificacion2}')
   else:
      print(f' ¡Bienvenido {nombre}! Tu edad {edad} y tus calificaciones: {calificacion1}, {calificacion2} te permiten ingresar')

print("\nProceso terminado")