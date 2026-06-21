TEMPLATE | kopie als lessons_{PROJEKT}.md ins projekt-repo | maschinen-only | read-only fuer worker, geschrieben vom cron

zweck | projektspezifische, projekt-lokale lessons | wird NICHT vom worker direkt befuellt | der worker legt erkenntnisse als finding ins project-root (templates/FINDING_TEMPLATE.md), der cron promoviert project-quirks hierher (lokal) bzw. zur globalen schicht (>=2 projekte/uebertragbar, siehe CRON_PROMOTION_SPEC.md)
lookup | worker matcht per lessons_lookup.py (tf-idf top-3) gegen wall_signatur, laedt nie komplett
schema je eintrag: wall_signatur | kategorie | fix | kontext | quelle
wall_signatur = literale symptom-/wand-vokabeln (error-klasse, traceback-phrase, lib-name, literal-strings) — was der lookup matcht, nicht die loesung umschreiben
kontext = eine zeile anwendungsgrenze (wann gilt, wann nicht)

lese-reihenfolge (worker, vor aufgabe)
1 lessons_lookup.py --task '<aufgabe>' (tf-idf top-3 ueber lessons_{PROJEKT}.md, ~500 token)
2 GLOBAL_LESSONS.md (workflow-catches + repair-eskalations-protokoll, universell)
3 bei tech-themen: passende lessons/{technologie}.md aus dem Claude-repo

---

wall_signatur | {literale wand-vokabeln}
kategorie | {z.b. backend/state, frontend/ui, cli/tool-drift, test/methodik}
fix | {knapp, was tun}
kontext | {anwendungsgrenze}
quelle | {patch-/finding-/commit-ref, sonst leer}

pflege | NUR der cron schreibt hier | promoviert ein finding global, bleibt der project-quirk lokal hier | dubletten vermeiden: bestehende wall_signatur um symptom-variante ergaenzen statt neuen block
