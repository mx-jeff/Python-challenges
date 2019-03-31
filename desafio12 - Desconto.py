print('========================================Desconto=promoção===========================================')

produto = float(input('Digite o preço do produto: '))
desconto = int(input('Digite o desconto que quer inserir: '))

total = (produto * desconto)/100

print('O desconto é: {}'.format(total))