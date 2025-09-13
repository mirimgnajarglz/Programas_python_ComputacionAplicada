# p011-operadores-asignacion.py
# Demostrar el uso de los operadores de asignación

print("=" * 40)
print(" Operadores de asignacion python")
print("=" * 40)

# Operador de asignación básico (=)
x = 15
print(f"El valor inicial de x: {x}")

# Aplicar diferentes operadores de asignación
x += 5
print(f"x += 5 → x = {x}") # Equivale a: x = x + 5
x -= 3
print(f"x -= 3 → x = {x}") # Equivale a: x = x - 3
x *= 2
print(f"x *= 2 → x = {x}") # Equivale a: x = x * 2
x /= 4
print(f"x /= 4 → x = {x}") # Equivale a: x = x / 4
x %= 3
print(f"x %= 3 → x = {x}") # Equivale a: x = x % 3
x **= 2
print(f"x **= 2 → x = {x}") # Equivale a: x = x ** 2
x //= 2
print(f"x //= 2 → x = {x}") # Equivale a: x = x // 2
print("=" * 40)