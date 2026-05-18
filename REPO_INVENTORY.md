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
