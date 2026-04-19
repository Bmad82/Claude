# SQLite & Datenbank-Migrationen

- DB-Migrationen IMMER idempotent: `PRAGMA table_info`-Check vor `ALTER TABLE`, `CREATE INDEX IF NOT EXISTS` (Zerberus P92)
- Vor jeder Schema-Änderung: manuelles DB-Backup. Die DB ist heilig (Zerberus P92)
- Alembic-Baseline NACH manueller Migration erstellen + `alembic stamp head` — sonst versucht Alembic die Spalte nochmal anzulegen (Zerberus P92)
- Laufender Server hat altes Schema im Speicher: Code-Änderung allein reicht nicht, Server-Restart nötig damit `init_db` greift (Zerberus P92)
- Lazy-Load-Guard bei Modell-Initialisierung: Variable kann `None` sein beim ersten Aufruf → immer prüfen (Zerberus P75)
