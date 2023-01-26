'''
escopo global e local
'''
'''
#x = 1

#def escopo():
#    x = 10
#    def outra_funcao():
#        y = 2
#        print(x, y)
#    outra_funcao()
#   print(x)


#escopo()

x = 1

def escopo():
    global x
    x = 10
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)


print(x)
escopo()
print(x)
'''

'''
parte 2 da aula
'''