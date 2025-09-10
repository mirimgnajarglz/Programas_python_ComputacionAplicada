# p004-paga-trabajador.py
# Calcula la paga de un trabajador

print('Calculando la paga de un trabajador \n')

# Entrada
nombre = input( "Nombre : " )
horas = int( input("Horas : ") )
paga = float(input( "Paga x Hora : ") )

# Proceso
tasa = 0.09 # Impuesto de hacienda
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

# Salida
print('\nResumen de pagos: \n')
print(f'El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga:.2f} pesos, con una tasa de {tasa:.2%} ' )
print(f'Paga bruta   : {pagabruta:,.2f} ')
print(f'Impuesto     : {impuesto:,.2f} ')
print(f'Paga neta    : {paganeta:,.2f} ')