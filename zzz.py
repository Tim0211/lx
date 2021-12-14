#coding=utf-8
import turtle as tt
import random as rd
import time as s
pg = tt.Screen()
pg.register_shape('e.gif')
pg.register_shape('j.gif')
tt.hideturtle()
tt.penup()
tt.home()
tt.write("你有五秒的准备时间，罗晓！！",align='center',font=("Comic Sans Ms",30,'bold'))
s.sleep(5)
tt.clear()
def up():

    j.setheading(90)
    j.fd(20)

def left():
    j.setheading(180)
    j.fd(20)

def right():
    j.setheading(0)
    j.fd(20)

def down():
    j.setheading(270)
    j.fd(20)
t = tt.Turtle()
j = tt.Turtle()
j.speed(0)

t.shape('e.gif')
t.penup()
t.goto(rd.randint(-250, 250), rd.randint(-250, 250))
j.shape('j.gif')
j.penup()
j.goto(rd.randint(-250, 250), rd.randint(-250, 250))
pg.onkey(up, 'w')
pg.onkey(left, 'a')
pg.onkey(right, 'd')
pg.onkey(down, 's')
pg.listen()
start=s.time()
while True:
    t.setheading(t.towards(j))
    t.forward(5)
    t.speed(0)
    if t.distance(j)<10:
        end=s.time()
        pg.clear()
        j.goto(0,0)
        j.write("游戏结束",align='center',font=("Comic Sans Ms",50,'bold'))
        j.goto(0,-50)
        j.write("你活了{:.1f}秒".format(end - start), align='center', font=("Comic Sans Ms", 30, 'bold'))
        break

