# SQLite & Datenbank-Migrationen

- DB-Migrationen IMMER idempotent: `PRAGMA table_info`-Check vor `ALTER TABLE`, `CREATE INDEX IF NOT EXISTS` (Zerberus P92)
- Vor jeder Schema-Änderung: manuelles DB-Backup. Die DB ist heilig (Zerberus P92)
- Alembic-Baseline NACH manueller Migration erstellen + `alembic stamp head` — sonst versucht Alembic die Spalte nochmal anzulegen (Zerberus P92)
- Laufender Server hat altes Schema im Speicher: Code-Änderung allein reicht nicht, Server-Restart nötig damit `init_db` greift (Zerberus P92)
- Lazy-Load-Guard bei Modell-Initialisierung: Variable kann `None` sein beim ersten Aufruf → immer prüfen (Zerberus P75)
- **Dedup-Insert-Guard Pattern:** Double-Inserts entstehen bei SSE-Timeout-Retries (Frontend abort → Backend committet trotzdem) oder Parallel-Pfaden (legacy.py + orchestrator.py rufen dieselbe store-Funktion). Guard direkt in der store-Funktion: vor `session.add(...)` per SELECT prüfen ob (session_id, role, content, timestamp within 30s) schon existiert → skip + warn. Window 30s ist Sweet Spot: fängt Retries, blockt keine schnellen legitimen Nachsendungen (Zerberus P113a)
- **Dedup-Scope je Role differenzieren:** Log-Tabellen mischen oft Produktionsdaten (Chat-Messages mit session_id) und Diagnose-Daten (Raw-Transcripts mit session_id=NULL). Dedup-Guard darf NULL-Session nicht touchen, sonst killt man legitime diagnostische Duplikate. Explizit per `role IN ('user','assistant') AND session_id IS NOT NULL` filtern (Zerberus P113a)
