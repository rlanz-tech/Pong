# Hauptloop

import logic

# Standardwerte in Variablen
bar_width = 5
bar_height = 1
barstartpos = 350
bar_speed = 20

wn = logic.create_window()

bar_left, bar_right = logic.create_bars(bar_width, bar_height, barstartpos)     # Importieren der Objekte Schläger aus logic.py

# Tasteneingabe führt Bewegungsfunktion aus (Robin Lanz)
wn.listen()
wn.onkeypress(lambda: logic.bar_left_up(bar_left, bar_speed), "w")
wn.onkeypress(lambda: logic.bar_left_down(bar_left, bar_speed), "s")
wn.onkeypress(lambda: logic.bar_right_up(bar_right, bar_speed), "Up")
wn.onkeypress(lambda: logic.bar_right_down(bar_right, bar_speed), "Down")



while True:
    wn.update()