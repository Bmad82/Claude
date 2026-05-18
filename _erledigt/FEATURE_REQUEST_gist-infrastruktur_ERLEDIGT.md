# AUFTRAG: Gist-Infrastruktur aufsetzen + Templates aktualisieren

## Kontext
Die Chat-Instanz (Supervisor) kann keine Raw-Links von GitHub fetchen, aber Gists lesen. Gists werden ab sofort die Brücke zwischen Coding-Instanz (Coda) und Supervisor. Jedes Projekt bekommt einen eigenen Gist mit Briefing-Dateien. Ein zentraler Index-Gist verweist auf alle Projekt-Gists. Der Cron-Job für Lessons-Konsolidierung wird ebenfalls über Gists arbeiten.

**WICHTIG:** Alle Gists müssen PUBLIC sein, damit der Supervisor (und andere LLM-Instanzen im Cron-Job) sie ohne Auth lesen können.

---

## Phase 1: Index-Gist erstellen

Erstelle einen PUBLIC Gist mit folgender Datei:

**Dateiname:** `GIST_INDEX.md`
**Beschreibung des Gists:** `Marathon Workflow — Projekt-Index für Supervisor-Instanzen`

**Inhalt:**
```markdown
# GIST_INDEX — Marathon Workflow
<!-- Zentrale Navigationsdatei für Supervisor-Instanzen und Cron-Jobs -->
<!-- Aktualisiert von Coda bei neuem Projekt-Setup -->

## Projekt-Gists

| Projekt | Gist-URL | Status | Letztes Update |
|---------|----------|--------|----------------|
| Claude-KB | [wird in Phase 2 eingetragen] | AKTIV | [ISO-Datum] |

## Konvention
- Ein Gist pro Projekt (Briefing-Dateien, nicht Quellcode)
- Ein Claude-KB-Gist für globale Lessons, Templates-Index, Workflow-Summary
- Coda aktualisiert Projekt-Gist am Session-Ende
- Index-Gist wird nur aktualisiert wenn ein neues Projekt hinzukommt
- Alle Gists PUBLIC (Lesezugriff für beliebige LLM-Instanzen)
```

**Nach Erstellung:** Gist-URL notieren. Die wird im Claude-Repo unter `GIST_LINK.md` abgelegt (siehe Phase 3).

---

## Phase 2: Claude-KB-Gist erstellen

Erstelle einen PUBLIC Gist mit folgenden Dateien:

**Beschreibung des Gists:** `Claude-KB — Globale Lessons, Templates, Workflow`

### Datei 1: `GLOBAL_LESSONS.md`
Inhalt: Aktuelle konsolidierte Lessons aus dem Claude-Repo (`lessons/LESSONS_KONSOLIDIERT.md`). Volltext kopieren. Header ergänzen:
```markdown
# GLOBAL_LESSONS — Projektübergreifende Erkenntnisse
<!-- Quelle: Bmad82/Claude/lessons/LESSONS_KONSOLIDIERT.md -->
<!-- Aktualisiert durch Cron-Job bei Lessons-Konsolidierung -->
<!-- Format: Bibel (Token-effizient, für LLM-Konsum) -->
```

### Datei 2: `TEMPLATES_INDEX.md`
Inhalt: Liste aller Templates im Claude-Repo mit Kurzbeschreibung und Version.
```markdown
# TEMPLATES_INDEX
<!-- Aktualisiert bei Template-Änderungen -->

| Template | Pfad im Repo | Zweck | Version |
|----------|-------------|-------|---------|
| [für jedes Template im templates/-Ordner eine Zeile] |
```

### Datei 3: `WORKFLOW_SUMMARY.md`
Inhalt: Kompakte Zusammenfassung des Marathon-Workflows. Bibel-Format. Max 100 Zeilen. Enthält:
- Die drei Rollen (Architekt, Supervisor, Coda)
- Session-Zyklus (Kurzform)
- Datei-Konventionen (Bibel vs Prosa, Naming mit Projektsuffix)
- Faulheits-Catches (Einzeiler pro Catch)
- Gist-Konvention (dieser neue Standard)

### Datei 4: `BOOTSTRAP_CHECKLIST.md`
Inhalt: Was Coda beim Bootstrap eines neuen Projekts tun muss. Checkliste:
```markdown
# BOOTSTRAP_CHECKLIST — Neues Projekt aufsetzen
<!-- Für Coda: Diese Checkliste bei jedem neuen Projekt abarbeiten -->

## Voraussetzungen
- [ ] PROJEKT_ANFRAGE_{name}.md liegt im leeren Projektordner
- [ ] Projektordner hat ein initialisiertes Git-Repo mit Remote

## Bootstrap-Schritte
- [ ] PROJEKT_ANFRAGE lesen und verstehen
- [ ] Templates aus Claude-Repo holen (GIST_INDEX → Claude-KB → TEMPLATES_INDEX für Pfade)
- [ ] GLOBAL_LESSONS aus Claude-KB-Gist lesen, relevante Einträge in projekt-lokale lessons.md übernehmen
- [ ] Projektstruktur anlegen (Ordner, Bibel-Dateien, DESIGN.md, ROADMAP.md, etc.)
- [ ] REPO_INDEX.md im Root generieren
- [ ] Projekt-Gist erstellen (PUBLIC) mit: HANDOVER.md, MJOLNIR.md, REPO_INDEX.md, STATUS.md, LESSONS.md
- [ ] Gist-URL in GIST_LINK.md im Repo-Root ablegen
- [ ] Index-Gist aktualisieren (neue Zeile in GIST_INDEX.md)
- [ ] Initial-Commit + Push
- [ ] mjolnir.md schreiben mit STATUS=FERTIG und Gist-URLs

## Projekt-Gist Dateiformat

### STATUS.md (Bibel-Format)
Projekt|Phase|Patch|Stack|Nächster Schritt
Einzeiler. Supervisor liest das zuerst.

### HANDOVER.md
Kopie der lokalen HANDOVER.md. Wird bei jedem Session-Ende überschrieben.

### MJOLNIR.md  
Kopie der lokalen mjolnir.md. Wird bei jedem Session-Ende überschrieben.

### REPO_INDEX.md
Kopie der lokalen REPO_INDEX.md. Wird bei Verzeichnisänderungen aktualisiert.

### LESSONS.md
Projekt-Lessons. Wird vom Cron-Job gelesen und in GLOBAL_LESSONS konsolidiert.

### DECISIONS.md (optional)
Aktive ADRs. Nur wenn Architekturentscheidungen offen sind.
```

**Nach Erstellung:** Gist-URL in den Index-Gist (Phase 1) eintragen.

---

## Phase 3: Claude-Repo aktualisieren

### 3a) `GIST_LINK.md` im Repo-Root erstellen
```markdown
# Gist-Brücke
Index-Gist: [URL des Index-Gists aus Phase 1]
Projekt-Gist (Claude-KB): [URL des Claude-KB-Gists aus Phase 2]
```

### 3b) REPO_INDEX.md aktualisieren (neue Datei aufnehmen)

### 3c) Templates aktualisieren

**In `CLAUDE_PROJEKT_TEMPLATE.md` ergänzen:**
```markdown
## Gist-Pflicht
- Jedes Projekt hat einen PUBLIC Gist mit Briefing-Dateien (HANDOVER, MJOLNIR, REPO_INDEX, STATUS, LESSONS)
- Gist-URL steht in `GIST_LINK.md` im Repo-Root
- Gist wird am Session-Ende aktualisiert (zusammen mit lokalen Dateien)
- Index-Gist wird bei neuem Projekt aktualisiert
- Session-Ende-Checkliste: "Gist-Dateien aktualisiert?"
```

**In `SUPERVISOR_PROJEKT_TEMPLATE.md` ergänzen:**
```markdown
## Gist-Navigation
- Index-Gist: [URL wird beim Bootstrap eingetragen]
- Projekt-Gist: [URL wird beim Bootstrap eingetragen]
- Der Supervisor fetcht bei Session-Start den Projekt-Gist für aktuellen Stand
- Kein manuelles Link-Relaying durch den Architekten nötig
- Bei Unklarheiten: Index-Gist fetchen → Projekt-Gist fetchen → Dateien lesen
```

**In der Session-Ende-Checkliste (falls in Templates vorhanden) ergänzen:**
```
- [ ] Gist-Dateien aktualisiert (HANDOVER, MJOLNIR, STATUS, ggf. REPO_INDEX, LESSONS)
```

---

## Phase 4: Zerberus-Gist erstellen (Bestandsprojekt nachrüsten)

Da Zerberus das reifste Projekt ist, soll es als erstes einen Projekt-Gist bekommen.

- Erstelle einen PUBLIC Gist mit Beschreibung `Zerberus Pro 4.0 — Supervisor-Briefing`
- Dateien: STATUS.md, HANDOVER.md (aktuelle Version aus Repo), MJOLNIR.md (letzte/aktuelle), REPO_INDEX.md (aus Repo), LESSONS.md (projekt-lokale Lessons)
- Gist-URL in Zerberus-Repo unter `GIST_LINK.md` ablegen
- Index-Gist aktualisieren (Zerberus-Zeile hinzufügen)
- REPO_INDEX im Zerberus-Repo aktualisieren

**Falls Zerberus noch keine REPO_INDEX.md hat:** Generieren (gleiche Konvention wie im Claude-Repo).

---

## Abschluss

1. Alle Änderungen im Claude-Repo committen + pushen
2. Alle Änderungen im Zerberus-Repo committen + pushen (falls Zerberus-Gist erstellt)
3. Alle Gist-URLs in mjolnir.md dokumentieren
4. Push-Verify via `$LASTEXITCODE`

## Akzeptanzkriterien

- [ ] Index-Gist existiert, ist PUBLIC, enthält GIST_INDEX.md
- [ ] Claude-KB-Gist existiert, ist PUBLIC, enthält 4 Dateien (GLOBAL_LESSONS, TEMPLATES_INDEX, WORKFLOW_SUMMARY, BOOTSTRAP_CHECKLIST)
- [ ] Claude-Repo hat GIST_LINK.md mit beiden URLs
- [ ] Templates enthalten Gist-Konvention
- [ ] Session-Ende-Checkliste enthält Gist-Update-Schritt
- [ ] Zerberus hat Projekt-Gist + GIST_LINK.md (falls umgesetzt)
- [ ] Index-Gist verweist auf alle erstellten Gists
- [ ] Alle Pushes verifiziert
- [ ] Kein Secret/Token in Gists oder Repo
- [ ] Alle Gists sind PUBLIC
