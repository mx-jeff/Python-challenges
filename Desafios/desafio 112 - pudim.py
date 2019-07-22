import requests

cores = {
    'limpa': '\33[m',
    'vermelho': '\33[1;31m',
    'azul': '\33[1;34m'
}

erro = cores['vermelho']
ok = cores['azul']
limpa = cores['limpa']


def check_connection(url='http://www.google.com.br'):
    try:
        request = requests.get(url)

    except:
        print(f'{erro} [ERRO] falha na conexão! {url} não funciona :( {limpa}')

    else:
        if request.status_code == 200:
            print(f'{ok}[SUCESSO] \n webpage {url} funcionando :) {limpa}')

        else:
            print(f'{erro}[ERRO] conexão não estabeçecida :( verifique a url e tente novamente! {limpa}')


def main():
    check_connection('http://www.pudim.com.br/')


if __name__ == '__main__':
    main()
