cores = {
    'limpa':'\33[m',
    'negativo':'\33[1,30;43m'
}
print('\33[33m*=\33[m'*51)
print('\33[33m=*\33[m'*20,'Emprestimos Tabajara','\33[33m=*\33[m'*20)
print('\33[33m*=\33[m'*51)

casa = float(input('O valor casa: R$'))
salario = float(input('O valor do seu salário: R$'))
ano = int(input('estimativa de anos necessários para concluir o emprestimo: '))
prestacao = casa /(ano * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos\nA prestação sera de R${:.2f}'.format(casa, ano, prestacao))
if prestacao <= minimo:
    print("o empréstimo pode ser concedido")
else:
    print("O empréstimo negado!")