lessons frontend-js | maschinen-only | schema: wall_signatur | kategorie | fix | kontext | quelle

wall_signatur | '\n' in python-html-string wird echtes newline, bricht js-string-literal, '\\n'
kategorie | frontend/python-html
fix | in python-html-strings immer '\\n' statt '\n'
kontext | js-string-literale in python-generiertem html
quelle | Zerberus P69c

wall_signatur | crypto.randomUUID versagt http non-secure, lan ohne https, fallback-uuid
kategorie | frontend/web-api
fix | fallback-uuid-generator bereitstellen, crypto.randomUUID nur im secure-context
kontext | lan ohne https
quelle | Zerberus P68

wall_signatur | $1 js-regex-backreference vs \1 python re.sub-backreference verwechselt
kategorie | frontend/regex
fix | js-regex: $1 | python re.sub: \1 — nicht verwechseln
kontext | regex zwischen js und python portieren
quelle | Zerberus P69a

wall_signatur | python inline-flags (?i)(?m)(?s) von js RegExp abgelehnt
kategorie | frontend/regex
fix | python inline-flags vor js-validierung rausstrippen, in flags-string uebernehmen
kontext | python-regex nach js RegExp portieren
quelle | Zerberus P90

wall_signatur | keypress deprecated, keydown
kategorie | frontend/events
fix | keydown statt keypress
kontext |
quelle |

wall_signatur | button in formular ohne type="button", ungewollter form-submit
kategorie | frontend/forms
fix | buttons in formularen brauchen type="button"
kontext |
quelle |

wall_signatur | llm ohne persona generisch "ich bin ein computerprogramm", persona-prompt
kategorie | frontend/llm
fix | expliziten persona-prompt setzen
kontext | ohne klare persona faellt llm in generisches verhalten zurueck
quelle | Zerberus P81

wall_signatur | chart.js pinch-zoom, chart.umd hammer.js chartjs-plugin-zoom lade-reihenfolge, zoom scheitert silent
kategorie | frontend/chartjs
fix | lade-reihenfolge chart.umd → hammer.js → chartjs-plugin-zoom | ohne hammer.js scheitert touch-zoom silent
kontext | chart.js touch-pinch-zoom
quelle | Zerberus P91

wall_signatur | new Chart() auf dasselbe canvas memory-leak, .destroy() referenz null
kategorie | frontend/chartjs
fix | vor neu-render .destroy() + referenz null setzen
kontext | chart auf dasselbe canvas neu rendern
quelle | Zerberus P91

wall_signatur | chart.js responsive container ohne feste hoehe rendert 0px oder blaeht auf
kategorie | frontend/chartjs
fix | container position:relative + feste height:Xpx
kontext | responsive chart
quelle | Zerberus P91

wall_signatur | emoji surrogate-pair 📄 windows-encoding-fehler python-string
kategorie | frontend/encoding
fix | ascii-alternativen statt emoji in python-strings
kontext | windows-encoding
quelle | Zerberus P68

wall_signatur | js-syntax in python-html-string, node --check, <script>-block extrahieren, pageerror-listener
kategorie | frontend/verify
fix | html aus router rendern, <script>-bloecke extrahieren, einzeln durch node --check (schneller als playwright pageerror)
kontext | js eingebettet in python-generiertem html, pre-commit
quelle | Zerberus P100

wall_signatur | retry-button nach frontend-timeout doppelter llm-call doppelte kosten, fetch abgebrochen backend arbeitet weiter
kategorie | frontend/retry
fix | retry erst per rest-endpoint pruefen ob antwort schon in db, nur bei echtem fehlen nochmal senden
kontext | frontend-timeout bricht nur fetch, backend committet trotzdem
quelle | Zerberus P109

wall_signatur | sse-heartbeat statt statischem timeout, "event: heartbeat", watchdog 15s, hard-stop 120s
kategorie | frontend/sse
fix | backend sendet "event: heartbeat\ndata: ok" alle 5s, frontend addEventListener('heartbeat') setzt watchdog (15s) zurueck, hard-stop 120s gegen leaks
kontext | langlauf-jobs: gpu-pfad straff, cpu-fallback bis max
quelle | Zerberus P114a

wall_signatur | "retry: 5000" als erste sse-nachricht, eventsource reconnect-interval
kategorie | frontend/sse
fix | yield "retry: 5000\n\n" als erste sse-nachricht setzt reconnect-interval dauerhaft fuer die verbindung
kontext | sse-spec, 5s zahm fuer mobile ohne reconnect-storm
quelle | Zerberus P114a

wall_signatur | sse-listener lebt laenger als fetch, window.__appSseWatchdogReset finally null
kategorie | frontend/sse
fix | window.__appSseWatchdogReset waehrend request gesetzt, im finally null | heartbeat-listener ruft ?.() (no-op wenn kein request)
kontext | sse-listener ueberlebt einzelne fetch-transaktion
quelle | Zerberus P114a

wall_signatur | dark theme produktionsumgebung wechselnde lichtverhaeltnisse
kategorie | frontend/ux
fix | dark theme bei wechselnden lichtverhaeltnissen (nicht nur aesthetik, besser lesbar)
kontext | shop-floor/produktion
quelle |

wall_signatur | single-file html offline shop-floor, alles inline keine externen deps, usb-verteilung
kategorie | frontend/deployment
fix | single-file html: css/js inline, keine externen abhaengigkeiten, verteilung per usb/netzlaufwerk
kontext | offline-/shop-floor-nutzung
quelle |

wall_signatur | autocomplete off / new-password gegen browser-autofill-leiste
kategorie | frontend/forms
fix | autocomplete="off" bzw "new-password" auf inputs gegen autofill
kontext |
quelle |

wall_signatur | python (?P<name>) named groups von js RegExp nicht verstanden
kategorie | frontend/regex
fix | python named groups vor new RegExp in standard-groups konvertieren
kontext | python-regex nach js
quelle |

wall_signatur | js-regex [^\n\r\[]+ in python triple-quote, "Invalid regular expression missing /", \\n\\r doppel-escape
kategorie | frontend/regex
fix | in """...""" entweder \\n\\r (python-doppel-escape) oder simpler (.+) (matcht ohne s-flag kein newline)
kontext | js-regex-charklassen mit newline-escapes in python-triple-quotes
quelle | Zerberus P118a

wall_signatur | klickbare entscheidungsbox [DECISION][OPTION:wert], createTextNode createElement, nie innerHTML mit llm-content
kategorie | frontend/xss
fix | llm gibt marker [DECISION][OPTION:wert] Label[/DECISION], frontend parst per regex baut <button> via dom | xss-safe: text via createTextNode, buttons via createElement, NIE innerHTML mit llm-content
kontext | llm-gestellte entscheidungen als buttons (feature-flag in settings)
quelle | Zerberus P118a
