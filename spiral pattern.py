import turtle
my_wn=turtle.Screen()
my_wn.bgcolor("dark magenta")
my_wn.title("Spiral Pattern")
my_pen=turtle.Turtle()
size=0
while True:
    for i in range(6):
        my_pen.fd(size+1)
        my_pen.left(90)
        size=size-5
    size+=1
turtle.done()