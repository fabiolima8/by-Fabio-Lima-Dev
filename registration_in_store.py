from datetime import datetime
import random

print('------Olá bem vindo à nossa empresa------')
nome_completo = input('Escreva seu nome completo: ')
idade = int(input('Qual a sua idade? '))
data_de_cadastro = datetime.now()
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
cartao = random.choice(cartoes)
aniversario = datetime.strptime(
    input('Digite sua data de aniversário no formato dd/mm/aaaa: '), '%d/%m/%Y')
print(f'Olá {nome_completo}, seu cadastro foi concluido com sucesso no dia\n {data_de_cadastro.day}/{data_de_cadastro.month}/{data_de_cadastro.year}.\nParabéns! Houve um sorteio e você ganhou um cartão de compras no valor de {cartao}.')
