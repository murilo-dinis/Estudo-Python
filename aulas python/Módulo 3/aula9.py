'''
dicionarios em Python
são estruturas de dados do tipo par de chave e valor

para criar dicionarios usamos as chaves {}

imutável: str, int, float, bool, tuple
mutável: dict, list
'''
'''
pessoa = {
    'nome': 'Murilo Dinis',
    'sobrenome': 'Alvarenga',
    'idade': 17,
    'altura': 1.8,
    'endereços': [
        {'rua': 'Francisco Munhoz Cegarra', 'número': 167},
    ],
}

print(pessoa, type(pessoa))
'''

pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Murilo Dinis'
pessoa['sobrenome'] = 'Alavrenga'

print(pessoa)
pessoa[chave] = 'Maria'
print(pessoa[chave])

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome', None):
    print('Existe')
