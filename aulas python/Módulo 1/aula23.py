'''
lista = ['Murilo', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)
'''

lista = ['Murilo', 'João', 'Maria',1,2,3,4,5,6,7,8,9]

n1, n2, *outra_lita, ultimo_da_lista = lista

print(n1, n2, outra_lita, ultimo_da_lista)
