import turtle
t=turtle.Turtle()
t.pensize(2)

t.color('blue')
t.speed(0)

def heart(x):
    t.begin_fill()
    t.fillcolor('Red')
    t.left(90)
    t.circle(-x,180)
    t.left(180)
    t.circle(-x,180)
    t.right(30)
    t.forward(4*x)
    t.right(120)
    t.forward(4*x)
def spokes(radius):
    t.left(90)
    t.circle(-radius)
    t.right(90)
    t.up()
    t.forward(radius)
    t.down()
    for i in range(24):

        t.forward(radius)
        t.backward(radius)
        t.left(15)










