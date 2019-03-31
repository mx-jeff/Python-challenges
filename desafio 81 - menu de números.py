print('=-' * 20, 'DESAFIO 81 - MENU DE NÚMEROS', '=-' * 20)

listaNumero = []
while True:
    num = int(input('Número: '))
    listaNumero.append(num)
    continua = str(input('Deseja Continuar? (Digite "S" para sair) ')).upper().strip()[0]
    if continua == 'S':
        break

print('='*40)
listaNumero.sort(reverse=True)
print(f'Os numeros são: {listaNumero}')
print('-'*40)
if 5 in listaNumero:
    print('Existe o número 5 na lista')
    print(f'O valor 5 se encontra em {listaNumero.index(5)}')
else:
    print('Não tem numero 5 na lista')
print('¨'*40)