lessons mobile-touch | maschinen-only | schema: wall_signatur | kategorie | fix | kontext | quelle

wall_signatur | :hover funktioniert nicht auf touch-geraeten, :active zusaetzlich setzen
kategorie | mobile/css
fix | :active zusaetzlich zu :hover setzen | bei jedem ui-patch generellen sweep machen
kontext | touch-geraete
quelle | Zerberus P85

wall_signatur | mindest-touch-target 44px, kleinere buttons mobil verfehlt
kategorie | mobile/touch
fix | touch-target >=44px (>=48 bevorzugt)
kontext |
quelle |

wall_signatur | backdrop-filter ohne fallback bricht aeltere mobile-browser
kategorie | mobile/css
fix | backdrop-filter mit fallback bereitstellen
kontext | aeltere mobile-browser
quelle |

wall_signatur | landscape @media orientation landscape max-height 500px, 100dvh keyboard-overlap header modals fressen hoehe
kategorie | mobile/css
fix | @media (orientation:landscape) and (max-height:500px) fuer header-/padding-reduktion | 100dvh gegen keyboard-overlap
kontext | landscape-modus auf mobile
quelle | Zerberus P90

wall_signatur | tailscale https pflicht mobile lan, crypto.randomUUID und web-apis versagen auf http
kategorie | mobile/network
fix | tailscale + https fuer mobile lan-nutzung
kontext | crypto.randomUUID und andere web-apis versagen auf http
quelle | Zerberus P68

wall_signatur | mime-type-check schlaegt mobil fehl bei datei-upload, nur dateiendung pruefen
kategorie | mobile/upload
fix | bei datei-uploads nur dateiendung pruefen
kontext | mobile datei-uploads
quelle | Zerberus P61
