import random

#tabela
print("{:-^40}".format("JO KEN PÔ"))
print(''' Suas opções:
    [0] pedra
    [1] papel
    [2] tesoura
''')

#entrada
item = ['PAPEL', 'PEDRA', 'TESOURA']

você = int(input('Escolha a sua opção: '))
computer = random.randint(0, 2)

print('Computador escolheu \33[1;30m{}\33[m'.format(item[computer]))
print('Você escolheu: \33[1;36m{}\33[m'.format(item[você]))

vitoria = computer - você

if vitoria == 0:
    print('\33[1;30mEMPATE')
elif vitoria == 1:
    print('\33[1;33mVITÓRIA')
elif vitoria == 2:
    print('\33[1;31mDERROTA')
elif vitoria == -1:
    print("\33[1;31mDERROTA")
elif vitoria == -2:
    print("\33[1;33mVITÓRIA")
else:
    print('Jogada anulada!')





