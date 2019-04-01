print("=" * 20, "DESAFIO 59 - PROGRESSÃO ARITMÉTICA 2.0", "=" * 20)

primeiro = int(input('!ºtermo: '))
razao = int(input('Razão: '))
c = 1
termo = primeiro
while c <= 10:
    print(f'{termo} > ', end='')
    termo += razao
    c += 1
print('FIM')