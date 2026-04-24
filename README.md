# Claude Global Knowledge Base

Globales Repo für Claude-Templates und Lessons-Learned.
Wird in jedem Projekt als Wissensquelle eingebunden.

⚠️ **DIESES REPO IST PUBLIC.**
Niemals Passwörter, API-Keys, Tokens, persönliche Daten, IP-Adressen,
interne URLs, Hostnamen oder projektspezifische Secrets reinschreiben.
Im Zweifel: NICHT committen und nachfragen.

## Struktur
- `templates/` — Vorlagen für CLAUDE.md und SUPERVISOR.md (nur manuell ändern)
- `lessons/` — Projektübergreifende Lessons-Learned (darf von Claude Code beschrieben werden)
- `DESIGN.md` — Globale Design-Referenz (Farben, Typography, Komponenten, Mobile-Regeln). Lebendes Dokument, wird direkt referenziert, nicht kopiert.

## Einbindung in Projekte
In der projekt-eigenen CLAUDE.md am Anfang:
> Globale Wissensbasis: https://github.com/Bmad82/Claude
> Vor Arbeitsbeginn: `lessons/`-Ordner auf relevante Einträge prüfen.
> Nach Abschluss: Neue universelle Erkenntnisse dort eintragen.

## ⚠️ Dateinamen-Konvention (WICHTIG)

Projektspezifische Dateien tragen IMMER den Projektnamen als Suffix:
- `CLAUDE_[PROJEKTNAME].md` — z.B. `CLAUDE_ZERBERUS.md`
- `SUPERVISOR_[PROJEKTNAME].md` — z.B. `SUPERVISOR_ZERBERUS.md`

Die Templates in `templates/` sind Schablonen für Tag 1 eines neuen Projekts.
- Templates werden EINMAL bei Projekterstellung kopiert → danach irrelevant
- Wenn ein Projekt bereits `CLAUDE_[PROJEKT].md` hat: Templates NICHT anfassen
- `lessons/` hingegen ist lebendig — wird bei JEDEM Patch konsultiert und ergänzt

Claude Code darf Templates lesen, aber NIEMALS eine `CLAUDE_[PROJEKT].md`
mit einem Template überschreiben oder zusammenführen.
