print('=' * 20, "DESAFIO 103 - NOTAS")


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

