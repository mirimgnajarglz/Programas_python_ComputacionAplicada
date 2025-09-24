# p031-2da-ley-de-newton.py
# Calcular la segunda ley de newton
# fuerza = masa * aceleracion, masa = fuerza / aceleracion, aceleracion = fuerza / masa

print("\033[2J\033[H")
print(' Calcular los valores de la segunda Ley de newton ')
print('[F] uerza = masa * aceleracion)')
print('[M] asa = fuerza / aceleracion)')
print('[A] celeracion  = fuerza / masa')
opcion = input("Elige una opcion ?").upper()

if opcion == "F":
    print('\n Calculando la Fuerza')
    masa = float(input('Dame la masa: '))
    aceleracion = float(input('Dame la aceleración: '))
    fuerza = masa * aceleracion
    print(f' La fuerza es: {fuerza} ')
elif opcion == "M":
      print('\n Calculando la Masa...')
      fuerza = float(input('Dame la fuerza: '))
      aceleracion = float(input('Dame la aceleración: '))
      masa = fuerza / aceleracion
      print(f' La masa es: {masa} ')
elif opcion == "A":
      print('\n Calculando la Aceleración...')
      fuerza = float(input('Dame la fuerza: '))
      masa = float(input('Dame la masa: '))
      aceleracion = fuerza / masa
      print(f' La aceleración es: {aceleracion} ')
else:
     print("\nOpcion invalida, elige F, M, o A")

print("\nProceso terminado")