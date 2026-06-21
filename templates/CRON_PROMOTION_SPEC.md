TEMPLATE/SPEC | cron-promotion (lessons + rules) | maschinen-only | dockt an schaltplan/fabrik_meta_workflow.json: be.cron.lessons (IST) + be.cron.rules (PLAN)

rolle | ein high-reasoning-frontier-cron-job, pro projekt, separat von der pipeline (layer "betrieb") | der EINZIGE schreiber der globalen schicht (lessons/, templates/, GLOBAL_LESSONS.md, gists) | supervisor/worker/solver schreiben NIE global, nur findings ins project-root
docking | be.cron.lessons (lessons_cron 04:30): findings + tages-logs → globale @L, eliminiert rag-muell | be.cron.rules (PLAN): nachgeschaerfte regeln → HITL-gate vor permanentem core-template-merge | be.cron.drift (—, bewusst gestrichen, bleibt sichtbar)

input | FINDINGS_{PROJEKT}.md im project-root (templates/FINDING_TEMPLATE.md) + tages-logs des laufs | je finding bereits im lesson-schema (wall_signatur|kategorie|fix|kontext|quelle)

promotion-kriterium
- global | finding wird global wenn in >=2 projekten gesehen (mehrere gesehen-zeilen) ODER vom cron als uebertragbar beurteilt
- lokal | project-quirks bleiben lokal → in lessons_{PROJEKT}.md (im projekt-repo) schreiben, nicht global
- ziel-datei global je kategorie: workflow/* → GLOBAL_LESSONS.md | technologie (python-fastapi, gpu-ml, ...) → lessons/{tech}.md | im 5-feld-schema

dedup vor dem schreiben (pflicht)
- finding gegen bestehende globale lessons matchen — mit DEMSELBEN tf-idf wie der worker-lookup (lessons_lookup.py)
- treffer → bestehende lesson STAERKEN: symptom-variante in wall_signatur ergaenzen (mehr literale vokabeln = besser auffindbar), fix/kontext nur schaerfen | KEINE dublette anlegen
- kein treffer → neue lesson im schema anlegen, quelle = finding-ref

ablauf je lauf
1 findings + tages-logs fetchen (project-root)
2 je finding: scope pruefen (>=2 projekte? uebertragbar?) → global-kandidat | lokal
3 dedup-tf-idf gegen globale lessons → treffer staerken ODER neu anlegen
4 rules (be.cron.rules): nachgeschaerfte regeln NICHT direkt mergen → HITL-gate (telegram) vor core-template-merge
5 status der findings setzen (vom-cron-gesichtet → promoviert | lokal-behalten), findings nie loeschen (audit-spur)
6 gist-sync der geaenderten globalen schicht (lessons-/templates-/wegweiser-gist)

reifegrad
- erster durchlauf | cron schlaegt nur vor, chris befoerdert manuell | autonomer gist-write spaeter
- invariante | cron = einziger globaler schreiber, sonst bricht das read-only-modell (siehe GLOBAL_LESSONS.md READ-ONLY-GLOBALE-SCHICHT)

offene andock-fracture (aus fabrik_meta_workflow.json) | fr.lessons-no-index (lessons-hierarchie braucht index → lessons/INDEX.md deckt das jetzt) | be.cron.rules merge noch offen (HITL-gate)
