# GLOBAL_LESSONS — Marathon-Workflow

Universelle Lessons für ALLE Projekte, die den Marathon-Workflow nutzen (Coda + Supervisor + Mjölnir).
Projekt-spezifische Lessons gehören in `lessons/<projekt>_lessons.md`. Diese Datei nur für projektübergreifend gültige Regeln.

Format: jede Lesson eine `##` Sektion mit Datum + Anlass-Patch im Titel. Inhalt in Pipe-Format (`|`-getrennte Punkte), ggf. mit Begründung darunter. Nicht löschen — historische Lessons bleiben, neue oben anhängen.

---

---

## Progressive Disclosure: Playbooks + .claude/rules statt Kern-Bibel-Wachstum (2026-05-21, mw-v2b Paket 2)

CLAUDE_{PROJEKT}.md ist Kern-Bibel (OBERSTES GEBOT + Faulheits-Catches + Workflow), max 150 Zeilen Ziel 100|Task-spezifische Regeln wandern in `playbooks/<task>.md` (testing, rag_pipeline, auth_security, database, observability)|Pfad-getriggerte Regeln wandern in `.claude/rules/<rule>.md` mit YAML-Frontmatter `globs: [pattern, ...]` (NICHT `paths:` — falsche Syntax wird ignoriert)|Claude Code matched globs gegen die aktive Datei und laedt nur passende Regeln in den Kontext|Anlass: IFScale-Benchmark zeigt bei 500 Rules max 68% Befolgung — Kontext-Stuffing schadet|Opt-in-Pattern: `.claude/rules/` ist permission-protected, daher Rules-Templates in `docs/claude_rules/` + README mit Install-Instructions (Variante A committed / Variante B lokal). Konsistent mit Hooks-Verdrahtung in `scripts/HOOK_SETUP.md`

---

## Lessons-Retrieval statt Lessons-Komplett-Load (2026-05-21, mw-v2a Paket 1)

`lessons_*.md` darf NICHT mehr im Session-Start komplett geladen werden|TF-IDF-Retrieval per `scripts/lessons_lookup.py --task '<aufgabe>'` liefert Top-3 relevante Bloecke (~500 Tokens) statt 80k Token Full-Load|Bei 0 Treffern: explizite Meldung "Aufgabe ist evtl. neu", kein Kontext-Stuffing|scikit-learn TF-IDF reicht: exakte Keyword-Matches (Funktionsnamen, Patch-IDs) schlagen FAISS, kein VRAM-Bedarf, Matrix-Build in Millisekunden|Session-Start-Pflicht-Zeile entsprechend angepasst (CLAUDE_{PROJEKT}.md ersetzt `→ lessons_{PROJEKT}.md →` durch `→ python scripts/lessons_lookup.py --task '<aufgabe>' →`)

---

## Stand-Anker SSOT statt N-fach-Edit (2026-05-21, mw-v2a Paket 3)

Patch-Nummer / Phase / Tests / Commit-Hashes in 6 Dateien manuell pflegen = ~15k Token-Overhead pro Patch und N Stellen koennen voneinander driften|`STAND.json` als SSOT|`scripts/propagate_stand.py` liest JSON, baut HTML-Kommentar-Block (`<!-- STAND-ANKER:START -->` … `END`) und ersetzt ihn in allen Target-Dateien|HTML-Kommentar ist im gerenderten Markdown unsichtbar — kein UI-Noise|Idempotent (zweimal hintereinander = 0 Updates) plus `--dry-run` und `--check` (CI-Drift-Erkennung mit Exit 1)|Coda touched nach Patch nur `STAND.json` + ein Befehl, statt 6 Datei-Edits

---

## Session-End-Mechanik buendeln statt N-Schritte-Checklist (2026-05-21, mw-v2a Paket 2)

Session-End-Checkliste hatte 6 mechanische Schritte (commit, sync_repos, Gist-PATCH Projekt-Gist, Gist-PATCH Claude-KB-Gist, RAG-Spiegel, verify_sync)|Coda hatte 3 Sessions in Folge Schritt 12 (Gist-PATCH) uebersprungen (Gist-Sync-Faulheits-Catch)|Fix: `scripts/session_end.ps1` buendelt alle 6 Schritte, best-effort fuer Netzwerk-Fehler (Warnung statt Crash), Summary mit Farbcode am Ende|Coda macht weiterhin manuell (kreative Arbeit): HANDOVER schreiben, SUPERVISOR aktualisieren, Lessons formulieren, mjolnir schreiben — nur die mechanischen Schritte automatisiert|`workflow/gist_publisher.py` bekommt `--patch <gist_id> <staging_dir>` CLI (vorher nur `create`)

---

## Session-Auffüll-Regel (2026-05-21, Kintsugi-Migration Token-Audit)

Sessions schlossen bei ~120k ab obwohl 300k+ Budget frei war|3 Sessions à 120k statt 1 à 360k = 200k verschwendet|Mega-Patch-Ära (P122–P152) bewies: 24k/Patch bei Auffüll-Logik vs 100k+/Patch ohne|Fix: Primärer Auftrag fertig UND < 300k verbraucht → nächstes Item nehmen, Stopp bei ~350k|Nur sichere unabhängige Items als Auffüller, destruktive Ops nie|Ein HANDOVER am Ende statt pro Zwischen-Patch

---

## Gist-Sync (Schritt 12) ist gleichrangige Session-End-Pflicht (2026-05-21, Zerberus Gist-Drift)

Vier Sessions in Folge übersprangen Schritt 12 (Gist-PATCH) des Session-Zyklus|Local-Commit + Push wurden gemacht, Gist-PATCH fiel aus|Gist-Stand fror auf Stand B-aufraeumen (2026-05-18) ein, drei große Sessions später vollständig veraltet|Supervisor (Chat-Instanz) kann Raw-Links nicht fetchen — nur Gists — also ist Mjölnir-Round-Trip auf Supervisor-Seite kaputt sobald Gist-Sync ausfällt|Identisches Anti-Pattern-Profil wie B-072 (mjolnir.md): Pflicht-Schritt am Ende der Session-Liste → Token-knapp-Risiko-Zone → wird als erster gestrichen

---

## OBERSTES GEBOT (2026-05-16, Zerberus P-umzug)

Chris terminalisiert NICHTS was Coda kann|NIEMALS git/pytest/pip/robocopy/npm-Befehle an Chris delegieren|Coda merged Branches SELBST auf main + pusht SELBST vor Session-Ende|mjolnir.md enthält NUR was physisch unmöglich ist (Touch-Test, echtes Gerät, Docker Desktop UI)|Supervisor (Chat-Fenster) gibt KEINE Terminal-Befehle sondern baut Coda-Prompts (.md)|Verstoß = sofortige Korrektur

---

## mjolnir.md ist PFLICHT am Session-Ende (2026-05-16, Zerberus B-072)

mjolnir.md wird am Ende JEDER Session überschrieben — ausnahmslos|Alte Version wird IMMER ersetzt|Ohne mjolnir.md-Update ist der Mjölnir-Round-Trip kaputt|Chris kann sonst nicht erkennen ob ein Auftrag abgeschlossen ist|Session-Zyklus Schritt 10 ist NICHT optional|Wenn Schritt 10 fehlt hat Schritt 11 (Push) auch keinen Wert weil Chris nichts davon erfährt

---

## Worktree-Branches selbst auf main mergen (2026-05-16, Zerberus B-061)

Coda merged Worktree-Branches SELBST auf main vor Session-Ende|NIEMALS einen ungemergten Branch als "Schritt 0" in mjolnir.md an Chris delegieren|Das ist Terminal-Arbeit und fällt unter das OBERSTE GEBOT|Wenn ff-merge nicht möglich: rebase selbst durchführen oder Merge-Commit erstellen

---

## Supervisor-Verhalten: Coda-Prompts statt Terminal-Befehle (2026-05-16, Zerberus)

Wenn Chris ein Problem schildert das Coda lösen kann: Supervisor baut einen Coda-Prompt (.md-Datei) statt Chris Terminal-Befehle zu geben|Auch "nur ein Befehl" ist einer zu viel|Die Frage ist immer: "Kann Coda das selbst?" — Antwort ist in 95% der Fälle ja

---

## Multi-Session-Status-Header für mjolnir.md (2026-05-17, Zerberus B-mjolnir-multisession)

mjolnir.md hat IMMER einen STATUS-Header als ERSTEN Block|STATUS = FERTIG | IN_ARBEIT | BLOCKIERT|Pflichtfelder: STATUS, AUFTRAG, FORTSCHRITT, NÄCHSTE SESSION|Bei IN_ARBEIT: WARNUNG-Block fett oben + FEATURE_REQUEST NICHT umbenennen|Conditional Lifecycle: Rename FEATURE_REQUEST → _ERLEDIGT.md nur bei STATUS=FERTIG|QUEUED-Pattern: neuer FEATURE_REQUEST während IN_ARBEIT → _QUEUED.md, alter bleibt|Schlüsselwort-Whitelist ist maschinell auswertbar

---

## Selbsttest-Pflicht für Workflow-Änderungen (2026-05-17, Try_Faulheits_catch)

Workflow-Änderungen brauchen dreiphasigen Selbsttest VOR Push|Phase A: Pattern in der Quelle erzeugen|Phase B: zweite Session/Sub-Agent simuliert frische Coda-Aufnahme|Phase C: Konflikt provozieren und prüfen ob Schutz greift|Phase D: Aufräumen + Listing|Auf "Coda hat es ja so geschrieben" zu hoffen ist KEIN Selbsttest|Hoffnung ≠ Verifikation

---

## Naming-Konvention für FEATURE_REQUEST-Dateien (2026-05-17, aufraeumarbeiten-post-catch)

NAMING|FEATURE_REQUEST_{kurzname}.md|kurzname = kebab-case-aus-FEATURE_REQUEST-Frontmatter|niemals Projektname als Filename|bei Umbenennung Lifecycle: kurzname-suffix bleibt erhalten (*_ERLEDIGT.md, *_QUEUED.md)

---

## Die 6 Faulheits-Catches — Quick Reference

Kanonische Liste (Stand 2026-05-17, faulheits-catch-integration). Jeder Catch verweist zurück auf die ausführliche Sektion oben.

1. **OBERSTES GEBOT** — Coda terminalisiert nichts was Coda kann. Kein git/pytest/pip/robocopy/npm an Chris.
2. **mjolnir.md PFLICHT am Session-Ende** — Single-Slot-Round-Trip, ausnahmslos, gleichrangig mit HANDOVER und Push.
3. **Worktree-Branches selbst auf main mergen** — Kein „Schritt 0 für Chris", Coda macht ff-merge oder rebase selbst.
4. **Supervisor baut Coda-Prompts statt Terminal-Befehle** — Auch „nur ein Befehl" im Chat ist einer zu viel.
5. **Multi-Session-STATUS-Header + QUEUED-Pattern** — mjolnir.md mit STATUS-Block als erster Zeile, FEATURE_REQUEST während IN_ARBEIT wandert zu _QUEUED.md.
6. **Selbsttest-Pflicht für Workflow-Änderungen** — Dreiphasig (A Setup, B Replay, C Adversarial, D Cleanup). Hoffnung ≠ Verifikation.

Anlass-Blöcke + Lesson-Generalisierungen siehe oben in den jeweiligen Sektionen.

---

---

## Selbsttest-Pattern (Phase A/B/C/D — prosaisch)

Workflow-Änderungen sind erst dann „durch", wenn ihr Pattern in derselben Session einmal end-to-end gegen sich selbst antritt. Vier Phasen, fest:

**Phase A — Setup.** Erzeuge in `%TEMP%\<auftragsname>_test\` (oder `/tmp/...`) den Zustand der den neuen Schutz auslösen müsste. Beispiel: lege eine `mjolnir.md` mit STATUS=IN_ARBEIT an, kopiere ein Dummy-FEATURE_REQUEST hinein, ersetze alle `{PLATZHALTER}`. Verifiziere per Listing+Read, dass Setup wirklich den gewünschten Zustand zeigt — keine Platzhalter mehr, alle Pflichtfelder gefüllt.

**Phase B — Replay (frischer Kontext).** Starte einen Sub-Agent oder eine zweite Coda-Instanz mit dem Auftrag „du bist eine frische Session in diesem Verzeichnis, lies das Bootstrap-README und führe die Standardschritte aus". Beobachte ob:
- die globalen Files (GLOBAL_LESSONS, SUPERVISOR_KODEX) erkannt werden,
- die Templates gefunden+verstanden werden,
- keine Terminal-Befehle an Chris vorgeschlagen werden,
- bei vorhandenem STATUS=IN_ARBEIT der laufende Auftrag korrekt rekonstruiert wird statt überschrieben.

**Phase C — Adversarial (Konflikt provozieren).** Erzeuge gegen den frischen Zustand eine gegnerische Aktion. Beispiel: lege während IN_ARBEIT einen zweiten FEATURE_REQUEST mit anderem Kurznamen ab. Prüfe ob der Schutz greift (z.B. neuer Request landet in `_QUEUED.md`, alter bleibt unangetastet). Wenn Schutz NICHT greift, ist die Workflow-Änderung nicht fertig — zurück zu Setup, Lücke schließen.

**Phase D — Cleanup.** Lösche das gesamte Test-Verzeichnis. Verifiziere per Listing der Working-Tree-Root, dass kein `*_test*`, `bootstrap_test/`, `*_QUEUED.md` von Phase C übrig ist. Test-Artefakte dürfen nicht in den Commit wandern.

Surrogat-Regel: wenn echtes Multi-Session-Verhalten nur über Tage testbar ist (z.B. Token-Reset, Cache-TTL), dokumentiere das Surrogat (Sub-Agent simuliert Token-Reset) — aber kein Skip.

---

---

## Bibel-Format Cheat Sheet

„Bibel-Format" = Maschinen-lesbares Pipe-Format für Lessons, Templates, Status-Header. Eine Zeile pro Lesson, Felder mit `|` getrennt. Anlass+Begründung+Generalisierung in **fett-prosaischen Folge-Absätzen** darunter — Maschine ignoriert Prosa, Mensch findet Kontext.
