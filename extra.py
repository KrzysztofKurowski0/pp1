from turtle import *
import math

def name():

    speed(20)
    #K
    up()
    setx(385)
    sety(450)
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
    setx(412)
    sety(450)
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
    setx(435)
    sety(450)
    down()
    right(300)
    forward(26)
    right(130)
    forward(45)
    left(130)
    forward(26)
    #Y
    up()
    setx(470)
    sety(450)
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
    setx(500)
    sety(450)
    down()
    left(90)
    forward(5)
    backward(5)
    circle(-9,-185)
    right(10)
    circle(9,-250)
    #Z
    up()
    setx(520)
    sety(450)
    down()
    right(285)
    forward(26)
    right(130)
    forward(45)
    left(130)
    forward(26)
    #T
    up()
    setx(550)
    sety(450)
    down()
    forward(25)
    backward(12.5)
    right(90)
    forward(35)
    #O
    up()
    setx(580)
    sety(434)
    down()
    circle(19)
    #F
    up()
    setx(630)
    sety(415)
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
    setx(695)
    sety(450)
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
    setx(725)
    sety(450)
    down()
    right(45)
    forward(25)
    circle(10,180)
    forward(26)

    #R
    up()
    setx(760)
    sety(450)
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
    setx(780)
    sety(422)
    down()
    circle(19)

    #W
    up()
    setx(825)
    sety(450)
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
    setx(870)
    sety(450)
    down()
    left(265)
    forward(5)
    backward(5)
    circle(-9,-185)
    right(10)
    circle(9,-250)

    #K
    up()
    setx(890)
    sety(450)
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
    setx(920)
    sety(450)
    down()
    right(45)
    forward(35)

    #Group name
    #Z
    up()
    setx(400)
    sety(360)
    down()
    right(90)
    forward(26)
    right(130)
    forward(45)
    left(130)
    forward(26)

    #Z
    up()
    setx(435)
    sety(360)
    down()
    forward(26)
    right(130)
    forward(45)
    left(130)
    forward(26)

    #I
    up()
    setx(450)
    sety(360)
    down()
    right(90)
    forward(35)

    #S
    up()
    setx(475)
    sety(395)
    down()
    left(267)
    forward(5)
    backward(5)
    circle(-9,-185)
    right(10)
    circle(9,-250)
    
    #N
    up()
    setx(495)
    sety(360)
    down()
    right(192)
    forward(35)
    right(150)
    forward(40)
    right(210)
    forward(35)





    #2
    up()
    setx(90)
    sety(140)
    down()
    right(450)
    circle(9,220)
    right(450)
    up()
    circle(9,220)
    down()
    right(230)
    forward(34)
    right(240)
    forward(20)




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

square(450,"red","black",-450,450,0)
right_triangle(300,"red","black",-450,100,0)
trefoil(50,"red","black",0,-450,0)
cross(80,"red","black",-450,-300,0)
rhombus(80,"red","black",450,-450,0)

done()
    
        