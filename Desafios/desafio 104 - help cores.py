from time import sleep

print('=' * 20,'DESAFIO 104 - HELPER PYTHON')


def titulo(msg):
    tam = len(msg) + 4
    print(f'~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)


titulo('PY HELPER - ajuda com comandos')

helper = ''
while helper != 'sair':
    helper = input('ajuda ou duvida> ').lower()
    titulo('Aguarde...')
    sleep(1)
    help(helper)