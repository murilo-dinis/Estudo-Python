'''
CPF = 168.995.350-09

1 * 10 = 10
6 * 9 = 54
8 * 8 = 64
9 * 7 = 63
9 * 6 = 54   +
5 * 5 = 25
3 * 4 = 12
5 * 3 = 15
0 * 2 = 0
        
        297
11 - (297 % 11) = 11
11 > 9 = 0
Digito 1 = 0

'''
while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:9]
    total = 0
    reverso = 10

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
        
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    if cpf == novo_cpf:
        print('Válido')
    else:
        print('Inválido')