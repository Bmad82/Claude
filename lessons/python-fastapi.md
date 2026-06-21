lessons python-fastapi | maschinen-only | schema: wall_signatur | kategorie | fix | kontext | quelle

wall_signatur | uvicorn --reload windows neue module/imports nicht erkannt, nur geladene dateien, reload zombie-worker parallele master-trees, start.bat ohne --reload ignoriert code lautlos
kategorie | python-fastapi/reload
fix | bei neuen imports manueller kill+restart | vor jedem restart ALLE python-pids killen dann neu starten | nach code-aenderung verifizieren dass neue logs/felder/marker erscheinen
kontext | gilt windows-uvicorn
quelle | Zerberus P88,P89,P99

wall_signatur | async update_interaction fehlendes await, double-start, race condition, background-task lock-guard
kategorie | python-fastapi/async
fix | i/o-funktionen async, alle call-sites await | lock-guard: pruefen ob task laeuft bevor neuer startet
kontext | kein blocking call im asyncio-loop (aiohttp statt requests)
quelle | Zerberus P59

wall_signatur | pacemaker/config yaml wirkt erst nach neustart, kein live-reload
kategorie | python-fastapi/config
fix | nach yaml/config-aenderung server neu starten
kontext | die meisten fastapi-setups haben keinen config-watcher
quelle |

wall_signatur | config split-brain, ui schreibt json backend liest yaml, ui-aenderung wirkt nie
kategorie | python-fastapi/config
fix | EINE config-datei als single source of truth, ui+backend lesen/schreiben dieselbe
kontext | getrennte ui-/backend-config-dateien
quelle |

wall_signatur | gps-ping 10hz sqlite-trommelfeuer absturz, in-memory-cache hot-path
kategorie | python-fastapi/performance
fix | hot-path-daten in-memory cachen statt db-hit pro request
kontext | hochfrequente schreib-pings
quelle |

wall_signatur | globaler singleton state-mixing mehrere clients, pro-verbindung session-instanz
kategorie | python-fastapi/state
fix | pro verbindung eigene session-instanz, kein globaler singleton
kontext | mehrere parallele clients
quelle |

wall_signatur | deterministisches caching dateiname=hash des inhalts, doppelt-generieren
kategorie | python-fastapi/caching
fix | dateiname = hash(inhalt) → gleicher input gleiche datei, kein doppelt-generieren
kontext | teure deterministische generierung (tts/render)
quelle |

wall_signatur | path-traversal, os.path.basename user-input, download-route .. sentinel
kategorie | python-fastapi/security
fix | os.path.basename auf alles vom user, auch bei "internen" download-routes
kontext | jede route die pfad/dateiname aus user-input baut
quelle |

wall_signatur | isoformat T-separator, sqlite speichert space, datetime-vergleich bricht lautlos
kategorie | python-fastapi/datetime
fix | datetime-format zwischen isoformat (T) und sqlite (space) angleichen
kontext | sqlite-zeitstempel-vergleiche
quelle |

wall_signatur | neuer scheduler duplikation, apscheduler bestehenden job erweitern, overnight 04:30, try/except um neuen teil
kategorie | python-fastapi/scheduler
fix | bestehenden apscheduler-job erweitern statt neuen scheduler | try/except um den neuen teil, damit dessen exception den job nicht abbricht
kontext | jobs die dieselben daten lesen, reihenfolge egal
quelle | Zerberus P115

wall_signatur | IndexFlatL2 kein remove(), faiss soft-delete deleted-flag, drei filterstellen retrieval status reindex
kategorie | python-fastapi/faiss
fix | metadata-flag deleted:true statt rebuild | in ALLEN drei stellen filtern (retrieval-search, status-listing, reindex-quelle) + per grep-checkpoint testen
kontext | IndexFlatL2 hat kein remove(); index waechst bis naechstem expliziten reindex (loeschen O(1))
quelle | Zerberus P116

wall_signatur | l2-cosine umrechnung normalize_embeddings, cos_sim = 1 - L2²/2, threshold 0.9 cos L2 0.447
kategorie | python-fastapi/embeddings
fix | bei normalize_embeddings=True gilt cos_sim = 1 - L2²/2 (0.9 cos ≈ L2 0.447)
kontext | nur normalisierte embeddings (minilm, bge)
quelle | Zerberus P115
