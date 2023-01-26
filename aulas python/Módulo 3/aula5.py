'''
exercicios funções
'''
'''
def multiplica(*args):
    total = 1
    for n in args:
        total *= n
    return total


resultado = multiplica(2,5,10)
print(resultado)
'''

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    else:
        return f'{numero} é impar'


    
print(par_impar(2))
print(par_impar(3))