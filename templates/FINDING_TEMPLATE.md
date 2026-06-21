TEMPLATE | kopie als FINDINGS_{PROJEKT}.md ins projekt-root | append-only | maschinen-only

zweck | der read-only-konforme schreib-kanal fuer supervisor/worker/solver | diese rollen schreiben NIE in lessons/GLOBAL_LESSONS/gists, sondern legen erkenntnisse HIER ab | der cron (templates/CRON_PROMOTION_SPEC.md) fetcht diese findings, urteilt ueber generalisierbarkeit und promoviert taugliche zur globalen schicht
wann | bei jedem >=2-min-stolperstein ODER nach einer eskalation (repair-eskalations-protokoll punkt 7, GLOBAL_LESSONS.md) | wand + angewandte lesson + ergebnis nie nur still selbstheilen
format | je finding ein block im lesson-schema + promotion-meta | wall_signatur literal (error-klasse, traceback-phrase, lib-name, literal-strings) damit der cron-tf-idf gegen bestehende lessons dedupt | dieselben felder wie eine lesson → promotion ist 1:1-uebernahme

schema je finding:
wall_signatur | <literale symptom-/wand-vokabeln>
kategorie | <z.b. fixture/mock, cuda-mismatch, path-portability, workflow/...>
fix | <knapp, was tun>
kontext | <eine zeile anwendungsgrenze: wann gilt, wann nicht>
quelle | <ref auf eskalation/patch/commit/session, sonst leer>
scope | lokal | global-kandidat   (vermutung des finders; der cron entscheidet final)
gesehen | {PROJEKT} {YYYY-MM-DD}   (mehrere zeilen wenn in mehreren projekten/sessions getroffen → staerkt den global-kandidaten)
status | neu | vom-cron-gesichtet | promoviert | lokal-behalten

---

wall_signatur | {literale wand-vokabeln}
kategorie | {kategorie}
fix | {was tun}
kontext | {anwendungsgrenze}
quelle | {ref}
scope | {lokal|global-kandidat}
gesehen | {PROJEKT} {YYYY-MM-DD}
status | neu

pflege
- append-only: neue findings unten anhaengen, alte nie umschreiben (der cron setzt status)
- keine dubletten von hand: gibt es schon ein finding mit gleicher wand-signatur → gesehen-zeile ergaenzen statt neuen block (das ist das >=2-projekte-signal fuer den cron)
- promoviertes finding bleibt mit status=promoviert stehen (audit-spur), wird nicht geloescht
