print('=*' * 10, 'DESAFIO 54 - ANALISADOR', '=*' * 10)

def metodo1():
    nomes = []  # Armazena os nomes das pessoas
    idades = []  # Armazena as idades das pessoas
    sexos = []  # Armazena os sexos das pessoas
    soma = 0  # Soma as idades das pessoas
    maisVelho = 0  # Armazena a idade do homem mais velho
    nomeM = ''  # Concatena nome e idade do homem mais velho
    mSub20 = 0  # Armazena a quantidade de mulheres com idades abaixo de 20 anos
    nomeF = ''  # Concatena nome e idade das mulheres abaixo de 20 anos

    for i in range(0, 4):
        print(str(i + 1) + 'ª' + ' pessoa: ')
        nomes.append(input('Nome: ').capitalize())
        idades.append(int(input('Idade: ')))
        sexos.append(input('Sexo(M/F): ').upper())
        soma += idades[i]
        if sexos[i] == 'F' and idades[i] < 20:
            nomeF += nomes[i] + ',' + str(idades[i]) + ' anos; '
            mSub20 += 1

    for i in range(0, len(idades)):
        if sexos[i] == 'M' and idades[i] > maisVelho:
            maisVelho = idades[i]
            nomeM = nomes[i]

    print('Média de idade do grupo: {:.2f} anos.'.format(soma / 4))
    print('Homem mais velho: {}, {} anos.'.format(nomeM, maisVelho))
    print('Mulheres acima de 20 anos: {}. {}'.format(mSub20, nomeF))


def metodo2():
    somaIdade = 0
    mediaIdade = 0
    MIH = 0  # maior idade do homem
    NV = ''  # nome mais velho
    mulher20 = 0
    for p in range(1, 5):
        print(f'-------{p}º Pessoa -------')
        nome = str(input('Nome: ')).strip()
        idade = int(input('Idade: '))
        sexo = str(input('Sexo: M/F? ')).strip().upper()
        somaIdade = somaIdade + idade

        if p == 1 and sexo in 'Mm':
            MIH = idade
            NV = nome
        if sexo in 'Mm' and idade > MIH:
            MIH = idade
            MV = nome
        if sexo in 'Ff' and idade < 20:
            mulher20 += 1

    mediaIdade = somaIdade / 4
    print(f'A média de idade do grupo é de {mediaIdade} anos ')
    print(f'O homem mais velho tem {MIH}º anos e se chama {MV}')
    print(f'Tem {mulher20} mulheres abaixo de 20 anos')

metodo2()
