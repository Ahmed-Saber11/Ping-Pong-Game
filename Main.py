from screen_setup import create_screen
from paddles import create_paddle, move_up, move_down
from ball import create_ball
from scoreboard import create_scoreboard, update_score

import turtle

wind = create_screen()

paddle1 = create_paddle(-350, "blue")
paddle2 = create_paddle(350, "red")

 
ball = create_ball()

 
score1 = 0
score2 = 0
score = create_scoreboard()
update_score(score, score1, score2)


wind.listen()
wind.onkeypress(lambda: move_up(paddle1), 'w')
wind.onkeypress(lambda: move_down(paddle1), 's')
wind.onkeypress(lambda: move_up(paddle2), 'Up')
wind.onkeypress(lambda: move_down(paddle2), 'Down')

# Game loop
while True:
    wind.update()

     
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dy *= -1

    if (340 < ball.xcor() < 350) and (paddle2.ycor() + 40 > ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        score1 += 1
        update_score(score, score1, score2)

    if (-350 < ball.xcor() < -340) and (paddle1.ycor() + 40 > ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        score2 += 1
        update_score(score, score1, score2)
