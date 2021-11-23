import turtle

t = turtle.Turtle()
t.speed(0)

t.left(90)

for i in range(4):
    t.forward(45)
    t.left(90)
    
for k in range(999):
    for n in range(3):
        t.forward(45)
        t.left(90)
    t.penup()
    t.forward(45)
    t.left(135)
    t.forward(2)
    t.right(45)
    t.pendown()