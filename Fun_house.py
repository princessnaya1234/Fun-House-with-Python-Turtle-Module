# Program to draw a house using the turtle module
# Import turtle module

import turtle

# create turtle as t and give window screen attributes
t = turtle.Turtle()
wn_src = turtle.getscreen()
wn_src.bgcolor("Pink")
wn_src.title("A Simple Fun House")
wn_src.canvheight

# color and speed of turtle
t.color("black")
t.shape("turtle")
t.speed(1)

# creating the body of the house
t.penup()
t.pensize(2)
t.color("black", "skyblue")
t.begin_fill()
t.goto(-200, -250)
t.pendown()
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.end_fill()

# creating the roof of the house
t.color("black", "brown")
t.begin_fill()
t.left(50)
t.right(150)
t.left(150)
t.forward(200)
t.right(200)
t.forward(150)
t.backward(150)
t.left(100)
t.backward(200)
t.right(100)
t.left(200)
t.tiltangle(90)
t.end_fill()

# creating house partition
t.penup()
t.goto(20, -2)
t.down()
t.right(60)
t.left(90)
t.right(70)
t.right(10)
t.left(10)
t.right(10)
t.left(60)
t.right(60)
t.backward(249)
t.forward(300)
t.end_fill()

# creating right window
t.penup()
t.setheading(270)
t.goto(-140, 0)
t.pendown()
t.color("black", "gray")
t.begin_fill()
t.left(90)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.backward(50)
t.tilt(45)
t.right(45)
t.forward(40)
t.left(45)
t.forward(20)
t.end_fill()

# creating the left window
t.penup()
t.setheading(270)
t.goto(20, 0)
t.pendown()
t.color("black", "gray")
t.begin_fill()
t.left(90)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.backward(50)
t.tilt(45)
t.right(45)
t.forward(40)
t.left(45)
t.forward(20)
t.end_fill()

# creating the house door
t.penup()
t.setheading(270)
t.goto(-50, -250)
t.pendown()
t.color("black", "gray")
t.begin_fill()
t.right(90)
t.forward(75)
t.right(90)
t.forward(150)
t.right(90)
t.forward(75)
t.right(90)
t.forward(150)
t.backward(150)
t.tilt(45)
t.right(45)
t.left(45)
t.forward(150)
t.left(45)
t.backward(50)
t.right(90)
t.tilt(90)
t.left(45)
t.backward(120)
t.end_fill()
