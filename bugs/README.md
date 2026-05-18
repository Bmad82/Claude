# bugs/ — Projekt-spezifische Bug-Tracker

Hier liegen Bug-Tracker für die Projekte, die mit dem Marathon-Workflow arbeiten. **Ein Unterordner pro Projekt.**

## Struktur

```
bugs/
├── README.md            # diese Datei
└── {projekt}/
    ├── {domain1}.md     # z.B. regex.md, whisper.md, sqlite.md
    └── {domain2}.md
```

Pro Projekt ein Unterordner (`bugs/zerberus/`, `bugs/{nächstesprojekt}/`). Innerhalb des Projekt-Ordners eine Datei pro Technologie-Domäne (Regex, Whisper, SQLite, Frontend, …).

## Aktive Projekt-Ordner

- `bugs/zerberus/` — Zerberus Pro 4.0 (Python-Backend, Voice/Whisper, Regex-Pattern)

Weitere Projekte folgen, sobald sie auf den Marathon-Workflow umgestellt werden.

## Format pro Bug-Datei

Bibel-Format mit ID, Severity, Status. Beispiel:

```markdown
# {Domain}-Bugs für {Projekt}

## {ID}|{Severity}|{Status}|{Kurztitel}
- Symptom: …
- Reproduktion: …
- Workaround: …
- Lösung (falls behoben): …
```

IDs nach Konvention `RX-001` (Regex), `W-001` (Whisper), `DB-001` (SQLite) — Präfix pro Domain.

## Pflege

- Supervisor sichtet vor Patch-Planung offene Bugs, schlägt passende für nächsten Patch vor.
- Coda trägt nach Patch-Abschluss neu entdeckte Bugs hier ein (vor `git push`).
- Behobene Bugs bleiben mit STATUS=ERLEDIGT stehen — Historie nicht löschen.
