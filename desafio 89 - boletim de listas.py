print('-'*20,'DESAFIO 89 - BOLETIM','-' * 20)

aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Media do aluno: '))
print('-='*60)
if aluno['media'] >= 7.0:
    aluno['situação'] = 'Aprovado!'
else:
    aluno['situação'] = 'Reprovado!'

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')