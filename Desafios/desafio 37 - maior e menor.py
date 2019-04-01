print('=*'*20,'comparador de números','=*'*20)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o Segunro número: '))
print("\33[30mAnalisando os números, aguarde...\33[m")

if n1 <= n2:
    print('\33[31mO Primeiro número {} é menor que o Segundo número {}\33[m'.format(n1, n2))
elif n1 >= n2:
    print('\33[33mO primeiro número {} é maior que o segundo número {}\33[m'.format(n1, n2))
elif n1 == n2:
    print("\33[32mO primeiro número: {} e segundo número: {} são iguais\33[m".format(n1, n2))