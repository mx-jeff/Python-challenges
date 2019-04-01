print('=-'*20, 'DESAFIO 80 - LISTA ORDENADA', '=-'*20)

lista = []
for contador in range(0, 5):
    numero = int(input('Numero: '))
    #se for o primeiro valor da lista e o ultimo
    if contador == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista...')
    # descobrir o valor do meio
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1

    print('-='*30)
    print(f'Os valores digitados em ordem {lista}')