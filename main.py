# Hauptloop

import logic
import time 

# Standardwerte in Variablen
# Anmerkung: Im Vollbild stimmt die Posistion der Schläger nicht mehr
bar_width = 5
bar_height = 1
barstartpos = 350
bar_speed = 5   # Update: Nach neuem Tasteninput Geschwindigkeit angepasst (Robin Lanz)

# Punktestand wird auf Null gesetzt 
score_one = 0
score_two = 0

# Optische Wiedergabe des Spielfensters, Schläger (Robin Lanz) und Ball (Sebastian Hacker) und Scoreboard (Christina Kaiser) werden erstellt.
wn = logic.wn
bar_left, bar_right = logic.create_bars(bar_width, bar_height, barstartpos) 
ball = logic.create_ball()
pen = logic.create_scoreboard()

while True:
    # sleep Sorgt dafür, dass die Geschwindigkeit regelmäßiger ist. max. 0.01 ~ 100 fps. Wenn diese Anzahl unterschritten wird, trotzdem ungleichmäßiges v(Ball) (Sebastian Hacker)
    time.sleep(0.01)
    wn.update()

    # Ballbewegung (Sebastian Hacker)
    logic.move_ball(ball)

    # Kollisionserkennung mit den Grenzen(Fabian Thiele)
    # Funktion gibt den aktuellen Punktestand zurück
    score_one, score_two = logic.collision_border(ball, pen, score_one, score_two)

    # Kollision von Schläger und Ball (Christina Kaiser)
    logic.collision_bar(ball, bar_left, bar_right)

    # Tasteninput abfragen (Robin Lanz )
    if logic.key_w:
        logic.bar_left_up(bar_left, bar_speed)      # führt Bewegung des linken Schlägers nach oben aus
    if logic.key_s:
        logic.bar_left_down(bar_left, bar_speed)    # führt Bewegung des linken Schlägers nach unten aus
    if logic.key_up:
        logic.bar_right_up(bar_right, bar_speed)    # führt Bewegung des rechten Schlägers nach oben aus
    if logic.key_down:
        logic.bar_right_down(bar_right, bar_speed)  # führt Bewegung des rechten Schlägers nach unten aus