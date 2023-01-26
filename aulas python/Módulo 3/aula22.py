import sys

'''
generator, expression, iterables e iterators
'''

# iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iter(iterable)  # tem __iter__ e __next__

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iter(iterable)
# lista = [n for n in range(10000)]
# generator = (n for n in range(10000))
# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))

# generator functions

# def generator(n=0):
#     yield 1   # pausar
#     print('Continuando...')
#     yield 2
#     print('Mais uma...')
#     yield 3
#     print('Vou terminar')
#     return 'ACABOU'


# def generator(n=0, maximum=10):
#     while True:
#         yield n

#         if n > maximum:
#             return

        
#         n += 1


# gen = generator()
# # print(next(gen))
# # print(next(gen))

# for n in gen:
#     print(n)

def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')

def gen3():
    print('COMECOU GEN3')

    yield 10
    yield 20
    yield 30

def gen2(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')

g1 = gen2(gen1)
g2 = gen2(gen3)
for numero in g1:
    print(numero)
for numero in g2:
    print(numero)