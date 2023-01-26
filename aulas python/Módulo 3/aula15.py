a, b = 1, 2
a, b = b, a

pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Souza',
}

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa = {
    'idade' : 16,
    'altura' : 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Joana', qlqr=123)
mostro_argumentos_nomeados(**pessoa_completa)