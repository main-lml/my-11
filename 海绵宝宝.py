from time import sleep
from turtle import *
open(1)
sleep(0)
def bk():#外部轮廓
    fillcolor('yellow')
    begin_fill()
    up()
    goto(100,100)
    down()
    right(-40)
    
    seth(-70)#设置画笔朝向
    for i in range(3):
        circle(-40,60)
        circle(40,60)
    circle(-11.5,120)
    seth(150)#设置画笔朝向
    for naim in range(3):
        circle(35,60)
        circle(-35,60)
    circle(-11.5,100)
    seth(125)#设置画笔朝向
    for manin in range(3):
        circle(-40,60)
        circle(40,60)
    circle(-11.5,120)
    seth(-30)#设置画笔朝向
    for lisd in range(4):
        circle(35,60)
        circle(-35,60)
    seth(-110)
    circle(35,37)
    end_fill()
def man():#眼睛内圈
    fillcolor('black')
    begin_fill()
    circle(15)
    end_fill()
def mann():#眼睛外圈
    fillcolor('white')
    begin_fill()
    circle(30,450)
    end_fill()

bk()#外部轮廓
seth(0)#设置画笔朝向

up()
goto(-110,30)
down()

mann()

up()
goto(-90,60)
down()

man()
seth(0)#设置画笔朝向

up()
goto(30,30)
down()

fillcolor('white')
begin_fill()
circle(30,360+270)
end_fill()

up()
goto(10,60)
down()

man()

up()
goto(-110,90)
down()
seth(180)
circle(30,25)
seth(115)
pensize(5)
fd(10)

up()
goto(-110,90)
down()
seth(90)
fd(10)

up()
goto(-110,90)
seth(0)
circle(-30,25)
down()
seth(65)
fd(10)
#左眼毛

up()
goto(30,90)
seth(180)
circle(30,25)
down()
seth(115)
pensize(5)
fd(10)

up()
goto(30,90)
down()
seth(90)
fd(10)

up()
goto(30,90)
seth(0)
circle(-30,25)
down()
seth(65)
fd(10)






sleep(400000)