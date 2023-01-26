string = 'ABCD'
lista = ['Maria','Helena',1,2,3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Maria', 'Helena', ],
    ['Elaine', ],
    ['Luiz', 'João','Eduarda', ],
]

#a, b, *_, u = lista
#print(a, u)

#for nome in lista:
#    print(nome, end=' ')


print(*lista)
print(*tupla)
print(*salas, sep='\n')