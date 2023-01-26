'''
calculadora com python
'''

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro valor: '))
operador = input('Digite um operador: ')

if operador == '+':
    print(numero_1 + numero_1)
elif operador == '-':
    print(numero_1 - numero_2)
elif operador == '*':
    print(numero_1 * numero_2)
elif operador == '/':
    print(numero_1 / numero_2)
else:
    print('você não digitou um operaodr válido.')