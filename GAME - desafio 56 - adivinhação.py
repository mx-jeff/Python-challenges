from random import randint
from time import sleep
print('x~' * 10, 'GAME - DESAFIO 56 - adivinhação 2.0', '~x' * 10)

adversario = randint(0, 10)

print(f'Sou seu PC... Acabei de pensar em um número de 1 a 10')
sleep(1)
print('Será que você consegue adivinhar o me número?')
acertou = False
palpite = 0
while not acertou:
    voce = int(input('Digite o seu número: '))
    palpite += 1
    if voce == adversario:
        acertou = True
    else:
        if voce < adversario:
            print('Mais...Tende denovo!')
        elif voce > adversario:
            print('Menos...tente mais uma vez!')
print('Acertou!')
print(f'em {palpite} palpites')