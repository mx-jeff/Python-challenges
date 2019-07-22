from linhas import titulo, options, linhas
from dados import cadastrar, exibir, excluir


def main():
    while True:
        titulo('menu principal')
        options()
        linhas()
        opcao = int(input('Sua opção: '))

        if opcao == 1:
            print('Aguarde...')
            exibir()

        elif opcao == 2:
            print('Aguarde...')
            cadastrar()

        elif opcao == 3:
            print('Aguarde...')
            excluir()

        elif opcao == 4:
            titulo('Saindo do sistema..até logo!')
            break

        else:
            print('[ERRO] insira uma opção valida!')


if __name__ == '__main__':
    main()
