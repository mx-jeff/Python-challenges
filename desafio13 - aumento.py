salario = float(input('insira seu salario: '))

aumento = (salario * 15)/100
total = salario + aumento
print('O aumento no salario será de {:.5}\n O seu novo salario será de {:.5}'.format(aumento,total))