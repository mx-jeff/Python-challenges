from random import randint
from time import sleep
print('$&' * 20, 'DESAFIO 87 - PALPITE DE MEGA SENA', '$' * 20)



def myMethod():
    try:
        megaNumeros = []
        print('Quantos jogos voce quer que eu sorteie? ')
        jogos = int(input('$: '))

        for jogo in range(0, jogos):

            print('Quantos numeros você quer que sorteie: ')
            numeros = int(input('$: '))

            for i in range(0, numeros):
                mega = randint(1, 60)
                megaNumeros.append(mega)

                print(f'Numero {i + 1}: {megaNumeros}',end='')
                megaNumeros.clear()
        print('\n=-'*40)

    except ValueError:
        print('VALOR INVALIDO!')

def cursoEmVideo():
    try:
        lista = []
        jogos = []
        print('-' * 30)
        print(' JOGA NA MEGA SENA  ')
        print('-' * 30)
        quantidade = int(input('Quantos jogos? ')) - 1

        total = 0
        while total <= quantidade:
            cont = 0
            while True:
                num = randint(1, 60)
                if num not in lista:
                    lista.append(num)
                    cont += 1
                if cont >= 6:
                    break
            lista.sort()
            jogos.append(lista[:])
            lista.clear()
            total += 1

        print('-='*3,f'SORTEANDO {quantidade + 1} JOGOS','-='*3)
        for jogo in jogos:
            print(f'Os numeros jogos são {jogo}')
            sleep(1)
        print('-='*5,'BOA SORTE','-='*5)

    except ValueError:
        print('VALOR INVALIDO!')

cursoEmVideo()