# Zerberus Pro 4.0 — Live State (Gist Draft)

LAST_PATCH: P-???  |  TS: TBD  |  PROJECT: Zerberus Pro 4.0

## Files in diesem Gist (wenn aktiv)

- `mjolnir_zerberus.md` — Round-Trip-Status, was Chris physisch tun muss
- `SUPERVISOR_zerberus.md` — Bibel-Format-Überblick für Chat-Instanzen
- `MARATHON_WORKFLOW_zerberus.md` — Operative Workflow-Doku

## Nicht in diesem Gist

- `CLAUDE_zerberus.md` (Codas Betriebsanleitung, bleibt lokal + Repo)
- Lessons (separater Lessons-Gist später, ändert sich selten)
- Source-Code (bleibt in eigenständigem Repo)

## Sync-Mechanik (Phase-3-Konzept)

Wenn Phase 3 aktiv:
1. Coda schreibt mjolnir.md am Session-Ende lokal — wie bisher
2. Coda pusht zusätzlich ins Gist (via gh-CLI oder Git-Remote auf Gist)
3. Supervisor-Chat-Instanz fetched Gist statt lokales File
4. Architekt sieht den Gist direkt im Browser/Handy — kein Repo-Klon nötig
