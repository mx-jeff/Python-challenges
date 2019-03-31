print("\33[30m=" * 20, "DESAFIO 50 - NÚMEROS PRIMOS", "=\33[m" * 20)

num = int(input("Digite um número: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print(f'{c} ', end='')
print(f'\n\33[mO número {num} foi divísivel {tot} vezes')
if tot == 2:
    print('E por isso ELE É PRIMO')
else:
    print('por isso ele NÃO É PRIMO')