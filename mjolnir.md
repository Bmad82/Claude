# mjolnir.md — Claude (Meta-Repo)

```
STATUS|FERTIG|AUFTRAG: ordner-cleanup|FORTSCHRITT: 6/6 Schritte | EINE Session|NÄCHSTE SESSION: FEATURE_REQUEST_supervisor-aufbau.md liegt bereit (untracked, separater Auftrag)
```

**STATUS:** FERTIG
**AUFTRAG:** `ordner-cleanup` — INVENTORY-Mapping ausgeführt (gated, reversibel). FR umbenannt zu `_erledigt/FEATURE_REQUEST_ordner-cleanup_ERLEDIGT.md`.
**FORTSCHRITT:** Alle 6 Schritte in EINER Session. Restore-Punkt → GLOBAL_LESSONS-Merge → Absolutpfad-Gate → Moves → REPO_INDEX/README/DECISIONS nachgezogen → commit/push → mjolnir.
**NÄCHSTE SESSION:** `FEATURE_REQUEST_supervisor-aufbau.md` ist der nächste, eigenständige Auftrag (liegt untracked im Root, bewusst nicht angefasst). Optional offen: Design/Intake-Ablage + LESSONS_KONSOLIDIERT-Extraktion (siehe DECISIONS_PENDING).

---

## Restore-Punkt (Reversibilität)

- Branch `cleanup/ordner-cleanup`, ff-gemergt auf `main`.
- Pre-Cleanup `main` = `4321adb`. Baseline-Commit (Ist-Stand vor Moves) = `408ec48`.
- Vollständiger Rückbau: `git reset --hard 4321adb` (verwirft den gesamten Cleanup).
- Es wurde nur EIN File hart gelöscht: `workflow/__pycache__/*.pyc` (regenerierbar, gitignored). Alles andere ist verschoben/archiviert, nichts verloren.

---

## Was Chris physisch prüfen sollte (Stichprobe)

- Root ist von ~28 auf 13 Dateien runter — kurz drüberschauen ob die Struktur passt.
- `schaltplan/fabrik_meta_workflow.html` im Browser öffnen: lädt es die JSON noch (relativer fetch, beide liegen jetzt zusammen in `schaltplan/`)? Sollte unverändert funktionieren.
- Gist-Abgleich (Claude-KB-Gist) bewusst NICHT angefasst — laut FR macht Chris den Repo/Gist-Abgleich später selbst.

---

## Auftragshistorie (kurz)

INVENTORY-Mapping ausgeführt: Schaltplan-Ablage `schaltplan/` neu, `_archive/` für abgelöste Files neu, `_drafts_gist/` aufgelöst. 17 `git mv`-Moves (History erhalten), 1 `.pyc` gelöscht. GLOBAL_LESSONS_KONTEXT-Prosa in GLOBAL_LESSONS zurückgemergt (per `comm -23` verifiziert, keine Lesson verloren), dann KONTEXT archiviert. Namens-Kollision abgefangen: Root-`FEATURE_REQUEST_CLAUDE_ERLEDIGT.md` (mw-v2a) hätte die gleichnamige `_erledigt/`-Datei (faulheits-catch) überschrieben → kollisionssicher zu `FEATURE_REQUEST_mw-v2a-kontextentlastung_ERLEDIGT.md` umbenannt. Absolutpfad-gepinnte Files (GLOBAL_LESSONS, KODEX, DECISIONS_PENDING, BOOTSTRAP, GIST_LINK, DESIGN) am Root belassen → kein Template-Pfad gebrochen. REPO_INDEX voll re-synct (alte Drift mitgeheilt), README-Struktur + DECISIONS_PENDING aktualisiert.
