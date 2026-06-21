<!-- TEMPLATE | kopie als CLAUDE_{PROJEKT}.md ins projekt-root | limit <150 zeilen (ziel ~100) | task-regeln in playbooks/, pfad-regeln in .claude/rules/ mit globs:-frontmatter (mw-v2b paket 2) | NIE bestehende projekt-CLAUDE-datei ueberschreiben -->
<!-- ab 2026-06-15: claude -p faellt in credit-pool (api-vollpreis), interaktive sessions bleiben im abo | headless-sessions (z.b. via mjolnir) auf interaktiv umstellen | siehe GLOBAL_LESSONS billing-split-faustformel -->

CLAUDE_{PROJEKT}.md | maschinen-only | token-opt (artikelfrei, pipe, keine ##, kein fett)

IDENTITAET
du bist coda | du baust {PROJEKT}

REGEL-0 — faulheits-catches (gilt VOR jeder anderen regel)
volltext: GLOBAL_LESSONS.md sektion DIE-6-FAULHEITS-CATCHES-INDEX. kurzform:
1 coda terminalisiert NICHTS was coda kann — kein git/pytest/pip/robocopy/npm an chris
2 HANDOVER.json PFLICHT am session-ende — single-slot mit status-header, ausnahmslos
3 worktree-branches selbst auf main mergen — kein "schritt 0 fuer chris"
4 supervisor baut coda-prompts statt terminal-befehle — gilt auch im chat
5 multi-session-status-header + QUEUED-pattern — multi-session-auftraege nicht ueberschreiben
6 selbsttest-pflicht fuer workflow-aenderungen — phase A-D, hoffnung != verifikation

SESSION-START-PFLICHT
1 konflikt-check | HANDOVER.json mit STATUS:IN_ARBEIT UND FEATURE_REQUEST_{PROJEKT}.md mit abweichendem kurznamen? → neuen FR zu _QUEUED.md, alten auftrag aus HANDOVER.json rekonstruieren, zuerst fertig
2 FEATURE_REQUEST_{PROJEKT}.md pruefen | existiert? → sofort abarbeiten, prioritaet 1 | nach STATUS=FERTIG → rename _ERLEDIGT.md
3 HANDOVER.json einlesen (status-header zuerst), NICHT loeschen (status wird ueberschrieben, historie append-only)
4 SCHALTPLAN_PROJEKT.json lesen (projekt-gedaechtnis: module, status, brueche)
5 MARATHON_WORKFLOW_{PROJEKT}.md lesen
6 python scripts/lessons_lookup.py --task '<aufgabe>' (tf-idf top-3, ~500 token) | 0 treffer → "aufgabe neu", kein stuffing | NICHT lessons_{PROJEKT}.md komplett laden (mw-v2a paket 1)
7 globale quellen: GLOBAL_LESSONS.md, SUPERVISOR_KODEX.md | task-regeln aus playbooks/<task>.md, pfad-regeln aus .claude/rules/ (mw-v2b paket 2)

READ-ONLY-LESSONS | lessons/GLOBAL_LESSONS/templates/gists sind read-only | coda schreibt KEINE lesson direkt | erkenntnis (>=2-min-stolperstein) → finding in FINDINGS_{PROJEKT}.md (vorlage templates/FINDING_TEMPLATE.md) | der cron promoviert (templates/CRON_PROMOTION_SPEC.md)

GLOBALE-WISSENSBASIS
repo https://github.com/Bmad82/Claude | PUBLIC | keine secrets/keys/tokens/ips/interne-urls in lessons/templates
GLOBAL_LESSONS | C:\Users\chris\Python\Claude\GLOBAL_LESSONS.md
SUPERVISOR_KODEX | C:\Users\chris\Python\Claude\SUPERVISOR_KODEX.md
templates | C:\Users\chris\Python\Claude\templates\
bootstrap | C:\Users\chris\Python\Claude\PROJECT_BOOTSTRAP_README.md
lessons | C:\Users\chris\Python\Claude\lessons\
bug-tracker | C:\Users\chris\Python\Claude\bugs\{PROJEKT}\

PROJEKTPFAD | {PFAD}

TECH-STACK
backend|{...} frontend|{...} db|{...} auth|{...} port|{...} startskript|{...}

NEUSTART-LOKALER-DIENSTE (R-CLEAN-RESTART, global) | endzustand immer: genau EINE instanz, EIN fenster, nie zombie-stapel
grundsatz | neustart lang laufenden lokalen dienstes beendet alt-instanz VOLLSTAENDIG vor start der neuen
drei ebenen muessen weg | (1) prozess (2) reloader-kinder (3) terminal-fenster | alle drei, nicht nur ebene 1
prozess!=fenster | prozess-kill schliesst cmd/terminal-fenster NICHT (fenster = eigener prozess cmd.exe) | sonst stapeln sich offene fenster
reloader | --reload/watchfiles spawnt parent+worker-child | simpler pid-kill erwischt nur einen → anderer verwaist, haelt port+vram | beide killen
methode | fenstertitel- oder portbasiert beenden | NIE breiter interpreter-kill (taskkill /IM python.exe nuked ALLE python-tools) | muster: instanz in fest betiteltes fenster starten → vor neustart alles mit dem titel killen → fenster+prozess+reloader-kind in einem rutsch
gate | nach neustart verifizieren: nur EIN prozess auf dem port, nur EIN fenster | pruefen, nicht annehmen

REGELN (zusaetzlich zu regel 0)
1 erst lesen | dann schreiben | keine blinden ueberschreibungen
2 .env nie leaken | nicht in logs
3 db-schema-aenderung | backup vor patch
4 nur aendern was patch braucht | kein opportunistisches refactoring
5 diagnose vor fix | grep/Select-String | pfad identifizieren
6 unsicherheit → DECISIONS_PENDING.md | nicht raten
7 keine annahmen ueber dateninhalte | immer verifizieren

HANDY-FIRST | mobile viewport zuerst | touch-targets >=44px (>=48 bevorzugt) | :active zusaetzlich zu :hover | dvh statt vh (keyboard-overlay)

WHISPER-EINGABEN | 75% sprachdiktat | phonetische wortdreher normal | intention priorisieren | bei unlogik fragen statt raten

DOKU-PFLICHT nach patch (datei | trigger | limit)
CLAUDE_{PROJEKT}.md | architektur-aenderung | <150 zeilen
SUPERVISOR_{PROJEKT}.md | jeder patch | <400 zeilen
MARATHON_WORKFLOW_{PROJEKT}.md | jeder patch | status-spalte
CHANGELOG.md | jeder patch | vollstaendig
README.md | ui/cli/api-change | patch-nr im footer
HANDOVER.json | session-ende | PFLICHT ausnahmslos — status-kopf ueberschreiben + 1 historie-eintrag
SCHALTPLAN_PROJEKT.json | fenster-ende VOR handover | projekt-gedaechtnis module/status/brueche, gestrichenes ('—') sichtbar lassen
HUMAN_TESTS.json | sobald mensch-test auftaucht/abgehakt | offene geraete-/mikrofon-/touch-/vram-tests
FINDINGS_{PROJEKT}.md | jeder >=2-min-stolperstein | finding ablegen (read-only-modell) — coda schreibt KEINE lesson direkt
REPO_INDEX.md | verzeichnisaenderung in session | verzeichnisbaum, vor finalem push (repo-intern)
projekt-gist (STATUS, HANDOVER, SCHALTPLAN, REPO_INDEX, LESSONS) | session-ende | PATCH via gist_publisher.py, nach push

REPO_INDEX-PFLICHT
- REPO_INDEX.md im repo-root ist pflicht (repo-interne navigation)
- bei verzeichnisaenderungen am session-ende aktualisiert, VOR dem finalen push
- format: verzeichnisbaum | KEINE raw-link-tabelle — der supervisor (chat) kann github-raw-links nicht fetchen
- keine verzeichnisaenderung → REPO_INDEX nicht anfassen (kein diff-noise)
- zweck: repo-ueberblick | der supervisor liest den stand ueber den projekt-gist (REPO_INDEX liegt im gist-set), nicht ueber raw-links

GIST-PFLICHT
- jedes projekt hat einen PUBLIC gist mit briefing-dateien (STATUS, HANDOVER, SCHALTPLAN, REPO_INDEX, LESSONS)
- gist-url in GIST_LINK.md im repo-root
- gist am session-ende aktualisiert (mit lokalen dateien) — helfer workflow/gist_publisher.py aus dem Claude-repo
- index-gist nur bei neuem projekt aktualisieren
- hintergrund: supervisor (claude.ai chat) kann raw-links nicht fetchen, gists schon — kein auth-bedarf

GIT-PFLICHT nach patch (coda macht das SELBST)
1 tests ausfuehren | ergebnis pruefen
2 verzeichnisaenderungen? → REPO_INDEX.md aktualisieren
3 git add (gezielt, nicht -A)
4 git commit -m "Patch XX – {kurztitel}"
5 git push | $LASTEXITCODE pruefen | bei fehler: BLOCKIERT in HANDOVER.json
6 SUPERVISOR_{PROJEKT}.md updaten

GIT-WORKFLOW am session-ende
1 eigene branch-edits committen + pushen
2 worktree-branch SELBST auf main mergen (kein auftrag an chris): merge --ff-only oder rebase + ff-merge
3 worktree NICHT loeschen | sicherheitsnetz
4 merge-konflikt → DECISIONS_PENDING.md + BLOCKIERT in HANDOVER.json, nicht destruktiv
5 projekt-gist aktualisieren (PATCH via workflow/gist_publisher.py): STATUS, HANDOVER, SCHALTPLAN, ggf. REPO_INDEX, LESSONS
6 HANDOVER.json traegt gist-url (oder verweis auf GIST_LINK.md)

STOPP-REGELN
- kontext <400k → sauber abschliessen | SCHALTPLAN_PROJEKT.json pflegen | HANDOVER.json STATUS=IN_ARBEIT
- test-failure → fixen VOR naechstem feature
- blockiert → DECISIONS_PENDING.md | STATUS=BLOCKIERT in HANDOVER.json | naechsten unabhaengigen patch
- repair: bei wand lessons_lookup auf wand-text, anwenden UND melden (nie still), niedriger match-score → frueh eskalieren | N waende ungebrochen → BLOCKIERT (repair-eskalations-protokoll, GLOBAL_LESSONS.md)

SESSION-AUFFUELL-REGEL (Kintsugi-migration 2026-05-21)
primaerauftrag fertig UND <300k → weiterarbeiten, nicht abschliessen | reihenfolge: FR-restpunkte > MARATHON_WORKFLOW-offen > backlog > test-schulden > doku-hygiene | stopp ~350k (50k reserve) | zwischen-patches eigener commit, aber EIN handover am session-ende | AUSNAHME: destruktive/riskante patches nie als auffueller

STEUER-FILES: schaltplan (gedaechtnis) + handover (staffelstab) + human-tests
json ist ssot, die .html-renderer sind reine anzeige — nie mischen
- SCHALTPLAN_PROJEKT.json | gedaechtnis | modul-/abhaengigkeitskarte: module, status (IST/TEIL/PLAN/—), brueche, verworfene ansaetze | status nur mit ref-beleg | gestrichenes ('—') bleibt sichtbar | alles DAUERHAFTE hier | vorlage templates/SCHALTPLAN_PROJEKT_TEMPLATE.json
- HANDOVER.json | staffelstab | NUR heisser in-flight-kontext: status-kopf (komplett ueberschrieben) + historie (append-only, 1 eintrag/lauf) + was-chris-physisch-tun-muss | verworfene ansaetze/brueche NICHT hier (→ schaltplan) | vorlage templates/HANDOVER_TEMPLATE.json
- HUMAN_TESTS.json | offene mensch-tests (kategorien → items, abhak-status) | vorlage templates/HUMAN_TESTS_TEMPLATE.json
wiedereinstieg liest: schaltplan (volle wahrheit) + die letzten 1-2 handover-historie-eintraege | am fenster-ende: erst schaltplan pflegen, dann handover schreiben

AUSGABE-REGELN | prompts + strukturierte ausgaben als .md-datei, kein inline-text | self-contained, mobilfreundlich kopierbar

SICHERHEIT
- {projektspezifische auth/allowlist}
- file-upload | basename | keine dot-files | keine ..-sentinels
- subprocess | argv-liste statt shell=True

ENDPOINTS/MODULE | {tabelle mit endpoints oder modulen}

NAMEN | {naming-konvention fuer codenamen}
