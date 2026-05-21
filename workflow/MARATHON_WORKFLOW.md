# Marathon-Workflow — Architektur und Ablauf

Drei-Rollen-System zur Software-Entwicklung, bei dem der Architekt selbst kein Terminal anfasst und keinen Code schreibt. Optimiert für mobiles Arbeiten via Spracheingabe (Whisper).

## Die drei Rollen

| Rolle | Person/Instanz | Aufgabe |
|---|---|---|
| **Architekt** | Chris (Mensch) | Ideen, Richtung, Whisper-Eingaben — kein Code, kein Terminal |
| **Supervisor** | Claude im Chat-Fenster (claude.ai) | plant, prüft, schreibt Coda-Prompts als `.md`-Dateien |
| **Coda** | Claude Code (Terminal/CLI) | implementiert, testet, committet, merged, pusht — folgt dem Prompt |

**Trennung:** Architekt fasst kein Terminal an. Supervisor schickt keinen Inline-Befehl. Coda macht die Hände-schmutzig-Arbeit. Verstöße gegen diese Trennung sind als „Faulheits-Catches" katalogisiert (siehe [GLOBAL_LESSONS.md](../GLOBAL_LESSONS.md)).

## Datei-Hierarchie pro Projekt

Jedes Projekt, das den Marathon-Workflow nutzt, hat folgende Pflicht-Dateien (Vorlagen in [`templates/`](../templates/)):

| Datei | Zweck | Lifecycle |
|---|---|---|
| `CLAUDE_{PROJEKT}.md` | Betriebsanleitung für Coda | wächst mit Patches, < 150 Zeilen |
| `SUPERVISOR_{PROJEKT}.md` | Strategischer Stand für Chat-Supervisor | jeder Patch aktualisiert, < 400 Zeilen |
| `MARATHON_WORKFLOW_{PROJEKT}.md` | Aufgabenliste mit Status | jeder Patch aktualisiert Status-Spalte |
| `mjolnir.md` | Session-Abschluss-State (Single-Slot) | wird beim nächsten Session-Start gelesen + überschrieben |
| `FEATURE_REQUEST_{kurzname}.md` | aktive Aufträge an Coda | bei STATUS=FERTIG → Rename zu `_ERLEDIGT.md` |
| `HANDOVER_{PROJEKT}.md` | Detail-Übergabe zwischen Sessions | bei Session-Ende mit ausstehender Arbeit |
| `lessons_{PROJEKT}.md` | projektspezifische Stolperstein-Sammlung | nach ≥2-Min-Falle eintragen |
| `DECISIONS_{PROJEKT}.md` | offene Architektur-Fragen + Entscheidungen | bei Unsicherheit eintragen |
| `DESIGN_{PROJEKT}.md` | projektspezifische Design-Entscheidungen | bei UI-Patch |
| `ROADMAP_{PROJEKT}.md` | Phasen-Roadmap (Prosa erlaubt) | bei Phasen-Wechsel |
| `REPO_INDEX.md` | automatisch gepflegtes Verzeichnis mit Raw-Links | bei Verzeichnisänderungen |
| `GIST_LINK.md` | Gist-Brücke (Index-Gist + Projekt-Gist-URL) | bei Bootstrap, dann statisch |

## Session-Zyklus (Coda)

1. **Konflikt-Check**: existiert `mjolnir.md` mit STATUS=IN_ARBEIT UND `FEATURE_REQUEST_{kurzname}.md` mit anderem Kurznamen? → neuer Request wird zu `_QUEUED.md`, alter zuerst fertig machen.
2. `FEATURE_REQUEST_{kurzname}.md` lesen — falls vorhanden, Priorität 1. Bei STATUS=FERTIG am Ende → Rename zu `_ERLEDIGT.md`.
3. `mjolnir.md` lesen (STATUS-Header zuerst), dann löschen (Single-Slot).
4. `HANDOVER_{PROJEKT}.md` lesen, falls vorhanden.
5. `MARATHON_WORKFLOW_{PROJEKT}.md` lesen.
6. `python scripts/lessons_lookup.py --task '<aufgabe>'` (TF-IDF Top-3, ~500 Token statt 80k Full-Load). Bei 0 Treffern → „Aufgabe ist neu", kein Kontext-Stuffing. Detail: GLOBAL_LESSONS „Lessons-Retrieval statt Lessons-Komplett-Load" (mw-v2a Paket 1).
7. Globale Quellen: `GLOBAL_LESSONS.md`, `SUPERVISOR_KODEX.md`. Task-spezifische Regeln aus `playbooks/`, pfadspezifische aus `.claude/rules/` (mw-v2b Paket 2).
8. Arbeit ausführen — Tests, Commit, Push selbst (`$LASTEXITCODE` verifizieren).
9. **Auffüll-Check:** Auftrag erledigt UND < 300k Token verbraucht → nächstes Item aus FEATURE_REQUEST / MARATHON_WORKFLOW / BACKLOG nehmen statt abzuschließen. Stopp bei ~350k (50k Reserve für Doku). NUR sichere, unabhängige Items — destruktive Ops nie als Auffüller. Siehe Sektion „Session-Auffüll-Regel" unten.
10. Worktree-Branches selbst auf main mergen (kein „Schritt 0 für Chris").
11. `mjolnir.md` neu schreiben mit STATUS-Header (FERTIG | IN_ARBEIT | BLOCKIERT) — Pflicht, ausnahmslos.
12. Bei Verzeichnisänderungen: `REPO_INDEX.md` aktualisieren VOR dem finalen Push.
13. Projekt-Gist aktualisieren (PATCH via `workflow/gist_publisher.py`): HANDOVER, MJOLNIR, STATUS, ggf. REPO_INDEX, LESSONS — Supervisor kann nur Gists fetchen, keine Raw-Links.

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

Doku-Pflicht bei Auffüll-Patches: eigener `git commit` pro Folge-Patch, kein separater HANDOVER/SUPERVISOR/Gist pro Zwischen-Patch — EIN HANDOVER am Session-Ende für alle.

Anti-Pattern: „Patch fertig bei 120k → Doku → Handover → STOPP" verbrennt 80% des Budgets für Overhead und gilt als Verstoß gegen diese Regel. Anlass: Kintsugi-Migration Token-Audit (3 Sessions à 120k statt 1 à 360k = 200k verschwendet). Lesson: [GLOBAL_LESSONS.md](../GLOBAL_LESSONS.md) „Session-Auffüll-Regel".

## Die 6 Faulheits-Catches (Quick Reference)

Kanonische Liste der Anti-Patterns, die den Workflow brechen würden. Vollständig dokumentiert in [GLOBAL_LESSONS.md](../GLOBAL_LESSONS.md):

1. **OBERSTES GEBOT** — Coda terminalisiert nichts, was Coda kann.
2. **mjolnir.md PFLICHT am Session-Ende** — Single-Slot-Round-Trip, ausnahmslos.
3. **Worktree-Branches selbst auf main mergen** — kein „Schritt 0 für Chris".
4. **Supervisor baut Coda-Prompts statt Terminal-Befehle** — auch „nur ein Befehl" ist einer zu viel.
5. **Multi-Session-STATUS-Header + QUEUED-Pattern** — mjolnir.md mit Status-Block als erster Zeile.
6. **Selbsttest-Pflicht für Workflow-Änderungen** — dreiphasig (A Setup, B Replay, C Adversarial, D Cleanup).

## Mjölnir-Round-Trip

`mjolnir.md` ist der Single-Slot-Übergabepunkt zwischen Sessions. Inhalt: STATUS-Header (Pipe-Format) + 5-10 Zeilen Prosa über den letzten Stand.

- **STATUS=FERTIG**: Auftrag durch, `FEATURE_REQUEST` ist umbenannt zu `_ERLEDIGT.md`, mjolnir.md wird beim nächsten Session-Start gelesen + gelöscht.
- **STATUS=IN_ARBEIT**: Auftrag läuft über mehrere Sessions, `FEATURE_REQUEST` bleibt unverändert, mjolnir.md trägt Fortschritt + nächsten Schritt.
- **STATUS=BLOCKIERT**: Blocker dokumentiert in `DECISIONS_PENDING.md`, mjolnir.md trägt BLOCKIERT-Header.

Chris fetcht über den ZUSAMMENFASSUNG-Button die mjolnir.md vom Handy und sieht sofort, ob Aktion nötig ist.

## Bibel-Format

Maschinenlesbares Pipe-Format für Lessons, Templates, Status-Header. Eine Zeile pro Lesson, Felder mit `|` getrennt. Anlass + Begründung + Generalisierung in fett-prosaischen Folge-Absätzen darunter. Maschine ignoriert Prosa, Mensch findet Kontext.

Status-Header-Beispiel (`mjolnir.md` Zeile 1):
```
STATUS|FERTIG|AUFTRAG: kurzname|FORTSCHRITT: X/Y Schritte / N Sessions|NÄCHSTE SESSION: ...
```

Vollständige Cheat-Sheet-Sektion in [GLOBAL_LESSONS.md](../GLOBAL_LESSONS.md).

## Gist-Brücke (Supervisor-Lesezugang)

Die Supervisor-Instanz (claude.ai Chat-Fenster) kann GitHub-Raw-Links **nicht** fetchen, aber GitHub-Gists **schon**. Daher hält jedes Projekt einen parallelen PUBLIC Gist mit den Briefing-Dateien (HANDOVER, MJOLNIR, STATUS, REPO_INDEX, LESSONS).

- **Index-Gist:** Zentrale Navigationsdatei mit allen Projekt-Gist-URLs. Wird nur bei neuem Projekt erweitert.
- **Claude-KB-Gist:** Globale Wissensbasis (GLOBAL_LESSONS, TEMPLATES_INDEX, WORKFLOW_SUMMARY, BOOTSTRAP_CHECKLIST). Wird vom Lessons-Cron-Job aktualisiert.
- **Projekt-Gists:** Eine je aktivem Projekt. Coda aktualisiert am Session-Ende via PATCH.

Konkrete URLs stehen in [`GIST_LINK.md`](../GIST_LINK.md). Helfer-Skript: [`workflow/gist_publisher.py`](gist_publisher.py).

## Weitere Workflow-Dokumente

- [GLOBAL_LESSONS.md](../GLOBAL_LESSONS.md) — universelle Lessons, Faulheits-Catches, Selbsttest-Pattern, Bibel-Format
- [SUPERVISOR_KODEX.md](../SUPERVISOR_KODEX.md) — NIE/IMMER-Listen für Chat-Supervisor
- [PROJECT_BOOTSTRAP_README.md](../PROJECT_BOOTSTRAP_README.md) — Schritt-für-Schritt für neues Projekt
- [DECISIONS_PENDING.md](../DECISIONS_PENDING.md) — offene Meta-Layer-Architektur-Fragen
- [GIST_LINK.md](../GIST_LINK.md) — Gist-Brücke (URLs)
- [concepts/Try_Faulheits_catch.md](../concepts/Try_Faulheits_catch.md) — historischer Konzept-Ursprung der Faulheits-Catches
- [templates/](../templates/) — Bootstrap-Vorlagen für neue Projekte
