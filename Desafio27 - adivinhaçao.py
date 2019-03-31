import random

print('Teste de adivinhação!!')

teste = random.randint(0, 5)

print('Tente Adivinhar o número de 0 a 5, sera que ganha da maquina?')
adv = int(input('Digite um número de 0 a 5: '))
print('O número é {}'.format(teste))
if adv == teste:
    print('Parabéns!!! Você acertou :)')
else:
    print("Você errou! tente novamente :)")
