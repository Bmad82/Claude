<!-- TEMPLATE | Kopie als MARATHON_WORKFLOW_{PROJEKT}.md ins Projekt-Root | Aufgabenliste mit Status nach jedem Patch updaten -->

# MARATHON_WORKFLOW_{PROJEKT}.md | Bibel-Format
Aufgabenliste {PROJEKT} | Status nach jedem Patch updaten

Status-Symbole: ⬜ offen · 🔄 in Arbeit · ✅ fertig · ⏸ blockiert · ⚠ teilweise

## Regel 0 — Faulheits-Catches gelten VOR jeder Patch-Logik
Siehe `C:\Users\chris\Python\Claude\GLOBAL_LESSONS.md` Sektion „Die 6 Faulheits-Catches — Quick Reference".

## Session-Zyklus (PFLICHT)
1. **Konflikt-Check:** `mjolnir.md` mit `STATUS: IN_ARBEIT` + abweichender FEATURE_REQUEST-Kurzname → QUEUED-Pattern (siehe CLAUDE_{PROJEKT}.md Session-Start-Pflicht).
2. `FEATURE_REQUEST_{kurzname}.md` prüfen | existiert? → abarbeiten | bei STATUS=FERTIG umbenennen zu `_ERLEDIGT.md`.
3. `mjolnir.md` einlesen (STATUS-Header zuerst), dann löschen (Single-Slot).
4. `HANDOVER_{PROJEKT}.md` lesen.
5. `python scripts/lessons_lookup.py --task '<aufgabe>'` (TF-IDF Top-3, mw-v2a Paket 1) | globale Quellen: `GLOBAL_LESSONS.md`, `SUPERVISOR_KODEX.md` | task-spezifische Regeln aus `playbooks/`, pfadspezifische aus `.claude/rules/` (mw-v2b Paket 2).
6. Nächsten ⬜-Eintrag aus Workflow ziehen.
7. Patch durchführen | Status updaten.
8. Doku-Pflicht (CLAUDE/SUPERVISOR/CHANGELOG/lessons) | git commit+push (Coda macht SELBST, kein Auftrag an Chris).
9. **Auffüll-Check** (siehe Session-Auffüll-Regel unten): Auftrag erledigt UND < 300k Token verbraucht → nächstes Item aus FEATURE_REQUEST/Workflow/BACKLOG nehmen statt abzuschließen.
10. `mjolnir.md` mit STATUS-Header schreiben (Session-Ende, ausnahmslos).

## Session-Auffüll-Regel (2026-05-21)

Primärer Auftrag erledigt UND Token-Stand < 300k → NICHT abschließen, weiterarbeiten.

Auffüll-Reihenfolge:
1. Weitere Punkte im selben FEATURE_REQUEST (z.B. N+3, N+4... bei Multi-Session-Plänen)
2. Offene Items in MARATHON_WORKFLOW mit Status OFFEN + keine Abhängigkeiten
3. BACKLOG-Items mit Status OFFEN, sortiert nach Priorität (Sofort > Mittelfristig > Nice-to-have)
4. Bekannte Test-Schulden (pre-existing Failures fixen)
5. Doku-Hygiene (veraltete Stand-Anker, README-Drift, Lessons-Konsolidierung)

Stopp-Schwelle: ~350k Token (50k Reserve für sauberen Doku-Abschluss).

Ausnahmen — NIE als Auffüller:
- Destruktive Operationen (DB-Migration, Auth-Refactor, FAISS-Switch)
- Items die Chris-Entscheidung brauchen (DECISIONS_PENDING)
- Items die externe Ressourcen brauchen (Docker-Pull, Modell-Download > 1 GB)
- Items die die Test-Suite fundamental ändern (neues Framework, Fixture-Umbau)

Doku-Pflicht bei Auffüll-Patches:
- Eigener `git commit` pro Folge-Patch (mit Patch-Nummer/Name)
- Lesson-Eintrag falls nötig
- KEIN separater HANDOVER/SUPERVISOR/Gist-Update pro Zwischen-Patch
- Am Session-Ende: EIN HANDOVER der ALLE Patches zusammenfasst

Anti-Pattern: "Patch fertig bei 120k → Doku → Handover → STOPP" — verbrennt 80% des Budgets für Overhead.

## Phase 1 — {PHASENNAME}

| # | Ziel | Braucht | Status | Notizen |
|---|------|---------|--------|---------|
| 1 | {Aufgabe} | — | ⬜ | {Hinweis/Patch-Nr} |

## Phase 2 — {PHASENNAME}

| # | Ziel | Braucht | Status | Notizen |
|---|------|---------|--------|---------|
| n | {Aufgabe} | #{vorher} | ⬜ | {Hinweis} |

## Backlog (ohne Phase)
- {Idee/Wunsch ohne Termin}

## Decisions Pending
Verweis auf `DECISIONS_{PROJEKT}.md` oder Projekt-Root `DECISIONS_PENDING.md`. Nicht inline doppeln.
