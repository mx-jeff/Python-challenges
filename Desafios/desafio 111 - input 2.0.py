print('=' * 20, 'DESAFIO 102 - VALIDAÇÃO DE NUMEROS', '=' * 20)


def leiaInt(msg):

    try:
        numero = int(msg)

    except ValueError:
        print(f'\33[0;31m[ERRO] invalido, numero inteiro necessario!\33[m')

    except KeyboardInterrupt:
        print('Saindo...')

    else:
        return numero


def leiaFloat(num):

    try:
        numero = float(num)

    except ValueError:
        print(f'\33[0;31m[ERRO] invalido, numero inteiro necessario!\33[m')

    except KeyboardInterrupt:
        print('Saindo...')

    else:
        return numero


def validate(numero):
    while True:
        msg = input(numero)
        if leiaFloat(msg) or leiaFloat(msg):
            return msg
        break


def main():

    numero = validate("Digite um numero: ")
    print(f'Você digitou número {numero}')
    print('=' * 20)


if __name__ == '__main__':
    main()
