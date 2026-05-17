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
