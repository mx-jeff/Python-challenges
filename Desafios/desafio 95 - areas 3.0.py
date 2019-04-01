print('=' * 40, 'DESAFIO 95 - ÁREA 3.0', '=' * 40)


def titulo(titulo, linha):
    print('-' * 40)
    print(' ' * linha, f"{str(titulo)}")
    print('-' * 40)


def cacularArea(comprimento, largura):
    area = comprimento * largura
    return area


titulo('appEnginer', 15)
print('Bem vindo appEnginer, por favor informe a largura e o comprimento que calcularemos a área :) ')
print('Largura(m) ')
largura = float(input('$ '))
print('Comprimento(m) ')
comprimento = float(input('$ '))

titulo('resultados', 15)
print(f'A area total é de {cacularArea(comprimento, largura)}')

