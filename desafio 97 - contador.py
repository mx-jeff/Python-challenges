from time import sleep

print('-=' * 20, 'DESAFIO 97 - CONTADORES', '=-' * 20)


def linhas(linha):
    print('-' * linha)


def titulo(msg):
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)


def contador(inicio, fim, passo):

    if inicio < fim:

        c = inicio
        while c <= fim:
            print(f'{c} ', end='')
            sleep(0.5)
            c += passo
        print('FIM!')

    else:
        c = inicio
        while c >= fim:
            print(f'{c} ', end='')
            sleep(0.5)
            c -= passo
        print('FIM!')


linhas(25)
titulo('Contador tradicional')
linhas(25)
sleep(1)
contador(1, 10, 1)
linhas(25)

titulo('Contador reverso')
sleep(1)
linhas(20)
contador(10, 0, 2)
linhas(20)
sleep(3)

print('Sua vez de personalizar a contagem:')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Nº de pulos? '))

linhas(20)
contador(inicio, fim, passo)
linhas(20)