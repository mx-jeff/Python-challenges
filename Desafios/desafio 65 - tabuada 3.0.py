from time import sleep

print("._"*20)
print("DESAFIO 65 - TABUADA 3.0")
print("._"*20)

def teste1():
    c = 0
    while c < 20 + 1:
        print(f'{c}','-> ', end="")
        sleep(0.5)
        c += 1

def teste2():
    while True:
        c = 1
        m = int(input("Qual tabuada você escolhe? "))
        if m < 0:
            break
        print("*=" * 20)
        while c < 10:
            c += 1
            t = c * m
            print(f"{m} x {c} = {t}")
    print("acabou")



teste2()