# INVENTORY.md — Bestandsaufnahme `C:\Users\chris\Python\Claude\`

**Erstellt:** 2026-06-19
**Phase:** 1 — REINE ANALYSE. Nichts verschoben, geändert oder gelöscht.
**Methode:** Rekursives Listing (ohne `.git/`) + Inhalts-Sichtung jeder Datei (große Files angelesen, JSON-Steuer-Files komplett).
**Scope:** Nur der lokale Ordner. Kein Git-Repo-Inhalt, keine Gists, keine History herangezogen.

> **Pfad-Hinweis:** Der Auftrag enthielt den Platzhalter `[PFAD EINSETZEN]`. Verwendet wurde das Arbeitsverzeichnis `C:\Users\chris\Python\Claude\`, das die im Kontext genannten Files (Fabrik-Schaltplan, Übergabe-Template, Workflow) enthält. Falls ein anderer Ordner gemeint war: sagen, dann neu.

---

## 0. Kennzahlen

- **65 Dateien** (+ `.gitignore`), davon **1 Build-Artefakt** (`.pyc`) und **1 echte Steuer-JSON**.
- Vorhandene Kern-Ordner: `templates/` (11), `lessons/` (14), `workflow/` (3 inkl. `.pyc`), `bugs/` (3), `concepts/` (1), `_erledigt/` (7), `_drafts_gist/` (3).
- **22 lose Dateien im Root** — der Hauptgrund für die Unübersichtlichkeit.
- Kategorien-Verteilung grob: Template 11 · Lesson 16 · Workflow 4 · Schaltplan 2 · Concept 6 · Bug 3 · Erledigt 13 · Draft 3 · Müll-Verdacht 1.

**Kategorie-Legende:** Template · Lesson · Workflow · Schaltplan · Concept · Bug · Erledigt · Draft · Müll-Verdacht
**Dup-Spalte:** ⊕ = inhaltliche Überlappung/Fast-Duplikat (Details in §2).

---

## 1. Datei-Inventar (gruppiert nach aktuellem Ort)

### 1.1 Root — Steuer-/Plan-Files (Schaltplan) ⚠️ Sonderkategorie

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [fabrik_meta_workflow.json](fabrik_meta_workflow.json) | **Echte Steuer-/Plan-JSON.** Master-Schaltplan der „Fabrik"-Pipeline: 7 Stages (Intake→Research→Bootstrap→Build→Review→Handover + quer-liegender Betrieb/KVP), Nodes mit IST/TEIL/PLAN-Status, Edges (flow/loopback/gate-pass/gate-fail), `fractures` (offene Bruchstellen mit Severity), `pflege_protokoll` (SSOT-Regeln). Steuert die „wie wird vorgegangen"-Sicht, nicht die Code-Karte. | **Schaltplan** | 15.3 KB | 2026-06-19 | | **Behalten** → eigene Ablage `schaltplan/`. SSOT, NICHT Müll. |
| [fabrik_meta_workflow.html](fabrik_meta_workflow.html) | Gerenderte, animierte Ansicht (Kintsugi-Optik) desselben Schaltplans. Laut JSON-Pflege-Protokoll: „HTML zieht den Stand beim Öffnen". Präsentations-Layer, kein eigener Datenstand. | **Schaltplan** | 48.9 KB | 2026-06-19 | ⊕ | **Behalten** mit der JSON zusammen. Prüfen ob HTML wirklich live aus JSON liest oder Werte duplal hält (dann Drift-Risiko). |

### 1.2 Root — Übergabe-/Token-Schemata

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [uebergabe_template_v1_0.md](uebergabe_template_v1_0.md) | **Template** für Conversation-Handover-JSONs (Chat→Chat-Fenster bei ~50% Kontext). Annotiertes JSON-Skeleton: `meta/register/wer_minimal/spine/fractures/ressourcen_referenzen/sensibel_nicht_aufgreifen/letzter_stand` + Generier-Disziplin. | **Template** | 6.4 KB | 2026-06-19 | ⊕ | **ANPASSEN + verschieben** → `templates/`. Verhältnis zu `HANDOVER_TEMPLATE.md` (Session-Handover) und `mjolnir_TEMPLATE.md` im Kopf klären (3 Handover-Arten). |
| [TOKEN_OPT_RULES.md](TOKEN_OPT_RULES.md) | Vier Stilstufen (ultra-knapp/knapp/kurz/prosaisch) für token-sparsame LLM-Ausgaben: Floskeln raus, Pipe-Format, max 3 Reasoning-Schritte, Abkürzungs-Dict. Reines Referenz-/Regelblatt. | **Concept** (Reference) | 3.1 KB | 2026-06-13 | | **Behalten**, verschieben → `concepts/` oder `reference/`. Steht thematisch nah am „Bibel-Format". |

### 1.3 Root — Governance / „Verfassung" (per Absolutpfad referenziert ⚠️)

> Diese Files werden in den Templates per **hartem Absolutpfad** `C:\Users\chris\Python\Claude\<datei>` referenziert. Verschieben bricht die Templates → entweder am Root lassen oder alle Referenzen mitziehen.

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [GLOBAL_LESSONS.md](GLOBAL_LESSONS.md) | **Operative** globale Lessons-Quelle: 6 Faulheits-Catches, Selbsttest-Pattern A–D, Bibel-Format-Cheat-Sheet, mw-v2a/v2b-Pakete, Billing-/Cost-Guard-Lessons (neueste: Cost Guard 2026-06-13). | **Lesson** | 15.9 KB | 2026-06-13 | ⊕ | **Behalten** (kanonisch). Root-pinned. |
| [GLOBAL_LESSONS_KONTEXT.md](GLOBAL_LESSONS_KONTEXT.md) | **Älterer, ausführlicherer Zwilling** von GLOBAL_LESSONS.md: gleiche Sektionen, aber mit „Lesson generalisierbar"-Prosa. **Fehlen** die 5 neuesten Lessons (Cost-Guard, --bare/OAuth, Billing-Split, Credits, Model-IDs). Nur in `mjolnir.md` + 1 historischem FR referenziert. | **Lesson** | 25.6 KB | 2026-05-21 | ⊕⊕ | **MERGEN dann archivieren/löschen.** Reichere Prosa in GLOBAL_LESSONS zurückführen, dann diese veraltete Kopie weg (sonst Zwei-Wahrheiten). Siehe §2-A. |
| [SUPERVISOR_KODEX.md](SUPERVISOR_KODEX.md) | NIE/IMMER-Listen für jede Chat-Supervisor-Instanz (projektübergreifend), Prompt-Skelett, Eskalations-Regel. | **Workflow** (Governance) | 6.6 KB | 2026-05-17 | | **Behalten**, root-pinned. |
| [DECISIONS_PENDING.md](DECISIONS_PENDING.md) | Meta-Layer-Entscheidungslog: 1 offene Frage (Zerberus-Lessons-Konsolidierung) + 7 getroffene Entscheidungen mit Datum/Begründung. | **Workflow** (Governance) | 9.4 KB | 2026-05-21 | | **Behalten**, root-pinned. |
| [PROJECT_BOOTSTRAP_README.md](PROJECT_BOOTSTRAP_README.md) | Schritt-für-Schritt-Anleitung für Coda, um ein frisches Marathon-Projekt aufzusetzen (Templates ziehen, Skelett, Gist anlegen, Walkthrough). | **Workflow** | 8.0 KB | 2026-05-18 | | **Behalten**, root-pinned. Entspricht genau dem „Bootstrap-LLM zieht Templates"-Schritt aus dem Kontext. |
| [GIST_LINK.md](GIST_LINK.md) | Kanonische Gist-URLs (Index-Gist, Claude-KB-Gist) + Raw-URLs + Wartungsregeln. Die „Gist-Brücke". | **Reference** | 1.5 KB | 2026-05-18 | | **Behalten**, root-pinned. |
| [README.md](README.md) | Repo-Einstieg: Drei-Rollen-Modell, Ordnerstruktur-Tabelle, Einbindung in Projekte, Naming-Konvention. | **Workflow** (Doc) | 4.1 KB | 2026-05-18 | | **Behalten** + ANPASSEN (Ordnerstruktur-Tabelle nach Umzug aktualisieren). |

### 1.4 Root — Design-/Intake-Assets

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [DESIGN.md](DESIGN.md) | Globale UI-Referenz (Farben, Typo, Komponenten, Mobile). **Werte sind großteils `[TODO: aus Projekt-:root]`-Platzhalter** — Gerüst, noch nicht befüllt. | **Concept** (Reference) | 35.5 KB | 2026-05-18 | ⊕ | **ANPASSEN/mergen.** Überlappt mit DESIGN_KINTSUGI (das echte Werte hat). Entweder DESIGN.md mit Kintsugi-Werten füllen oder als generisches Schema-Skelett kennzeichnen. → `design/`. |
| [DESIGN_KINTSUGI.md](DESIGN_KINTSUGI.md) | Konkretes, befülltes Designsystem „Kintsugi" (Farbtokens mit Hex, Status-Farben, Transparenz-Muster). Reproduktions-Referenz aus den Showcases. | **Concept** (Reference) | 17.9 KB | 2026-05-24 | ⊕ | **Behalten** → `design/`. Das ist die *gelebte* Design-Quelle (gleiche Tokens wie in den HTMLs). |
| [Projektanfrage.html](Projektanfrage.html) | Gestaltetes HTML-Formular „Projekt-Anfrage" (Kintsugi-Optik) — Intake-Artefakt, der Einstiegspunkt der Pipeline (`in.start` im Schaltplan, ref `Projektanfrage.html`). | **Workflow** (Asset) | 32.0 KB | 2026-05-18 | | **Behalten** → `intake/` oder `assets/`. Ist Teil des Workflows, kein Müll. |

### 1.5 Root — Konzept / Strategie

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [ORCHESTRATOR_KONZEPT_v2.md](ORCHESTRATOR_KONZEPT_v2.md) | Strategie-Konzept „nach dem 15.06.2026"-Billing: Hybrid-Modell DeepSeek baut / Claude prüft (Monokel-Review), drei Lösungswege, Begründung gegen `--bare`. | **Concept** | 16.9 KB | 2026-05-24 | | **Behalten** → `concepts/`. Lebendes Strategie-Dokument, speist den Schaltplan. |

### 1.6 Root — Einmalige historische Reports (erledigt)

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [REPO_INVENTORY.md](REPO_INVENTORY.md) | Einmal-Bestandsaufnahme vom 2026-05-18 (Tree inkl. damaligem ungenutztem Worktree). Heute veraltet, durch REPO_INDEX abgelöst. | **Erledigt** | 18.9 KB | 2026-05-18 | ⊕ | **Archivieren** → `_erledigt/` oder `_archiv/`. Historischer Snapshot. |
| [SUPERVISOR_BRIEFING.md](SUPERVISOR_BRIEFING.md) | Einmal-Infopaket (2026-05-18) für den Supervisor zur Repo-Restrukturierung — voller Tree + Datei-Beschreibungen. Auftrag längst erledigt. | **Erledigt** | 50.5 KB | 2026-05-18 | ⊕ | **Archivieren.** Größte Einzeldatei nach den Lessons; reiner Verlaufsballast. |
| [GIT_DIAGNOSE.md](GIT_DIAGNOSE.md) | Einmal-Diagnose (2026-05-18): „warum zeigt GitHub alten Stand" → Ergebnis: kein Git-Problem, CDN-Cache. Abgeschlossen. | **Erledigt** | 10.2 KB | 2026-05-18 | | **Archivieren** (oder löschen — Erkenntnis steht als Lesson in `lessons/git-deployment.md`). |
| [REPO_INDEX.md](REPO_INDEX.md) | Auto-gepflegter Verzeichnisbaum + Raw-Link-Tabelle für Supervisor-Navigation. **Selbst markiert: „Drift seit 2026-05-18"** — fehlen Kintsugi, Orchestrator-Konzept, fabrik_*, scripts/ u.a. | **Workflow** | 14.1 KB | 2026-05-24 | | **Behalten + ANPASSEN (dringend):** Re-Sync nach dem Aufräumen. Root-pinned (Raw-Link-Einstieg). |

### 1.7 Root — FEATURE_REQUEST-Archive (am falschen Ort)

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [FEATURE_REQUEST_CLAUDE_ERLEDIGT.md](FEATURE_REQUEST_CLAUDE_ERLEDIGT.md) | Erledigter Auftrag `mw-v2a-kontextentlastung` (Kontextentlastung, IFScale, Lessons-RAG). | **Erledigt** | 7.3 KB | 2026-05-21 | | **Verschieben** → `_erledigt/`. (Liegt fälschlich im Root.) |
| [FEATURE_REQUEST_CLAUDE_mw-v2b-durchsetzung_ERLEDIGT.md](FEATURE_REQUEST_CLAUDE_mw-v2b-durchsetzung_ERLEDIGT.md) | Erledigter Auftrag `mw-v2b-durchsetzung` (Hooks, Bibel-Schlankheitskur, Playbooks). | **Erledigt** | 10.9 KB | 2026-05-21 | | **Verschieben** → `_erledigt/`. |
| [FEATURE_REQUEST_CLAUDE_orchestrator-konsolidierung_ERLEDIGT.md](FEATURE_REQUEST_CLAUDE_orchestrator-konsolidierung_ERLEDIGT.md) | Erledigter Auftrag `orchestrator-konsolidierung` (4 neue Lessons, ORCHESTRATOR_KONZEPT-Korrektur). | **Erledigt** | 7.4 KB | 2026-05-24 | | **Verschieben** → `_erledigt/`. |

### 1.8 Root — Single-Slot-Status

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [mjolnir.md](mjolnir.md) | Single-Slot-Session-Status (STATUS=FERTIG, Auftrag orchestrator-konsolidierung). Letzter Stand des Meta-Repos selbst. | **Workflow** (State) | 4.9 KB | 2026-05-24 | | **Behalten** am Root (Konvention). Inhaltlich veraltet — wird ohnehin beim nächsten Lauf überschrieben. |

### 1.9 `templates/` — Bootstrap-Vorlagen (Kern-Bucket)

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [CLAUDE_PROJEKT_TEMPLATE.md](templates/CLAUDE_PROJEKT_TEMPLATE.md) | Betriebsanleitung-Vorlage für Coda (Regel 0, Session-Start-Pflicht, Doku-Pflicht, Git-/Gist-Workflow). | **Template** | 8.2 KB | 2026-05-24 | | **Behalten.** |
| [SUPERVISOR_PROJEKT_TEMPLATE.md](templates/SUPERVISOR_PROJEKT_TEMPLATE.md) | Strategie-Stand-Vorlage für Supervisor-Instanz (Rollen, Kontext-Mgmt, Bug-Tracker, Gist-Navigation). | **Template** | 5.3 KB | 2026-05-18 | | **Behalten.** |
| [MARATHON_WORKFLOW_TEMPLATE.md](templates/MARATHON_WORKFLOW_TEMPLATE.md) | Aufgabenlisten-Vorlage mit Status-Symbolen + Session-Zyklus + Auffüll-Regel. | **Template** | 3.4 KB | 2026-05-21 | ⊕ | **Behalten.** Auffüll-Regel-Block ist Wiederholung (s. §2-C). |
| [FEATURE_REQUEST_TEMPLATE.md](templates/FEATURE_REQUEST_TEMPLATE.md) | Auftrags-Vorlage (Header, Akzeptanzkriterien, Schritte, Selbsttest A–D, Lifecycle). | **Template** | 2.8 KB | 2026-05-17 | | **Behalten.** |
| [HANDOVER_TEMPLATE.md](templates/HANDOVER_TEMPLATE.md) | Session-Handover-Vorlage (Stand, offen, Bugs, Tests, nächster Patch). | **Template** | 1.1 KB | 2026-05-17 | ⊕ | **Behalten.** Abgrenzung zu `uebergabe_template_v1_0.md` dokumentieren. |
| [mjolnir_TEMPLATE.md](templates/mjolnir_TEMPLATE.md) | mjolnir.md-Vorlage (STATUS-Header, was-Chris-physisch-tun-muss, Lifecycle-Notiz). | **Template** | 1.8 KB | 2026-05-17 | | **Behalten.** |
| [DECISIONS_TEMPLATE.md](templates/DECISIONS_TEMPLATE.md) | Projekt-Entscheidungslog-Vorlage. | **Template** | 1.0 KB | 2026-05-17 | | **Behalten.** |
| [DESIGN_PROJEKT_TEMPLATE.md](templates/DESIGN_PROJEKT_TEMPLATE.md) | Projekt-Designdokument-Vorlage (Prosa, verweist auf globale DESIGN.md). | **Template** | 1.5 KB | 2026-05-17 | | **Behalten.** |
| [ROADMAP_TEMPLATE.md](templates/ROADMAP_TEMPLATE.md) | Roadmap-Vorlage (Vision-Horizont, nicht Patch-Tracker). | **Template** | 1.0 KB | 2026-05-17 | | **Behalten.** |
| [lessons_TEMPLATE.md](templates/lessons_TEMPLATE.md) | Projekt-Lessons-Vorlage (Bibel-Format, Lese-Reihenfolge, Promotion-Sektion). | **Template** | 1.3 KB | 2026-05-17 | | **Behalten.** |

### 1.10 `lessons/` — Technologie-Lessons (Kern-Bucket)

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [INDEX.md](lessons/INDEX.md) | Erklärt die 3-Ebenen-Lessons-Hierarchie (Workflow/Technologie/Projekt) + Konsultations-/Eintragungsregeln. | **Lesson** (Index) | 4.2 KB | 2026-05-18 | | **Behalten.** Gute Navigations-Datei. |
| [README.md](lessons/README.md) | Kurz-Intro zum Lessons-Ordner + Public-Repo-Warnung. | **Lesson** (Doc) | 0.6 KB | 2026-04-19 | ⊕ | **Mergen** in INDEX.md (Überschneidung) oder behalten. |
| [workflow.md](lessons/workflow.md) | Claude-CLI/Chat-Workflow-Lessons (Checkpoints, Supervisor/Executor-Trennung, PowerShell). | **Lesson** | 4.3 KB | 2026-05-16 | | **Behalten.** |
| [frontend-js.md](lessons/frontend-js.md) | Frontend/JS-Stolpersteine (Regex-Backrefs, Chart.js, SSE-Heartbeat, XSS-safe Decision-Buttons). | **Lesson** | 4.6 KB | 2026-04-23 | | **Behalten.** |
| [python-fastapi.md](lessons/python-fastapi.md) | FastAPI/Uvicorn-Lessons (--reload Windows, Async, FAISS-Soft-Delete, Config-SSOT). | **Lesson** | 2.8 KB | 2026-04-23 | | **Behalten.** |
| [gpu-ml.md](lessons/gpu-ml.md) | GPU/ML (Device-Detection, torch+CUDA-Index, VRAM-Budget). | **Lesson** | 3.0 KB | 2026-04-23 | | **Behalten.** |
| [documentation.md](lessons/documentation.md) | Shop-Floor-Doku + Projekt-Doku-Konvention (Suffix-Regeln, Bibel vs Prosa). | **Lesson** | 2.6 KB | 2026-05-15 | | **Behalten.** |
| [whisper-transcription.md](lessons/whisper-transcription.md) | Whisper-Handling (Chunk-Splitting, temperature=0, Dedup-Pipeline). | **Lesson** | 1.5 KB | 2026-04-23 | | **Behalten.** |
| [sqlite-db.md](lessons/sqlite-db.md) | SQLite/Migrationen (idempotent, Backup, Dedup-Insert-Guard). | **Lesson** | 1.5 KB | 2026-04-23 | | **Behalten.** |
| [testing.md](lessons/testing.md) | Playwright/pytest (HTTPS-Certs, pageerror-Listener, ausführen statt annehmen). | **Lesson** | 1.0 KB | 2026-04-23 | | **Behalten.** |
| [mobile-touch.md](lessons/mobile-touch.md) | Mobile/Touch (`:active`, 44px, dvh, Tailscale+HTTPS). | **Lesson** | 0.7 KB | 2026-04-19 | | **Behalten.** |
| [git-deployment.md](lessons/git-deployment.md) | Git/Deployment (start.bat-Activate, große Dateien, $LASTEXITCODE, CDN-Cache). | **Lesson** | 0.8 KB | 2026-04-23 | | **Behalten.** |
| [json-data.md](lessons/json-data.md) | JSON/Datenformate (typografische Quotes brechen Import, json.loads als Validierung). | **Lesson** | 0.4 KB | 2026-04-23 | | **Behalten.** |
| [zerberus_lessons.md](lessons/zerberus_lessons.md) | **Projektspezifische** Zerberus-Lessons (386 KB, Master liegt im Zerberus-Repo) — Sync-Kopie. Multi-Agent-Contract-First, RAG-Scoping, TTS-Strip u.v.m. | **Lesson** (Projekt-Sync) | 386.4 KB | 2026-06-18 | ⊕ | **ANPASSEN-Entscheidung offen** (siehe DECISIONS_PENDING): gehört laut eigener Regel ins Projekt-Repo, nicht hierher. Konsolidierung mit GLOBAL_LESSONS ausstehend. 90% des lessons/-Volumens. |

### 1.11 `workflow/` — Ablaufbeschreibung + Helfer (Kern-Bucket)

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [MARATHON_WORKFLOW.md](workflow/MARATHON_WORKFLOW.md) | Volltext-Architektur des Marathon-Workflows (3 Rollen, Datei-Hierarchie, Session-Zyklus, 6 Catches, Mjölnir-Round-Trip, Gist-Brücke). | **Workflow** | 8.8 KB | 2026-05-21 | ⊕ | **Behalten** (kanonische Ablaufbeschreibung). |
| [gist_publisher.py](workflow/gist_publisher.py) | Python-Helfer: PUBLIC-Gist erstellen/patchen via GitHub-REST, Token aus `git credential`. | **Workflow** (Tool) | 4.2 KB | 2026-05-21 | | **Behalten.** Einziges echtes Skript lokal. |
| workflow/__pycache__/gist_publisher.cpython-310.pyc | Kompiliertes Bytecode-Artefakt von `gist_publisher.py`. Regenerierbar, von `.gitignore` (`__pycache__/`) abgedeckt. | **Müll-Verdacht** | 2.9 KB | 2026-05-21 | | **Löschen.** Build-Artefakt, kein Quelltext. |

### 1.12 `concepts/` — historische Konzept-Ursprünge

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [Try_Faulheits_catch.md](concepts/Try_Faulheits_catch.md) | Rekonstruierter Konzept-Ursprung der 6 Faulheits-Catches + Selbsttest-Pattern + Bibel-Cheat-Sheet. Explizit als „historisch" markiert. | **Concept** | 5.0 KB | 2026-05-17 | ⊕ | **Behalten.** Bewusst archivierter Ursprung (siehe DECISIONS_PENDING). |

### 1.13 `bugs/` — Projekt-Bug-Tracker

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [README.md](bugs/README.md) | Struktur + Format-Konvention des Bug-Trackers (ein Unterordner pro Projekt, ID-Präfixe). | **Bug** (Doc) | 1.3 KB | 2026-05-18 | | **Behalten.** |
| [zerberus/regex.md](bugs/zerberus/regex.md) | 1 offener Regex-Bug (RX-001 ZDF-Halluzination). | **Bug** | 0.6 KB | 2026-04-19 | | **Behalten.** Prüfen ob inzwischen erledigt (Stand April). |
| [zerberus/whisper.md](bugs/zerberus/whisper.md) | 1 offener Whisper-Bug (W-001 Phrasen-Repetition) — wirkt durch spätere Dedup-Lessons evtl. bereits gelöst. | **Bug** | 1.1 KB | 2026-04-19 | ⊕ | **ANPASSEN:** gegen `lessons/whisper-transcription.md` (Zwei-Stufen-Dedup, P113b) prüfen — vermutlich nach „Erledigt" verschiebbar. |

### 1.14 `_erledigt/` — FEATURE_REQUEST-Archiv (Audit-Log)

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md](_erledigt/FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md) | Erledigter Aufräum-Auftrag (Templates-Konsolidierung, Naming, _drafts_gist). | **Erledigt** | 18.9 KB | 2026-05-17 | | **Behalten** (Audit). |
| [FEATURE_REQUEST_CLAUDE_ERLEDIGT.md](_erledigt/FEATURE_REQUEST_CLAUDE_ERLEDIGT.md) | Erledigter Auftrag `faulheits-catch-integration`. | **Erledigt** | 9.1 KB | 2026-05-17 | | **Behalten** (Audit). |
| [FEATURE_REQUEST_gist-infrastruktur_ERLEDIGT.md](_erledigt/FEATURE_REQUEST_gist-infrastruktur_ERLEDIGT.md) | Erledigter Auftrag: Gist-Brücke aufsetzen. | **Erledigt** | 7.5 KB | 2026-05-18 | | **Behalten** (Audit). |
| [FEATURE_REQUEST_git-push-diagnose_ERLEDIGT.md](_erledigt/FEATURE_REQUEST_git-push-diagnose_ERLEDIGT.md) | Erledigter Auftrag: Git-Push-Diagnose (Quelle von GIT_DIAGNOSE.md). | **Erledigt** | 1.3 KB | 2026-05-18 | ⊕ | **Behalten** (Audit). |
| [FEATURE_REQUEST_repo-inventur_ERLEDIGT.md](_erledigt/FEATURE_REQUEST_repo-inventur_ERLEDIGT.md) | Erledigter Auftrag: Repo-Inventur (Quelle von REPO_INVENTORY.md). | **Erledigt** | 2.0 KB | 2026-05-18 | ⊕ | **Behalten** (Audit). |
| [FEATURE_REQUEST_repo-restrukturierung_ERLEDIGT.md](_erledigt/FEATURE_REQUEST_repo-restrukturierung_ERLEDIGT.md) | Erledigter Auftrag: Repo-Restrukturierung + REPO_INDEX. | **Erledigt** | 8.3 KB | 2026-05-18 | | **Behalten** (Audit). |
| [FEATURE_REQUEST_supervisor-briefing_ERLEDIGT.md](_erledigt/FEATURE_REQUEST_supervisor-briefing_ERLEDIGT.md) | Erledigter Auftrag: Supervisor-Briefing (Quelle von SUPERVISOR_BRIEFING.md). | **Erledigt** | 3.2 KB | 2026-05-18 | ⊕ | **Behalten** (Audit). |

### 1.15 `_drafts_gist/` — Gist-Konzept-Entwürfe

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [WORKFLOW_SUMMARY.md](_drafts_gist/WORKFLOW_SUMMARY.md) | **Kompakte, aktuelle** Workflow-Zusammenfassung (3 Rollen, Session-Zyklus, 6 Catches, Progressive Disclosure, Hooks, Gist-Konvention). Ist laut GIST_LINK.md **Live-Datei im Claude-KB-Gist** — kein Draft. | **Workflow** | 5.5 KB | 2026-05-21 | ⊕ | **Falsch einsortiert.** Verschieben → `workflow/` oder eigenes `gist-staging/`. Aktiv genutzt, nicht „draft". |
| [INDEX_GIST_DRAFT.md](_drafts_gist/INDEX_GIST_DRAFT.md) | Konzept-Entwurf für Projekt-Index-Gist. Gist-Infra ist **bereits realisiert** (echte URLs in GIST_LINK.md). | **Draft** (obsolet) | 1.1 KB | 2026-05-17 | ⊕ | **Archivieren/löschen.** REPO_INDEX notiert selbst „Konzept realisiert 2026-05-18". |
| [ZERBERUS_GIST_DRAFT.md](_drafts_gist/ZERBERUS_GIST_DRAFT.md) | Konzept-Entwurf für Zerberus-Projekt-Gist (Platzhalter `P-???`/`TBD`). Überholt. | **Draft** (obsolet) | 0.9 KB | 2026-05-17 | ⊕ | **Archivieren/löschen.** |

### 1.16 Root — Infrastruktur

| Datei | Was tatsächlich drinsteht | Kat. | Größe | Geändert | Dup | Empfehlung |
|---|---|---|---|---|---|---|
| [.gitignore](.gitignore) | Ignoriert `.env`, `*.bak`, `__pycache__/`, `.cache/`, `*.exe`. | Infra | 0.1 KB | 2026-04-19 | | **Behalten.** Deckt das `.pyc` bereits ab (liegt nur lokal). |

---

## 2. Duplikate & Fast-Duplikate (explizit)

**A) `GLOBAL_LESSONS.md` ⟷ `GLOBAL_LESSONS_KONTEXT.md` — echtes Fast-Duplikat (höchste Priorität).**
Gleiche Lessons-Sektionen, aber KONTEXT ist ein **älterer Stand (2026-05-21)** mit reicherer „Lesson generalisierbar"-Prosa; es fehlen die 5 neuesten Lessons (Cost-Guard 06-13, --bare/OAuth, Billing-Split, Credits, Model-IDs). Zwei konkurrierende „globale Lessons"-Wahrheiten sind gefährlich — genau das Anti-Pattern, das der Workflow killen will. → Reiche Prosa zurück in GLOBAL_LESSONS mergen, KONTEXT dann entfernen.

**B) Repo-State-Snapshots — 3-fach überlappend.**
`REPO_INDEX.md` (auto, lebendig, aber gedriftet), `REPO_INVENTORY.md` (Einmal-Snapshot 05-18) und `SUPERVISOR_BRIEFING.md` (Einmal-Briefing 05-18, enthält denselben Tree). Die letzten zwei sind durch REPO_INDEX abgelöst → archivieren. Nur REPO_INDEX bleibt lebendig (braucht Re-Sync).

**C) „Session-Auffüll-Regel" — 5× verbatim.**
In `GLOBAL_LESSONS.md`, `GLOBAL_LESSONS_KONTEXT.md`, `LESSONS_KONSOLIDIERT.md`, `templates/MARATHON_WORKFLOW_TEMPLATE.md`, `workflow/MARATHON_WORKFLOW.md`. Template + Workflow-Wiederholung ist gewollt (verschiedene Layer); die Kopie in `LESSONS_KONSOLIDIERT.md` (oben drangeklatscht, eigentlich ein P49-Snapshot) ist Redundanz.

**D) „6 Faulheits-Catches / Quick Reference" — 5×.**
In `GLOBAL_LESSONS.md`, `GLOBAL_LESSONS_KONTEXT.md`, `workflow/MARATHON_WORKFLOW.md`, `_drafts_gist/WORKFLOW_SUMMARY.md`, `concepts/Try_Faulheits_catch.md`. Bewusste Mehrfach-Verankerung über Layer (kanonisch = GLOBAL_LESSONS); akzeptabel, aber Single-Source wäre sauberer.

**E) `LESSONS_KONSOLIDIERT.md` ⟷ `GLOBAL_LESSONS.md`.**
KONSOLIDIERT ist ein P49-Snapshot (2026-05-15) aus Supervisor-Chats mit **einigen unique alten Lessons** (PWA, CSS-Industriepanel, Claude-Design-Workflow), die nicht in GLOBAL_LESSONS stehen. DECISIONS_PENDING führt die Konsolidierung als offen. → Unique-Items extrahieren (ggf. nach `lessons/`), dann archivieren.

**F) Drei „Handover"-Schemata nebeneinander (konzeptuell verwandt, NICHT identisch — kein Löschkandidat, nur dokumentieren).**
`templates/mjolnir_TEMPLATE.md` (Single-Slot-Status), `templates/HANDOVER_TEMPLATE.md` (Detail-Session-Handover, Bibel-MD), `uebergabe_template_v1_0.md` (Conversation/Chat-Fenster-Handover, JSON). Verhältnis in einem kurzen Kopf-Block klären, damit niemand sie verwechselt.

**G) `fabrik_meta_workflow.json` ⟷ `.html`.**
Kein Fehler — die HTML ist die Visualisierung. Risiko nur, falls die HTML Werte hartkodiert statt aus der JSON zu lesen (Drift). Beim Aufräumen verifizieren.

**H) `DESIGN.md` ⟷ `DESIGN_KINTSUGI.md`.**
DESIGN.md ist ein Platzhalter-Gerüst (`[TODO]`), DESIGN_KINTSUGI.md die befüllte Realität. Entweder zusammenführen oder DESIGN.md klar als „generisches Schema, Werte projektweise" kennzeichnen.

---

## 3. Vorschlag Zielstruktur + Mapping

Kern laut Auftrag: **`templates/` · `lessons/` · `workflow/` + eigene Schaltplan-Ablage.** Drumherum so wenig wie möglich. Vorschlag:

```
Claude/
├── README.md                      ← Einstieg (Ordnerstruktur-Tabelle nachziehen)
├── REPO_INDEX.md                  ← auto, root-pinned (Re-Sync nötig)
├── mjolnir.md                     ← Single-Slot, root-pinned
├── .gitignore
│
├── governance/   (NEU, optional)  ← die „Verfassung" — ⚠️ nur mit Referenz-Update verschiebbar
│   ├── GLOBAL_LESSONS.md
│   ├── SUPERVISOR_KODEX.md
│   ├── DECISIONS_PENDING.md
│   ├── PROJECT_BOOTSTRAP_README.md
│   └── GIST_LINK.md
│       (Alternativ: am Root lassen, weil per Absolutpfad in Templates verdrahtet.)
│
├── templates/                     ← KERN (unverändert) + uebergabe_template_v1_0.md rein
├── lessons/                       ← KERN (unverändert; zerberus_lessons.md-Frage offen)
├── workflow/                      ← KERN: MARATHON_WORKFLOW.md, gist_publisher.py, WORKFLOW_SUMMARY.md
│
├── schaltplan/   (NEU)            ← Steuer-Files
│   ├── fabrik_meta_workflow.json  (SSOT)
│   └── fabrik_meta_workflow.html  (Render)
│
├── intake/       (NEU, optional)  ← Projektanfrage.html
├── design/       (NEU, optional)  ← DESIGN.md, DESIGN_KINTSUGI.md
├── concepts/                      ← Try_Faulheits_catch.md, ORCHESTRATOR_KONZEPT_v2.md, TOKEN_OPT_RULES.md
├── bugs/                          ← unverändert
│
├── _erledigt/                     ← FR-Archiv + die 3 Root-FR-Archive rein
└── _archiv/      (NEU)            ← REPO_INVENTORY.md, SUPERVISOR_BRIEFING.md, GIT_DIAGNOSE.md,
                                      GLOBAL_LESSONS_KONTEXT.md, LESSONS_KONSOLIDIERT.md,
                                      _drafts_gist/* (obsolete Drafts)
```

**Mapping-Tabelle (jede nicht-am-Platz-Datei):**

| Datei | → Ziel | Aktion |
|---|---|---|
| fabrik_meta_workflow.json / .html | `schaltplan/` | verschieben |
| uebergabe_template_v1_0.md | `templates/` | verschieben + Kopf-Abgrenzung |
| Projektanfrage.html | `intake/` (oder `assets/`) | verschieben |
| DESIGN.md, DESIGN_KINTSUGI.md | `design/` | verschieben + mergen-Prüfung |
| ORCHESTRATOR_KONZEPT_v2.md, TOKEN_OPT_RULES.md | `concepts/` | verschieben |
| FEATURE_REQUEST_CLAUDE_ERLEDIGT.md (Root) | `_erledigt/` | verschieben |
| FEATURE_REQUEST_CLAUDE_mw-v2b-durchsetzung_ERLEDIGT.md | `_erledigt/` | verschieben |
| FEATURE_REQUEST_CLAUDE_orchestrator-konsolidierung_ERLEDIGT.md | `_erledigt/` | verschieben |
| REPO_INVENTORY.md, SUPERVISOR_BRIEFING.md, GIT_DIAGNOSE.md | `_archiv/` | archivieren |
| GLOBAL_LESSONS_KONTEXT.md | `_archiv/` | mergen → dann archivieren |
| LESSONS_KONSOLIDIERT.md | `_archiv/` | unique-Items extrahieren → archivieren |
| _drafts_gist/WORKFLOW_SUMMARY.md | `workflow/` | verschieben (ist live) |
| _drafts_gist/INDEX_GIST_DRAFT.md, ZERBERUS_GIST_DRAFT.md | `_archiv/` | archivieren/löschen |
| workflow/__pycache__/*.pyc | — | löschen |
| GLOBAL_LESSONS / SUPERVISOR_KODEX / DECISIONS_PENDING / PROJECT_BOOTSTRAP_README / GIST_LINK | `governance/` **oder** Root | nur mit Template-Referenz-Update verschieben |

> **Wichtigste Nebenbedingung:** Templates referenzieren `GLOBAL_LESSONS.md`, `SUPERVISOR_KODEX.md`, `PROJECT_BOOTSTRAP_README.md`, `DECISIONS_PENDING.md`, `GIST_LINK.md`, `templates/`, `workflow/gist_publisher.py` per **hartem Absolutpfad** `C:\Users\chris\Python\Claude\...`. Jede dieser Dateien zu verschieben heißt: **alle Templates + REPO_INDEX + Gist-Inhalte mitziehen.** Im Zweifel diese 5 am Root lassen (Aufwand/Risiko > Nutzen) und nur den unstrittigen Rest umräumen.

---

## 4. Pro-Datei-Empfehlung — Kurzfassung

- **Behalten unverändert:** alle `templates/*` (10), alle `lessons/*` außer zerberus_lessons (Frage offen), `workflow/MARATHON_WORKFLOW.md`, `workflow/gist_publisher.py`, `bugs/*` (whisper.md prüfen), `concepts/Try_Faulheits_catch.md`, `_erledigt/*` (7), `SUPERVISOR_KODEX.md`, `DECISIONS_PENDING.md`, `PROJECT_BOOTSTRAP_README.md`, `GIST_LINK.md`, `mjolnir.md`, `.gitignore`, `fabrik_meta_workflow.json/.html`.
- **ANPASSEN:** `README.md` (Struktur-Tabelle nach Umzug), `REPO_INDEX.md` (Re-Sync, Drift seit 05-18), `DESIGN.md` (Platzhalter füllen oder als Schema kennzeichnen), `uebergabe_template_v1_0.md` (Abgrenzung zu HANDOVER/mjolnir), `bugs/zerberus/whisper.md` (vermutlich → Erledigt), `GLOBAL_LESSONS.md` (reiche Prosa aus KONTEXT zurückholen).
- **Mergen:** `GLOBAL_LESSONS_KONTEXT.md` → in GLOBAL_LESSONS; `LESSONS_KONSOLIDIERT.md` → unique-Items in `lessons/`; `lessons/README.md` ggf. in INDEX.md.
- **Verschieben (nur Ortswechsel):** 3 Root-FR-Archive → `_erledigt/`; `WORKFLOW_SUMMARY.md` raus aus `_drafts_gist/`; Schaltplan/Design/Intake/Concept-Files in ihre Buckets.
- **Archivieren:** `REPO_INVENTORY.md`, `SUPERVISOR_BRIEFING.md`, `GIT_DIAGNOSE.md`, `GLOBAL_LESSONS_KONTEXT.md`, `LESSONS_KONSOLIDIERT.md`, beide Gist-Drafts.
- **Löschen:** `workflow/__pycache__/gist_publisher.cpython-310.pyc` (Build-Artefakt). `GIT_DIAGNOSE.md` optional löschbar (Erkenntnis steht als Lesson).
- **Offene Entscheidung (nicht durch Aufräumen lösbar):** `lessons/zerberus_lessons.md` (386 KB Sync-Kopie) — gehört laut eigener Regel ins Projekt-Repo; Konsolidierung steht in DECISIONS_PENDING.

---

## 5. LÜCKEN — was für das beschriebene System fehlt (nur Vorschlag)

Das System ist erstaunlich vollständig (Templates ✅, Lessons ✅, Workflow ✅, Schaltplan ✅). Auffällige Lücken:

1. **Kein `scripts/`-Ordner lokal**, obwohl Templates/Workflow ihn massiv referenzieren (`scripts/lessons_lookup.py`, `propagate_stand.py`, `session_end.ps1`, Hook-Scripts, `STAND.json`). Diese leben offenbar im Zerberus-Repo. **Lücke:** Die generischen, projekt-übergreifenden Helfer sollten als **Template/Referenz hier** liegen (so wie `gist_publisher.py`), sonst kann ein frisches Bootstrap-Projekt sie nicht ziehen. → `scripts/`-Template-Ordner oder `templates/scripts/`.

2. **Kein Index/Register für den Schaltplan + Übergabe-Schema.** `fabrik_meta_workflow.json` und `uebergabe_template_v1_0.md` sind neu und in REPO_INDEX/README noch **nicht verzeichnet**. → in REPO_INDEX + README aufnehmen.

3. **Kein „Lessons-Hierarchie-Index" auf oberster Ebene.** Die Schaltplan-JSON nennt das selbst als Fracture (`fr.lessons-no-index`): GLOBAL_LESSONS / LESSONS_KONSOLIDIERT / KONTEXT / lessons/ / projekt-lessons haben keinen gemeinsamen Einstieg. `lessons/INDEX.md` deckt nur den Unterordner ab. → ein Top-Level-`LESSONS_MAP.md`, das alle Ebenen verlinkt.

4. **Kein `CHANGELOG.md` für das Meta-Repo selbst.** Templates verlangen es von jedem Projekt, das Meta-Repo führt aber keins (Historie steckt verstreut in `_erledigt/` + mjolnir). → optional.

5. **Kein Verteilungs-Mechanismus für globale Lessons IN laufende Projekte** dokumentiert. Der Kontext sagt „Lessons werden während des Laufs an Worker UND Supervisor mitgegeben" — der Schaltplan hat dafür Cron-Knoten (`be.cron.lessons`, HITL-gated Merge), aber lokal fehlt die Beschreibung, wie GLOBAL_LESSONS konkret in ein Projekt gespiegelt wird (nur Gist-Pflicht ist dokumentiert). → kurzer Abschnitt in `workflow/`.

6. **`bugs/` hat nur Zerberus** und der Bug-Tracker driftet (April-Stand, beide „offen", obwohl Lessons spätere Fixes andeuten). → Status-Abgleich, keine strukturelle Lücke.

---

*Ende INVENTORY.md — Phase 1 abgeschlossen, keine Datei verändert.*
