import random

a = str(input('Digite o nome do aluno: '))
b = str(input('O nome do aluno: '))
c = str(input('O nome do aluno: '))
d = str(input('O nome do aluno: '))

lista = [a,b,c,d]

r = random.choice(lista)

print('o escolhido é {}'.format(r))