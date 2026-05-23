# Marathon Workflow v3 — Orchestrator-Konzept v2

## Die ehrliche Architektur nach dem 15. Juni 2026

**Autor:** Chris (Architekt) · **Konzeptarbeit:** Supervisor
**Stand:** 23. Mai 2026
**Quellen:** Copilot Deep Research, Gemini Deep Research (technische Machbarkeit), Web-Recherche (Anthropic Billing Split)

---

## Was sich seit v1 geändert hat

Am 14. Mai 2026 hat Anthropic angekündigt, dass ab dem **15. Juni 2026** alle programmatischen Aufrufe (`claude -p`, Agent SDK, GitHub Actions, Dritt-Agenten) aus dem Abo-Kontingent herausgelöst und in einen separaten Kredit-Topf verschoben werden — abgerechnet zu **vollen API-Listenpreisen**, ohne Max-Rabatt, ohne Rollover.

| Abo-Stufe | Monatlicher Kredit | Abrechnung |
|---|---|---|
| Pro | 20 USD | Voller API-Preis |
| Max 5x | 100 USD | Voller API-Preis |
| Max 20x | 200 USD | Voller API-Preis |

**Was das für den Marathon-Workflow bedeutet:**

- **Mjölnir startet aktuell `claude -p` (Headless).** Das fällt ab Juni in den teuren Topf.
- **Interaktive Claude-Code-Sessions bleiben im Abo** — unverändert.
- **100 USD zu API-Vollpreis** reichen für einen Power-User nicht annähernd. Ein einzelner Opus-Patch kann mehrere Dollar kosten.
- **Das v1-Konzept** (Orchestrator spawnt Worker per SDK/`-p`) ist unter dieser Bepreisung **wirtschaftlich nicht tragfähig** für den Dauerbetrieb.

**Konsequenz:** Das Konzept muss grundlegend umgebaut werden — weg von Claude als Dauerläufer, hin zu einem Hybrid-Modell mit Claude als Premium-Gutachter.

---

## Das Hybrid-Modell: DeepSeek baut, Claude prüft

### Die neue Rollenverteilung

```
                        BILLIG                           TEUER (aber selten)
                        ══════                           ══════════════════
                        
Architekt (Chris)  ──→  DeepSeek V4 Pro (Zerberus)  ──→  Claude (Monokel-Review)
                        │                                 │
                        │ Bulk-Arbeit:                    │ Gutachter-Rolle:
                        │ - Code schreiben                │ - Architektur-Review
                        │ - Tests bauen                   │ - Security-Audit
                        │ - Refactoring                   │ - Code-Qualität
                        │ - Patches abarbeiten            │ - Strategische Fragen
                        │                                 │
                        │ Kosten: API/selbstgehostet      │ Kosten: Im Abo (interaktiv)
                        │ Frequenz: Dauerhaft             │ Frequenz: 1x pro Iteration
                        └─────────────────────────────────┘
```

### Warum das funktioniert

- **DeepSeek** ist günstig genug für Dauerbetrieb (API oder perspektivisch self-hosted auf RTX 3060)
- **Claude** wird nur für den Final Refine eingesetzt — hoher Hebel, niedrige Frequenz
- **Claude-Review läuft interaktiv** (kein `-p`), bleibt also im Abo-Kontingent
- **Eigenvalidierung wird vermieden:** Wer den Code schreibt, reviewed ihn nicht (dokumentiertes Anti-Pattern)

### Der Monokel-Review-Schritt

Claude als viktorianischer Gutachter: setzt das Monokel auf, schaut einmal distinguiert über DeepSeeks Arbeit, gibt seinen Senf dazu, legt das Monokel wieder ab.

**Trigger:** Nach jeder großen Iteration (nicht nach jedem Patch)
**Eingabe:** Strukturiertes Code-Dossier (siehe unten)
**Ausgabe:** Bewertung pro Review-Frage + konkrete Verbesserungsvorschläge
**Kosten:** 1 interaktive Session, im Abo, kein `-p`

---

## Das Code-Dossier als universelles Kontextpaket

### Was existiert: `code_dossier.py`

Bereits gebaut und einsatzbereit. Extrahiert alle architekturentscheidenden Code-Teile in einen strukturierten Ordner:

```
code_dossier/
├── BRIEFING.md              ← Architektur-Kontext für den Reviewer
├── MANIFEST.md              ← Was liegt wo + Dateigrößen
├── REVIEW_FRAGEN.md         ← 15 konkrete Review-Fragen
├── 01_core/                 ← Kernmodule
├── 02_routers/              ← FastAPI-Router
├── ...                      ← 11 Kategorien total
└── 10_frontend_embedded/    ← Extrahierte HTML/CSS/JS
```

**Designprinzip:** "Coda hat den Code geschrieben. Coda soll ihn NICHT reviewen."

### Die Erweiterung: Dossier-Fabrik

Dasselbe Extraktions-Pattern lässt sich in zwei Richtungen erweitern:

**1. Review-Dossier (bestehend):** Ganzes Projekt → strukturiertes Paket für externen Gutachter (Claude Monokel-Review)

**2. Worker-Playbook (neu):** Einzelner Task → schlankes Paket für einen fokussierten Worker-Agenten

```python
# Konzeptionell:
class DossierFactory:
    def build_review_dossier(project) -> FullDossier:
        """Ganzes Projekt für Gutachter-Review"""
        # = das bestehende code_dossier.py
        
    def build_worker_playbook(task, relevant_rules, code_slice) -> Playbook:
        """Fokussierter Task für einen Worker-Agenten"""
        # Nur die 5-10 relevanten Regeln
        # Nur den betroffenen Code-Ausschnitt
        # Klare Akzeptanzkriterien
        # Forbidden Actions
```

**Die Verbindung:** Beide nutzen dasselbe Prinzip — relevanten Kontext extrahieren, strukturieren, dem richtigen Empfänger geben. Das Review-Dossier ist ein Playbook für den Gutachter.

---

## Orchestrator-Worker: Was bleibt, was sich ändert

### Was sich NICHT ändert (technisch validiert)

Die gesamte technische Machbarkeit aus der Gemini-Recherche bleibt gültig:

- **`--bare` Flag:** Volle Kontext-Isolation. Worker sieht NUR sein Playbook, keine globale CLAUDE.md.
- **Modell-Mischbetrieb:** Orchestrator=Opus, Worker=Sonnet/Haiku via `CLAUDE_CODE_SUBAGENT_MODEL`.
- **Worktree-Isolation:** `isolation: worktree` im Frontmatter → jeder Worker in eigenem Git-Branch.
- **.claude/agents/*.md:** Volle Agenten-Definition per Markdown (name, model, tools, disallowedTools, effort, isolation, maxTurns, permissionMode, initialPrompt).
- **Dynamische Agenten:** `--agents '{json}'` beim CLI-Start oder SDK `agents`-Dict.
- **Agent Teams:** Research Preview, DAG-basierte Task-Koordination, dateibasiertes Locking, Mailbox-System.

### Was sich ändert (wirtschaftlich erzwungen)

| Aspekt | v1 (vor Billing-Split) | v2 (nach Billing-Split) |
|---|---|---|
| **Worker-Modell** | Claude Sonnet/Opus | DeepSeek V4 Pro (primär), Claude nur für Review |
| **Dispatch-Weg** | `claude -p` / SDK | Interaktiv oder Zerberus-API |
| **Orchestrator** | Claude Opus (großes Fenster) | Zerberus RAG-Pipeline + DeepSeek |
| **Claude-Rolle** | Dauerläufer | Gutachter (selten, interaktiv, im Abo) |
| **Kosten-Modell** | Pauschale (Max-Abo) | DeepSeek-API + gelegentlich Claude interaktiv |
| **Mjölnir-Startweg** | `claude -p` (headless) | Interaktive Session ODER Zerberus-Dispatch |

---

## Mjölnir-Evolution: Weg von `-p`

### Das Problem

Mjölnir startet aktuell Claude-Code-Sessions per `claude -p` (headless). Ab 15. Juni fällt das in den teuren Kredit-Topf.

### Drei Lösungswege

**Weg A — Bildschirm-Klick-Steuerung (Brücke):**
Mjölnir simuliert echte menschliche Eingaben: Fenster öffnen, Position anklicken, Prompt einfügen. Interaktiv → im Abo. Vorteil: Sessions sind sichtbar, Fehler erkennbar. Nachteil: Fragil bei Layout-Drift. Mitigation: Screenshot-basierter Anker-Check vor jedem Klick.

**Weg B — In-Process Agent Teams (zu verifizieren):**
Agent Teams im `--teammate-mode in-process` starten alle Worker in der primären Terminal-Session. **Offene Frage:** Zählt das als interaktiv (Abo) oder programmatisch (Kredit)? Wenn interaktiv → Königsweg. Wenn nicht → Sackgasse.

**Weg C — Zerberus als Orchestrator (Endgame):**
Zerberus dispatcht an DeepSeek-Instanzen per eigener API. Kein Claude für Bulk-Arbeit. Claude nur noch als optionaler Monokel-Review. Unabhängig von Anthropics Preispolitik.

### Empfohlene Reihenfolge

1. **Sofort:** Klären ob Weg B (in-process) im Abo bleibt (eine Web-Recherche)
2. **Kurzfristig:** Weg A als Brücke bauen (Bildschirm-Klick via RustDesk)
3. **Mittelfristig:** Weg C als Endgame (Zerberus mit DeepSeek)

---

## Zerberus als modellagnostischer Orchestrator (Endgame)

### Warum Zerberus das richtige Zuhause ist

Zerberus hat bereits:
- **Intent-Routing** → neuer Intent-Typ: `ORCHESTRATE`
- **RAG-Pipeline** → zieht relevante Regeln und Lessons automatisch
- **Persona-Merge** → kann Worker-Profile pro Task konfigurieren
- **DeepSeek V4 Pro** als primäres LLM → günstig im Dauerbetrieb
- **Mistral Small 3** als Guard → unabhängig von Anthropic
- **code_dossier.py** → Dossier-Fabrik bereits gebaut

### Der ORCHESTRATE-Pfad

```
Eingabe: "Refactore den Auth-Endpoint mit Alembic-Migration"
    │
    ▼
[Intent-Router] → ORCHESTRATE erkannt
    │
    ▼
[DossierFactory] → Baut Worker-Playbook
    ├── Relevante Regeln via RAG
    ├── Code-Slice via Extraction-Map
    └── Akzeptanzkriterien
    │
    ▼
[Dispatcher] → Sendet an DeepSeek-Worker (API oder lokal)
    │
    ▼
[Konsolidierer] → Prüft Ergebnisse, merged
    │
    ▼
[Optional: Monokel-Review] → Claude interaktiv (nur bei großen Iterationen)
    │
    ▼
[Response → Nala UI] → "Patch bereit. Review empfohlen: ja/nein"
```

### Modell-Routing im Orchestrator

| Aufgabe | Modell | Grund |
|---|---|---|
| Bulk-Coding | DeepSeek V4 Pro | Günstig, stark genug für Implementierung |
| Tests schreiben | DeepSeek / Haiku | Repetitiv, braucht kein Frontier-Reasoning |
| Architektur-Review | Claude Opus (interaktiv) | Höchste Reasoning-Qualität, selten nötig |
| Security-Audit | Claude + Mistral Guard | Zwei unabhängige Prüfer |
| Doku-Updates | DeepSeek / Sonnet | Routine, kein Premium nötig |

---

## MD-Hierarchie: Vom Monolith zum Baukasten (unverändert)

### Ebene 0 — Master (Orchestrator liest)
```
CLAUDE_MASTER.md           ← Architektur-Invarianten, 50-80 Zeilen
LESSONS_KONSOLIDIERT.md    ← Gesamtes Wissen, nach Domäne getaggt
MARATHON_WORKFLOW.md       ← Task-Liste + Abhängigkeitsgraph
```

### Ebene 1 — Worker-Profile (Orchestrator wählt passende)
```
.claude/rules/
├── worker-backend.md      ← globs: **/*.py
├── worker-frontend.md     ← globs: **/*.html, **/*.css, **/*.js
├── worker-test.md         ← globs: **/tests/**
├── worker-infra.md        ← globs: **/*.yaml, **/*.toml, **/alembic/**
└── worker-docs.md         ← globs: **/*.md
```

### Ebene 2 — Playbooks (DossierFactory generiert on-the-fly)
```
_playbooks/
├── PLAYBOOK_aktiv_001.md  ← Vom Orchestrator/DossierFactory erstellt
├── PLAYBOOK_aktiv_002.md  ← Lebt nur während der Task-Ausführung
└── REVIEW_DOSSIER.md      ← Für Claude Monokel-Review
```

**Modellagnostisch:** Die MD-Hierarchie funktioniert unabhängig vom Worker-Modell. DeepSeek, Claude, Gemini — alle lesen Markdown.

---

## Technische Schlüssel-Findings (Gemini-Recherche)

### Claude Code Subagenten — Bestätigte Mechanismen

| Mechanismus | CLI-Flag / Config | Funktion |
|---|---|---|
| Volle Isolation | `--bare` | Deaktiviert CLAUDE.md, Hooks, Skills, Projektconfig |
| Eigenes Arbeitsverzeichnis | `--cwd <path>` | Worker in anderem Verzeichnis |
| Custom System-Prompt | `--system-prompt-file` | Eigener Prompt, aber CLAUDE.md wird trotzdem geladen |
| Worktree-Isolation | `isolation: worktree` | Eigener Git-Branch + Verzeichnis pro Worker |
| Modell-Routing | `model: sonnet` im Frontmatter | Worker nutzt anderes Modell als Orchestrator |
| Tool-Restriktion | `tools: Read, Grep, Glob` | Worker auf Lese-Tools beschränkt |
| Turn-Limit | `maxTurns: 25` | Verhindert Endlosschleifen |
| JSON-Injektion | `--agents '{...}'` | Dynamische Agenten-Definition beim CLI-Start |
| Headless + JSON-Output | `-p --output-format json` | Strukturiertes Ergebnis + Kosten + Token |

### Agent Teams — Status Research Preview

- Aktivierung: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
- Mindest-CLI: v2.1.32
- Koordination: Dateibasiert unter `~/.claude/teams/` und `~/.claude/tasks/`
- DAG-basierte Ablaufsteuerung mit dateibasiertem Locking
- Delegate Mode: Team-Lead nur koordinierend, kein Schreibzugriff
- **Einschränkung:** `skills` und `mcpServers` im Frontmatter werden bei Teammates ignoriert
- **tmux-Modus nicht auf Windows** → nur `in-process` verfügbar

### Worktree-Isolation — Dokumentierte Fallstricke

| Problem | Lösung |
|---|---|
| .env fehlt im Worktree | `.worktreeinclude`-Datei (inverse .gitignore) |
| DB-Kollisionen | WorktreeCreate-Hook erstellt isolierte DB |
| Fehlende Dependencies | Setup-Skript im Hook (npm install etc.) |
| Merge-Konflikte | Hauptagent merged sequenziell + Testläufe |

### Kein nativer Webhook

Benachrichtigung bei Subagent-Abschluss nur über:
- Prozess-Exit-Monitoring (bei `-p`)
- SessionEnd-Hook in `.claude/settings.json`
- SDK-Callback-Hooks

---

## Kontext-Einsparung: Die Zahlen (aktualisiert)

### Monolith (bisheriger Ansatz)
```
Gesamter Kontext pro Coda-Session:     ~325.000 Token
Verbleibend für Arbeit:                ~675.000 Token (67%)
Kosten: Im Abo (Pauschale)
```

### Orchestrator + Worker (v1 — vor Billing-Split)
```
Orchestrator:                          ~23.000 Token
Pro Worker:                            ~13.000 Token (93% frei)
Kosten: Im Abo (Pauschale) — NICHT MEHR GÜLTIG für -p/SDK
```

### Hybrid-Modell (v2 — nach Billing-Split)
```
DeepSeek-Worker: Kontext-Kosten nach API-Preis (günstig)
Claude Monokel-Review: 1 interaktive Session (im Abo)
Code-Dossier als Kontextpaket: ~50.000-100.000 Token (strukturiert)
Effektive Kosten: DeepSeek-API + 0 EUR Claude-Aufpreis
```

---

## Migrations-Pfad (aktualisiert)

### Stufe 1 — MD-Split + Dossier-Fabrik (2-3 Coda-Sessions)
- CLAUDE.md-Monolith aufbrechen → CLAUDE_MASTER.md + Worker-Profile
- `.claude/rules/` mit `globs:`-Syntax einrichten
- `code_dossier.py` zu generischer DossierFactory erweitern
- Playbook-Template erstellen und testen
- **Ergebnis:** Schlankere Kontextfenster, Dossier-Fabrik einsatzbereit

### Stufe 2 — Mjölnir weg von `-p` (1-2 Sessions)
- Klären ob in-process Agent Teams im Abo bleiben
- Bildschirm-Klick-Steuerung als Brücke implementieren
- Mjölnir-Backend auf interaktiven Startweg umbauen
- **Ergebnis:** Mjölnir funktioniert nach dem 15. Juni ohne Extrakosten

### Stufe 3 — DeepSeek-Integration in Zerberus (3-5 Sessions)
- ORCHESTRATE-Intent in Zerberus-Pipeline
- DossierFactory als Worker-Playbook-Generator
- DeepSeek als primäres Worker-Modell
- Monokel-Review als optionaler Schritt
- **Ergebnis:** Modellagnostische Orchestrierung

### Stufe 4 — Claude als Premium-Modul (ongoing)
- Monokel-Review-Workflow verfeinern
- Review-Fragen pro Projekt kalibrieren
- Claude nur noch für: Architektur-Review, Security-Audit, strategische Fragen
- **Ergebnis:** Unabhängigkeit von Anthropics Preispolitik

---

## Einordnung in die Roadmap

| Phase | Was | Status |
|---|---|---|
| 1 | Konsolidierung | ✅ |
| 2 | Bootstrap-Fabrik | 🟡 aktiv |
| 3 | Gist-Migration | 🟢 live |
| **4.5** | **Orchestrator-Layer (Hybrid)** | **⚡ Konzept v2 steht** |
| 5 | Selbststeuerung | 💭 |
| 6 | Endgame | 🌟 |

---

## Offene Punkte (zu klären)

1. **In-Process Agent Teams Billing:** Zählt `--teammate-mode in-process` als interaktiv (Abo) oder programmatisch (Kredit)? → Entscheidend für Weg B.
2. **DeepSeek-Reasoning-Qualität:** Kann DeepSeek V4 Pro die Orchestrator-Rolle mit derselben Zuverlässigkeit wie Opus tragen? → Praxistest nötig.
3. **Kredit beanspruchen:** Anthropic schickt um den 8. Juni eine Mail. Aktiv klicken vor dem 15. Juni, sonst verfällt der Kredit.
4. **Modell-ID-Retirement:** `claude-sonnet-4-20250514` und `claude-opus-4-20250514` werden am 15. Juni abgeschaltet. Aliase ohne Datum-Suffix nutzen.

---

## Zusammenfassung in einem Satz

*Der Workflow bleibt — das Modell wechselt: DeepSeek baut, Claude prüft, Zerberus orchestriert, und der Mensch trinkt Kaffee.*

— Marathon Workflow v3, Konzept v2, 23. Mai 2026
