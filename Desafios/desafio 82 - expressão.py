print('-'*20, 'DESAFIO 82 - VALIDADOR DE EXPRESSÃO','-'*20)

def teste():
    lista = [str(input('Expressão:'))]
    F = V = 0
    for palavra in lista:
        for letra in palavra:
            if letra.count('(') and letra.count('[') and letra.count('{'):
                V += 1
            elif letra.count(')') and letra.count(']') and letra.count(']'):
                F += 1

    if F == V:
        print('Expressão correta!')
    else:
        print('Expressão errada!')



def cursoEmVideo():
    expr = str(input('Expressão: '))
    pilha = []
    for simbolo in expr:
        if simbolo == '(':
            pilha.append('(')
        elif simbolo == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break

    #verificar
    if len(pilha) == 0:
        print('Sua expressão esta certa!')
    else:
        print('Sua expressão esta errada!')


teste()