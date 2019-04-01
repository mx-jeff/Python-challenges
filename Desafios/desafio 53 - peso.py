from time import sleep

print('=' * 20, 'DESAFIO 55 - PESO', '=' * 20)

def metodo1():
    v = []
    for peso in range(1,6):
        pessoas = float(input(f'Qual é o peso da {peso}º pessoa: '))
        v.append(pessoas)
    v.sort()

    print(f'O maior peso é {max(v)}Kg', end=' ')
    print(f'O menor peso é {min(v)}Kg', end='')

def metodo2():
    maior = 0
    menor = 0
    for p in range(1,6):
        peso = float(input(f'Peso da {p}º pessoa: '))
        if peso == 1:
            maior = p
            menor = p
        else:
           if peso > maior:
                maior = peso
           elif peso < maior:
               menor = peso
    print(f'O maior peso lindo foi de {maior}Kg')
    print(f'O menor peso lido foi de {menor}Kg')

print('''Métodos: escolha o seu
    [1] método personalizado
    [2] método tradicional''')

opcao = int(input('Número: '))

if opcao == 1:
    print(metodo1())
elif opcao == 2:
    print(metodo2())
else:
    print('Opção invalida')

sleep(1)
input('pressione ENTER para sair...')
sleep(3)