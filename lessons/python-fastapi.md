# Python & FastAPI

- Uvicorn `--reload` auf Windows unzuverlässig: neue Module/Imports werden nicht erkannt, nur Änderungen an bereits geladenen Dateien. Bei neuen Imports: manueller Kill + Restart nötig (Zerberus P89)
- Uvicorn `--reload` Zombie-Worker: wiederholte Kill-Zyklen erzeugen parallele Master-Trees. Vor jedem Restart ALLE Python-PIDs prüfen und killen, dann erst neu starten (Zerberus P99)
- `start.bat` ohne `--reload`-Flag: Code-Änderungen werden lautlos ignoriert. Immer verifizieren dass neue Logs/Felder/Marker tatsächlich erscheinen (Zerberus P88)
- Async-Funktionen: `update_interaction()` o.ä. muss async sein, alle Call-Sites brauchen `await` — sonst Double-Start / Race Conditions (Zerberus P59)
- Lock-Guard bei Background-Tasks: prüfen ob Task bereits läuft bevor neuer gestartet wird
- Pacemaker/Config-Änderungen in YAML wirken erst nach Neustart (kein Live-Reload bei den meisten FastAPI-Setups)
- Config-Split-Brain: wenn UI in eine Datei schreibt (json) und Backend eine andere liest (yaml), wirken UI-Änderungen nie → eine einzige Config-Datei als Single Source of Truth
- Async-First: alle I/O-Operationen (DB, Netzwerk, TTS) async. Kein blocking call im asyncio-Loop — `aiohttp` statt `requests`
- In-Memory-Cache für Hot-Path-Daten statt DB-Hit (z.B. bei GPS-Pings mit 10 Hz → SQLite-Trommelfeuer → Absturz)
- Pro-Verbindung eigene Session-Instanz, kein globaler Singleton — verhindert State-Mixing bei mehreren Clients
- Deterministisches Caching via Hash: Dateiname = Hash des Inhalts → gleicher Input = gleiche Datei, kein Doppelt-Generieren
- Path-Traversal-Schutz: `os.path.basename()` auf alles was vom User kommt, auch bei "internen" Download-Routes
- `isoformat()` produziert `T`-Separator, SQLite speichert mit Space → Vergleiche brechen lautlos
