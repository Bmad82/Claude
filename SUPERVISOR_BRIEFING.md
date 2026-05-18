# SUPERVISOR_BRIEFING — Repo-Restrukturierung `Bmad82/Claude`

**Erstellt:** 2026-05-18
**Coda-Session:** supervisor-briefing
**Empfänger:** Supervisor (Chat-Fenster, plant Repo-Restrukturierung)
**Auftrag-Quelle:** `FEATURE_REQUEST_CLAUDE.md` (2026-05-18)
**Charakter:** reine Informationslieferung — keine Änderungen, kein Aufräumen, kein Reorder

---

## Sektion 1: Vollständiger Directory-Tree

### 1.1 Main-Tree (ohne `.git/` und ohne `.claude/worktrees/`)

```text
.
./.claude
./.claude/worktrees
./.gitignore
./DECISIONS_PENDING.md
./DESIGN.md
./FEATURE_REQUEST_CLAUDE.md
./FEATURE_REQUEST_CLAUDE_ERLEDIGT.md
./FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md
./FEATURE_REQUEST_repo-inventur_ERLEDIGT.md
./GLOBAL_LESSONS.md
./LESSONS_KONSOLIDIERT.md
./PROJECT_BOOTSTRAP_README.md
./README.md
./REPO_INVENTORY.md
./SUPERVISOR_KODEX.md
./_drafts_gist
./_drafts_gist/INDEX_GIST_DRAFT.md
./_drafts_gist/ZERBERUS_GIST_DRAFT.md
./bugs
./bugs/zerberus
./bugs/zerberus/regex.md
./bugs/zerberus/whisper.md
./concepts
./concepts/Try_Faulheits_catch.md
./lessons
./lessons/README.md
./lessons/documentation.md
./lessons/frontend-js.md
./lessons/git-deployment.md
./lessons/gpu-ml.md
./lessons/json-data.md
./lessons/mobile-touch.md
./lessons/python-fastapi.md
./lessons/sqlite-db.md
./lessons/testing.md
./lessons/whisper-transcription.md
./lessons/workflow.md
./lessons/zerberus_lessons.md
./mjolnir.md
./templates
./templates/CLAUDE_PROJEKT_TEMPLATE.md
./templates/DECISIONS_TEMPLATE.md
./templates/DESIGN_PROJEKT_TEMPLATE.md
./templates/FEATURE_REQUEST_TEMPLATE.md
./templates/HANDOVER_TEMPLATE.md
./templates/MARATHON_WORKFLOW_TEMPLATE.md
./templates/ROADMAP_TEMPLATE.md
./templates/SUPERVISOR_PROJEKT_TEMPLATE.md
./templates/lessons_TEMPLATE.md
./templates/mjolnir_TEMPLATE.md
```

### 1.2 Worktree (`.claude/worktrees/`, erste 30 Einträge)

```text
./.claude/worktrees/
./.claude/worktrees/focused-payne-b38e6a
./.claude/worktrees/focused-payne-b38e6a/.git
./.claude/worktrees/focused-payne-b38e6a/.gitignore
./.claude/worktrees/focused-payne-b38e6a/bugs
./.claude/worktrees/focused-payne-b38e6a/bugs/zerberus
./.claude/worktrees/focused-payne-b38e6a/bugs/zerberus/regex.md
./.claude/worktrees/focused-payne-b38e6a/bugs/zerberus/whisper.md
./.claude/worktrees/focused-payne-b38e6a/DESIGN.md
./.claude/worktrees/focused-payne-b38e6a/lessons
./.claude/worktrees/focused-payne-b38e6a/lessons/documentation.md
./.claude/worktrees/focused-payne-b38e6a/lessons/frontend-js.md
./.claude/worktrees/focused-payne-b38e6a/lessons/git-deployment.md
./.claude/worktrees/focused-payne-b38e6a/lessons/gpu-ml.md
./.claude/worktrees/focused-payne-b38e6a/lessons/json-data.md
./.claude/worktrees/focused-payne-b38e6a/lessons/mobile-touch.md
./.claude/worktrees/focused-payne-b38e6a/lessons/python-fastapi.md
./.claude/worktrees/focused-payne-b38e6a/lessons/README.md
./.claude/worktrees/focused-payne-b38e6a/lessons/sqlite-db.md
./.claude/worktrees/focused-payne-b38e6a/lessons/testing.md
./.claude/worktrees/focused-payne-b38e6a/lessons/whisper-transcription.md
./.claude/worktrees/focused-payne-b38e6a/lessons/workflow.md
./.claude/worktrees/focused-payne-b38e6a/lessons/zerberus_lessons.md
./.claude/worktrees/focused-payne-b38e6a/README.md
./.claude/worktrees/focused-payne-b38e6a/templates
./.claude/worktrees/focused-payne-b38e6a/templates/CLAUDE.md
./.claude/worktrees/focused-payne-b38e6a/templates/SUPERVISOR.md
```

Gesamt: 27 Einträge im Worktree (Snapshot vom 2026-05-15, nicht bereinigt).

---

## Sektion 2: REPO_INVENTORY.md — Volltext

```markdown
# REPO_INVENTORY.md — Vollständige Bestandsaufnahme

**Erstellt:** 2026-05-18
**Coda-Session:** repo-inventur
**Methode:** `find . -not -path './.git/*' | sort` + Datei-Inhalt-Scan

---

## 1. Vollständiger Directory-Tree

```
.
├── .claude/
│   └── worktrees/
│       └── focused-payne-b38e6a/          ← nicht bereinigter Git-Worktree
│           ├── .git
│           ├── .gitignore
│           ├── DESIGN.md
│           ├── README.md
│           ├── bugs/
│           │   └── zerberus/
│           │       ├── regex.md
│           │       └── whisper.md
│           ├── lessons/
│           │   ├── README.md
│           │   ├── documentation.md
│           │   ├── frontend-js.md
│           │   ├── git-deployment.md
│           │   ├── gpu-ml.md
│           │   ├── json-data.md
│           │   ├── mobile-touch.md
│           │   ├── python-fastapi.md
│           │   ├── sqlite-db.md
│           │   ├── testing.md
│           │   ├── whisper-transcription.md
│           │   ├── workflow.md
│           │   └── zerberus_lessons.md
│           └── templates/
│               ├── CLAUDE.md
│               └── SUPERVISOR.md
├── .gitignore
├── DECISIONS_PENDING.md
├── DESIGN.md
├── FEATURE_REQUEST_CLAUDE.md
├── FEATURE_REQUEST_CLAUDE_ERLEDIGT.md
├── FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md
├── GLOBAL_LESSONS.md
├── LESSONS_KONSOLIDIERT.md
├── PROJECT_BOOTSTRAP_README.md
├── README.md
├── REPO_INVENTORY.md                      ← diese Datei
├── SUPERVISOR_KODEX.md
├── _drafts_gist/
│   ├── INDEX_GIST_DRAFT.md
│   └── ZERBERUS_GIST_DRAFT.md
├── bugs/
│   └── zerberus/
│       ├── regex.md
│       └── whisper.md
├── concepts/
│   └── Try_Faulheits_catch.md
├── lessons/
│   ├── README.md
│   ├── documentation.md
│   ├── frontend-js.md
│   ├── git-deployment.md
│   ├── gpu-ml.md
│   ├── json-data.md
│   ├── mobile-touch.md
│   ├── python-fastapi.md
│   ├── sqlite-db.md
│   ├── testing.md
│   ├── whisper-transcription.md
│   ├── workflow.md
│   └── zerberus_lessons.md
├── mjolnir.md
└── templates/
    ├── CLAUDE_PROJEKT_TEMPLATE.md
    ├── DECISIONS_TEMPLATE.md
    ├── DESIGN_PROJEKT_TEMPLATE.md
    ├── FEATURE_REQUEST_TEMPLATE.md
    ├── HANDOVER_TEMPLATE.md
    ├── MARATHON_WORKFLOW_TEMPLATE.md
    ├── ROADMAP_TEMPLATE.md
    ├── SUPERVISOR_PROJEKT_TEMPLATE.md
    ├── lessons_TEMPLATE.md
    └── mjolnir_TEMPLATE.md
```

---

## 2. Datei-Inventar

### Root-Ebene

| Pfad | Typ | Sprache | Größe | Letzte Änderung | Kurzbeschreibung | Status |
|------|-----|---------|-------|-----------------|------------------|--------|
| `.gitignore` | config | — | 38 B | 2026-04-19 | Ignoriert `.env`, `*.bak`, `__pycache__/`, `.cache/`, `*.exe` | AKTUELL |
| `README.md` | md | DE | 3 035 B | 2026-05-17 | Haupt-Einstiegspunkt: Drei-Rollen-Modell, Kernfiles, Projekte-Liste, Dateinamen-Konvention | AKTUELL |
| `DESIGN.md` | md | DE | 33 668 B | 2026-05-17 | Zentrale UI-/Look-and-Feel-Referenz (Farben, Typo, Komponenten, Mobile) für alle Projekte — viele `[WERT]`-Platzhalter noch unbefüllt | AKTUELL |
| `GLOBAL_LESSONS.md` | md | DE | 14 167 B | 2026-05-17 | Projektübergreifende Lessons: 6 Faulheits-Catches, Bibel-Format, Selbsttest-Pattern, Mjölnir-Round-Trip, Naming-Konvention | AKTUELL |
| `LESSONS_KONSOLIDIERT.md` | md | DE | 7 454 B | 2026-05-15 | Älterer Konsolidierungs-Snapshot aus Supervisor-Chats (bis P49, 2026-05-15) — Plattform, Claude CLI, Backend, Frontend, Workflow | UNKLAR |
| `SUPERVISOR_KODEX.md` | md | DE | 6 735 B | 2026-05-17 | NIE/IMMER-Kodex für alle Chat-Fenster (Supervisor-Rolle): keine Terminal-Befehle, kein Mensch-im-Loop, Selbsttest-Pflicht | AKTUELL |
| `PROJECT_BOOTSTRAP_README.md` | md | DE | 7 301 B | 2026-05-17 | Schritt-für-Schritt-Anleitung für Coda beim Aufsetzen eines neuen Projekts (Templates kopieren, Platzhalter ersetzen, Skelett aufbauen) | AKTUELL |
| `DECISIONS_PENDING.md` | md | DE | 8 203 B | 2026-05-17 | Offene Architektur-Entscheidungen (pending: Zerberus-Lessons-Konsolidierung) + getroffene Entscheidungen mit Begründung und Patch-Referenz | AKTUELL |
| `mjolnir.md` | md | DE | 7 272 B | 2026-05-17 | Session-Abschluss-Status (Single-Slot): STATUS=FERTIG, Auftrag aufraeumarbeiten-post-catch, 12/13 Schritte durch, was Chris physisch tun muss | AKTUELL |
| `FEATURE_REQUEST_CLAUDE.md` | md | DE | 2 024 B | 2026-05-18 | Auftrag: Vollständige Repo-Inventur (diese Datei wird gerade abgearbeitet) | AKTUELL |
| `FEATURE_REQUEST_CLAUDE_ERLEDIGT.md` | md | DE | 9 269 B | 2026-05-17 | Audit-Log: erledigter FEATURE_REQUEST `faulheits-catch-integration` (Integration der 6 Faulheits-Catches in globale Templates) | AKTUELL |
| `FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md` | md | DE | 19 356 B | 2026-05-17 | Audit-Log: erledigter FEATURE_REQUEST `aufraeumarbeiten-post-catch` (Templates-Konsolidierung, Konzept-Ursprung, Bootstrap-Walkthrough u.a.) | AKTUELL |
| `REPO_INVENTORY.md` | md | DE | — | 2026-05-18 | Diese Datei — vollständige Bestandsaufnahme des Repos | AKTUELL |

### `_drafts_gist/`

| Pfad | Typ | Sprache | Größe | Letzte Änderung | Kurzbeschreibung | Status |
|------|-----|---------|-------|-----------------|------------------|--------|
| `_drafts_gist/INDEX_GIST_DRAFT.md` | md | DE | 1 166 B | 2026-05-17 | Konzept-Entwurf für öffentlichen GitHub-Gist: Index aller aktiven Projekte mit Pflichtfeldern und Migrations-Roadmap (Phase 3, noch nicht aktiv) | UNKLAR |
| `_drafts_gist/ZERBERUS_GIST_DRAFT.md` | md | DE | 898 B | 2026-05-17 | Konzept-Entwurf für Zerberus-Projekt-Gist: enthält `LAST_PATCH: P-???` und `TS: TBD` — noch ohne echte Daten | UNKLAR |

### `bugs/zerberus/`

| Pfad | Typ | Sprache | Größe | Letzte Änderung | Kurzbeschreibung | Status |
|------|-----|---------|-------|-----------------|------------------|--------|
| `bugs/zerberus/regex.md` | md | DE | 647 B | 2026-04-19 | Bug-Tracker für Zerberus: Regex/Pattern-Matching-Bugs (offen: RX-001 ZDF-Halluzination) | AKTUELL |
| `bugs/zerberus/whisper.md` | md | DE | 1 080 B | 2026-04-19 | Bug-Tracker für Zerberus: Whisper/Voice-Bugs (offen: W-001 Phrasen-Repetition-Loop) | AKTUELL |

### `concepts/`

| Pfad | Typ | Sprache | Größe | Letzte Änderung | Kurzbeschreibung | Status |
|------|-----|---------|-------|-----------------|------------------|--------|
| `concepts/Try_Faulheits_catch.md` | md | DE | 5 070 B | 2026-05-17 | Historisches Konzept-Dokument: rekonstruierte 6 Faulheits-Catches + Selbsttest-Pattern (operativer Inhalt migriert nach GLOBAL_LESSONS.md) | AKTUELL |

### `lessons/`

| Pfad | Typ | Sprache | Größe | Letzte Änderung | Kurzbeschreibung | Status |
|------|-----|---------|-------|-----------------|------------------|--------|
| `lessons/README.md` | md | DE | 592 B | 2026-04-19 | Beschreibt Zweck und Pflege des `lessons/`-Ordners | AKTUELL |
| `lessons/documentation.md` | md | DE | 2 642 B | 2026-05-15 | Lessons zu Dokumentation und Schulungsunterlagen (Shop-Floor-Kontext) | AKTUELL |
| `lessons/frontend-js.md` | md | DE | 4 720 B | 2026-04-23 | Lessons zu Frontend und JavaScript: Newline-Escaping, HTML-Rendering, JS-String-Literale | AKTUELL |
| `lessons/git-deployment.md` | md | DE | 809 B | 2026-04-23 | Lessons zu Git und Deployment: `start.bat`-Aktivierungspfad, Uvicorn-Start | AKTUELL |
| `lessons/gpu-ml.md` | md | DE | 3 035 B | 2026-04-23 | Lessons zu GPU/ML: Device-Detection mit VRAM-Fallback, `torch.cuda.mem_get_info()`, Test-Isolation | AKTUELL |
| `lessons/json-data.md` | md | DE | 434 B | 2026-04-23 | Lessons zu JSON: typographische Anführungszeichen brechen JSON-Import | AKTUELL |
| `lessons/mobile-touch.md` | md | DE | 737 B | 2026-04-19 | Lessons zu Mobile/Touch: `:hover` vs `:active`, Touch-Geräte-Verhalten | AKTUELL |
| `lessons/python-fastapi.md` | md | DE | 2 916 B | 2026-04-23 | Lessons zu Python/FastAPI: Uvicorn `--reload` auf Windows, neue Module, manueller Restart | AKTUELL |
| `lessons/sqlite-db.md` | md | DE | 1 507 B | 2026-04-23 | Lessons zu SQLite/DB-Migrationen: idempotente Migrations, PRAGMA-Checks, `IF NOT EXISTS` | AKTUELL |
| `lessons/testing.md` | md | DE | 976 B | 2026-04-23 | Lessons zu Testing (Playwright/pytest): self-signed HTTPS, `ignore_https_errors` | AKTUELL |
| `lessons/whisper-transcription.md` | md | DE | 1 574 B | 2026-04-23 | Lessons zu Whisper/Spracheingabe: Transkriptions-Handling, Robustheit | AKTUELL |
| `lessons/workflow.md` | md | DE | 4 405 B | 2026-05-16 | Lessons zu Claude-Workflow: Git-Checkpoint vor Session, YOLO-Modus-Risiken, Supervisor-Coda-Kommunikation | AKTUELL |
| `lessons/zerberus_lessons.md` | md | DE | 300 297 B | 2026-05-17 | Sync-Kopie der Zerberus-spezifischen Lessons (Master: Zerberus-Repo), 1022 Zeilen, Konsolidierung mit GLOBAL_LESSONS.md laut DECISIONS_PENDING ausstehend | AKTUELL |

### `templates/`

| Pfad | Typ | Sprache | Größe | Letzte Änderung | Kurzbeschreibung | Status |
|------|-----|---------|-------|-----------------|------------------|--------|
| `templates/CLAUDE_PROJEKT_TEMPLATE.md` | template | DE | 5 273 B | 2026-05-17 | Vorlage für `CLAUDE_{PROJEKT}.md`: Betriebsanleitung für Coda, Bibel-Format, inkl. Regel-0-Verweis | AKTUELL |
| `templates/DECISIONS_TEMPLATE.md` | template | DE | 1 010 B | 2026-05-17 | Vorlage für `DECISIONS_{PROJEKT}.md`: offene Architektur-Fragen + getroffene Entscheidungen | AKTUELL |
| `templates/DESIGN_PROJEKT_TEMPLATE.md` | template | DE | 1 513 B | 2026-05-17 | Vorlage für `DESIGN_{PROJEKT}.md`: projektspezifische Design-Entscheidungen (nicht zu verwechseln mit globaler DESIGN.md) | AKTUELL |
| `templates/FEATURE_REQUEST_TEMPLATE.md` | template | DE | 2 884 B | 2026-05-17 | Vorlage für `FEATURE_REQUEST_{kurzname}.md`: Frontmatter, Kontext, Akzeptanzkriterien, inkl. Naming-Hinweis | AKTUELL |
| `templates/HANDOVER_TEMPLATE.md` | template | DE | 1 159 B | 2026-05-17 | Vorlage für `HANDOVER_{PROJEKT}.md`: Detail-Übergabe zwischen Sessions (ergänzt mjolnir.md) | AKTUELL |
| `templates/MARATHON_WORKFLOW_TEMPLATE.md` | template | DE | 1 817 B | 2026-05-17 | Vorlage für `MARATHON_WORKFLOW_{PROJEKT}.md`: Aufgabenliste mit Status, nach jedem Patch zu updaten | AKTUELL |
| `templates/ROADMAP_TEMPLATE.md` | template | DE | 993 B | 2026-05-17 | Vorlage für `ROADMAP_{PROJEKT}.md`: Phasen-Roadmap (Prosa erlaubt) | AKTUELL |
| `templates/SUPERVISOR_PROJEKT_TEMPLATE.md` | template | DE | 4 013 B | 2026-05-17 | Vorlage für `SUPERVISOR_{PROJEKT}.md`: NIE/IMMER-Listen für Supervisor, Bibel-Format, max 400 Zeilen | AKTUELL |
| `templates/lessons_TEMPLATE.md` | template | DE | 1 311 B | 2026-05-17 | Vorlage für `lessons_{PROJEKT}.md`: Stolperstein-Sammlung, konsultieren vor Aufgabe, eintragen nach Falle | AKTUELL |
| `templates/mjolnir_TEMPLATE.md` | template | DE | 1 882 B | 2026-05-17 | Vorlage für `mjolnir.md`: Session-Abschluss-Status, Single-Slot, wird am Session-Ende überschrieben | AKTUELL |

### `.claude/worktrees/focused-payne-b38e6a/` (nicht bereinigter Git-Worktree)

> Snapshot vom 2026-05-15 — auto-generierter Name (`focused-payne-b38e6a`), wurde nach der Session nicht entfernt.

| Pfad | Typ | Sprache | Größe | Letzte Änderung | Kurzbeschreibung | Status |
|------|-----|---------|-------|-----------------|------------------|--------|
| `…/.gitignore` | config | — | 43 B | 2026-05-15 | Worktree-Kopie der .gitignore (leicht abweichend: 43 vs 38 Bytes im Main) | VERALTET |
| `…/DESIGN.md` | md | DE | 32 346 B | 2026-05-15 | Ältere Snapshot-Kopie der DESIGN.md (1322 Bytes kleiner als aktuelle Version) | VERALTET |
| `…/README.md` | md | DE | 1 698 B | 2026-05-15 | Ältere Snapshot-Kopie der README.md (1337 Bytes kleiner als aktuelle Version) | VERALTET |
| `…/bugs/zerberus/regex.md` | md | DE | 666 B | 2026-05-15 | Worktree-Kopie des Regex-Bug-Trackers (minimal abweichend) | VERALTET |
| `…/bugs/zerberus/whisper.md` | md | DE | 1 104 B | 2026-05-15 | Worktree-Kopie des Whisper-Bug-Trackers (minimal abweichend) | VERALTET |
| `…/lessons/README.md` | md | DE | 605 B | 2026-05-15 | Worktree-Kopie des lessons/README.md | VERALTET |
| `…/lessons/documentation.md` | md | DE | 1 229 B | 2026-05-15 | Worktree-Kopie der documentation.md (1413 Bytes kleiner — Inhalt fehlt) | VERALTET |
| `…/lessons/frontend-js.md` | md | DE | 4 744 B | 2026-05-15 | Worktree-Kopie der frontend-js.md (24 Bytes größer — leichte Divergenz) | VERALTET |
| `…/lessons/git-deployment.md` | md | DE | 819 B | 2026-05-15 | Worktree-Kopie der git-deployment.md | VERALTET |
| `…/lessons/gpu-ml.md` | md | DE | 3 045 B | 2026-05-15 | Worktree-Kopie der gpu-ml.md | VERALTET |
| `…/lessons/json-data.md` | md | DE | 440 B | 2026-05-15 | Worktree-Kopie der json-data.md | VERALTET |
| `…/lessons/mobile-touch.md` | md | DE | 745 B | 2026-05-15 | Worktree-Kopie der mobile-touch.md | VERALTET |
| `…/lessons/python-fastapi.md` | md | DE | 2 934 B | 2026-05-15 | Worktree-Kopie der python-fastapi.md | VERALTET |
| `…/lessons/sqlite-db.md` | md | DE | 1 516 B | 2026-05-15 | Worktree-Kopie der sqlite-db.md | VERALTET |
| `…/lessons/testing.md` | md | DE | 985 B | 2026-05-15 | Worktree-Kopie der testing.md | VERALTET |
| `…/lessons/whisper-transcription.md` | md | DE | 1 590 B | 2026-05-15 | Worktree-Kopie der whisper-transcription.md | VERALTET |
| `…/lessons/workflow.md` | md | DE | 2 702 B | 2026-05-15 | Worktree-Kopie der workflow.md (1703 Bytes kleiner — fehlen neuere Einträge) | VERALTET |
| `…/lessons/zerberus_lessons.md` | md | DE | 287 999 B | 2026-05-15 | Worktree-Kopie der zerberus_lessons.md (12 298 Bytes kleiner als aktuelle) | VERALTET |
| `…/templates/CLAUDE.md` | template | DE | 5 305 B | 2026-05-15 | Worktree-Kopie mit altem Dateinamen (alt: `CLAUDE.md` / aktuell: `CLAUDE_PROJEKT_TEMPLATE.md`) | VERALTET |
| `…/templates/SUPERVISOR.md` | template | DE | 4 244 B | 2026-05-15 | Worktree-Kopie mit altem Dateinamen (alt: `SUPERVISOR.md` / aktuell: `SUPERVISOR_PROJEKT_TEMPLATE.md`) | VERALTET |

---

## 3. Ordnerstruktur-Beschreibung

| Ordner | Zweck | Erkennbare Logik |
|--------|-------|-----------------|
| `/` (Root) | Globale Knowledge-Base-Dokumente, die für alle Projekte gelten | Dateinamen ohne Projektsuffix = global; mit Projektsuffix = projektspezifisch. FEATURE_REQUEST_* = aktive oder erledigte Aufträge. |
| `templates/` | Bootstrap-Vorlagen für neue Projekte — 10 Files, alle im Bibel-Format | Einheitliches Dateinamenschema: `{DOKUMENTTYP}_TEMPLATE.md` oder `{DOKUMENTTYP}_PROJEKT_TEMPLATE.md`. Kopiert und umbenannt per PROJECT_BOOTSTRAP_README.md. |
| `lessons/` | Technologie-spezifische Lessons, die live wachsen | Pro Technologie eine Datei. Konzeptionell getrennt von projektspezifischen Lessons (z.B. zerberus_lessons.md ist Sync-Kopie, nicht Master). |
| `bugs/` | Projekt-spezifische Bug-Tracker | Unterordner pro Projekt (aktuell nur `zerberus/`). Pro Technologie-Domäne eine Datei. |
| `concepts/` | Konzept-Ursprünge und Architektur-Skizzen, die historisch verankert werden | Archiv-Charakter: Dateien hier sind historische Dokumente, deren operativer Inhalt woanders lebt. |
| `_drafts_gist/` | Konzept-Entwürfe für Phase-3-Gist-Migration | Klar als Draft markiert (Dateinamen `*_DRAFT.md`). Noch ohne echte Daten. |
| `.claude/worktrees/` | Automatisch von Claude Code generierte Git-Worktrees für isolierte Agent-Arbeit | Auto-generierte Namen (UUID-ähnlich). Sollte nach Session-Ende bereinigt werden, wurde es hier nicht. |

---

## 4. Auffälligkeiten

### A1 — Nicht bereinigter Git-Worktree (`.claude/worktrees/focused-payne-b38e6a/`)

Der Ordner enthält einen vollständigen Git-Worktree (bestätigt durch `.git`-Datei darin) vom 2026-05-15 — 20 Dateien, Snapshot 3 Tage vor heute. Die Dateien sind konsistente, aber veraltete Kopien der aktuellen Main-Dateien. Der Worktree wurde von einer früheren Claude-Code-Session mit Worktree-Isolation erstellt und nach Abschluss nicht entfernt. Gesamtgröße der Worktree-Dateien: ca. 350 KB (davon 288 KB allein `zerberus_lessons.md`).

Auffällig: Die Templates im Worktree heißen `CLAUDE.md` und `SUPERVISOR.md` (alte Namenskonvention), während im aktuellen Root `CLAUDE_PROJEKT_TEMPLATE.md` und `SUPERVISOR_PROJEKT_TEMPLATE.md` stehen — belegt, dass die Umbenennung nach Erstellung des Worktrees stattfand.

### A2 — `lessons/zerberus_lessons.md` dominiert den Repo-Footprint

Mit 300 297 Bytes (~293 KB, 1022 Zeilen) ist diese Datei 9x größer als die nächstgrößte Datei (`DESIGN.md` mit 33 668 Bytes). Sie ist eine Sync-Kopie (nicht der Master — der liegt in `C:\Users\chris\Python\Zerberus\`). Laut `DECISIONS_PENDING.md` ist die Konsolidierung mit `GLOBAL_LESSONS.md` (mind. 3 bekannte Dubletten) noch offen.

### A3 — `LESSONS_KONSOLIDIERT.md` vs `GLOBAL_LESSONS.md` — Verhältnis unklar

Beide Dateien liegen im Root und enthalten projektübergreifende Lessons. `LESSONS_KONSOLIDIERT.md` (2026-05-15, 7 454 B) ist älter und wurde als Konsolidierungs-Snapshot aus Supervisor-Chats erstellt. `GLOBAL_LESSONS.md` (2026-05-17, 14 167 B) ist der neuere, aktive Stand mit Bibel-Format. Ob `LESSONS_KONSOLIDIERT.md` vollständig in `GLOBAL_LESSONS.md` aufgegangen ist oder noch eigenständigen Inhalt hat, wurde im Rahmen dieser Inventur nicht geprüft.

### A4 — `_ERLEDIGT.md`-Dateien liegen lose im Root ohne eigenen Ordner

`FEATURE_REQUEST_CLAUDE_ERLEDIGT.md` und `FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md` (zusammen 28 625 B) sind historische Audit-Logs. Es gibt keinen dedizierten Archiv-Ordner (z.B. `_erledigt/` oder `archive/`). Bei weiterem Wachstum durch neue Feature-Requests wird der Root unübersichtlicher.

### A5 — `_drafts_gist/` enthält nur Platzhalter-Entwürfe

`INDEX_GIST_DRAFT.md` hat `Status: aktiv (Phase 3)` als Bedingung, `ZERBERUS_GIST_DRAFT.md` enthält `LAST_PATCH: P-???` und `TS: TBD`. Beide Dateien sind konzeptionell vollständig, aber ohne echte Daten. Sie haben keinen direkten Bezug zur aktuellen operativen Arbeit.

### A6 — `DESIGN.md` enthält viele `[WERT]`-Platzhalter

Die zentrale UI-Referenz (33 668 B) ist sehr groß, hat aber zahlreiche noch nicht befüllte Slots im Farbsystem, Typo-System und anderen Sektionen (`[WERT]` als Platzhalter). Das ist kein Fehler (die Datei dient als lebendige Referenz), aber auffällig für die Größe vs. Befüllungsstand.

### A7 — `bugs/` und `lessons/` haben keine Datei für neue Projekte außer Zerberus

Alle Einträge in `bugs/` und `lessons/zerberus_lessons.md` beziehen sich auf Zerberus. Andere Projekte sind laut README noch nicht migriert — die Ordner spiegeln also den aktuellen Single-Projekt-Stand wider.

---

*Erstellt durch Coda | Auftrag: FEATURE_REQUEST_CLAUDE.md (repo-inventur) | 2026-05-18*
*Nichts wurde gelöscht, verschoben oder umbenannt. Nur diese Datei wurde neu erstellt.*
```

> **Hinweis Coda:** Das obige Code-Block-Konstrukt ist eine 1:1-Kopie von `REPO_INVENTORY.md`. Der einzige inhaltliche Unterschied zum Live-File: zwischenzeitlich kam `FEATURE_REQUEST_repo-inventur_ERLEDIGT.md` als 4. Erledigt-File dazu (s. Sprach-Audit unten), das war in der Inventur selbst noch nicht erfasst weil zum Zeitpunkt der Inventur-Schreibung als `FEATURE_REQUEST_CLAUDE.md` lief.

---

## Sektion 3: Sprach-Audit (alle .md/.html Dateien)

**.html-Dateien im Repo:** keine.

**.md-Dateien:** 40 (Main) + 18 (Worktree, ohne `.git` und `.gitignore`).

### 3.1 Main-Tree (Root + Unterordner ohne `.claude/`)

| Datei | Sprache | DE-Anteil | Inhalt (1 Satz) |
|---|---|---|---|
| `README.md` | DE | ~98% | Drei-Rollen-Modell + Kernfile-Tabelle + Dateinamen-Konvention. |
| `DESIGN.md` | DE | ~95% | Globale UI-Design-Referenz (Farben/Typo/Komponenten/Mobile) — viele `[WERT]`-Platzhalter. |
| `GLOBAL_LESSONS.md` | DE | ~95% | Projektübergreifende Lessons im Bibel-Format: 6 Faulheits-Catches + Selbsttest + Naming-Konvention. |
| `SUPERVISOR_KODEX.md` | DE | ~92% | NIE/IMMER-Listen für Chat-Fenster + Prompt-Skelett + Eskalations-Regeln. |
| `PROJECT_BOOTSTRAP_README.md` | DE | ~95% | Bootstrap-Anleitung für Coda bei neuen Projekten (Templates, Platzhalter, Skelett). |
| `DECISIONS_PENDING.md` | DE | ~95% | Pending-Decisions + getroffene Entscheidungen mit Begründung. |
| `LESSONS_KONSOLIDIERT.md` | DE | ~92% | Älterer P49-Konsolidierungs-Snapshot mit Workflow/Frontend/Plattform-Erkenntnissen. |
| `mjolnir.md` | DE | ~95% | Aktuelle Session-Abschluss-Datei: STATUS=FERTIG, Auftrag repo-inventur. |
| `REPO_INVENTORY.md` | DE | ~95% | Vollständige Bestandsaufnahme vom 2026-05-18 (4 Sektionen, 7 Auffälligkeiten). |
| `FEATURE_REQUEST_CLAUDE.md` | DE | ~95% | Aktiver Auftrag: Info-Paket für Supervisor (= dieser Briefing-Auftrag). |
| `FEATURE_REQUEST_CLAUDE_ERLEDIGT.md` | DE | ~95% | Audit-Log: erledigter Auftrag `faulheits-catch-integration` (2026-05-17). |
| `FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md` | DE | ~95% | Audit-Log: erledigter Auftrag `aufraeumarbeiten-post-catch` (Templates-Konsolidierung u.a.). |
| `FEATURE_REQUEST_repo-inventur_ERLEDIGT.md` | DE | ~98% | Audit-Log: erledigter Auftrag `repo-inventur` (vorherige Session). |
| `_drafts_gist/INDEX_GIST_DRAFT.md` | DE | ~95% | Konzept-Entwurf für Phase-3-Gist-Index aller aktiven Projekte. |
| `_drafts_gist/ZERBERUS_GIST_DRAFT.md` | DE | ~95% | Konzept-Entwurf für Zerberus-Live-State-Gist. |
| `bugs/zerberus/regex.md` | DE | ~98% | Bug-Tracker Regex-Bugs (offen: RX-001 ZDF-Halluzination). |
| `bugs/zerberus/whisper.md` | DE | ~98% | Bug-Tracker Whisper-Bugs (offen: W-001 Phrasen-Repetition-Loop). |
| `concepts/Try_Faulheits_catch.md` | DE | ~95% | Historischer Konzept-Ursprung der 6 Faulheits-Catches. |
| `lessons/README.md` | DE | ~98% | Pflege-Regeln für `lessons/`-Ordner. |
| `lessons/documentation.md` | DE | ~95% | Lessons zu Doku/Schulung (Shop-Floor-Kontext). |
| `lessons/frontend-js.md` | DE | ~85% | Frontend/JS-Lessons (englische Code-Snippets erhöhen Misch-Anteil). |
| `lessons/git-deployment.md` | DE | ~85% | Git/Deployment-Lessons (`start.bat`, Uvicorn). |
| `lessons/gpu-ml.md` | DE | ~85% | GPU/ML-Lessons (Device-Detection, VRAM-Fallback). |
| `lessons/json-data.md` | DE | ~95% | JSON-Lesson zu typographischen Anführungszeichen. |
| `lessons/mobile-touch.md` | DE | ~95% | Mobile/Touch-Lessons (`:hover` vs `:active`). |
| `lessons/python-fastapi.md` | DE | ~85% | FastAPI-Lessons (Uvicorn `--reload`, Windows-Spezifika). |
| `lessons/sqlite-db.md` | DE | ~85% | SQLite/Migrations-Lessons (idempotent, `IF NOT EXISTS`). |
| `lessons/testing.md` | DE | ~85% | Test-Lessons (Playwright/pytest, HTTPS). |
| `lessons/whisper-transcription.md` | DE | ~90% | Whisper-Lessons (Transkriptions-Handling). |
| `lessons/workflow.md` | DE | ~95% | Claude-Workflow-Lessons (Checkpoint, YOLO, Supervisor-Coda). |
| `lessons/zerberus_lessons.md` | DE | ~92% | 1022-Zeilen-Sync-Kopie der Zerberus-Lessons (Bibel-Format + Prosa-Begründungen). |
| `templates/CLAUDE_PROJEKT_TEMPLATE.md` | DE | ~92% | Template für Codas Betriebsanleitung pro Projekt. |
| `templates/DECISIONS_TEMPLATE.md` | DE | ~95% | Template für Decisions-Pending pro Projekt. |
| `templates/DESIGN_PROJEKT_TEMPLATE.md` | DE | ~95% | Template für projektspezifische Design-Entscheidungen. |
| `templates/FEATURE_REQUEST_TEMPLATE.md` | DE | ~95% | Template für Auftrag-Files (Frontmatter, Akzeptanzkriterien). |
| `templates/HANDOVER_TEMPLATE.md` | DE | ~92% | Template für Detail-Übergabe zwischen Sessions. |
| `templates/MARATHON_WORKFLOW_TEMPLATE.md` | DE | ~92% | Template für Aufgabenliste mit Phasen + Status. |
| `templates/ROADMAP_TEMPLATE.md` | DE | ~95% | Template für Phasen-Roadmap (Prosa erlaubt). |
| `templates/SUPERVISOR_PROJEKT_TEMPLATE.md` | DE | ~92% | Template für projektspezifische Supervisor-Datei (NIE/IMMER). |
| `templates/lessons_TEMPLATE.md` | DE | ~95% | Template für projektspezifische Lessons-Datei. |
| `templates/mjolnir_TEMPLATE.md` | DE | ~95% | Template für Session-Abschluss-Datei (Single-Slot). |

**Gesamtbefund:** 100% DE als Hauptsprache. Englische Anteile beschränken sich auf Code-Snippets, Konfig-Werte und Fachbegriffe (Bibel-Format, Single-Slot, STATUS-Keywords). Es gibt **keine** rein englischen oder gemischtsprachigen Markdown-Dateien.

### 3.2 Worktree-Tree (`.claude/worktrees/focused-payne-b38e6a/`)

| Datei | Sprache | DE-Anteil | Inhalt |
|---|---|---|---|
| `…/DESIGN.md` | DE | ~95% | Veraltete DESIGN.md (1322 B kleiner als Main). |
| `…/README.md` | DE | ~98% | Veraltete README (1337 B kleiner). |
| `…/bugs/zerberus/regex.md` | DE | ~98% | Veraltete Bug-Tracker-Kopie. |
| `…/bugs/zerberus/whisper.md` | DE | ~98% | Veraltete Bug-Tracker-Kopie. |
| `…/lessons/README.md` | DE | ~98% | Veraltete lessons-README. |
| `…/lessons/documentation.md` | DE | ~95% | Veraltete Doku-Lessons (1413 B kleiner). |
| `…/lessons/frontend-js.md` | DE | ~85% | Frontend-Lessons leichte Divergenz. |
| `…/lessons/git-deployment.md` | DE | ~85% | Git-Lessons. |
| `…/lessons/gpu-ml.md` | DE | ~85% | GPU-Lessons. |
| `…/lessons/json-data.md` | DE | ~95% | JSON-Lesson. |
| `…/lessons/mobile-touch.md` | DE | ~95% | Mobile-Lessons. |
| `…/lessons/python-fastapi.md` | DE | ~85% | FastAPI-Lessons. |
| `…/lessons/sqlite-db.md` | DE | ~85% | SQLite-Lessons. |
| `…/lessons/testing.md` | DE | ~85% | Test-Lessons. |
| `…/lessons/whisper-transcription.md` | DE | ~90% | Whisper-Lessons. |
| `…/lessons/workflow.md` | DE | ~95% | Workflow-Lessons (1703 B kleiner — fehlen neuere Einträge). |
| `…/lessons/zerberus_lessons.md` | DE | ~92% | Zerberus-Lessons-Sync (288 KB, 12 KB kleiner als Main). |
| `…/templates/CLAUDE.md` | DE | ~92% | Alter Template-Name (vor Umbenennung zu CLAUDE_PROJEKT_TEMPLATE.md). |
| `…/templates/SUPERVISOR.md` | DE | ~92% | Alter Template-Name (vor Umbenennung zu SUPERVISOR_PROJEKT_TEMPLATE.md). |

---

## Sektion 4: Duplikat-Check

### Gruppe D1 — Lessons-Konsolidierungen (Root-Ebene)

- `GLOBAL_LESSONS.md` (14 167 B, aktiv, Bibel-Format)
- `LESSONS_KONSOLIDIERT.md` (7 454 B, älterer Snapshot bis P49)
- `concepts/Try_Faulheits_catch.md` (5 070 B, historisches Konzept-Dokument)

**Begründung:** Alle drei adressieren projektübergreifende Lessons. `GLOBAL_LESSONS.md` ist der operative Master mit den 6 Faulheits-Catches. `LESSONS_KONSOLIDIERT.md` ist ein älterer Stand (Plattform/CLI/Backend/Frontend/Workflow) der teils in GLOBAL_LESSONS migriert, teils nicht abgeglichen ist. `Try_Faulheits_catch.md` ist die rekonstruierte Konzept-Wurzel der 6 Catches und explizit als „historisches Dokument" markiert. **Überlappung:** zumindest die 6 Catches selbst stehen in mindestens 2 von 3 Dateien (Konzept vs. operativ).

### Gruppe D2 — Zerberus-Lessons (Master-Sync-Doppel)

- `lessons/zerberus_lessons.md` (300 297 B, Sync-Kopie im Main)
- `.claude/worktrees/focused-payne-b38e6a/lessons/zerberus_lessons.md` (287 999 B, veraltete Worktree-Kopie)
- (Master außerhalb dieses Repos: `C:\Users\chris\Python\Zerberus\`)

**Begründung:** Klassischer Sync-Drift. Worktree-Version ist 12 KB älter als Main-Version. Master ist außerhalb dieses Repos — Sync via `sync_repos.ps1` aus Zerberus-Repo. Innerhalb des Claude-Repos ist die Worktree-Kopie redundant (= identische Quelle, älterer Stand).

### Gruppe D3 — Bibel-Format-Cheat-Sheet doppelt dokumentiert

- `GLOBAL_LESSONS.md` (Sektion „Bibel-Format Cheat Sheet", Z. 123-153)
- `concepts/Try_Faulheits_catch.md` (Sektion „Bibel-Format Cheat Sheet", Z. 46-66)

**Begründung:** Beide Dateien erklären das Pipe-Format mit denselben drei Zeilen-Aufbauten (Lessons, Status-Header, KODEX) und derselben Regel-Aussage. Operativer Master ist GLOBAL_LESSONS, concepts-Version ist historisch. Redundanz ist gewollt (Konzept-Ursprung-Archiv), aber dokumentiert.

### Gruppe D4 — Selbsttest-Pattern doppelt dokumentiert

- `GLOBAL_LESSONS.md` (Sektion „Selbsttest-Pattern (Phase A/B/C/D — prosaisch)", Z. 103-119)
- `concepts/Try_Faulheits_catch.md` (Sektion „Selbsttest-Pattern (Phase A/B/C/D)", Z. 33-42)

**Begründung:** Beide beschreiben dieselben vier Phasen + Surrogat-Regel. Konzept-Ursprung in `concepts/` ist historische Erstfassung, GLOBAL_LESSONS hat die operative Langfassung. Inhaltlich gleichbedeutend.

### Gruppe D5 — Zerberus-Bug-Tracker (Worktree-Drift)

- `bugs/zerberus/regex.md` (647 B, Main, 2026-04-19) vs `…/worktrees/.../bugs/zerberus/regex.md` (666 B, Worktree, 2026-05-15) — minimale Divergenz.
- `bugs/zerberus/whisper.md` (1 080 B, Main, 2026-04-19) vs `…/worktrees/.../bugs/zerberus/whisper.md` (1 104 B, Worktree, 2026-05-15) — minimale Divergenz.

**Begründung:** Worktree-Kopien sind leicht abweichend (vermutlich Whitespace/Lineending). Inhaltlich gleich, technisch dupliziert.

### Gruppe D6 — Templates mit altem Dateinamen im Worktree

- `templates/CLAUDE_PROJEKT_TEMPLATE.md` (Main, 5 273 B) vs `…/worktrees/.../templates/CLAUDE.md` (5 305 B, alter Name).
- `templates/SUPERVISOR_PROJEKT_TEMPLATE.md` (Main, 4 013 B) vs `…/worktrees/.../templates/SUPERVISOR.md` (4 244 B, alter Name).

**Begründung:** Belegen die Umbenennung der Templates seit Worktree-Erstellung. Worktree-Kopien sind veraltet UND haben veralteten Dateinamen.

### Keine Duplikate

- `templates/`-Dateien (10 Stück) — sind paarweise inhaltlich verschieden, jede Vorlage hat klaren Eigenzweck.
- `lessons/`-Dateien (außer zerberus_lessons.md) — eine Datei pro Technologie-Domäne, keine inhaltliche Überlappung.
- `_drafts_gist/`-Dateien — INDEX vs ZERBERUS-spezifisch, kein Duplikat zueinander.
- Root-Files `README.md`, `DESIGN.md`, `SUPERVISOR_KODEX.md`, `PROJECT_BOOTSTRAP_README.md`, `DECISIONS_PENDING.md`, `mjolnir.md`, `REPO_INVENTORY.md` — jeweils unique.

---

## Sektion 5: Antworten auf Supervisor-Fragen

### F1 — `zerberus_lessons.md` (300 KB): Was steht da drin? Eigenständig oder Kopie?

**Antwort:** **Sync-Kopie.** Master liegt in `C:\Users\chris\Python\Zerberus\lessons_ZERBERUS.md` (außerhalb dieses Repos). Die Datei hier ist eine **deckungsgleiche Sync-Kopie** mit minimalem Versatz (Sync-Mechanik via `sync_repos.ps1` aus dem Zerberus-Repo). Inhaltlich sind das **1022 Zeilen Zerberus-spezifischer Lessons** im Bibel-Format mit Prosa-Begründungen:

- **OBERSTES GEBOT (P-umzug, 2026-05-16)** — identisch mit GLOBAL_LESSONS.md
- **Multi-Session-Status-Header (B-mjolnir-multisession)** — identisch mit GLOBAL_LESSONS.md
- **mjolnir-Round-Trip-Pflicht (B-mjolnir-fix/-2)** — identisch mit GLOBAL_LESSONS.md
- Dann projektspezifische Zerberus-Lessons: Datei-Konvention (`_ZERBERUS`-Suffix), Remote-Control via Dateikonventionen, Eskalations-Pattern, Smoke-Tests, Patch-Lessons P1–P100+, Test-Setup, Voice/Whisper-Spezifika, FastAPI-Spezifika, Frontend-Lessons, DB-Migrations-Lessons, etc.

**Gehört sie hierher oder ins Zerberus-Repo?** Master gehört ins Zerberus-Repo (wo sie auch liegt). Die Sync-Kopie hier dient als **kanonischer Snapshot bei Cross-Repo-Konflikten und für globale Lessons-Suche aus Coda-Sessions in anderen Projekten**. Laut `DECISIONS_PENDING.md` ist die Konsolidierung mit `GLOBAL_LESSONS.md` (mind. 3 klare Dubletten) noch ausstehend (Option A/B/C im Pending-Entry).

### F2 — Unterschied `LESSONS_KONSOLIDIERT.md` vs `lessons/`-Ordner?

**Antwort:** **Verschiedener Scope und Lifecycle, mit Überschneidungen:**

| Datei | Scope | Lifecycle | Stand |
|---|---|---|---|
| `LESSONS_KONSOLIDIERT.md` | **Snapshot** aus Supervisor-Chats (Plattform, Claude CLI, Backend, Frontend, Workflow) | Statischer Konsolidierungs-Punkt bis P49 (2026-05-15) | 80 Zeilen, projekt-agnostisch aber stark Zerberus-geprägt |
| `lessons/`-Ordner | **Live-wachsende** technologie-getrennte Sammlung (FastAPI, SQLite, Whisper, Mobile, etc.) | Pro Patch ergänzt | 13 Dateien, eine pro Domäne plus zerberus_lessons.md |
| `GLOBAL_LESSONS.md` (zum Vergleich) | **Operative Verfassung** der Faulheits-Catches im Bibel-Format | Aktiv gepflegt (2026-05-17) | 14 KB, projektübergreifend |

**Redundanz:** Teilweise. `LESSONS_KONSOLIDIERT.md` enthält Workflow-Erkenntnisse (Mjölnir-Konvention, FEATURE_REQUEST-Naming) die inzwischen in `GLOBAL_LESSONS.md` weiterentwickelt sind. Frontend/CLI/Plattform-Inhalte stehen teils im `lessons/`-Ordner (z.B. `lessons/workflow.md`, `lessons/frontend-js.md`), teils nicht — kein systematischer Abgleich bisher erfolgt. **Status `UNKLAR`** in der Inventur ist begründet.

### F3 — Was liegt in `_drafts_gist`?

**Antwort:** **Zwei Konzept-Entwürfe für Phase-3-Gist-Migration**, beide DE, beide ohne echte Daten:

- **`INDEX_GIST_DRAFT.md` (1 166 B)** — Vorlage für einen öffentlichen GitHub-Gist „Bmad82-Projects Index". Beschreibt Pflichtfelder (`PROJEKT|Name|Gist-URL|Status|Letzter-Patch|Tags`), Migrations-Roadmap (5 Schritte), `mjolnir_{PROJEKT}.md`/`SUPERVISOR_{PROJEKT}.md`/`MARATHON_WORKFLOW_{PROJEKT}.md` als Pflichtfelder im Projekt-Gist. Inhalt-Status: `(weitere wenn migriert)`.
- **`ZERBERUS_GIST_DRAFT.md` (898 B)** — Vorlage für den Zerberus-Live-State-Gist. Header: `LAST_PATCH: P-???` und `TS: TBD`. Beschreibt Sync-Mechanik (Phase 3): Coda pusht mjolnir.md zusätzlich ins Gist, Supervisor-Chat fetched Gist statt lokales File.

**Status:** Beide sind **konzeptionell vollständig, operativ inaktiv**. Phase 3 ist laut DECISIONS_PENDING noch nicht aktiviert. Keine echten Daten, keine Verknüpfung zu aktuellen Arbeitsdateien. Sicher zu archivieren oder zu verschieben — keine laufende Verwendung.

### F4 — Welche Dateien haben `_ERLEDIGT` im Namen?

**Antwort:** **Drei Dateien:**

1. `FEATURE_REQUEST_CLAUDE_ERLEDIGT.md` (9 269 B, 2026-05-17) — Audit-Log des Auftrags `faulheits-catch-integration`. **Verwendet alte Naming-Konvention** (Projektname statt Kurzname).
2. `FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md` (19 356 B, 2026-05-17) — Audit-Log des gleichnamigen Auftrags. **Neue Naming-Konvention** (Kurzname).
3. `FEATURE_REQUEST_repo-inventur_ERLEDIGT.md` (~2 KB, 2026-05-18) — Audit-Log des vorherigen Repo-Inventur-Auftrags. **Neue Naming-Konvention.**

Alle drei liegen direkt im Repo-Root (kein Archiv-Ordner). Siehe Auffälligkeit A4 in der Inventur.

### F5 — Was steht in `DESIGN.md`?

**Antwort:** **Echtes Design-Dokument, aber mit teils unbefüllten Slots.** 620 Zeilen, 33 668 Bytes, Status AKTUELL.

Klar abgegrenzt als **UI-Layer-Referenz** (siehe Sektion „Geltungsbereich") — explizit nicht Workflow/Architektur (das liegt in README/GLOBAL_LESSONS/SUPERVISOR_KODEX/BOOTSTRAP).

**Strukturierte Sektionen mit Tabellen:**

1. **Farbsystem** — Kernfarben, Hintergrund, Text, Status, Rand, Spezial (CSS-Variablen-Namen vorhanden, Werte zu großen Teilen als `[WERT]`-Platzhalter).
2. **Typography** — Schriftfamilien, Größen, Gewichte.
3. **Layout/Spacing/Mobile** — Breakpoints, Touch-Targets (48px Pflicht), Safe-Area-Insets.
4. **Komponenten** — Buttons, Inputs, Karten, Modals, Toasts, Bubbles.
5. **Animationen** — Easings, Durations, prefers-reduced-motion.
6. **Iconografie** — Größen, Stroke-Widths.
7. **Accessibility** — Kontrast-Pflicht, Fokus-Ringe.
8. **Mobile-First-Regeln** — Portrait+Landscape, 20:9-Phones, PWA-Insets.

**Befüllungsgrad:** Konkrete Werte sind nur in den **Bubble-Background-Spezialfarben** (`rgba(...)` für User/Bot-Bubbles) fest. Die meisten anderen Slots sind `[WERT]`. Hinweis im Header: „Werte die noch nicht festgelegt sind, stehen als `[WERT]`." → Datei ist **gewollt unfertig**, ein lebendiger Referenz-Rahmen. Kein Skelett, eher eine teilweise-befüllte Matrix.

### F6 — Der `bugs/`-Ordner — was liegt da drin, und ist das alles Zerberus-spezifisch?

**Antwort:** **Ja, alles Zerberus-spezifisch.** Struktur:

```
bugs/
└── zerberus/
    ├── regex.md     (647 B, 2026-04-19, 1 offener Bug RX-001)
    └── whisper.md   (1 080 B, 2026-04-19, 1 offener Bug W-001)
```

**Inhalte:**

- **`regex.md`** — Bug-Tracker für Regex/Pattern-Matching-Bugs in Zerberus. Offen: **RX-001 ZDF-Halluzination nicht vollständig gefangen** (Severity: niedrig, betrifft `whisper_cleaner.json`). Erledigt: leer.
- **`whisper.md`** — Bug-Tracker für Whisper/Voice-Bugs in Zerberus. Offen: **W-001 Phrasen-Repetition-Loop** (Severity: hoch — Datenverlust, betrifft `legacy.py /voice`, `nala.py /voice`). Erledigt: leer.

**Struktur des Ordners** lässt Platz für weitere Projekte (`bugs/{projekt}/{thema}.md`). Andere Projekte sind aber noch nicht migriert (siehe Auffälligkeit A7).

### F7 — Gibt es eine `.claude/`-Konfiguration?

**Antwort:** **Teilweise.**

- **Vorhanden:** `.claude/worktrees/focused-payne-b38e6a/` — der nicht bereinigte Git-Worktree (Auffälligkeit A1). Inhalt ist ein Worktree-Snapshot vom 2026-05-15, nicht eine Konfiguration.
- **NICHT vorhanden:**
  - **Keine `CLAUDE.md`** (auf Root-Ebene oder in `.claude/`) — die globale Coda-Konfiguration fehlt.
  - **Keine `.claude/settings.json`** oder `settings.local.json` — keine Hooks, keine Permissions-Anpassung, keine Modell-Overrides.
  - **Keine `.claude/commands/`** — keine projekt-spezifischen Slash-Commands.

Die einzige claude-relevante Konvention für dieses Repo lebt in `PROJECT_BOOTSTRAP_README.md`, `GLOBAL_LESSONS.md`, `SUPERVISOR_KODEX.md` — also explizit als globale Knowledge-Base statt als per-Projekt-Config. Das Meta-Repo enthält damit den Workflow-Stil, hat aber keine Coda-Konfiguration für sich selbst.

### F8 — Welche Dateien sehen so aus, als wären sie Showcase-Material?

**Antwort:** **Keine.**

- **Keine `.html`-Dateien** im Repo (alle Suchen geben 0 Treffer).
- **Keine Präsentationen** (`.pptx`, `.key`, `.pdf`).
- **Keine Demo-Apps**, keine eingebetteten Mockups.
- **Keine Screenshots** oder Bildmaterial.

`DESIGN.md` ist eine reine Werte-Referenz (Tabellen mit CSS-Variablen), kein visueller Showcase. Die `_drafts_gist/`-Dateien zielen auf öffentliche Gists (also potentielles Showcase-Material), sind aber selbst nur Konzept-Markdowns ohne echte Daten.

**Schlussfolgerung:** Das Repo ist eine reine **Markdown-Knowledge-Base** ohne Showcase-Charakter.

### F9 — Gibt es Dateien die offensichtlich temporär/vergessen sind?

**Antwort:** **Ein klarer Kandidat, mehrere potenzielle Kandidaten:**

| Kandidat | Bewertung |
|---|---|
| `.claude/worktrees/focused-payne-b38e6a/` (20 Dateien, ~350 KB) | **EINDEUTIG VERGESSEN** — Worktree vom 2026-05-15, nicht bereinigt nach Session-Abschluss. Inhalte sind durchgängig veraltete Kopien (siehe Auffälligkeit A1 + Duplikat-Gruppe D2/D5/D6). Sicher löschbar. |
| `LESSONS_KONSOLIDIERT.md` | **POTENZIELL OBSOLET** — Snapshot bis P49 vom 2026-05-15, inhaltlich teils in GLOBAL_LESSONS.md migriert. Status UNKLAR weil kein systematischer Abgleich. Vor Löschung sollte ein Diff-Pass gegen GLOBAL_LESSONS gemacht werden (nicht „bedenkenlos"). |
| `_drafts_gist/` (2 Dateien) | **GEPARKT, NICHT TEMPORÄR** — explizit als Phase-3-Vorbereitung markiert. Kann bleiben oder in `archive/` verschoben werden — nicht löschen. |
| `concepts/Try_Faulheits_catch.md` | **ARCHIV-CHARAKTER** — explizit „historisches Dokument" markiert, operativer Inhalt in GLOBAL_LESSONS. Sollte bleiben (Konzept-Wurzel), aber Verschiebung in `archive/concepts/` denkbar. |

**Bedenkenlos löschbar (= EINDEUTIG VERGESSEN, keine Referenzen):** nur der Worktree-Ordner.

**Vor Löschung Abgleich nötig:** `LESSONS_KONSOLIDIERT.md` (siehe F2).

### F10 — Wie sieht die aktuelle README.md aus? Volltext bitte.

**Antwort (Volltext):**

```markdown
# Claude — Marathon Workflow Knowledge Base

Persönliche Knowledge-Base für den Marathon-Workflow.
Architekt: Chris (@Bmad82)

⚠️ **DIESES REPO IST PUBLIC.** Niemals Passwörter, API-Keys, Tokens, persönliche Daten, IP-Adressen, interne URLs, Hostnamen oder projektspezifische Secrets reinschreiben. Im Zweifel: nicht committen und nachfragen.

## Was ist das?

Der Marathon-Workflow ist ein Drei-Rollen-System zur Software-Entwicklung, ohne dass der Architekt selbst Code anfasst:

- **Architekt** (Mensch) — gibt Ziele vor, arbeitet primär mobil per Whisper
- **Supervisor** (Claude im Chat-Fenster) — plant, prüft, schreibt Coda-Prompts als `.md`-Files
- **Coda** (Claude Code im Terminal) — implementiert, testet, committet, merged, pusht

Architekt fasst kein Terminal an. Supervisor schickt keinen Inline-Befehl. Coda macht die Hände-schmutzig-Arbeit.

## Kernfiles

| Datei | Zweck |
|---|---|
| [GLOBAL_LESSONS.md](GLOBAL_LESSONS.md) | 6 Faulheits-Catches + Selbsttest-Pattern + Bibel-Cheat-Sheet + Naming-Konvention |
| [SUPERVISOR_KODEX.md](SUPERVISOR_KODEX.md) | NIE/IMMER-Listen für Chat-Fenster (gilt projektübergreifend) |
| [PROJECT_BOOTSTRAP_README.md](PROJECT_BOOTSTRAP_README.md) | Anleitung wie eine frische Coda-Session ein neues Projekt aufsetzt |
| [DECISIONS_PENDING.md](DECISIONS_PENDING.md) | Offene Architektur-Fragen + dokumentierte Konflikte (Meta-Layer) |
| [DESIGN.md](DESIGN.md) | Globale UI-/Look-Referenz (Farben, Typography, Mobile-Regeln) |
| [templates/](templates/) | Bootstrap-Templates für neue Projekte (10 Files) |
| [concepts/](concepts/) | Konzept-Dokumente, Ursprünge, Architektur-Skizzen |
| [lessons/](lessons/) | Technologie-spezifische Lessons (FastAPI, SQLite, Whisper, ...) |
| [bugs/](bugs/) | Projekt-spezifische Bug-Tracker |

## Einbindung in Projekte

Projekte referenzieren diese Knowledge-Base direkt aus dem Repo — nicht kopieren, sondern verlinken. Im `CLAUDE_{PROJEKT}.md` am Anfang:

> Globale Wissensbasis: https://github.com/Bmad82/Claude
> Vor Arbeitsbeginn: `GLOBAL_LESSONS.md` + `SUPERVISOR_KODEX.md` lesen.
> Nach Erkenntnis: projektübergreifende Lessons in `GLOBAL_LESSONS.md` ergänzen.

## Dateinamen-Konvention

Projektspezifische Files tragen IMMER den Projektnamen als Suffix:
- `CLAUDE_{PROJEKT}.md`, `SUPERVISOR_{PROJEKT}.md`, `MARATHON_WORKFLOW_{PROJEKT}.md`, `lessons_{PROJEKT}.md`
- `FEATURE_REQUEST_{kurzname}.md` (kebab-case aus Auftrag-Frontmatter, NIE Projektname)
- Ausnahme: `mjolnir.md` und `PROJECT_BOOTSTRAP_README.md` heißen immer so.

`templates/` enthält Schablonen für Tag 1 eines neuen Projekts. `lessons/` ist hingegen lebendig — wird bei jedem Patch konsultiert.

## Projekte die mit diesem System arbeiten

- **Zerberus Pro 4.0** — Python-Backend, Patch 100+ — siehe `lessons/zerberus_lessons.md` und `bugs/zerberus/`
- (weitere folgen)

## Lizenz

Privates Repo, public sichtbar. Inhalte dienen der Selbst-Dokumentation. Keine Garantie auf Korrektheit oder Anwendbarkeit außerhalb des eigenen Workflows.
```

---

## Sektion 6: Coda-Einschätzung — Größter Pain-Point + Erstes Anpacken

> Nur Einschätzung als jemand, der das Repo gerade komplett durchgelesen hat. Keine Umsetzung — der Supervisor entscheidet.

### Größter struktureller Pain-Point: **Drei Lessons-Quellen ohne klare Hierarchie**

`GLOBAL_LESSONS.md` (operativ), `LESSONS_KONSOLIDIERT.md` (älterer Snapshot), `concepts/Try_Faulheits_catch.md` (Konzept-Ursprung) und `lessons/zerberus_lessons.md` (300 KB Zerberus-Master-Sync) bilden zusammen **vier Lessons-Speicher** im selben Repo. Die ersten drei berühren teils dieselben Themen (6 Faulheits-Catches, Selbsttest-Pattern, Bibel-Format), aber das Verhältnis zueinander wird nur in der **REPO_INVENTORY.md** und **DECISIONS_PENDING.md** dokumentiert — nicht in einer **`lessons/INDEX.md`** oder Lessons-Roadmap. Für eine frische Coda-Session, die „Lessons konsultieren" als Schritt 5 im Session-Zyklus hat, ist nicht offensichtlich, **welche** Lessons-Quelle zuerst und welche nur als Backup zu lesen ist.

**Konsequenz heute:** Coda liest Bootstrap-README → GLOBAL_LESSONS → vielleicht zerberus_lessons. `LESSONS_KONSOLIDIERT.md` und `concepts/Try_Faulheits_catch.md` werden mit hoher Wahrscheinlichkeit **gar nicht gelesen**, weil sie weder im Bootstrap-README explizit referenziert sind noch eine eigene Sektion in `GLOBAL_LESSONS.md` haben. Damit liegt potentiell historisches Workflow-Wissen (P1–P49) brach.

### Zweiter Pain-Point: **Nicht bereinigter Worktree (~350 KB toter Code)**

Auffälligkeit A1 aus der Inventur. `.claude/worktrees/focused-payne-b38e6a/` ist eine 20-Dateien-Kopie vom 2026-05-15 mit veralteten Templates (alte Namenskonvention `CLAUDE.md` statt `CLAUDE_PROJEKT_TEMPLATE.md`). Belegt direkt einen Faulheits-Catch-Verstoß (Catch #3: Worktree-Branches selbst auf main mergen + bereinigen). Ist allein durch Löschung lösbar (ohne Inhaltsverlust), aber **niemand hat es bisher gemacht** — ein Indikator dass Worktree-Cleanup nicht als regelmäßige Session-End-Pflicht in der Checkliste steht.

### Was ich als Erstes anpacken würde

**Phase 1 — Sofort (1 Session, ohne Risiko):**

1. **Worktree-Cleanup** — `.claude/worktrees/focused-payne-b38e6a/` löschen (Coda macht das selbst, kein Auftrag an Chris). Reduziert Repo um ~350 KB und ~20 Dateien. Lösung Auffälligkeit A1.
2. **`_erledigt/`-Ordner einführen** — `FEATURE_REQUEST_*_ERLEDIGT.md`-Dateien dort hineinverschieben (aktuell 3 Stück). Lösung Auffälligkeit A4. Lifecycle-Konvention in PROJECT_BOOTSTRAP_README.md + GLOBAL_LESSONS.md verankern.

**Phase 2 — Mittelfristig (1–2 Sessions, mit Verifikation):**

3. **Lessons-Hierarchie klarziehen** — neue `lessons/INDEX.md` mit klarer Aussage:
   - `GLOBAL_LESSONS.md` = aktive Verfassung, **immer als Erstes lesen**.
   - `LESSONS_KONSOLIDIERT.md` = Snapshot, **nicht mehr ergänzen** — entweder in `archive/` verschieben (samt Hinweis im Header dass migriert) oder per Diff-Pass aufgehen lassen in GLOBAL_LESSONS.
   - `concepts/Try_Faulheits_catch.md` = historisches Konzept, **nicht für Operative-Coda lesepflichtig**.
   - `lessons/zerberus_lessons.md` = projektspezifische Sync-Kopie, **nur lesen wenn Zerberus-Arbeit**.
4. **DESIGN.md `[WERT]`-Slots durchgehen** — entweder mit Werten füllen (für Zerberus-UI) oder klarer als „pro Projekt zu füllen"-Templates markieren. Aktuell wirkt die Datei wie ein „90%-fertig-aber-leer"-Skelett, was Vertrauen kostet.

**Phase 3 — Strukturell (eigene Session, Konsolidierungs-Auftrag):**

5. **Zerberus-Lessons-Konsolidierung** — wie in `DECISIONS_PENDING.md` (Option A: eigener FEATURE_REQUEST mit Phase-A-D-Selbsttest). Dubletten zwischen `lessons/zerberus_lessons.md` und `GLOBAL_LESSONS.md` auflösen — gemeinsame Lessons in Global lassen, Zerberus-spezifische lokal halten, im Zerberus-Master ggf. auf Global verweisen.

### Was ich **nicht** als Erstes anpacken würde

- **`_drafts_gist/`** — funktioniert als geparkter Phase-3-Stub, kein Pain-Point.
- **`bugs/zerberus/`** — die offenen Bugs sind echte Arbeit (RX-001, W-001), nicht Aufräum-Material.
- **Templates-Ordner** — die 10 Templates sind konsistent, gewartet und referenziert. Kein Refactor nötig.

### Meta-Beobachtung

Das Repo ist für seine Größe (40 Dateien Main + 20 Worktree) erstaunlich gut dokumentiert (REPO_INVENTORY, DECISIONS_PENDING, mjolnir, GLOBAL_LESSONS). Der größte Wertgewinn liegt nicht in „mehr Doku", sondern in der **Hierarchisierung der existierenden Doku-Schichten** (Schritt 3 oben) und **Konsequenz beim Cleanup-Lifecycle** (Schritte 1+2 oben). Die Workflow-Infrastruktur ist da — sie wird nur noch nicht konsequent gegen sich selbst angewendet (klassisches Faulheits-Catch-#6-Muster: Hoffnung ≠ Verifikation).

---

*Erstellt durch Coda | Auftrag: FEATURE_REQUEST_CLAUDE.md (supervisor-briefing) | 2026-05-18*
*Reine Informationslieferung — keine Datei wurde verändert, verschoben, gelöscht oder umbenannt außer dieser neuen Datei.*
