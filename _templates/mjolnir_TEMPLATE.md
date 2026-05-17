<!-- TEMPLATE | Kopie als mjolnir.md ins Projekt-Root | Coda überschreibt diese Datei am Session-Ende, ausnahmslos -->

# mjolnir.md — {PROJEKT}

```
STATUS|{FERTIG|IN_ARBEIT|BLOCKIERT}|AUFTRAG: {Kurzname}|FORTSCHRITT: {X von Y Sessions} / {Phasen-Stand}|NÄCHSTE SESSION: {was zuerst dran ist} | entfällt (FERTIG)
```

**STATUS:** FERTIG | IN_ARBEIT | BLOCKIERT
**AUFTRAG:** {Kurzname}
**FORTSCHRITT:** {X von Y Sessions} | {Phasen-Stand}
**NÄCHSTE SESSION:** {was zuerst dran ist} | entfällt (FERTIG)
**WARNUNG:** {nur wenn IN_ARBEIT/BLOCKIERT} KEINEN NEUEN FEATURE_REQUEST SCHICKEN — laufender Auftrag noch nicht durch

---

## Was Chris physisch tun muss

{Nur Dinge die Coda nicht selbst kann: Touch-Tests, echte Geräte, Mikrofon, UI-Klicks die kein Skript erreicht, App-Store-Push, Hardware-Reset}

Wenn nichts physisch nötig: hier `— nichts —` schreiben. NICHT die Sektion löschen.

---

## Auftragshistorie (kurz)

{1-3 Zeilen: was wurde gemacht, was hat funktioniert, was nicht. Beispiel: "Phase A-D durchgelaufen, Push grün, Selbsttest C hat einmal angeschlagen — Schutz nachgezogen."}

---

<!--
LIFECYCLE-Notiz für Coda:

- STATUS=FERTIG  →  beim nächsten Session-Start: mjolnir.md einlesen, dann löschen. FEATURE_REQUEST_{PROJEKT}.md zu _ERLEDIGT.md umbenennen.
- STATUS=IN_ARBEIT  →  beim nächsten Session-Start: mjolnir.md einlesen, FORTSCHRITT-Block prüfen, laufenden Auftrag fortsetzen. FEATURE_REQUEST NICHT umbenennen. Falls neuer FEATURE_REQUEST mit abweichendem Kurznamen vorhanden: zu _QUEUED.md umbenennen.
- STATUS=BLOCKIERT  →  beim nächsten Session-Start: mjolnir.md einlesen, DECISIONS_PENDING.md prüfen, BLOCKER auflösen oder eskalieren. FEATURE_REQUEST NICHT umbenennen.

mjolnir.md ist Single-Slot — genau EINE Datei zur Zeit, wird beim nächsten Session-Start gelöscht. _ERLEDIGT.md ist Audit-Log (akkumuliert).
-->
