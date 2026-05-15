# Dokumentation & Schulungsunterlagen

## Shop-Floor-Dokumente
- Praxiswissen von Maschinenbedienern > Herstellerdoku — erst implizites Wissen abfragen, dann gegenchecken
- Video-Transkripte sind Fallback, nicht Primärquelle
- Single-File HTML für Produktionsumgebungen: keine externen CSS/JS, kein Build-Tool, alles inline
- Dark Theme für wechselnde Lichtverhältnisse in Produktionsumgebungen
- Farbkodierung: Rot = Gefahr, Grün = Tipp, Teal = Hintergrund — wird intuitiv verstanden
- Profi/Rookie-Modus als CSS-Klasse: `body.expert-mode .step-detail { display: none !important; }`
- Click-Path-Blöcke: Klickpfade als monospace-Kette mit Pfeilen statt Fließtext
- Reset-Button ans Ende, nicht an den Anfang
- Sicherheitskritische Unterscheidungen: eigener farblicher Warnblock, nicht im Fließtext verstecken

## Persistenz
- localStorage für Fortschrittspersistenz in HTML-Anleitungen — Key pro Dokument eindeutig benennen
- Koordinatensystem-Fallen explizit dokumentieren (Panel vs. TCP vs. Workcontainer)

## Drei-Doku-Ebenen
- README.md = technisch, für Entwickler
- CLAUDE_[PROJEKT].md = Steuerungsdatei für Claude Code
- MANUAL.md oder Schulungsdoku = für Endnutzer ohne Tech-Sprech

## Projekt-Doku-Konvention (Konsolidierung 2026-05-15)
- Alle projektspezifischen Doku-Dateien tragen Suffix `_<PROJEKTNAME>` im Großbuchstaben-Format
- Liste: CLAUDE / SUPERVISOR / HANDOVER / MARATHON_WORKFLOW / lessons / DECISIONS / DESIGN / ROADMAP — jeweils `_<PROJEKTNAME>.md`
- Suffix-Position: PROJEKTNAME steht HINTEN, nicht vorne (`MARATHON_WORKFLOW_ZERBERUS.md`, nicht `ZERBERUS_MARATHON_WORKFLOW.md`)
- Ausnahmen: `mjolnir.md` (Mjölnir-Konvention, ephemer, wird beim nächsten Session-Start gelöscht), `FEATURE_REQUEST_<PROJEKT>.md` (Suffix bereits drin), `PROJEKTDOKUMENTATION.md`, `README.md`, `CHANGELOG.md`
- Sub-Doku in `docs/`-Unterordnern darf ohne Suffix bleiben wenn Tests/Code den Pfad hartcodieren (siehe Zerberus' `docs/DESIGN.md`)
- Bibel-Format für KI-gelesene Dateien (CLAUDE/SUPERVISOR/HANDOVER/MARATHON_WORKFLOW/lessons): artikelfrei, pipe-separiert, kein Prosa-Padding
- Mensch-gelesene Dateien (README/PROJEKTDOKUMENTATION/DESIGN): Prosa erlaubt
- Templates für alle 8 Dateitypen unter `templates/*_TEMPLATE.md` im Bibel-Format
- Session-Start-Pflicht in jeder `CLAUDE_<PROJEKT>.md`: 1) FEATURE_REQUEST prüfen → 2) HANDOVER lesen → 3) MARATHON_WORKFLOW lesen → 4) lessons konsultieren
- Mjolnir's `session_manager.DEFAULT_PROMPT_TEMPLATE` rendert `{PROJEKTNAME}` aus Allowlist und referenziert die suffixierten Dateinamen — damit jedes gesteuerte Projekt mit derselben Konvention läuft
