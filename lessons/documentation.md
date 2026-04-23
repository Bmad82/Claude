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
