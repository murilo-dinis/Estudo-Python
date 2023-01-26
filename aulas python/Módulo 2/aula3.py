'''
1) Exercício criar uma função que exibe uma saudação com saudação e nome


'''

'''
def saudacao(msg = 'Bom dia', nome = 'Murilo'):
    print(msg, nome)

saudacao()
'''

'''
2) Exercício criar uma função que recebe 3 parâmetros e executa a soma entre eles.
'''

'''
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(1,2,3)

'''

'''
3)
'''

'''
def aumento_percentual(valor, percentual):
    print(valor + (valor * percentual / 100))

aumento_percentual(50, 10)
aumento_percentual(100, 10)
'''

'''
4) Fizz Buzz
'''
'''
def fb(n):
    if n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    elif n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    else:
        return n
'''

'''
def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    return n
    
'''