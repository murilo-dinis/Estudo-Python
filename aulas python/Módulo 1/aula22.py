'''
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')
'''
'''
for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')
'''

'''
palavra = ''
contagem = 0
for v in lista_1:
    qtd_vezes = lista_1.count(v)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = v

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x).')
'''
'''
for v in lista_2:
    print(v.strip().capitalize())
'''
'''
string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)
'''
'''
string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])
'''
'''
lista = [
    [0,'Murilo'],
    [1,'João'],
    [2,'Maria'],
]

for indice, nome in lista:
    print(indice, nome)

# mesma coisa:

lista2 = ['Murilo', 'João', 'Maria']

for indice, valor in enumerate(lista2):
    print(indice, valor)
'''