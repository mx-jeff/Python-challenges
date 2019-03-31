print("=-" * 20, "DESAFIO 76 - VOGAIS EM TUPLAS", "=-" * 20)

lista = (
    'PYTHON', 'VOCAL', 'EMBED','SHOWING', 'FOUR',
    'LIFE','DEATH','DRAGON','FORCE','SNAKE', 'STEALTH',
    'SPEED','CAR', 'END'
)
vogal = ('A', 'E', 'I', 'O', 'U')

def alternativo(lista, vogal):
    for i in range(0, len(lista)):
        print(f'\nNa palavra {lista[i]} temos: ', end='')
        for i in lista[i]:
            if i in vogal:
                print(f'{i}', end='')

def cursoEmVideo(lista, vogal):
    for p in lista:
        print(f'\nNa palavra {p} temos: ', end='')
        for letra in p:
            if letra in vogal:
                print(f'{letra.lower()}', end=' ')

def meuMetodo(lista, vogal):
    for palavra in lista:
        print(f'\nTemos {palavra} em: ', end='')
        for letra in palavra:
            if letra in vogal:
                print(f'{letra}', end='')



#alternativo(lista, vogal)
#cursoEmVideo(lista,vogal)
meuMetodo(lista, vogal)