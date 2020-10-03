import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # with this the game runs much faster because the window doesnt update by it self

name1 = input("enter name: ")
name2 = input("enter name: ")
score1 = 0
score2 = 0
# Paddle1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.penup()
paddle1.goto(-380, 0)
paddle1.shapesize(stretch_wid=5, stretch_len=1)

# Paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.penup()
paddle2.goto(380, 0)
paddle2.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(name1 + ": " + str(score1) + "          " + name2 + ": " + str(score2), align="center",
          font=("Courier", 24, "normal"))


def paddle1_up():
    y = paddle1.ycor()
    y += 40
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 40
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 40
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 40
    paddle2.sety(y)


wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")
# Main game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if paddle1.ycor() > 240:
        paddle1.sety(240)
    if paddle1.ycor() < -240:
        paddle1.sety(-240)
    if paddle2.ycor() > 240:
        paddle2.sety(240)
    if paddle2.ycor() < -240:
        paddle2.sety(-240)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write(name1 + ": " + str(score1) + "          " + name2 + ": " + str(score2), align="center",
                  font=("Courier", 24, "normal"))
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write(name1 + ": " + str(score1) + "           " + name2 + ": " + str(score2), align="center",
                  font=("Courier", 24, "normal"))

    # Ball and paddle collision
    if (ball.xcor() > 370 and ball.xcor() < 380) and (
            ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(370)
        ball.dx *= -1
    if (ball.xcor() < -370 and ball.xcor() > -380) and (
            ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-370)
        ball.dx *= -1

    if score1 == 10:
        pen1 = turtle.Turtle()
        pen1.speed(0)
        pen1.color("white")
        pen1.penup()
        pen1.hideturtle()
        pen1.goto(0, 0)
        pen1.write(name1 + " WINNER", align="center", font=("Courier", 50, "normal"))

    if score2 == 10:
        pen2 = turtle.Turtle()
        pen2.speed(0)
        pen2.color("white")
        pen2.penup()
        pen2.hideturtle()
        pen2.goto(0, 0)
        pen2.write(name2 + "WINNER", align="center", font=("Courier", 50, "normal"))
