from turtle import Turtle

t = Turtle()
t.speed(1)
while True:
    direcao = input('Para qual direção devemos ir? F: frente e T: trás ')
    if direcao == 'f':
        distancia = int(input('Quantos pixels devemos movimentar para a frente? '))
        movimentar_lado = input(
            'Rotacionar para D: direita, E: esquerda ou N: não rotacionar?')
        if movimentar_lado == 'd':
            angulo = int(input('Quanto para a direita devemos rotacionar? '))
            t.right(angulo)
        elif movimentar_lado == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar? '))
            t.left(angulo)
        t.forward(distancia)

    if direcao == 't':
        distancia   = int(input('Quantos pixels devemos movimentar para a frente? '))
        movimentar_lado = input('Rotacionar para D: direita, E: esquerda ou N: não rotacionar?')
        if movimentar_lado == 'd':
            angulo = int(input('Quanto para a direita devemos rotacionar? '))
            t.right(angulo)
        elif movimentar_lado == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar? '))
            t.left(angulo)
        t.backward(distancia)

        resposta = input('Continuar andando? ')
        if resposta not in ('sim', 's'):
            break

