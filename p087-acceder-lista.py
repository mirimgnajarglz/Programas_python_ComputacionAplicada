# p087-acceder-lista.py 
# Accede a elementos de una lista

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print('\033[H\033[J')

print('Acceder a los elementos de una lista\n')

print('\nLongitud y contenido de las mediciones :')
print(f'Cuantas mediciones son : {len(nums)}')
print(f'Todas las mediciones : {nums} ')

print('\nPrimera y ultima medicion, por indice positivo : ')
print(f'Primera y última : {nums[0]}') 
print(f'Primera y última :{nums[8]}')

print('\nPrimera y ultima medicion,por indice negativo : ')
print(f'Primera y última : {nums[-9]}')
print(f'Primera y última : {nums[-1]}')

print('\nPor rango : ')
print(f'Mediciones de la 2 ala 6 (6 no incluida): {nums[2:6]}')

print('\nPor saltos consecutivos:')
print(f'Las primeras 3 desde el principio : {nums[:3]}')
print(f'Las ultimas 3 desde el 6 hasta el final : {nums[6:]}')

print ("\nPrograma terminado")