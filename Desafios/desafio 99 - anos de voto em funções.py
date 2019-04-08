from time import sleep

def titulo(msg):
    tam = len(msg)
    print('=' * tam, f'{msg}', '=' * tam)


def voto(ano):
    from datetime import date

    atual = date.today().year
    idade = atual - ano
    
    print(f'Sua idade é de {idade} anos')
    sleep(1)
    if idade <= 16:
        print('Voto negado!')

    elif 16 <= idade <= 65:
        print('Pode votar!')
    else:
        print('voto opcional!')


titulo('Desafio 99, votos em funções')

#idade = int(input('Sua idade: '))
voto(2010)
input('Digite Enter para sair...')
