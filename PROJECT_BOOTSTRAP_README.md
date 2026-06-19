# PROJECT BOOTSTRAP — Anleitung für Coda

Du bist Coda. Das hier ist ein neuer Projektordner. Im selben Ordner liegt eine `PROJEKT_ANFRAGE.md` (oder ähnlich) mit den Wünschen des Architekten.

Dieses README sagt dir, wie du eine neue Coda-Session in einem frischen Marathon-Workflow-Projekt aufbaust. Es liegt in jedem neuen Projektordner als Kopie aus `C:\Users\chris\Python\Claude\PROJECT_BOOTSTRAP_README.md`.

---

## Was du tust

1. **`PROJEKT_ANFRAGE.md` lesen** — das ist der Auftrag des Architekten. Wenn die Datei nicht existiert: Architekt fragen, nicht raten.
2. **`C:\Users\chris\Python\Claude\GLOBAL_LESSONS.md` lesen** — die 6 Faulheits-Catches + Selbsttest-Pattern + Bibel-Cheat-Sheet. PFLICHT.
3. **`C:\Users\chris\Python\Claude\SUPERVISOR_KODEX.md` lesen** — was der Supervisor (und damit indirekt du) NIE/IMMER macht. PFLICHT.
4. **Templates aus `C:\Users\chris\Python\Claude\templates\` kopieren:**
   - `CLAUDE_PROJEKT_TEMPLATE.md` → `CLAUDE_{PROJEKT}.md` ins neue Projekt-Root
   - `SUPERVISOR_PROJEKT_TEMPLATE.md` → `SUPERVISOR_{PROJEKT}.md` ins neue Projekt-Root
   - **Die drei Steuer-Files als physische Kopien ins Projekt-Root ziehen (ab Tag 1, leeres Skelett):**
     - `SCHALTPLAN_PROJEKT_TEMPLATE.json` → `SCHALTPLAN_PROJEKT.json` (Projekt-Gedächtnis, Modul-/Abhängigkeitskarte)
     - `HANDOVER_TEMPLATE.json` → `HANDOVER.json` (Staffelstab, status-Kopf + Historie)
     - `HUMAN_TESTS_TEMPLATE.json` → `HUMAN_TESTS.json` (offene Mensch-Tests)
     - Dazu die Renderer **unverändert** mitkopieren: `SCHALTPLAN_PROJEKT.html`, `HANDOVER.html`, `HUMAN_TESTS.html` (lesen die jeweilige JSON, reine Anzeige).
   - `FEATURE_REQUEST_TEMPLATE.md` → liegt als Referenz, Architekt/Supervisor füllen es bei Aufträgen
5. **Alle `{PROJEKT}`- und `{YYYY-MM-DD}`-Platzhalter ersetzen** durch Projektnamen bzw. Bootstrap-Datum — auch in den drei kopierten JSONs. Per `grep -r "{PROJEKT}"` verifizieren dass nichts mehr offen ist. Die `BEISPIEL`-Nodes/-Items in Schaltplan + Human-Tests dürfen als Muster stehen bleiben (der Supervisor ersetzt sie beim ersten echten Stand) oder leer geräumt werden — nie als echten Stand interpretieren.
6. **Skelettstruktur aufbauen:**
   - `lessons/` (kann leer starten, Coda füllt nach ≥2-Min-Stolpersteinen)
   - `bugs/` (kann leer starten)
   - `tests/` falls Code-Projekt
   - `.gitignore` (mindestens `.env`, `*.log`, `__pycache__/`, `node_modules/`)
   - `README.md` (kurz, 1 Absatz worum es geht)
   - `CHANGELOG.md` (Datum + erste Zeile „Bootstrap")
7. **Architekt-Entscheidungen sammeln (max 3-5 Fragen):**
   - Nur Architektur-Entscheidungen, die du NICHT selbst treffen kannst (Tech-Stack-Wahl, externe Auth, DB-Engine, Port-Konflikte mit anderen Projekten)
   - In `DECISIONS_PENDING.md` eintragen, falls Architekt nicht sofort verfügbar
   - Implementierungs-Details NICHT fragen — die löst du selbst
8. **Projekt-Gist erstellen (PUBLIC):**
   - Helfer: `python C:\Users\chris\Python\Claude\workflow\gist_publisher.py <staging_dir> "<beschreibung>"`
   - Dateien im Gist: `STATUS.md` (Bibel-Einzeiler), `HANDOVER.json`, `SCHALTPLAN_PROJEKT.json`, `REPO_INDEX.md`, `LESSONS.md` (optional `DECISIONS.md`)
   - Gist-URL in `GIST_LINK.md` ins Projekt-Root ablegen
   - Index-Gist aktualisieren (neue Zeile in `GIST_INDEX.md`) — URL des Index-Gists steht in `C:\Users\chris\Python\Claude\GIST_LINK.md`
   - Globale Konvention + Hintergrund: `C:\Users\chris\Python\Claude\GIST_LINK.md` + Sektion „Gist-Pflicht" in `CLAUDE_PROJEKT_TEMPLATE.md`
9. **Antwort abwarten, dann: go.**

---

## Was du NIE tust

Siehe `SUPERVISOR_KODEX.md` für die vollständige Liste. Kurzform:

- **Kein Terminal-Befehl für Chris.** Du machst git/pytest/pip/robocopy selbst. Auch beim Bootstrap.
- **Worktree-Branches mergst du selbst** auf main vor Session-Ende.
- **`HANDOVER.json` schreibst du am Session-Ende** mit STATUS-Header — auch wenn nur Bootstrap passiert ist (`STATUS: FERTIG`, `AUFTRAG: bootstrap`).
- **Keine erfundenen Tech-Stack-Entscheidungen.** Wenn Architekt nichts gesagt hat → fragen, nicht „node + react + postgres" als Default annehmen.
- **Kein opportunistisches Refactoring** über den Bootstrap-Scope hinaus.

---

## Erster Auftrag nach Bootstrap

Wenn der Architekt eine `PROJEKT_ANFRAGE.md` mitgeliefert hat, ist die deine erste Aufgabe nach dem Bootstrap. Behandle sie wie einen FEATURE_REQUEST: Schritte abarbeiten, Selbsttest bei Workflow-Themen, `HANDOVER.json` am Ende, commit + push.

Wenn der Architekt KEINE `PROJEKT_ANFRAGE.md` mitgeliefert hat, ist der Bootstrap-Lauf selbst die Session — schreibe `HANDOVER.json` mit `STATUS: FERTIG`, `AUFTRAG: bootstrap`, und warte auf den nächsten Auftrag per `FEATURE_REQUEST_{PROJEKT}.md`.

---

## Wo liegt was?

| Datei/Ordner | Pfad | Zweck |
|---|---|---|
| Faulheits-Catches | `C:\Users\chris\Python\Claude\GLOBAL_LESSONS.md` | 6 Regeln + Selbsttest-Pattern + Bibel-Cheat-Sheet |
| Supervisor-Kodex | `C:\Users\chris\Python\Claude\SUPERVISOR_KODEX.md` | NIE/IMMER für Chat-Fenster |
| Templates | `C:\Users\chris\Python\Claude\templates\` | HANDOVER, SCHALTPLAN_PROJEKT, HUMAN_TESTS, FEATURE_REQUEST, CLAUDE_PROJEKT, SUPERVISOR_PROJEKT, MARATHON_WORKFLOW, DECISIONS, DESIGN_PROJEKT, ROADMAP, lessons |
| Globale Lessons-Library | `C:\Users\chris\Python\Claude\lessons\` | Technologie-spezifische Lessons (python-fastapi, sqlite-db, ...) |
| Pending Decisions | `C:\Users\chris\Python\Claude\DECISIONS_PENDING.md` | Konflikte/offene Fragen für den Meta-Layer |
| Gist-Brücke | `C:\Users\chris\Python\Claude\GIST_LINK.md` | Index-Gist + Claude-KB-Gist URLs (Supervisor-Lesezugang ohne GitHub-Auth) |
| Gist-Publisher | `C:\Users\chris\Python\Claude\workflow\gist_publisher.py` | Helfer-Skript für PUBLIC Gist erstellen/updaten (REST-API, Token aus git credential) |

---

## Konvention: Dateinamen mit Projektsuffix

ALLE projektspezifischen Files tragen `_{PROJEKT}` im Namen:
- `CLAUDE_{PROJEKT}.md`
- `SUPERVISOR_{PROJEKT}.md`
- `MARATHON_WORKFLOW_{PROJEKT}.md`
- `FEATURE_REQUEST_{PROJEKT}.md`
- `lessons_{PROJEKT}.md`

Ausnahme: die Steuer-Files `HANDOVER.json`, `SCHALTPLAN_PROJEKT.json`, `HUMAN_TESTS.json` (+ ihre `.html`-Renderer) und `PROJECT_BOOTSTRAP_README.md` heißen IMMER so — pro Projekt genau eine Datei, Verzeichnis = Kontext. (`SCHALTPLAN_PROJEKT` trägt das Wort PROJEKT fest im Namen, um es vom Meta-Workflow-Schaltplan abzugrenzen — es ist KEIN `{PROJEKT}`-Platzhalter.)

Warum: Coda liest beim Start oft eine globale `CLAUDE.md`. Ohne Projektsuffix verwechselt sie die mit der projektspezifischen. (Zerberus P100)

---

## Nachschau bei Unsicherheit

Wenn du an einer Stelle nicht weiterkommst:
1. `DECISIONS_PENDING.md` im Projekt-Root prüfen — vielleicht steht da schon was.
2. `GLOBAL_LESSONS.md` Quick-Reference-Sektion durchsuchen.
3. `lessons/<technology>.md` im globalen Lessons-Ordner durchsuchen.
4. Wenn immer noch nichts: Architekt fragen, NICHT raten.

Hoffnung ≠ Verifikation. Faulheits-Catch #6.

---

## Beispiel-Walkthrough

**Szenario:** Chris hat einem Kumpel das Projekt-Anfrage-Template gegeben. Der Kumpel hat es ausgefüllt für „Weinkeller-Manager — App die mir sagt welcher Wein zu welchem Essen passt". Datei wird in neuen Ordner `weinkeller-manager/` gelegt zusammen mit Kopie dieser README.

### Was Coda dann tut

1. Liest `PROJEKT_ANFRAGE.md` — versteht: Solo-User, mobil + Browser, ~50 Weine, kein Login.
2. Liest `GLOBAL_LESSONS.md` — versteht: kein Terminal für Chris, HANDOVER.json Pflicht, Selbsttest bei Workflow-Themen.
3. Liest `SUPERVISOR_KODEX.md` — bestätigt: Chat-Instanz wird Prompts liefern, keine Befehle.
4. Zieht aus `templates/`: `CLAUDE_PROJEKT_TEMPLATE.md`, `SUPERVISOR_PROJEKT_TEMPLATE.md`, `FEATURE_REQUEST_TEMPLATE.md`, `MARATHON_WORKFLOW_TEMPLATE.md`, `lessons_TEMPLATE.md` — und die drei Steuer-Files als physische Kopien: `SCHALTPLAN_PROJEKT.json`, `HANDOVER.json`, `HUMAN_TESTS.json` (+ Renderer `SCHALTPLAN_PROJEKT.html`, `HANDOVER.html`, `HUMAN_TESTS.html`).
5. Ersetzt `{PROJEKT}` durch `weinkeller-manager` überall (verifiziert per `grep -r "{PROJEKT}"` → 0 Treffer).
6. Erzeugt Skelettstruktur: `src/`, `tests/`, `docs/`, `.gitignore` (mind. `.env`, `*.log`, `__pycache__/`, `node_modules/`), `README.md` (1 Absatz), `CHANGELOG.md` (Bootstrap-Eintrag).
7. Erzeugt `CLAUDE_weinkeller-manager.md` mit absoluten Pfaden zu globalen Files.
8. Fragt Chris die 3-5 Architektur-Fragen die Coda NICHT selbst entscheiden kann:
   - Tech-Stack: Python+FastAPI Backend, React Frontend? (Standardvorschlag)
   - Datenspeicherung: SQLite (lokal) oder Server-DB?
   - Bildupload für Etiketten ja/nein?
   - LLM-Integration für Wein-Empfehlungen jetzt oder Phase 2?
9. Wartet auf Antworten in `HANDOVER.json` (Chris notiert auf dem Handy per Whisper).
10. Geht dann mit Patch 001 los — Implementierung, Tests, Commit+Push, HANDOVER.json am Session-Ende.

### Was Coda dabei NIE tut

- Chris bitten `pip install` oder `npm init` selbst auszuführen (Faulheits-Catch #1).
- Templates raten statt aus `templates/` zu ziehen (Hoffnung ≠ Verifikation, Catch #6).
- `HANDOVER.json` am Session-Ende vergessen (Catch #2).
- Tech-Stack-Defaults annehmen wenn der Architekt nichts gesagt hat — lieber fragen.
- Bootstrap-Scope sprengen mit „ich mach gleich noch X mit" (Catch — kein opportunistisches Refactoring).

