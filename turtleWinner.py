#!/usr/bin/env python 3

# Naz-Al Islam
# 05/02/16
# Prints which turtle wins the race

import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.setup(400, 500)
wn.bgcolor("lightgreen")
wn.screensize(400, 500)
wn.setworldcoordinates(0, 0, 400, 500)
t.penup()
t.goto(0, 350)
t.pendown()
t.forward(400)

tess = turtle.Turtle()
tess.color("purple")
tess.penup()
tess.forward(100)
tess.pendown()
tess.left(90)
tess.forward(10)

alex = turtle.Turtle()
alex.color("blue")
alex.penup()
alex.forward(200)
alex.pendown()
alex.left(90)
alex.forward(10)

def h1():                   
    tess.forward(50)
    if tess.pos()[1] >= t.pos()[1]:             
        wn.bye()
        print('TESS')

def h2():                   
    alex.forward(50)
    if alex.pos()[1] >= t.pos()[1]:             
        wn.bye()
        print('ALEX')
       
wn.onkey(h1, 't')
wn.onkey(h2, 'a')

def handler_for_tess(x, y):
    wn.title("Tess clicked at {0}, {1}".format(x, y))
    tess.forward(50)
    if tess.pos()[1] >= t.pos()[1]:             
        wn.bye()
        print('TESS')

def handler_for_alex(x, y):
    wn.title("Alex clicked at {0}, {1}".format(x, y))
    alex.forward(50)
    if alex.pos()[1] >= t.pos()[1]:             
        wn.bye()
        print('ALEX')

tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)

wn.listen()
wn.mainloop()
