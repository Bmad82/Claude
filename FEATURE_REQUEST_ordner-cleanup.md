<!-- TEMPLATE | Dateiname: FEATURE_REQUEST_ordner-cleanup.md | Kopie ins Projekt-Root | Coda arbeitet diese Datei beim Session-Start als Priorität ab -->

# FEATURE_REQUEST: Ordner-Cleanup — INVENTORY-Mapping ausführen (gated)

**Datum:** 2026-06-19
**Auftraggeber:** Chris (direkt, über Supervisor-Chat)
**Empfänger:** Coda
**Kurzname:** ordner-cleanup
**Erwartete Dauer:** 1 Session

---

## Kontext

Der Asset-Ordner ist über die Zeit gewachsen und unübersichtlich (lose Root-Files, Dubletten, falsch einsortierte Archive). Du hast in Phase 1 bereits eine `INVENTORY.md` mit vollständigem Mapping erstellt (65 Files gesichtet). Dieser FR führt das Mapping aus — destruktiv, aber reversibel und gated. Ziel-Kernstruktur: `Templates/`, `Lessons/`, `Workflow/` (+ eigene Schaltplan-Ablage). Alles andere muss sich begründen oder fliegt raus.

Quelle: `INVENTORY.md` (dein eigenes Phase-1-Mapping)

---

## Akzeptanzkriterien (TL;DR)

- [ ] Restore-Punkt gesetzt (Commit/Branch) BEVOR irgendwas verschoben/gelöscht wird
- [ ] `GLOBAL_LESSONS_KONTEXT.md`-Prosa in `GLOBAL_LESSONS.md` zurückgemergt, Merge verifiziert, DANN KONTEXT archiviert (nicht hart gelöscht)
- [ ] Absolutpfad-Files: pro File entschieden — am Root belassen ODER Pfad in ALLEN Templates nachgezogen; keine gebrochene Referenz
- [ ] Zielstruktur Templates/ Lessons/ Workflow/ (+ Schaltplan-Ablage) steht, Mapping ausgeführt
- [ ] FR-Archive aus Root → `_erledigt/`; Einmal-Reports archiviert; `.pyc`/`__pycache__` raus
- [ ] Commit + Push erfolgt, `$LASTEXITCODE = 0` verifiziert
- [ ] `HANDOVER.json` mit STATUS-Header geschrieben (bzw. `mjolnir.md`, falls FR supervisor-aufbau noch nicht gelaufen)

---

## Schritt 01 — Restore-Punkt (PFLICHT, zuerst)

Setze einen sauberen Wiederherstellungspunkt, bevor du irgendetwas anfasst: Commit des Ist-Stands ODER eigener Branch. Reversibilität geht vor Tempo. Verschieben statt Löschen, wo möglich (Ziel `_archive/` statt `rm`).

**Done:** Restore-Punkt existiert, im Handover notiert.

---

## Schritt 02 — GLOBAL_LESSONS-Merge (Risiko-Schritt)

`GLOBAL_LESSONS_KONTEXT.md` ist ein älterer, prosareicherer Zwilling von `GLOBAL_LESSONS.md`, dem die neuesten Lessons fehlen. Zwei konkurrierende Lessons-Wahrheiten = das Anti-Pattern, das der Workflow killt.
1. Übernimm die wertvolle Prosa aus KONTEXT in `GLOBAL_LESSONS.md` (nichts verlieren).
2. Verifiziere den Merge (Diff prüfen, keine Lesson fällt weg).
3. ERST DANN KONTEXT nach `_archive/` (nicht hart löschen).

Bei Unsicherheit, welche Version recht hat → DECISIONS_PENDING.md, nicht raten.

**Done:** Eine einzige GLOBAL_LESSONS-Wahrheit, KONTEXT archiviert, Merge im Handover belegt.

---

## Schritt 03 — Absolutpfad-Gate (Bruch-Risiko)

`GLOBAL_LESSONS.md`, `SUPERVISOR_KODEX.md`, `DECISIONS_PENDING.md`, `PROJECT_BOOTSTRAP_README.md`, `GIST_LINK.md` u. a. sind per HARTEM Absolutpfad in den Templates verdrahtet. Verschieben bricht die Templates lautlos.

Pro betroffenem File EINE Entscheidung:
- **am Root belassen** (Default bei Unsicherheit), ODER
- **verschieben + Pfad in ALLEN referenzierenden Templates nachziehen** (vorher per Suche alle Referenzen auflisten).

Liste die betroffenen Files + gewählte Option im Handover auf. Keine halbe Migration.

**Done:** Kein gebrochener Template-Pfad; Entscheidung je File dokumentiert.

---

## Schritt 04 — Rest-Mapping ausführen

Führe dein INVENTORY-Mapping für den unkritischen Rest aus:
- 3 FR-Archive aus dem Root → `_erledigt/`.
- Einmal-Reports (`REPO_INVENTORY.md`, `SUPERVISOR_BRIEFING.md`, `GIT_DIAGNOSE.md`) → `_archive/` (von REPO_INDEX abgelöst).
- `WORKFLOW_SUMMARY.md` korrekt einordnen (ist Live-File, kein Draft).
- `.pyc` / `workflow/__pycache__/` löschen (regenerierbar, gitignored).
- Schaltplan-Files (`fabrik_meta_workflow.json` + `.html`) in eigene Schaltplan-Ablage bzw. `Workflow/` gemäß Mapping.
- Dubletten-Gruppen aus der INVENTORY auflösen.

**Done:** Zielstruktur steht, Root ist aufgeräumt, Listing im Handover.

---

## Schritt 05 — Commit + Push

Branch: main (oder Cleanup-Branch aus Schritt 01)
Commits getrennt nach Wirkung:
1. `refactor(lessons): GLOBAL_LESSONS-Merge, KONTEXT-Zwilling archiviert`
2. `chore(struktur): Root aufgeräumt, Archive einsortiert, pycache entfernt`

Push auf `origin/main`. `$LASTEXITCODE = 0` verifizieren. Bei Fehler → DECISIONS_PENDING.md + Handover BLOCKIERT, auf Deutsch.

---

## Schritt 06 — HANDOVER schreiben

Schreibe `HANDOVER.json` (neues Format, falls FR supervisor-aufbau schon lief) oder `mjolnir.md` (Ist-Format, sonst) mit STATUS-Header + was Chris physisch prüfen sollte (Stichprobe Struktur) + Auftragshistorie.

---

## Wichtige Hinweise

- **Reversibilität vor Tempo.** Verschieben/Archivieren statt Löschen. Restore-Punkt steht vor jedem destruktiven Schritt.
- **NICHT ins Git-Repo-Inneres, NICHT in Gists** — nur die lokalen Files in diesem Ordner. Repo-Abgleich macht Chris später selbst.
- **Bei Konflikten/Unklarheiten:** Nicht raten. DECISIONS_PENDING.md + Handover-Verweis.
- **Quellen-Files** bleiben liegen; Verteilung über GLOBAL_LESSONS / Kodex / templates, nicht durch Verschieben der Ursprungsdatei.
