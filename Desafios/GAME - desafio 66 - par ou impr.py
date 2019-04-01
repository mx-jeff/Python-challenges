from random import randint

print("="*20)
print("GAME - PÁR OU IMPAR 2.0")
print("="*20)

v = 0
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0,11)
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou impar? [P/I] ")).strip().upper()[0]
    total = jogador + computador
    print(f"Você jogou {jogador} e o computador {computador}. total de {total}")
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print("Você perdeu!")
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER, Você venceu {v} vezes.")
