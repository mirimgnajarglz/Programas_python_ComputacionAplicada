# p008-entrada-con-espacio.py
# Leer tres numeros enteros separados por un espacio

print("Entrada de varios valores separados por un espacio")

print('Dame tres números separados por espacio :')

n1, n2, n3 = input().split() # Leo una linea y la separo en base al espacio (split)

n1, n2, n3 =  int(n1), int(n2), int(n3) 

print('Los valores introducidos son:')
print(n1, n2, n3)