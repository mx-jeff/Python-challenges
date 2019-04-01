print(";-;!" * 20)
print("~" * 25, "\33[1;36mNIVELADOR DE CATEGORIAS\33[m", "~" * 30)
print(";-;!" * 20)

cores = {
    'limpa':'\33[m',
    'azulclaro':'\33[1;36m',
    'bordazul':'\33[1;30;46'
}

ano = int(input('Insira a asua idade: '))
print("Analisando sua categoria...")
if ano <= 9:
    print("Sua categoria é MIRIN")
elif ano >= 9 and ano <= 14:
    print("Sua Categoria é INFANTIL")
elif ano >= 14 and ano <= 19:
    print("Sua categoria é JUNIOR")
elif ano == 20:
    print("Sua categoria é SENIOR")
elif ano > 20:
    print("sua categoria é MASTER")
