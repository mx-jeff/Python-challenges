print('=' * 20, 'DESAFIO 96 - INPUTS PERSONALIZADOS', '=' * 20)

def escreva(msg):
    tamanho = len(msg) + 4
    print('´' * tamanho)
    print(f'  {msg}')
    print('`' * tamanho)


entrada = str(input('$ '))
escreva(entrada)