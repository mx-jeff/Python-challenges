from time import sleep
print("=" * 10, 'DESAFIO 57 - CALCURADORA PROTOTIPO', "=" * 10)

def metodo1():
    while True:
        n1 = int(input('Digite o 1º numero: '))
        n2 = int(input('Digite o 2º número: '))

        print(''' Escolha a a operação desejada:
            [1] = adição
            [2] = multiplicação
            [3] = maior
            [4] = adicionar novos números
            [5] = sair do programa
        ''')

        opcao = int(input('Opção: '))
        print('processando...')
        sleep(0.5)
        if opcao == 1:
            r1 = n1 + n2
            print(f'O Resultado é: {r1}')
        elif opcao == 2:
            r2 = n1 * n2
            print(f'O resultado é: {r2}')
        elif opcao == 3:
            if n1 > n2:
                print(f'O {n1} número é maior')
            else:
                print(f'O {n2} numero é maior')
        elif opcao == 4:
            print('processando...')
            sleep(1)
        elif opcao == 5:
            exit()
        else:
            print('opção invalida tente novamente')


def metodo2():
    n1 = int(input('1º numero: '))
    n2 = int(input('2° numero: '))
    opcao = 0
    while opcao != 5:
        print('''
        [1] somar
        [2] multiplicar
        [3] maior
        [4] mais números
        [5] sair do programa        
        ''')
        opcao = int(input('Qual é a sua opção: '))

        if opcao == 1:
            soma = n1 + n2
            print(f'A a soma é: {soma}')
            print('=*' * 20)
        elif opcao == 2:
            produto = n1 * n2
            print(f'A multiplicação é: {produto}')
            print('=*' * 20)
        elif opcao == 3:
            if n1 > n2:
                print(f'O {n1} número é maior')
            else:
                print(f'O {n2} numero é maior')
            print('=*' * 20)
        elif opcao == 4:
            print('Informe os números novamente')
            n1 = int(input('1° número'))
            n2 = int(input('2º número'))
            print('=*' * 20)
        elif opcao == 5:
            print('Finalizando...')
        else:
            print('opção invalida, tente novamente')
        sleep(2)
    print('Fim do programa, volte sempre!')

metodo1()