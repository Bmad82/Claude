<!-- TEMPLATE | Kopie als CLAUDE_{PROJEKTNAME}.md anlegen | NIE bestehende Projekt-CLAUDE-Datei überschreiben -->

# CLAUDE_{PROJEKTNAME}.md | Bibel-Format

## Identität
Du bist {AGENTNAME}. Du baust {PROJEKTNAME}.

## Session-Start-Pflicht
1. FEATURE_REQUEST_{PROJEKTNAME}.md prüfen | existiert? → sofort abarbeiten | Priorität 1 | nach Abarbeitung → Rename zu FEATURE_REQUEST_{PROJEKTNAME}_ERLEDIGT.md
2. HANDOVER_{PROJEKTNAME}.md lesen
3. MARATHON_WORKFLOW_{PROJEKTNAME}.md lesen
4. lessons_{PROJEKTNAME}.md konsultieren

## Globale Wissensbasis
Repo: https://github.com/Bmad82/Claude | PUBLIC | keine Secrets/Keys/Tokens/IPs/interne URLs in Lessons/Templates
Lessons-Verzeichnis: C:\Users\chris\Python\Claude\lessons\
Templates-Verzeichnis: C:\Users\chris\Python\Claude\templates\
Bug-Tracker: C:\Users\chris\Python\Claude\bugs\{PROJEKTNAME}\

## Projektpfad
{PFAD}

## Tech-Stack
Backend|{...}
Frontend|{...}
DB|{...}
Auth|{...}
Port|{...}
Startskript|{...}

## Regeln
1. Erst lesen | dann schreiben | keine blinden Überschreibungen
2. .env niemals nach außen leaken | nicht in Logs
3. DB-Schema-Änderung | Backup vor Patch
4. Nur ändern was Patch braucht | kein opportunistisches Refactoring
5. Diagnose vor Fix | grep/Select-String | Pfad identifizieren
6. Unsicherheit → fragen | nicht raten
7. Keine Annahmen über Dateninhalte | immer verifizieren

## Handy-First
- Mobile Viewport zuerst | Desktop danach
- Touch-Targets ≥ 44px (≥ 48px bevorzugt)
- `:active` zusätzlich zu `:hover` | Touch hat kein Hover
- `dvh` statt `vh` | Keyboard-Overlay-Schutz
- Überstehende Elemente|horizontales Scrollen|abgeschnittene Texte = Blocker
- `backdrop-filter` braucht Fallback
- `@media (orientation: landscape) and (max-height: 500px)` für Landscape-Edge

## Whisper-Eingaben
75% per Spracheingabe | phonetische Wortdreher normal | beabsichtigte Bedeutung priorisieren | bei Unlogik fragen statt raten

## Doku-Pflicht nach Patch
| Datei | Trigger | Limit |
|---|---|---|
| CLAUDE_{PROJEKTNAME}.md | Architektur-Änderung | < 150 Zeilen |
| SUPERVISOR_{PROJEKTNAME}.md | jeder Patch | < 400 Zeilen |
| MARATHON_WORKFLOW_{PROJEKTNAME}.md | jeder Patch | Status-Spalte |
| CHANGELOG.md | jeder Patch | vollständig |
| README.md | UI/CLI/API-Change | Patch-Nr im Footer |
| mjolnir.md | Session-Ende | ephemer, wird gelöscht |
| lessons_{PROJEKTNAME}.md | jeder ≥2-Min-Stolperstein | Bibel-Format |

## Git-Pflicht nach Patch
1. Tests ausführen | Ergebnis prüfen
2. `git add -A`
3. `git commit -m "Patch XX – {Kurztitel}"`
4. `git push` | `$LASTEXITCODE` prüfen | bei Fehler User informieren
5. SUPERVISOR_{PROJEKTNAME}.md updaten

## Git-Workflow am Session-Ende
1. Commit + Push: `git push -u origin <branch>` (erstes Mal) | später `git push`
2. In main mergen: `git checkout main` | `git merge <branch>` | `git push origin main` | `git checkout <branch>`
3. Worktree NICHT löschen | Sicherheitsnetz
Merge-Konflikt → eskalieren | nicht eigenmächtig destruktiv

## Stopp-Regeln
- Kontext < 400k Token → sauber abschließen | HANDOVER_{PROJEKTNAME}.md schreiben
- Test-Failure → fixen VOR nächstem Feature
- Blockiert → DECISIONS_PENDING_{PROJEKTNAME}.md | nächsten unabhängigen Patch
- Lessons konsultieren VOR Aufgabe | eintragen NACH ≥2-Min-Falle

## mjolnir.md-Konvention
Coding-Session schreibt am Ende mjolnir.md ins Projektroot | 5-10 Zeilen | Patch-Stand | offene Punkte | Fehler | wird beim nächsten Session-Start gelesen+gelöscht

## Ausgabe-Regeln
- Prompts + strukturierte Ausgaben als .md-Datei | kein Inline-Text
- Datei self-contained | mobilfreundlich kopierbar

## Sicherheit
- {projektspezifische Auth/Allowlist}
- File-Upload | Basename | keine Dot-Files | keine `..`-Sentinels
- Subprocess | argv-Liste statt shell=True | hartcodierte Befehle bei Utility-Aktionen

## Endpoints/Module
{Tabelle mit Endpoints oder Modulen}

## Namen
{Naming-Konvention für Codenamen}
