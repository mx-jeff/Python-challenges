print("=" * 20, "DESAFIO 100 - FATORIAL EM FUNÇÃO", "=" * 20)

def fatorial(numero, show=False):
    """
    -> Calcula o fatorial
    :param numero: numero do fatorial
    :param show: mostra o fatorial completo
    :return: retorna o fatorial
    """
    fatorial = 1
    for contador in range(numero, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(f'{contador} x ', end='')
                
            else:
                print(' = ', end='')
            
        fatorial *= contador
        
    return fatorial

#print(fatorial(5, show=True))
help(fatorial)
