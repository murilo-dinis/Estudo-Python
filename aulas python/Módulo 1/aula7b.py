'''
desafio

Criar variáveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa,
criar variável com ano atual (int),
obter o ano de nascimento da pessoa (baseado na idade e no ano atual),
obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa),
exibir um texto com todos os valores na tela usando F-Strings (com as chaves),
'''

nome = 'Murilo'
idade = 17
altura = 1.82
peso = 60.0
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, pesa {peso}kg e tem {altura} de altura, nasceu em {ano_nascimento} e seu IMC é {imc:.2f}')
