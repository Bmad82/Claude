# Claude — Marathon Workflow Knowledge Base

Persönliche Knowledge-Base für den Marathon-Workflow.
Architekt: Chris (@Bmad82)

⚠️ **DIESES REPO IST PUBLIC.** Niemals Passwörter, API-Keys, Tokens, persönliche Daten, IP-Adressen, interne URLs, Hostnamen oder projektspezifische Secrets reinschreiben. Im Zweifel: nicht committen und nachfragen.

## Was ist der Marathon-Workflow?

Drei-Rollen-System zur Software-Entwicklung, bei dem der Architekt selbst kein Terminal anfasst:

- **Architekt** (Mensch) — gibt Ziele vor, arbeitet primär mobil per Spracheingabe (Whisper)
- **Supervisor** (Claude im Chat-Fenster) — plant, prüft, schreibt Coda-Prompts als `.md`-Dateien
- **Coda** (Claude Code im Terminal) — implementiert, testet, committet, merged, pusht

Architekt fasst kein Terminal an. Supervisor schickt keinen Inline-Befehl. Coda macht die Hände-schmutzig-Arbeit. Ausführliche Beschreibung: [`workflow/MARATHON_WORKFLOW.md`](workflow/MARATHON_WORKFLOW.md).

## Navigations-Einstieg

[`REPO_INDEX.md`](REPO_INDEX.md) ist die kanonische Liste aller Dateien im Repo mit Raw-Links. Der Supervisor fetcht diese Datei und leitet daraus Links für beliebige andere Dateien ab — kein manuelles Link-Relaying.

## Ordnerstruktur

| Pfad | Zweck |
|---|---|
| [`README.md`](README.md) | Diese Datei — Einstieg, Drei-Rollen-Modell, Verzeichniserklärung |
| [`REPO_INDEX.md`](REPO_INDEX.md) | Auto-gepflegtes Verzeichnis mit Raw-Links für Supervisor-Navigation |
| [`INVENTORY.md`](INVENTORY.md) | Bestandsaufnahme + Aufräum-Mapping (ordner-cleanup, 2026-06-19) |
| [`DESIGN.md`](DESIGN.md) / [`DESIGN_KINTSUGI.md`](DESIGN_KINTSUGI.md) | Globale UI-Referenz (Schema) + befülltes Kintsugi-Designsystem |
| [`Projektanfrage.html`](Projektanfrage.html) | Intake-Formular — Pipeline-Einstieg (Schaltplan-Knoten `in.start`) |
| [`GLOBAL_LESSONS.md`](GLOBAL_LESSONS.md) | Universelle Lessons: 6 Faulheits-Catches, Selbsttest-Pattern, Bibel-Format |
| [`SUPERVISOR_KODEX.md`](SUPERVISOR_KODEX.md) | NIE/IMMER-Listen für Chat-Supervisor (gilt projektübergreifend) |
| [`PROJECT_BOOTSTRAP_README.md`](PROJECT_BOOTSTRAP_README.md) | Anleitung: frische Coda-Session setzt neues Projekt auf |
| [`DECISIONS_PENDING.md`](DECISIONS_PENDING.md) | Offene Meta-Layer-Architektur-Fragen + getroffene Entscheidungen |
| [`GIST_LINK.md`](GIST_LINK.md) | Gist-Brücke: Index- + Claude-KB-Gist-URLs (Supervisor-Lesezugang) |
| [`HANDOVER.json`](HANDOVER.json) | Session-Abschluss-State (Single-Slot, STATUS-Header) |
| [`schaltplan/`](schaltplan/) | **Steuer-/Plan-Files** — Fabrik-Meta-Workflow als JSON (SSOT) + HTML-Render |
| [`workflow/`](workflow/) | Marathon-Workflow-Dokumentation (Rollen, Datei-Hierarchie, Session-Zyklus, Catches) |
| [`templates/`](templates/) | Bootstrap-Vorlagen für neue Projekte (CLAUDE, SUPERVISOR, HANDOVER, SCHALTPLAN, FEATURE_REQUEST, Übergabe u.a.) |
| [`lessons/`](lessons/) | Technologie-spezifische Lessons (siehe [`lessons/INDEX.md`](lessons/INDEX.md) für Hierarchie) |
| [`concepts/`](concepts/) | Konzept-/Strategie-Dokumente (Faulheits-Catch-Ursprung, Orchestrator-Konzept, Token-Opt) |
| [`bugs/`](bugs/) | Projektspezifische Bug-Tracker (pro Projekt ein Unterordner) |
| [`_erledigt/`](_erledigt/) | Archiv erledigter FEATURE_REQUEST-Aufträge (Audit-Historie, nicht löschen) |
| [`_archive/`](_archive/) | Abgelöste/veraltete Inhalts- & Struktur-Dateien (Audit, nicht live — siehe [`_archive/README.md`](_archive/README.md)) |

## Einbindung in Projekte

Projekte referenzieren diese Knowledge-Base direkt aus dem Repo — nicht kopieren, sondern verlinken. Im `CLAUDE_{PROJEKT}.md` am Anfang:

> Globale Wissensbasis: https://github.com/Bmad82/Claude
> Vor Arbeitsbeginn: `GLOBAL_LESSONS.md` + `SUPERVISOR_KODEX.md` lesen.
> Nach Erkenntnis: projektübergreifende Lessons in `GLOBAL_LESSONS.md` ergänzen.

## Dateinamen-Konvention

Projektspezifische Files tragen IMMER den Projektnamen als Suffix:
- `CLAUDE_{PROJEKT}.md`, `SUPERVISOR_{PROJEKT}.md`, `MARATHON_WORKFLOW_{PROJEKT}.md`, `lessons_{PROJEKT}.md`
- `FEATURE_REQUEST_{kurzname}.md` (kebab-case aus Auftrag-Frontmatter, NIE Projektname)
- Ausnahmen: `HANDOVER.json`, `PROJECT_BOOTSTRAP_README.md`, `REPO_INDEX.md` heißen immer so.

`templates/` enthält Schablonen für Tag 1 eines neuen Projekts. `lessons/` ist hingegen lebendig — wird bei jedem Patch konsultiert.

## Projekte die mit diesem System arbeiten

- **Zerberus Pro 4.0** — Python-Backend, Patch 100+ — siehe `lessons/zerberus_lessons.md` und `bugs/zerberus/`
- (weitere folgen)

## Lizenz

Privates Repo, public sichtbar. Inhalte dienen der Selbst-Dokumentation. Keine Garantie auf Korrektheit oder Anwendbarkeit außerhalb des eigenen Workflows.
