try:
    print("=" * 20, "DESAFIO 49 - PROGRESSÃO ARITMÉTICA!", "=" * 20)

    primeiro = int(input("1 Termo: "))
    razao = int(input("Razão: "))
    decimo = primeiro + (10 - 1) * razao

    for c in range(primeiro, decimo + razao, razao):
        print(f"{c} ", end=" > ")
    print("ACABOU")

except ValueError:
    print('\33[1;41m Caracter invalido! \33[m')
