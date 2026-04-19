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
