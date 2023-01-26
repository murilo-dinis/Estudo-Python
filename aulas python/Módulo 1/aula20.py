'''
#        0     1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E', 10.5]

#        5    4    3    2    1
'''
'''
string = 'ABacanaCDE'

print(string[1])
print(lista[1])
'''
'''
lista[5] = 'Qualquer outra coisa'
print(lista[5])
'''
'''
print(lista[0:3])
print(lista[1:4])
print(lista[:3])
print(lista[2:])
print(lista[::2])
print(lista[::-1])
'''

'''
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

l1.append(l2)
print(l2)
l2.insert(0, 'banana')
print(l2)
l2.pop()
print(l2)
'''


'''
l = [1,2,3,4,5,6,7,8,9]

l.insert(0, 'banana')

print(l)

del(l[0])

print(l)
'''

'''
l2 = [0,1,2,3,4,5,6,7,8,9]

soma = 0
for valor in l2:
    soma = soma + valor
    
print(soma)
'''

'''
l2 = ['string', True, 10, -20.5]

for elem in l2:
    print(f'O tipo de elem é {type(elem)} e o seu valor é {elem}')
'''

'''
# Jogo da forca python


secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ah isso não vale, digite apenas uma letra.')
        continue
    
    digitadas.append(letra)
    
    if letra in secreto:
        print(f'Boa, a letra {letra} existe na palavra secreta.')
    else:
        print(f'Ah, a letra {letra} não existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, Você ganhou! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    
    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()

'''