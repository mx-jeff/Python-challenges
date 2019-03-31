print('=' * 20, 'DESAFIO 81 - LISTAS PARES E ÌMPARES', '=' * 20)

listaPar = []
listaTotal = []
ListaImpar = []
while True:
    num = int(input('Número: '))
    continua = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    listaTotal.append(num)

    if continua == 'N':
        break

    if num % 2 == 0:
        listaPar.append(num)
    else:
        ListaImpar.append(num)

print('%*' * 40)
print(f'Os números colocados são {listaTotal}')
print(f'Os numeros pares são {listaPar}')
print(f'Os números ímpares são {ListaImpar}')
