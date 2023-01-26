'''
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

var = func(1,2,3,4,5, nome='Murilo', a6='5')
print(var[0], var[1])
'''
'''
def func(*args):
    print(args)

lista = [1,2,3,4,5]
print(*lista, sep='-')
'''
'''
def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1,2,3,4,5)
'''
'''
def func(*args):
    args = list(args)
    args[0] = 20
    print(args)

func(1,2,3,4,5)
'''
'''
def func(*args, **kwargs):
    print(args)
    
    nome = kwargs.get('nome')
    print(nome)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Murilo', sobrenome = 'Alvarenga')
'''