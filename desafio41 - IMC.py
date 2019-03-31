print('*='*20)
print('ANALISE IMC CORPORAL')
print('*='*20)

peso = float(input('Qual é a seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso/(altura**2)

print("Seu IMC é de {:.1f}".format(imc))
if imc <= 18.5:
    print('\33[30mVocê esta abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Você esta no peso ideal')
elif imc >= 25 and imc <= 30:
    print('\33[33mVocê esta gordo!')
elif imc >= 30 and imc <= 40:
    print('\33[4;33mVocê tem OBESIDADE!')
else:
    print('\33[1;31mVocê tem OBESIDADE MORBIDA!')