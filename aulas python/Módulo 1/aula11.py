'''
a = 2
b = 2
c = 3


a == b and b < c

not a == b and not b < c
'''
'''
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

idade = int(idade)

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')

'''
'''
a = 2
b = 3

if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')

'''

nome = 'Murilo Dinis'

if 'u' in nome:
    print('Existe a letra u no seu nome')
