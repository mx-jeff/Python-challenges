from random import randint
from time import sleep
from operator import itemgetter

print('◘' * 20, 'DESAFIO - 90', '◘' * 20)


def metodo1():
    jogador = {
        'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
    }

    lider = dict()

    def mostra(jogador):
        for key, value in jogador.items():
            print('◘' * 3, f'{key}: tirou {value}', '◘' * 3)
            sleep(1)
        print('◘' * 23)

    #def lideres(jogador, lider):
    #    lider = sorted(jogador.itens(), key=itemgetter(1))
    #    print(lider)

    def inicia():
        mostra(jogador)
        #lideres(jogador, lider)

    inicia()


def cursoEmVideo():
    jogo = {
        'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)
    }



    print('Valores sorteados: ')
    for k, v in jogo.items():
        print(f'{k} tirou {v} no dado.')
        sleep(1)

    ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
    print('◘'*40)
    print('  -=  RANKING  =-  ')
    for i, v in enumerate(ranking):
        print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
        sleep(1)

cursoEmVideo()