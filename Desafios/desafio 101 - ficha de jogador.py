#!/usr/bin/python
# -*- coding: utf-8 -*-

print("=" * 20, "ficha de jogador", "=" * 20 )


def ficha(nome = '<desconhecido>', gol=2):
    print (f'O jogador {nome} fez {gol} No campeonato')

continua = ' '
while continua != 'S':
    nome = str(input("Nome do jogador: "))
    gols = str(input("Nº de gols: ")) 

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    if nome.strip() == '':
        ficha(gol=gols)
    else:
        ficha(nome, gols)
            
    continua = str(input("Sair? [S/N]")).upper()

    

input("Digite ENTER para sair...")
