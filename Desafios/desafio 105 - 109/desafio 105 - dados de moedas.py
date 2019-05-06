import moeda

preco = float(input("Digite o seu preço: "))

print(f' A metade de {preco} é {moeda.metade(preco)}')
print(f' O dobro de {preco} é {moeda.dobro(preco)}')
print(f' 10% de aumento {preco} é de {moeda.aumentar(preco, 10)}')
print(f' 10% de redução {preco} é de {moeda.diminuir(preco, 10)}')
