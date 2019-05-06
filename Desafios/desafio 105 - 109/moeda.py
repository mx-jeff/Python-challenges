# mostragem de dinheiro


def aumentar(preco, taxa):
    resultado = preco + (preco * taxa / 100)
    return resultado


def diminuir(preco, taxa):
    resultado = preco - (preco * taxa / 100)
    return resultado


def dobro(moeda):
    resultado = moeda * 2
    return resultado


def metade(moeda):
    resultado = moeda / 2
    return resultado


def real(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
