'''
while True:
    nome = input('Qual o seu nome? ')
    print(f'Olá {nome}!')

print('Isso não será executado')
'''
'''
x = 0
while x <= 5:
    print(x)
    x = x + 1

print('Acabou!')
'''
'''
x = 0
while x <= 10:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1

print('Acabou!')
'''
'''
x = 0   # coluna
y = 0   # linha

while x < 10:
    y = 0
    
    while y < 5:
        print(f'({x},{y})')
        y += 1
    
    x += 1    # x = x + 1

print('Acabou!')
'''

'''
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido')

'''

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break
    
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')
print('Cheguei no else.')