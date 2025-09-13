# p020-numero-suerte.py
# Cacular el numero de suerte

print('Calcular el numero de la suerte\n')

año_nacimiento = int(input('El año de nacimiento es ?: '))
suma_digitos = sum(int(digito) for digito in str(año_nacimiento))

d1 = año_nacimiento // 1000           
d2 = (año_nacimiento // 100) % 10     
d3 = (año_nacimiento // 10) % 10      
d4 = año_nacimiento % 10             

print("\nDigitos individuales:")
print(d1)
print(d2)
print(d3)
print(d4)

print(f'Tu numero de la suerte es: {suma_digitos}') 

