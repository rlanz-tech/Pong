# Hauptloop

import logic

# Standardwerte in Variablen
bar_width = 5
bar_height = 1
barstartpos = 350

# Optische Wiedergabe des Spielfensters: Bars(Robin Lanz) und Ball(Sebastian Hacker)
wn = logic.create_window()
logic.create_bars(bar_width, bar_height, barstartpos)
logic.create_ball()

while True:
    wn.update()