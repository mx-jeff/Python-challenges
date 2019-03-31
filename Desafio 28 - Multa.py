print('<--Calculos-de-multas-->')

vel = float(input('Digite a sua velocidade: '))
print("Sua velocidade é {}Km/h".format(vel))
multa = (vel-80) * 7
if vel > 80:
    print('Você ultrapassou a velocidade permitida!!')
    print('Sua multa é R${:.2f}'.format(multa))
else:
    print("Você está na velocidade limite, parabéns!")