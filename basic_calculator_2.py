print('******************** Calculadora em Python ********************')
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def division(x, y):
    return x / y
print('\nSelecione o número da opção desejada: \n')
print('1 - soma')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')
fim =  '\n************************************ Developed by Fabio Lima Dev'
escolha = input('\nDigite sua opção 1/ 2/ 3/ 4: ')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if escolha == "1":
    print('\n')
    print(f'A soma de {num1} e {num2} é igual a: {add(num1, num2)}\n{fim}')
elif escolha == '2':
    print('\n')
    print(f'A subtração entre {num1} e {num2} é: {subtract(num1, num2)}')
elif escolha == "3":
    print('\n')
    print(f'A multiplicação de {num1} e {num2} é: {multiply(num1, num2)}')
elif escolha == '4':
    print('\n')
    print(f'A divisão de {num1} por {num2} é: {division(num1, num2)}')
else:
    print('Opção inválida')
    
