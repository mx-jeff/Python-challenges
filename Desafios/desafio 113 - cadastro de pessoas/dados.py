from time import sleep
from linhas import titulo
#Dados em arquivos

note = 'pessoas.txt'


def cadastrar():
    try:
        cadastro = open(note, "a")
        nome = str(input('nome: '))
        idade = int(input('Idade: '))
        cadastro.write(f'\n{nome} \t\t{idade} Anos')
        print('Feito!')
        sleep(1.5)
        cadastro.close()
        
    except Exception as error:
        print('Formato invalido, tente novamente')


def exibir():
    try:
        leitura = open(note, 'r')

    except FileNotFoundError:
        print('Arquivo vazio :(')
        sleep(2)

    else:
        print(leitura.read())
        leitura.close()
        sleep(3)


def excluir():
    import os
    if os.path.exists(note):
        os.remove(note)
        titulo('Deletado com sucesso!')
        sleep(2)

    else:
        print('[ERRO] Pasta não existe ou ação cancelada')
        sleep(2)
