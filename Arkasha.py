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
ark.shapesize(2,2)
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
        y = random.randint(300, 1400)
        objectt.goto(x, y)
        listOfObjects.append(objectt)


generatingObjects(10, "circle", "red", apples)
generatingObjects(5, "triangle", "black", obstacles)
score = 0

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-250, 350)
score_display.write(f"Счёт: {score}", font=("Arial", 16, "normal"))


def move_left():
    global curcoor
    if curcoor > 0:
        curcoor -= 1
        ark.setx(coor_x[curcoor])


def move_right():
    global curcoor
    if curcoor < 2:
        curcoor += 1
        ark.setx(coor_x[curcoor])


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")


def propadanie(objj, y=-410, leftb=300, rightb=1400):
    global coor_x

    if y < -400:
        x_new = random.choice(coor_x)
        y_new = random.randint(leftb, rightb)
        objj.goto(x_new, y_new)


def checking_match(listOfObjects, objectt):
    for objj in listOfObjects:
        if objj.ycor() < 1100 and objectt.ycor() < 1100:
            if objectt != objj and objectt.distance(objj) < 20:
                propadanie(objectt, leftb=1100)


def checking_match1(listOfObjects, objectt):
    count = 0
    for objj in listOfObjects:
        if objectt != objj and (abs(objectt.ycor() - objj.ycor()) < 20):
            count += 1
            if count > 2:
                propadanie(objj, -410)

fall_speed = 4
speed_increase_interval = 10
speed_multiplier = 1.2
last_speed_increase_time = time.time()

while isPlaying:
    current_time = time.time()
    if current_time - last_speed_increase_time > speed_increase_interval:
        fall_speed *= speed_multiplier
        last_speed_increase_time = current_time

    screen.update()

    for apple in apples:
        y = apple.ycor()
        y -= fall_speed
        apple.sety(y)
        checking_match(apples, apple)
        propadanie(apple, y=y)

        if (abs(apple.xcor() - coor_x[curcoor]) < 20) and (abs(apple.ycor() - ark.ycor()) < 20):
            score += 1
            score_display.clear()
            score_display.write(f"Счёт: {score}", font=("Arial", 16, "normal"))
            propadanie(apple)

    for obstacle in obstacles:
        y = obstacle.ycor()
        y -= fall_speed
        obstacle.sety(y)
        checking_match(apples, obstacle)
        checking_match(obstacles, obstacle)
        propadanie(obstacle, y=y)
        checking_match1(obstacles, obstacle)

        if (abs(obstacle.xcor() - coor_x[curcoor]) < 4) and (abs(obstacle.ycor() - ark.ycor()) < 4):
            isPlaying = False

    time.sleep(0.017)
kist.clear()
kist.penup()
kist.goto(0, 0)
kist.pendown()
kist.write(f"Игра окончена!\nВаш счет: {score}", align="center", font=("Courier", 24, "normal"))
kist.hideturtle()
screen.bgcolor("white")
def end_of_the_game(list_of_objects):
    for objj in list_of_objects :
        objj.hideturtle()
        screen.update()
end_of_the_game(apples)
end_of_the_game(obstacles)
score_display.clear()
ark.hideturtle()
screen.update()
turtle.done()