#layout


def titulo(msg):
    tamanho = len(msg) + 4
    print('-' * tamanho * 2)
    print(msg.center(40))
    print('-' * tamanho * 2)


def options():
    opcoes = ['Ver pessoas cadastradas', 'Cadastrar pessoas novas', 'Deletar cadastro', 'Sair do sistema']
    for lista, opcao in enumerate(opcoes):
        print(f"{lista+1} - {opcao}")


def linhas(linhas=40):
    print(f'-' * linhas)