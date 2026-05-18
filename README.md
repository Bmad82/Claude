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
| [`DESIGN.md`](DESIGN.md) | Globale UI-Layer-Referenz (Farben, Typografie, Komponenten, Mobile-Regeln) |
| [`GLOBAL_LESSONS.md`](GLOBAL_LESSONS.md) | Universelle Lessons: 6 Faulheits-Catches, Selbsttest-Pattern, Bibel-Format |
| [`SUPERVISOR_KODEX.md`](SUPERVISOR_KODEX.md) | NIE/IMMER-Listen für Chat-Supervisor (gilt projektübergreifend) |
| [`PROJECT_BOOTSTRAP_README.md`](PROJECT_BOOTSTRAP_README.md) | Anleitung: frische Coda-Session setzt neues Projekt auf |
| [`DECISIONS_PENDING.md`](DECISIONS_PENDING.md) | Offene Meta-Layer-Architektur-Fragen + getroffene Entscheidungen |
| [`mjolnir.md`](mjolnir.md) | Session-Abschluss-State (Single-Slot, STATUS-Header) |
| [`workflow/`](workflow/) | Marathon-Workflow-Dokumentation (Rollen, Datei-Hierarchie, Session-Zyklus, Catches) |
| [`templates/`](templates/) | Bootstrap-Vorlagen für neue Projekte (CLAUDE, SUPERVISOR, mjolnir, FEATURE_REQUEST u.a.) |
| [`lessons/`](lessons/) | Technologie-spezifische Lessons (siehe [`lessons/INDEX.md`](lessons/INDEX.md) für Hierarchie) |
| [`bugs/`](bugs/) | Projektspezifische Bug-Tracker (pro Projekt ein Unterordner) |
| [`concepts/`](concepts/) | Historische Konzept-Dokumente (Ursprünge, Architektur-Skizzen) |
| [`_erledigt/`](_erledigt/) | Archiv erledigter FEATURE_REQUEST-Aufträge (Audit-Historie, nicht löschen) |
| [`_drafts_gist/`](_drafts_gist/) | Konzept-Entwürfe für Phase-3-Gist-Migration (nicht aktiv) |

## Einbindung in Projekte

Projekte referenzieren diese Knowledge-Base direkt aus dem Repo — nicht kopieren, sondern verlinken. Im `CLAUDE_{PROJEKT}.md` am Anfang:

> Globale Wissensbasis: https://github.com/Bmad82/Claude
> Vor Arbeitsbeginn: `GLOBAL_LESSONS.md` + `SUPERVISOR_KODEX.md` lesen.
> Nach Erkenntnis: projektübergreifende Lessons in `GLOBAL_LESSONS.md` ergänzen.

## Dateinamen-Konvention

Projektspezifische Files tragen IMMER den Projektnamen als Suffix:
- `CLAUDE_{PROJEKT}.md`, `SUPERVISOR_{PROJEKT}.md`, `MARATHON_WORKFLOW_{PROJEKT}.md`, `lessons_{PROJEKT}.md`
- `FEATURE_REQUEST_{kurzname}.md` (kebab-case aus Auftrag-Frontmatter, NIE Projektname)
- Ausnahmen: `mjolnir.md`, `PROJECT_BOOTSTRAP_README.md`, `REPO_INDEX.md` heißen immer so.

`templates/` enthält Schablonen für Tag 1 eines neuen Projekts. `lessons/` ist hingegen lebendig — wird bei jedem Patch konsultiert.

## Projekte die mit diesem System arbeiten

- **Zerberus Pro 4.0** — Python-Backend, Patch 100+ — siehe `lessons/zerberus_lessons.md` und `bugs/zerberus/`
- (weitere folgen)

## Lizenz

Privates Repo, public sichtbar. Inhalte dienen der Selbst-Dokumentation. Keine Garantie auf Korrektheit oder Anwendbarkeit außerhalb des eigenen Workflows.
