print('x=' * 20, 'DESAFIO 82 - LISTAGEM DE PESOS', 'x=' * 20)


def meu():
    total = 0
    pessoas = []
    while True:
        pessoa = str(input('Digite o nome da pessoa: '))
        peso = float(input('Digite o peso da pessoa: '))
        pessoas.append(pessoa)
        pessoas.append(peso)
        continua = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
        if continua == 'N':
            break

    print(f'A lista de pessoas é: {len(pessoas)}')
    print(f'A pessoa mais pesada é {max(pessoas)} ')
    print(f'A pessoa mais leve é {min(pessoas)}')
    print(f'O total é de {total} pessoas')


def cursoEmVideo():
    temp = []
    princ = []
    mai = men = 0
    while True:
        temp.append(str(input('Nome: ')))
        temp.append(float(input('Peso: ')))
        if len(princ) == 0:
            mai = men = temp[1]
        else:
            if temp[1] > mai:
                mai = temp[1]
            if temp[1] < men:
                men = temp[1]
        princ.append(temp[:])
        temp.clear()
        resp = str(input('Você deseja continuar? [S/N] '))
        if resp in 'Nn':
            break

    print('-=' * 30)
    print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
    print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
    for p in princ:
        if p[1] == mai:
            print(f'{p[0]} ', end='')
    print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')
    for p in princ:
        if p[1] == men:
            print(f'{p[0]} ', end='')


cursoEmVideo()
