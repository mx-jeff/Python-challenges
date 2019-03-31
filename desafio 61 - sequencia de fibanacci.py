from time import sleep
print("=*" * 10, "SEQUENCIA DE FIBANACCI", "=*" * 10)

n = int(input("Digite um numero: "))
t1 = 0
t2 = 1
print("~*" * 35)
print(f"{t1} - {t2}", end="")
c = 3

while c <= n:
    t3 = t1 + t2
    print(f" {t3} - ", end="")
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
