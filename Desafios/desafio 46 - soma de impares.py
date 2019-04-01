soma = 0
c = 0
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        c = c + 1
        soma = soma + contador
print(f"A soma dos {c} os valores é de {soma}")