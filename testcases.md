# Testcases – Projekt Pong

## Testcase 1: Ball-Kollision mit Wand
**ID:** TC-001  
**Beschreibung:** Der Ball soll bei Kontakt mit der oberen Wand korrekt abprallen.  
**Vorbedingungen:** Spiel läuft, Ball bewegt sich nach oben.  

**Schritte:**  
1. Spiel starten  
2. Ball Richtung obere Wand bewegen lassen  
3. Kollision abwarten  

**Erwartetes Ergebnis:**  
- Ball ändert Y-Richtung von + nach −  

**Tatsächliches Ergebnis:**  
- (Eintragen nach Test)

**Status:** Funktioniert  

---

## Testcase 2: Punktgewinn Spieler A
**ID:** TC-002  
**Beschreibung:** Spieler A erhält einen Punkt, wenn der Ball die rechte Grenze passiert.  
**Vorbedingungen:** Spiel läuft.  

**Schritte:**  
1. Ball auf die rechte Seite spielen  
2. Ball muss Grenze überschreiten  

**Erwartetes Ergebnis:**  
- Score[A] = Score[A] + 1  

**Tatsächliches Ergebnis:**  
- (Eintragen nach Test)

**Status:** Funktioniert  

**Aber:**  
Zahlen wurden anfangs übereinander geschrieben, da der Score mit dem Pen gezeichnet wurde.

**Lösung:**  
- Vor neuem Score wird `pen.clear()` ausgeführt, damit der alte Score entfernt wird.

---

## Testcase 3: Paddle bewegt sich nach oben
**ID:** TC-003  
**Beschreibung:** Das Paddle soll sich nach oben bewegen, wenn die entsprechende Taste gedrückt wird.  
**Vorbedingungen:** Spiel läuft.  

**Schritte:**  
1. Taste **W** (Spieler A) oder **↑** (Spieler B) drücken  
2. Bewegung beobachten  

**Erwartetes Ergebnis:**  
- Paddle.y erhöht sich → Paddle bewegt sich nach oben  

**Tatsächliches Ergebnis:**  
- (Eintragen nach Test)

**Status:** Funktioniert  

**Aber:**  
Wenn Spieler A eine Taste gedrückt hält und Spieler B eine Bewegung startet, wurde die Bewegung von Spieler A unterbrochen.

**Lösung:**  
- Einführung einer Key-State-Verarbeitung:  
  - `onkeypress` → Taste als aktiv merken  
  - `onkeyrelease` → Taste wieder lösen  
  - Game Loop bewegt Paddles anhand aller aktiven Tasten  
- Dadurch können beide Spieler gleichzeitig steuern.

---

## Testcase 4: Gleichzeitige Tasteneingaben
**ID:** TC-004  
**Beschreibung:** Beide Spieler sollen ihre Paddles gleichzeitig bewegen können.  
**Vorbedingungen:** Spiel läuft.  

**Schritte:**  
1. Spieler A hält **W** gedrückt  
2. Spieler B drückt währenddessen **↑**  
3. Bewegung beider Paddles beobachten  
4. Weitere Kombinationen testen (W + ↑, S + ↓)  

**Erwartetes Ergebnis:**  
- Beide Paddles bewegen sich unabhängig voneinander  
- Keine Eingabe blockiert sich gegenseitig  
- Bewegung bleibt stabil  

**Tatsächliches Ergebnis:**  
- (Eintragen nach Test)

**Status:**  
- (Funktioniert / Fehlerhaft – später eintragen)

---

## Zusätzliche Probleme & Lösungen

### Problem: W, S, ↑, ↓ funktionierten am Anfang nicht
**Grund:**  
- Turtle-Ereignisse haben Tasten festgehalten  
- Tasten wurden dauerhaft als „gedrückt“ behandelt  
- Paddles liefen aus dem Bild  
- Manche Tasten funktionierten nicht mehr  

**Lösung:**  
- Keine blockierenden Schleifen in Tastenevents  
- Verwendung des Key-State-Systems zur stabilen Eingabeverarbeitung  
- Begrenzungen der Paddle-Position (z. B. `MAX_Y`)  
- Beispiel:
  ```python
  if paddle.ycor() < MAX_Y:
      paddle.sety(paddle.ycor() + speed)
