# REPO_INDEX — Bmad82/Claude

<!-- AUTO-GENERATED — Wird von Claude Code bei Verzeichnisänderungen aktualisiert -->
<!-- Letzte Aktualisierung: 2026-06-19 -->
<!-- Generator: Claude Code Session — ordner-cleanup -->
<!-- HINWEIS: Vollständig re-synct im Zuge von ordner-cleanup (2026-06-19). Drift seit 2026-05-18 behoben. -->

Diese Datei wird von Coda bei Verzeichnisänderungen (Erstellen/Löschen/Verschieben/Umbenennen von Dateien) am Session-Ende aktualisiert. Der Supervisor (Chat-Instanz) fetcht sie via Raw-Link und leitet daraus Raw-Links für alle anderen Dateien ab — kein manuelles Link-Relaying durch Chris.

**Repo-Basis-URL (Raw):** `https://raw.githubusercontent.com/Bmad82/Claude/main/`

**Gist-Brücke:** Für Supervisor-Instanzen, die GitHub-Raw-Links nicht fetchen können, existiert ein paralleles Gist-System. Siehe [`GIST_LINK.md`](GIST_LINK.md) für URLs.

> **Struktur-Update 2026-06-19 (ordner-cleanup):** Schaltplan-Ablage `schaltplan/` neu; Einmal-Reports + veraltete Zwillinge nach `_archive/`; `_drafts_gist/` aufgelöst (Inhalt → `_archive/`); Konzept-/Strategie-Files nach `concepts/`; Übergabe-Template nach `templates/`. Details: [`INVENTORY.md`](INVENTORY.md).

---

## Verzeichnisbaum

```
.
├── .gitignore
├── DECISIONS_PENDING.md
├── DESIGN.md
├── DESIGN_KINTSUGI.md
├── GIST_LINK.md
├── GLOBAL_LESSONS.md
├── INVENTORY.md
├── PROJECT_BOOTSTRAP_README.md
├── Projektanfrage.html
├── README.md
├── REPO_INDEX.md
├── SUPERVISOR_KODEX.md
├── mjolnir.md
├── schaltplan/                (Steuer-/Plan-Files — Fabrik-Meta-Workflow)
│   ├── fabrik_meta_workflow.json   (SSOT)
│   └── fabrik_meta_workflow.html   (Render, zieht JSON live)
├── templates/
│   ├── CLAUDE_PROJEKT_TEMPLATE.md
│   ├── DECISIONS_TEMPLATE.md
│   ├── DESIGN_PROJEKT_TEMPLATE.md
│   ├── FEATURE_REQUEST_TEMPLATE.md
│   ├── HANDOVER_TEMPLATE.md
│   ├── MARATHON_WORKFLOW_TEMPLATE.md
│   ├── ROADMAP_TEMPLATE.md
│   ├── SUPERVISOR_PROJEKT_TEMPLATE.md
│   ├── lessons_TEMPLATE.md
│   ├── mjolnir_TEMPLATE.md
│   └── uebergabe_template_v1_0.md  (Conversation-Handover-Schema)
├── lessons/
│   ├── INDEX.md
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
├── workflow/
│   ├── MARATHON_WORKFLOW.md
│   ├── WORKFLOW_SUMMARY.md         (Live-Datei im Claude-KB-Gist)
│   └── gist_publisher.py
├── concepts/
│   ├── Try_Faulheits_catch.md
│   ├── ORCHESTRATOR_KONZEPT_v2.md
│   └── TOKEN_OPT_RULES.md
├── bugs/
│   ├── README.md
│   └── zerberus/
│       ├── regex.md
│       └── whisper.md
├── _erledigt/                 (FEATURE_REQUEST-Audit-Log, akkumuliert)
│   ├── FEATURE_REQUEST_CLAUDE_ERLEDIGT.md
│   ├── FEATURE_REQUEST_CLAUDE_mw-v2b-durchsetzung_ERLEDIGT.md
│   ├── FEATURE_REQUEST_CLAUDE_orchestrator-konsolidierung_ERLEDIGT.md
│   ├── FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md
│   ├── FEATURE_REQUEST_gist-infrastruktur_ERLEDIGT.md
│   ├── FEATURE_REQUEST_git-push-diagnose_ERLEDIGT.md
│   ├── FEATURE_REQUEST_mw-v2a-kontextentlastung_ERLEDIGT.md
│   ├── FEATURE_REQUEST_ordner-cleanup_ERLEDIGT.md
│   ├── FEATURE_REQUEST_repo-inventur_ERLEDIGT.md
│   ├── FEATURE_REQUEST_repo-restrukturierung_ERLEDIGT.md
│   └── FEATURE_REQUEST_supervisor-briefing_ERLEDIGT.md
└── _archive/                  (Einmal-Reports + abgelöste/veraltete Dateien, Audit, nicht live)
    ├── README.md
    ├── GIT_DIAGNOSE.md
    ├── GLOBAL_LESSONS_KONTEXT.md
    ├── INDEX_GIST_DRAFT.md
    ├── LESSONS_KONSOLIDIERT.md
    ├── REPO_INVENTORY.md
    ├── SUPERVISOR_BRIEFING.md
    └── ZERBERUS_GIST_DRAFT.md
```

> **Nicht im Tree (transient):** `FEATURE_REQUEST_supervisor-aufbau.md` liegt untracked im Root — separater, noch nicht gestarteter Auftrag. Wird beim Start dieses Auftrags getrackt.

---

## Dateien mit Raw-Links

### Root

| Pfad | Raw-Link | Typ | Beschreibung |
|------|----------|-----|-------------|
| README.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/README.md) | md | Repo-Einstiegsseite, Drei-Rollen-Modell, Ordnerstruktur |
| REPO_INDEX.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/REPO_INDEX.md) | md | Diese Datei — Navigations-Einstieg für Supervisor |
| INVENTORY.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/INVENTORY.md) | md | Bestandsaufnahme + Mapping (Phase 1 ordner-cleanup) |
| DESIGN.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/DESIGN.md) | md | Globale UI-Layer-Referenz (Farben, Typo, Komponenten) — Platzhalter-Schema |
| DESIGN_KINTSUGI.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/DESIGN_KINTSUGI.md) | md | Befülltes Kintsugi-Designsystem (Farbtokens mit Hex) |
| Projektanfrage.html | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/Projektanfrage.html) | html | Intake-Formular (Pipeline-Einstieg, Kintsugi-Optik) |
| GLOBAL_LESSONS.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/GLOBAL_LESSONS.md) | md | 6 Faulheits-Catches, Selbsttest-Pattern, Bibel-Format, mw-v2a/v2b, Billing/Cost-Guard |
| SUPERVISOR_KODEX.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/SUPERVISOR_KODEX.md) | md | NIE/IMMER-Listen für Chat-Supervisor (Rolle Supervisor) |
| PROJECT_BOOTSTRAP_README.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/PROJECT_BOOTSTRAP_README.md) | md | Anleitung: frische Coda-Session setzt neues Projekt auf |
| DECISIONS_PENDING.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/DECISIONS_PENDING.md) | md | Offene Meta-Layer-Architektur-Fragen + getroffene Entscheidungen |
| GIST_LINK.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/GIST_LINK.md) | md | Gist-Brücke: Index-Gist + Claude-KB-Gist URLs |
| mjolnir.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/mjolnir.md) | md | Session-Abschluss-State (Single-Slot), STATUS-Header |
| .gitignore | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/.gitignore) | config | Git-Ignore-Regeln |

### `schaltplan/`

| Pfad | Raw-Link | Typ | Beschreibung |
|------|----------|-----|-------------|
| schaltplan/fabrik_meta_workflow.json | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/schaltplan/fabrik_meta_workflow.json) | json | **Steuer-File (SSOT).** Fabrik-Meta-Workflow: Stages, Nodes (IST/TEIL/PLAN), Edges, Fractures, Pflege-Protokoll |
| schaltplan/fabrik_meta_workflow.html | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/schaltplan/fabrik_meta_workflow.html) | html | Gerenderte Schaltplan-Ansicht (lädt die JSON live per relativem fetch) |

### `templates/`

| Pfad | Raw-Link | Typ | Beschreibung |
|------|----------|-----|-------------|
| templates/CLAUDE_PROJEKT_TEMPLATE.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/templates/CLAUDE_PROJEKT_TEMPLATE.md) | template | Vorlage für CLAUDE_{PROJEKT}.md |
| templates/SUPERVISOR_PROJEKT_TEMPLATE.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/templates/SUPERVISOR_PROJEKT_TEMPLATE.md) | template | Vorlage für SUPERVISOR_{PROJEKT}.md |
| templates/MARATHON_WORKFLOW_TEMPLATE.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/templates/MARATHON_WORKFLOW_TEMPLATE.md) | template | Vorlage für MARATHON_WORKFLOW_{PROJEKT}.md |
| templates/mjolnir_TEMPLATE.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/templates/mjolnir_TEMPLATE.md) | template | Vorlage für mjolnir.md (Session-Abschluss) |
| templates/FEATURE_REQUEST_TEMPLATE.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/templates/FEATURE_REQUEST_TEMPLATE.md) | template | Vorlage für FEATURE_REQUEST_{kurzname}.md |
| templates/HANDOVER_TEMPLATE.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/templates/HANDOVER_TEMPLATE.md) | template | Vorlage für HANDOVER_{PROJEKT}.md (Session-Handover) |
| templates/uebergabe_template_v1_0.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/templates/uebergabe_template_v1_0.md) | template | Conversation-Handover-Schema (Chat→Chat, JSON), ergänzt HANDOVER/mjolnir |
| templates/lessons_TEMPLATE.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/templates/lessons_TEMPLATE.md) | template | Vorlage für lessons_{PROJEKT}.md |
| templates/DECISIONS_TEMPLATE.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/templates/DECISIONS_TEMPLATE.md) | template | Vorlage für DECISIONS_{PROJEKT}.md |
| templates/DESIGN_PROJEKT_TEMPLATE.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/templates/DESIGN_PROJEKT_TEMPLATE.md) | template | Vorlage für DESIGN_{PROJEKT}.md (projektspezifisch) |
| templates/ROADMAP_TEMPLATE.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/templates/ROADMAP_TEMPLATE.md) | template | Vorlage für ROADMAP_{PROJEKT}.md |

### `lessons/`

| Pfad | Raw-Link | Typ | Beschreibung |
|------|----------|-----|-------------|
| lessons/INDEX.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/INDEX.md) | md | Lessons-Hierarchie: 3 Ebenen (Workflow, Technologie, Projekt) |
| lessons/README.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/README.md) | md | Lessons-Format-Regeln |
| lessons/documentation.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/documentation.md) | md | Lessons: Schulungsunterlagen, Shop-Floor |
| lessons/frontend-js.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/frontend-js.md) | md | Lessons: Frontend, JavaScript |
| lessons/git-deployment.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/git-deployment.md) | md | Lessons: Git, Deployment, Aktivierungspfade |
| lessons/gpu-ml.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/gpu-ml.md) | md | Lessons: GPU/ML, VRAM-Fallback |
| lessons/json-data.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/json-data.md) | md | Lessons: JSON, typographische Anführungszeichen |
| lessons/mobile-touch.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/mobile-touch.md) | md | Lessons: Mobile, Touch, :hover vs :active |
| lessons/python-fastapi.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/python-fastapi.md) | md | Lessons: Python, FastAPI, Uvicorn |
| lessons/sqlite-db.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/sqlite-db.md) | md | Lessons: SQLite, idempotente Migrationen |
| lessons/testing.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/testing.md) | md | Lessons: Testing, Playwright, pytest |
| lessons/whisper-transcription.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/whisper-transcription.md) | md | Lessons: Whisper, Spracheingabe |
| lessons/workflow.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/workflow.md) | md | Lessons: Claude-CLI-Workflow, YOLO-Modus |
| lessons/zerberus_lessons.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/lessons/zerberus_lessons.md) | md | Sync-Kopie der Zerberus-Lessons (Master: Zerberus-Repo, ~386 KB) |

### `workflow/`

| Pfad | Raw-Link | Typ | Beschreibung |
|------|----------|-----|-------------|
| workflow/MARATHON_WORKFLOW.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/workflow/MARATHON_WORKFLOW.md) | md | Marathon-Workflow-Beschreibung: 3 Rollen, Datei-Hierarchie, Session-Zyklus, Catches |
| workflow/WORKFLOW_SUMMARY.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/workflow/WORKFLOW_SUMMARY.md) | md | Kompakte Workflow-Zusammenfassung (Live-Datei im Claude-KB-Gist) |
| workflow/gist_publisher.py | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/workflow/gist_publisher.py) | py | Helfer-Skript: GitHub-Gist erstellen/updaten via REST-API |

### `concepts/`

| Pfad | Raw-Link | Typ | Beschreibung |
|------|----------|-----|-------------|
| concepts/Try_Faulheits_catch.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/concepts/Try_Faulheits_catch.md) | md | Historischer Ursprung der 6 Faulheits-Catches |
| concepts/ORCHESTRATOR_KONZEPT_v2.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/concepts/ORCHESTRATOR_KONZEPT_v2.md) | md | Strategie: Hybrid-Modell DeepSeek baut / Claude prüft (Billing-Split) |
| concepts/TOKEN_OPT_RULES.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/concepts/TOKEN_OPT_RULES.md) | md | Token-sparsame Ausgabe-Stilstufen (Referenzblatt) |

### `bugs/`

| Pfad | Raw-Link | Typ | Beschreibung |
|------|----------|-----|-------------|
| bugs/README.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/bugs/README.md) | md | Scope-Erklärung: pro Projekt ein Unterordner |
| bugs/zerberus/regex.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/bugs/zerberus/regex.md) | md | Zerberus: Regex/Pattern-Bugs |
| bugs/zerberus/whisper.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/bugs/zerberus/whisper.md) | md | Zerberus: Whisper/Voice-Bugs |

### `_erledigt/` (FEATURE_REQUEST-Audit-Log)

| Pfad | Raw-Link | Typ | Beschreibung |
|------|----------|-----|-------------|
| _erledigt/FEATURE_REQUEST_CLAUDE_ERLEDIGT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_erledigt/FEATURE_REQUEST_CLAUDE_ERLEDIGT.md) | md | Audit: faulheits-catch-integration |
| _erledigt/FEATURE_REQUEST_mw-v2a-kontextentlastung_ERLEDIGT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_erledigt/FEATURE_REQUEST_mw-v2a-kontextentlastung_ERLEDIGT.md) | md | Audit: mw-v2a-kontextentlastung (war fälschlich im Root als FEATURE_REQUEST_CLAUDE_ERLEDIGT, kollisions-umbenannt) |
| _erledigt/FEATURE_REQUEST_CLAUDE_mw-v2b-durchsetzung_ERLEDIGT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_erledigt/FEATURE_REQUEST_CLAUDE_mw-v2b-durchsetzung_ERLEDIGT.md) | md | Audit: mw-v2b-durchsetzung |
| _erledigt/FEATURE_REQUEST_CLAUDE_orchestrator-konsolidierung_ERLEDIGT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_erledigt/FEATURE_REQUEST_CLAUDE_orchestrator-konsolidierung_ERLEDIGT.md) | md | Audit: orchestrator-konsolidierung |
| _erledigt/FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_erledigt/FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md) | md | Audit: aufraeumarbeiten-post-catch |
| _erledigt/FEATURE_REQUEST_gist-infrastruktur_ERLEDIGT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_erledigt/FEATURE_REQUEST_gist-infrastruktur_ERLEDIGT.md) | md | Audit: gist-infrastruktur |
| _erledigt/FEATURE_REQUEST_git-push-diagnose_ERLEDIGT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_erledigt/FEATURE_REQUEST_git-push-diagnose_ERLEDIGT.md) | md | Audit: git-push-diagnose |
| _erledigt/FEATURE_REQUEST_ordner-cleanup_ERLEDIGT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_erledigt/FEATURE_REQUEST_ordner-cleanup_ERLEDIGT.md) | md | Audit: ordner-cleanup (dieser Auftrag) |
| _erledigt/FEATURE_REQUEST_repo-inventur_ERLEDIGT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_erledigt/FEATURE_REQUEST_repo-inventur_ERLEDIGT.md) | md | Audit: repo-inventur |
| _erledigt/FEATURE_REQUEST_repo-restrukturierung_ERLEDIGT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_erledigt/FEATURE_REQUEST_repo-restrukturierung_ERLEDIGT.md) | md | Audit: repo-restrukturierung |
| _erledigt/FEATURE_REQUEST_supervisor-briefing_ERLEDIGT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_erledigt/FEATURE_REQUEST_supervisor-briefing_ERLEDIGT.md) | md | Audit: supervisor-briefing |

### `_archive/` (abgelöste/veraltete Dateien — Audit, nicht live)

| Pfad | Raw-Link | Typ | Beschreibung |
|------|----------|-----|-------------|
| _archive/README.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_archive/README.md) | md | Erklärt Zweck des Archivs + warum jede Datei hier liegt |
| _archive/GLOBAL_LESSONS_KONTEXT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_archive/GLOBAL_LESSONS_KONTEXT.md) | md | Veralteter, prosareicher Zwilling — Prosa in GLOBAL_LESSONS zurückgemergt (2026-06-19) |
| _archive/LESSONS_KONSOLIDIERT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_archive/LESSONS_KONSOLIDIERT.md) | md | P49-Lessons-Snapshot (2026-05-15), Unique-Items-Extraktion offen (DECISIONS_PENDING) |
| _archive/REPO_INVENTORY.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_archive/REPO_INVENTORY.md) | md | Einmal-Bestandsaufnahme (2026-05-18) — von REPO_INDEX abgelöst |
| _archive/SUPERVISOR_BRIEFING.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_archive/SUPERVISOR_BRIEFING.md) | md | Einmal-Briefing (2026-05-18) — Auftrag erledigt |
| _archive/GIT_DIAGNOSE.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_archive/GIT_DIAGNOSE.md) | md | Einmal-Diagnose (2026-05-18) — abgeschlossen, Erkenntnis als Lesson |
| _archive/INDEX_GIST_DRAFT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_archive/INDEX_GIST_DRAFT.md) | md | Obsoleter Gist-Entwurf (Infra realisiert 2026-05-18) |
| _archive/ZERBERUS_GIST_DRAFT.md | [raw](https://raw.githubusercontent.com/Bmad82/Claude/main/_archive/ZERBERUS_GIST_DRAFT.md) | md | Obsoleter Gist-Entwurf (Infra realisiert 2026-05-18) |

---

## Statistik

- Dateien gesamt (ohne `.git/`, ohne untracked `FEATURE_REQUEST_supervisor-aufbau.md`): 64
- Neue Ordner ggü. 2026-05-24: `schaltplan/`, `_archive/`; entfernt: `_drafts_gist/` (Inhalt → `_archive/` bzw. `workflow/`)
- Letzte strukturelle Änderung: 2026-06-19 (ordner-cleanup — Root entrümpelt, Schaltplan-Ablage, Archive konsolidiert, GLOBAL_LESSONS-Zwilling gemergt)
- Letzter Generator-Lauf: 2026-06-19

## Aktualisierungs-Regel

Diese Datei wird VOR dem finalen Push aktualisiert, wenn in der Session Verzeichnisänderungen (Dateien erstellt/gelöscht/verschoben/umbenannt) stattfanden. Bei reinen Inhalts-Änderungen (kein File-Move): nicht anfassen, kein Diff-Noise.
