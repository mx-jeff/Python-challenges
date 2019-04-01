print('Desafio - maior e menor')

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite o ultimo número: "))
# verificar quem é o menor
menor = a
if b < a and c < b:
    menor = b
if c < a and c < b:
    menor = c
print("O menor valor é {}".format(menor))
# verificar o maior
maior = a
if a < b < c:
    maior = b
if c > a and c > b:
    maior = c
print("o maior valor é {}".format(maior))
