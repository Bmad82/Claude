# mjolnir.md — Claude (Meta-Repo)

```
STATUS|FERTIG|AUFTRAG: mw-v2a-kontextentlastung|FORTSCHRITT: 3 von 3 Pakete | EINE Coding-Session|NÄCHSTE SESSION: v2b (Hooks, Schlankheitskur, Doku) — bei Token-Budget direkt anschließend per Auffüll-Regel
```

**STATUS:** FERTIG
**AUFTRAG:** FEATURE_REQUEST_CLAUDE.md mw-v2a-kontextentlastung (Marathon-Workflow v2a, Kontextentlastung — Sichere Gewinne). Umbenannt zu `FEATURE_REQUEST_CLAUDE_ERLEDIGT.md`.
**FORTSCHRITT:** Alle drei Pakete in EINER Coding-Session geliefert (EIN Commit pro Paket per OVERRIDE-Direktive). Paket 1 (Zerberus `60e42a1`) — `scripts/lessons_lookup.py` TF-IDF + `CLAUDE_ZERBERUS.md` Session-Start umgestellt. Paket 2 (Zerberus `948c1d5`) — `scripts/session_end.ps1` Sammel-Bundle für 6 mechanische Schritte. Paket 3 (Zerberus `615abe4`) — `STAND.json` SSOT + `scripts/propagate_stand.py` + 5 STAND-Anker eingefügt. Claude-Repo Begleit-Commit: `workflow/gist_publisher.py` `--patch`-CLI + FR-Rename + drei neue Lessons in `GLOBAL_LESSONS.md`.
**NÄCHSTE SESSION:** Per FR-Folge-Auftrag `FEATURE_REQUEST_MW_V2B.md` (Hooks, Schlankheitskur `CLAUDE_ZERBERUS.md`, Doku-Refresh). Wenn Token-Budget < 300k erlaubt (Auffüll-Regel) direkt anschließend, sonst neue Session.

---

## Was diese Session war

Coda hat `FEATURE_REQUEST_CLAUDE.md` (mw-v2a-kontextentlastung) als Sammel-Auftrag mit drei unabhängigen Paketen abgearbeitet. Grundlage: Deep-Research-PDF "LLM Regelbefolgung" (IFScale-Benchmark: 500 Regeln → max 68% Accuracy bei Frontier-Modellen, Auslassungsfehler ab 200 Regeln) + Supervisor-Audit 2026-05-21. Ziel laut FR: ~109k Token Bootstrap-Overhead pro Session abbauen (Lessons-Komplett-Load + manuelles Session-End + 6× Stand-Anker-Pflege). Pilot-Projekt: Zerberus.

## Was geliefert wurde

**Paket 1 — `scripts/lessons_lookup.py` (Zerberus `60e42a1`)**

TF-IDF-Retrieval per scikit-learn (bereits Zerberus-Dependency) über alle `lessons_*.md` im Repo-Root. CLI mit `--task`, `--file`, `--top`, `--max-chars`, `--all`. Default Top-3, max 1200 Zeichen pro Block. Verifiziert: `"uvicorn reload"` → 3 Treffer ~500 Tokens statt 80k Full-Load. Bei 0 Treffern explizite Meldung "Aufgabe ist evtl. neu — kein Lesson-Kontext nötig". Funktioniert sowohl gegen `lessons_ZERBERUS.md` als auch gegen `GLOBAL_LESSONS.md` / `LESSONS_KONSOLIDIERT.md` (via `--file`). `CLAUDE_ZERBERUS.md` Session-Start-Pflicht-Zeile entsprechend angepasst.

**Paket 2 — `scripts/session_end.ps1` (Zerberus `948c1d5`)**

Sechs mechanische Session-End-Schritte in einem Aufruf: (1) git add+commit für uncommittete Doku/State-Files via Temp-File-F-Flag, (2) `sync_repos.ps1`, (3) Gist-PATCH Zerberus-Gist (HANDOVER + MJOLNIR + STATUS aus mjolnir-Header generiert + LESSONS + REPO_INDEX), (4) Gist-PATCH Claude-KB-Gist (GLOBAL_LESSONS + Optionals WORKFLOW_SUMMARY/TEMPLATES_INDEX/BOOTSTRAP_CHECKLIST wenn lokal vorhanden), (5) `huginn_kennt_zerberus.md` → `docs/RAG Testdokumente/` Hash-vergleich-basiert spiegeln, (6) `verify_sync.ps1`. Best-effort: Netzwerk-Fehler → Warnung statt Crash. Flags `-SkipCommit -SkipGist -DryRun -CommitMessage`. Farbcodierte Summary. Voraussetzung: `workflow/gist_publisher.py` mit neuem `--patch`-CLI (siehe Claude-Commit).

**Paket 3 — `STAND.json` + `scripts/propagate_stand.py` + 5 Anker (Zerberus `615abe4`)**

`STAND.json` als Single Source of Truth mit `patch`/`phase`/`datum`/`tests`/`commits.{zerberus,ratatoskr,claude}`. `propagate_stand.py` baut kanonischen HTML-Kommentar-Block (`<!-- STAND-ANKER:START -->` … `END`) und ersetzt ihn in 5 Target-Dateien. Modi: default = schreiben + Summary, `--dry-run` = Diff, `--check` = exit 1 bei Drift (CI-Modus). Idempotent verifiziert (zweimal hintereinander = 0 Updates). Drift-Detection verifiziert mit Test-Patch `P221_TEST`. Alle 5 Targets haben Anker-Block direkt nach H1.

**Claude-Repo Begleit-Änderungen** (in diesem Commit):
- `workflow/gist_publisher.py`: neuer `--patch <gist_id> <staging_dir>` CLI-Modus.
- `FEATURE_REQUEST_CLAUDE.md` → `FEATURE_REQUEST_CLAUDE_ERLEDIGT.md` (Marathon-Konvention).
- `GLOBAL_LESSONS.md`: drei neue Lessons oben — (a) Lessons-Retrieval statt Full-Load, (b) Stand-Anker SSOT statt N-Edit, (c) Session-End-Mechanik bündeln.

## Was nicht passiert ist

- Kein Hook-System (per FR-Verweis → v2b).
- Kein realer `session_end.ps1`-Live-Lauf (Gist-PATCH unter Echtbedingungen). DryRun und Staging-Build verifiziert, Happy-Path-Live-Test gehört in das nächste Session-Ende.
- Keine `CLAUDE_ZERBERUS.md`-Schlankheitskur (v2b).

## Akzeptanzkriterien

- P1: AK1 ✅ (3 Treffer) · AK2 ✅ (~500 Tokens) · AK3 ✅ · AK4 ✅ · AK5 ✅.
- P2: AK1 ✅ (DryRun grün) · AK3 ✅ · AK4 ✅ · AK5 ✅. AK2 (Gist-Timestamps) wird im nächsten realen Session-End belegt.
- P3: AK1 ✅ · AK2 ✅ · AK3 ✅ · AK4 ✅ · AK5 ✅.

---

<!--
LIFECYCLE-Notiz für Coda:

- STATUS=FERTIG  →  beim nächsten Session-Start: mjolnir.md einlesen, dann löschen. FEATURE_REQUEST_CLAUDE.md bereits zu _ERLEDIGT.md umbenannt mit drei-Paket-Bericht.
- STATUS=IN_ARBEIT  →  entfällt hier.
- STATUS=BLOCKIERT  →  entfällt hier.

mjolnir.md ist Single-Slot — genau EINE Datei zur Zeit, wird beim nächsten Session-Start gelesen + gelöscht.
-->
