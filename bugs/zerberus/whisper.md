# Whisper / Voice — Bug-Tracker (Zerberus)

## Offen

### W-001 Phrasen-Repetition-Loop
**Severity:** Hoch — Datenverlust
**Betrifft:** legacy.py /voice, nala.py /voice
**Erfasst:** 2026-04-19

Whisper erzeugt mittendrin im Transkript Phrasen-Loops, bei denen ganze Sätze wiederholt werden bis das Segment voll ist. Nicht nur am Ende, sondern mitten im Text — dadurch geht echter Content verloren.

Beispiel: "ist das zu dem wie du das tust ist das zu dem wie du in deinem universum bist" in Endlosschleife.

**Warum bestehender Cleaner nicht greift:**
Bestehende Patterns fangen nur Einzelwort-Duplikate (`\b(\w{2,})\s+\1\b`) und hardcodierte Phrasen. Generische Phrasen-Loops rutschen komplett durch.

**Lösung:**
Python-basierter Phrasen-Repetitions-Detektor als neuer Schritt in der Cleaner-Pipeline, VOR den Regex-Regeln. Sliding-Window über N-Gramme (4-6 Wörter), erkennt Wiederholungen ab 2x, behält erstes Vorkommen, schneidet Rest. Kein Regex — echte Python-Logik. Muss in BEIDE Voice-Endpoints (legacy.py UND nala.py /voice).

---

## Erledigt

(noch leer)
