# mjolnir.md — Claude (Meta-Repo)

```
STATUS|FERTIG|AUFTRAG: session-auffuell-regel|FORTSCHRITT: 1 von 1 Sessions / alle Stufen durch|NÄCHSTE SESSION: entfällt (FERTIG)
```

**STATUS:** FERTIG
**AUFTRAG:** session-auffuell-regel
**FORTSCHRITT:** 1 von 1 Sessions | alle Stufen durch (Templates + Lessons + Workflow + Gist-Sync + Zerberus)
**NÄCHSTE SESSION:** entfällt (FERTIG)

---

## Was Chris physisch tun muss

— nichts —

Alle Änderungen sind Doku-only. Supervisor (Chat-Instanz) sieht beim nächsten Briefing-Fetch des Claude-KB-Gists die neue Auffüll-Regel automatisch im WORKFLOW_SUMMARY.md (neuer Schritt 9) und der GLOBAL_LESSONS.md (neue Lesson oben). Keine manuelle Verifikation nötig — Round-Trip läuft.

---

## Auftragshistorie (kurz)

FEATURE_REQUEST_CLAUDE.md „session-auffuell-regel" komplett abgearbeitet. Auffüll-Regel verankert: primärer Auftrag erledigt UND < 300k Token verbraucht → nächstes Item aus FEATURE_REQUEST / MARATHON_WORKFLOW / BACKLOG / Test-Schulden / Doku-Hygiene nehmen statt abzuschließen; Stopp ~350k (50k Reserve für Doku); destruktive Ops nie als Auffüller. Anlass: Kintsugi-Migration Token-Audit (3 Sessions à ~120k statt 1 à ~360k = 200k verschwendet) — Mega-Patch-Ära P122–P152 hatte gezeigt, dass Auffüll-Logik 24k/Patch statt 100k+/Patch bringt.

**Gepatcht:**
- Claude-Repo: `templates/MARATHON_WORKFLOW_TEMPLATE.md`, `templates/CLAUDE_PROJEKT_TEMPLATE.md`, `LESSONS_KONSOLIDIERT.md`, `GLOBAL_LESSONS.md`, `workflow/MARATHON_WORKFLOW.md` (Session-Zyklus 12 → 13 Schritte, neuer Schritt 9 Auffüll-Check). Commit `149d1c2`.
- Zerberus-Repo: `CLAUDE_ZERBERUS.md`, `MARATHON_WORKFLOW_ZERBERUS.md`, `lessons_ZERBERUS.md`. Bestehende Regeln unverändert (Diff = nur Additions). Commit `3a5ad83`.
- Gist-PATCH: Claude-KB-Gist (WORKFLOW_SUMMARY.md neuer Schritt 9 + GLOBAL_LESSONS.md Lesson) `updated_at=2026-05-21T10:28:54Z`; Zerberus-Gist (LESSONS.md) `updated_at=2026-05-21T10:28:55Z`.

**Selbsttest:** grep `Auffüll` → 7 Treffer im Claude-Repo (Erwartung ≥ 4), 3 im Zerberus-Repo (Erwartung ≥ 2). Fresh-Fetch der drei Gist-Files bestätigt Auffüll-Präsenz.

**Übersprungen mit Begründung:**
- Sága (`C:\Users\chris\Python\Saga\`) — Pfad existiert nicht im Filesystem.
- `marathon_workflow_showcase.html` — Glob `**/*showcase*.html` und `**/marathon*.html` unter `C:\Users\chris\Python\` lieferten beide null Treffer.

FEATURE_REQUEST_CLAUDE.md → FEATURE_REQUEST_CLAUDE_ERLEDIGT.md umbenannt, Audit-Sektion angehängt. Beide Repos gepusht (Remote-State 0/0).

---

<!--
LIFECYCLE-Notiz für Coda:

- STATUS=FERTIG  →  beim nächsten Session-Start: mjolnir.md einlesen, dann löschen. FEATURE_REQUEST_CLAUDE.md bereits zu _ERLEDIGT.md umbenannt mit Audit-Sektion.
- STATUS=IN_ARBEIT  →  entfällt hier.
- STATUS=BLOCKIERT  →  entfällt hier.

mjolnir.md ist Single-Slot — genau EINE Datei zur Zeit, wird beim nächsten Session-Start gelesen + gelöscht.
-->
