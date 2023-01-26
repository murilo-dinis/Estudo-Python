'''
função lambda
'''

# lista = [4, 32, 1, 34, 5, 6, 6, 21]
# lista.sort(reverse=True) #.sort ordena a lista


# print(lista)
'''
lista = [
    {'nome': 'Murilo', 'sobrenome': 'alvarenga'},
    {'nome': 'maria', 'sobrenome': 'fernanda'},
    {'nome': 'gabriel', 'sobrenome': 'sette'},
    {'nome': 'eduardo', 'sobrenome': 'moreira'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()


# lista.sort(key=lambda item: item['nome'])
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)

'''

def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n*m,
    2
)
print(duplica(2))

# print(
#     executa(
#         lambda x, y: x + y,
#         2, 3
#     ),
#     executa(soma, 2, 3)
# )

