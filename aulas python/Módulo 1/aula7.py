nome = 'Murilo'
idade = 17
altura = 1.82
e_maior = idade > 18  # nesse caso retornará false
peso = 60
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

print('{} tem {} anos de idade e seu imc é {:.2f}'. format(nome, idade, imc))

print('{n} tem {i} anos de idade e seu imc é {im}'. format(n=nome, i=idade, im=imc))