print("TABELA DE PREÇOS")
km = int(input("Digite a distância da viagem: "))
print("analisando o custo, por favor espere...")
if km <= 200:
    p1 = km * 0.50
    d1 = (km/200)*0.50
    print("o valor da passagem será: R${:.2f}, com o acréscimo de R${:.2f}".format(p1, d1))
else:
    p2 = km *0.45
    d2 = (km/200)*0.50
    print("O valor da passagem sera: R${:.2f}, com o acréscimo de R${:.2f}".format(p2, d2))

input("Digite ENTER para sair...")