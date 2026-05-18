# FEATURE_REQUEST: Integration Faulheits-Catches in globale Templates

**Datum:** 2026-05-17
**Auftraggeber:** Supervisor (Chat-Fenster)
**Empfänger:** Coda
**Kurzname:** faulheits-catch-integration
**Erwartete Dauer:** 1 Session

---

## Kontext

Chris hat in `Try_Faulheits_catch.md` sechs Faulheits-Catches plus
das Selbsttest-Pattern formalisiert. Das ist die operative Verfassung
des Marathon-Workflows und muss überall greifen — sowohl in bestehenden
Projekten (rückwirkend) als auch in neuen Projekten (automatisch beim
Bootstrap).

Quelle: `C:\Users\chris\Python\Claude\Try_Faulheits_catch.md`

Dieser Auftrag macht aus dem Konzept-Dokument eine durchgreifende
Strukturänderung im `Claude/`-Verzeichnis.

---

## Akzeptanzkriterien (TL;DR)

- [ ] `Claude/GLOBAL_LESSONS.md` existiert oder ist um die 6 Catches ergänzt
- [ ] `Claude/SUPERVISOR_KODEX.md` existiert (NIE/IMMER-Listen für Chat-Instanzen)
- [ ] `Claude/_templates/mjolnir_TEMPLATE.md` enthält Multi-Session-Status-Header
- [ ] `Claude/_templates/FEATURE_REQUEST_TEMPLATE.md` existiert mit Lifecycle-Hinweisen
- [ ] `Claude/PROJECT_BOOTSTRAP_README.md` existiert und referenziert die Catches
- [ ] Verzeichnisstruktur ist verifiziert (Listing am Ende)
- [ ] Selbsttest mit Dummy-Projekt ist durchgelaufen (Phase A-D)
- [ ] Commit + Push erfolgt mit `$LASTEXITCODE = 0` verifiziert
- [ ] `mjolnir.md` enthält STATUS=FERTIG-Header

---

## Schritt 01 — Bestandsaufnahme

Liste den Inhalt von `Claude/` auf. Stelle fest:

- Existiert bereits ein `GLOBAL_LESSONS.md`? Wenn ja, was steht drin?
- Existiert ein `_templates/`-Verzeichnis? Wenn ja, welche Files?
- Existiert `SUPERVISOR_KODEX.md`?
- Existiert `PROJECT_BOOTSTRAP_README.md`?
- Wo liegt aktuell `Try_Faulheits_catch.md`? (Quelle nicht löschen, nur lesen)

Ergebnis als kurze Liste in den Patch-Notes festhalten.

---

## Schritt 02 — `GLOBAL_LESSONS.md` erstellen oder ergänzen

Wenn `Claude/GLOBAL_LESSONS.md` **nicht existiert**: Datei neu anlegen.
Wenn sie **existiert**: die 6 Catches als Sektion hinten anhängen,
existierende Inhalte nicht verändern.

Format der Datei: prosaischer Header + Bibel-Format-Lessons.

Die 6 Lessons im Bibel-Format aus `Try_Faulheits_catch.md` übernehmen.
Die Anlass-Blöcke (B-072, B-061 etc.) prosaisch direkt unter jeder
Lesson lassen — das ist die menschenlesbare Kontextschicht.

Pflicht-Sektionen in `GLOBAL_LESSONS.md`:

1. Header (Datum, Geltungsbereich, Quelle)
2. **Die 6 Faulheits-Catches** (Bibel-Format + Anlass)
3. **Selbsttest-Pattern** (Phase A/B/C/D, prosaisch)
4. **Bibel-Format Cheat Sheet** (wie in der Quelle)

---

## Schritt 03 — `SUPERVISOR_KODEX.md` anlegen

Neue Datei `Claude/SUPERVISOR_KODEX.md`. Inhalt: die NIE/IMMER-Listen
aus `Try_Faulheits_catch.md`, plus Bibel-Format-Zeile am Anfang:

```
KODEX|für Chat-Fenster (Supervisor-Rolle)|gilt für ALLE Projekte|Verstoß = sofortige Korrektur
```

Dann prosaisch:

**Was Supervisor NIE darf:**
- Chris Terminal-Befehle geben (git, pytest, pip, robocopy, npm, cd, …)
- Chris als Mensch-im-Loop für Routine-Arbeit einbauen
- Mehrere Dateien als Coda-Input ohne klare Trennung welche der FEATURE_REQUEST ist und welche Vorlage
- Auf Coda-Erfolg hoffen statt mit Selbsttest verifizieren

**Was Supervisor IMMER muss:**
- Coda-Prompt als `.md`-Datei (Ein-Klick-Kopier-fähig)
- Akzeptanzkriterien als Checkliste am Ende
- Bei Workflow-Themen: Selbsttest-Pflicht in den Prompt schreiben
- Bei Unsicherheit: lieber zu paranoid spezifizieren als zu locker

---

## Schritt 04 — Template-Verzeichnis aufbauen

Erzeuge `Claude/_templates/` falls nicht vorhanden.

### 04a — `mjolnir_TEMPLATE.md`

```
# mjolnir.md — {PROJEKT}

**STATUS:** FERTIG | IN_ARBEIT | BLOCKIERT
**AUFTRAG:** {Kurzname}
**FORTSCHRITT:** {X von Y Sessions} | {Phasen-Stand}
**NÄCHSTE SESSION:** {was zuerst dran ist} | entfällt (FERTIG)
**WARNUNG:** {nur wenn IN_ARBEIT/BLOCKIERT} KEINEN NEUEN FEATURE_REQUEST SCHICKEN

---

## Was Chris physisch tun muss

{Nur Dinge die Coda nicht selbst kann: Touch-Tests, echte Geräte, UI-Klicks die kein Skript erreicht}

---

## Auftragshistorie (kurz)

{1-3 Zeilen: was wurde gemacht, was hat funktioniert, was nicht}
```

### 04b — `FEATURE_REQUEST_TEMPLATE.md`

Vorlage mit Pflichtfeldern: Kurzname, Auftraggeber, Empfänger,
Kontext, Akzeptanzkriterien, Schritte, Selbsttest-Block falls
Workflow-relevant.

Lifecycle-Hinweis am Ende des Templates:

```
LIFECYCLE|FERTIG: rename zu *_ERLEDIGT.md|IN_ARBEIT: Datei bleibt|BLOCKIERT: Datei bleibt + Grund in DECISIONS_PENDING.md
```

### 04c — `CLAUDE_PROJEKT_TEMPLATE.md`

Skelett für `CLAUDE_{PROJEKT}.md`. Maximal 150 Zeilen. Enthält
Hinweise auf GLOBAL_LESSONS.md und SUPERVISOR_KODEX.md damit
Coda bei neuen Projekten weiß wo der Globale Stand liegt.

### 04d — `SUPERVISOR_PROJEKT_TEMPLATE.md`

Skelett für `SUPERVISOR_{PROJEKT}.md`. Bibel-Format. Maximal 400 Zeilen.

---

## Schritt 05 — `PROJECT_BOOTSTRAP_README.md` anlegen

Auf Top-Level in `Claude/`. Diese Datei wird vom Architekten in
jeden neuen Projektordner kopiert, damit eine frische Coda-Session
weiß was zu tun ist.

Inhalt (Kurzfassung):

```markdown
# PROJECT BOOTSTRAP — Anleitung für Coda

Du bist Coda. Das hier ist ein neuer Projektordner. Im selben Ordner
liegt eine PROJEKT_ANFRAGE.md mit den Wünschen des Architekten.

## Was du tust:

1. Lies PROJEKT_ANFRAGE.md
2. Lies C:\Users\chris\Python\Claude\GLOBAL_LESSONS.md (Pflicht)
3. Lies C:\Users\chris\Python\Claude\SUPERVISOR_KODEX.md (Pflicht)
4. Ziehe Templates aus C:\Users\chris\Python\Claude\_templates\
5. Ersetze alle {PROJEKT}-Platzhalter
6. Baue die Skelettstruktur dieses Projekts auf
7. Frag den Architekten NUR die 3-5 Architektur-Entscheidungen die du nicht selbst treffen kannst
8. Dann: go

## Was du NIE tust:

Siehe SUPERVISOR_KODEX.md. Kurzform: kein Terminal-Befehl für Chris.
Worktree-Branches merged du selbst. mjolnir.md schreibst du am Session-Ende.
```

---

## Schritt 06 — Selbsttest (Phase A-D, PFLICHT)

### Phase A — Template-Anwendung

Erstelle in `/tmp/` (oder `%TEMP%`) ein Dummy-Verzeichnis `bootstrap_test/`.
Kopiere die neuen Templates rein, ersetze `{PROJEKT}` durch `TESTPROJEKT`.
Verifiziere per `Get-Content` dass keine `{PROJEKT}`-Platzhalter mehr drin sind.

### Phase B — Sub-Agent simuliert frische Session

Starte einen Sub-Agent (oder zweite Coda-Instanz, falls verfügbar) mit
dem Auftrag: „Du bist eine frische Coda-Session in `bootstrap_test/`.
Lies PROJECT_BOOTSTRAP_README.md und führe Schritte 1-7 aus."

Verifiziere dass der Sub-Agent:
- Beide globalen Files erkennt (GLOBAL_LESSONS, SUPERVISOR_KODEX)
- Die Templates findet und versteht
- Keine Terminal-Befehle an Chris vorschlägt

### Phase C — Konflikt provozieren

Erzeuge in `bootstrap_test/` eine `mjolnir.md` mit STATUS=IN_ARBEIT,
dann eine zweite `FEATURE_REQUEST_*.md` mit anderem Kurznamen.
Verifiziere dass der Sub-Agent das QUEUED-Pattern korrekt anwendet:
neue Datei zu `_QUEUED.md`, alte bleibt.

### Phase D — Aufräumen

Lösche `bootstrap_test/` und alle Test-Artefakte. Stelle sicher dass
in `Claude/` nichts vom Test übrig ist (keine `*_TEST.md`, kein `bootstrap_test/`).

Verifiziere per Listing.

---

## Schritt 07 — Commit + Push

Branch: direkt auf `main` (kein Worktree für Strukturarbeit nötig).

Commits idealerweise getrennt:
1. `feat(global): add GLOBAL_LESSONS.md with 6 Faulheits-Catches`
2. `feat(global): add SUPERVISOR_KODEX.md`
3. `feat(templates): add _templates/ with mjolnir, FEATURE_REQUEST, CLAUDE_PROJEKT, SUPERVISOR_PROJEKT`
4. `feat(bootstrap): add PROJECT_BOOTSTRAP_README.md`

Push auf `origin/main`. Verifiziere `$LASTEXITCODE = 0`.
Bei Fehler: in mjolnir.md unter BLOCKIERT dokumentieren, **auf Deutsch**.

---

## Schritt 08 — mjolnir.md schreiben

Überschreibe `Claude/mjolnir.md` mit:

```
**STATUS:** FERTIG
**AUFTRAG:** faulheits-catch-integration
**FORTSCHRITT:** 1 von 1 Session | alle 8 Schritte durch
**NÄCHSTE SESSION:** entfällt (FERTIG)

## Was Chris physisch tun muss

- Auf dem Handy nach Push prüfen ob Repo grün ist (1 Klick auf GitHub)
- Heute Abend: Demo mit Kumpel — PROJEKT_ANFRAGE.html ausfüllen lassen, in neuen Ordner kopieren mitsamt PROJECT_BOOTSTRAP_README.md, dann „go" sagen

## Auftragshistorie

GLOBAL_LESSONS.md, SUPERVISOR_KODEX.md, _templates/, PROJECT_BOOTSTRAP_README.md angelegt. Selbsttest A-D durchgelaufen. Push grün.
```

---

## Wichtige Hinweise

**Bibel-Format nutzen** für alle Maschinen-Files (GLOBAL_LESSONS, Lifecycle-Hinweise).
**Prosa nutzen** für alle Menschen-Files (BOOTSTRAP_README, Anlass-Blöcke).
**Niemals mischen** innerhalb einer Datei.

**Bei Konflikten oder Unklarheiten:** Nicht raten. In `DECISIONS_PENDING.md`
festhalten und in mjolnir.md unter BLOCKIERT verweisen.

**Try_Faulheits_catch.md** bleibt unverändert liegen als Konzept-Ursprung.
Die Verteilung geschieht über GLOBAL_LESSONS.md, SUPERVISOR_KODEX.md und
die Templates — nicht durch Verschieben der Ursprungsdatei.
