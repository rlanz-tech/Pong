# Hauptloop

import logic

# Standardwerte in Variablen
bar_width = 5
bar_height = 1
barstartpos = 350

wn = logic.create_window()
#logic.create_bars(logic.bar_width, logic.bar_height, logic.barstartpos)


while True:
    wn.update()
    logic.create_bars(bar_width, bar_height, barstartpos)