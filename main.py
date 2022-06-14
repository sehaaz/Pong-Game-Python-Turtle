from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ball = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen = Screen()

scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        ball.reset_position()

    if ball.xcor() < -400:
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        ball.reset_position()

screen.exitonclick()
