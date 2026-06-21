<!-- TEMPLATE | kopie als MARATHON_WORKFLOW_{PROJEKT}.md ins projekt-root | aufgabenliste mit status nach jedem patch updaten -->

MARATHON_WORKFLOW_{PROJEKT}.md | maschinen-only | token-opt
aufgabenliste {PROJEKT} | status nach jedem patch updaten
status-symbole: ⬜ offen · 🔄 in arbeit · ✅ fertig · ⏸ blockiert · ⚠ teilweise

REGEL-0 — faulheits-catches gelten VOR jeder patch-logik
siehe GLOBAL_LESSONS.md sektion DIE-6-FAULHEITS-CATCHES-INDEX

SESSION-ZYKLUS (pflicht)
1 konflikt-check | HANDOVER.json mit STATUS:IN_ARBEIT + abweichender FR-kurzname → QUEUED-pattern (siehe CLAUDE_{PROJEKT}.md session-start-pflicht)
2 FEATURE_REQUEST_{kurzname}.md pruefen | existiert? → abarbeiten | bei STATUS=FERTIG → rename _ERLEDIGT.md
3 HANDOVER.json einlesen (status-header zuerst), NICHT loeschen (status ueberschrieben, historie append-only)
4 SCHALTPLAN_PROJEKT.json lesen (projekt-gedaechtnis: module, status, brueche)
5 python scripts/lessons_lookup.py --task '<aufgabe>' (tf-idf top-3, mw-v2a paket 1) | globale quellen GLOBAL_LESSONS.md, SUPERVISOR_KODEX.md | task-regeln aus playbooks/, pfad-regeln aus .claude/rules/ (mw-v2b paket 2)
6 naechsten ⬜-eintrag aus workflow ziehen
7 patch durchfuehren | status updaten
8 doku-pflicht (CLAUDE/SUPERVISOR/CHANGELOG) | erkenntnis → finding in FINDINGS_{PROJEKT}.md (read-only-modell, KEINE lesson direkt) | git commit+push (coda macht SELBST, kein auftrag an chris)
9 auffuell-check (siehe auffuell-regel) | auftrag erledigt UND <300k → naechstes item aus FR/workflow/backlog statt abschliessen
10 HANDOVER.json mit status-header schreiben (session-ende, ausnahmslos)

SESSION-AUFFUELL-REGEL (2026-05-21)
primaerauftrag fertig UND token <300k → NICHT abschliessen, weiterarbeiten
reihenfolge: 1 weitere punkte im selben FEATURE_REQUEST (N+3, N+4...) | 2 offene MARATHON_WORKFLOW-items ohne abhaengigkeiten | 3 backlog nach prioritaet (sofort > mittelfristig > nice-to-have) | 4 test-schulden (pre-existing failures) | 5 doku-hygiene
stopp-schwelle ~350k (50k reserve)
AUSNAHMEN, nie als auffueller: destruktive ops (db-migration, auth-refactor, faiss-switch) | chris-entscheidungs-items (DECISIONS_PENDING) | externe ressourcen (docker-pull, modell-download >1gb) | test-suite-fundamentalumbau
doku bei auffuell-patches: eigener commit pro folge-patch | finding falls noetig | KEIN separater HANDOVER/SUPERVISOR/gist pro zwischen-patch | am session-ende EIN HANDOVER der alle patches zusammenfasst
anti-pattern: "patch fertig bei 120k → doku → handover → stopp" verbrennt 80% des budgets

PHASE-1 — {PHASENNAME} (# | ziel | braucht | status | notizen)
1 | {aufgabe} | — | ⬜ | {hinweis/patch-nr}

PHASE-2 — {PHASENNAME} (# | ziel | braucht | status | notizen)
n | {aufgabe} | #{vorher} | ⬜ | {hinweis}

BACKLOG (ohne phase) | {idee/wunsch ohne termin}

DECISIONS-PENDING | verweis auf DECISIONS_{PROJEKT}.md oder projekt-root DECISIONS_PENDING.md | nicht inline doppeln
