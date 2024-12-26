from turtle import *
from time import sleep
color('green')
bgcolor('black')
speed(20)#画笔速度
up()
goto(0,150)
down()
namlist=0
while namlist<200:
    right(namlist)
    forward(namlist*3)
    namlist+=1
sleep(1)