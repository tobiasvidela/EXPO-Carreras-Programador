import turtle
import time
import random

posponer = 0.1

# Marcador
score = 0
high_score = 0

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("light blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("circle")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Cargar la imagen de comida
wn.addshape("comida.gif")

# Comida con imagen personalizada
comida = turtle.Turtle()
comida.speed(0)
comida.shape("comida.gif")  # Establece la imagen como la forma de la comida
comida.penup()
comida.goto(0, 100)

# Segmentos
segmentos = []

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Puntaje: 0     Récord: 0", align="center", font=("Impact", 24, "normal"))

# Funciones de dirección
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
    
while True:
    wn.update()

    # Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        for segmento in segmentos:
            segmento.goto(1000, 1000)

        segmentos.clear()

        score = 0
        texto.clear()
        texto.write("Puntaje: {}     Récord: {}".format(score, high_score), 
                    align="center", font=("Impact", 24, "normal"))

    # Colisiones comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("green")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        score += 1
        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Puntaje: {}    Récord: {}".format(score, high_score), 
                    align="center", font=("Impact", 24, "normal"))

    # Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()

    # Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 5:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            for segmento in segmentos:
                segmento.goto(1000, 1000)

            segmentos.clear()

            score = 0
            texto.clear()
            texto.write("Puntaje: {}    Récord: {}".format(score, high_score), 
                        align="center", font=("Impact", 24, "normal"))

    time.sleep(posponer)
