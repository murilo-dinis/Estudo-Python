'''
#dir, hasattr e getattr 
'''

string = 'Murilo'
metodo = 'upper1'

if hasattr(string, 'upper'):
    print('existe upper')
    print(getattr(string, metodo)())
    print(string)
else:
    print('não existe o método', metodo)