# mostragem de dinheiro


def aumentar(preco=0, taxa=0, format=False):
    '''

    => aumento de preços em porcentagens
    :param preco: preço sugerido
    :param taxa: a taxa sugerida
    :param format: formato em valor R$
    :return: a porcetagem emitida
    '''
    resultado = preco + (preco * taxa / 100)
    return resultado if format is False else real(resultado)


def diminuir(preco=0, taxa=0, format=False):
    '''
    => diminuição de preços em porcentagens
    :param preco: preço sugerido
    :param taxa: taca sugerida
    :param format: formato em R$
    :return: a porcentagem emitida
    '''
    resultado = preco - (preco * taxa / 100)
    return resultado if format is False else real(resultado)


def dobro(moeda=0, format=False):
    '''

    => retorna o dobro do valor
    :param moeda:  valor a ser dobrado
    :param format: retorna o valor em R$
    :return: o valor dobrado
    '''
    resultado = moeda * 2
    return resultado if format is False else real(resultado)


def metade(moeda=0, format=True):
    '''
    => retorna a metade do valor
    :param moeda: valor a ser emitido
    :param format: retorna em R$
    :return: retorna a metade o valor emitido
    '''
    resultado = moeda / 2
    return resultado if format is False else real(resultado)


def real(preco=0, moeda='R$'):
    '''

    => formata para o modelo real
    :param preco: valor a ser formatado
    :param moeda: padrão(R$)
    :return: valor formatado em R$
    '''
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxa_de_aumento=10, taxa_de_reducao=10):
    def lin(linhas=30):
        print('-' * linhas)

    lin()
    print('RESUMO DO VALOR'.center(30))
    lin()
    print(f'Preço analisando: \t{real(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_de_aumento}% de aumento: \t{aumentar(preco, taxa_de_aumento, True)}')
    print(f'{taxa_de_reducao}% de redução: \t{diminuir(preco, taxa_de_reducao, True)}')
    lin()
