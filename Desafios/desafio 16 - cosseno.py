import math

x = float(input('Digite o cateto oposto! '))
y = float(input('Digite o cateto adjacente: '))

h = x**2+y**2
seno = x/h
cosseno = y/h
tg = x/y

print('o seno é: {:.1}, o consseno é {:.1}, o tangente é: {:.1}'.format(seno, cosseno, tg))
