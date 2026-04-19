# CLAUDE.md – [PROJEKTNAME]

## Globale Wissensbasis
Repository: https://github.com/Bmad82/Claude
- Vor Arbeitsbeginn: `lessons/`-Ordner auf relevante Einträge prüfen
- Nach Abschluss: Neue universelle Erkenntnisse dort eintragen
- Templates: `templates/` enthält Vorlagen und Standardregeln

⚠️ **Das globale Repo ist PUBLIC.**
Niemals Passwörter, API-Keys, Tokens, persönliche Daten, IP-Adressen,
interne URLs oder projektspezifische Secrets in Lessons oder Templates schreiben.
Bei jedem Commit ins globale Repo: Inhalt auf Secrets prüfen. Im Zweifel NICHT committen, nachfragen.

## Pflicht nach jedem Patch
Nach Abschluss jedes Patches SUPERVISOR.md aktualisieren:
- Aktueller Patch: Nummer, Datum, 3–5 Zeilen was gemacht wurde
- Offene Items: Liste aktuell halten (erledigte raus, neue rein)
- Architektur-Warnungen: nur wenn sich etwas geändert hat
SUPERVISOR.md ist die einzige Datei, die die Chat-Instanz beim Session-Start liest.

Vollständige Projektdokumentation: `docs/PROJEKTDOKUMENTATION.md`

## Projektpfad
[PFAD EINTRAGEN]

## Regeln
1. Immer erst lesen, dann schreiben — keine blinden Überschreibungen
2. .env niemals nach außen leaken oder in Logs ausgeben
3. Vor jeder DB-Schema-Änderung: Backup der Datenbank
4. [PROJEKTSPEZIFISCHE REGELN ERGÄNZEN]

## Weiterführende Doku
- **Projektspezifische Lessons:** `lessons.md` im Projektroot
- **Globale Lessons:** https://github.com/Bmad82/Claude/tree/main/lessons
- **Vollständiges Patch-Archiv:** `docs/PROJEKTDOKUMENTATION.md`
