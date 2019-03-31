print('=-' * 20, 'DESAFIO 79 - LISTA DE NùMEROS', '=-' * 20)

def metodoProprio():
    listaNumeros = []

    while True:
        num = int(input('Numero: '))
        if num in listaNumeros:
            print('Desculpa, Numero ja existe!')
        else:
            listaNumeros.append(num)
        info = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
        if info == 'N':
            break

    print('=*'*40)
    listaNumeros.sort()
    for exibir in listaNumeros:
        print(f'{exibir} ')
    print('acabou!')

metodoProprio()