# FEATURE_REQUEST — Marathon Workflow v2a: Kontextentlastung (Sichere Gewinne)

**Kurzname:** mw-v2a-kontextentlastung
**Projekt:** Claude (Meta-Repo) + Zerberus (Pilot)
**Priorität:** KRITISCH
**Datum:** 2026-05-21
**Grundlage:** Deep Research PDF "LLM Regelbefolgung" + Supervisor-Audit 2026-05-21
**Abhängigkeit:** Keine — alle Pakete sofort und unabhängig machbar
**Folge-Auftrag:** `FEATURE_REQUEST_MW_V2B.md` (Hooks, Schlankheitskur, Doku) — ERST NACH v2a

---

## OVERRIDE — Effizienz-Pflicht

Alle Pakete unten sind logische ARBEITSPAKETE, keine separaten Sessions.
Alles in EINER Session|Ein Commit pro Paket|EIN Sammel-HANDOVER am Ende.
Session-Auffüll-Regel gilt: wenn < 300k Token nach Paket 3 → weiter mit v2b.

---

## Kontext (für Coda — NICHT überspringen)

Empirische Forschung (IFScale-Benchmark, 2025) belegt:
- 500 Regeln → max 68% Accuracy bei Frontier-Modellen
- Ab 200 Regeln: Fehler werden zu **Auslassungsfehlern** (lautloses Ignorieren)
- Professionelle Systeme (Devin, SWE-Agent, Aider) arbeiten ALLE mit Progressive Disclosure

Unser Problem: `lessons_ZERBERUS.md` allein = ~316 KB ≈ 80k Token.
Bootstrap-Overhead pro Session: ~100-170k Token (25-42% des Budgets).
Das System produziert mehr Regeln als es befolgen kann.

Dieser FR eliminiert den größten Token-Ballast durch drei unabhängige Maßnahmen.

---

## Paket 1: Lessons-Archiv mit TF-IDF-Retrieval

### Was
`scripts/lessons_lookup.py` — CLI-Tool das relevante Lessons per Keyword findet.

### Warum TF-IDF (nicht FAISS/Embeddings)
- Kein VRAM-Bedarf (RTX 3060 ist durch Zerberus-Inference voll belegt)
- Exakte Keyword-Matches bei technischen Begriffen (Funktionsnamen, Patch-Nummern) schlagen semantische Embeddings
- scikit-learn ist bereits installiert (Zerberus-Dependency)
- Matrix-Aufbau: Millisekunden, kein Model-Download

### Wie
- Liest `lessons_ZERBERUS.md` (oder jede `lessons_*.md`)
- Splittet nach Lesson-Blöcken (Trennzeichen: `---` oder `## `)
- Baut TF-IDF-Matrix mit `sklearn.feature_extraction.text.TfidfVectorizer`
- CLI-Interface:
  ```
  python scripts/lessons_lookup.py "Gist-Sync"           → Top-3 Lessons (~500 Token)
  python scripts/lessons_lookup.py --task "CSS migration" → Task-bezogene Suche
  python scripts/lessons_lookup.py --all                  → Dump (Fallback, nur für Debug)
  ```
- Output: Plaintext auf stdout, sofort im Coda-Kontext sichtbar

### Integration in CLAUDE_ZERBERUS.md
Bestehenden Schritt 04 ersetzen:

**Alt:**
```
04 — Lessons konsultieren (lessons_ZERBERUS.md komplett lesen)
```

**Neu:**
```
04 — Lessons konsultieren: `python scripts/lessons_lookup.py --task '<aktuelle Aufgabe>'` ausführen|NUR die zurückgegebenen Lessons lesen|NICHT die gesamte Datei laden|Bei 0 Treffern: Aufgabe ist neu, kein Lesson-Kontext nötig
```

### WICHTIG — Trigger-Überlegung für v2b
In diesem FR ist der Lookup ein manueller CLI-Aufruf (Schritt 04 im Session-Zyklus).
Das ist eine weiche Regel — unter Kontextlast ignorierbar.
In v2b (Hooks) wird der Lookup als SessionStart-Hook verdrahtet → mechanisch erzwungen.
Hier trotzdem schon bauen, weil: (a) sofortiger Token-Gewinn, (b) Hook braucht ein fertiges Tool.

### Akzeptanzkriterien
- [ ] `python scripts/lessons_lookup.py "uvicorn reload"` gibt ≤5 relevante Lessons zurück
- [ ] Output ist < 2000 Token (verifizieren per `wc -w`)
- [ ] `lessons_ZERBERUS.md` wird im Session-Zyklus NICHT mehr komplett geladen
- [ ] CLAUDE_ZERBERUS.md Schritt 04 ist angepasst
- [ ] Script funktioniert auch mit `lessons_KONSOLIDIERT.md` und `GLOBAL_LESSONS.md`

---

## Paket 2: Session-End-Automation (`scripts/session_end.ps1`)

### Was
Ein einziges Script das ALLE mechanischen Session-End-Aufgaben bündelt.

### Wie
```powershell
# session_end.ps1 — Reihenfolge:
# 1. git add + commit (falls uncommitted changes)
# 2. sync_repos.ps1 aufrufen (Zerberus → Ratatoskr, Lessons → Claude)
# 3. Gist-PATCH: Zerberus-Gist (HANDOVER, LESSONS, STATUS, MJOLNIR, REPO_INDEX)
# 4. Gist-PATCH: Claude-KB-Gist (GLOBAL_LESSONS, WORKFLOW_SUMMARY)
# 5. huginn_kennt_zerberus.md → docs/RAG Testdokumente/ kopieren
# 6. verify_sync.ps1 aufrufen
# 7. Ergebnis-Summary auf stdout (was synced, was fehlte, was übersprungen)
```

### Was Coda weiterhin manuell macht
- HANDOVER schreiben (kreative Arbeit)
- SUPERVISOR updaten (kreative Arbeit)
- Lessons formulieren (kreative Arbeit)
- mjolnir.md schreiben (kreative Arbeit)
- Committen

Dann EIN Befehl: `.\scripts\session_end.ps1` — alles Mechanische ist automatisch.

### Fehlerbehandlung
- Gist-PATCH fehlgeschlagen → Warnung ausgeben, NICHT abbrechen (Netzwerk kann down sein)
- sync_repos.ps1 nicht vorhanden → Warnung, skip
- verify_sync.ps1 nicht vorhanden → Warnung, skip
- Kein uncommitted changes → Skip Schritt 1, kein Fehler

### Akzeptanzkriterien
- [ ] `.\scripts\session_end.ps1` läuft ohne Fehler durch (Happy Path)
- [ ] Gist-Timestamps sind nach Lauf aktueller als vorher
- [ ] Bei Netzwerk-Fehler: Warnung, kein Crash
- [ ] Ergebnis-Summary zeigt klar was passiert ist
- [ ] Script ist idempotent (zweimal hintereinander = kein Schaden)

---

## Paket 3: Stand-Anker SSOT (`STAND.json` + Propagierung)

### Was
Eine zentrale JSON-Datei als Master für alle Stand-Anker. Ein Script propagiert in alle Zieldateien.

### STAND.json Format
```json
{
  "patch": "P220",
  "phase": "5b",
  "datum": "2026-05-21",
  "tests": "2900+",
  "commits": {
    "zerberus": "da0e5a0",
    "ratatoskr": "6bf7936",
    "claude": "9a47b1d"
  }
}
```

### Propagierungs-Script
`scripts/propagate_stand.py`:
- Liest `STAND.json`
- Sucht+Ersetzt Stand-Anker in:
  - `SUPERVISOR_ZERBERUS.md` (Header-Block)
  - `docs/PROJEKTDOKUMENTATION.md` (Header-Block)
  - `README.md` (Badge/Status-Zeile)
  - `huginn_kennt_zerberus.md` (Stand-Zeile)
  - `docs/RAG Testdokumente/huginn_kennt_zerberus.md` (Spiegel)
- Regex-basiert: sucht Pattern wie `Patch \d+` oder `P\d+` und ersetzt mit aktuellem Wert
- Dry-Run-Modus: `python scripts/propagate_stand.py --dry-run` zeigt was sich ändern würde

### Workflow-Änderung
Coda aktualisiert nach jedem Patch NUR `STAND.json`, dann:
```
python scripts/propagate_stand.py
```
Fertig. Keine 6 Dateien manuell anfassen.

### Akzeptanzkriterien
- [ ] `STAND.json` existiert mit aktuellem Stand
- [ ] `python scripts/propagate_stand.py` aktualisiert alle 5 Zieldateien
- [ ] `--dry-run` zeigt Diff ohne zu schreiben
- [ ] Patch-Nummer ist nach Lauf in allen Dateien identisch
- [ ] Script ist idempotent

---

## Erwartete Token-Einsparung (konservativ)

| Maßnahme | Vorher (Token) | Nachher (Token) | Ersparnis |
|---|---|---|---|
| Lessons komplett laden (Paket 1) | ~80.000 | ~2.000 | **~78.000** |
| Session-End manuell (Paket 2) | ~20.000 | ~3.000 | **~17.000** |
| Stand-Anker 6× editieren (Paket 3) | ~15.000 | ~1.000 | **~14.000** |
| **GESAMT pro Session** | | | **~109.000** |

---

## Was NICHT geändert wird

- HANDOVER bleibt handgeschrieben
- mjolnir.md bleibt handgeschrieben
- Lessons werden weiterhin geschrieben — nur nicht mehr komplett geladen
- Gist-System bleibt — wird nur mechanisch synced
- CLAUDE_ZERBERUS.md wird hier NICHT entrümpelt (→ v2b)
- Keine Hooks (→ v2b)
- Keine Playbooks (→ v2b)
