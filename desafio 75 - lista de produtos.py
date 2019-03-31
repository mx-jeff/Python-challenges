print('=' * 20,'DESAFIO 75 - LISTA DE PRODUTOS', '=' * 20)

produtos = (
    'Lápis', 1.50,
    'Caneta', 1.50,
    'Caderno', 5.00
)

print('-'*30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-'*30)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f'R${produtos[item]:>4.2f}')