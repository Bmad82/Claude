# lessons/INDEX.md — Lessons-Hierarchie

Dieses Repo hat **mehrere Lessons-Quellen** auf unterschiedlichen Ebenen. Diese Datei erklärt, was wo liegt und welche Datei für welchen Zweck konsultiert wird.

## Drei Ebenen

### 1. Workflow-Lessons (im Root)

Universelle Erkenntnisse über den Marathon-Workflow selbst — gelten für jedes Projekt, das diesen Workflow nutzt.

| Datei | Zweck |
|---|---|
| [`../GLOBAL_LESSONS.md`](../GLOBAL_LESSONS.md) | **Aktive operative Quelle.** Faulheits-Catches, Selbsttest-Pattern, Bibel-Format, Multi-Session-Pattern, Naming-Konvention. Bibel-Format. Wird bei jeder Workflow-Erkenntnis ergänzt. |
| [`../LESSONS_KONSOLIDIERT.md`](../LESSONS_KONSOLIDIERT.md) | Älterer Snapshot (Stand 2026-05-15) aus Supervisor-Chats. Konsolidierung mit GLOBAL_LESSONS.md noch offen — siehe [`../DECISIONS_PENDING.md`](../DECISIONS_PENDING.md). |

**Regel:** Workflow-Erkenntnisse (Mjölnir, Faulheits-Catches, Session-Hygiene) gehören nach `GLOBAL_LESSONS.md`. Nicht in den thematischen `lessons/`-Ordner.

### 2. Technologie-Lessons (hier in `lessons/`)

Thematische Stolpersteine, die mehrere Projekte betreffen können — pro Technologie eine Datei.

| Datei | Themengebiet |
|---|---|
| [`documentation.md`](documentation.md) | Schulungsunterlagen, Shop-Floor-Kontext |
| [`frontend-js.md`](frontend-js.md) | Frontend, JavaScript, Newline-Escaping, HTML-Rendering |
| [`git-deployment.md`](git-deployment.md) | Git, Deployment, Aktivierungspfade, Uvicorn-Start |
| [`gpu-ml.md`](gpu-ml.md) | GPU/ML, Device-Detection, VRAM-Fallback, Test-Isolation |
| [`json-data.md`](json-data.md) | JSON, typographische Anführungszeichen |
| [`mobile-touch.md`](mobile-touch.md) | Mobile/Touch, `:hover` vs `:active` |
| [`python-fastapi.md`](python-fastapi.md) | Python/FastAPI, Uvicorn `--reload` auf Windows |
| [`sqlite-db.md`](sqlite-db.md) | SQLite, idempotente Migrationen, PRAGMA-Checks |
| [`testing.md`](testing.md) | Testing (Playwright/pytest), self-signed HTTPS |
| [`whisper-transcription.md`](whisper-transcription.md) | Whisper, Spracheingabe, Transkriptions-Handling |
| [`workflow.md`](workflow.md) | Claude-CLI-Workflow, YOLO-Modus, Git-Checkpoints |

**Regel:** Wenn eine Erkenntnis aus einem Projekt potenziell für andere Projekte (in einer anderen Technologie-Domäne) relevant ist, hier eintragen. Format: kurz, konkret, Problem → Lösung. Quellprojekt + Patchnummer als Referenz, z.B. `(Zerberus P89)`.

### 3. Projekt-Lessons (im jeweiligen Projekt-Repo)

Projektspezifische Stolpersteine gehören **NICHT** in dieses Repo, sondern in das Projekt-Repo als `lessons_{PROJEKT}.md`. Vorlage: [`../templates/lessons_TEMPLATE.md`](../templates/lessons_TEMPLATE.md).

| Projekt | Master-Datei | Sync-Status |
|---|---|---|
| Zerberus | `lessons_zerberus.md` im Zerberus-Repo (`C:\Users\chris\Python\Zerberus\`) | [`zerberus_lessons.md`](zerberus_lessons.md) hier ist eine **Sync-Kopie** (ca. 300 KB, ~1022 Zeilen). Master liegt im Zerberus-Repo. Konsolidierung mit GLOBAL_LESSONS.md offen (siehe DECISIONS_PENDING.md). |

**Regel:** Projektspezifische Lessons-Dateien bleiben primär im Projekt-Repo. Eine Sync-Kopie hier ist erlaubt, muss aber als solche markiert sein (siehe `zerberus_lessons.md` Header). Neue Projekte kopieren `templates/lessons_TEMPLATE.md` in ihr eigenes Repo, nicht hierher.

## Konsultations-Reihenfolge bei neuem Patch

Nicht ALLE Lessons-Dateien bei jedem Patch lesen — das wäre Token-Verschwendung. Konsultations-Regel:

1. **Immer**: `GLOBAL_LESSONS.md` (Workflow-Catches sind universell)
2. **Immer für Projekt-Patches**: `lessons_{PROJEKT}.md` im Projekt-Repo
3. **Themenbezogen**: Nur die `lessons/{technologie}.md`-Dateien, die zur aktuellen Aufgabe passen. Beispiel: Frontend-Patch → `frontend-js.md` + `mobile-touch.md`, nicht `gpu-ml.md`.

## Eintragungs-Regel nach Patch

Bei einem ≥ 2-Min-Stolperstein:

- **Workflow-Erkenntnis** (Session-Hygiene, Coda-Verhalten, Supervisor-Pattern) → `GLOBAL_LESSONS.md`
- **Technologie-Erkenntnis** (FastAPI, SQLite, Whisper, …) → passende `lessons/{technologie}.md`
- **Projekt-Erkenntnis** (nur in diesem Projekt relevant) → `lessons_{PROJEKT}.md` im Projekt-Repo

Doppelte Einträge vermeiden: wenn etwas projektübergreifend gilt, dann hier; wenn projektspezifisch, dann dort.
