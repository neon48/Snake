import turtle
import time
import random

posponer = 0.1 #bajar el tiempo de ejecucion
wn = turtle.Screen()  # crear la pantalla
cabeza = turtle.Turtle() #Crear serpiente
comida  = turtle.Turtle() #crear Comida


# Crear comida
def crearComida():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    comida.goto(x, y)

def IniciarApp():
    wn.title('Juego Snake por Solrac') #titulo de la pantalla
    wn.bgcolor('black') #fondo de la pantalla
    wn.setup(width=600, height=600) #tamaño de la pantalla
    wn.tracer(0) #que deje estela

IniciarApp()


#Cabeza serpiente
def iniciarCabeza():
    cabeza.speed(0)
    cabeza.shape('square')
    cabeza.color("white")
    cabeza.penup() #que no deje estela
    cabeza.goto(0,0)
    cabeza.direction = 'stop'

iniciarCabeza()

#cuerpo serpiente
segmentos = []

#Generar Comida
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
crearComida()


#definir funciones de movimientos
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

#teclado definir movimientos con las teclas
wn.listen() #poner en escucha para que reciba teclado
wn.onkeypress(arriba,"Up") #tecla flecha arriba
wn.onkeypress(abajo,"Down") #Tecla flecha abajo
wn.onkeypress(izquierda,"Left") #tecla flecha izquierda
wn.onkeypress(derecha,"Right") #tecla flecha derecha

#funciones
def mov(): #definir movimientos
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)

while True:
    wn.update() #actualizar la pantalla segun posponer



    #definir colision con la comida
    if cabeza.distance(comida) < 20:
        crearComida()
        #x=random.randint(-280,280)
        #y=random.randint(-280,280)
        #comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.color("white")
        nuevo_segmento.penup()  # que no deje estela
        nuevo_segmento.direction = 'stop'
        segmentos.append(nuevo_segmento)

    totalSeg = len(segmentos)
    for index in range(totalSeg -1,0,-1):
        x = segmentos[index -1].xcor()
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    #definir colision con las paredes
    if cabeza.xcor()>300 or cabeza.xcor() < -300:
        cabeza.goto(0,0)

        for segmento in segmentos:
            segmento.hideturtle()
        segmentos.clear()
        iniciarCabeza()
        crearComida()
    if cabeza.ycor()>300 or cabeza.ycor() < -300:
        cabeza.goto(0,0)
        for segmento in segmentos:
            segmento.hideturtle()
        segmentos.clear()
        iniciarCabeza()
        crearComida()

    mov()
    time.sleep(posponer)


