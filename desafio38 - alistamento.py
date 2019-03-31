from datetime import date
cores = {
    'limpa': '\33[m',
    'branco': '\33[m'
}

print('xY' * 20, 'ALISTE-SE JÁ!!!', 'xY' * 20)

ano = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade == 18:
    print("nascidos em {}, que possuem {} anos tem que se alistar agora".format(ano, idade))
elif idade <= 18:
    saldo = 18 - idade
    print('nascidos em {}, que possuem {} anos ja chegarão no tempo de alistamento, faltam {} anos'.format(ano, idade, saldo))
elif idade >= 18:
    saldo = idade - 18
    print('nascidos em {}, que possuem {} anos ja passaram do tempo de alistamento, em {} anos'.format(ano , idade, saldo))
