# mjolnir.md — Claude (Meta-Repo)

```
STATUS|FERTIG|AUFTRAG: mw-v2b-durchsetzung|FORTSCHRITT: 4 von 4 Paketen | EINE Coding-Session (Sammel-Lieferung)|NÄCHSTE SESSION: BACKLOG/Auffüll — keine FR offen
```

**STATUS:** FERTIG
**AUFTRAG:** `FEATURE_REQUEST_CLAUDE.md` mw-v2b-durchsetzung (Marathon-Workflow v2b: Mechanische Durchsetzung & Alignment). Umbenannt zu `FEATURE_REQUEST_CLAUDE_mw-v2b-durchsetzung_ERLEDIGT.md`.
**FORTSCHRITT:** Alle vier Pakete in EINER Coding-Session geliefert (Commits per Paket im Zerberus-Repo, Sammel-Commit fuer Claude-Begleit-Doku). Paket 1 (Zerberus `a031719` + `a6c3cae`) — SessionStart/PreToolUse/SessionEnd Hooks (Scripts committed, Verdrahtung opt-in). Paket 2 (Zerberus `3eb52bf` + `b6e7ce6` + `c2dded8` + Nachzug `4b02f0e`) — Lessons-Split + CLAUDE_ZERBERUS.md 282→121 Zeilen + 5 Playbooks + 2 Path-Rules in docs/claude_rules/. Paket 3 (Zerberus `4edfd35`) — SUPERVISOR_ZERBERUS.md 2423→74 Zeilen Archiv-Schnitt. Paket 4 (Claude `<HASH-C>`) — Templates + WORKFLOW + GLOBAL_LESSONS Progressive-Disclosure-Lesson + WORKFLOW_SUMMARY Gist-Update + MARATHON_WORKFLOW_ZERBERUS.md v2b-Alignment.
**NÄCHSTE SESSION:** Keine FR offen. Auffüll-Regel greift falls Token-Budget. Wenn Chris weitere Arbeit reingibt: Eröffnungs-Message hat Vorrang. Sonst BACKLOG (Zerberus B-074 ff.) oder Lessons-Hygiene.

---

## Was diese Session war

Coda hat `FEATURE_REQUEST_CLAUDE.md` (mw-v2b-durchsetzung) als Sammel-Auftrag mit vier Paketen abgearbeitet. Grundlage: Deep-Research-PDF „LLM Regelbefolgung" + Supervisor-Audit 2026-05-21. Ziel laut FR: mw-v2a-Gewinne mechanisch unumgehbar machen (Hooks) + Kern-Bibel-Wachstum stoppen (Playbooks + Path-Rules) + Naming/Doku-Drift bereinigen.

## Was geliefert wurde

**Paket 1 — Claude Code Hooks (Zerberus, opt-in via `scripts/HOOK_SETUP.md`)**
- `scripts/lessons_lookup_auto.py` (SessionStart, leitet Query aus FEATURE_REQUEST/mjolnir ab)
- `scripts/validate_edit.py` (PreToolUse, blockt Edits an Schutzdateien: GLOBAL_LESSONS, KODEX, *_TEMPLATE_*)
- `scripts/session_end_check.py` (SessionEnd, prueft mjolnir/HANDOVER/STAND/Gist-Marker als JSON systemMessage)
- `.claude/settings.json`-Verdrahtung BLEIBT OPT-IN (Chris-Entscheidung, dokumentiert in `DECISIONS_PENDING.md`)

**Paket 2 — Kern-Bibel-Schlankheitskur + Playbooks + Path-Rules (Zerberus)**
- `lessons_ZERBERUS.md` (1093 Z / 316k chars) gesplittet via `scripts/split_lessons.py` in Pipe-only (142k chars, 147 Sektionen) + `lessons_ZERBERUS_KONTEXT.md` (317k chars Prosa)
- `CLAUDE_ZERBERUS.md` (282 → 121 Zeilen) — nur noch Kern: OBERSTES GEBOT + Autonome Prioritaetsliste + 6 Faulheits-Catches + Marathon-Workflow + Session-Auffuell + Token-Effizienz + Basics-Regeln
- `playbooks/` (5 Stueck): `testing.md`, `rag_pipeline.md`, `auth_security.md`, `database.md`, `observability.md`
- `docs/claude_rules/` (opt-in Path-Rules): `frontend_mobile.md` (globs: Templates/CSS/HTML), `destructive_ops.md` (globs: *.py/scripts/alembic) + README mit Install-Variante A/B
- `.claude/rules/` ist permission-protected — Setup bleibt Chris-Entscheidung, konsistent mit Hooks-Wiring

**Paket 3 — Zerberus-Marathon-Alignment (Zerberus)**
- `SUPERVISOR_ZERBERUS.md` (2423 → 74 Zeilen), Patch-Historie ausgelagert in `SUPERVISOR_ZERBERUS_ARCHIV_2026-05-21.md`
- Naming HYPERVISOR→SUPERVISOR auditiert (verbleibende Hits sind intentional: Archiv-Audit-Logs, Don't-Reminder, technischer VM-Begriff in Huginn-Doc)

**Paket 4 — Workflow-Doku-Updates (Claude-Repo + Zerberus)**
- `MARATHON_WORKFLOW_ZERBERUS.md` Step 4 (lessons_lookup statt full-load), Steps 12-13 (session_end.ps1 + Hook-Erweiterung), neue Sektion „Playbook-Architektur"
- `workflow/MARATHON_WORKFLOW.md` Step 6/7 (lessons_lookup + Playbook-Verweis)
- `templates/CLAUDE_PROJEKT_TEMPLATE.md` (Limit-Hinweis playbooks/rules + Step 6/7-Update)
- `templates/MARATHON_WORKFLOW_TEMPLATE.md` Step 5
- `GLOBAL_LESSONS.md` + `GLOBAL_LESSONS_KONTEXT.md`: neue Lesson „Progressive Disclosure: Playbooks + .claude/rules statt Kern-Bibel-Wachstum"
- `_drafts_gist/WORKFLOW_SUMMARY.md`: Session-Zyklus + neue Sektionen Progressive-Disclosure + Hooks

## Bekannte Limitations

- `.claude/settings.json` und `.claude/rules/` sind permission-protected. Verdrahtung bleibt opt-in via `scripts/HOOK_SETUP.md` (Hooks) bzw. `docs/claude_rules/README.md` (Rules). Konsistent mit Variante A/B-Konvention.
- „Anpassungen_11_05.2026" aus dem FR ist eine Projekt-Knowledge-Datei in claude.ai, nicht im Repo — kann Coda nicht editieren. Supervisor-Aufgabe.
- Backups (`CLAUDE_ZERBERUS.md.bak_pre_v2b_paket2`, `lessons_ZERBERUS.md.bak_pre_v2b`, `GLOBAL_LESSONS.md.bak_pre_v2b`) liegen im Repo und sind in `.gitignore` ausgeschlossen oder werden bei Bedarf manuell entfernt.

## Was Chris noch machen muss (physisch)

- **Optional:** `.claude/settings.json` aktivieren (Hook-Verdrahtung) — Anleitung in `Zerberus/scripts/HOOK_SETUP.md`. Variante B (`settings.local.json`) ist sicherer Default.
- **Optional:** `.claude/rules/` aktivieren — `cp Zerberus/docs/claude_rules/*.md Zerberus/.claude/rules/`. README im selben Verzeichnis.
- Projekt-Knowledge „Anpassungen_11_05.2026" in claude.ai mit „⚠️ HISTORISCH"-Header versehen (Supervisor-Aufgabe, nicht Coda).
- Gist-Sync nach diesem Commit — passiert idealerweise via `scripts/session_end.ps1`, falls Chris den `gist_publisher.py --patch`-Aufruf manuell triggern moechte.
