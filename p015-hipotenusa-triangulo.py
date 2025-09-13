# p015-hipotenusa-triangulo.py 
# calcula la longitud de la hipotenusa de un triángulo rectángulo

import math as mt

cateto1 = float(input("Ingresa la longitud del primer cateto: "))
cateto2 = float(input("Ingresa la longitud del segundo cateto: "))

hipotenusa = mt.sqrt(cateto1**2 + cateto2**2) 

print('El valor de la hipotenusa es: {:.2f}'.format(hipotenusa))

