# p027-calcular-paga-extra.py
# Calcula la paga de un trabajador considerando horas extra

print("\033[2J\033[H")
print('Calculando la paga de un trabajador ')

# Entrada 
print("Datos del trabajador: ")
nombre = input('Nombre del trabajador: ')
horas = int(input('Horas trabajadas: '))
paga_hora = float(input('Paga por hora: '))

# Proceso
horas_normales = 40
paga_normal = 0
paga_extra = 0
total = 0

if horas<= horas_normales:
    paga_norma = horas * paga_hora
else:
    horas_estra = horas - horas_normales
    paga_extra = paga_extra * (paga_hora * 2)
    total = horas_normales * paga_hora * paga_extra


print("\n Cálculo completo")
print(f'\n {nombre} trabajo {horas} horas, a una paga de {paga_hora} pesos por hora')
print(f'Paga normal = ${paga_normal:13,.2f}')
print(f'Paga extra = ${paga_extra:13,.2f}')
print(f'El pago total = ${total:13,.2f}')
print('\n* ¡Programa finalizado! *')