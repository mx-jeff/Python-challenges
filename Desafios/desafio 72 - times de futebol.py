from time import sleep
print('+x'*10,'(DESAFIO 72 - LISTA DE TIMES DE FUTEBOL)','x+'*10)

times = ('São paulo', 'Corinthians', 'Santos','Palmeiras', 'Grêmio',
         'Internacional', 'Fluminense','Flamengo','Vasco','Nautico')

#print(f'Os times mais colocados são: {times[:5]}')
print('=*' * 20)
print('Os times mais colocados são: \n')
for primeiros in times[:5]:
    sleep(0.5)
    print(primeiros)
print('\n')

print('=*' * 20)
print('Os ultimos times foram: \n')
for ultimos in  times[-4:]:
    sleep(0.5)
    print(ultimos)

print('=*' * 20)
org = sorted(times)
print(f'Os times são: {org} \n')
print('=*' * 20)
print(f'O flamengo esta em: {times.index("Flamengo") + 1}º lugar')