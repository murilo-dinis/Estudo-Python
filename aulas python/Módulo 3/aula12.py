'''
sets em python
'''

# s1 = set('Murilo')
# print(s1)

# s1 = {'Murilo',2,3,4}
# print(s1)

# s1 = set()   # sem dados
# s1 = {'Murilo', 1, 2, 3}   # com dados


# sets são eficientes para remover valores duplicados

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3, 3, 3, 3, 1}
# print(s1)

#set não tem índices

# para saber se existe um elemento no set usamos in:
# s1 = {1, 2, 3}
# print(3 not in s1)

# for numero in s1:
#     print(numero)


#métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('Murilo')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()
# s1.discard('Olá mundo')
# print(s1)



# operados úteis
# união, | (union) - une
# intersecção & (intersection) - itens presentes em ambos
# diferença - itens presentes apenas no set da esquerda
# siferença simétrica ^ - itens que não estão em ambos

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = s1 | s2
# s3 = s1 & s2
#s3 = s2 - s1
# s3 = s1 ^ s2
#print(s3)


'''
exemplo de uso de set
'''
# letras = set()
# while True:
#     letra = input('Digite: ')
#     letras.add(letra)


#     if 'l' in letras:
#         print('Parabéns!')
#         break

#     print(letras)

