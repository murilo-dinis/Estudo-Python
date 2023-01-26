'''
métodos úteis dos dicionarios em Python
len - quantas chaves
items - iterável com chaves e valores
values - iterável com os valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave específica (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
'''
import copy
# pessoa = {
#     'nome': 'Murilo Dinis',
#     'sobrenome': 'Alvarenga',
#     'idade': 900,
# }

#print(len(pessoa))
#print(list(pessoa.keys()))
#print(list(pessoa.values()))
#print(list(pessoa.items()))
#pessoa.setdefault('idade', 0)
#print(pessoa['idade'])



#for chave in pessoa.keys():
#    print(chave)

#for chave, valor in pessoa.items():
#    print(chave, valor)

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2],
# }

# d2 = d1.copy(d1)

# d2['c1'] = 100
# d2['l1'][1] = 99999

# print(d1)
# print(d2)

p1 = {
    'nome': 'Murilo',
    'sobrenome' : 'Alvarenga',
}

# print(p1.get('nome'))
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# nome = p1.popitem()
# print(nome)
# print(p1)

# p1.update({
#     'nome': 'novo valor',
#     'idade': 17,
# })
p1.update(nome='novo valor', idade=17)
tupla = ('nome', 'novo valor'),
p1.update(tupla)
print(p1)