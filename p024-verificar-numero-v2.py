# p024-verificar-numero-v2.py
# Verificar si un numero es positivo, negativo o cero 

print('Verificando si un numero es positivo, negativo o cero')

# Entrada
print ('Dame un numero entero: ')
numero = int(input())

# Proceso o la toma de desicision 
if numero==0:
    print("El numero es cero 👹")
else:
 if numero < 0:
    print ("El numero es negativo👎")
 else:
    print ("El numero es positivo 👍")


print('\n Proceso terminado')