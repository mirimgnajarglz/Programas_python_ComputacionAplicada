# p012-funcion-matematicas-equacion.py
# Evaluar la función f(x, y) = 3x2 + √(x2 + y2) + e^(ln(x))

import math as mt 


x = 2
y = 2


fxy1 = 3 * mt.pow (x,2) + mt.sqrt( mt.pow  (x,2 ) + mt.pow(y,2)) + mt.pow(mt.e, mt.log(x))
fxy2 = 3 * x**2 +mt.sqrt (x**2 + y**2) + mt.e ** mt.log(x) 

print(f"El resultado es : {fxy1:.4f}")
print(f"El resultado es : {fxy2:.4f}")