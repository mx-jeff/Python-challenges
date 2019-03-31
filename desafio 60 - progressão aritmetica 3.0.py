print("=" * 20, "DESAFIO 60 - PROGRESSÃO ARITMÉTICA 2.0", "=" * 20)

primeiro = int(input('!ºtermo: '))
razao = int(input('Razão: '))
c = 1
termo = primeiro
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} > ', end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos teros você quer adicionar? '))
print(f'A progressão finalizada com {total} termos')