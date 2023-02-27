print('Bem-vindo(a) à calculadora')
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = input("Digite uma das operações: +, -, *, /: ")
if operacao == "+":
    resultado = n1 + n2
    print(f'A soma é: {resultado}')
    print('Obrigado por usar a Calculadora by Fabio Lima!')
elif operacao == "-":
    resultado = n1 - n2
    print(f'A subtração é: {resultado}')
    print('Obrigado por usar a Calculadora by Fabio Lima!')
elif operacao == "*":
    resultado = n1 * n2
    print(f'A multiplicação é: {resultado}')
    print('Obrigado por usar a Calculadora by Fabio Lima!')
elif operacao == "/":
    resultado = n1 / n2
    print(f'A divisão é: {resultado}')
    print('Obrigado por usar a Calculadora by Fabio Lima!')
else:
    print("Resultado inválido")
    print('Verifique se você digitou algo errado e tente outra vez.')
