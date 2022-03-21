import math  # Modulo para usar função Square Root
import os  # Para "Pausar" quando o programa for finalizado.

# Introdução da Calculadora
print('Bem Vindo a Calculadora Básica')
print('Primeiro digite o tipo de operação, Usando os números indicados!')
print('1 - Operações Básicas(Multiplicação, Divisão, Adição, Subtração)\n2 - Potenciação\n3 - Raíz Quadrada')

# Váriavel Global, Criada para lidar com erros usando loops while.
asking = True

# Funções
# Raiz Quadrada
def raizq(n1):
    """ Usa o módulo math para retornar a raíz quadrada do número indicado """
    nf = math.sqrt(n1)
    return ('A Raiz quadrada é ' + str(nf))

# Potenciação
def pot(n, p):
    """ Simplesmente retorna a potência de um número indicado. Usando um expoente indicado também """
    return (f'{n}^{p} = {n ** p}')

# Calculos Básicos
def calc(a, b, op):
    """ Checa se a pessoa colocou o operador correto e faz a operação indicada. """
    if op not in '*/+-':
        return "Alguma coisa está errada, certifique-se que digitou o operador correto.(*, /, +, -)"
    if op == '*':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))
    if op == '+':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))

# Função Principal
def main():
    while asking:
        type1 = input('O que você gostaria de fazer? ').lower()
        if type1 not in '1 2 3':
            print('Você não digitou o tipo certo, tente novamente!')
            continue
        else:
            break

    if type1.startswith('1'):
        while asking:
            try:
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
                op = input("Que tipo de operador gostaria de usar? (*, /, +, -) ")
            except:
                print('Você digitou alguma coisa errada, tente novamente!')
                continue
            else:
                break
        print(calc(n1, n2, op))

    if type1.startswith('2'):
        while asking:
            try:
                n = int(input('Digita um número base inteiro: '))
                p = int(input('Digite um número expoente inteiro: '))
            except:
                print('Isto não é um número inteiro!')
                continue
            else:
                break
        print(pot(n, p))

    if type1.startswith('3'):
        while asking:
            try:
                n1 = float(input('Digite o número do qual você que saber a raiz quadrada: '))
            except:
                print('Você não digitou um número, tente novamente! ')
                continue
            else:
                break
        print(raizq(n1))

if __name__ == '__main__':
    main()

os.system("pause")
