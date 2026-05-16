# Claude-Workflow (Code + Chat)

- Vor jeder Claude-Code-Session: git commit als Checkpoint — YOLO-Modus ohne Backup ist Russisch Roulette
- Max 2–3 Patches pro Code-Session — ab Patch 4+ leidet die Kontextqualität spürbar
- CLAUDE.md und SUPERVISOR.md sind heilig — Claude Code darf ergänzen, niemals überschreiben
- Bei unerwartetem Verhalten: erst SUPERVISOR.md lesen, dann debuggen
- Patch-Prompts in der Chat-Instanz planen, Claude Code nur ausführen lassen — kein Mischen
- Chat-Instanz = Supervisor (plant, prüft, promptet). Erstellt keine Dateien außer Prompts für die Code-Instanz
- Code-Instanz = Executor (implementiert, testet). Folgt dem Prompt, fragt bei Unklarheiten nach
- Bei mehreren Code-Pfaden (z.B. legacy.py vs. orchestrator.py): IMMER prüfen welcher Router den aktiven Traffic führt, bevor ein Fix nur in einem Pfad landet (Zerberus P80b)
- Bei jedem Pipeline-Fix alle betroffenen Pfade prüfen — nicht nur den offensichtlichen (Zerberus P82)
- CLAUDE_[PROJEKTNAME].md Konvention: Projektspezifische Dateien tragen IMMER den Projektnamen als Suffix. Claude Code liest beim Start automatisch eine globale CLAUDE.md und verwechselt sie sonst mit der projektspezifischen. In Prompts IMMER vollen Dateinamen verwenden. (Zerberus P100)
- Alle Prompts und strukturierte Ausgaben als `.md`-Datei ausgeben — kein Inline-Text, mobilfreundlich kopierbar
- Konzept vor Implementierung: bei kreativen Projekten erst Konzept als .md ausarbeiten, dann technische Umsetzung
- Lebende Konzept-Dokumente: Ideen, Audits, Design-Regeln in separater .md sammeln, getrennt vom Projektstatus
- Kein opportunistisches Refactoring: Claude Code ändert nur was der aktuelle Patch erfordert
- Bei Scope-Unsicherheit: FRAGEN, nicht selbst entscheiden — keine kreativen Erweiterungen über den Prompt hinaus
- Entscheidungsboxen: bei Aktionen die User-Input erfordern (Server-Restart, destruktive Ops) immer klar formatierte Box mit konkreten Optionen + "Soll ich das übernehmen?"
- Verbosity-Management: Coding-Instanz = stiller Handwerker (kurz, präzise). Chat-Instanz = ausführlich, assoziativ. Nicht mischen
- Diagnose vor Fix: erst grep/Select-String, dann reparieren — betroffenen Code-Pfad identifizieren bevor ein Patch landet
- Git-Push-Verifikation: nach jedem `git push` Exit-Code prüfen (`$LASTEXITCODE`), bei Fehler User auf Deutsch informieren
- Git-Credential-Prüfung: vor erstem Push in einer Session `git config credential.helper` checken
- PowerShell kennt kein `&&` — Befehle mit `;` trennen oder einzeln ausführen
- OneDrive NIEMALS als Arbeitsverzeichnis für aktive Projekte — lockt Dateien (SQLite, Logs, Python-Prozesse)

## Marathon-Workflow (Coda + Supervisor + Mjölnir)
Volltext-Sektionen mit Pipe-Format in `GLOBAL_LESSONS.md` im Repo-Root. Kurzform:
- **OBERSTES GEBOT (2026-05-16, Zerberus P-umzug):** Coda terminalisiert NICHTS was Coda selbst kann — keine git/pytest/pip/robocopy/npm-Befehle an Chris delegieren. Worktree-Merges + Push macht Coda selbst vor Session-Ende. `mjolnir.md` enthält NUR physisch unmögliche Tests (Touch, echtes Gerät, Mikrofon). Auch der Supervisor (Chat) gibt KEINE Terminal-Befehle, sondern baut Coda-Prompts. Verstoß = Korrektur. Backstop pro Projekt: Regel 0 in `CLAUDE_<PROJEKT>.md`.
- **mjolnir.md ist PFLICHT am Session-Ende (2026-05-16, Zerberus B-072):** wird am Ende JEDER Session überschrieben, ausnahmslos. Single-Slot-State (genau eine aktuelle Zusammenfassung), nicht zu verwechseln mit `_ERLEDIGT.md` (Audit-Log, akkumuliert). Ohne mjolnir.md-Update bricht der Mjölnir-Round-Trip — Chris kann nicht erkennen ob ein Auftrag durch ist.
- **Worktree-Branches selbst auf main mergen (2026-05-16, Zerberus B-061):** Coda merged + pusht eigene Worktree-Branches vor Session-Ende. Pattern: `git stash push` für lokale Edits → `git merge --ff-only` → `stash pop` → eigenen Branch per `rebase main` aktualisieren → ff-merge → push. Ungemergte Branches NICHT als „Schritt 0" in `mjolnir.md` an Chris delegieren.
- **Supervisor baut Coda-Prompts statt Terminal-Befehle (2026-05-16, Zerberus):** Wenn Chris ein Problem schildert das Coda lösen kann → Supervisor schreibt `.md`-Prompt (FEATURE_REQUEST oder Mjölnir-Auftrag) statt PowerShell-Snippet im Chat. „Nur ein Befehl" ist einer zu viel. Trennung Supervisor=plant/prüft/promptet vs Coda=implementiert/testet gilt auch hier.
