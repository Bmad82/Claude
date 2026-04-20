<!-- ⚠️ TEMPLATE — NUR FÜR NEUE PROJEKTE
Bei Projekterstellung als CLAUDE_[PROJEKTNAME].md kopieren.
NIEMALS eine bestehende CLAUDE_[PROJEKT].md damit überschreiben. -->

# CLAUDE_[PROJEKTNAME].md – [PROJEKTNAME]

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

## Bug-Tracker Integration

Globaler Bug-Tracker: https://github.com/Bmad82/Claude/bugs/
Projektspezifische Bugs: `bugs/<projektname>/`

**Vor jedem Patch:**
- `bugs/<projektname>/` auf offene Einträge prüfen
- Passende Bugs (gleiche Datei/Modul, geringer Mehraufwand) als zusätzliche Blöcke in den Patch einbauen
- Kleinere Fixes (Severity Niedrig, <10 Zeilen) dürfen ohne Rückfrage mit eingebaut werden
- Größere Fixes (Severity Hoch, eigener Patch nötig) nur melden, nicht eigenmächtig starten

**Nach jedem Patch:**
- Erledigte Bugs von "Offen" nach "Erledigt" verschieben mit Patch-Nummer und Datum
- Wenn während der Arbeit neue Bugs auffallen: unter passender Kategorie-MD eintragen
- Wenn keine passende Kategorie existiert: neue MD anlegen (Namenskonvention: `<thema>.md`)

**WICHTIG:** Der Bug-Tracker-Ordner liegt AUSSERHALB des Projektordners im übergeordneten Claude-Repo. Der Pfad wird in der CLAUDE.md des jeweiligen Projekts konfiguriert. Wenn der Bug-Tracker-Pfad nicht erreichbar ist oder der Ordner nicht eingebunden wurde, den User aktiv darauf hinweisen — nicht stillschweigend ohne Bug-Check weiterarbeiten.

## User-Eingaben & Kommunikation

Der Architekt kommuniziert ca. 75% per Spracheingabe (Whisper/Dictation). Phonetisch seltsame Wörter, fehlende Satzzeichen und Wortdreher sind normal — immer die beabsichtigte Bedeutung priorisieren. Bei unlogischen Passagen lieber nachfragen statt falsch interpretieren.

**Handy-First ist Pflicht.** Der Architekt und die Endnutzerin arbeiten primär auf Mobilgeräten (iPhone, Android). Desktop ist sekundär. Bei JEDEM UI/CSS/HTML/Frontend-Change gelten folgende Regeln ohne Ausnahme:
- Mobile Viewports zuerst testen, Desktop danach
- Minimum Touch-Targets: 44px
- `:hover` funktioniert auf Touch nicht — immer `:active` zusätzlich setzen
- `dvh` statt `vh` verwenden (Keyboard-Overlay-Schutz)
- Überstehende Elemente, horizontales Scrollen, abgeschnittene Texte sind Blocker-Bugs
- `backdrop-filter` braucht Fallback
- `@media (orientation: landscape) and (max-height: 500px)` für Landscape-Edge-Cases
- Beispiel FALSCH: Button mit 28px Höhe, nur `:hover`-State, feste `100vh`-Höhe
- Beispiel RICHTIG: Button mit 44px min-height, `:active`-State, `100dvh`-Höhe, Touch-Target-Padding
