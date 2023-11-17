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

def calculadora():
    opcao = menu_principal()

    if opcao == 1:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = soma(a, b)
        print("O resultado da soma é:", resultado)

    elif opcao == 2:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = subtracao(a, b)
        print("O resultado da subtração é:", resultado)

    elif opcao == 3:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = multiplicacao(a, b)
        print("O resultado da multiplicação é:", resultado)

    elif opcao == 4:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = divisao(a, b)
        print("O resultado da divisão é:", resultado)

    elif opcao == 5:
        a = float(input("Digite o número base: "))
        b = float(input("Digite o expoente: "))
        resultado = potenciacao(a, b)
        print("O resultado da potenciação é:", resultado)

    elif opcao == 6:
        a = float(input("Digite o número: "))
        resultado = raiz_quadrada(a)
        print("O resultado da raiz quadrada é:", resultado)

    elif opcao == 7:
        a = float(input("Digite o número: "))
        resultado = logaritmo(a)
        print("O resultado do logaritmo é:", resultado)

    else:
        print("Opção inválida")


if __name__ == '__main__':

    calculadora()