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
    # Update: 13.03: Geschwindigkeit des Balls hinzugefügt. Return zur Benutzung im main.py ergänzt. (Sebastian Hacker)
    # Update: 19.03: Variable Farbe (Sebastian Hacker)
def create_ball():
    ball = turtle.Turtle()
    ball.speed(0)   
    ball.shape("square")
    ball.startcolor = "white"
    ball.color(ball.startcolor)
    ball.penup()
    ball.goto(0, 0)
    # Variable Farbe (Farben und Anzahl der Liste darf ohne weiteres verändert werden)
    ball.colorlst = ["green", "red", "blue", "purple"]
    ball.hitcount = 0
    # Ballgeschwindigkeit
    ball.xaxis = 2.5
    ball.yaxis = 2

    return ball    

#  Ball Bewegung berechnen ohne Kolision(Sebastian Hacker)
def move_ball(ball):
    ball.setx(ball.xcor() + ball.xaxis)
    ball.sety(ball.ycor() + ball.yaxis)

# Kollisionserkennung mit der Obergrenze und Untergrenze(Fabian Thiele)
# Score wird erhöht, wenn der Ball die Grenze auf einer x Seite berührt. Punktestand wird zurückgegeben, aktuallisiert und angezeigt.(Christina Kaiser)
    #Update: 19.03: Ballfarbe (Sebastian Hacker)
def collision_border(ball, pen, score_one, score_two):
    if ball.ycor() > 290:
        ball.sety(290)
        ball.yaxis *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.yaxis *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.xaxis *= -1
        score_one += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_one, score_two), align="center", font=("Courier", 26, "normal"))
        # Ballfarbe und Liste zurücketzen
        ball.hitcount = 0
        ball.color(ball.startcolor)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.xaxis *= -1
        score_two += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_one, score_two), align="center", font=("Courier", 26, "normal"))
        # Ballfarbe und Liste zurücketzen
        ball.hitcount = 0
        ball.color(ball.startcolor)

    return score_one, score_two


# Kollision von Schäger und Ball (Christina Kaiser)
    # Update: 19.03: If-Abfrage und hitcount (Sebastian Hacker)
def collision_bar(ball, bar_left, bar_right):
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bar_right.ycor() + 68 and ball.ycor() > bar_right.ycor() - 68):
        # If, damit der Ball nicht mehrmals die Kollision erkennt
        if ball.xaxis > 0:
            ball.setx(340)
            ball.xaxis *= -1
            #Farbe ändern
            ball.hitcount += 1
            ball.color(ball.colorlst[ball.hitcount %len(ball.colorlst)])

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bar_left.ycor() + 68 and ball.ycor() > bar_left.ycor() - 68):
        # If, damit der Ball nicht mehrmals die Kollision erkennt
        if ball.xaxis < 0:
            ball.setx(-340)
            ball.xaxis *= -1
            #Farbe ändern
            ball.hitcount += 1
            ball.color(ball.colorlst[ball.hitcount %len(ball.colorlst)])

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
    return pen
