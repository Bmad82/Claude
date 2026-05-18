# AUFTRAG: Vollständige Repo-Inventur

## Kontext
Das Repo `Bmad82/Claude` soll aufgeräumt und neu strukturiert werden. Erster Schritt: eine komplette Bestandsaufnahme von ALLEM was hier liegt.

## Was du tun sollst

1. **Vollständiger Directory-Tree** — Rekursiv, alle Ebenen, keine Ausnahmen. Auch versteckte Dateien (`.gitignore`, `.github/` etc.), auch leere Ordner.

```bash
find . -not -path './.git/*' | sort
```

2. **Datei-Inventar als Tabelle** — Für JEDE Datei (nicht Ordner):

| Pfad | Typ | Sprache | Größe | Letzte Änderung | Kurzbeschreibung (1 Satz) | Status-Einschätzung |
|------|-----|---------|-------|-----------------|---------------------------|---------------------|

- **Typ**: md, html, py, json, template, config, bild, sonstig
- **Sprache**: DE, EN, gemischt
- **Status-Einschätzung**: `AKTUELL` / `VERALTET` / `UNKLAR` / `MÜLL` — basierend auf Inhalt, Datum, ob es referenziert wird

3. **Ordnerstruktur-Beschreibung** — Für jeden Ordner/Unterordner: Was scheint der Zweck zu sein? Gibt es eine erkennbare Logik?

4. **Auffälligkeiten melden**:
   - Dateien die doppelt oder fast-doppelt aussehen
   - Dateien ohne erkennbaren Zweck
   - Leere oder fast-leere Dateien
   - Dateien die offensichtlich woanders hingehören
   - Namenskonflikte (z.B. mehrere CLAUDE.md, README.md etc.)

## Output-Format

Gib alles in EINER Markdown-Datei aus: `REPO_INVENTORY.md`
Speichere sie im Repo-Root.

## Was du NICHT tun sollst

- Nichts löschen
- Nichts verschieben
- Nichts umbenennen
- Keine Strukturvorschläge machen (das kommt im nächsten Schritt)
- Kein `git push` — nur lokale Datei erstellen

## Akzeptanzkriterien

- [ ] `find`-Output ist vollständig (ohne `.git/`)
- [ ] Jede Datei hat einen Eintrag in der Tabelle
- [ ] Jeder Ordner hat eine Zweck-Beschreibung
- [ ] Auffälligkeiten-Sektion existiert (auch wenn leer)
- [ ] `REPO_INVENTORY.md` liegt im Repo-Root
- [ ] Nichts wurde verändert außer der neuen Datei
