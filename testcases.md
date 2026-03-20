# Testcases – Projekt Pong

## Testcase 1: Ball-Kollision mit Wand
**ID:** TC-001  
**Beschreibung:** Der Ball soll bei Kontakt mit der oberen Wand korrekt abprallen.  
**Vorbedingungen:** Spiel läuft, Ball bewegt sich nach oben.  
**Schritte:**
1. Spiel starten
2. Ball Richtung obere Wand bewegen lassen
3. Kollision abwarten
**Erwartetes Ergebnis:** Ball ändert Y-Richtung von + zu -.  
**Tatsächliches Ergebnis:**  
**Status:** Funktioniert  
---

## Testcase 2: Punktgewinn Spieler A
**ID:** TC-002  
**Beschreibung:** Spieler A erhält einen Punkt, wenn der Ball die rechte Grenze passiert.  
**Vorbedingungen:** Spiel läuft.  
**Schritte:**
1. Ball auf die rechte Seite spielen
2. Ball muss Grenze überschreiten
**Erwartetes Ergebnis:** Score[A] = Score[A] + 1  
**Tatsächliches Ergebnis:**  
**Status:** Funktioniert  
---
**Aber:** Am Anfang wurden die Zahlen alle übereinander geschrieben, da wir es mit dem Pen gelöst haben
**Lösung:** Es wird sobald ein neuer Score vorliegt der alte "wegradiert" und der neue hingeschrieben

## Testcase 3: Paddle bewegt sich nach oben
**ID:** TC-003  
**Beschreibung:** Das Paddle soll sich nach oben bewegen, wenn der entsprechende Key gedrückt wird.  
**Vorbedingungen:** Spiel läuft.  
**Schritte:**
1. Taste „W“ (Spieler A) oder „↑“ (Spieler B) drücken
2. Bewegung beobachten
**Erwartetes Ergebnis:** Paddle.y erhöht sich (bewegt nach oben).  
**Tatsächliches Ergebnis:**  
**Status:** Funktioniert

**Aber:**
Wenn eine Taste gehalten wird von Spieler A und Spieler B seinen Paddle bewegen möchte unterbricht die Bewegung von Spieler A
**Lösung:**

