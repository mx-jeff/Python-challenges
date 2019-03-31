print('-' * 10, 'DESAFIO 55 - CONFIRMAÇÃO DE SEXO', '-' * 10)


def metodo1():
    r = ''
    #resposta = ''
    while r != 'MF':
        r = str(input('Qual o seu sexo? [F/M] ')).upper()
    #      if r == 'M':
    #           resposta = 'masculino'
    #      elif r == 'F':
    #         resposta = 'feminino'
    print(f'seu sexo é {r}')


def metodo2():
    resposta = ''
    sexo = str(input('Digite o seu sexo: [F/M] ')).strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Opção invalidade, por favor digite novamente! ')).strip().upper()[0]
    print(f'Sexo {sexo} registrado com sucesso')


print(''' Escolha uma opção:
    [1] metodo1 - customizado
    [2] metodo2 - tradicional
''')

c = int(input('Opção: '))

if c == 1:
    metodo1()
elif c == 2:
    metodo2()
