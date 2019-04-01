print("=*", "DESAFIO 63 - MEDIA REPETIÇÃO", "=*")

resp = "S"
media = quant = soma = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / quant
print(f"Você digitou {quant} números, e a media foi {media}, o maior é {maior} e o menor é {menor}")

