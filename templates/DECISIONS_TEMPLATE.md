<!-- TEMPLATE | kopie als DECISIONS_{PROJEKT}.md ins projekt-root | architektur-entscheidungen + offene fragen | ergaenzt globales DECISIONS_PENDING.md (meta-layer) -->

DECISIONS_{PROJEKT}.md | maschinen-only | token-opt
architektur-entscheidungen {PROJEKT} | jede entscheidung mit datum+begruendung | offene fragen separat

VERHAELTNIS zu DECISIONS_PENDING.md (global)
C:\Users\chris\Python\Claude\DECISIONS_PENDING.md = meta-layer (workflow/marathon/tooling)
DECISIONS_{PROJEKT}.md = projekt-layer (tech-stack, datenmodell, auth, port)
bei unsicherheit meta-layer pruefen, dann hier

GETROFFENE ENTSCHEIDUNGEN
{DATUM} | {titel}
entscheidung | {1-satz was}
begruendung | {warum}
alternativen | {verworfene optionen + grund}
konsequenz | {was muss/wird sich aendern}
patch-referenz | P{N}

OFFENE ENTSCHEIDUNGEN (pending)
{titel}
frage | {konkrete frage an architekt}
hintergrund | {warum stellt sich die frage}
optionen | A) {...} | B) {...} | C) {...}
blockiert | patch {N} oder phase {X}
eingetragen | {DATUM}
