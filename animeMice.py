import turtle
def draw(x, y):
    t.pendown()
    t.goto(x, y)
    t.penup()

screen = turtle.Screen()
t = turtle.Turtle()
t.penup()

turtle.onscreenclick(draw)

screen.mainloop()