# Spielfenster für Pong mit der turtlebibliothek

import turtle

# Fenster erstellen (Fabian Thiele)
def create_window():
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    return wn

# Schläger erstellen (Robin Lanz)
def create_bars(barwidth, barheight, barstartpos):
        bar_left = turtle.Turtle()
        bar_left.speed(0)
        bar_left.shape("square")
        bar_left.color("white")
        bar_left.shapesize(stretch_wid = barwidth, stretch_len = barheight)
        bar_left.penup()
        bar_left.goto(-barstartpos, 0)

        bar_right = turtle.Turtle()
        bar_right.speed(0)
        bar_right.shape("square")
        bar_right.color("white")
        bar_right.shapesize(stretch_wid = barwidth, stretch_len = barheight)
        bar_right.penup()
        bar_right.goto(barstartpos, 0)
        return bar_left, bar_right

# Schläger bewegen (Robin Lanz)
def bar_left_up(bar, speed):
    y = bar.ycor()
    y += speed
    bar.sety(y)

def bar_left_down(bar, speed):
    y = bar.ycor()
    y -= speed
    bar.sety(y)

def bar_right_up(bar, speed):
    y = bar.ycor()
    y += speed
    bar.sety(y)

def bar_right_down(bar, speed):
    y = bar.ycor()
    y -= speed
    bar.sety(y)

# Ball erstellen -> Grafische Visualisierung (Sebastian Hacker) 
def create_ball():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)

# Scoreboard erstellen (Christina Kaiser)
# pen beschreibt eine unsichtbare tutrle, die zum Schreiben des Scoreboards benutzt wird
def create_scoreboard():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("White")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 26, "normal"))
