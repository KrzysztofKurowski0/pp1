from turtle import *
import math
def square(size,linecolor,fillcol,coord_x,coord_y,angle):
    color(linecolor)
    fillcolor(fillcol)
    up()
    setx(coord_x)
    sety(coord_y)
    down()
    right(angle)
    for i in range (4):
        forward(size)
        right(90)

square(200,"red","black",-600,400,0)

def right_triangle(size,linecolor,fillcol,coord_x,coord_y,angle):
    color(linecolor)
    fillcolor(fillcol)
    up()
    setx(coord_x)
    sety(coord_y)
    down()
    right(angle)
    right(180)
    forward(size/2)
    right(90)
    forward((size*math.sqrt(3))/2)
    right(150)
    forward(size)
    
    
right_triangle(300,"red","black",-200,100,0)

def trefoil(size,linecolor,fillcol,coord_x,coord_y,angle):
    color(linecolor)
    fillcolor(fillcol)
    up()
    setx(coord_x)
    sety(coord_y)
    down()
    right(angle)
    for i in range(3):
        circle(size,240)
        right(120)

trefoil(50,"red","black",0,-200,0)

def cross(size,linecolor,fillcol,coord_x,coord_y,angle):
    color(linecolor)
    fillcolor(fillcol)
    up()
    setx(coord_x)
    sety(coord_y)
    down()
    right(angle)
    for i in range(4):
        forward(size)
        right(90)
        forward(size)
        right(90)
        forward(size)
        left(90)
cross(80,"red","black",-200,-300,0)

def rhombus(size,linecolor,fillcol,coord_x,coord_y,angle):
    color(linecolor)
    fillcolor(fillcol)
    up()
    setx(coord_x)
    sety(coord_y)
    down()
    right(angle)
    right(90)
    for i in range (4):
        forward(size)
        right(90)
rhombus(80,"red","black",400,-200,0)
done()
    
        