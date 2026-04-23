# Frontend & JavaScript

- `'\n'` in Python-HTML-Strings wird als echtes Newline gerendert → bricht JS-String-Literale. Immer `'\\n'` verwenden (Zerberus P69c)
- `crypto.randomUUID()` versagt in HTTP-Non-Secure-Kontexten (LAN ohne HTTPS) → Fallback-UUID-Generator bereitstellen (Zerberus P68)
- `$1` = JS-Regex-Backreference, `\1` = Python `re.sub`-Backreference — nicht verwechseln (Zerberus P69a)
- Python-Inline-Flags `(?i)` / `(?m)` / `(?s)` werden von JS `RegExp` abgelehnt — vor Validierung rausstrippen und in flags-String übernehmen (Zerberus P90)
- `keypress` ist deprecated → `keydown` verwenden
- Buttons in Formularen brauchen `type="button"` — sonst ungewollter form-submit
- LLM ohne klare Persona fällt in generisches Verhalten zurück ("Ich bin ein Computerprogramm") — immer expliziten Persona-Prompt setzen (Zerberus P81)
- Chart.js: `chart.umd.min.js` allein reicht NICHT für Touch-Pinch-Zoom. Lade-Reihenfolge: chart.umd → hammer.js → chartjs-plugin-zoom. Ohne hammer.js scheitert Zoom silent (Zerberus P91)
- Chart.js `new Chart()` auf dasselbe Canvas = Memory-Leak → immer `.destroy()` + Referenz null setzen vor Neu-Render (Zerberus P91)
- Chart.js responsive: Container braucht feste Höhe (`position: relative; height: Xpx`) — ohne rendert es 0px oder bläht sich auf (Zerberus P91)
- Emoji-Surrogate-Pairs (`📄` = `\uD83D\uDCC4`) können Windows-Encoding-Fehler in Python-Strings erzeugen → ASCII-Alternativen verwenden (Zerberus P68)
- JS-Syntax in Python-HTML-Strings immer mit `node --check` als Pre-Commit-Verifizierung: HTML aus dem Router rendern, `<script>`-Blöcke extrahieren, einzeln durch `node --check` jagen. Schnellere Variante als Playwright mit `pageerror`-Listener (Zerberus P100)
- Retry-Button nach Frontend-Timeout darf NICHT blind den Request wiederholen. Der Frontend-Timeout bricht nur `fetch()` ab — das Backend arbeitet weiter und speichert die Antwort. Naiver Retry = doppelter LLM-Call + doppelte Kosten. Pattern: Erst per REST-Endpoint prüfen ob die Antwort inzwischen in der DB ist, nur bei echtem Fehlen nochmal senden (Zerberus P109)
- Dark Theme in Produktionsumgebungen: nicht nur Ästhetik — bei wechselnden Lichtverhältnissen besser lesbar
- Single-File HTML für Offline-/Shop-Floor-Nutzung: alles inline, keine externen Abhängigkeiten, Verteilung per USB/Netzlaufwerk
- `autocomplete="off"` bzw. `autocomplete="new-password"` auf Inputs gegen Browser-Autofill-Leisten
- Python-Regex `(?P<name>...)` Named Groups werden von JS `RegExp` nicht verstanden → vor `new RegExp()` in Standard-Groups konvertieren
