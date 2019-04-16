print('=' * 20, "DESAFIO 103 - NOTAS")


def notas(*nota):
    respostas = {}
    respostas['total'] = len(nota)
    respostas['maior'] = max(nota)
    respostas['menor'] = min(nota)
    respostas['media'] = sum(nota) / len(nota)
    if respostas['media'] >= 7:
        respostas['situacao'] = 'Aprovado'
    else:
        respostas['situacao'] = 'Reprovado'

    return respostas


resposta = notas(7, 7, 7, 7)
print(resposta)

