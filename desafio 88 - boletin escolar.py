print('='*20,'DESAFIO 88 - BOLETIM ESCOLAR','='*20)

def meuMetodo():
    cache = []
    aluno = []

    while True:
        print('Digite o nome do aluno: ')
        nome = str(input('-+- '))
        cache.append(nome)

        print('Nota 1')
        n1 = float(input('-+- '))
        cache.append(n1)

        print('Nota 2: ')
        n2 = float(input('-+- '))
        cache.append(n2)

        media = (cache[1]+cache[2])/2

        print('DESEJA CONTINUAR? [S/N]')
        continua = str(input('-+- ')).upper().strip()[0]
        if continua == 'N':
            break

    print(f'as notas são: {cache}')
    print(f'A media é de {media}')

def CursoEmVideo():
    ficha = list()
    while True:

        nome = str(input('Nome: '))
        n1 = int(input('Nota 1: '))
        n2 = int(input('Nome 2: '))
        resp = str(input('Deseja continuar? [S/N]'))

        media = (n1 + n2) / 2
        ficha.append([nome, [n1, n2], media])

        if resp in 'nN':
            break

    print('-=' * 30)
    print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
    print('-'*26)
    for i, a in enumerate(ficha):
        print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
    while True:
        print('-='*40)
        opc = int(input('Selecione Aluno (999 imterrompe): ' + 1))
        if opc == 999:
            break
        if opc <= len(ficha) - 1:
            print(f'Notas {ficha[opc][0]} são {ficha[opc][1]}')
    print('<<< Volte sempre >>>')


CursoEmVideo()