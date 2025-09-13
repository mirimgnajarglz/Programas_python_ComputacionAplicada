# p010-operaciones-matematicas.py 
# Demostrar el uso de los diferentes operadores aritmeticos con numero

print("=" * 80)
print(" calculadora de operaciones matematicas ")
print("=" * 80)

# Entrada
x = float(input('Valor de x ? : '))
y = float(input('Valor de y ? : '))


# Salida 
print(f"Suma             : {x:>6} + {y:<6} = {x + y:>10.2f}")
print(f"Resta            : {x:>6} - {y:<6} = {x - y:>10.2f}")
print(f"Multiplicación   : {x:>6} × {y:<6} = {x * y:>10.2f}")
print(f"División         : {x:>6} ÷ {y:<6} = {x / y:>10.2f}")
print(f"Módulo           : {x:>6} % {y:<6} = {x % y:>10.2f}")
print(f"Exponenciación   : {x:>6} ^ {y:<6} = {x ** y:>10.2f}")
print(f"División entera  : {x:>6} // {y:<6} = {x // y:>10.2f}")
print("=" * 80)
