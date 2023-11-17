from operacoes import soma, subtracao, multiplicacao, divisao, potenciacao, raiz_quadrada, logaritmo

def menu_principal ():
    print ('Selecione a opção desejada:')
    print ('1 - Para Soma')
    print ('2 - Para Subtração')
    print ('3 - Para Multiplicação')
    print ('4 - Para Divisão')
    print ('5 - Para Potenciação')
    print ('6 - Para Raiz Quadrada')
    print ('7 - Para Logaritmo')
    opcoes = float(input('Digite a opção desejada: '))
    return opcoes