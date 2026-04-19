# Python & FastAPI

- Uvicorn `--reload` auf Windows unzuverlässig: neue Module/Imports werden nicht erkannt, nur Änderungen an bereits geladenen Dateien. Bei neuen Imports: manueller Kill + Restart nötig (Zerberus P89)
- Uvicorn `--reload` Zombie-Worker: wiederholte Kill-Zyklen erzeugen parallele Master-Trees. Vor jedem Restart ALLE Python-PIDs prüfen und killen, dann erst neu starten (Zerberus P99)
- `start.bat` ohne `--reload`-Flag: Code-Änderungen werden lautlos ignoriert. Immer verifizieren dass neue Logs/Felder/Marker tatsächlich erscheinen (Zerberus P88)
- Async-Funktionen: `update_interaction()` o.ä. muss async sein, alle Call-Sites brauchen `await` — sonst Double-Start / Race Conditions (Zerberus P59)
- Lock-Guard bei Background-Tasks: prüfen ob Task bereits läuft bevor neuer gestartet wird
- Pacemaker/Config-Änderungen in YAML wirken erst nach Neustart (kein Live-Reload bei den meisten FastAPI-Setups)
