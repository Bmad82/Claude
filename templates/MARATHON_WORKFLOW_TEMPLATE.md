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
5. `lessons_{PROJEKT}.md` konsultieren | globale Quellen: `GLOBAL_LESSONS.md`, `SUPERVISOR_KODEX.md`.
6. Nächsten ⬜-Eintrag aus Workflow ziehen.
7. Patch durchführen | Status updaten.
8. Doku-Pflicht (CLAUDE/SUPERVISOR/CHANGELOG/lessons) | git commit+push (Coda macht SELBST, kein Auftrag an Chris).
9. `mjolnir.md` mit STATUS-Header schreiben (Session-Ende, ausnahmslos).

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
