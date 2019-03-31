cidade = input("Digite o nome de uma cidade: ").strip()

if(cidade[:5].upper().find('SANTO') == -1):
    print('Não tem santo no nome')
else:
    print('cidade Tem santo no nome')