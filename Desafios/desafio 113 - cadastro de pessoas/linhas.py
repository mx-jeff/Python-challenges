#layout


def titulo(msg):
    tamanho = len(msg) + 4
    print('-' * tamanho)
    print(f'  {msg}')
    print('-' * tamanho)


def options():
    print('''1 - Ver pessoas cadastradas
2 - Cadastrar pessoas novas
3 - Deletar cadastro
4 - Sair do sistema
    ''')


def linhas():
    print(f'-' * 40)