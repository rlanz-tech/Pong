# Hauptloop

import logic

# Standardwerte in Variablen
bar_width = 5
bar_height = 1
barstartpos = 350

wn = logic.create_window()
logic.create_bars(bar_width, bar_height, barstartpos)


while True:
    wn.update()