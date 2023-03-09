import time
import turtle as t
import os

script_dir = os.path.dirname(__file__)
rel_path = "snowman.png"
snowman = os.path.join(script_dir, rel_path)


# Draws body
t.speed(10)
t.penup()
t.setpos(0, -175)
t.pendown()
t.fillcolor("White")
t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()
t.setpos(0, 0)
t.pendown()
t.fillcolor("White")
t.begin_fill()
t.circle(80)
t.end_fill()
t.penup()
t.setpos(0, 150)
t.pendown()
t.fillcolor("White")
t.begin_fill()
t.circle(60)
t.end_fill()
t.penup()


# Draws mouth
t.pencolor("Red")
t.pensize(8)
t.penup()
t.setpos(0, 175)
t.pendown()
t.circle(20, 45)
t.penup()
for i in range(6):
    t.circle(20, 45)
t.pendown()
t.circle(20, 45)


# Draws eyes
t.pencolor("Black")
t.pensize(1)
t.penup()
t.setpos(-25, 225)
t.pendown()
t.dot(10, "black")
t.penup()
t.setpos(25, 225)
t.pendown()
t.dot(10, "black")


# Draws buttons
t.pencolor("Blue")
t.pensize(1)
t.penup()
t.setpos(0, 100)
t.pendown()
t.dot(15, "blue")
t.penup()
t.setpos(0, 80)
t.pendown()
t.dot(15, "blue")
t.penup()
t.setpos(0, 60)
t.pendown()
t.dot(15, "blue")


# Draws hands
t.pencolor("Brown")
t.pensize(6)
t.penup()
t.setpos(75, 100)
t.pendown()
t.setpos(120, 170)
t.penup()
t.setpos(-75, 100)
t.pendown()
t.setpos(-120, 170)


# Draw hat
t.pencolor("Black")
t.penup()
t.setpos(0, 265)
t.fillcolor("Black")
t.begin_fill()
t.pendown()
t.setpos(-50, 265)
t.setpos(50, 265)
t.setpos(50, 275)
t.setpos(35, 275)
t.setpos(35, 325)
t.setpos(-35, 325)
t.setpos(-35, 275)
t.setpos(-50, 275)
t.setpos(-50, 265)
t.end_fill()


# Meet requirments
time.sleep(0.1)
t.clear()
t.bgpic(snowman)


# Prevents exit
hold = input()