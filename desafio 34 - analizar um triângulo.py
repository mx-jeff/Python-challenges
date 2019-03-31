print('-='*20)
print("<--ANALISADOR DE TRIÂNGULOS-->")
print('-='*20)
r1 = float(input("digite o primeiro lado de um triâgulo: "))
r2 = float(input("Digiteo segundo lado de um triângulo: "))
r3 = float(input("Digite o terceiro lado de um triângulo: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO')
else:
    print("Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO")

