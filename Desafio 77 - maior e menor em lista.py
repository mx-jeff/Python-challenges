print("=-" * 20, 'DESAFIO 77 maior e menor em lista', "=-" * 20)

numero = []
for c in range(0, 5):
    numero.append(int(input(f'Número {c + 1}: ')))

for cont in numero:
    print(f'{cont} ',end='')

print('\n')
print(f'Sendo o maior {max(numero)}')
print(f'Sendo o menor {min(numero)}')