print('=-' * 10, 'DESAFIO 74 - ANALISE DE DADOS COM TUPLAS', '=-' * 10)

storage = (
    int(input('Valor 1: ')),
    int(input('Valor 2: ')),
    int(input('Valor 3: ')),
    int(input('Valor 4: '))
)

print('=-' * 40 )
print('Os numeros são: ')
for n in storage:
    print(f'{n} ', end='')
print('\n')
print('=-' * 40 )
print(f'O numero 9 aparece {storage.count(9)} vezes')
print('=-' * 40 )
if 3 in storage:
    print(f'O valor 3 apareceu {storage.index(3) + 1}ª posição')
else:
    print('O valor 3 não existe em nenhuma posição')
print('=-' * 40 )
print('Os valores pares foram: ', end=' ')
for n in storage:
    if n % 2 == 0:
        print(n, end=' ')