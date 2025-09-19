# p025-verificar-suma.py
# Verificar si la suma de dos numeros es igual a un tercero

print('-' * 60)
print('Verificar si la \"suma\" de dos numeros es igual a un tercero 🤔')
print('-' * 60) 

# Entrada
print("\n Dame 3 numeros enteros : ")
n1 = int(input("Numero 1 ? "))
n2 = int(input("Numero 2 ? "))
n3 = int(input("Numero 3 ? "))

# Proceso
suma = n1 + n2

if suma == n3:
    print(f"\n ✔!Correcto! {n1} + {n2} Es igual {n3}")
else:
    print(f"\n ❌No coinciden {n1} + {n2} No es igual {n3}!")

print('-' * 60)
print("\n Fin del programa")