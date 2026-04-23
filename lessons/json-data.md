# JSON & Datenformate

- Geschwungene/typographische Anführungszeichen (`„"`, `‚'`) brechen JSON-Imports → in Dialogfeldern IMMER gerade ASCII `"..."` verwenden
- JSON-Hygiene vor Import: alle Sonderzeichen prüfen, `json.loads()` als Validierung
- CSV-Formate bei Maschinen-Import exakt beibehalten — ein falsches Komma = Import-Fehler
- Proprietäre Binärformate: erst Hexdump, dann Encoding raten, dann Textmarker suchen
