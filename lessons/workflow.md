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
