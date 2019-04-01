print("=-"*40)
print('DESAFIO 70 - SIMULADOR DE CAIXA ELETRÔNICO')
print("=-"*40)

def caixa1():

    #Logica: tirar 50 do valor total, para cedula
    print("-"*40)
    print('{:^30}'.format('BANCO TABAJARA'))
    print("-" * 40)

    valor = int(input('Qual valor requerido? R$'))
    total = valor
    cedula = 50
    totalCedula = 0

    while True:

        if total >= cedula:
            total -= cedula
            totalCedula += 1

        else:

            if totalCedula > 0:
                print(f'Total de {totalCedula} cedulas de R${cedula} reais')

            if cedula == 50:
                cedula = 20

            elif cedula == 20:
                cedula = 10

            elif cedula == 10:
                cedula = 1

            totalCedula = 0

            if total == 0:
                break
    print("=" * 40)
    print("Volte sempre ao banco tabajara!")

def caixa2():

    saque = int(input('Sacar R$: '))
    cedulas = [1, 10, 20, 50]
    c = 3
    while saque > 0:
        qtdced = saque // cedulas[c]
        saque -= qtdced * cedulas[c]
        c -= 1﻿
        if qtdced > 0:
            print(f'{qtdced} cédulas de R$ {cedulas[c]}')


caixa1()

