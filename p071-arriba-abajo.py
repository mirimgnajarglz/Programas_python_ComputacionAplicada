# p071-arriba-abajo.py
# Imprimir numeros de 1 a n o de n a 1

while(True):
    print('\033[H\033[J')
    print('Imprimir numeros usando ciclo for - arriba o abajo')
    print('[ 1 ] Imprimir numeros de 1 a n ')
    print('[ 2 ] Imprimir numeros de n a 1 ')
    op = int(input('Elige ? '))
    if op==1:
        print(f'\nImprimir numeros de 1 a n')#{n}
        n = int(input('Limite ? '))
        for x in range(1, n):
            print(x, end=' ')
    elif op==2:
        print(f'\nImprimir numeros de n a 1')
        n = int(input('Desde donde ? '))
        for x in range(n, 0, -1):
            print(x, end=' ')
    else:
        print('\nOpción No valida')
    
    if input('\n\nDeseas continuar ( S / N ) ? ').upper()=='N': break

print('\nPrograma terminado')
