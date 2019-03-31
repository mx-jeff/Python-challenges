from math import factorial
print('=-' * 10, 'DESAFIO 58 - FATORIAIS' , '=-' * 20)

def simples():
    n = int(input('Digite um número: '))
    f = factorial(n)

    print(f'o fatorial de {n} é {f}')

def metodo1():
    n = int(input('Digite um número: '))
    c = n
    f = 1 # multiplicação limpa
    print(f'Calculando {n}! = ', end='')
    while c > 0:
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c
        c -= 1
    print(f'o fatorial de {n} é {f}')

metodo1()