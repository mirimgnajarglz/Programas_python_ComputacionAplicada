# p026–convertir-temperaturas-v2.py
# Convertir temperaturas de grados celcius a farenheit y viceversa

print("\033[2J\033[H")
print("\033[31mConvertir de grados Celcius a grados Farenheit\033[0m")
      

print("\033[34m")
print("[C] elcius a Farenheit")
print("[F] arenheit a Celcius")
print("\033[0m")
op = input("Elige ? ").upper()

if op == "C":
    print("\nConvirtiendo de Celcius a Farenheit 🌡")
    c = float(input("Introduce los grados Celcius ? "))
    f = (c * 9 / 5 ) + 32
    print(f"\n{c:.2f} grados Celcius, equivale a {f:.2f} grados Farenheit")
else:
    if op=="F":
        print("\nConvirtiendo de Farenheit a Celcius 🌡")
        f = float(input("Introduce los grados Celcius ? "))
        c = (f -32) * 5 / 9
        print(f"\n{f:.2f} grados Farenheit, equivale a {c:.2f} grados Centigrados")
    else:
        print("❌Opcion invalida !!!")