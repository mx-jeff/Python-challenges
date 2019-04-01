from time import sleep
from datetime import datetime

print('=' * 20,'DESAFIO 91 - DADOS CADASTRAIS', '=' * 20)

cadastro = dict()

def dados(cadastro):

    anoAtual = datetime.now().year

    def idade(anoAtual, anoContratado):
        return anoAtual - anoContratado

    def contribuicao(ano, idade):
        anosContribuicao = 35
        return (ano + anosContribuicao) - idade

    cadastro['nome'] = str(input('Nome: '))
    cadastro['ano'] = int(input('Ano de nascimento: '))
    cadastro['idade'] = idade(anoAtual, cadastro['ano'])
    cadastro['CLT'] = int(input('Carteira de trabalho: '))

    if cadastro['CLT'] != 0:
        cadastro['contratação'] = int(input('Ano de contratação: '))
        cadastro['salario'] = float(input('Salário: '))
        cadastro['aposento'] = contribuicao(cadastro['contratação'], anoAtual)


def dadosSaida(cadastro):
    print('-='*60)
    for k, v in cadastro.items():
        print(f' - {k} tem o valor {v}')
        sleep(1)


def dadosTrabalhistas():
    dados(cadastro)
    dadosSaida(cadastro)

dadosTrabalhistas()