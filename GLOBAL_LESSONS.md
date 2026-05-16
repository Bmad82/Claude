# GLOBAL_LESSONS — Marathon-Workflow

Universelle Lessons für ALLE Projekte, die den Marathon-Workflow nutzen (Coda + Supervisor + Mjölnir).
Projekt-spezifische Lessons gehören in `lessons/<projekt>_lessons.md`. Diese Datei nur für projektübergreifend gültige Regeln.

Format: jede Lesson eine `##` Sektion mit Datum + Anlass-Patch im Titel. Inhalt in Pipe-Format (`|`-getrennte Punkte), ggf. mit Begründung darunter. Nicht löschen — historische Lessons bleiben, neue oben anhängen.

---

## OBERSTES GEBOT (2026-05-16, Zerberus P-umzug)

Chris terminalisiert NICHTS was Coda kann|NIEMALS git/pytest/pip/robocopy/npm-Befehle an Chris delegieren|Coda merged Branches SELBST auf main + pusht SELBST vor Session-Ende|mjolnir.md enthält NUR was physisch unmöglich ist (Touch-Test, echtes Gerät, Docker Desktop UI)|Supervisor (Chat-Fenster) gibt KEINE Terminal-Befehle sondern baut Coda-Prompts (.md)|Verstoß = sofortige Korrektur

**Anlass:** Zerberus P-umzug 2026-05-16 — die vorige Coda-Session hatte den Worktree-Merge + Robocopy + Venv-Aufbau in `mjolnir.md` an Chris delegiert. Klassischer Coda-Faulheits-Verstoß. Das OBERSTE GEBOT zementiert die Trennung: mechanische Terminal-Arbeit ist Coda-Pflicht, mjolnir.md ist nur für Touch/Mikrofon/echtes-Gerät/externe-App-Tests.

**Backstop pro Projekt:** Als Regel 0 in `CLAUDE_<PROJEKT>.md` (vor jeder anderen Regel) plus als erste Sektion in `lessons_<PROJEKT>.md`.

---

## mjolnir.md ist PFLICHT am Session-Ende (2026-05-16, Zerberus B-072)

mjolnir.md wird am Ende JEDER Session überschrieben — ausnahmslos|Alte Version wird IMMER ersetzt|Ohne mjolnir.md-Update ist der Mjölnir-Round-Trip kaputt|Chris kann sonst nicht erkennen ob ein Auftrag abgeschlossen ist|Session-Zyklus Schritt 10 ist NICHT optional|Wenn Schritt 10 fehlt hat Schritt 11 (Push) auch keinen Wert weil Chris nichts davon erfährt

**Anlass:** Zerberus B-072 (Huginn Voice-to-Whisper) 2026-05-16 — Code + Tests + Commit + `_ERLEDIGT.md`-Audit waren komplett, aber `mjolnir.md` wurde nicht überschrieben. Chris hat über den ZUSAMMENFASSUNG-Button die alte P-umzug-Datei gefetcht und konnte B-072 nicht als erledigt sehen.

**Single-Slot vs Audit-Log:** `mjolnir.md` ist Single-Slot-State (genau EINE aktuelle Session-Zusammenfassung) — wird beim nächsten Session-Start eingelesen und gelöscht. `_ERLEDIGT.md` ist Audit-Log (akkumuliert, bleibt bis User es löscht). Beide Datei-Typen haben unterschiedliche Pflege-Regeln und dürfen nicht verwechselt werden.

---

## Worktree-Branches selbst auf main mergen (2026-05-16, Zerberus B-061)

Coda merged Worktree-Branches SELBST auf main vor Session-Ende|NIEMALS einen ungemergten Branch als "Schritt 0" in mjolnir.md an Chris delegieren|Das ist Terminal-Arbeit und fällt unter das OBERSTE GEBOT|Wenn ff-merge nicht möglich: rebase selbst durchführen oder Merge-Commit erstellen

**Anlass:** Zerberus B-061 (Pfad-Audit + Sync-Scripts) 2026-05-16 — Worktree-Branch lag fertig, vorige Coda-Session hatte den Merge nicht gemacht und Chris in `mjolnir.md` darum gebeten. Die nachfolgende Session musste den Merge im Hauptcheckout selbst durchführen plus den eigenen Worktree-Branch rebasen.

**Pattern:** `git stash push` für uncommitted Edits → `git merge --ff-only` → `git stash pop` → eigenen Worktree-Branch per `git rebase main` aktualisieren → ff-merge → push. Konfliktfrei wenn die Edits unterschiedliche Zeilen treffen.

---

## Supervisor-Verhalten: Coda-Prompts statt Terminal-Befehle (2026-05-16, Zerberus)

Wenn Chris ein Problem schildert das Coda lösen kann: Supervisor baut einen Coda-Prompt (.md-Datei) statt Chris Terminal-Befehle zu geben|Auch "nur ein Befehl" ist einer zu viel|Die Frage ist immer: "Kann Coda das selbst?" — Antwort ist in 95% der Fälle ja

**Anlass:** Zerberus 2026-05-16 — die Trennung Supervisor (plant, prüft, promptet) vs Coda (implementiert, testet) wird brüchig, wenn der Supervisor "nur einen kleinen Befehl" an Chris gibt. Das OBERSTE GEBOT gilt für beide Rollen: weder Coda-im-Code noch Supervisor-im-Chat delegieren Terminal-Arbeit an Chris.

**Konkretes Pattern für Supervisor:** wenn ein Schritt mehr als "Browser öffnen, klicken, sehen" verlangt → Coda-Prompt als `.md`-Datei (FEATURE_REQUEST oder Mjölnir-Auftrag), nicht ein Inline-PowerShell-Snippet im Chat.
