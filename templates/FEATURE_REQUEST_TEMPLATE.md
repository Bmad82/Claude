<!-- TEMPLATE | dateiname FEATURE_REQUEST_{kurzname}.md (kebab-case aus frontmatter) — NIE projektname als filename | kopie ins projekt-root | coda arbeitet diese datei beim session-start als prioritaet ab -->

FEATURE_REQUEST: {auftrags-titel}
datum | {YYYY-MM-DD}
auftraggeber | supervisor (chat) | chris (direkt)
empfaenger | coda
kurzname | {kurz-eindeutig, kein leerzeichen}
erwartete dauer | {N sessions}

KONTEXT
{warum dieser auftrag? 2-5 saetze, geschaeftsmotivation nicht "ich hab lust". vor-auftrag → verweisen. quelle/konzept-datei → pfad nennen}
quelle (falls vorhanden) | {pfad zur konzept-datei}

AKZEPTANZKRITERIEN (TL;DR)
- [ ] {kriterium 1 — binaer abpruefbar}
- [ ] {kriterium 2 — binaer abpruefbar}
- [ ] {kriterium N — binaer abpruefbar}
- [ ] selbsttest A-D durchgelaufen (bei workflow-themen pflicht)
- [ ] commit + push erfolgt, $LASTEXITCODE = 0 verifiziert
- [ ] HANDOVER.json mit status-header geschrieben

SCHRITT 01 — {titel}
{beschreibung. konkrete done-definition am ende}

SCHRITT 02 — {titel}
{...}

SCHRITT 0N — selbsttest (phase A-D, PFLICHT bei workflow-themen)
A setup | {zustand erzeugen der das neue pattern triggert}
B replay (frischer kontext) | {sub-agent oder zweite session simuliert frische coda-aufnahme}
C adversarial (konflikt provozieren) | {gegnerische aktion + pruefung ob schutz greift}
D cleanup | {test-artefakte loeschen + listing der working-tree-root verifiziert sauberkeit}

SCHRITT 0M — commit + push
branch | {main | worktree-name}
commits idealerweise getrennt: 1 {feat|fix|refactor}({scope}): {1-satz} | 2 ...
push auf origin/{branch}, $LASTEXITCODE = 0 verifizieren
bei fehler: in HANDOVER.json unter BLOCKIERT dokumentieren, auf deutsch

SCHRITT 0L — HANDOVER.json schreiben
ueberschreibe {projekt-root}/HANDOVER.json mit status-header (FERTIG|IN_ARBEIT|BLOCKIERT) + fortschritt + was-chris-physisch-tun-muss + auftragshistorie
vorlage C:\Users\chris\Python\Claude\templates\HANDOVER_TEMPLATE.json

WICHTIGE HINWEISE
- token-opt fuer alle maschinen-files (lessons/CLAUDE/SUPERVISOR/MARATHON_WORKFLOW: artikelfrei, pipe, keine ##/fett) | prosa fuer mensch-files (README/DESIGN/ROADMAP) | niemals mischen innerhalb einer datei
- konflikt/unklarheit → nicht raten | in DECISIONS_PENDING.md festhalten + in HANDOVER.json unter BLOCKIERT verweisen
- erkenntnis → finding in FINDINGS_{PROJEKT}.md (read-only-modell), keine lesson direkt schreiben
- quellen-files bleiben unveraendert liegen | verteilung ueber GLOBAL_LESSONS/SUPERVISOR_KODEX/templates, nicht durch verschieben der ursprungsdatei

LIFECYCLE | FERTIG: rename _ERLEDIGT.md | IN_ARBEIT: datei bleibt, HANDOVER.json traegt status | BLOCKIERT: datei bleibt + grund in DECISIONS_PENDING.md | QUEUED: neuer FR waehrend IN_ARBEIT → _QUEUED.md
