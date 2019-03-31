print('=' * 30, 'DESAFIO 93 - ANALISE DE PESSOAS', '=' * 30)

galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]

        if pessoa['sexo'] in 'MF':
            break
        print('ERROR! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERROR! Responda S ou N')
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastadas.')
media = soma /len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ',end='')
print()
print(f'D) A lista de pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print(f'  ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print('<<< ENCERRADO >>>')