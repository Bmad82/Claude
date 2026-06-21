lessons json-data | maschinen-only | schema: wall_signatur | kategorie | fix | kontext | quelle

wall_signatur | typographische anfuehrungszeichen „" ‚' brechen json-import, gerade ascii "..."
kategorie | json/encoding
fix | in dialogfeldern immer gerade ascii "..." | json-hygiene vor import: json.loads() als validierung, alle sonderzeichen pruefen
kontext | json-import aus user-/dialog-text
quelle |

wall_signatur | csv maschinen-import format exakt, ein falsches komma = import-fehler
kategorie | json/csv
fix | csv-format bei maschinen-import exakt beibehalten
kontext |
quelle |

wall_signatur | proprietaeres binaerformat, hexdump encoding raten textmarker
kategorie | json/binary
fix | erst hexdump, dann encoding raten, dann textmarker suchen
kontext | proprietaere binaerformate
quelle |
