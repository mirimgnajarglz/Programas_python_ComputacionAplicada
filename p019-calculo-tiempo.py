# p019-calculo-tiempo.py
# calcular y mostrar el equivalente en tiempo

horas = int(input("Ingresa una cantidad de horas : "))


dias = horas // 24
minutos = horas * 60
segundos = minutos * 60


print(f"{horas} horas equivalen a:")
print(f"- {dias} dias")
print(f"- {minutos} minutos")
print(f"- {segundos} segundos")
