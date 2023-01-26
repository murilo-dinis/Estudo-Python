'''
retorno de valores das funções
'''

variavel = print('Murilo')
print(variavel)

def soma(x, y):
    ...

variavel = soma(1, 2)
print(variavel)

x, y, *resto = 1, 2, 3, 4


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

soma_4_5_6 = soma(4,5,6)
print(soma_4_5_6)

print(sum((1,2,3,4,5,6,7,78,10)))