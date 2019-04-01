print('-----Expermento de nomes----')

nome = str(input('Digite seu nome Completo: ')).strip()
dividindo = nome.split()
fistname = len(dividindo[0])
print('Seu nome completo é: {}\n em maiuscula {}\n com {} caracteres\n o primeiro nome é {} tem {} caracteres'
      .format(nome, nome.upper(), len(nome)-nome.count(' '), dividindo[0],fistname))