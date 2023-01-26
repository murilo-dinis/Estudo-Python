'''
def funcao(var):
    return var
    

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor')

'''

'''
def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8, -1)
if divide:
    print(divide)
else:
    print('Inválido.')
'''
'''
def dumb():
    return [1,2,3,4,5]

var = dumb()
print(var, type(dumb()))
'''
'''
def f(var):
    print(var)

def dumb():
    return f

var = dumb()('Colocar o valor aqui.')
'''