# _archive/ — Abgelöste & veraltete Dateien (Audit, nicht live)

Hier liegen Dateien, die **bewusst aus dem aktiven Betrieb genommen** wurden, aber für die Historie erhalten bleiben. Nichts hier wird beim Session-Start gelesen oder aktiv gepflegt. Wenn du nach dem aktuellen Stand suchst, ist die Datei hier **nicht** die Quelle.

Unterschied zu `_erledigt/`: dort liegen abgeschlossene FEATURE_REQUEST-Aufträge (Auftrags-Audit). Hier liegen **abgelöste Inhalts-/Struktur-Dateien**.

Eingeräumt im Zuge von `ordner-cleanup` (2026-06-19). Siehe [`../INVENTORY.md`](../INVENTORY.md) für die volle Begründung.

| Datei | Warum hier | Ersetzt durch |
|---|---|---|
| `GLOBAL_LESSONS_KONTEXT.md` | Älterer, prosareicherer Zwilling von GLOBAL_LESSONS.md; fehlten die neuesten Lessons. Die wertvolle „Anlass/Lesson generalisierbar"-Prosa wurde am 2026-06-19 in `GLOBAL_LESSONS.md` zurückgemergt. | [`../GLOBAL_LESSONS.md`](../GLOBAL_LESSONS.md) |
| `LESSONS_KONSOLIDIERT.md` | P49-Lessons-Snapshot (2026-05-15) aus Supervisor-Chats. Enthält einige unique alte Lessons (PWA, CSS-Industriepanel, Claude-Design-Workflow) — Extraktion nach `lessons/` steht noch offen (siehe `DECISIONS_PENDING.md`). | teils `GLOBAL_LESSONS.md` |
| `REPO_INVENTORY.md` | Einmal-Bestandsaufnahme (2026-05-18). | [`../REPO_INDEX.md`](../REPO_INDEX.md) |
| `SUPERVISOR_BRIEFING.md` | Einmal-Infopaket für Repo-Restrukturierung (2026-05-18). Auftrag erledigt. | — (historisch) |
| `GIT_DIAGNOSE.md` | Einmal-Diagnose (2026-05-18): Push-Verifikation. Ergebnis als Lesson in `lessons/git-deployment.md`. | `lessons/git-deployment.md` |
| `INDEX_GIST_DRAFT.md` | Konzept-Entwurf für Index-Gist; Gist-Infra ist realisiert. | [`../GIST_LINK.md`](../GIST_LINK.md) |
| `ZERBERUS_GIST_DRAFT.md` | Konzept-Entwurf für Zerberus-Projekt-Gist; überholt. | [`../GIST_LINK.md`](../GIST_LINK.md) |

**Regel:** Wiederbeleben nur mit gutem Grund. Wenn eine Datei hier wieder aktiv wird, raus aus `_archive/` und in den passenden Live-Ordner — nicht von hier aus referenzieren.
