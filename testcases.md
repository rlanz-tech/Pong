## Testcases

### TC-001: Ball-Kollision mit Wand

**ID:** TC-001  
**Beschreibung:** Der Ball soll bei Kontakt mit der oberen Wand korrekt abprallen.  
**Vorbedingungen:** Spiel läuft, Ball bewegt sich nach oben.

**Schritte:**

1.  Spiel starten
2.  Ball Richtung obere Wand bewegen lassen
3.  Kollision abwarten

**Erwartetes Ergebnis:**  
– Ball ändert Y‑Richtung von + nach −

**Tatsächliches Ergebnis:**  
– Ball ändert Y‑Richtung von + nach −

**Status:** Funktioniert

***

### TC-002: Punktgewinn Spieler A

**ID:** TC-002  
**Beschreibung:** Spieler A erhält einen Punkt, wenn der Ball die rechte Grenze passiert.  
**Vorbedingungen:** Spiel läuft.

**Schritte:**

1.  Ball auf die rechte Seite spielen
2.  Ball muss Grenze überschreiten

**Erwartetes Ergebnis:**  
– Score\[A] = Score\[A] + 1

**Tatsächliches Ergebnis:**  
– Score\[A] = Score\[A] + 1

**Status:** Funktioniert

**Aber:**  
Zahlen wurden anfangs übereinander geschrieben, da der Score mit dem Pen gezeichnet wurde.

**Lösung:**  
– Vor neuem Score wird `pen.clear()` ausgeführt, damit der alte Score entfernt wird.

***

### TC-003: Paddle bewegt sich nach oben

**ID:** TC-003  
**Beschreibung:** Das Paddle soll sich nach oben bewegen, wenn die entsprechende Taste gedrückt wird.  
**Vorbedingungen:** Spiel läuft.

**Schritte:**

1.  Taste **W** (Spieler A) oder **↑** (Spieler B) drücken
2.  Bewegung beobachten

**Erwartetes Ergebnis:**  
– Paddle.y erhöht sich → Paddle bewegt sich nach oben

**Tatsächliches Ergebnis:**  
– paddle.y erhöht sich -> Paddle bewegt sich nach oben

**Status:** Funktioniert

***

### TC-004: Tasteneingabe – gleichzeitige Eingaben

**ID:** TC-004  
**Beschreibung:** Mehrere gleichzeitige Tasteneingaben sollen korrekt verarbeitet werden.  
**Vorbedingungen:** Spiel läuft, beide Spieler können Eingaben machen.

**Schritte:**

1.  Spieler A hält eine Taste gedrückt
2.  Spieler B drückt gleichzeitig eine Bewegungstaste
3.  Bewegung beider Paddles beobachten

**Erwartetes Ergebnis:**  
– Beide Tasten werden verarbeitet  
– Beide Paddles bewegen sich gleichzeitig

**Tatsächliches Ergebnis:**  
– Zuvor wurde bei zwei Tasten nur die zuletzt gedrückte verwendet

**Status:** Funktioniert nach Fix

**Lösung:**  
– Die Eingabewerte werden für jede Taste (w, W, s, S, Pfeil hoch, Pfeil runter) in einem Bool gespeichert  
– Sind mehrere Booleans aktiv, werden mehrere Funktionen ausgeführt  
– Dadurch können mehrere Inputs gleichzeitig verarbeitet werden

***

### TC-005: Schläger-Begrenzung am Spielfeldrand

**ID:** TC-005  
**Beschreibung:** Die Paddles sollen nicht über den oberen oder unteren Spielfeldrand hinausragen.  
**Vorbedingungen:** Spiel läuft.

**Schritte:**

1.  Paddle nach oben bewegen
2.  Paddle nach unten bewegen
3.  Verhalten am Rand beobachten

**Erwartetes Ergebnis:**  
– Paddle stoppt am oberen Rand  
– Paddle stoppt am unteren Rand

**Tatsächliches Ergebnis:**  
– Zuvor gingen die Schläger über den Rand hinaus

**Status:** Funktioniert nach Fix

**Lösung:**  
– Vor jeder Bewegung wird die Paddle‑Position in y‑Richtung abgefragt  
– Bewegung wird nur ausgeführt, wenn der Paddle nicht den Spielfeldrand überschreiten würde

***

### TC-006: Ballfarbe – Farbwechsel bei Schlägerkontakt

**ID:** TC-006  
**Beschreibung:** Der Ball soll bei jeder Schlägerberührung die Farbe wechseln. Die Farbfolge muss korrekt durchlaufen werden und sich nach dem Reset wieder auf die Startfarbe zurücksetzen.(nach jeder nur aus Testzwecken, im Spiel wird es mehr sein)
**Vorbedingungen:** Spiel läuft, Farbwechsel-Liste ist definiert.

**Schritte:**

1.  Ball mehrmals abwechselnd an beide Schläger spielen
2.  Farbänderungen beobachten
3.  Punkt erzielen → Ball reset
4.  Prüfen, ob Startfarbe korrekt wiederhergestellt wird
5.  Farbwechsel-Liste vollständig durchlaufen und prüfen, ob sie anschließend wieder vorne beginnt

**Erwartetes Ergebnis:**  
– Bei jeder Schlägerberührung wechselt die Ballfarbe  
– Die Startfarbe bestimmt die Reset-Farbe  
– Die Frequenz des Farbwechsels stimmt  
– Nach Ende der Liste beginnt sie wieder vorne

**Tatsächliches Ergebnis:**  
– Alles wie erwartet, keine Probleme festgestellt

**Status:** Funktioniert

**Lösung:**  
– Keine Fehlerkorrektur notwendig, alle Verhalten wurden mit „ja“ bestätigt
