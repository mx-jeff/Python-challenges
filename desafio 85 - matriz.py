print('=' * 20, 'DESAFIO 85 - MATRIZ', '=' * 20)

def cursoEmVideo():
    try:
        matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for linha in range(0, 3):
            for coluna in range(0, 3):
                matriz[linha][coluna] = int(input(f'digite um valor para [{linha}, {coluna}]: '))

        print('-=' * 30)
        for linha in range(0,3):
            print('-'*20)
            for coluna in range(0, 3):
                print(f'[{matriz[linha][coluna]:^5}]', end='')
            print()

    except ValueError:
        print('Valor invalido!')

def menos():
    matriz = [[], [], []]
    for c in range(3):
        for l in range(3):
            matriz[c].append(int(input(f'Digite valor para [{c},{l}]: ')))
    for c in range(3):
        print('\n', end='') if c > 0 else ''
        for l in matriz[c]:
            print(f'[{l:^5}]', end='')

def menos2():
    try:
        linhas = 3
        colunas = 3
        matriz = [[input(f'({linha},{coluna})') for coluna in range(1, colunas + 1)] for linha in range(1, linhas + 1)]
        for i in matriz:
            print(i)
    except ValueError:
        print('Valor invalido!')


menos2()