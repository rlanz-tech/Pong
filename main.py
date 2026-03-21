##############################################################################
#                                  Pong Spiel                                #
##############################################################################   
#                                                                            #      
# Version: 1.0 (Stand 20.03.2026)                                            #
# Autoren: Robin Lanz, Sebastian Hacker, Christina Kaiser, Fabian Thiele     #
# Spielbeschreibung:                                                         #
#   Pong Spiel für zwei Spieler, mit wachsender Schwierigkeit durch          #
#   zunehmende Geschwindigkeit des Balls.                                    #
#   Der erste mit 5 Punkten gewinnt.                                         #
#                                                                            #
##############################################################################


import logic
import time 

# Standardwerte in Variablen
bar_width = 1       # Breite der Schläger: width*20 (Robin Lanz)
bar_height = 5      # Höhe der Schläger: height*20 (Robin Lanz)
barstartpos = 350
barstoppos = 245    # Update: Endposition der Schläger definiert (Robin Lanz)
bar_speed = 5       # Update: Nach neuem Tasteninput Geschwindigkeit angepasst (Robin Lanz)

# Punktestand wird auf Null gesetzt 
score_one = 0
score_two = 0

# beschreibt den Spielzustand
game_active = False

# Optische Wiedergabe des Spielfensters, Schläger (Robin Lanz) und Ball (Sebastian Hacker) und Scoreboard (Christina Kaiser) werden erstellt.
wn = logic.wn
bar_left, bar_right = logic.create_bars(bar_width, bar_height, barstartpos) 
ball = logic.create_ball()
pen = logic.create_scoreboard()

# Notwendig, um Spiel zu starten, aktualisiert den Satuts und setzt Score zurück (Christina Kaiser)
def press_any_key():
    global game_active, score_one, score_two
    game_active, score_one, score_two = logic.game_start(game_active, score_one, score_two, ball, pen)

wn.onkeypress(press_any_key) # Reagiert auf jede taste zum Starten

logic.update_scoreboard(pen, score_one, score_two, status="start")

# Hauptloop
while True:
    wn.update()

    if game_active:
         # sleep Sorgt dafür, dass die Geschwindigkeit regelmäßiger ist. max. 0.01 ~ 100 fps. Wenn diese Anzahl unterschritten wird, trotzdem ungleichmäßiges v(Ball) (Sebastian Hacker)
        time.sleep(0.01)

        # Ballbewegung (Sebastian Hacker)
        logic.move_ball(ball)

        # Kollisionserkennung mit den Grenzen(Fabian Thiele)
        # Funktion gibt den aktuellen Punktestand zurück und speichert die alten Scores
        old_score_one, old_score_two = score_one, score_two
        score_one, score_two = logic.collision_border(ball, pen, score_one, score_two)

        # Scoreboard aktualisieren, wenn sich der Punktestand ändert
        if score_one != old_score_one or score_two != old_score_two:
            logic.update_scoreboard(pen, score_one, score_two, status="playing")

        # Kollision von Schläger und Ball (Christina Kaiser)
        logic.collision_bar(ball, bar_left, bar_right)

        if score_one >= 5 or score_two >= 5:
            game_active = False
            ball.hideturtle()
            ball.goto(0, 0)
            logic.update_scoreboard(pen, score_one, score_two, status="game_over")

        # Tasteninput abfragen (Robin Lanz )
        if logic.key_w:
            logic.bar_left_up(bar_left, bar_speed, barstoppos)      # führt Bewegung des linken Schlägers nach oben aus
        if logic.key_s:
            logic.bar_left_down(bar_left, bar_speed, barstoppos)    # führt Bewegung des linken Schlägers nach unten aus
        if logic.key_up:
            logic.bar_right_up(bar_right, bar_speed, barstoppos)    # führt Bewegung des rechten Schlägers nach oben aus
        if logic.key_down:
            logic.bar_right_down(bar_right, bar_speed, barstoppos)  # führt Bewegung des rechten Schlägers nach unten aus

    else:
        time.sleep(0.1)

