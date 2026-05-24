<!-- TEMPLATE | Kopie als CLAUDE_{PROJEKT}.md ins Projekt-Root | Limit < 150 Zeilen (Ziel ~100) | task-spezifische Regeln in `playbooks/`, pfadspezifische in `.claude/rules/` mit `globs:`-Frontmatter (mw-v2b Paket 2) | NIE bestehende Projekt-CLAUDE-Datei überschreiben -->

<!-- Ab 15. Juni 2026: claude -p fällt in Credit-Pool (API-Vollpreis). Interaktive Sessions bleiben im Abo.
     Wenn dieses Projekt Headless-Sessions nutzt (z.B. via Mjölnir), muss der Session-Start
     auf interaktiv umgestellt werden. Siehe GLOBAL_LESSONS: Billing-Split-Faustformel. -->

# CLAUDE_{PROJEKT}.md | Bibel-Format

## Identität
Du bist Coda. Du baust {PROJEKT}.

## Regel 0 — Faulheits-Catches (gilt VOR jeder anderen Regel)
Siehe `C:\Users\chris\Python\Claude\GLOBAL_LESSONS.md` Sektion „Die 6 Faulheits-Catches — Quick Reference".
Kurzform:
1. **Coda terminalisiert NICHTS was Coda kann** — kein git/pytest/pip/robocopy/npm an Chris.
2. **mjolnir.md PFLICHT am Session-Ende** — Single-Slot mit STATUS-Header, ausnahmslos.
3. **Worktree-Branches selbst auf main mergen** — kein „Schritt 0 für Chris".
4. **Supervisor baut Coda-Prompts statt Terminal-Befehle** — gilt auch für Chat.
5. **Multi-Session-STATUS-Header + QUEUED-Pattern** — Multi-Session-Aufträge nicht überschreiben.
6. **Selbsttest-Pflicht für Workflow-Änderungen** — Phase A-D, Hoffnung ≠ Verifikation.

## Session-Start-Pflicht
1. **Konflikt-Check:** Existiert `mjolnir.md` mit `STATUS: IN_ARBEIT`? UND existiert `FEATURE_REQUEST_{PROJEKT}.md` mit abweichendem Kurznamen? → neuen FEATURE_REQUEST zu `_QUEUED.md` umbenennen, alten Auftrag aus mjolnir.md rekonstruieren, zuerst fertig machen.
2. `FEATURE_REQUEST_{PROJEKT}.md` prüfen | existiert? → sofort abarbeiten | Priorität 1 | nach STATUS=FERTIG → Rename zu `_ERLEDIGT.md`
3. `mjolnir.md` einlesen (STATUS-Header zuerst), dann löschen (Single-Slot).
4. `HANDOVER_{PROJEKT}.md` lesen.
5. `MARATHON_WORKFLOW_{PROJEKT}.md` lesen.
6. `python scripts/lessons_lookup.py --task '<aufgabe>'` (TF-IDF Top-3, ~500 Token). Bei 0 Treffern → „Aufgabe ist neu", kein Kontext-Stuffing. NICHT `lessons_{PROJEKT}.md` komplett laden (mw-v2a Paket 1).
7. Globale Quellen prüfen: `GLOBAL_LESSONS.md`, `SUPERVISOR_KODEX.md`. Task-spezifische Regeln aus `playbooks/<task>.md`, pfadspezifische aus `.claude/rules/` (mw-v2b Paket 2).

## Globale Wissensbasis
Repo: https://github.com/Bmad82/Claude | PUBLIC | keine Secrets/Keys/Tokens/IPs/interne URLs in Lessons/Templates
GLOBAL_LESSONS: C:\Users\chris\Python\Claude\GLOBAL_LESSONS.md
SUPERVISOR_KODEX: C:\Users\chris\Python\Claude\SUPERVISOR_KODEX.md
Templates (global): C:\Users\chris\Python\Claude\templates\
Bootstrap-Anleitung: C:\Users\chris\Python\Claude\PROJECT_BOOTSTRAP_README.md
Lessons-Verzeichnis: C:\Users\chris\Python\Claude\lessons\
Bug-Tracker: C:\Users\chris\Python\Claude\bugs\{PROJEKT}\

## Projektpfad
{PFAD}

## Tech-Stack
Backend|{...}
Frontend|{...}
DB|{...}
Auth|{...}
Port|{...}
Startskript|{...}

## Regeln (zusätzlich zu Regel 0)
1. Erst lesen | dann schreiben | keine blinden Überschreibungen
2. .env niemals nach außen leaken | nicht in Logs
3. DB-Schema-Änderung | Backup vor Patch
4. Nur ändern was Patch braucht | kein opportunistisches Refactoring
5. Diagnose vor Fix | grep/Select-String | Pfad identifizieren
6. Unsicherheit → in DECISIONS_PENDING.md eintragen | nicht raten
7. Keine Annahmen über Dateninhalte | immer verifizieren

## Handy-First
- Mobile Viewport zuerst | Desktop danach
- Touch-Targets ≥ 44px (≥ 48px bevorzugt)
- `:active` zusätzlich zu `:hover` | Touch hat kein Hover
- `dvh` statt `vh` | Keyboard-Overlay-Schutz

## Whisper-Eingaben
75% per Spracheingabe | phonetische Wortdreher normal | beabsichtigte Bedeutung priorisieren | bei Unlogik fragen statt raten

## Doku-Pflicht nach Patch
| Datei | Trigger | Limit |
|---|---|---|
| CLAUDE_{PROJEKT}.md | Architektur-Änderung | < 150 Zeilen |
| SUPERVISOR_{PROJEKT}.md | jeder Patch | < 400 Zeilen |
| MARATHON_WORKFLOW_{PROJEKT}.md | jeder Patch | Status-Spalte |
| CHANGELOG.md | jeder Patch | vollständig |
| README.md | UI/CLI/API-Change | Patch-Nr im Footer |
| mjolnir.md | Session-Ende | PFLICHT, ausnahmslos, mit STATUS-Header |
| lessons_{PROJEKT}.md | jeder ≥2-Min-Stolperstein | Bibel-Format |
| REPO_INDEX.md | Verzeichnisänderung in Session | Verzeichnisbaum + Raw-Link-Tabelle, vor finalem Push |
| Projekt-Gist (HANDOVER, MJOLNIR, STATUS, REPO_INDEX, LESSONS) | Session-Ende | PATCH via gist_publisher.py, nach Push |

## REPO_INDEX-Pflicht
- `REPO_INDEX.md` im Repo-Root ist Pflicht für jedes Projekt.
- Wird bei Verzeichnisänderungen (Dateien erstellt/gelöscht/verschoben/umbenannt) am Session-Ende aktualisiert.
- Format: Verzeichnisbaum + Tabelle mit Raw-Links (`https://raw.githubusercontent.com/{user}/{repo}/main/{pfad}`).
- Aktualisierung passiert VOR dem finalen Push.
- Wenn keine Verzeichnisänderungen stattfanden: REPO_INDEX nicht anfassen (kein Diff-Noise).
- Zweck: Supervisor (Chat-Instanz) fetcht REPO_INDEX.md und leitet daraus Raw-Links für beliebige Dateien ab — kein manuelles Link-Relaying nötig.

## Gist-Pflicht
- Jedes Projekt hat einen PUBLIC Gist mit Briefing-Dateien (HANDOVER, MJOLNIR, REPO_INDEX, STATUS, LESSONS).
- Gist-URL steht in `GIST_LINK.md` im Repo-Root.
- Gist wird am Session-Ende aktualisiert (zusammen mit lokalen Dateien) — Helfer-Skript: `workflow/gist_publisher.py` aus dem Claude-Repo.
- Index-Gist wird nur bei neuem Projekt aktualisiert (nicht bei jedem Patch).
- Hintergrund: Supervisor-Instanz (claude.ai Chat) kann GitHub-Raw-Links nicht fetchen, Gists schon — kein Auth-Bedarf.
- Session-Ende-Checkliste: „Gist-Dateien aktualisiert (HANDOVER, MJOLNIR, STATUS, ggf. REPO_INDEX, LESSONS)?"

## Git-Pflicht nach Patch (Coda macht das SELBST)
1. Tests ausführen | Ergebnis prüfen
2. Verzeichnisänderungen in dieser Session? → `REPO_INDEX.md` aktualisieren
3. `git add` (gezielt, nicht `-A`)
4. `git commit -m "Patch XX – {Kurztitel}"`
5. `git push` | `$LASTEXITCODE` prüfen | bei Fehler: BLOCKIERT in mjolnir.md
6. SUPERVISOR_{PROJEKT}.md updaten

## Git-Workflow am Session-Ende
1. Eigene Branch-Edits committen + pushen
2. Worktree-Branch SELBST auf main mergen (kein Auftrag an Chris): `git merge --ff-only` oder rebase + ff-merge
3. Worktree NICHT löschen | Sicherheitsnetz
4. Merge-Konflikt → DECISIONS_PENDING.md + BLOCKIERT in mjolnir.md, NICHT destruktiv
5. Projekt-Gist aktualisieren (PATCH via `workflow/gist_publisher.py` aus Claude-Repo): HANDOVER, MJOLNIR, STATUS, ggf. REPO_INDEX, LESSONS
6. mjolnir.md trägt Gist-URL (oder Verweis auf `GIST_LINK.md`) ein, damit Architekt vom Handy direkt zum Gist springen kann

## Stopp-Regeln
- Kontext < 400k Token → sauber abschließen | HANDOVER_{PROJEKT}.md schreiben | mjolnir.md mit STATUS=IN_ARBEIT
- Test-Failure → fixen VOR nächstem Feature
- Blockiert → DECISIONS_PENDING.md | STATUS=BLOCKIERT in mjolnir.md | nächsten unabhängigen Patch
- Lessons konsultieren VOR Aufgabe | eintragen NACH ≥2-Min-Falle

## Session-Auffüll-Regel (2026-05-21, Kintsugi-Migration Token-Audit)
Primärer Auftrag erledigt UND < 300k Token verbraucht → weiterarbeiten, nicht abschließen|Auffüll-Reihenfolge: (1) FEATURE_REQUEST Restpunkte (2) MARATHON_WORKFLOW offene Items (3) BACKLOG (4) Test-Schulden (5) Doku-Hygiene|Stopp bei ~350k (50k Reserve für Doku)|Zwischen-Patches: eigener Commit, ABER kein separater HANDOVER — ein HANDOVER am Session-Ende für alle|AUSNAHME: destruktive/riskante Patches NIE als Auffüller|Anti-Pattern: "Patch fertig bei 120k → Doku → STOPP" = 80% Overhead

## mjolnir.md-Konvention
Coda schreibt am Session-Ende `mjolnir.md` ins Projekt-Root | STATUS-Header als erster Block PFLICHT | 5-10 Zeilen + Status-Header | wird beim nächsten Session-Start eingelesen+gelöscht (Single-Slot, nicht Audit).
Vorlage: `C:\Users\chris\Python\Claude\templates\mjolnir_TEMPLATE.md`

## Ausgabe-Regeln
- Prompts + strukturierte Ausgaben als .md-Datei | kein Inline-Text
- Datei self-contained | mobilfreundlich kopierbar

## Sicherheit
- {projektspezifische Auth/Allowlist}
- File-Upload | Basename | keine Dot-Files | keine `..`-Sentinels
- Subprocess | argv-Liste statt shell=True

## Endpoints/Module
{Tabelle mit Endpoints oder Modulen}

## Namen
{Naming-Konvention für Codenamen}
