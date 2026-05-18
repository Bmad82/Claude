# AUFTRAG: Repo-Restrukturierung + REPO_INDEX-Einführung

## Kontext
Das `Bmad82/Claude`-Repo wird aufgeräumt und bekommt ein neues Feature: `REPO_INDEX.md` — eine automatisch gepflegte Verzeichnisdatei, die dem Supervisor (Chat-Instanz) ermöglicht, jede Datei im Repo via Raw-Link zu fetchen, ohne dass Chris Links manuell weiterleiten muss. Dies ersetzt die geplante Gists-Migration.

**WICHTIG:** Dieses Repo ist PUBLIC. Niemals Passwörter, API-Keys, Tokens, persönliche Daten, IP-Adressen, interne URLs, Hostnamen oder projektspezifische Secrets reinschreiben.

## Voraussetzung: Push-Status prüfen
Bevor du irgendetwas anderes tust: Prüfe ob `SUPERVISOR_BRIEFING.md` und `REPO_INVENTORY.md` im Repo existieren und gepusht sind. Falls nicht → erst pushen. Dann weiter.

---

## Phase 1: Aufräumen (Cleanup)

### 1a) Worktree löschen
Der Worktree unter `.claude/worktrees/focused-payne-b38e6a/` ist veraltet und abgehängt. 
```bash
# Zuerst prüfen ob git worktree den kennt:
git worktree list
# Falls gelistet: git worktree remove
# Falls nicht gelistet: rm -rf .claude/worktrees/focused-payne-b38e6a/
# Falls .claude/worktrees/ danach leer: rm -rf .claude/worktrees/
```

### 1b) _erledigt/-Ordner anlegen
Alle Dateien mit `_ERLEDIGT` im Namen in einen neuen Ordner `_erledigt/` verschieben.
```bash
mkdir -p _erledigt
mv *_ERLEDIGT* _erledigt/ 2>/dev/null
```
In `.gitignore` NICHT aufnehmen — die sollen als Historie sichtbar bleiben.

### 1c) DESIGN.md — Platzhalter füllen oder dokumentieren
Prüfe alle `[WERT]`-Platzhalter in `DESIGN.md`. Für jeden Platzhalter:
- Wenn der Wert aus dem Repo-Kontext ableitbar ist → einsetzen
- Wenn nicht → Platzhalter mit `[TODO: Beschreibung was hier hin muss]` ersetzen, damit klar ist was fehlt

### 1d) bugs/ — Scope markieren
Falls `bugs/` existiert und nur Zerberus-Content enthält: Entweder in `bugs/zerberus/` verschieben (Sub-Ordner), oder eine `bugs/README.md` anlegen die erklärt: "Hier liegen projektspezifische Bug-Tracker. Pro Projekt ein Unterordner."

---

## Phase 2: Ordnerstruktur etablieren

### Zielstruktur (nach Cleanup):
```
Bmad82/Claude/
├── README.md                    # Einstiegsseite (wird in Phase 3 neu geschrieben)
├── REPO_INDEX.md                # NEU — automatisch gepflegt (Phase 3)
├── DESIGN.md                    # Design-Philosophie (Kintsugi, Rollen, Prinzipien)
├── lessons/
│   ├── INDEX.md                 # NEU — erklärt die Lessons-Hierarchie
│   ├── LESSONS_KONSOLIDIERT.md  # Globale, projektübergreifende Lessons
│   ├── faiss-lessons.md         # (und weitere thematische Lessons)
│   └── ...
├── templates/
│   ├── CLAUDE_TEMPLATE.md       # Bootstrap-Vorlage für CLAUDE_PROJEKT.md
│   ├── SUPERVISOR_TEMPLATE.md   # Bootstrap-Vorlage für SUPERVISOR_PROJEKT.md
│   └── ...
├── workflow/                    # NEU — Marathon-Workflow-Dokumentation
│   ├── MARATHON_WORKFLOW.md     # Workflow-Beschreibung
│   ├── ROADMAP.md               # Phasen-Roadmap
│   ├── FAULHEITS_CATCHES.md     # Try/Catch-Dokument
│   └── ...
├── bugs/
│   └── zerberus/                # Projektspezifische Bug-Tracker
├── _erledigt/                   # Archiv erledigter Aufträge
└── .gitignore
```

### 2a) Ordner anlegen
```bash
mkdir -p workflow bugs/zerberus
```

### 2b) Dateien in Ordner verschieben
Prüfe welche Dateien im Root liegen, die thematisch in einen Ordner gehören. Verschiebe sie.
Konkret: Alles was `MARATHON`, `WORKFLOW`, `ROADMAP`, `FAULHEIT` im Namen hat → `workflow/`.

### 2c) lessons/INDEX.md erstellen
Inhalt: Kurze Erklärung der Lessons-Hierarchie:
- `LESSONS_KONSOLIDIERT.md` = projektübergreifende, universelle Erkenntnisse
- Thematische Dateien (faiss-lessons, etc.) = Spezialthemen die mehrere Projekte betreffen
- Projektspezifische Lessons (z.B. zerberus_lessons.md) gehören ins jeweilige Projekt-Repo, NICHT hierher
- Falls `zerberus_lessons.md` hier liegt: Datei löschen oder durch einen Verweis ersetzen ("Master liegt in Zerberus-Repo")

---

## Phase 3: REPO_INDEX.md — Implementierung

### 3a) Format definieren und erstellen

`REPO_INDEX.md` im Repo-Root mit folgendem Format:

```markdown
# REPO_INDEX — Bmad82/Claude
<!-- AUTO-GENERATED — Wird von Claude Code bei Verzeichnisänderungen aktualisiert -->
<!-- Letzte Aktualisierung: {ISO-Timestamp} -->
<!-- Generator: Claude Code Session -->

## Verzeichnisbaum

{Ausgabe von: find . -not -path './.git/*' -not -name 'REPO_INDEX.md' | sort}

## Dateien mit Raw-Links

| Pfad | Raw-Link | Typ | Beschreibung |
|------|----------|-----|-------------|
| README.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/README.md) | md | Repo-Einstiegsseite |
| lessons/INDEX.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/INDEX.md) | md | Lessons-Hierarchie |
| ... | ... | ... | ... |

## Statistik

- Dateien gesamt: {N}
- Letzte strukturelle Änderung: {Datum}
- Letzter Generator-Lauf: {Datum}
```

### 3b) REPO_INDEX initial befüllen
Generiere die Datei JETZT mit dem aktuellen Stand (nach allen Verschiebungen aus Phase 1+2).

---

## Phase 4: Templates aktualisieren

### 4a) CLAUDE_TEMPLATE.md — Ergänzungen
Füge in die CLAUDE_TEMPLATE.md (falls vorhanden) folgende Regeln ein:

```markdown
## REPO_INDEX-Pflicht
- `REPO_INDEX.md` im Repo-Root ist Pflicht für jedes Projekt.
- Wird bei Verzeichnisänderungen (Dateien erstellt/gelöscht/verschoben/umbenannt) am Session-Ende aktualisiert.
- Format: Verzeichnisbaum + Tabelle mit Raw-Links.
- Aktualisierung passiert VOR dem finalen Push.
- Wenn keine Verzeichnisänderungen stattfanden: REPO_INDEX nicht anfassen (kein Diff-Noise).
```

### 4b) SUPERVISOR_TEMPLATE.md — Ergänzungen
Falls vorhanden, ergänze:

```markdown
## Repo-Navigation via REPO_INDEX
- Der Supervisor kann `REPO_INDEX.md` via Raw-Link fetchen:
  `https://raw.githubusercontent.com/{user}/{repo}/main/REPO_INDEX.md`
- Daraus leitet der Supervisor Raw-Links für beliebige Dateien ab.
- Bei Session-Start: REPO_INDEX fetchen, um aktuellen Repo-Stand zu kennen.
- Kein manuelles Link-Relaying durch den Architekten nötig.
```

### 4c) Session-Ende-Checkliste aktualisieren
Falls die Checkliste in einem der Templates existiert: Neuen Schritt einfügen:
"Verzeichnisänderungen in dieser Session? → REPO_INDEX.md aktualisieren"

---

## Phase 5: README.md neu schreiben

Die aktuelle README ist minimal (5 Zeilen). Neue Version:

- Titel: "Claude — Marathon Workflow Knowledge Base"
- Kurzbeschreibung (3-4 Sätze): Was ist der Marathon Workflow? Supervisor-Executor-Architektur, Phone-first, Voice-driven.
- Ordnerstruktur mit Einzeilern pro Ordner
- Hinweis auf REPO_INDEX.md als Navigations-Einstieg
- Public-Repo-Warnung (die bestehende) beibehalten
- Sprache: **Deutsch** (Repo-Sprache ist DE, Zielgruppe ist zunächst Chris selbst)
- Kein Hype, kein Marketing — sachlich, knapp, nützlich

---

## Was du NICHT tun sollst

- Keine Dateien löschen die du nicht sicher als Müll identifiziert hast (im Zweifel: stehen lassen und in `SUPERVISOR_BRIEFING.md` markieren)
- Keine Inhalte übersetzen (DE→EN kommt später als separater Schritt)
- Keine Änderungen am Zerberus-Repo oder anderen Projekt-Repos (das kommt in einem Folge-Auftrag)
- Keine Showcases (HTML) erstellen oder ins Repo legen

## Abschluss

1. Alle Änderungen committen: `git add -A && git commit -m "refactor: Repo-Restrukturierung + REPO_INDEX-Einführung"`
2. Push + `$LASTEXITCODE`-Verify
3. REPO_INDEX.md muss den finalen Stand abbilden (nach allen Verschiebungen)
4. mjolnir.md aktualisieren

## Akzeptanzkriterien

- [ ] Worktree ist bereinigt
- [ ] `_erledigt/` existiert mit allen ERLEDIGT-Dateien
- [ ] `workflow/` existiert mit Workflow-Dokumenten
- [ ] `bugs/` hat klare Scope-Markierung
- [ ] `DESIGN.md` hat keine anonymen `[WERT]`-Platzhalter mehr
- [ ] `lessons/INDEX.md` existiert und erklärt Hierarchie
- [ ] `REPO_INDEX.md` existiert im Root, ist initial befüllt, hat Raw-Links
- [ ] Templates sind um REPO_INDEX-Regeln ergänzt
- [ ] README.md ist neu geschrieben
- [ ] Push verifiziert via `$LASTEXITCODE`
- [ ] Kein Secret/Token/Key im Repo
