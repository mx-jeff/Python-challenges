print('-=' * 20, 'DESAFIO 92 - GERENCIAMENTOS DE TIMES', '-=' * 20)


def master():
    futJogador = dict()
    gols = list()
    futJogador['nome'] = str(input('Nome do jogador: '))
    partida = int(input('Nº de partidas: '))
    for c in range(0, partida):
        gols.append(int(input('Nº de gols: ')))

    futJogador['gol'] = gols[:]
    futJogador['total'] = sum(gols)
    print('-' * 60)

    print(f'O jogador {futJogador["nome"]} jogou {len(futJogador["gol"])} partidas. ')
    for indice, valor in enumerate(futJogador["gol"]):
        print(f' -> Na partida {indice + 1} fez {valor} gols. ')
    print(f'Total de {futJogador["total"]} gols')


def cursoEmVideo():
    jogador = dict()
    partidas = list()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {c + 1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    print("-=" * 30)
    for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}')
    print("-=" * 30)
    print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
    for i, v in enumerate(jogador['gols']):
        print(f'   ==> Na partida {i + 1}, fez {v} gols.')
    print(f'Foi um total de {jogador["total"]} gols')


def another():

    class Jogador(object):

        def __init__(self, partidas, jogador=[{'nome': 'nome'}, {'gols': []}, {'total': 0}]):

            self.jogador = jogador
            self.partidas = partidas

        def info(self, nome):

            self.jogador[0]['nome'] = nome
            for i in range(self.partidas):
                gol = int(input(f"  Quantos gols {nome} fez na partida {i + 1}? "))
                self.jogador[1]['gols'].append(gol)
            self.jogador[2]['total'] += sum(self.jogador[1]['gols'])

        def imprimirValores(self):
            print(20 * "-=")
            print(self.jogador)
            print(20 * "-=")
            print(f"O campo nome tem o valor {self.jogador[0]['nome']}")
            print(f"O campo gols tem o valor {self.jogador[1]['gols']}")
            print(f"O campo total tem o valor {self.jogador[2]['total']}")
            print(20 * "-=")
            print(f"O jogador {self.jogador[0]['nome']} jogou {self.partidas} partidas.")
            for i in range(self.partidas):
                print(f"    => Na partida {i + 1}, ele fez {self.jogador[1]['gols'][i]} gols.")
            print(f"Foi um total de {self.jogador[2]['total']} gols.")


    nome = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {nome} jogou? "))

    i = Jogador(partidas)
    i.info(nome)
    i.imprimirValores()

master()