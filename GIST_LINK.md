# Gist-Brücke

Stand 2026-06-21 — Infrastruktur auf vier Gists umgebaut. Alte IDs (`6fb4ba84…`, `48b997e5…`, `7f5af9dd…`) sind **tot (404)** und nicht mehr verwenden.

| Gist | ID | Zweck | Dateien |
|------|----|-------|---------|
| **Wegweiser** | `415ba74b768bc53ecb4e3231ae7caf9d` | Index/Navigation, Einstiegspunkt | Wegweiser.md |
| **Lessons für Supervisoren** | `4268d8013cd341f414194099ebbd57d7` | Globale Lessons-Wissensbasis | GLOBAL_LESSONS.md, `1. Lessons_Übersicht.md`, Lessons_RAG.md |
| **Templates für Bootstrap** | `e3a95ed1132da6e959dc3471f7625298` | Rollen- und Projekt-Templates | Template_worker.md, Template_Supervisor.md, MARATHON_WORKFLOW_TEMPLATE.md, lessons_TEMPLATE.md, FINDING_TEMPLATE.md, DECISIONS_TEMPLATE.md, FEATURE_REQUEST_TEMPLATE.md, HANDOVER_TEMPLATE.json, HUMAN_TESTS_TEMPLATE.json, SCHALTPLAN_PROJEKT_TEMPLATE.json, CRON_PROMOTION_SPEC.md |
| **Die Reise** | `39d5425e1f86af551e2ca39d34d6587d` | Narrativ/Projekt-Reise | Die Reise |

## Lokal ↔ Gist Namensmapping

Die Gist-Dateinamen weichen z.T. von den lokalen Dateinamen ab. Der Publisher matched per **Dateiname im Staging-Dir = Gist-Dateiname** — beim Stagen entsprechend umbenennen:

| Lokal (Repo) | Gist-Datei |
|--------------|-----------|
| `templates/CLAUDE_PROJEKT_TEMPLATE.md` (Coda/Worker-Bibel) | `Template_worker.md` |
| `templates/SUPERVISOR_PROJEKT_TEMPLATE.md` | `Template_Supervisor.md` |
| `GLOBAL_LESSONS.md` | `GLOBAL_LESSONS.md` |

Übrige Templates (MARATHON_WORKFLOW, lessons, FINDING, DECISIONS, FEATURE_REQUEST, HANDOVER, HUMAN_TESTS, SCHALTPLAN, CRON_PROMOTION_SPEC) sind unter gleichem Namen im Templates-Gist.

## Raw-URLs (Latest, ohne SHA)

Pattern: `https://gist.githubusercontent.com/Bmad82/{gist_id}/raw/{filename}`

### Wegweiser
- Wegweiser.md: https://gist.githubusercontent.com/Bmad82/415ba74b768bc53ecb4e3231ae7caf9d/raw/Wegweiser.md

### Lessons-Gist
- GLOBAL_LESSONS.md: https://gist.githubusercontent.com/Bmad82/4268d8013cd341f414194099ebbd57d7/raw/GLOBAL_LESSONS.md
- Lessons_RAG.md: https://gist.githubusercontent.com/Bmad82/4268d8013cd341f414194099ebbd57d7/raw/Lessons_RAG.md

### Templates-Gist
- Template_worker.md: https://gist.githubusercontent.com/Bmad82/e3a95ed1132da6e959dc3471f7625298/raw/Template_worker.md
- Template_Supervisor.md: https://gist.githubusercontent.com/Bmad82/e3a95ed1132da6e959dc3471f7625298/raw/Template_Supervisor.md
- MARATHON_WORKFLOW_TEMPLATE.md: https://gist.githubusercontent.com/Bmad82/e3a95ed1132da6e959dc3471f7625298/raw/MARATHON_WORKFLOW_TEMPLATE.md

## Patch-Workflow

`python workflow/gist_publisher.py --patch <gist_id> <staging_dir>`

Token kommt aus `git credential fill` (Windows Credential Manager), nicht hartkodiert. PATCH lässt nicht-gestagete Dateien des Gists unangetastet — Staging-Dir nur mit den zu aktualisierenden Dateien füllen (unter dem Gist-Dateinamen).

## Zweck

Der Supervisor (Chat-Instanz auf claude.ai) kann GitHub-Raw-Links **nicht** fetchen, aber Gists **schon**. Diese Datei ist die Source of Truth der kanonischen Gist-URLs für alle Supervisor-Instanzen und den Lessons-Cron-Job.

## Wartung

- **Wegweiser:** Wird aktualisiert, wenn ein neues Projekt/eine neue Navigation hinzukommt.
- **Lessons-Gist:** Wird aktualisiert, wenn `GLOBAL_LESSONS.md` o.Ä. sich ändert, oder durch den Lessons-Cron-Job.
- **Templates-Gist:** Wird aktualisiert, wenn ein Template sich ändert.
- **Projekt-Gists:** Werden von Coda am Session-Ende aktualisiert (zusammen mit den lokalen Dateien).
- Alle Gists sind PUBLIC — keine Auth nötig für Lesezugriff.
- IDs driften: bei Verdacht via `https://api.github.com/users/Bmad82/gists` gegenchecken.

## Verifikation

Stand 2026-06-21 — alle vier Gists liefern HTTP 200 anonym; die in dieser Datei gelisteten Raw-URLs per HEAD auf 200 geprüft.
