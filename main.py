# Hauptloop

import logic

# Standardwerte in Variablen
# Anmerkung: Im Vollbild stimmt die Posistion der Schläger nicht mehr
bar_width = 5
bar_height = 1
barstartpos = 350
bar_speed = 20

score_one = 0
score_two = 0

# Optische Wiedergabe des Spielfensters, Schläger (Robin Lanz) und Ball (Sebastian Hacker) und Scoreboard (Christina Kaiser) werden erstellt.
wn = logic.create_window()
bar_left, bar_right = logic.create_bars(bar_width, bar_height, barstartpos) 
ball = logic.create_ball()

logic.create_scoreboard()

# Tasteneingabe führt Bewegungsfunktion aus (Robin Lanz)
wn.listen()
wn.onkeypress(lambda: logic.bar_left_up(bar_left, bar_speed), "w")
wn.onkeypress(lambda: logic.bar_left_down(bar_left, bar_speed), "s")
wn.onkeypress(lambda: logic.bar_right_up(bar_right, bar_speed), "Up")
wn.onkeypress(lambda: logic.bar_right_down(bar_right, bar_speed), "Down")


while True:
    wn.update()

    # Ballbewegung (Sebastian Hacker)
    logic.move_ball(ball)

    # Kollisionserkennung mit den Grenzen(Fabian Thiele)
    logic.collision_border(ball)

    # Kollision von Schläger und Ball (Christina Kaiser)
    logic.collision_bar(ball, bar_left, bar_right)

