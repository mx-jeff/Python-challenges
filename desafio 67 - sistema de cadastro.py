from time import sleep

print('='*20, 'DESAFIO 67', '='*20)

def metodo1():
    cores = {
        'limpa': '\33[m',
        'branco': '\33[1:30m',
        'roxo': '\33[35m'
    }
    dezoito = masculino = feminino = 0

    while True:
        nome = str(input("Nome: ")).strip()
        idade = int(input("Idade: "))
        sexo = str(input("Sexo: [M/F]")).upper()
        stay = str(input("Você quer continuar? [S/N]")).upper()

        if idade > 18:
            dezoito += 1

        if sexo == 'M':
            masculino += 1

        if sexo == 'F':
            feminino += 1

        if stay == 'N':
            break

    print("processando...")
    sleep(0.5)
    print(f"Tem {cores['branco']}{dezoito}{cores['limpa']} pessoas maiores de 18 anos")
    print(f"{masculino} homens foram cadastrados")
    print(f"{feminino} mulheres foram cadastradas")
    input("Digite ENTER para sair...")

def metodo2():
    c18 = cm = cf = 0
    while True:

        idade = int(input("Idade: "))
        if idade > 18:
            c18 += 1

        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input("sexo: [M/F] ")).upper().strip()[0]

        if sexo == 'M':
            cm += 1

        elif sexo == 'F' and idade < 20:
            cf += 1

        resp = ' '
        while resp not in 'SN':
            resp = str(input("Você quer continuar? [S/N]")).strip().upper()[0]

        if resp == 'N':
            break

    print('=' * 20)
    sleep(1)
    print(f"o total de pessoas de maiores de 18 anos foi? {c18}")
    sleep(1)
    print('='*20)
    print(f"O total de homens foi: {cm}")
    sleep(1)
    print('=' * 20)
    sleep(1)
    print(f"O total de mulheres com menos de 20 anos {cf} ")
    print('=' * 20)

metodo2()