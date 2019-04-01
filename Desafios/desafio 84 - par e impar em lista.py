print("=" * 20, "DESAFIO 84 - PAR E IMPAR EM LISTA", "=*", 20)

listaDeNumeros = [[], []]
for contador in range(0, 6):
    print(f'Digite o {contador + 1} numero')
    numero = int(input('$: '))

    parOuImpar = numero % 2 == 0
    if parOuImpar:
        listaDeNumeros[0].append(numero)
    else:
        listaDeNumeros[1].append(numero)

print(f'Pares {sorted(listaDeNumeros[0])}')
print(f'Impar {sorted(listaDeNumeros[1])}')
