# AUFTRAG: Info-Paket für Supervisor (Repo-Restrukturierung)

## Kontext
Der Supervisor (Chat-Instanz) plant die Restrukturierung des `Bmad82/Claude`-Repos. Er hat die mjolnir-Zusammenfassung der Inventur gelesen, braucht aber die Details. Dieser Auftrag ist **reine Informationslieferung** — du änderst nichts, du räumst nichts auf, du pushst nichts.

## Was du liefern sollst

Erstelle eine Datei `SUPERVISOR_BRIEFING.md` im Repo-Root mit folgenden Sektionen:

### Sektion 1: Vollständiger Directory-Tree
```bash
find . -not -path './.git/*' -not -path './.claude/worktrees/*' | sort
```
Plus separat:
```bash
find ./.claude/worktrees/ -not -path './.git/*' 2>/dev/null | head -30
```

### Sektion 2: REPO_INVENTORY.md — Volltext
Cat die komplette `REPO_INVENTORY.md` hier rein. Der Supervisor kann sie nicht sehen, weil sie nicht gepusht wurde oder GitHub sie nicht zeigt.

### Sektion 3: Sprach-Audit
Für JEDE .md und .html Datei im Repo (außer Worktree): 
- Dateiname
- Hauptsprache (DE / EN / gemischt)
- Geschätzter DE-Anteil in Prozent (grob reicht)
- Einzeiler: Worum geht es inhaltlich?

### Sektion 4: Duplikat-Check
Gibt es Dateien, die inhaltlich dasselbe oder fast dasselbe abdecken? Liste Paare/Gruppen auf mit kurzer Begründung warum du Überlappung siehst.

### Sektion 5: Antworten auf Supervisor-Fragen

**F1:** Die `zerberus_lessons.md` ist 300KB groß laut Inventur. Was steht da drin — ist das eine Kopie der Zerberus-Projekt-Lessons, oder ist das was Eigenständiges? Gehört die hierher oder ins Zerberus-Repo?

**F2:** Was ist der Unterschied zwischen `LESSONS_KONSOLIDIERT.md` und dem `lessons/`-Ordner? Redundanz oder verschiedene Scope?

**F3:** Was liegt in `_drafts_gist`? Ist das leer/Platzhalter, oder gibt es Inhalt?

**F4:** Welche Dateien haben `_ERLEDIGT` im Namen? Liste sie auf.

**F5:** Was steht in `DESIGN.md`? Ist das ein echtes Design-Dokument oder nur ein Skelett mit Platzhaltern?

**F6:** Der `bugs/`-Ordner — was liegt da drin, und ist das alles Zerberus-spezifisch?

**F7:** Gibt es eine `.claude/`-Konfiguration (CLAUDE.md, settings, commands) im Repo? Wenn ja, was steht drin?

**F8:** Welche Dateien sehen so aus, als wären sie Showcase-Material (HTML-Seiten, Präsentationen etc.)?

**F9:** Gibt es Dateien die offensichtlich temporär/vergessen sind und bedenkenlos gelöscht werden könnten?

**F10:** Wie sieht die aktuelle README.md aus? Volltext bitte.

### Sektion 6: Deine Einschätzung
Als jemand der das Repo gerade komplett durchgelesen hat: Was ist der größte strukturelle Pain-Point? Was würdest du als Erstes anfassen, wenn du es aufräumen dürftest? (Nur Einschätzung, keine Umsetzung.)

## Output
Alles in `SUPERVISOR_BRIEFING.md` im Repo-Root. Dann `git add`, `git commit -m "docs: Supervisor-Briefing für Repo-Restrukturierung"`, `git push`. Push-Erfolg mit `$LASTEXITCODE` verifizieren, Ergebnis ins mjolnir.

## Akzeptanzkriterien
- [ ] Alle 6 Sektionen sind befüllt
- [ ] REPO_INVENTORY.md ist im Volltext enthalten (nicht nur Verweis)
- [ ] Jede .md/.html hat einen Sprach-Audit-Eintrag
- [ ] Alle 10 Fragen sind beantwortet
- [ ] Datei ist gepusht und Push verifiziert
- [ ] Nichts anderes wurde verändert
