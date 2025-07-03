import turtle

t = turtle.Turtle()

def runn(t):
    for _ in range(4):
        t.forward(100)
        t.left(90)
    turtle.done()

#runn(leo)

t.shape('turtle')
t.color('blue')

def move_forward(step):
    t.forward(step)

def move_backward():
    t.backward(100)

def turn_left():
    t.left(45)

def turn_right():
    t.backward(45)




#runn(leo)

screen = turtle.Screen()
screen.onkey(lambda: move_forward(100), "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(screen.bye, "Escape")

screen.listen()
screen.mainloop()