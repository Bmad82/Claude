# FEATURE_REQUEST — Marathon Workflow v2b: Mechanische Durchsetzung & Alignment

**Kurzname:** mw-v2b-durchsetzung
**Projekt:** Claude (Meta-Repo) + Zerberus (Pilot)
**Priorität:** HOCH (aber nach v2a)
**Datum:** 2026-05-21
**Grundlage:** Deep Research PDF "LLM Regelbefolgung" + Supervisor-Audit 2026-05-21
**Abhängigkeit:** v2a MUSS abgeschlossen sein (Lessons-Lookup-Tool + session_end.ps1 existieren)
**Vorgänger:** `FEATURE_REQUEST_MW_V2A.md` bzw. `_ERLEDIGT.md`

---

## OVERRIDE — Effizienz-Pflicht

Alle Pakete unten sind logische ARBEITSPAKETE, keine separaten Sessions.
Alles in EINER Session|Ein Commit pro Paket|EIN Sammel-HANDOVER am Ende.
Session-Auffüll-Regel gilt.

---

## Kontext

v2a hat die Token-Last um ~109k/Session reduziert (Lessons-RAG, session_end.ps1, STAND.json).
Dieser FR macht die Gewinne **mechanisch unumgehbar** (Hooks) und räumt historische Altlasten auf.

Drei Säulen:
1. Claude Code Hooks → weiche Regeln werden harte Constraints
2. Bibel-Schlankheitskur + Playbooks → CLAUDE_ZERBERUS.md von ~15k auf ~5k Token
3. Zerberus-Marathon-Alignment → Naming, Struktur, Lessons-Zuordnung bereinigen

---

## Paket 1: Claude Code Hooks (`.claude/settings.json`)

### RECHERCHE ZUERST — vor jeder Implementierung

Die Deep Research PDF beschreibt Hooks konzeptionell. Exakte Syntax muss verifiziert werden.

**Schritt 0 (Pflicht):**
```bash
cat ~/.claude/settings.json 2>/dev/null || echo "Datei existiert nicht"
cat .claude/settings.json 2>/dev/null || echo "Datei existiert nicht"
```
Dann Claude Code Docs konsultieren: https://code.claude.com/docs/en/hooks

**Erst wenn die Syntax verifiziert ist, weitermachen. Bei Unklarheit: Paket überspringen, in DECISIONS_PENDING parken, mit Paket 2 weitermachen.**

### SessionStart-Hook: Lessons auto-inject
```
Trigger: SessionStart
Aktion: python scripts/lessons_lookup.py --task "$(git branch --show-current)"
Zweck: Relevante Lessons werden automatisch in den Kontext injiziert
       Coda muss Schritt 04 nicht mehr manuell ausführen
       Weiche Regel → mechanischer Automatismus
```

### PreToolUse-Hook: Infrastruktur-Dateien schützen
```
Trigger: PreToolUse (Matcher: Edit|Write)
Aktion: python scripts/validate_edit.py
Zweck: Blockiert Edits an geschützten Dateien:
       - GLOBAL_LESSONS.md (nur Supervisor darf ändern)
       - CLAUDE_GLOBAL.md (nur Reasoning-Modell nach Backup)
       - Templates mit _TEMPLATE_ im Namen
       Exit-Code 2 → harte Blockade
```

### SessionEnd-Hook: Pflichten-Check
```
Trigger: SessionEnd
Aktion: python scripts/session_end_check.py
Prüft:
  - [ ] mjolnir.md existiert und ist nicht leer
  - [ ] HANDOVER wurde in dieser Session geändert (git diff)
  - [ ] Stand-Anker-Konsistenz (STAND.json vs. SUPERVISOR Patch-Nummer)
  - [ ] Gist-Sync-Timestamp (Warnung wenn veraltet)
Gibt: Fehler-Text auf stdout den Coda sieht → kann nicht ignoriert werden
```

### validate_edit.py
```python
# Liest stdin (JSON mit geplanter Aktion von Claude Code)
# Prüft Zieldatei gegen Schutzliste
# Exit 0 = erlaubt, Exit 2 = blockiert
# stdout bei Blockade: {"permissionDecision": "deny", "reason": "..."}
```

### Akzeptanzkriterien
- [ ] `.claude/settings.json` enthält alle drei Hooks
- [ ] SessionStart injiziert Lessons (verifizieren per Kontext-Check)
- [ ] Edit auf `CLAUDE_GLOBAL.md` wird blockiert (Exit 2)
- [ ] SessionEnd meldet Fehler wenn mjolnir.md fehlt
- [ ] WENN Hook-Syntax unklar: Paket sauber in DECISIONS_PENDING geparkt mit Recherche-Ergebnis

---

## Paket 2: CLAUDE_ZERBERUS.md Schlankheitskur + Playbooks

### Analyse-Schritt (Pflicht, vor Änderungen)
Aktuelle CLAUDE_ZERBERUS.md lesen und kategorisieren:
- **Kern-Bibel** = Regeln die IMMER gelten, unabhängig vom Task
- **Task-spezifisch** = Regeln die nur bei bestimmten Dateitypen/Modulen relevant sind

### Kern-Bibel (Ziel: max 30-40 Regeln, ~5k Token)
Was reingehört:
- Commit-Convention, Branch-Policy
- Test-Pflicht, Stopp-Schwelle, Auffüll-Regel
- Session-Zyklus (13 Schritte, kompakt)
- Oberstes Gebot (kein Terminal für Chris)
- Faulheits-Catches (die 6 Kern-Catches als Pipe-Zeilen)
- Doku-Pflicht-Tabelle (welche Datei nach Patch, kompakt)
- Verweis auf Playbooks + Lessons-Lookup

### Playbooks (Verzeichnis `playbooks/`)
Task-spezifische Regeln auslagern:

```
playbooks/
├── css_migration.md      — Heilige Anker, Class-Annex, Foundation-Token-Fallback
├── rag_pipeline.md       — DualEmbedder, Cross-Encoder, Chunk-Hygiene, Query-Expansion
├── auth_security.md      — /v1/-Bypass, Dictate-Header, JWT-Workarounds
├── frontend_mobile.md    — Touch-Targets, :hover→:active, viewport, PWA-Cache-Bust
├── session_lifecycle.md  — Doku-Pflichten als Checkliste, Gist-Sync, Stand-Anker
└── database.md           — Alembic, Idempotenz, Backup-Pflicht, Schema-Änderungen
```

Jedes Playbook:
- Max 50 Zeilen, Bibel-Format
- Header mit Trigger-Beschreibung: "Lade dieses Playbook wenn du an `*.css` oder `nala.py`-Frontend arbeitest"
- Kein Prosa-Ballast — reine Handlungsanweisungen

### `.claude/rules/` mit globs-Frontmatter (aus Deep Research PDF)
Zusätzlich zu Playbooks: pfadspezifische Regeln die Claude Code automatisch lädt:

```yaml
# .claude/rules/frontend.md
---
globs: "**/*.css, **/nala.py, **/hel.py"
---
- Touch-Target minimum 44px|:hover immer mit :active doppeln|Cache-Bust ?v=NN an CSS/JS-URLs
- backdrop-filter braucht Fallback für ältere Mobile-Browser
```

```yaml
# .claude/rules/rag.md
---
globs: "**/rag/*.py, **/orchestrator.py"
---
- Code-Pfad prüfen: legacy.py vs orchestrator.py — welcher führt aktiven Traffic?
- RAG-Skip-Logik: AND-verknüpft, nicht OR|Cross-Encoder-Reranker ist aktiv
```

**WICHTIG:** `globs:` verwenden, NICHT `paths:`. `paths:` ist buggy und wird lautlos ignoriert (dokumentierter Bug, GitHub Issue #17204).

### Akzeptanzkriterien
- [ ] CLAUDE_ZERBERUS.md ist < 150 Zeilen (Ziel: ~100)
- [ ] `playbooks/` Verzeichnis existiert mit mindestens 4 Playbooks
- [ ] `.claude/rules/` hat mindestens 2 Regel-Dateien mit `globs:`-Frontmatter
- [ ] Kein Inhalt ging verloren — alles ist in Playbooks oder rules/ gewandert
- [ ] Kern-Bibel enthält Oberstes Gebot + alle 6 Faulheits-Catches

---

## Paket 3: Zerberus-Marathon-Alignment (aus Supervisor-Audit)

### 3a: Naming-Bereinigung Hypervisor → Supervisor
- `HYPERVISOR.md` → `SUPERVISOR_ZERBERUS.md` (git mv)
- Alle Referenzen in CLAUDE_ZERBERUS.md anpassen
- Alle Referenzen in lessons_ZERBERUS.md anpassen
- Alle Referenzen in MARATHON_WORKFLOW_ZERBERUS.md anpassen

### 3b: SUPERVISOR_ZERBERUS.md Entschlackung
Aktuell: ~269 Zeilen, davon ~200 Zeilen Patch-Historie (Patches 66-99).
Eigene Regel sagt: "Erledigte Einträge raus."

- Patches 66-95 → komplett raus (leben in PROJEKTDOKUMENTATION.md)
- Patches 96-99 → bleiben als "letzte 3-4 Patches"
- Aktueller Patch + Offene Items + Architektur-Warnungen + Langfrist-Vision + Dont's = das bleibt
- Ziel: < 80 Zeilen

### 3c: Lessons-Zuordnung klären
Dokumentieren (in MARATHON_WORKFLOW_ZERBERUS.md oder CLAUDE_ZERBERUS.md):
```
Coda liest: lessons_ZERBERUS.md (via TF-IDF-Lookup, NICHT komplett)
Supervisor liest: GLOBAL_LESSONS.md (im Claude-KB-Gist)
Archiv (niemand liest aktiv): LESSONS_KONSOLIDIERT.md
```

### 3d: Gist-Lessons Prosa-Split
Die GLOBAL_LESSONS.md im Claude-KB-Gist und die lessons_ZERBERUS.md im Zerberus-Gist enthalten pro Lesson Pipe-Zeilen + 15-30 Zeilen Prosa (Anlass, Backstop, Generalisierung).

Split in:
- `GLOBAL_LESSONS.md` → NUR Pipe-Zeilen (Coda-tauglich, ~30% der aktuellen Größe)
- `GLOBAL_LESSONS_KONTEXT.md` → Prosa-Blöcke mit Referenz per Lesson-ID (Chris-Archiv)

Gleiches für Zerberus:
- `lessons_ZERBERUS.md` → Pipe-only
- `lessons_ZERBERUS_KONTEXT.md` → Prosa-Archiv

### Akzeptanzkriterien
- [ ] `HYPERVISOR.md` existiert nicht mehr, `SUPERVISOR_ZERBERUS.md` existiert
- [ ] Keine Referenz auf "Hypervisor" mehr in CLAUDE_ZERBERUS.md oder lessons
- [ ] SUPERVISOR_ZERBERUS.md < 80 Zeilen
- [ ] Lessons-Zuordnung ist dokumentiert
- [ ] GLOBAL_LESSONS.md (Gist) enthält NUR Pipe-Zeilen
- [ ] lessons_ZERBERUS.md (Gist) enthält NUR Pipe-Zeilen
- [ ] Prosa-Kontext lebt in separaten `_KONTEXT.md`-Dateien

---

## Paket 4: Workflow-Dokumentation aktualisieren

### Was anpassen
- MARATHON_WORKFLOW_ZERBERUS.md:
  - Session-Zyklus Schritt 04: "Lessons-Lookup" statt "komplett lesen"
  - Session-Zyklus Schritt 12-13: "session_end.ps1 aufrufen" statt manuelle Schritte
  - Neue Sektion: Playbook-Verzeichnis mit Trigger-Beschreibungen
- MARATHON_WORKFLOW_TEMPLATE (Claude-Repo):
  - Playbook-Struktur einführen
  - `.claude/rules/`-Konzept dokumentieren
  - Lessons-Lookup als Standard-Schritt
- CLAUDE_PROJEKT_TEMPLATE (Claude-Repo):
  - Max 150 Zeilen-Regel verschärfen auf: "Kern-Bibel max 100 Zeilen + Verweis auf Playbooks"
  - `.claude/rules/` und `globs:`-Syntax dokumentieren (NICHT `paths:`)
- GLOBAL_LESSONS.md:
  - Neue Lesson: "Progressive Disclosure > Mega-Prompt|IFScale zeigt 68% max bei 500 Regeln|Lessons als RAG, Rules als globs-Lazy-Load|Kern-Bibel <100 Zeilen"
- Gist WORKFLOW_SUMMARY:
  - Session-Zyklus aktualisieren

### Anpassungen_11_05.2026 (Projekt-Knowledge)
Header einfügen:
```
> ⚠️ HISTORISCH — Teile revidiert. Aktueller Stand: MARATHON_WORKFLOW_DOKUMENTATION.md
> Insbesondere: Handover wurde NICHT eliminiert, CRASH_RESUME.md wurde nicht eingeführt.
```

### Akzeptanzkriterien
- [ ] Session-Zyklus in allen relevanten Dateien konsistent (Lessons-Lookup + session_end.ps1)
- [ ] Templates im Claude-Repo spiegeln die neue Architektur
- [ ] GLOBAL_LESSONS hat Progressive-Disclosure-Lesson
- [ ] Anpassungen-Datei ist als historisch markiert
- [ ] Gist WORKFLOW_SUMMARY ist aktuell

---

## Erwartete Token-Einsparung (zusätzlich zu v2a)

| Maßnahme | Vorher (Token) | Nachher (Token) | Ersparnis |
|---|---|---|---|
| CLAUDE_ZERBERUS.md (Paket 2) | ~15.000 | ~5.000 | **~10.000** |
| Lessons-Gist Prosa-Split (Paket 3d) | ~40.000 | ~12.000 | **~28.000** |
| SUPERVISOR Entschlackung (Paket 3b) | ~8.000 | ~2.500 | **~5.500** |
| Hooks eliminieren manuellen Aufwand (Paket 1) | ~5.000 | ~500 | **~4.500** |
| **GESAMT zusätzlich pro Session** | | | **~48.000** |

**Kumuliert mit v2a: ~157.000 Token/Session gespart.**
Bei 400k Budget = von ~42% Overhead auf ~10% Overhead.

---

## Reihenfolge innerhalb dieser Session

```
Paket 1 (Hooks) → Recherche zuerst, bei Unklarheit überspringen
Paket 2 (Schlankheitskur) → unabhängig von Hooks, sicher machbar
Paket 3 (Alignment) → unabhängig, sicher machbar
Paket 4 (Doku) → am Ende, fasst alles zusammen
```

---

## Was NICHT geändert wird

- HANDOVER bleibt handgeschrieben
- mjolnir.md bleibt handgeschrieben
- Gist-System bleibt (Bridge-Layer für Supervisor)
- Kintsugi-Philosophie bleibt
- Zerberus-Code wird NICHT angefasst — alles ist Workflow/Doku
