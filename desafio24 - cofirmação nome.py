nome = input('Digite seu nome: ').strip().upper()

if(nome.find('SILVA') == -1):
    print("Não tem silva no nome!")
else:
    print("Tem silva no nome!")