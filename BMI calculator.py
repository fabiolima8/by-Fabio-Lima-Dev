def imc(peso, altura):
    altura_quadrada = altura ** 2
    meu_imc = peso / altura_quadrada
    return meu_imc


print('')
print(f'Olá! Bem-Vindo(a) ao projeto Python:Calculadora de Indice de Massa Corporal.')
nome = input('Por favor, digite o seu nome: ')
peso = float(input('Agora digite seu peso, por favor: '))
altura = float(input('Agora só preciso saber sua altura. Digite por favor: '))
meu_imc = imc(peso, altura)
print('')
print(f'{nome}, seu IMC é: {meu_imc:.2f}')
print('')
print('Obrigado por usar a calculadora desenvolvida por fabiolima8!')
