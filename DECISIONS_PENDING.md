<!-- DECISIONS_PENDING | offene Architektur-Fragen, blockierte Aufträge, dokumentierte Konflikte -->

# DECISIONS_PENDING.md | Bibel-Format
Offene Entscheidungen + Konflikte für `Claude/`-Meta-Layer | jede Frage mit Datum+Hintergrund+Optionen

## Offene Entscheidungen (Pending)

### 2026-05-17 | Quelle Try_Faulheits_catch.md fehlt
Frage|Wo liegt `Try_Faulheits_catch.md` aus dem die 6 Faulheits-Catches stammen sollen?
Hintergrund|FEATURE_REQUEST_CLAUDE.md verweist als Quelle auf `C:\Users\chris\Python\Claude\Try_Faulheits_catch.md`. Datei existiert weder im Working Directory noch in Git-History (`git log --all -- "*Faulheit*"` liefert null Treffer). Coda hat die 6 Catches aus existierenden Quellen rekonstruiert: 4 aus `GLOBAL_LESSONS.md` (OBERSTES GEBOT, mjolnir-Round-Trip, Worktree-Self-Merge, Supervisor-Prompts), 1 aus `lessons/zerberus_lessons.md` Commit `08c7e9e` (Multi-Session-Status-Header + QUEUED-Pattern), 1 aus Supervisor-Don'ts der FEATURE_REQUEST selbst (Selbsttest-Pflicht für Workflow-Änderungen).
Optionen|A) Bestätigen dass die rekonstruierten 6 Catches korrekt sind | B) Original `Try_Faulheits_catch.md` nachliefern damit Coda 1:1 abgleichen kann | C) Liste der 6 Catches im Chat bestätigen lassen
Blockiert|nichts mehr — Implementierung ist mit rekonstruierter Liste durchgelaufen. Bei Abweichung: `GLOBAL_LESSONS.md` Sektion "Die 6 Faulheits-Catches" anpassen.
Eingetragen|2026-05-17

### 2026-05-17 | Dual-Templates-Folder (templates/ + _templates/)
Frage|Soll `templates/` (alt, 8 Files) parallel zu `_templates/` (neu, 4 Files) bestehen bleiben oder konsolidiert werden?
Hintergrund|FEATURE_REQUEST_CLAUDE.md fordert explizit `Claude/_templates/` als Ziel. Bestehender `Claude/templates/`-Ordner (commit 31b32f5, 2026-05-15) enthält bereits 8 Projekt-Templates (CLAUDE_, SUPERVISOR_, MARATHON_WORKFLOW_, HANDOVER_, DECISIONS_, DESIGN_, ROADMAP_, lessons_). Coda hat strikt nach FEATURE_REQUEST `_templates/` neu angelegt mit den 4 dort spezifizierten Files. `CLAUDE_PROJEKT_TEMPLATE.md` und `SUPERVISOR_PROJEKT_TEMPLATE.md` in `_templates/` sind Teildoppelung der bestehenden `CLAUDE_TEMPLATE.md` und `SUPERVISOR_TEMPLATE.md` in `templates/`.
Optionen|A) Beide Ordner behalten — `_templates/` als globaler Marathon-Workflow-Bootstrap, `templates/` als ältere Projekt-Skelette | B) `templates/` in `_templates/` mergen (Inhalte übernehmen, Namen konsolidieren) | C) `templates/` löschen, `_templates/` als alleinige Quelle
Blockiert|nichts — `PROJECT_BOOTSTRAP_README.md` verweist auf `_templates/` wie im FEATURE_REQUEST gefordert. Bestehende `CLAUDE_TEMPLATE.md`-Verweise auf `templates/` bleiben gültig.
Eingetragen|2026-05-17

## Getroffene Entscheidungen

### 2026-05-17 | Auftrag faulheits-catch-integration auf main statt im Worktree
Entscheidung|Direktes Arbeiten auf `main` ohne Worktree-Branch
Begründung|FEATURE_REQUEST Schritt 07 sagt explizit: „Branch: direkt auf `main` (kein Worktree für Strukturarbeit nötig)."
Alternativen|Worktree-Branch wäre Overkill für reine Dateierstellung ohne Code-Risiko
Konsequenz|4 thematische Commits direkt auf main, Push danach
Patch-Referenz|faulheits-catch-integration (2026-05-17)
