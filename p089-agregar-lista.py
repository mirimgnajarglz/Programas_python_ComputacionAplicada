# p089-agregar-lista.py
# Agregar elementos a una lista

print('\033[H\033[J')
print('Agregar elementos a una lista')

nums = [80.3, 12.5, 60.2, 30.4]

print(f'Temperaturas iniciales:: {nums} - {len(nums)}\n')

print(f'Agregar 90 y 100 al final:')
nums.append(90)
nums.append(100)
print(f'Resultado : {nums} - {len(nums)}\n')

print(f'Insertar 80 en la posicion 4:')
nums.insert(4, 80)
print(f'Resultado : {nums} - {len(nums)}\n')

print(f'Externder datos agregando [110, 120, 130] se agregan al final:')
otros = [110, 120, 130]
nums.extend(otros)
print(f'Resultado : {nums} - {len(nums)}\n')

print ("\nPrograma terminado")