<!-- TEMPLATE | Kopie als DECISIONS_{PROJEKT}.md ins Projekt-Root | Architektur-Entscheidungen + offene Fragen | ergänzt globales DECISIONS_PENDING.md (Meta-Layer) -->

# DECISIONS_{PROJEKT}.md | Bibel-Format
Architektur-Entscheidungen {PROJEKT} | jede Entscheidung mit Datum+Begründung | offene Fragen separat

## Verhältnis zu DECISIONS_PENDING.md (global)
- `C:\Users\chris\Python\Claude\DECISIONS_PENDING.md` = Meta-Layer (Workflow/Marathon/Tooling)
- `DECISIONS_{PROJEKT}.md` = Projekt-Layer (Tech-Stack, Datenmodell, Auth, Port)
Bei Unsicherheit Meta-Layer prüfen, dann hier.

## Getroffene Entscheidungen

### {DATUM} | {Titel}
Entscheidung|{1-Satz Was}
Begründung|{Warum}
Alternativen|{verworfene Optionen + Grund}
Konsequenz|{was muss/wird sich ändern}
Patch-Referenz|P{N}

## Offene Entscheidungen (Pending)

### {Titel}
Frage|{konkrete Frage an Architekt}
Hintergrund|{warum stellt sich die Frage}
Optionen|A) {…} | B) {…} | C) {…}
Blockiert|Patch {N} oder Phase {X}
Eingetragen|{DATUM}
