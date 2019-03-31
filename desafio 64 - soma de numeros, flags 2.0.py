c = s = i = 0
while True:
    i = int(input("Número: (999 para sair) "))
    if i == 999:
        break
    s += i
    c += 1
print(f"a quantidade foi de {c}, a soma dos numeros foi de {s}")