print('=' * 20, "DESAFIO 103 - NOTAS")

def tests():
    def notas(*notas):

        def media(total):
            return (total + total) / 3


        listadenotas = {
            'total': notas,
            'media': media(notas)
        }

        #total = listadenotas['total']

        #listadenotas['media'] = media(total)

        for chave, valor in listadenotas.items():
           print(f'{chave} => {valor}')


    notas(10, 5, 8)


def schatch():

    def media(number1, number2):
        return number1 + number2 / 2

    def aprovacao(situacao):
        if retornamedia >= 7.0:
            situacao = "APROVADO"
        elif retornamedia == 7.0:
            situacao = "Passou perto"
        else:
            situacao = "REPROVADO!"

        return situacao

    nota1 = float(input("notas 1: "))
    nota2 = float(input("notas 2: "))

    retornamedia = media(nota1, nota2)
    sit = aprovacao(retornamedia)
    

    print(f'media: {retornamedia}, situação {sit}')



schatch()

