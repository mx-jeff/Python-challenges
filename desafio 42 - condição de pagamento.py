print('{:=^40}'.format('MX SERVIÇOS LMTA'))

preco = float(input('Qual é preço do produto? '))
print('''Condição de pagamento:

   [ 1 ]- vista no cartão
   [ 2 ]- 2 x no cartão
   [ 3 ]- 3 x no cartão, com 20% de juros
''')
condicao = int(input('Qual é a condição de pagamento? '))

if condicao == 1:
    desconto = preco * ( 10 / 100)
    total =  preco - desconto
    print('O desconto é de {:.2f}, que será o valor de {:.2f} '.format(desconto, total))

elif condicao == 2:
    parcela2 = preco / 2
    print('As parcelas serão de {}'.format(parcela2))
elif condicao == 3:
    parcela3 = preco / 3
    juros = preco * 0.020 * 3
    total2 = parcela3 + juros
    print('com as parcelas de R${:.2f}, será adicionado R${:.2f} de juros'.format(parcela3, juros), end=" ")
    print('no total de R${:.2f}'.format(total2))