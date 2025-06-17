import turtle

def create_scoreboard():
    score_turtle = turtle.Turtle()
    score_turtle.speed(0)
    score_turtle.color('white')
    score_turtle.penup()
    score_turtle.hideturtle()
    score_turtle.goto(0, 260)
    return score_turtle

def update_score(score_turtle, score1, score2):
    score_turtle.clear()
    score_turtle.write(f"Player 1 : {score1}  player 2 : {score2}", align="center", font=("Courier", 24, "normal"))
