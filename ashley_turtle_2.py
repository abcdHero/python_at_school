import random
import turtle

t = turtle.Turtle()
t.speed(0)

for j in range(999):
    for k in range(25):
        b = random.randint(-45, 45)
        t.left(b)
        t.forward(10)
        t.right(b)
    t.penup()
    t.goto(0, 0)
    t.pendown()