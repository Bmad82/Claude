# Testing (Playwright / pytest)

- Self-signed HTTPS-Certs: Playwright braucht `ignore_https_errors: True` im Browser-Context (Zerberus P93)
- Locator-Strategie: echte IDs der App verwenden, nicht generische Selektoren erfinden. Vor Test-Schreiben einmal in die Zieldatei grepen (Zerberus P93)
- Test-Accounts statisch in Config anlegen — NICHT zur Laufzeit per Fixture, die überleben keinen Server-Restart (Zerberus P93)
- Chaos-Tests: `@pytest.mark.parametrize` für Payload-Listen, `force=True` bei `.click()`, Exceptions in Schleifen stumm schlucken (Zerberus P93)
- `playwright install chromium` = einmaliger ~250 MB Download, dann offline nutzbar (Zerberus P93)
- `page.on("pageerror", ...)` MUSS VOR `page.goto()` registriert werden — initiale Script-Parse-Errors werden sonst verschluckt. DOM-/API-Level-Tests ohne `pageerror`-Listener fangen JS-Syntax-Fehler NICHT (Zerberus P100)
