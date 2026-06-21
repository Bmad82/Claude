lessons documentation | maschinen-only | schema: wall_signatur | kategorie | fix | kontext | quelle

wall_signatur | praxiswissen maschinenbediener > herstellerdoku, implizites wissen abfragen, video-transkript fallback
kategorie | doku/shop-floor
fix | erst implizites wissen der bediener abfragen, dann gegen herstellerdoku checken
kontext | video-transkripte sind fallback, nicht primaerquelle
quelle |

wall_signatur | single-file html produktion, keine externen css/js, kein build-tool, alles inline
kategorie | doku/shop-floor
fix | single-file html: alles inline, kein build-tool
kontext | produktionsumgebung
quelle |

wall_signatur | dark theme wechselnde lichtverhaeltnisse, farbkodierung rot gefahr gruen tipp teal hintergrund
kategorie | doku/shop-floor
fix | dark theme | farbkodierung rot=gefahr gruen=tipp teal=hintergrund (intuitiv verstanden)
kontext | produktion
quelle |

wall_signatur | profi/rookie-modus css-klasse, body.expert-mode .step-detail display none
kategorie | doku/shop-floor
fix | profi/rookie-modus als css-klasse: body.expert-mode .step-detail{display:none!important}
kontext |
quelle |

wall_signatur | click-path monospace-kette pfeile, reset-button ans ende, sicherheitskritisch eigener warnblock
kategorie | doku/shop-floor
fix | klickpfade als monospace-kette mit pfeilen | reset-button ans ende | sicherheitskritisches in eigenen farblichen warnblock, nicht im fliesstext
kontext | anleitungen
quelle |

wall_signatur | localStorage fortschrittspersistenz html-anleitung key pro dokument eindeutig, koordinatensystem panel tcp workcontainer
kategorie | doku/persistenz
fix | localStorage fuer fortschritt, key pro dokument eindeutig | koordinatensystem-fallen explizit dokumentieren (panel vs tcp vs workcontainer)
kontext | html-anleitungen
quelle |

wall_signatur | drei doku-ebenen README technisch, CLAUDE_PROJEKT steuerdatei, MANUAL/schulungsdoku endnutzer
kategorie | doku/ebenen
fix | README.md=technisch fuer entwickler | CLAUDE_{PROJEKT}.md=steuerdatei fuer coda | MANUAL/schulungsdoku=endnutzer ohne tech-sprech
kontext |
quelle |

wall_signatur | projekt-doku-suffix _{PROJEKT} HINTEN, CLAUDE SUPERVISOR MARATHON_WORKFLOW lessons DECISIONS DESIGN ROADMAP
kategorie | doku/naming
fix | alle projektspezifischen doku-dateien tragen suffix _<PROJEKTNAME> HINTEN (MARATHON_WORKFLOW_ZERBERUS.md, nicht ZERBERUS_MARATHON_WORKFLOW.md)
kontext | coda liest beim start oft eine globale CLAUDE.md, verwechselt sie sonst mit der projektspezifischen
quelle | Zerberus P100

wall_signatur | steuer-files feste namen ohne projekt-suffix, HANDOVER.json SCHALTPLAN_PROJEKT.json HUMAN_TESTS.json + renderer .html
kategorie | doku/naming
fix | suffix-ausnahme: die steuer-files heissen IMMER so (pro projekt eine datei, verzeichnis=kontext) | README/CHANGELOG/PROJEKTDOKUMENTATION ebenfalls suffix-frei
kontext | SCHALTPLAN_PROJEKT traegt "PROJEKT" fest im namen (abgrenzung zum meta-workflow-schaltplan), kein {PROJEKT}-platzhalter
quelle |

wall_signatur | format nach leser, maschinen-files artikelfrei pipe kein prosa-padding keine ## fett, mensch-files prosa erlaubt, nie mischen
kategorie | doku/format
fix | maschinen-files (CLAUDE/SUPERVISOR/MARATHON_WORKFLOW/lessons): artikelfrei, pipe-separiert, kein prosa-padding, keine ##/fett | mensch-files (README/PROJEKTDOKUMENTATION/DESIGN/ROADMAP): prosa erlaubt | nie mischen innerhalb einer datei
kontext | format nach leser
quelle |

wall_signatur | session-start-pflicht CLAUDE_PROJEKT, lessons_lookup tf-idf top-3 statt komplett-load
kategorie | doku/session-start
fix | session-start in jeder CLAUDE_<PROJEKT>.md: FEATURE_REQUEST → HANDOVER.json → SCHALTPLAN_PROJEKT.json → MARATHON_WORKFLOW → lessons_lookup.py (tf-idf top-3)
kontext | kein komplett-load der lessons
quelle | mw-v2a

wall_signatur | mjolnir orchestrator session_manager DEFAULT_PROMPT_TEMPLATE rendert {PROJEKTNAME} allowlist suffixierte dateinamen
kategorie | doku/mjolnir
fix | der orchestrator mjolnir rendert {PROJEKTNAME} aus allowlist und referenziert die suffixierten dateinamen, damit jedes projekt mit derselben konvention laeuft
kontext | mjolnir = orchestrator-software (behaelt den namen); das uebergabe-dokument heisst HANDOVER.json
quelle |
