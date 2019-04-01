print("Aumento de salários")

salario = float(input("Digite seu salário: R$ "))

print("verificando o seu aumento, por favor aguarde...")

if salario >= 1250.00:
    a1 = salario + (salario * 10 / 100)
    print("seu salario é de {}".format(a1))
else:
    a2 = salario + (salario * 15 / 100)
    print("seu salário é de {}".format(a2))