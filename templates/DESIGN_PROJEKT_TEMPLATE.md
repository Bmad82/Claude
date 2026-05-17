<!-- TEMPLATE | Kopie als DESIGN_{PROJEKT}.md ins Projekt-Root | Mensch-lesbar | Prosa erlaubt | NICHT zu verwechseln mit globaler DESIGN.md (Design-Referenz für UI/Look) -->

# DESIGN_{PROJEKT}.md
*Designdokument für {PROJEKT} — primär für Menschen, daher Prosa erlaubt.*

## Verhältnis zur globalen DESIGN.md
- `C:\Users\chris\Python\Claude\DESIGN.md` = globale UI-Referenz (Farben, Typography, Mobile-Regeln) — wird direkt referenziert
- `DESIGN_{PROJEKT}.md` = projektspezifische Vision/Architektur — eigenständig

## Vision
Was soll {PROJEKT} sein? Welches Problem löst es?

## Zielgruppe
Wer benutzt es, in welchem Kontext, auf welcher Plattform?

## Kernfunktionen
- Funktion 1 — kurze Beschreibung
- Funktion 2 — kurze Beschreibung

## Nicht-Ziele
Was {PROJEKT} explizit NICHT sein soll. Wichtig zur Scope-Verteidigung gegen späteres Feature-Creep.

## Architektur-Skizze

### Komponenten
- Frontend: …
- Backend: …
- Datenhaltung: …

### Datenfluss
Wie fließen Daten durch das System? Welche Komponente kommuniziert mit welcher? Wo sind die Grenzen?

### Designprinzipien
- Prinzip 1 (z.B. „Handy zuerst")
- Prinzip 2 (z.B. „Keine Auth innerhalb Tailscale-Netz")

## Look & Feel
Optisches Konzept — Farben, Typografie, Inspiration, Referenzbilder. Für UI-Defaults globale `DESIGN.md` referenzieren statt duplizieren.

## Offene Designfragen
Verweis auf `DECISIONS_{PROJEKT}.md`.

## Referenzen
- Verwandte Designs, Inspirationen, Vorbilder
- Externe Doku, Spezifikationen
