print("=-" * 20, 'DESAFIO 78 maior e menor em lista 2.0', "=-" * 20)

numero = []
for contador in range(0, 5):
    numero.append(int(input(f'Número {contador + 1}: ')))

for i, cont in enumerate(numero):
    print(f'Na posição {i} temos {numero}')

print('\n')
print(f'Sendo o maior {max(numero)} na posição {numero.index(max(numero + 1))}')
print(f'Sendo o menor {min(numero)} na posição {numero.index(min(numero + 1))}')