<!-- TEMPLATE | Kopie als HANDOVER_{PROJEKT}.md ins Projekt-Root | Detail-Übergabe zwischen Sessions | ergänzt mjolnir.md (Status-Layer), nicht ersetzt -->

# HANDOVER_{PROJEKT}.md | Bibel-Format
Letzte Session: Patch {N} ({DATUM}) | Nächste Session liest dies NACH mjolnir.md, VOR MARATHON_WORKFLOW

## Verhältnis zu mjolnir.md
mjolnir.md = Single-Slot-Status (STATUS-Header + was-Chris-physisch-tun-muss, ephemer)
HANDOVER.md = Detail-Layer (technische Stände, Test-Status, nächste Schritte — bleibt zwischen Sessions)

## Stand
Patch|{N}
Branch|{branch}
Status|{grün|gelb|rot}
Letzte Aktion|{1-Satz}

## Was läuft
- {konkreter Stand was funktioniert}

## Was offen ist
1. {nächster logischer Schritt}
2. {danach}

## Bekannte Bugs/Risiken
- {Bug oder Risiko mit Severity}

## Tests-Status
| Bereich | Stand | Hinweis |
|---|---|---|
| Smoke | grün/rot | {n/n} |
| Unit | grün/rot | {n/n} |
| Live | grün/rot | {Datum} |

## Letzte Commits
- {hash} {Titel}

## Nächster Patch
Scope|{1-Satz}
Berührte Dateien|{Liste}
Risiko|{niedrig/mittel/hoch}

## Kontext-Hinweise
- {was Coda beim Wiedereinstieg wissen muss aber nicht offensichtlich ist}
