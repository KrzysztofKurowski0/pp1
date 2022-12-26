from turtle import *
import math

def name():

    speed(20)
    #K
    up()
    setx(000)
    sety(200)
    down()
    right(90)
    forward(35)
    left(180)
    forward(17.5)
    right(45)
    forward(25)
    right(180)
    forward(25)
    left(90)
    forward(25)
    #R
    up()
    setx(30)
    sety(200)
    down()
    right(45)
    forward(35)
    right(180)
    forward(17.5)
    left(-450)
    circle(9,180)
    left(90)
    forward(17.5)
    left(30)
    forward(22)
    #Z
    up()
    setx(55)
    sety(200)
    down()
    right(300)
    forward(26)
    right(130)
    forward(45)
    left(130)
    forward(26)
    #Y
    up()
    setx(90)
    sety(200)
    down()
    right(65)
    forward(20)
    left(130)
    forward(20)
    backward(20)
    right(155)
    forward(18)
    #S
    up()
    setx(125)
    sety(200)
    down()
    left(90)
    forward(5)
    backward(5)
    circle(-9,-185)
    right(10)
    circle(9,-250)
    #Z
    up()
    setx(145)
    sety(200)
    down()
    right(285)
    forward(26)
    right(130)
    forward(45)
    left(130)
    forward(26)
    #T
    up()
    setx(180)
    sety(200)
    down()
    forward(25)
    backward(12.5)
    right(90)
    forward(35)
    #O
    up()
    setx(210)
    sety(182)
    down()
    circle(19)
    #F
    up()
    setx(260)
    sety(165)
    down()
    right(180)
    forward(20)
    right(91)
    forward(16)
    backward(16)
    left(91)
    forward(15)
    right(90)
    forward(17)

    #Nazwisko
    #K
    up()
    setx(320)
    sety(200)
    down()
    right(90)
    forward(35)
    left(180)
    forward(17.5)
    right(45)
    forward(25)
    right(180)
    forward(25)
    left(90)
    forward(25)

    #U
    up()
    setx(345)
    sety(200)
    down()
    right(45)
    forward(25)
    circle(10,180)
    forward(26)

    #R
    up()
    setx(380)
    sety(200)
    down()
    right(180)
    forward(35)
    right(180)
    forward(17.5)
    left(-450)
    circle(9,180)
    left(90)
    forward(17.5)
    left(30)
    forward(22)

    #O
    up()
    setx(400)
    sety(173)
    down()
    circle(19)

    #W
    up()
    setx(445)
    sety(200)
    down()
    right(30)
    forward(35)
    right(-120)
    forward(12)
    right(60)
    forward(12)
    left(120)
    forward(35)

    #S
    up()
    setx(490)
    sety(200)
    down()
    left(265)
    forward(5)
    backward(5)
    circle(-9,-185)
    right(10)
    circle(9,-250)

    #K
    up()
    setx(510)
    sety(200)
    down()
    right(10)
    forward(35)
    left(180)
    forward(17.5)
    right(45)
    forward(25)
    right(180)
    forward(25)
    left(90)
    forward(25)

    #I
    up()
    setx(540)
    sety(200)
    down()
    right(45)
    forward(35)

    #ID
    #2
    up()
    setx(30)
    sety(140)
    down()
    right(200)
    circle(9,220)
    right(400)
    up()
    circle(9,220)
    down()
    right(230)
    forward(34)
    right(240)
    forward(20)

    #2
    up()
    setx(60)
    sety(140)
    down()
    left(70)
    circle(9,220)
    right(400)
    up()
    circle(9,220)
    down()
    right(230)
    forward(34)
    right(240)
    forward(20)

    #8
    up()
    setx(85)
    sety(130)
    down()
    circle(10.5)
    up()
    goto(85,110)
    down()
    circle(10.5)

    #5
    up()
    setx(125)
    sety(150)
    down()
    right(180)
    forward(15)
    left(90)
    forward(17)
    left(90)
    forward(5)
    right(90)
    up()
    forward(23)
    down()
    right(90)
    forward(5)
    backward(5)
    right(180)
    circle(11.5,190)

    #2
    up()
    setx(155)
    sety(140)
    left(240)
    down()
    circle(9,220)
    right(400)
    up()
    circle(9,220)
    down()
    right(230)
    forward(34)
    right(240)
    forward(20)

    #8
    up()
    setx(180)
    sety(130)
    down()
    circle(10.5)
    up()
    goto(180,110)
    down()
    circle(10.5)



name() 

def square(size,linecolor,fillcol,coord_x,coord_y,angle):
    color(linecolor)
    up()
    setx(coord_x)
    sety(coord_y)
    down()
    fillcolor(fillcol)
    begin_fill()
    right(angle)
    for i in range (4):
        forward(size)
        right(90)
    end_fill()


def right_triangle(size,linecolor,fillcol,coord_x,coord_y,angle):
    color(linecolor)
    fillcolor(fillcol)
    up()
    setx(coord_x)
    sety(coord_y)
    down()
    begin_fill()
    right(angle)
    right(180)
    forward(size/2)
    right(90)
    forward((size*math.sqrt(3))/2)
    right(150)
    forward(size)
    end_fill()
    

def trefoil(size,linecolor,fillcol,coord_x,coord_y,angle):
    color(linecolor)
    fillcolor(fillcol)
    up()
    setx(coord_x)
    sety(coord_y)
    down()
    begin_fill()
    right(angle)
    for i in range(3):
        circle(size,240)
        right(120)
    right(30)
    end_fill()


def cross(size,linecolor,fillcol,coord_x,coord_y,angle):
    color(linecolor)
    fillcolor(fillcol)
    up()
    setx(coord_x)
    sety(coord_y)
    down()
    begin_fill()
    right(angle)
    for i in range(4):
        forward(size)
        right(90)
        forward(size)
        right(90)
        forward(size)
        left(90)
    end_fill()

def rhombus(size,linecolor,fillcol,coord_x,coord_y,angle):
    color(linecolor)
    fillcolor(fillcol)
    up()
    setx(coord_x)
    sety(coord_y)
    down()
    begin_fill()
    right(30)
    right(angle)
    for i in range (1,5):
        if i%2!=0:
            forward(size)
            right(120)
        else:
            forward(size)
            right(60)
    end_fill()

square(200,"red","black",-600,400,0)
right_triangle(300,"red","black",-200,100,0)
trefoil(50,"red","black",0,-200,0)
cross(80,"red","black",-200,-300,0)
rhombus(80,"red","black",400,-200,0)

done()
    
        