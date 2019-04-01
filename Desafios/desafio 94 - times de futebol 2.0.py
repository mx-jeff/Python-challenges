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
    time = []
    jogador = dict()
    partidas = list()

    while True:
        #entrada
        jogador.clear()
        jogador['nome'] = str(input('Nome do jogador: '))
        tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
        partidas.clear()
        for c in range(0, tot):
            partidas.append(int(input(f'  Quantos gols na partida {c + 1}? ')))

        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
        time.append(jogador.copy())

        while True:
            resp = str(input('Quer continuar? [S/N]')).upper()[0]
            if resp in 'SN':
                break
            print('ERRO!, responda apenas S ou N')
        if resp == 'N':
            break

    #cabecalho
    print('-='*20)
    print('cod ', end='')
    for i in jogador.keys():
        print(f'{i:<15}', end='')
    print()

    # tabela
    print("-" * 40)
    for chave, valor in enumerate(time):
        print(f'{chave:>3} ', end='')
        for dados in valor.values():
            print(f'{str(dados):<15}', end='')
        print()
    print("-" * 40)

    #Resultados
    while True:
        busca = int(input('Mostrar dados de qual jogador? (999 para sair) '))
        if busca == 999:
            break

        if busca >= len(time):
            print(f'ERRO! Não existe jogador com esse codigo {busca}')
        else:
            print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
            for i, g in enumerate(time[busca]['gols']):
                print(f'    No jogo {i + 1} fez {g} gols.')
        print('-' * 40)
    print('Volte sempre')


cursoEmVideo()
