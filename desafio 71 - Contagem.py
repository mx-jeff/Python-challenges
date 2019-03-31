from time import sleep

print("="*20,'DESAFIO 70 - CONTAGEM DE TUPLAS' ,"="*20)

def unfinished():
    while True:
        numero = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinto',
                'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
                'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
                'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove',
                'Vinte'
                )

        while True:
            opcao = int(input("Digite um número de 0 a 20:  "))
            if 0 <= opcao <= 20:
                break
            print('Tente novamente. \n')

        print(f'O numero é {numero[opcao]}')
        continua = str(input('Deseja sair? [S/N]')).upper().strip()[0]
        if continua == 'S':
            break

def oficial():
    cont = ('Zero','Um', 'Dois', 'Tres', 'Quatro', 'Cinto',
        'Seis','Sete','Oito','Nove','Dez',
        'Onze','Doze','Treze','Quatorze','Quinze',
        'Dezesseis','Dezesete','Dezoito','Dezenove',
        'Vinte'
    )

    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tene novamente. ', end='')
    print(f'você digitou o numero: {cont[num]}')

unfinished()