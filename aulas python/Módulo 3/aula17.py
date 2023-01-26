'''
mais sobre list comprehension
'''

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
# lista = [
#     (x, y)
#     for x in range(3)
#     for y in range(3)
# ]
lista = [
    [(x, letra) for letra in 'Murilo']
    for x in range(3)
]

print(lista)