"""Spiral de Spiral com default de 4 minimo de 2 e maximo de 6 """
# Script feito por Matheus Silva
# Parecido com feito em Ensine Seus Filhos a Programar mais com minha Evoloção no mesmo
# Aceito criticas construtivas pro mesmo
# Feito 30/01/2018 Hs 17:00

import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")

""" pede ao usuario um numero de lados
      2-4-6 ! ! !
"""
lados = int(turtle.numinput("numero de lados",
                        "Quantos lados ? 2 - 4 -6 "))
cores = ["red","yellow","blue","green","purple","orange"]

"""Laço multiplicando os lados 
espiral 10*10 = 100 """

for m in range(100):
    t.forward(m*4)
    posicao = t.position() # Armazena um lado da spiral
    direcao = t.heading() # Armazena a direção para spiral seguir
    print(posicao, direcao)

    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(cores[n%lados])
        t.forward(2*n)
        t.right(360/lados - 2)
        t.penup()
    t.setx(posicao[0])
    t.sety(posicao[1])
    t.setheading(direcao)
    t.left(360/lados + 2)