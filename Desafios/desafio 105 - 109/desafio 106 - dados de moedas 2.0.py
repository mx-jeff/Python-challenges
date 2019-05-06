import moeda

preco = float(input("Digite o seu preço: "))

print(f' A metade de {moeda.real(preco)} é {moeda.real(moeda.metade(preco))}')
print(f' O dobro de {moeda.real(preco)} é {moeda.real(moeda.dobro(preco))}')
print(f' 10% de aumento {moeda.real(preco)} é de {moeda.real(moeda.aumentar(preco, 10))}')
print(f' 10% de redução {moeda.real(preco)} é de {moeda.real(moeda.diminuir(preco, 10))}')
