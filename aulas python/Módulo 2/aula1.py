'''
def funcao():
    print('Hello World!')

funcao()
funcao()
funcao()
funcao()

'''
'''
def funcao(msg):
    print(msg)

funcao('Mensagem')

'''
'''
def saudacao(msg, nome):
    print(msg, nome)

saudacao('Olá', 'Bruna')

'''

def saudacao(msg='Olá', nome='Bruna'):
    print(msg, nome)

saudacao('Olá', 'Bruna')
saudacao('','')
saudacao(nome='Bruna', msg='Oi')