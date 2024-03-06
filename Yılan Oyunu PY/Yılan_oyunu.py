import turtle
import time
import random

hiz = 0.15
pencere = turtle.Screen()
pencere.title('Yilan Oyunu')
pencere.bgcolor('lightgreen')
pencere.setup(width=600, height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape('square')
kafa.color('black')
kafa.penup()
kafa.goto(0, 100)
kafa.direction = 'stop'

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape('circle')
yemek.color('red')
yemek.penup()
yemek.goto(0, 0)
yemek.shapesize(0.80, 0.80)

kuyruklar = []
puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape('square')
yaz.color('white')
yaz.penup()
yaz.goto(0, 260)
yaz.hideturtle()
yaz.write('Puan: {}'.format(puan),align='center',font=('Courier',24,'normal') )

def move():
    if kafa.direction == 'up':
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == 'down':
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == 'right':
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == 'left':
        x = kafa.xcor()
        kafa.setx(x - 20)

def goUp():
    if kafa.direction != 'down':
        kafa.direction = 'up'

def goDown():
    if kafa.direction != 'up':
        kafa.direction = 'down'

def goRight():
    if kafa.direction != 'left':
        kafa.direction = 'right'

def goLeft():
    if kafa.direction != 'right':
        kafa.direction = 'left'

pencere.listen()
pencere.onkey(goUp, 'Up')
pencere.onkey(goDown, 'Down')
pencere.onkey(goRight, 'Right')
pencere.onkey(goLeft, 'Left')

def reset_game():
    global puan  
    puan = 0
    yaz.clear()
    yaz.write('Puan: {}'.format(puan),align='center',font=('Courier',24,'normal') )
    kafa.goto(0, 100)
    kafa.direction = 'stop'
    for segment in kuyruklar:
        segment.goto(1000, 1000)  
    kuyruklar.clear()  

def oyun_alani_guncelle():
    global puan  
    move()
    pencere.update()    

    if kafa.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)
        yeniKuyruk = turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape('square')
        yeniKuyruk.color('white')
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)

        puan = puan + 1
        yaz.clear()
        yaz.write('Puan: {}'.format(puan),align='center',font=('Courier',24,'normal') )

    if (kafa.xcor() > 290 or kafa.xcor() < -290 or
        kafa.ycor() > 290 or kafa.ycor() < -290):
        reset_game()

    for i in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[i - 1].xcor()
        y = kuyruklar[i - 1].ycor()
        kuyruklar[i].goto(x, y)
        

    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    pencere.ontimer(oyun_alani_guncelle, int(hiz * 1000))

oyun_alani_guncelle()

pencere.mainloop()
