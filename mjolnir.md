# mjolnir.md — Claude (Meta-Repo)

```
STATUS|FERTIG|AUFTRAG: orchestrator-konsolidierung|FORTSCHRITT: 3 von 3 Paketen | EINE Coding-Session|NÄCHSTE SESSION: BACKLOG/Auffüll — keine FR offen
```

**STATUS:** FERTIG
**AUFTRAG:** `FEATURE_REQUEST_CLAUDE.md` orchestrator-konsolidierung (Drei Arbeitspakete: GLOBAL_LESSONS-Updates, ORCHESTRATOR_KONZEPT_v2-Korrekturen, Template-Check). Umbenannt zu `FEATURE_REQUEST_CLAUDE_orchestrator-konsolidierung_ERLEDIGT.md`.
**FORTSCHRITT:** Alle drei Pakete in EINER Coding-Session. Paket 2 (ORCHESTRATOR_KONZEPT_v2.md) — `--bare` durch `--settings ./worker-config.json` ersetzt mit OAuth-Begründung, Agent-Teams-Billing als geklärt markiert, Weg-B-Status aktualisiert, Empfohlene Reihenfolge entsprechend angepasst. Paket 1 (GLOBAL_LESSONS.md) — 4 neue Lessons oben angehängt: `--bare` bricht OAuth, Billing-Split-Faustformel, Credits verfallen ohne Claim, Model-IDs mit Datum-Suffix sterben (alle im Bibel-Format + Anlass-Prosa). Paket 3 (Templates) — `grep "20250514"` über `templates/` = 0 Treffer (sauber), Billing-Kommentar als HTML-Block in `CLAUDE_PROJEKT_TEMPLATE.md` eingefügt; FEATURE_REQUEST_TEMPLATE nicht angefasst (Billing-Relevanz wäre Overengineering, ist globale Lesson). Claude-KB-Gist (`48b997e5...`) per `gist_publisher.py --patch` aktualisiert mit neuer GLOBAL_LESSONS. REPO_INDEX.md minimal-Update (Datum + Drift-Hinweis), kein voller Re-Sync.
**NÄCHSTE SESSION:** Keine FR offen. Auffüll-Regel greift falls Token-Budget. REPO_INDEX hat seit 2026-05-18 erheblichen Drift (mw-v2a/v2b, Kintsugi, Orchestrator-Konzept) — als eigener Auftrag vorgemerkt, nicht hier gefixt um Diff-Noise zu vermeiden.

---

## Was diese Session war

Coda hat `FEATURE_REQUEST_CLAUDE.md` (orchestrator-konsolidierung) als Sammel-Auftrag mit drei Paketen abgearbeitet. Anlass: ORCHESTRATOR_KONZEPT_v2 hatte `--bare` als Worker-Isolation empfohlen — Web-Recherche zur Verifikation zeigte OAuth-Bruch. Gleichzeitig drei neue Anthropic-Billing-/Modell-Themen (Billing-Split ab 15.06., Credit-Claim, Modell-ID-Retirement) als globale Lessons hinterlegen, damit sie projektübergreifend gelten.

## Was geliefert wurde

**Paket 2 — `ORCHESTRATOR_KONZEPT_v2.md` korrigiert (Claude-Repo)**
- Sektion „Was sich NICHT ändert": `--bare` ersetzt durch `--settings ./worker-config.json` mit `{"disableAllHooks": true}`. OAuth-Bruch erklärt, Issue #48840 verlinkt.
- Tabelle „Technische Schlüssel-Findings": Zwei Zeilen — saubere Hook-Isolation (Abo-tauglich) + `--bare` mit Warnhinweis.
- „Offene Punkte" Punkt 1: Agent-Teams-Billing als ✅ GEKLÄRT markiert (interaktiv = Abo, aber Rate-Limit proportional).
- „Drei Lösungswege" Weg B: Offene Frage → Geklärt, als mittelfristige Option.
- „Empfohlene Reihenfolge": Weg A jetzt sofort, Weg B mittelfristig, Weg C Endgame.

**Paket 1 — `GLOBAL_LESSONS.md` (Claude-Repo)**
Vier neue Sektionen oben angehängt (nach Header-Block), jeweils im Bibel-Format (Pipe-Line) + Anlass-Block (fett-prosaisch) + Generalisierung:
- `--bare` bricht OAuth (2026-05-23, Orchestrator-Konzept)
- Billing-Split-Faustformel (2026-05-23, Anthropic Billing)
- Credits verfallen ohne Claim (2026-05-23, Anthropic Billing)
- Model-IDs mit Datum-Suffix sterben (2026-05-23, Anthropic)

**Paket 3 — Template-Check (Claude-Repo)**
- 3a: `CLAUDE_PROJEKT_TEMPLATE.md` mit HTML-Kommentar-Block zur Billing-Split-Warnung versehen (oben nach dem TEMPLATE-Kommentar).
- 3b: `FEATURE_REQUEST_TEMPLATE.md` — KEINE Änderung (Empfehlung aus FR: Overengineering vermeiden, Billing ist globale Lesson).
- 3c: `grep "20250514" templates/` — 0 Treffer, sauber.

**Gist-Sync:** Claude-KB-Gist (`48b997e53ff331eeefef53c810ee7331`) per `python workflow/gist_publisher.py --patch ... /tmp/claude_kb_staging` → `PATCHED=GLOBAL_LESSONS.md`. Index-Gist + Projekt-Gists nicht betroffen.

**REPO_INDEX.md:** Minimal-Update (Datum + Drift-Hinweis). Voller Re-Sync ist Folge-Auftrag.

## Bekannte Limitations

- REPO_INDEX hat erheblichen Drift (Stand 2026-05-18 vs. aktueller Repo-Stand). Neue Dateien wie `DESIGN_KINTSUGI.md`, `GLOBAL_LESSONS_KONTEXT.md`, `ORCHESTRATOR_KONZEPT_v2.md`, `Projektanfrage.html`, `mjolnir.md`, `scripts/`, `_drafts_gist/WORKFLOW_SUMMARY.md` fehlen im Tree.
- `--settings`-Worker-Config-Beispiel im ORCHESTRATOR_KONZEPT_v2.md ist nur Snippet `{"disableAllHooks": true}` — falls weitere Felder (z.B. `disableAllSkills`) erwünscht sind, müssten die in einer Follow-up-Session ergänzt werden.

## Was Chris noch machen muss (physisch)

- **Vor dem 15. Juni 2026:** Anthropic-Aktivierungs-Mail abwarten (~8. Juni) und auf den Claim-Link klicken, sonst verfallen die monatlichen Agent-SDK-Credits.
- **Optional:** Mjölnir-Backend von `claude -p` auf interaktiven Startweg umstellen (siehe ORCHESTRATOR_KONZEPT_v2 Weg A — Bildschirm-Klick via RustDesk). Eigene FR sinnvoll.
- **Optional:** `grep -r "20250514" .` über alle weiteren Projekt-Repos laufen lassen (außerhalb des Claude-Repos prüfen).
