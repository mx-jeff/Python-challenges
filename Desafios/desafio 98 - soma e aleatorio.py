from random import randint
from time import sleep

def titulo(msg):
    tam = len(msg) + 4
    print("=" * tam)
    print(f"  {msg}")
    print("=" * tam)


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        numeroAleatorios = randint(1, 10)
        lista.append(numeroAleatorios)
        print(f'{numeroAleatorios} ', end='')
        sleep(1)
    print("Ready! ")

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lista}, temos {soma}")

titulo("DESAFIO 98 - SOMA DE PARES E ALEATÓRIOS")

numeros = []
sorteia(numeros)
titulo(" Somas ")
somaPar(numeros)


    
