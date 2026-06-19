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

1. Konflikt-Check: HANDOVER.json STATUS=IN_ARBEIT + abweichender FEATURE_REQUEST → neuer → _QUEUED.md
2. FEATURE_REQUEST_{kurzname}.md lesen → Priorität 1 → bei FERTIG: _ERLEDIGT.md
3. HANDOVER.json lesen (STATUS-Header zuerst), Datei NICHT löschen (status wird überschrieben, historie ist append-only)
4. SCHALTPLAN_PROJEKT.json lesen (Projekt-Gedächtnis: Module, Status, Brüche)
5. MARATHON_WORKFLOW_{PROJEKT}.md lesen
6. `python scripts/lessons_lookup.py --task '<aufgabe>'` (TF-IDF Top-3, mw-v2a Paket 1) — NICHT `lessons_{PROJEKT}.md` komplett laden
7. Globale Quellen: GLOBAL_LESSONS.md, SUPERVISOR_KODEX.md | task-spezifisch aus `playbooks/`, pfadspezifisch aus `.claude/rules/` (mw-v2b Paket 2)
8. Arbeit ausführen — Tests, Commit, Push selbst ($LASTEXITCODE verifizieren)
9. **Auffüll-Check:** Auftrag erledigt UND < 300k Token verbraucht → nächstes Item aus MARATHON_WORKFLOW oder BACKLOG nehmen. Stopp bei ~350k (50k Reserve für Doku). NUR sichere, unabhängige Items — destruktive Ops nie als Auffüller.
10. Worktree-Branches selbst auf main mergen (kein „Schritt 0 für Chris")
11. HANDOVER.json neu schreiben mit STATUS-Header (FERTIG|IN_ARBEIT|BLOCKIERT) — PFLICHT
12. Bei Verzeichnisänderungen: REPO_INDEX.md aktualisieren VOR finalem Push
13. Bei Session-Ende: `scripts/session_end.ps1` (mw-v2a Paket 2) buendelt Push + sync_repos + Gist-PATCH + verify_sync; Gist-Dateien (STATUS, HANDOVER, SCHALTPLAN, ggf. REPO_INDEX, LESSONS) | optional: SessionEnd-Hook (mw-v2b Paket 1, opt-in)

## Datei-Konventionen

### Bibel-Format (Pipe-getrennt, maschinen-lesbar)
- Lessons, Status-Header, KODEX-Zeilen → Pipe-Format
- Begründung/Kontext darunter als fett-prosaische Absätze
- Status-Header (HANDOVER.json Zeile 1): `STATUS|{FERTIG|IN_ARBEIT|BLOCKIERT}|AUFTRAG: {kurzname}|FORTSCHRITT: X/Y|NÄCHSTE SESSION: ...`

### Prosa
- BOOTSTRAP_README, FEATURE_REQUEST-Anhänge → reine Prosa
- Mensch-freundlich für Whisper-Eingabe

### Naming
- FEATURE_REQUEST_{kurzname}.md — kebab-case aus Frontmatter, NIE Projektname
- Projektspezifische Files mit Projekt-Suffix: CLAUDE_zerberus.md, SUPERVISOR_zerberus.md, MARATHON_WORKFLOW_zerberus.md, lessons_zerberus.md
- Kurzname-Files (HANDOVER.json, FEATURE_REQUEST_*.md) ohne Projekt-Suffix — Verzeichnis ist Kontext
- Lifecycle-Suffixe: _ERLEDIGT.md (Audit), _QUEUED.md (Konflikt)

## Die 6 Faulheits-Catches (Quick Reference)

1. **OBERSTES GEBOT** — Coda terminalisiert NICHTS was Coda kann. Kein git/pytest/pip/robocopy/npm an Chris.
2. **HANDOVER.json PFLICHT am Session-Ende** — Single-Slot-Round-Trip, ausnahmslos.
3. **Worktree-Branches selbst auf main mergen** — Kein „Schritt 0 für Chris", ff-merge oder rebase selbst.
4. **Supervisor baut Coda-Prompts statt Terminal-Befehle** — Auch „nur ein Befehl" im Chat ist einer zu viel.
5. **Multi-Session-STATUS-Header + QUEUED-Pattern** — HANDOVER.json mit STATUS-Block als erster Zeile.
6. **Selbsttest-Pflicht für Workflow-Änderungen** — Dreiphasig (A Setup, B Replay, C Adversarial, D Cleanup). Hoffnung ≠ Verifikation.

## Progressive Disclosure (mw-v2b Paket 2, 2026-05-21)

CLAUDE_{PROJEKT}.md ist Kern-Bibel (OBERSTES GEBOT + Faulheits-Catches + Workflow), Ziel ~100 Zeilen, Max 150. Detail-Wissen wandert:
- **Task-Playbooks** in `playbooks/<task>.md` (z.B. testing, rag_pipeline, auth_security, database, observability) — werden gelesen wenn Patch das Task-Gebiet beruehrt
- **Path-Rules** in `.claude/rules/<rule>.md` mit YAML-Frontmatter `globs: [...]` (NICHT `paths:`) — Claude Code matched globs gegen die aktive Datei und laedt nur passende Rules
- **Opt-in-Setup:** Path-Rules-Templates in `docs/claude_rules/` + README mit Install-Instructions (Variante A committed / Variante B lokal). Konsistent mit Hooks-Wiring (`scripts/HOOK_SETUP.md`)

Wenn der Kern wachsen will: lieber Auslagern als Komprimieren. Drei-Schichten: (1) was IMMER gilt → Kern, (2) was bei Task-Typ gilt → Playbook, (3) was bei Datei-Klasse gilt → Rule.

## Claude Code Hooks (mw-v2b Paket 1, opt-in)

Scripts liegen lauffaehig im Repo (`scripts/`), Verdrahtung in `.claude/settings.json` ist Chris-Entscheidung (siehe `scripts/HOOK_SETUP.md`). Drei Hooks vorbereitet:
- **SessionStart** | `lessons_lookup_auto.py` | leitet Query aus FEATURE_REQUEST/HANDOVER ab + ruft `lessons_lookup.py`
- **PreToolUse** (Edit|Write|MultiEdit) | `validate_edit.py` | blockt Edits an Schutzdateien (GLOBAL_LESSONS, KODEX, *_TEMPLATE_)
- **SessionEnd** | `session_end_check.py` | prueft HANDOVER/STAND/Gist-Marker, JSON systemMessage

## Gist-Konvention (Seit 2026-05-18)

- Jedes Projekt hat einen PUBLIC Gist (Briefing-Dateien: STATUS, HANDOVER, SCHALTPLAN, REPO_INDEX, LESSONS)
- Gist-URL steht in `GIST_LINK.md` im Repo-Root
- Index-Gist navigiert zu allen Projekt-Gists
- Claude-KB-Gist enthält globale Wissensbasis (GLOBAL_LESSONS, TEMPLATES_INDEX, WORKFLOW_SUMMARY, BOOTSTRAP_CHECKLIST)
- Coda aktualisiert Projekt-Gist am Session-Ende — neben den lokalen Dateien
- Supervisor (Chat-Instanz) fetcht Projekt-Gist statt Raw-Links — keine Auth nötig
- Alle Gists PUBLIC (Lesezugriff für beliebige LLM-Instanzen ohne Token)
