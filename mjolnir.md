# mjolnir.md — Claude (Meta-Layer)

```
STATUS|FERTIG|AUFTRAG: gist-infrastruktur|FORTSCHRITT: 4/4 Phasen / 1 Session|NÄCHSTE SESSION: entfällt (FERTIG)
```

**STATUS:** FERTIG
**AUFTRAG:** gist-infrastruktur
**FORTSCHRITT:** 1 Session | alle 4 Phasen + Templates-Update durch | drei PUBLIC Gists live, alle Akzeptanzkriterien erfüllt
**NÄCHSTE SESSION:** entfällt

---

## Was Chris physisch tun muss

- **Index-Gist im Browser/Handy aufrufen:** https://gist.github.com/Bmad82/6fb4ba84419edc0e2d8290cacef1faeb — von dort führen Links zu Claude-KB- und Zerberus-Gist.
- **Supervisor-Memory aktualisieren** (im claude.ai-Chat-Setting): den Index-Gist-Link als „Single Source of Truth für Marathon-Workflow-Projekte" hinterlegen. Dann findet jede frische Supervisor-Instanz von selbst die Projekt-Gists, ohne dass Chris Links relayen muss.
- **Selbsttest am Handy:** Index-Gist in einer frischen, nicht-eingeloggten Browser-Session öffnen → muss HTTP 200 + Inhalt zeigen (verifiziert die PUBLIC-Eigenschaft aus Chris' Sicht).

---

## Erledigte Phasen (TL;DR)

### Phase 1 — Index-Gist (PUBLIC)
- URL: https://gist.github.com/Bmad82/6fb4ba84419edc0e2d8290cacef1faeb
- Description: „Marathon Workflow — Projekt-Index für Supervisor-Instanzen"
- Datei: `GIST_INDEX.md` mit Verweisen auf Claude-KB- und Zerberus-Gist.

### Phase 2 — Claude-KB-Gist (PUBLIC, 4 Dateien)
- URL: https://gist.github.com/Bmad82/48b997e53ff331eeefef53c810ee7331
- Description: „Claude-KB — Globale Lessons, Templates, Workflow"
- Dateien: `GLOBAL_LESSONS.md` (Volltext aus Repo + Header), `TEMPLATES_INDEX.md` (alle 10 Templates), `WORKFLOW_SUMMARY.md` (62 Zeilen, < 100), `BOOTSTRAP_CHECKLIST.md` (mit Gist-Schritt).

### Phase 3 — Claude-Repo-Updates
- `GIST_LINK.md` neu im Repo-Root: enthält Index-Gist + Claude-KB-Gist URLs (Latest-Raws, ohne SHA).
- `REPO_INDEX.md` aktualisiert: `GIST_LINK.md`, `GIT_DIAGNOSE.md`, `workflow/gist_publisher.py`, beide neuen `_erledigt/`-Audits, Datei-Statistik (46 → 51).
- `templates/CLAUDE_PROJEKT_TEMPLATE.md`: Sektion „Gist-Pflicht" + Eintrag in Doku-Pflicht-Tabelle + Schritte 5–6 im Git-Workflow am Session-Ende.
- `templates/SUPERVISOR_PROJEKT_TEMPLATE.md`: Sektion „Gist-Navigation" mit Platzhalter-Bootstrap-Pattern.
- `workflow/MARATHON_WORKFLOW.md`: `GIST_LINK.md` in Datei-Hierarchie + Schritt 12 im Session-Zyklus + neue Sektion „Gist-Brücke (Supervisor-Lesezugang)".
- `PROJECT_BOOTSTRAP_README.md`: Bootstrap-Schritt 8 (Projekt-Gist erstellen) + Tabellen-Eintrag für Gist-Brücke und Publisher.
- `workflow/gist_publisher.py` neu: Helfer-Skript für POST/PATCH gegen Gist-API (Token aus `git credential fill`, kein hartkodierter Secret). Wird vom Lessons-Cron und für künftige Projekt-Gist-Updates verwendet.

### Phase 4 — Zerberus-Gist (PUBLIC, 5 Dateien)
- URL: https://gist.github.com/Bmad82/7f5af9dd878a6a9d664f062976b27ae8
- Description: „Zerberus Pro 4.0 — Supervisor-Briefing"
- Dateien: `STATUS.md` (Bibel-Einzeiler), `HANDOVER.md` (aus Repo), `MJOLNIR.md` (aus Repo), `REPO_INDEX.md` (für Zerberus neu generiert, gleiche Konvention wie Claude-Repo), `LESSONS.md` (lessons_zerberus.md Master, 1022 Zeilen).
- Zerberus-Repo bekam zusätzlich `GIST_LINK.md` + `REPO_INDEX.md` als Commit `347e317`, Push verifiziert (ahead/behind 0/0).

---

## Gist-URLs (kanonisch, kopierfertig)

```
INDEX:        https://gist.github.com/Bmad82/6fb4ba84419edc0e2d8290cacef1faeb
CLAUDE-KB:    https://gist.github.com/Bmad82/48b997e53ff331eeefef53c810ee7331
ZERBERUS:     https://gist.github.com/Bmad82/7f5af9dd878a6a9d664f062976b27ae8
```

Raw-Latest-Pattern: `https://gist.githubusercontent.com/Bmad82/{gist_id}/raw/{filename}.md`

---

## Akzeptanzkriterien (alle ✓)

- [x] Index-Gist existiert, ist PUBLIC, enthält `GIST_INDEX.md`
- [x] Claude-KB-Gist existiert, ist PUBLIC, enthält 4 Dateien (GLOBAL_LESSONS, TEMPLATES_INDEX, WORKFLOW_SUMMARY, BOOTSTRAP_CHECKLIST)
- [x] Claude-Repo hat `GIST_LINK.md` mit beiden URLs
- [x] Templates (CLAUDE_PROJEKT, SUPERVISOR_PROJEKT, MARATHON_WORKFLOW, PROJECT_BOOTSTRAP_README) enthalten Gist-Konvention
- [x] Session-Ende-Checkliste enthält Gist-Update-Schritt (im `Git-Workflow am Session-Ende` der CLAUDE-Template)
- [x] Zerberus hat Projekt-Gist + `GIST_LINK.md` (Commit `347e317` gepusht)
- [x] Index-Gist verweist auf alle erstellten Gists (Claude-KB + Zerberus)
- [x] Alle Pushes verifiziert (`$LASTEXITCODE` / `git rev-list --left-right --count` → 0/0)
- [x] Kein Secret/Token in Gists oder Repo — `gist_publisher.py` liest Token live aus `git credential fill`, hartkodiert nichts; gezielte Regex-Suche über alle Gist-Raws (`ghp_/gho_/sk-/AKIA/JWT/40-hex`) → 0 Treffer
- [x] Alle Gists sind PUBLIC (anonyme `curl` ohne Auth liefert HTTP 200 + Inhalt)

---

## Selbsttest-Spur (Phase A–D)

- **A Setup:** drei Staging-Verzeichnisse unter `_gist_staging/` mit den späteren Gist-Inhalten gefüllt, Pre-API-Verifikation via `wc -l`.
- **B Replay:** alle drei Gists nach Erstellung anonym (ohne Token-Header) gefetcht — HTTP 200, Inhalt identisch zu Staging.
- **C Adversarial:** Secret-Pattern-Scan (`ghp_|gho_|github_pat_|sk-|AKIA|JWT|40-hex`) gegen alle 10 Gist-Raw-Dateien — 0 Treffer.
- **D Cleanup:** `_gist_staging/` entfernt (Inhalt lebt in Gists), `create_gist.py` als `workflow/gist_publisher.py` persistiert für Cron-Job und künftige Updates.

Ein Surrogat-Hinweis: „Supervisor-Replay via Sub-Agent" entfällt — die anonyme `curl`-Fetch-Verifikation simuliert das Supervisor-Lesen ohne Auth realistisch.

---

## Commits (final)

- Claude-Repo `fb288d5` — prior-session-Audit (git-push-diagnose) committed, da vorige Coda-Session den Push vergessen hatte. Saubere Trennung Audit ↔ neuer Auftrag.
- Claude-Repo: gist-infrastruktur-Commit folgt direkt im Anschluss (mit dieser mjolnir.md + `GIST_LINK.md`, Templates, REPO_INDEX, gist_publisher.py, neuer `_erledigt/`-Audit).
- Zerberus-Repo `347e317` — `GIST_LINK.md` + `REPO_INDEX.md`, gepusht, Remote-State 0/0.

---

<!--
LIFECYCLE-Notiz für Coda:

- STATUS=FERTIG  →  beim nächsten Session-Start: mjolnir.md einlesen, dann löschen. FEATURE_REQUEST liegt bereits unter _erledigt/FEATURE_REQUEST_gist-infrastruktur_ERLEDIGT.md (kebab-case-Konvention statt CLAUDE-Filename).
- STATUS=IN_ARBEIT  →  entfällt hier.
- STATUS=BLOCKIERT  →  entfällt hier.

mjolnir.md ist Single-Slot — genau EINE Datei zur Zeit, wird beim nächsten Session-Start gelesen + gelöscht.
-->
