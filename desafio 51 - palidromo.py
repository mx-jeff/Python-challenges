print('='*20, 'EXERCICIO 51 - PALÍDROMO','='*20)

def metodo1():
    frase = input("Qual a frase? ").upper().replace(" ", "")

    if frase == frase[::-1]:
        print("A frase é um palíndromo")
    else:
        print('A frase não é um palidromo')



def metodo2():
    frase = str(input('Digite uma frase: '))
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    for letra in range(len(junto) -1, -1, -1):
        inverso += junto[letra]
    print(f'O inverso de {junto} é {inverso}')
    if inverso == junto:
        print('temos um PALÍDROMO')
    else:
        print('Não é um PALìDROMO')

print(metodo2())