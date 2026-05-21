# WORKFLOW_SUMMARY — Marathon-Workflow Kompakt
<!-- Quelle: Bmad82/Claude/workflow/MARATHON_WORKFLOW.md + GLOBAL_LESSONS.md -->
<!-- Bibel-Format, Token-effizient. Volltext im Claude-Repo. -->

## Die drei Rollen

| Rolle | Instanz | Aufgabe |
|---|---|---|
| Architekt | Chris (Mensch, Whisper-Eingabe) | Ideen, Richtung — kein Code, kein Terminal |
| Supervisor | Claude im Chat (claude.ai) | plant, prüft, schreibt Coda-Prompts als .md |
| Coda | Claude Code (CLI) | implementiert, testet, committet, merged, pusht |

## Session-Zyklus (Coda, Kurzform)

1. Konflikt-Check: mjolnir.md STATUS=IN_ARBEIT + abweichender FEATURE_REQUEST → neuer → _QUEUED.md
2. FEATURE_REQUEST_{kurzname}.md lesen → Priorität 1 → bei FERTIG: _ERLEDIGT.md
3. mjolnir.md lesen (STATUS-Header zuerst), dann löschen (Single-Slot)
4. HANDOVER_{PROJEKT}.md lesen
5. MARATHON_WORKFLOW_{PROJEKT}.md lesen
6. lessons_{PROJEKT}.md konsultieren
7. Globale Quellen: GLOBAL_LESSONS.md, SUPERVISOR_KODEX.md
8. Arbeit ausführen — Tests, Commit, Push selbst ($LASTEXITCODE verifizieren)
9. **Auffüll-Check:** Auftrag erledigt UND < 300k Token verbraucht → nächstes Item aus MARATHON_WORKFLOW oder BACKLOG nehmen. Stopp bei ~350k (50k Reserve für Doku). NUR sichere, unabhängige Items — destruktive Ops nie als Auffüller.
10. Worktree-Branches selbst auf main mergen (kein „Schritt 0 für Chris")
11. mjolnir.md neu schreiben mit STATUS-Header (FERTIG|IN_ARBEIT|BLOCKIERT) — PFLICHT
12. Bei Verzeichnisänderungen: REPO_INDEX.md aktualisieren VOR finalem Push
13. Bei Session-Ende: Gist-Dateien aktualisieren (HANDOVER, MJOLNIR, STATUS, ggf. REPO_INDEX, LESSONS)

## Datei-Konventionen

### Bibel-Format (Pipe-getrennt, maschinen-lesbar)
- Lessons, Status-Header, KODEX-Zeilen → Pipe-Format
- Begründung/Kontext darunter als fett-prosaische Absätze
- Status-Header (mjolnir.md Zeile 1): `STATUS|{FERTIG|IN_ARBEIT|BLOCKIERT}|AUFTRAG: {kurzname}|FORTSCHRITT: X/Y|NÄCHSTE SESSION: ...`

### Prosa
- BOOTSTRAP_README, FEATURE_REQUEST-Anhänge → reine Prosa
- Mensch-freundlich für Whisper-Eingabe

### Naming
- FEATURE_REQUEST_{kurzname}.md — kebab-case aus Frontmatter, NIE Projektname
- Projektspezifische Files mit Projekt-Suffix: CLAUDE_zerberus.md, SUPERVISOR_zerberus.md, MARATHON_WORKFLOW_zerberus.md, lessons_zerberus.md
- Kurzname-Files (mjolnir.md, FEATURE_REQUEST_*.md) ohne Projekt-Suffix — Verzeichnis ist Kontext
- Lifecycle-Suffixe: _ERLEDIGT.md (Audit), _QUEUED.md (Konflikt)

## Die 6 Faulheits-Catches (Quick Reference)

1. **OBERSTES GEBOT** — Coda terminalisiert NICHTS was Coda kann. Kein git/pytest/pip/robocopy/npm an Chris.
2. **mjolnir.md PFLICHT am Session-Ende** — Single-Slot-Round-Trip, ausnahmslos.
3. **Worktree-Branches selbst auf main mergen** — Kein „Schritt 0 für Chris", ff-merge oder rebase selbst.
4. **Supervisor baut Coda-Prompts statt Terminal-Befehle** — Auch „nur ein Befehl" im Chat ist einer zu viel.
5. **Multi-Session-STATUS-Header + QUEUED-Pattern** — mjolnir.md mit STATUS-Block als erster Zeile.
6. **Selbsttest-Pflicht für Workflow-Änderungen** — Dreiphasig (A Setup, B Replay, C Adversarial, D Cleanup). Hoffnung ≠ Verifikation.

## Gist-Konvention (Seit 2026-05-18)

- Jedes Projekt hat einen PUBLIC Gist (Briefing-Dateien: HANDOVER, MJOLNIR, REPO_INDEX, STATUS, LESSONS)
- Gist-URL steht in `GIST_LINK.md` im Repo-Root
- Index-Gist navigiert zu allen Projekt-Gists
- Claude-KB-Gist enthält globale Wissensbasis (GLOBAL_LESSONS, TEMPLATES_INDEX, WORKFLOW_SUMMARY, BOOTSTRAP_CHECKLIST)
- Coda aktualisiert Projekt-Gist am Session-Ende — neben den lokalen Dateien
- Supervisor (Chat-Instanz) fetcht Projekt-Gist statt Raw-Links — keine Auth nötig
- Alle Gists PUBLIC (Lesezugriff für beliebige LLM-Instanzen ohne Token)
