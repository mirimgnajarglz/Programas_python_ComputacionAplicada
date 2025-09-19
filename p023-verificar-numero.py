# p023-verificar-numero.py
# Verificar si un numero es positivo, negativo o cero

print ("Verificando si un numero es positivo, negativo o cero")

# Entrada 
print("Dame un numero entero: ")
numero = int (input())

# Proceso
if numero > 0:
    print ("El numero es positivo 👍")
if numero < 0:
    print ("El numero es negativo 👎")
if numero==0:
    print ("El numero es cero 👹")

print ("\n Proceso terminado")