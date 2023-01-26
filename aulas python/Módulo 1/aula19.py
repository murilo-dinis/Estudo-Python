texto = 'Python'
'''
c = 0
while c < len(texto):
    print(texto[c])
    c += 1
'''
'''
for n,letra in enumerate(texto):
    print(n,letra)

'''
'''
for n in range(5, 10, 1):  # comece no 5, termina no 10 e pule de 1 em 1
    print(n)

'''
'''
for n in range(20, 10, -1):
    print(n)


for n in range(100):
    if n % 8 == 0:
        print(n)

'''
nova_string = ''

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)