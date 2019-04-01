from time import sleep

while True:
    print("DESAFIO 61 - GERENCIADOR DE NÚMEROS")

    def metodo1():
        n = total = cont = 0
        while n != 999:
            n = int(input('Digite um número inteiro (ou 999 para parar): '))
            total += n
            cont += 1
        sleep(1)
        print(f"Foram Digitados {cont} números e a soma foi {total}")

    def metodo2():

        num = s = c = 0
        num = int(input("Digite o numero: "))
        while num != 999:
            c += 1
            s += num
            num = int(input("Digite o numero: "))
        print(f"você digitou {c} numeros, e a soma foi {s}")
        sleep(1)
        print("ACABOU!!!")

    print('''Digite um método:
    [1] = metodo personalizado
    [2] = metodo acadêmico
    [3] = sair''')
    opcao = int(input("Digite uma opção: "))
    print("^º" * 20)

    if opcao == 1:
        metodo1()
    elif opcao == 2:
        metodo2()
    elif opcao == 3:
        break
    else:
        print("valor invalido!")