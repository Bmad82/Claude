lessons/INDEX | maschinen-only | lessons-hierarchie + konsultations-/eintragungs-regel

READ-ONLY: lessons sind read-only fuer supervisor, worker, solver | diese rollen schreiben NIE in lessons/GLOBAL_LESSONS/gists | erkenntnis → finding ins project-root (templates/FINDING_TEMPLATE.md) | nur der cron promoviert (templates/CRON_PROMOTION_SPEC.md)
schema je lesson: wall_signatur | kategorie | fix | kontext | quelle

drei ebenen
1 workflow-lessons (root) | universell ueber den marathon-workflow | datei: GLOBAL_LESSONS.md = aktive operative quelle (faulheits-catches, selbsttest-pattern, repair-eskalations-protokoll, schema-definition) | aelterer snapshot LESSONS_KONSOLIDIERT.md liegt archiviert in _archive/ (konsolidierung offen, siehe DECISIONS_PENDING.md)
2 technologie-lessons (hier in lessons/) | thematische stolpersteine, mehrere projekte betreffend, pro technologie eine datei
3 projekt-lessons (im jeweiligen projekt-repo) | projektspezifisch, NICHT hier | vorlage templates/lessons_TEMPLATE.md

technologie-dateien
documentation.md | schulungsunterlagen, shop-floor, doku-naming/format
frontend-js.md | frontend, js, newline-escaping, chart.js, sse, regex-portierung, xss
git-deployment.md | git, deployment, aktivierungspfade, push-verifikation
gpu-ml.md | gpu/ml, device-detection, vram, torch/cuda-install
json-data.md | json, csv, typografische anfuehrungszeichen
mobile-touch.md | mobile/touch, :hover vs :active, https-pflicht
python-fastapi.md | python/fastapi, uvicorn-reload windows, config-ssot, faiss, dedup
sqlite-db.md | sqlite, idempotente migrationen, alembic, dedup-guard
testing.md | testing (playwright/pytest), self-signed https, pageerror
whisper-transcription.md | whisper, spracheingabe, chunking, sentence-dedup
workflow.md | claude-cli-workflow, rollen, diagnose, git-checkpoints (marathon-volltext → GLOBAL_LESSONS.md)
zerberus_lessons.md | SYNC-KOPIE des master lessons_zerberus.md aus dem Zerberus-Repo (C:\Users\chris\Python\Zerberus\), ~423 KB | read-only hier, NICHT umformatieren/editieren — master ist die quelle | im wegweiser-gist separat verlinkt

konsultations-reihenfolge bei neuem patch (nicht alle dateien laden = token-verschwendung)
1 immer | GLOBAL_LESSONS.md (workflow-catches sind universell)
2 immer fuer projekt-patches | lessons_{PROJEKT}.md im projekt-repo (per lessons_lookup.py tf-idf, nicht komplett-load)
3 themenbezogen | nur die lessons/{technologie}.md die zur aufgabe passen (frontend-patch → frontend-js + mobile-touch, nicht gpu-ml)

eintragungs-regel nach patch (read-only-modell)
worker/solver schreiben KEINE lesson direkt | ein >=2-min-stolperstein → finding ins project-root (templates/FINDING_TEMPLATE.md), kategorie gewaehlt, wand-signatur literal
der cron fetcht findings, dedupt gegen bestehende lessons (gleiches tf-idf wie der worker-lookup), promoviert generalisierbare zu globalen lessons/templates (>=2 projekte ODER cron-urteil uebertragbar), project-quirks bleiben lokal
erster cron-durchlauf: nur vorschlag, chris befoerdert manuell | autonomer gist-write spaeter
