from time import sleep
print("="*20,"DESAFIO 69 - LISTA DE COMPRAS","="*20)
def metodo1():
    total = mil = 0
    while True:
        nome = str(input("Nome do produto: "))
        preco = float(input("Preço do produto: R$"))
        total += preco
        continua = str(input("Você quer continuar? [S/N]")).strip().upper()[0]
        if continua == 'N':
            break

        if preco > 1.000:
            mil += 1

    print(f'O total dos produtos foram de total: {total}')
    print(f"Numero de produtos que passam da faixa dos mil reais: {mil}")

def metodo2():
    total = totmil = contador = menor = 0
    while True:
        produto = str(input("Nome do produto: "))
        preço = float(input("Preço do produto: R$"))
        total += preço
        contador += 1
        resp = ' '

        while resp not in 'SN':
            resp = str(input("Você quer continuar? [S/N]")).strip().upper()[0]

        if resp == 'N':
            break

        if preço > 1000:
            totmil += 1

        if contador == 1:
            menor = preço
        else:
            if preço < menor:
                menor = preço


    print('{:-^40}'.format('RESULTADOS:'))
    sleep(3)
    print(f'O total da compra foi R${total:.2f}')
    print('-=' * 20)
    sleep(3)
    print(f'Temos {totmil} produtos com mais de R$1000,00')
    print('-=' * 20)
    sleep(3)
    print(f'O menor preço do produto é de R${menor:.2f}')
    print('-=' * 20)

metodo2()