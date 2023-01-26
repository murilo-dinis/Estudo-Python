'''
Argumentos nomeados e não nomeados
'''

#def soma(x, y):
#    print(f'{x=} y={y}', '|', 'x + y =', x + y)

#soma(1, 2)
#soma(y=2, x=1)

'''
valores padrão para parâmetro em funções Python + NoneType e None
'''

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1,2)
soma(3,5)
soma(100,200)
soma(7, 9, 0)