lessons workflow (claude code + chat) | maschinen-only | schema: wall_signatur | kategorie | fix | kontext | quelle
marathon-volltext (6 faulheits-catches + selbsttest-pattern) liegt in GLOBAL_LESSONS.md — hier nur cli-workflow + kurzform

wall_signatur | vor claude-code-session git commit checkpoint, yolo-modus ohne backup
kategorie | workflow/git
fix | vor jeder claude-code-session git commit als checkpoint
kontext | yolo-modus ohne backup = russisch roulette
quelle |

wall_signatur | max 2-3 patches pro code-session, ab patch 4 kontextqualitaet leidet
kategorie | workflow/session
fix | max 2-3 patches pro code-session
kontext | ab patch 4+ leidet kontextqualitaet spuerbar (ausnahmen siehe auffuell-regel in GLOBAL_LESSONS)
quelle |

wall_signatur | CLAUDE.md SUPERVISOR.md heilig, claude code ergaenzt nie ueberschreibt, bei unerwartetem verhalten erst SUPERVISOR lesen
kategorie | workflow/files
fix | CLAUDE/SUPERVISOR-dateien nur ergaenzen nie ueberschreiben | bei unerwartetem verhalten erst SUPERVISOR lesen dann debuggen
kontext |
quelle |

wall_signatur | patch-prompts in chat planen, code nur ausfuehren, supervisor plant prueft promptet, coda implementiert testet
kategorie | workflow/rollen
fix | chat=supervisor (plant/prueft/promptet, erstellt nur prompts) | code=executor (implementiert/testet, folgt prompt, fragt bei unklarheit)
kontext | nicht mischen
quelle |

wall_signatur | mehrere code-pfade legacy.py vs orchestrator.py, welcher router fuehrt aktiven traffic, pipeline-fix alle pfade
kategorie | workflow/diagnose
fix | bei mehreren pfaden IMMER pruefen welcher router den aktiven traffic fuehrt bevor ein fix nur in einem landet | bei pipeline-fix alle betroffenen pfade pruefen
kontext |
quelle | Zerberus P80b,P82

wall_signatur | CLAUDE_[PROJEKTNAME].md konvention suffix, globale CLAUDE.md verwechslung, vollen dateinamen im prompt
kategorie | workflow/naming
fix | projektspezifische dateien tragen projektnamen als suffix | in prompts immer vollen dateinamen verwenden
kontext | claude code liest beim start automatisch eine globale CLAUDE.md
quelle | Zerberus P100

wall_signatur | prompts und ausgaben als .md-datei, kein inline-text, mobilfreundlich kopierbar
kategorie | workflow/output
fix | alle prompts/strukturierten ausgaben als .md-datei, kein inline-text
kontext | architekt kopiert vom handy
quelle |

wall_signatur | konzept vor implementierung kreative projekte, lebende konzept-dokumente getrennt vom status
kategorie | workflow/konzept
fix | bei kreativen projekten erst konzept als .md, dann umsetzung | ideen/audits/design-regeln in separater .md getrennt vom projektstatus
kontext |
quelle |

wall_signatur | kein opportunistisches refactoring, nur was patch braucht, scope-unsicherheit fragen nicht selbst entscheiden
kategorie | workflow/scope
fix | nur aendern was der aktuelle patch erfordert | bei scope-unsicherheit fragen, keine kreativen erweiterungen ueber den prompt hinaus
kontext |
quelle |

wall_signatur | entscheidungsboxen user-input server-restart destruktive ops, klar formatiert "Soll ich das uebernehmen?"
kategorie | workflow/interaktion
fix | bei aktionen die user-input erfordern: klar formatierte box mit konkreten optionen + "Soll ich das uebernehmen?"
kontext | server-restart, destruktive ops
quelle |

wall_signatur | verbosity coding-instanz still kurz praezise, chat-instanz ausfuehrlich assoziativ, nicht mischen
kategorie | workflow/verbosity
fix | coding=stiller handwerker (kurz/praezise) | chat=ausfuehrlich/assoziativ
kontext | nicht mischen
quelle |

wall_signatur | diagnose vor fix, grep/Select-String betroffenen pfad identifizieren bevor patch landet
kategorie | workflow/diagnose
fix | erst grep/Select-String, betroffenen code-pfad identifizieren, dann reparieren
kontext |
quelle |

wall_signatur | git-push-verifikation $LASTEXITCODE, credential.helper vor erstem push, powershell kein &&, onedrive lockt sqlite logs python
kategorie | workflow/environment
fix | nach git push $LASTEXITCODE pruefen (fehler → user auf deutsch) | vor erstem push credential.helper checken | powershell befehle mit ; | onedrive NIE als arbeitsverzeichnis fuer aktive projekte (lockt sqlite/logs/python)
kontext | windows
quelle |

wall_signatur | marathon-workflow oberstes gebot coda terminalisiert nichts, HANDOVER.json pflicht single-slot, worktree selbst mergen, supervisor baut coda-prompts
kategorie | workflow/marathon
fix | kurzform der 6 faulheits-catches: coda terminalisiert nichts was coda kann | HANDOVER.json am session-ende pflicht (single-slot ueberschreiben) | worktree-branches selbst mergen+pushen | supervisor baut .md-prompts statt terminal-befehle
kontext | volltext + selbsttest-pattern A-D + repair-protokoll in GLOBAL_LESSONS.md
quelle | GLOBAL_LESSONS.md (Zerberus P-umzug/B-072/B-061 2026-05-16)
