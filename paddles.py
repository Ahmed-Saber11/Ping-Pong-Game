import turtle

def create_paddle(x_pos, color):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(color)
    paddle.shapesize(stretch_wid=4, stretch_len=1)
    paddle.penup()
    paddle.goto(x_pos, 0)
    return paddle

def move_up(paddle):
    y = paddle.ycor()
    paddle.sety(y + 20)

def move_down(paddle):
    y = paddle.ycor()
    paddle.sety(y - 20)
