from time import sleep

print('=' * 20,'DESAFIO 104 - HELPER PYTHON')


def cores(color):
    cor = {
        'limpa': '\33[m',
        'vermelho': '\33[1;30;41m',
        'amarelo': '\33[30;43m',
        'azul': '\33[1;30;44m'
    }

    return cor[color]


def titulo(msg, cor):
    tam = len(msg) + 4
    print(cores(cor),end='')
    print(f'~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)
    print(cores('limpa'),end='')


titulo('PY HELPER - ajuda com comandos','amarelo')


helper = ''
while helper != 'sair':
    helper = input('ajuda ou duvida> ').lower()
    sleep(1)
    titulo('Aguarde...', 'vermelho')
    sleep(2)
    print(cores('azul'))
    help(helper)
    print(cores('limpa'))