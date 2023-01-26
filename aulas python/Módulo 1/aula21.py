variavel = ['Murilo Dinis', 'Joãozinho', 'Maria']

'''
for valor in variavel:
    print(valor)
    continue
    #break
    print(valor)
'''

'''
for v in variavel:
    if v.startswith('J'):
        print('Começa com J', v)
    else:
        print('Não começa com J', v)
'''

comeca_com_j = False
for v in variavel:
    if v.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J.')
    
'''
if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')
'''