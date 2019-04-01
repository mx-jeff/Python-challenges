from random import sample
from random import randint
from time import sleep

print('=' * 10 , 'DESAFIO - 73 SORTEIO DE TUPLAS', '=' * 10)

def optimzed():
    z = tuple(sample(range(10), 5))
    print(z)
    print(f'O maior valor é {max(z)} e o menor é {min(z)}')

def cursoEmVideo():

    aleatorio = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),)

    print(f'O numeros foram de: ', end='')
    for n in aleatorio:
        print(f'{n} ', end='')
    print('\nAguarde...')
    sleep(1)
    print(f'O maior valor sorteado foi de {max(aleatorio)}')
    print(f'O menor valor sorteado foi de {min(aleatorio)}')
    sleep(1)


cursoEmVideo()