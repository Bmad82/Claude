# FEATURE_REQUEST: orchestrator-konsolidierung

## STATUS: FERTIG (2026-05-24)

## KURZNAME: orchestrator-konsolidierung

---

## Auftrag

Drei Arbeitspakete in einer Session — alle betreffen das Claude-Repo (Projektstruktur), keines betrifft Mjölnir oder Zerberus direkt.

---

## Paket 1: GLOBAL_LESSONS aktualisieren

Vier neue Lessons in `GLOBAL_LESSONS.md` im Claude-KB-Gist eintragen. Format: Bibel-Format (Pipe-getrennt), Anlass-Block prosaisch darunter. Neue Lessons OBEN anhängen (neueste zuerst).

### Lesson A: `--bare` bricht OAuth (2026-05-23, Orchestrator-Konzept)

```
--bare deaktiviert Hooks+CLAUDE.md+MCP+Skills — aber auch OAuth|Erzwingt ANTHROPIC_API_KEY|Für Abo-Nutzer nicht brauchbar|Alternative: --settings ./config.json mit {"disableAllHooks": true}|GitHub Issue #48840 fordert --no-hooks ohne OAuth-Bruch, existiert noch nicht|NIEMALS --bare in Playbooks empfehlen die im Abo-Modus laufen sollen
```

**Anlass:** ORCHESTRATOR_KONZEPT_v2 empfiehlt `--bare` für Worker-Isolation. Web-Recherche zeigt: `--bare` bricht den OAuth-Flow, weil es den kompletten Startup-Prozess umgeht. Worker-Sessions die per `--bare` gestartet werden, brauchen einen manuell gesetzten `ANTHROPIC_API_KEY` — das widerspricht dem Abo-Modell, bei dem OAuth die Authentifizierung übernimmt. Die Alternative `--settings` mit `disableAllHooks: true` deaktiviert Hooks ohne OAuth zu brechen.

### Lesson B: Billing-Split-Faustformel (2026-05-23, Anthropic Billing)

```
Ab 15. Juni 2026: Wer tippt den Prompt?|Mensch am Terminal = interaktiv = Abo|Maschine/Script/Cron = programmatisch = Credit-Pool mit API-Raten|claude -p, Agent SDK, GitHub Actions → Credit-Pool|Interaktive Terminal-Sessions + Claude.ai + Cowork → Abo|Agent Teams in-process = interaktiv (Mensch sitzt am Terminal), aber Rate-Limit proportional zu Anzahl paralleler Teammates
```

**Anlass:** Anthropic Billing-Split angekündigt am 14. Mai 2026, wirksam ab 15. Juni. Mjölnir startet aktuell `claude -p` und fällt damit in den teuren Topf. Die Faustformel "Wer tippt?" ist die einfachste Entscheidungshilfe.

### Lesson C: Credits verfallen ohne Claim (2026-05-23, Anthropic Billing)

```
Agent SDK Credits sind pro Account|Nicht poolbar, nicht übertragbar|Verfallen am Monatsende ohne Rollover|Müssen EINMALIG per Mail-Link beansprucht werden|Mail kommt ~8. Juni 2026|Ohne Claim vor 15. Juni → kein Credit|Danach automatische monatliche Erneuerung
```

**Anlass:** Anthropic Help Center (15036540). Viele Power-User werden die Mail übersehen — das ist bares Geld das verfällt.

### Lesson D: Model-IDs mit Datum-Suffix sterben (2026-05-23, Anthropic)

```
claude-sonnet-4-20250514 und claude-opus-4-20250514 werden am 15. Juni 2026 abgeschaltet|Immer Aliase OHNE Datum-Suffix verwenden: claude-sonnet-4-6, claude-opus-4-6|Grep-Check in allen Projekten: grep -r "20250514" .|Betrifft: LLM-Config, Guard-Config, Persona-Config, Mjölnir Model-Selector, OpenRouter-Aufrufe
```

**Anlass:** Anthropic Modell-Retirement-Policy. Wer hartgecodete Datum-Suffixe hat, bekommt am 15. Juni Fehler.

---

## Paket 2: ORCHESTRATOR_KONZEPT_v2.md korrigieren

Die Datei `ORCHESTRATOR_KONZEPT_v2.md` liegt im Projektstruktur-Ordner (Chris hat sie abgelegt). Folgende Korrekturen einarbeiten:

### Korrektur 1: `--bare` durch `--settings` ersetzen

**Suche:** Alle Stellen die `--bare` als Lösung für Worker-Isolation empfehlen.

**Ersetze durch:** `--settings ./worker-config.json` mit `{"disableAllHooks": true}`.

**Begründung einfügen:** `--bare` bricht OAuth. Für Abo-Nutzer nicht brauchbar. `--settings` deaktiviert Hooks ohne den Auth-Flow zu zerstören. Sobald GitHub Issue #48840 (`--no-hooks`) landed, kann das vereinfacht werden.

**Konkret betroffen (mindestens):**
- Abschnitt "Was sich NICHT ändert (technisch validiert)" → `--bare` Flag-Beschreibung
- Jede Stelle die `--bare` als "vollen Kontext-Isolation" beschreibt

### Korrektur 2: Agent Teams Billing-Ergebnis eintragen

Im Abschnitt "Offene Punkte" steht:
> 1. **In-Process Agent Teams Billing:** Zählt `--teammate-mode in-process` als interaktiv (Abo) oder programmatisch (Kredit)? → Entscheidend für Weg B.

**Ersetze durch:**
> 1. **In-Process Agent Teams Billing:** ✅ GEKLÄRT — zählt als interaktiv (Abo), weil der Mensch am Terminal sitzt. Aber: Rate-Limit wird proportional zur Anzahl paralleler Teammates aufgebraucht (10 Agents = 10x schneller). Kein Kredit-Problem, aber ein Tempo-Problem. Quelle: Anthropic Help Center + CloudZero-Analyse.

### Korrektur 3: Weg B Status aktualisieren

Im Abschnitt "Drei Lösungswege" bei Weg B:

**Ersetze:**
> **Offene Frage:** Zählt das als interaktiv (Abo) oder programmatisch (Kredit)? Wenn interaktiv → Königsweg. Wenn nicht → Sackgasse.

**Durch:**
> **Geklärt:** Zählt als interaktiv (Abo). Königsweg-Potential bestätigt, aber noch Research Preview und frisst Rate-Limit proportional. Als Brücke vor dem 15. Juni nicht tauglich (zu experimentell), als mittelfristige Option interessant.

---

## Paket 3: Template-Check

Prüfe ob bestehende Templates Anpassungen brauchen:

### 3a. CLAUDE_PROJEKT_TEMPLATE.md

Prüfe ob ein Hinweis zum Billing-Split rein sollte. Empfehlung: JA, als Kommentar-Block:
```
<!-- Ab 15. Juni 2026: claude -p fällt in Credit-Pool. Interaktive Sessions bleiben im Abo.
     Wenn dieses Projekt Headless-Sessions nutzt (z.B. via Mjölnir), muss der Session-Start
     auf interaktiv umgestellt werden. Siehe GLOBAL_LESSONS: Billing-Split-Faustformel. -->
```

### 3b. FEATURE_REQUEST_TEMPLATE.md

Prüfe ob das Template einen optionalen Abschnitt "Billing-Relevanz" braucht. Empfehlung: NEIN, das wäre Overengineering. Billing ist eine globale Lesson, kein Feature-Request-Attribut.

### 3c. Alle Templates: Model-ID-Check

Grep alle Templates nach `20250514`. Falls gefunden → durch Aliase ohne Suffix ersetzen.

---

## Reihenfolge

1. ORCHESTRATOR_KONZEPT_v2.md korrigieren (Paket 2) — weil GLOBAL_LESSONS auf das korrigierte Dokument verweisen
2. GLOBAL_LESSONS aktualisieren (Paket 1)
3. Template-Check (Paket 3)
4. Gist aktualisieren (Claude-KB-Gist mit neuer GLOBAL_LESSONS)
5. REPO_INDEX.md aktualisieren falls sich Dateien geändert haben
6. Commit + Push
7. mjolnir.md schreiben

---

## Akzeptanzkriterien

- [ ] ORCHESTRATOR_KONZEPT_v2.md: Kein `--bare` mehr als Empfehlung für Abo-Nutzer
- [ ] ORCHESTRATOR_KONZEPT_v2.md: `--settings`-Alternative dokumentiert
- [ ] ORCHESTRATOR_KONZEPT_v2.md: Agent Teams Billing als geklärt markiert
- [ ] ORCHESTRATOR_KONZEPT_v2.md: Weg B Status aktualisiert
- [ ] GLOBAL_LESSONS.md: 4 neue Lessons im Bibel-Format, oben angehängt
- [ ] GLOBAL_LESSONS.md: Keine Duplikate mit bestehenden Lessons
- [ ] Templates: Kein `20250514` in irgendeinem Template
- [ ] Templates: CLAUDE_PROJEKT_TEMPLATE hat Billing-Kommentar
- [ ] Claude-KB-Gist: GLOBAL_LESSONS aktualisiert
- [ ] REPO_INDEX.md: Aktuell
- [ ] Commit-Message: `feat: orchestrator-konsolidierung — billing-lessons, --bare-korrektur, template-check`
- [ ] mjolnir.md: Geschrieben mit STATUS-Header

---

## Was NICHT angefasst werden darf

- Mjölnir-Code (eigener Feature Request läuft separat)
- Zerberus-Code (eigenes Handover liegt bei Chris)
- Bestehende Lessons (nicht ändern, nur neue anhängen)
- Showcase-HTMLs (kosmetisch, nicht jetzt)

---

*Erstellt: 23. Mai 2026 · Supervisor-Session · Bezug: HANDOVER_PROJEKTSTRUKTUR_20260523.md*
