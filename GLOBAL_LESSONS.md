GLOBAL_LESSONS | Marathon-Workflow | maschinen-only | gilt fuer ALLE Projekte (Coda + Supervisor + Cron)
schema je lesson: wall_signatur | kategorie | fix | kontext | quelle
wall_signatur = literale symptom-/trigger-vokabeln fuer den tf-idf-lookup (error-klasse, traceback-phrase, lib-name, literal-strings) — nicht die loesung umschreiben
kontext = eine zeile anwendungsgrenze (wann gilt die lesson, wann nicht)
projektspezifisches NICHT hierher — gehoert als finding ins project-root, der cron promoviert (siehe READ-ONLY + REPAIR-PROTOKOLL unten)
historie nicht loeschen, neue lessons oben anhaengen | namens-stand: uebergabe-modell = HANDOVER.json + SCHALTPLAN_PROJEKT.json + HUMAN_TESTS.json (das alte mjolnir.md/handover.md ist tot)

READ-ONLY-GLOBALE-SCHICHT
lessons + templates (lessons/, templates/, GLOBAL_LESSONS.md, SUPERVISOR_KODEX.md, die gists) sind READ-ONLY fuer supervisor, worker, solver-worker | diese rollen schreiben NIE in die globale schicht
erkenntnis aus einer session → worker/solver legt ein FINDING im project-root ab (vorlage templates/FINDING_TEMPLATE.md), nicht in lessons/gists/GLOBAL_LESSONS/irgendwo sonst
der high-reasoning-cron (pro projekt, separat) ist der EINZIGE schreiber der globalen schicht: er fetcht findings, urteilt ueber generalisierbarkeit, promoviert taugliche zu globalen lessons/templates (spec: templates/CRON_PROMOTION_SPEC.md, docking be.cron.lessons/be.cron.rules in schaltplan/fabrik_meta_workflow.json)

REPAIR-ESKALATIONS-PROTOKOLL
1 | diagnose gehoert zum worker | supervisor gibt richtung, sieht nie code, diagnostiziert nie
2 | lookup auf wand-text nicht task-text | build: supervisor kennt kategorie, benennt build-lessons | repair: nur worker kennt die wand, holt selbst per lessons_lookup | gleicher lookup, anderer input/zeitpunkt
3 | lookup re-triggert mittendrin | neue wand → neuer lookup auf neuen wand-text
4 | anwenden ja aber melden, nie still | wand + angewandte lesson + ergebnis nach oben signalisieren | stilles selbstheilen = durchrattern
5 | niedriger match-score = undokumentierte wand → frueh eskalieren, nicht blind force-fitten
6 | N waende ungebrochen → STATUS=BLOCKIERT → eskalation | merge-konflikte und undokumentierte waende laufen ueber denselben kanal an den menschen | merge ist eine wahl (seite/3-way-diff), kein blosses approve
7 | eskalation fuettert den korpus read-only-konform | solver schreibt KEINE lesson, legt ein finding im project-root ab | befoerderung zur globalen lesson macht ausschliesslich der cron

wall_signatur | dienst-neustart laesst alt-instanz leben, zombie-stapel, mehrere terminal-fenster, port/vram belegt nach restart, --reload watchfiles parent+worker verwaist, taskkill /IM python.exe nuked alle tools, uvicorn flask reloader pid-kill
kategorie | lokale-dienste/neustart
fix | neustart beendet alt-instanz VOLLSTAENDIG vor start der neuen, endzustand genau EINE instanz + EIN fenster | drei ebenen killen: prozess + reloader-worker-child + terminal-fenster (cmd.exe ist eigener prozess, prozess-kill schliesst fenster NICHT) | fenstertitel-/portbasiert beenden, NIE breiter interpreter-kill (taskkill /IM python.exe trifft ALLE python-tools) | muster: instanz in fest betiteltes fenster starten → vor neustart alles mit dem titel killen → fenster+prozess+reloader-kind in einem rutsch | gate danach: nur EIN prozess auf port + EIN fenster (pruefen, nicht annehmen)
kontext | jeder lang laufende lokale dienst mit neustart (uvicorn/flask --reload, watchfiles, dev-server) auf windows | reine einmal-skripte ohne reload unkritisch
quelle | R-CLEAN-RESTART global, 2026-06-21

wall_signatur | reasoning-modell max_tokens, finish_reason=length leerer output, openrouter long-context 2x preis, "bezahlt null output", cost_guard.py, $42-vorfall
kategorie | llm-api/cost-guard
fix | vor jedem llm-call: reasoning-modell→max_tokens>=3x antwortlaenge | prompt>128k→2x-multiplier einrechnen | hard cap pro call (default $5), teure modelle nur mit override | post-call finish_reason=length+leer = warnung | shared modul cost_guard.py importieren nicht kopieren
kontext | jeder neue llm-api-call vor deploy | long-context-tier oft nicht in /models ausgewiesen
quelle | Zerberus commit 3109cb1, 2026-06-13

wall_signatur | claude --bare deaktiviert hooks claude.md mcp skills UND oauth, erzwingt ANTHROPIC_API_KEY, abo-modus bricht
kategorie | claude-cli/flags
fix | nie --bare in abo-playbooks | stattdessen --settings ./config.json mit {"disableAllHooks":true} (deaktiviert hooks ohne auth-bruch)
kontext | gilt abo-/oauth-nutzer | im reinen api-modus unkritisch
quelle | GitHub #48840, ORCHESTRATOR_KONZEPT_v2 2026-05-23

wall_signatur | billing split abo vs credit-pool, wer tippt den prompt, claude -p agent-sdk github-actions credit-pool, interaktiv terminal abo
kategorie | anthropic-billing
fix | vor jeder integration fragen "wer tippt?": mensch am terminal = abo | maschine/script/cron = credit-pool zu api-raten
kontext | ab 2026-06-15 | agent-teams in-process = interaktiv, aber rate-limit proportional zu parallelen teammates
quelle | Anthropic billing-split 2026-05-14

wall_signatur | agent-sdk credits pro account, verfallen monatsende ohne claim, aktivierungs-mail-link beanspruchen
kategorie | anthropic-billing
fix | aktivierungs-mail (~2026-06-08) sofort anklicken | ohne claim vor 2026-06-15 kein credit
kontext | einmalig, danach automatische monatliche erneuerung | anthropic-aktivierungs-mails sind betriebsvoraussetzung, kein marketing
quelle | Anthropic Help 15036540

wall_signatur | claude-sonnet-4-20250514 opus-4-20250514 abgeschaltet, model-id mit datum-suffix stirbt, ImportError model not found
kategorie | anthropic/model-ids
fix | immer alias OHNE datum-suffix (claude-sonnet-4-6, claude-opus-4-6) | pre-flight grep -r "<altes-suffix>" ueber alle projekte als ci-check
kontext | datum-suffix nur als historischer marker in memos erlaubt, nie in config/code | betrifft llm-/guard-/persona-config, model-selector, openrouter-calls
quelle | Anthropic retirement-policy 2026-05-23

wall_signatur | CLAUDE.md zu gross, 500 regeln 68% befolgung, kontext-stuffing, playbooks, .claude/rules globs-frontmatter, paths: ignoriert
kategorie | kontext/regel-architektur
fix | kern-bibel max 150 (ziel 100) zeilen | task-regeln→playbooks/<task>.md | pfad-regeln→.claude/rules/<r>.md mit globs:-frontmatter (NICHT paths:, falsche syntax wird ignoriert) | rules opt-in via docs/claude_rules/ + readme (permission-protected)
kontext | frontier-modelle ignorieren ab ~200 regeln lautlos | bei wachsender regel-datei: raus/rein-splitten statt komprimieren (komprimieren versteckt, auslagern macht on-demand)
quelle | mw-v2b Paket 2, IFScale-Benchmark

wall_signatur | lessons komplett-load 80k token, bootstrap-overhead, tf-idf retrieval lessons_lookup.py, 0 treffer aufgabe neu
kategorie | kontext/lessons-lookup
fix | lessons nie komplett im session-start laden | python scripts/lessons_lookup.py --task '<aufgabe>' liefert top-3 (~500 token) | 0 treffer → explizite meldung "aufgabe evtl neu", kein stuffing
kontext | scikit-learn tf-idf reicht (exakte keyword-matches/funktionsnamen/patch-ids schlagen faiss, kein vram) | coda laedt per default keinen >5k-token-block, fragt gezielt
quelle | mw-v2a Paket 1

wall_signatur | patch-nummer phase tests commit-hash in N dateien manuell, stand-anker drift, STAND.json propagate_stand.py html-kommentar START END
kategorie | doku/ssot
fix | gemeinsame status-info in 1 ssot-file (STAND.json) + propagations-script | html-kommentar-marker <!-- STAND-ANKER:START --> .. END, regex-replace zwischen markern | idempotent + --dry-run + --check (ci-drift exit 1)
kontext | wenn dieselbe info in N dateien stehen MUSS | kein anker im target → warnung + block-snippet, keine auto-insertion (sicherheit > komfort)
quelle | mw-v2a Paket 3

wall_signatur | session-end checkliste 6 mechanische schritte, gist-patch uebersprungen, session_end.ps1, stop-hook
kategorie | workflow/automation
fix | mechanische pflicht-schritte in EIN tool buendeln (session_end.ps1), best-effort bei netzwerkfehler (warnung statt crash) | an stop-hook haengen → mechanisch erzwungen
kontext | wenn ein pflicht-schritt unter kontextdruck systematisch faellt: antwort ist "mechanik buendeln", nicht "coda muss disziplinierter sein" | kreative arbeit (handover/lessons formulieren) bleibt manuell
quelle | mw-v2a Paket 2

wall_signatur | session schliesst bei 120k trotz 300k budget frei, bootstrap-overhead pro mini-patch, auffuell-regel, mega-patch-aera 24k/patch
kategorie | workflow/token-budget
fix | primaerauftrag fertig UND <300k verbraucht → naechstes item nehmen (FR-rest > workflow-offen > backlog > test-schulden > doku-hygiene) | stopp ~350k (50k reserve) | je folge-patch eigener commit, aber EIN handover am session-ende fuer alle
kontext | nur sichere unabhaengige items | destruktive ops, chris-entscheidungs-items, grosse downloads, test-framework-umbauten NIE als auffueller
quelle | Kintsugi-Migration token-audit 2026-05-21

wall_signatur | gist-patch schritt 12 uebersprungen, gist-drift, supervisor kann raw-links nicht fetchen nur gists, mjolnir-round-trip kaputt
kategorie | workflow/gist
fix | gist-sync am session-ende ist gleichrangige pflicht (nicht optional) | ohne gist-sync ist der supervisor-round-trip kaputt sobald der gist-stand veraltet
kontext | pflicht-schritt am listen-ende = token-knapp-risiko-zone, faellt als erster | an tool/hook binden, nicht auf disziplin hoffen
quelle | Zerberus gist-drift 2026-05-21

wall_signatur | coda terminalisiert, git pytest pip robocopy npm an chris delegieren, terminal-befehl an architekt, worktree-merge an chris, "schritt 0 fuer chris"
kategorie | workflow/oberstes-gebot
fix | coda macht ALLE terminal-ops selbst (git/pytest/pip/robocopy/npm), merged+pusht worktree-branches selbst vor session-ende | supervisor gibt nie terminal-befehle, baut coda-prompts (.md)
kontext | gilt immer | einzige ausnahme: physisch unmoegliche tests (touch, echtes geraet, mikrofon) → HUMAN_TESTS.json | backstop pro projekt: regel 0 in CLAUDE_<PROJEKT>.md
quelle | Zerberus P-umzug 2026-05-16

wall_signatur | handover am session-ende vergessen, round-trip kaputt, chris erkennt auftrag-status nicht, single-slot ueberschreiben, HANDOVER.json pflicht
kategorie | workflow/handover
fix | HANDOVER.json am ende JEDER session: status-kopf KOMPLETT ueberschreiben (single-slot) + genau 1 historie-eintrag (append-only) | ausnahmslos, gleichrangig mit push
kontext | single-slot-status != _ERLEDIGT.md (audit-log, akkumuliert) | dauerhaftes (modul-status, verworfene ansaetze, brueche) → SCHALTPLAN_PROJEKT.json, NICHT in den handover
quelle | Zerberus B-072 2026-05-16 (frueher mjolnir.md)

wall_signatur | worktree-branch ungemergt, schritt 0 fuer chris, ff-merge rebase stash pop
kategorie | workflow/git
fix | coda merged+pusht worktree-branches selbst vor session-ende: git stash push → merge --ff-only → stash pop → eigenen branch per rebase main → ff-merge → push | nie als "schritt 0" an chris delegieren
kontext | terminal-arbeit, faellt unter das oberste gebot | bei nicht-moeglichem ff-merge: rebase selbst oder merge-commit
quelle | Zerberus B-061 2026-05-16

wall_signatur | supervisor gibt terminal-befehl im chat, "nur ein befehl", powershell-snippet statt coda-prompt
kategorie | workflow/supervisor
fix | supervisor schreibt .md-prompt (FEATURE_REQUEST/auftrag) statt terminal-snippet | "kann coda das selbst?" ist in 95% ja
kontext | trennung supervisor=plant/prueft/promptet vs coda=implementiert/testet gilt auch im chat | "nur ein befehl" ist einer zu viel
quelle | Zerberus 2026-05-16

wall_signatur | multi-session auftrag, STATUS-header IN_ARBEIT FERTIG BLOCKIERT, FEATURE_REQUEST _QUEUED.md _ERLEDIGT.md lifecycle, schluesselwort-whitelist
kategorie | workflow/multi-session
fix | HANDOVER.json status-kopf als erster block | conditional lifecycle: rename FEATURE_REQUEST → _ERLEDIGT.md nur bei STATUS=FERTIG | neuer FEATURE_REQUEST mit abweichendem kurznamen waehrend IN_ARBEIT → _QUEUED.md, alter bleibt
kontext | pflichtfelder status/auftrag/fortschritt/naechste-session maschinell auswertbar
quelle | Zerberus B-mjolnir-multisession 2026-05-17

wall_signatur | workflow-aenderung ohne selbsttest, hoffnung ungleich verifikation, phase A B C D, replay sub-agent, adversarial konflikt provozieren
kategorie | workflow/selbsttest
fix | workflow-aenderung braucht 3-phasen-selbsttest VOR push: A setup (zustand erzeugen der den schutz ausloest) | B replay (sub-agent/2. session als frische coda) | C adversarial (gegnerische aktion + pruefen ob schutz greift) | D cleanup (test-verzeichnis loeschen, working-tree-root sauber)
kontext | "coda hat es ja so geschrieben" ist kein selbsttest | echtes multi-session-verhalten nur ueber tage testbar → surrogat dokumentieren (sub-agent simuliert reset), kein skip
quelle | Try_Faulheits_catch 2026-05-17

wall_signatur | feature_request filename, kebab-case aus frontmatter, nie projektname als filename, lifecycle-suffix bleibt bei rename
kategorie | workflow/naming
fix | FEATURE_REQUEST_{kurzname}.md, kurzname = kebab-case aus dem frontmatter | nie projektname als filename | bei umbenennung bleibt kurzname-suffix erhalten (_ERLEDIGT.md, _QUEUED.md)
kontext | gilt alle projekte
quelle | aufraeumarbeiten-post-catch 2026-05-17

DIE-6-FAULHEITS-CATCHES-INDEX (quick-ref, details als eigene lessons oben)
1 oberstes gebot — coda terminalisiert nichts was coda kann
2 HANDOVER.json pflicht am session-ende — single-slot, ausnahmslos
3 worktree-branches selbst auf main mergen — kein schritt 0 fuer chris
4 supervisor baut coda-prompts statt terminal-befehle
5 multi-session-STATUS-header + QUEUED-pattern
6 selbsttest-pflicht fuer workflow-aenderungen (phase A-D)
