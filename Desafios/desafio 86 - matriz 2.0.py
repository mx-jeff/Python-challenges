print('=' * 20, 'DESAFIO 86 - matriz 2.0', '=' * 20)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):

        tabela = matriz[linha][coluna]
        print(f'[{tabela:^5}]', end='')

        par = tabela % 2 == 0
        if par:
            spar += tabela

    print()

print('-=' * 30)
print(f'A soma dos valores pares é de {spar}')

for linha in range(0, 3):
    scol += matriz[linha][2]

print(f'A soma dos valores da terceira coluna é de: {scol}')
for coluna in range(0, 3):

    maiorColuna = matriz[1][coluna]
    if coluna == 3 or maiorColuna > maior:
        maior = maiorColuna

print(f'O maior valor da segunda linha é {maior}')
