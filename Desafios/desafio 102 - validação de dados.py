print('=' * 20, 'DESAFIO 102 - VALIDAÇÃO DE NUMEROS', '=' * 20 )


def leiaInt(msg):
        ok = False

        valor = 0
        while True:
                n = str(input(msg))
                if n.isnumeric():
                        valor = int(n)
                        ok = True
                else:
                        print('\33[0;31m ERROR 404! \033[m')

                if ok:
                        break
        return valor


numero = leiaInt("Digite um numero: ")
print(f'Você digitou número {numero}')
print('=' * 20)
