print('=´¨'*5,"Convensor de numeros", '=´¨'*5)
print("Bem vindo a conversão de numeros, Digite o número a sua escolha\ndepois escolha o método de covensão ")

num = int(input('Digite o número para conversão:'))
print("1 - Binario\n2 - octal\n3 - hexadecimal ")
con = int(input("Digite a opção para conversão: "))

if con == 1:
    print("O número {} Convertido para binário, será de: {:0b}".format(num, num))
elif con == 2:
    print("O número {} convertido para OCTAL, será de: {:0o}".format(num, num))
elif con == 3:
    print("O número {} convertido para HEXADECIMAL, será de: {:0x}".format(num, num))
else:
    print("Opção errada tente novamente")

input("digite ENTER para sair...")

