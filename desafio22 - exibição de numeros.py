num = int(input('Insira um numero aqui: '))


uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print('Analisando o {} ...'.format(num))

print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('centena: {}'.format(uni))
print('milhar: {}'.format(mil))

