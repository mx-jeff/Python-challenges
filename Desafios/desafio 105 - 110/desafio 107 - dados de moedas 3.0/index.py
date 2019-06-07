import moeda
from time import sleep

while True:
    print("""bem vindo ao console principal!
        --start para iniciar a contagem de preços 
        --help para ajuda  
        --exit para sair
    """)
    menu = str(input('=> '))

    if menu == '--help':
        helper = str(input('Sua duvida: '))
        print('processando...')
        sleep(2)
        help(helper)
        sleep(3)

    elif menu == '--exit':
        break

    elif menu == '--start':

        preco = 0
        while preco != 999:
            print('-' * 60)
            print("Bem vindo! (Digite 999 para sair)")
            preco = float(input("Digite o seu preço: "))

            print(f' A metade de {moeda.real(preco)} é {(moeda.metade(preco, True))}')
            print(f' O dobro de {moeda.real(preco)} é {moeda.dobro(preco, True)}')
            print(f' 10% de aumento {moeda.real(preco)} é de {moeda.aumentar(preco, 10, True)}')
            print(f' 10% de redução {moeda.real(preco)} é de {moeda.diminuir(preco, 10, True)}')