# Gist-Brücke

Index-Gist: https://gist.github.com/Bmad82/6fb4ba84419edc0e2d8290cacef1faeb
Projekt-Gist (Claude-KB): https://gist.github.com/Bmad82/48b997e53ff331eeefef53c810ee7331

## Raw-URLs (Latest, ohne SHA)

### Index-Gist
- GIST_INDEX.md: https://gist.githubusercontent.com/Bmad82/6fb4ba84419edc0e2d8290cacef1faeb/raw/GIST_INDEX.md

### Claude-KB-Gist
- GLOBAL_LESSONS.md: https://gist.githubusercontent.com/Bmad82/48b997e53ff331eeefef53c810ee7331/raw/GLOBAL_LESSONS.md
- TEMPLATES_INDEX.md: https://gist.githubusercontent.com/Bmad82/48b997e53ff331eeefef53c810ee7331/raw/TEMPLATES_INDEX.md
- WORKFLOW_SUMMARY.md: https://gist.githubusercontent.com/Bmad82/48b997e53ff331eeefef53c810ee7331/raw/WORKFLOW_SUMMARY.md
- BOOTSTRAP_CHECKLIST.md: https://gist.githubusercontent.com/Bmad82/48b997e53ff331eeefef53c810ee7331/raw/BOOTSTRAP_CHECKLIST.md

## Zweck

Der Supervisor (Chat-Instanz auf claude.ai) kann GitHub-Raw-Links **nicht** fetchen, aber Gists **schon**. Diese Datei dokumentiert die kanonischen Gist-URLs als Einstiegspunkt für alle Supervisor-Instanzen und für den Lessons-Cron-Job.

## Wartung

- **Index-Gist:** Wird nur aktualisiert, wenn ein neues Projekt hinzukommt.
- **Claude-KB-Gist:** Wird aktualisiert, wenn `GLOBAL_LESSONS.md` oder Templates sich ändern, oder durch den Lessons-Cron-Job.
- **Projekt-Gists:** Werden von Coda am Session-Ende aktualisiert (zusammen mit den lokalen Dateien).
- Alle Gists sind PUBLIC — keine Auth nötig für Lesezugriff.

## Verifikation

Stand 2026-05-18 — alle drei Gists liefern HTTP 200 anonym (curl ohne Token).
