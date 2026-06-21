lessons sqlite-db | maschinen-only | schema: wall_signatur | kategorie | fix | kontext | quelle

wall_signatur | db-migration idempotent, PRAGMA table_info vor ALTER TABLE, CREATE INDEX IF NOT EXISTS
kategorie | sqlite/migration
fix | migrationen idempotent: PRAGMA table_info-check vor ALTER TABLE, CREATE INDEX IF NOT EXISTS
kontext |
quelle | Zerberus P92

wall_signatur | vor schema-aenderung manuelles db-backup, db ist heilig
kategorie | sqlite/backup
fix | vor jeder schema-aenderung manuelles db-backup
kontext |
quelle | Zerberus P92

wall_signatur | alembic-baseline nach manueller migration, alembic stamp head, sonst spalte nochmal angelegt
kategorie | sqlite/alembic
fix | alembic-baseline NACH manueller migration erstellen + alembic stamp head
kontext | sonst versucht alembic die spalte nochmal anzulegen
quelle | Zerberus P92

wall_signatur | laufender server altes schema im speicher, init_db greift erst nach server-restart
kategorie | sqlite/migration
fix | nach schema-aenderung server-restart, code-aenderung allein reicht nicht
kontext | init_db greift erst bei restart
quelle | Zerberus P92

wall_signatur | lazy-load-guard modell-init None beim ersten aufruf
kategorie | sqlite/init
fix | lazy-load-guard: variable kann None sein beim ersten aufruf → immer pruefen
kontext |
quelle | Zerberus P75

wall_signatur | dedup-insert-guard double-insert sse-timeout-retry, parallel-pfade legacy+orchestrator, SELECT vor add 30s-fenster
kategorie | sqlite/dedup
fix | guard in der store-funktion: vor session.add per SELECT pruefen ob (session_id, role, content, timestamp innerhalb 30s) existiert → skip+warn
kontext | double-inserts aus sse-timeout-retries oder parallel-pfaden | 30s-fenster faengt retries, blockt keine legitimen schnellen nachsendungen
quelle | Zerberus P113a

wall_signatur | dedup-scope je role, log-tabelle mischt produktion+diagnose, session_id NULL nicht touchen
kategorie | sqlite/dedup
fix | dedup-guard explizit per "role IN ('user','assistant') AND session_id IS NOT NULL" filtern
kontext | NULL-session = legitime diagnostische duplikate, nicht killen
quelle | Zerberus P113a
