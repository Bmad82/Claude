# mjolnir.md — Claude (Meta-Layer)

```
STATUS|FERTIG|AUFTRAG: repo-restrukturierung|FORTSCHRITT: 5/5 Phasen / 1 Session|NÄCHSTE SESSION: entfällt (FERTIG)
```

**STATUS:** FERTIG
**AUFTRAG:** repo-restrukturierung
**FORTSCHRITT:** 1 Session | Phase 1-5 durch (Cleanup, Ordnerstruktur, REPO_INDEX, Templates, README)
**NÄCHSTE SESSION:** entfällt

---

## Was Chris physisch tun muss

- Auf Handy nach Push prüfen ob Repo grün ist (https://github.com/Bmad82/Claude)
- **Restschuld Worktree-Lock:** `.claude/worktrees/focused-payne-b38e6a/` (leer, nicht versioniert) ließ sich aus laufender Claude-Code-Session nicht löschen — Filesystem-Lock. Bei Gelegenheit aus geschlossener Session oder nach Reboot manuell entfernen: `Remove-Item -Recurse -Force "C:\Users\chris\Python\Claude\.claude\worktrees"`. Beeinflusst Repo nicht (kein Tracking).

---

## Auftragshistorie

- **Phase 1 (Cleanup):** `_erledigt/`-Ordner angelegt, 4 `_ERLEDIGT`-Files verschoben. `bugs/README.md` mit Scope-Erklärung erstellt. `DESIGN.md`-Platzhalter zu `[TODO: aus Projekt-:root]` umbenannt (Konvention klargemacht: Werte kommen aus projektspezifischer `:root`, globale DESIGN bleibt leer).
- **Phase 2 (Struktur):** `workflow/MARATHON_WORKFLOW.md` angelegt. `lessons/INDEX.md` mit 3-Ebenen-Hierarchie (Workflow/Technologie/Projekt) geschrieben.
- **Phase 3 (REPO_INDEX):** `REPO_INDEX.md` im Root mit Verzeichnisbaum + Raw-Link-Tabelle (46 Dateien). Format autoritativ dokumentiert.
- **Phase 4 (Templates):** `CLAUDE_PROJEKT_TEMPLATE.md` um REPO_INDEX-Pflicht ergänzt. `SUPERVISOR_PROJEKT_TEMPLATE.md` um Repo-Navigation-Sektion ergänzt.
- **Phase 5 (README):** `README.md` neu — "Claude — Marathon Workflow Knowledge Base", Drei-Rollen-Modell, Ordnerstruktur-Tabelle, Public-Repo-Warnung erhalten.
- **Abschluss:** `FEATURE_REQUEST_CLAUDE.md` (Root-Übergabe-Variante) entfernt — Inhalt ist bereits konventionskonform unter `_erledigt/FEATURE_REQUEST_repo-restrukturierung_ERLEDIGT.md` archiviert (kebab-case Kurzname-Konvention). Push verifiziert via `$LASTEXITCODE`.

---

<!--
LIFECYCLE-Notiz für Coda:

- STATUS=FERTIG  →  beim nächsten Session-Start: mjolnir.md einlesen, dann löschen. FEATURE_REQUEST_{PROJEKT}.md zu _ERLEDIGT.md umbenennen.
- STATUS=IN_ARBEIT  →  beim nächsten Session-Start: mjolnir.md einlesen, FORTSCHRITT-Block prüfen, laufenden Auftrag fortsetzen. FEATURE_REQUEST NICHT umbenennen.
- STATUS=BLOCKIERT  →  beim nächsten Session-Start: mjolnir.md einlesen, DECISIONS_PENDING.md prüfen, BLOCKER auflösen oder eskalieren.

mjolnir.md ist Single-Slot — genau EINE Datei zur Zeit, wird beim nächsten Session-Start gelöscht. _ERLEDIGT.md ist Audit-Log (akkumuliert).
-->
