from turtle import *
import math

def name():
    #K
    up()
    setx(200)
    sety(500)
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
    setx(230)
    sety(500)
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
    
        