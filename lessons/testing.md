lessons testing | maschinen-only | schema: wall_signatur | kategorie | fix | kontext | quelle

wall_signatur | self-signed https-cert playwright ignore_https_errors browser-context
kategorie | testing/playwright
fix | playwright browser-context ignore_https_errors: True
kontext | self-signed certs
quelle | Zerberus P93

wall_signatur | locator echte app-ids nicht generische selektoren erfinden, vor test grep zieldatei
kategorie | testing/playwright
fix | echte app-ids verwenden, vor test-schreiben einmal in die zieldatei grepen
kontext |
quelle | Zerberus P93

wall_signatur | test-accounts statisch in config nicht laufzeit-fixture, ueberleben keinen server-restart
kategorie | testing/fixtures
fix | test-accounts statisch in config anlegen, nicht zur laufzeit per fixture
kontext | fixtures ueberleben server-restart nicht
quelle | Zerberus P93

wall_signatur | chaos-test parametrize payload-listen, force=True click, exceptions in schleifen schlucken
kategorie | testing/chaos
fix | @pytest.mark.parametrize fuer payloads, force=True bei .click(), exceptions in schleifen stumm schlucken
kontext | chaos-/fuzz-tests
quelle | Zerberus P93

wall_signatur | playwright install chromium 250mb einmalig dann offline
kategorie | testing/playwright
fix | playwright install chromium = einmaliger ~250mb download, danach offline nutzbar
kontext |
quelle | Zerberus P93

wall_signatur | page.on("pageerror") MUSS vor page.goto, initiale script-parse-errors verschluckt, dom-/api-test faengt js-syntax nicht
kategorie | testing/playwright
fix | page.on("pageerror",...) VOR page.goto() registrieren
kontext | dom-/api-level-tests ohne pageerror-listener fangen js-syntax-fehler nicht
quelle | Zerberus P100

wall_signatur | tests schreiben UND ausfuehren, nicht annehmen sie laufen
kategorie | testing/disziplin
fix | tests schreiben UND ausfuehren
kontext | hoffnung != verifikation
quelle |
