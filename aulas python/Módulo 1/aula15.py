num_1 = 1
num_2 = 1150
divisao = num_1 / num_2

# print('{:.2f}'.format(divisao))
# print(f'{divisao:.2f}')

# nome = 'Murilo Dinis'
# print(f'{nome:s}')

'''
print(f'{num_1:0>10}')

print(f'{num_2:0^10}')
print(f'{num_2:0>10.2f}')

'''

nome = 'Murilo Dinis'
# print(f'{nome:#^50}')

nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)