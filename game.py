import turtle
import random
import time

isPlaying = True
screen = turtle.Screen()
screen.title("Аркаша за яблоками")
screen.bgcolor("lightgreen")
screen.setup(width=600, height=800)
screen.tracer(0)
kist = turtle.Turtle()
kist.penup()
kist.goto(-100, -400)

def draw_lines():
    kist.speed(0)
    kist.pendown()
    kist.goto(-100, 400)
    kist.penup()
    kist.goto(100, 400)
    kist.pendown()
    kist.goto(100, -400)

draw_lines()
ark = turtle.Turtle()
ark.shape("square")
ark.color("brown")
ark.shapesize(0.2, 0.2)
ark.penup()
ark.speed(0)

coor_x = [-200, 0, 200]
curcoor = 1
ark.goto(coor_x[curcoor], -350)

apples = []
obstacles = []

def generatingObjects(iterr, shape, color, listOfObjects):
    global coor_x
    for _ in range(iterr):
        objectt = turtle.Turtle()
        objectt.shape(shape)
        objectt.color(color)
        objectt.penup()
        x = random.choice(coor_x)
        y = 600
        objectt.goto(x, y)
        listOfObjects.append(objectt)

generatingObjects(20,"circle","red", apples)
generatingObjects(10,"triangle","black", obstacles)
score = 0

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-250, 350)
score_display.write(f"Счёт: {score}", font=("Arial", 16, "normal"))
def move_left():
    global curcoor
    if curcoor > 0:
        curcoor -=1
        ark.setx(coor_x[curcoor])

def move_right():
    global curcoor
    if curcoor < 2:
        curcoor +=1
        ark.setx(coor_x[curcoor])

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")


def propadanie(objj, y=-410):
    global coor_x

    if y < -400:
        x_new = random.choice(coor_x)
        y_new = 600
        objj.goto(x_new, y_new)


while isPlaying:
    screen.update()

    for apple in apples:
        y = apple.ycor()
        y -= 4
        apple.sety(y)
        for obst in obstacles:
            if (abs(apple.xcor() - obst.xcor()) < 5) and (abs(apple.ycor() - obst.ycor()) < 5):
                propadanie(apple)
        propadanie(apple, y=y)
        for appl in apples:
            if (abs(apple.xcor() - appl.xcor()) < 5) and (abs(apple.ycor() - appl.ycor()) < 5):
                propadanie(apple)

        if (abs(apple.xcor() - coor_x[curcoor]) < 20) and (abs(apple.ycor() - ark.ycor()) < 20):
            score +=1
            score_display.clear()
            score_display.write(f"Счёт: {score}", font=("Arial", 16, "normal"))
            propadanie(apple)
    for obstacle in obstacles:
        y = obstacle.ycor()
        y -= 4
        obstacle.sety(y)
        for appl in apples:
            if (abs(apple.xcor() - appl.xcor()) < 5) and (abs(apple.ycor() - appl.ycor()) < 5):
                propadanie(apple)
        for appl in apples:
            if (abs(apple.ycor() - appl.ycor()) < 20):
                propadanie(apple)
        propadanie(obstacle, y=y)
        if (abs(obstacle.xcor() - coor_x[curcoor]) < 4) and (abs(obstacle.ycor() - ark.ycor()) < 4):
            screen.bye()
            isPlaying = False

    time.sleep(0.017)