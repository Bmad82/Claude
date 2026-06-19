<!-- DECISIONS_PENDING | offene Architektur-Fragen, blockierte Aufträge, dokumentierte Konflikte -->

# DECISIONS_PENDING.md | Bibel-Format
Offene Entscheidungen + Konflikte für `Claude/`-Meta-Layer | jede Frage mit Datum+Hintergrund+Optionen

## Offene Entscheidungen (Pending)

### 2026-05-17 | Zerberus-Lessons-Konsolidierung in eigene Session ausgelagert
Frage|Zerberus-Lessons gegen GLOBAL_LESSONS abgleichen — welche der ~1017 Zeilen in `lessons_ZERBERUS.md` sind bereits in `GLOBAL_LESSONS.md` promoviert und sollten dort auf Verweis reduziert werden?
Hintergrund|Schritt 08 aus `aufraeumarbeiten-post-catch` adressiert das. Quick-Scan zeigt mind. 3 klare Dubletten in den ersten 100 Zeilen: „OBERSTES GEBOT (P-umzug, 2026-05-16)", „Multi-Session-Status-Header (B-mjolnir-multisession)", „mjolnir.md-Round-Trip-Pflicht (B-mjolnir-fix/B-mjolnir-fix-2)". Master liegt in `C:\Users\chris\Python\Zerberus\lessons_ZERBERUS.md`, Sync-Kopie in `C:\Users\chris\Python\Claude\lessons\zerberus_lessons.md` (1017 Zeilen). Sync via `sync_repos.ps1` aus Zerberus-Repo. Bearbeitung bräuchte Cross-Repo-Commits + Selbsttest A-D + Wachsamkeit gegen Sync-Drift.
Optionen|A) Eigener FEATURE_REQUEST `lessons-konsolidierung` mit Phase A-D Selbsttest (vollständig) | B) Inline-Quick-Win nur die 3 offensichtlichen Dubletten ersetzen, ohne kompletten Scan | C) Master in Zerberus-Repo unverändert lassen, nur Sync-Kopie in Claude/lessons als „kanonischer Snapshot bei Repo-Move" behandeln
Blockiert|nichts unmittelbar — die Dubletten sind nicht schädlich, nur redundant. Eskalation wenn das Volumen weiter wächst.
Eingetragen|2026-05-17 (aufraeumarbeiten-post-catch verschoben)

### 2026-06-19 | Deferred aus ordner-cleanup: Design/Intake-Ablage + LESSONS_KONSOLIDIERT-Extraktion
Frage|(a) Sollen `DESIGN.md`, `DESIGN_KINTSUGI.md`, `Projektanfrage.html` in eigene Ordner `design/` bzw. `intake/`? (b) Sollen die unique alten Lessons aus `_archive/LESSONS_KONSOLIDIERT.md` (PWA, CSS-Industriepanel, Claude-Design-Workflow) nach `lessons/` extrahiert werden, bevor die Datei rein archiviert bleibt?
Hintergrund|ordner-cleanup hat den unstrittigen Teil ausgeführt. (a) wurde NICHT gemacht, weil `DESIGN.md` per HARTEM Absolutpfad in Templates verdrahtet ist (DESIGN_PROJEKT_TEMPLATE u.a.) — verschieben bräuchte ein Template-Referenz-Update, und die drei Design/Intake-Files bilden eine Gruppe, die man zusammen bewegen sollte. (b) Extraktion einzelner Lessons ist Inhalts-Arbeit mit Verlust-Risiko → nicht im Cleanup geraten. LESSONS_KONSOLIDIERT liegt jetzt vollständig in `_archive/` (nichts verloren).
Optionen|A) So lassen (Design-Files am Root, KONSOLIDIERT nur archiviert) | B) `design/` + `intake/` anlegen und alle DESIGN.md-Referenzen in Templates nachziehen | C) Eigener Mini-FR `lessons-konsolidierung` der KONSOLIDIERT + Zerberus-Lessons gemeinsam gegen GLOBAL_LESSONS abgleicht
Blockiert|nichts — rein kosmetisch/optional.
Eingetragen|2026-06-19 (ordner-cleanup)

## Getroffene Entscheidungen

### 2026-06-19 | Supervisor-Aufbau: Handover→JSON, Projekt-Schaltplan, Human-Tests (FR supervisor-aufbau)
Entscheidung|Sechs Grenzentscheidungen, die der FR nicht explizit vorgab, hier dokumentiert (alle reversibel):
1. **Begriff `mjolnir`/`Mjölnir` zweideutig — nur das DOKUMENT umbenannt.** Es gibt zwei Bedeutungen: (a) das Übergabe-DOKUMENT `mjolnir.md`/`mjolnir_TEMPLATE.md` → umbenannt zu `HANDOVER.json`/`HANDOVER_TEMPLATE.json` (FR-Ziel); (b) die Orchestrator-SOFTWARE „Mjölnir/Hammerfall" (der `claude -p`-Launcher in `concepts/ORCHESTRATOR_KONZEPT_v2.md`, das Cockpit in `DESIGN_KINTSUGI.md` 9.4) → NAME BEHALTEN, ist nicht das Übergabedokument. Grenze: bare „Mjölnir" (Software) blieb, nur Dokument-Strings (`*.md`, `-Round-Trip`, `-Konvention`) wurden ersetzt.
2. **Altes Bibel-`templates/HANDOVER_TEMPLATE.md` (Prosa-Detail-Layer) abgelöst + archiviert** → `_archive/HANDOVER_TEMPLATE_bibel-detail.md`. Im neuen Modell wandert sein Dauerhaft-Inhalt (Stände, Bugs, Risiken) in `SCHALTPLAN_PROJEKT.json`, sein heißer Kontext in `HANDOVER.json`. Es gibt KEIN Prosa-Detail-Handover mehr. Alle Lese-/Schreib-Referenzen auf `HANDOVER_{PROJEKT}.md` → `SCHALTPLAN_PROJEKT.json` umgebogen.
3. **Gist-Briefing-Set neu verdrahtet** auf `STATUS, HANDOVER, SCHALTPLAN, REPO_INDEX, LESSONS` (alt: HANDOVER-Bibel + MJOLNIR getrennt). Mapping: altes HANDOVER (Bibel/Dauerhaft) → SCHALTPLAN; altes MJOLNIR (Status) → HANDOVER. Nötig, damit der Supervisor den Schaltplan per Gist fetchen kann (er liest nur Gists, keine Raw-Links).
4. **`schaltplan/fabrik_meta_workflow.json/.html` unverändert gelassen** (FR-geschützte DNA-Vorlage). Es nennt weiter „Mjölnir" und trägt den Bruch `fr.mjolnir-handover`. Das dort nachzuziehen (Fracture schließen, Term aktualisieren) ist ein SEPARATER Folge-Auftrag — bewusst nicht in diesem FR.
5. **Lessons/Historie historisch belassen** (`GLOBAL_LESSONS.md`, `lessons/`, `_erledigt/`, `_archive/`): dated Lesson-Einträge nennen weiter `mjolnir.md` (nicht rückwirkend fälschen). Stattdessen EIN Vorwärts-Hinweis oben in `GLOBAL_LESSONS.md` (mjolnir→HANDOVER).
Begründung|FR-Regel „Bei Konflikten/Unklarheiten: nicht raten, DECISIONS_PENDING.md + Handover-Verweis". Alle fünf folgen direkt aus dem im FR definierten Modell (Schaltplan=Gedächtnis, Handover=Staffelstab) und sind reversibel (Archiv statt Löschen, geschützte Quelle unangetastet).
Alternativen|A) Auch die Orchestrator-Software umbenennen — falsch, ist nicht das Übergabedokument | B) Bibel-Handover behalten — widerspricht der Gedächtnis/Staffelstab-Trennung, erzeugt dritte Wahrheit | C) Gist-Set unverändert lassen — dann fehlt dem Supervisor der Schaltplan-Zugang
Offene Folge-Aufgaben (NICHT in diesem FR erledigt)|
- **Hook-Scripts im Zerberus-Repo** (`scripts/lessons_lookup_auto.py`, `scripts/session_end_check.py`) prüfen noch auf `mjolnir.md`/`HANDOVER` — müssen auf `HANDOVER.json` (+ `SCHALTPLAN_PROJEKT.json`) umgestellt werden, sonst erkennt der SessionEnd-Hook den neuen Handover nicht. Cross-Repo, eigener Auftrag.
- **`fabrik_meta_workflow.json`** Fracture `fr.mjolnir-handover` schließen + Term „Mjölnir"→„Handover" im Meta-Workflow nachziehen (separater Auftrag, da Quelle FR-geschützt war).
Patch-Referenz|supervisor-aufbau (2026-06-19)

### 2026-06-19 | Ordner-Cleanup ausgeführt (Mapping aus INVENTORY)
Entscheidung|Zielstruktur Templates/ Lessons/ Workflow/ + neue `schaltplan/`-Ablage hergestellt. Neu: `schaltplan/` (fabrik_meta_workflow.json+html), `_archive/` (abgelöste/veraltete Files). `_drafts_gist/` aufgelöst. Verschoben: 3 Root-FR-Archive → `_erledigt/`, Einmal-Reports (REPO_INVENTORY/SUPERVISOR_BRIEFING/GIT_DIAGNOSE) + Gist-Drafts + LESSONS_KONSOLIDIERT + GLOBAL_LESSONS_KONTEXT → `_archive/`, WORKFLOW_SUMMARY → `workflow/`, ORCHESTRATOR_KONZEPT_v2 + TOKEN_OPT_RULES → `concepts/`, uebergabe_template_v1_0 → `templates/`. `workflow/__pycache__/*.pyc` gelöscht (regenerierbar, gitignored).
Begründung|Root war auf ~28 lose Files gewachsen (Unübersichtlichkeit). Mapping kam aus der Phase-1-`INVENTORY.md`. Reversibilität gewahrt: eigener Branch `cleanup/ordner-cleanup` + Baseline-Commit als Restore-Punkt; `git mv` statt rm; Löschen nur beim regenerierbaren `.pyc`.
Alternativen|A) Alles am Root lassen — Status quo, unübersichtlich | B) Hart löschen statt archivieren — irreversibel, verwirft Audit-Historie
Konsequenz|Absolutpfad-gepinnte Files (GLOBAL_LESSONS, SUPERVISOR_KODEX, DECISIONS_PENDING, PROJECT_BOOTSTRAP_README, GIST_LINK, DESIGN) bewusst am Root belassen — kein Template-Pfad gebrochen. `FEATURE_REQUEST_CLAUDE_ERLEDIGT.md` (Root, Auftrag mw-v2a) kollidierte beim Move mit der gleichnamigen Datei in `_erledigt/` (Auftrag faulheits-catch-integration) — kollisionssicher umbenannt zu `FEATURE_REQUEST_mw-v2a-kontextentlastung_ERLEDIGT.md`. REPO_INDEX + README + GLOBAL_LESSONS aktualisiert. `FEATURE_REQUEST_supervisor-aufbau.md` (separater, noch nicht gestarteter Auftrag) bewusst untracked liegen gelassen.
Patch-Referenz|ordner-cleanup (2026-06-19)

### 2026-06-19 | GLOBAL_LESSONS_KONTEXT in GLOBAL_LESSONS zurückgemergt, dann archiviert
Entscheidung|Die fünf nur im KONTEXT-Zwilling vorhandenen „Anlass/Lesson generalisierbar"-Prosablöcke (Progressive Disclosure, Lessons-Retrieval, Stand-Anker, Session-End-Mechanik, Session-Auffüll-Regel) in `GLOBAL_LESSONS.md` zurückgeführt. KONTEXT dann nach `_archive/` verschoben.
Begründung|Zwei konkurrierende „globale Lessons"-Wahrheiten sind das Anti-Pattern, das der Workflow killt. KONTEXT war älter (fehlende 5 neueste Lessons), aber prosareicher. Merge holt die Reasoning-Prosa zurück, ohne die neueren Lessons zu verlieren.
Alternativen|A) KONTEXT hart löschen — Prosa-Verlust | B) Beide behalten — Drift-Risiko bleibt
Konsequenz|Verifiziert per `comm -23` der `##`-Header: keine KONTEXT-Sektion fehlt in GLOBAL_LESSONS (21 vs 16 Sektionen, Anlass-Blöcke 10→15). KONTEXT bleibt als historischer Beleg in `_archive/`.
Patch-Referenz|ordner-cleanup (2026-06-19)

### 2026-05-21 | v2b-Paket 1 Hooks bleiben opt-in (settings.json NICHT committed)
Entscheidung|Die drei Hook-Scripts (`scripts/lessons_lookup_auto.py`, `scripts/validate_edit.py`, `scripts/session_end_check.py`) sind im Zerberus-Repo committed und verifiziert. Die Verdrahtung in `.claude/settings.json` wird NICHT committed. Chris aktiviert sie nach Bedarf in `.claude/settings.local.json` (Variante B aus `scripts/HOOK_SETUP.md`).
Begründung|Schreibversuch auf `.claude/settings.json` wurde in der v2b-Session abgelehnt. Konsistent mit der Vorab-Direktive in `HOOK_SETUP.md` ("opt-in, weil Hooks Befehle automatisch ausfuehren"). Variante B ist kein Funktionsverlust — alle Hooks feuern auch bei lokaler Verdrahtung.
Alternativen|A) settings.json doch committen — wäre Verstoß gegen Permission-Entscheidung | C) Hooks komplett zurueckbauen — Funktionsverlust
Konsequenz|Akzeptanzkriterien Paket 1 (settings.json enthält Hooks, SessionStart injiziert Lessons, Edit auf CLAUDE_GLOBAL.md blockiert, SessionEnd meldet Fehler) sind auf Skript-Ebene erfuellt + per CLI-Smoke-Test verifiziert. Die finale "Mechanik unumgehbar"-Eigenschaft tritt erst nach Chris-seitiger Aktivierung der Variante B ein. Sub-Aufgabe Akzeptanzkriterium 1 (settings.json enthält Hooks) ist daher als "READY, Aktivierung opt-in" zu lesen.
Patch-Referenz|mw-v2b-durchsetzung (2026-05-21)

### 2026-05-17 | Quelle Try_Faulheits_catch.md als Konzept-Ursprung in concepts/ verankert
Entscheidung|Rekonstruierte Fassung als `concepts/Try_Faulheits_catch.md` mit Status-Header „Historisches Dokument. Operative Version siehe GLOBAL_LESSONS.md".
Begründung|Original existiert nur im Anthropic-Chat-Projekt-Speicher, nicht im Git. Damit die Konzept-Wurzel dauerhaft auf der Platte verankert ist (nicht nur in flüchtigen Chat-Sessions), wird die rekonstruierte Liste der 6 Catches + Selbsttest-Pattern + Bibel-Cheat-Sheet als kanonische Konzept-Datei archiviert.
Alternativen|A) Datei nicht anlegen — Inhalte sind ja in GLOBAL_LESSONS migriert | B) Chris bitten Original nachzureichen — bisher keine Reaktion
Konsequenz|Wenn Chris das Original-Volltext nachliefert, kann diese Datei mit dem Original abgeglichen werden. Bis dahin ist `concepts/Try_Faulheits_catch.md` die kanonische rekonstruierte Fassung.
Patch-Referenz|aufraeumarbeiten-post-catch (Schritt 04)

### 2026-05-17 | Dual-Templates-Folder konsolidiert zu templates/
Entscheidung|Option C+B-Hybrid: alte `templates/` gelöscht, `_templates/` umbenannt zu `templates/`. Vorher 6 alte Templates (MARATHON_WORKFLOW, HANDOVER, DECISIONS, DESIGN, ROADMAP, lessons) auf neuen Bibel-Format-Standard aktualisiert + nach _templates/ migriert (mit Verweis auf Regel 0/KODEX/GLOBAL_LESSONS wo passend). 2 alte (CLAUDE_TEMPLATE, SUPERVISOR_TEMPLATE) durch ihre _PROJEKT-Pendants ersetzt — als obsolet markiert.
Begründung|Parallele Existenz war Provisorium der vorigen Session. Konsolidierter Stand: 10 Files in `templates/`, alle mit konsistenten Headern + Regel-0-Verweisen. Pfade in PROJECT_BOOTSTRAP_README.md, SUPERVISOR_KODEX.md, CLAUDE_PROJEKT_TEMPLATE.md, FEATURE_REQUEST_TEMPLATE.md, SUPERVISOR_PROJEKT_TEMPLATE.md, GLOBAL_LESSONS.md angepasst.
Alternativen|A) Beide Ordner behalten — verwirrender Doppelpfad | B) Nur Migration ohne Umbenennung — `_templates/` als endgültiger Name war hässlich (Unterstrich war Provisorium)
Konsequenz|Selbsttest A-D durchgelaufen, alle Phasen grün. Sub-Agent erkennt korrekten Pfad, listet alle 10 Templates. Historische Verweise in `FEATURE_REQUEST_CLAUDE_ERLEDIGT.md` und im aktuellen `FEATURE_REQUEST_CLAUDE.md` (vor Rename) bleiben unangetastet — Geschichts-Logs nicht verfälschen.
Patch-Referenz|aufraeumarbeiten-post-catch (Schritt 03)

### 2026-05-17 | Naming-Konvention FEATURE_REQUEST_{kurzname}.md durchgesetzt
Entscheidung|FEATURE_REQUEST-Dateien heißen `FEATURE_REQUEST_{kurzname}.md` (kebab-case aus Frontmatter), niemals `FEATURE_REQUEST_{PROJEKT}.md`. Bei Lifecycle-Übergang bleibt der Kurzname-Teil erhalten (`*_ERLEDIGT.md`, `*_QUEUED.md`).
Begründung|Anlass: die vorige `faulheits-catch-integration`-Session legte ihre Auftrags-Datei als `FEATURE_REQUEST_CLAUDE.md` ab. Bei mehreren parallelen Aufträgen in einem Projekt (QUEUED-Pattern) wäre die Datei nicht eindeutig identifizierbar.
Alternativen|A) Konvention nicht festklopfen — nächste Session macht denselben Fehler | B) Projektname als Filename behalten — bricht QUEUED-Pattern
Konsequenz|Lesson in GLOBAL_LESSONS.md verankert (eigene Sektion „Naming-Konvention für FEATURE_REQUEST-Dateien"). Backstop-Kommentar im `templates/FEATURE_REQUEST_TEMPLATE.md`. Bestehende `FEATURE_REQUEST_CLAUDE_ERLEDIGT.md` bleibt unangetastet (historisch). Aktueller `FEATURE_REQUEST_CLAUDE.md` wird bei STATUS=FERTIG zu `_ERLEDIGT.md` umbenannt — Filename bleibt mit alter Konvention erhalten weil Historie. Künftige Files folgen der neuen Konvention.
Patch-Referenz|aufraeumarbeiten-post-catch (Schritt 02)

### 2026-05-17 | DESIGN.md als UI-Layer abgegrenzt (nicht Workflow-Layer)
Entscheidung|DESIGN.md bekommt eine „Geltungsbereich"-Sektion direkt nach der Einleitung, die klarstellt dass die Datei den UI-/Look-and-Feel-Layer dokumentiert. Marathon-Workflow-Themen (Drei-Rollen-Modell, File-Hierarchie, Bibel-Format, Mjölnir-Round-Trip, Faulheits-Catches, Bootstrap-Prinzip) sind explizit in README/GLOBAL_LESSONS/SUPERVISOR_KODEX/PROJECT_BOOTSTRAP_README dokumentiert, nicht hier.
Begründung|Auftrag erwartete Marathon-Workflow-Sektionen in DESIGN.md (Schritt 07). Existierende DESIGN.md ist aber klar UI-Design-Referenz mit 17 Sektionen zu Farben/Komponenten/Mobile. Themen-Mix in einer Datei hätte UI-Fokus + Workflow-Architektur kontaminiert.
Alternativen|A) Marathon-Workflow-Sektionen direkt in DESIGN.md einbauen — Themen-Mix, schlecht für Update-Zyklen | B) Eigene MARATHON_DESIGN.md anlegen — würde README.md+GLOBAL_LESSONS.md-Doppelung erzeugen
Konsequenz|Update-Datum 2026-05-17 in Änderungshistorie ergänzt. Tabelle in Geltungsbereich-Sektion verweist auf die kanonischen Quellen pro Aspekt. UI-Werte unverändert.
Patch-Referenz|aufraeumarbeiten-post-catch (Schritt 07)

### 2026-05-17 | _drafts_gist/ Vorbereitungsordner für Phase 3 angelegt
Entscheidung|Neuer Ordner `_drafts_gist/` mit `INDEX_GIST_DRAFT.md` + `ZERBERUS_GIST_DRAFT.md`. Beide Files sind reine Konzept-Entwürfe, werden NICHT zu echten Gists in dieser Session.
Begründung|Phase 3 der Roadmap (Gist-Migration) soll bei Aktivierung keine Konzept-Arbeit mehr brauchen, nur noch Migration und Push.
Alternativen|A) Erst bei Phase-3-Start anlegen — verschleppt Konzept-Klärung | B) Direkt echte Gists anlegen — verfrüht, Format könnte noch driften
Konsequenz|Bei Phase-3-Aktivierung: `gh gist create` der beiden Entwurfs-Files + URL in Supervisor-Memories + Repo-Verweis ergänzen.
Patch-Referenz|aufraeumarbeiten-post-catch (Schritt 09)

### 2026-05-17 | Auftrag aufraeumarbeiten-post-catch auf main statt im Worktree
Entscheidung|Direktes Arbeiten auf `main` ohne Worktree-Branch
Begründung|FEATURE_REQUEST sagt explizit „Branch: direkt auf `main` (kein Worktree für Strukturarbeit nötig)."
Alternativen|Worktree-Branch wäre Overkill für Dateierstellung/Umbenennung ohne Code-Risiko
Konsequenz|Mehrere thematische Commits direkt auf main, Push danach
Patch-Referenz|aufraeumarbeiten-post-catch (2026-05-17)

### 2026-05-17 | Auftrag faulheits-catch-integration auf main statt im Worktree
Entscheidung|Direktes Arbeiten auf `main` ohne Worktree-Branch
Begründung|FEATURE_REQUEST Schritt 07 sagt explizit: „Branch: direkt auf `main` (kein Worktree für Strukturarbeit nötig)."
Alternativen|Worktree-Branch wäre Overkill für reine Dateierstellung ohne Code-Risiko
Konsequenz|4 thematische Commits direkt auf main, Push danach
Patch-Referenz|faulheits-catch-integration (2026-05-17)
