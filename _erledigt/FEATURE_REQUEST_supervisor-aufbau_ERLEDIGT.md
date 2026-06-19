<!-- TEMPLATE | Dateiname: FEATURE_REQUEST_supervisor-aufbau.md | Kopie ins Projekt-Root | Coda arbeitet diese Datei beim Session-Start als Priorität ab -->

# FEATURE_REQUEST: Supervisor-Aufbau — Handover-JSON, Projekt-Schaltplan, Human-Test-Liste, Kodex

**Datum:** 2026-06-19
**Auftraggeber:** Chris (direkt, über Supervisor-Chat)
**Empfänger:** Coda
**Kurzname:** supervisor-aufbau
**Erwartete Dauer:** 2–3 Sessions

---

## Kontext

Wir richten den Projekt-Overseer ("Supervisor") sauber ein, damit er ab dem nächsten Bootstrap von Anfang an mitläuft. Der Supervisor sieht KEINEN Code — er orientiert sich ausschließlich an strukturierten Steuer-Files (Schaltplan + Handover) und routet darüber die Agenten. Drei Bausteine fehlen bzw. liegen im falschen Format vor: (1) das Übergabedokument heißt kryptisch `mjolnir` und ist Prosa statt Maschinen-JSON, (2) es gibt keinen projektspezifischen Schaltplan (nur den Fabrik-Meta-Workflow, das ist die Prozess-Sicht, NICHT die Modul-/Abhängigkeitskarte eines Projekts), (3) menschliche Tests werden nirgends strukturiert gesammelt.

Quelle Schaltplan-DNA (Vorlage, NICHT verschieben/ändern): `fabrik_meta_workflow.json`
Quelle Handover-Ist-Format: `templates/mjolnir_TEMPLATE.md` + reales Beispiel im Repo (ASR-Switch-Lauf).

---

## Akzeptanzkriterien (TL;DR)

- [ ] Begriff `mjolnir`/`Mjölnir` projektweit ersetzt durch `Handover` (Templates, Kodex, FR-Template, Doku) — kein Vorkommen mehr außer in Auftragshistorie/Lessons (dort historisch belassen)
- [ ] `HANDOVER.json`-Schema existiert: überschriebener STATUS-Kopf + append-only Historie, JSON
- [ ] `templates/HANDOVER_TEMPLATE.json` + Render-`HANDOVER.html` (HTML liest JSON, mischt nicht)
- [ ] `templates/SCHALTPLAN_PROJEKT_TEMPLATE.json` existiert: projektspezifisch, leeres Skelett, gleiche DNA wie Meta-Workflow (status IST/TEIL/PLAN/—, nodes, edges, fractures, ref-Belegpflicht, pflege_protokoll) + Render-HTML
- [ ] `templates/HUMAN_TESTS_TEMPLATE.json` + Render-`HUMAN_TESTS.html`: Kategorien/Reiter → Items mit Abhak-Status, HTML-auslesbar
- [ ] Kodex/CLAUDE.md trägt Doku-Pflicht: Supervisor pflegt Schaltplan am Fenster-Ende, liest ihn zum Routen, Dauerhaftes wandert in den Schaltplan (nicht in den Handover)
- [ ] Bootstrap zieht Schaltplan + Handover + Test-Liste als physische Files ins neue Projekt
- [ ] Selbsttest A–D durchgelaufen
- [ ] Commit + Push erfolgt, `$LASTEXITCODE = 0` verifiziert
- [ ] `HANDOVER.json` (neues Format) mit STATUS-Kopf geschrieben

---

## Schritt 01 — Handover: Umbenennung + Format-Umbau auf JSON

**Teil A — Umbenennung.** Ersetze projektweit `mjolnir`/`Mjölnir` durch `Handover`, in Datei-Inhalten UND Dateinamen (`mjolnir_TEMPLATE.md` → `HANDOVER_TEMPLATE.json`, `mjolnir.md`-Referenzen → `HANDOVER.json`). Suche alle Vorkommen (Templates, SUPERVISOR_KODEX.md, FEATURE_REQUEST-Template, Doku-Files). In Auftragshistorie/Lessons den Begriff historisch belassen (nicht rückwirkend fälschen), aber neue Vorkommen = `Handover`.

**Teil B — Format.** Baue `HANDOVER.json` mit zwei Zonen:
- `status` (Objekt, wird bei jedem Lauf ÜBERSCHRIEBEN): Felder aus dem Ist-Template ableiten — `status` (FERTIG|IN_ARBEIT|BLOCKIERT), `auftrag`, `fortschritt`, `naechste_session`, `warnung`, `chris_physisch` (Liste, "— nichts —" wenn leer, Sektion nie löschen).
- `historie` (Array, APPEND-only): pro Lauf ein Eintrag `{datum, auftrag, ergebnis_kurz}`. Ersetzt NICHT `_ERLEDIGT.md` (FR-Lifecycle-Log bleibt), sammelt nur den Supervisor-zu-Supervisor-Faden.

Single-Slot-Logik des Kopfes bleibt, Historie akkumuliert. LIFECYCLE-Notiz aus dem Ist-Template (FERTIG/IN_ARBEIT/BLOCKIERT-Verhalten) sinngemäß ins neue Schema übernehmen.

**Done:** `HANDOVER_TEMPLATE.json` + `HANDOVER.html` existieren, altes `mjolnir`-Vokabular ist weg, ein Beispiel-Handover validiert gegen das Schema.

---

## Schritt 02 — Projekt-Schaltplan-Template

Lege `templates/SCHALTPLAN_PROJEKT_TEMPLATE.json` an. Nimm `fabrik_meta_workflow.json` als Struktur-DNA, aber für die PROJEKT-Sicht statt der Prozess-Sicht:
- `nodes` = Module/Komponenten des Projekts (z. B. Modellwahl, Frontend, Routing, GPU-Lifecycle), nicht Pipeline-Phasen.
- `edges` = Abhängigkeiten/Verbindungen zwischen Modulen.
- Beibehalten: `status` (IST/TEIL/PLAN/—, gestrichen bleibt sichtbar), `ref`-Belegpflicht (Status nur belegbar, sonst nicht raten), `fractures`, `legend`, `pflege_protokoll`.
- Als **leeres Skelett** mit 1–2 Beispiel-Nodes als Muster — der Supervisor füllt es pro Projekt.

Plus Render-`SCHALTPLAN_PROJEKT.html` analog zur Meta-Workflow-HTML: HTML liest die JSON, ist reine Anzeige, mischt kein Format.

**Done:** Template + HTML existieren, JSON validiert, klar als Projekt-Karte (nicht Prozess-Karte) gekennzeichnet.

---

## Schritt 03 — Human-Test-Liste

Lege `templates/HUMAN_TESTS_TEMPLATE.json` an: strukturierte Sammlung der Tests, die NUR ein Mensch ausführen kann (echte Geräte, Mikrofon, UI-Klicks, VRAM-Messung etc.).
- Struktur: `kategorien` (= Reiter) → je Kategorie `items` mit `{id, beschreibung, status: offen|getestet|fehlgeschlagen, datum, notiz}`.
- Bewusst HTML-auslesbar halten (flache, klare Keys), damit eine Render-HTML Reiter + Abhakboxen daraus bauen kann.
- Wird laufend gepflegt (Items kommen dazu, werden abgehakt) — nichts darf untergehen.

Plus Render-`HUMAN_TESTS.html`: Reiter pro Kategorie, Abhak-Darstellung, liest die JSON.

**Done:** Template + HTML existieren, ein Beispiel-Item pro Status demonstriert die Darstellung.

---

## Schritt 04 — Kodex / CLAUDE.md: Doku-Pflicht & Routing

Trage in SUPERVISOR_KODEX.md (und CLAUDE.md wo passend) als harte Regeln ein:
- Supervisor liest den Projekt-Schaltplan VOR dem Routen und nutzt `fractures`/Status, um zu entscheiden, wohin ein Agent geschickt wird.
- Supervisor pflegt den Schaltplan am Fenster-Ende (vor dem Handover): neuer Stand rein, gestrichenes sichtbar lassen, SSOT = JSON.
- **Trennung Gedächtnis vs. Staffelstab:** Dauerhaftes (Status, verworfene Ansätze, Bruchstellen) wandert in den SCHALTPLAN. Der HANDOVER trägt nur heißen In-Flight-Kontext. Nachfolger liest: Schaltplan (volle Wahrheit) + letzte 1–2 Handover-Einträge.
- `pflege_protokoll` aus den JSONs hier im Kodex spiegeln, damit es nicht nur am Dateiende der JSON steht.

**Done:** Regeln stehen im Kodex, Begriff `Handover` durchgängig.

---

## Schritt 05 — Bootstrap-Integration

Sorge dafür, dass der Bootstrap (Instanz-Datei-Anlage) die drei neuen Files als physische Kopien ins neue Projekt zieht: leerer Projekt-Schaltplan, leere Human-Test-Liste, leeres Handover. Neue Projekte starten damit ab Tag 1.

**Done:** Bootstrap-Logik/Template referenziert die drei neuen Templates; ein Trockenlauf legt sie korrekt im Zielordner an.

---

## Schritt 06 — Selbsttest (Phase A–D, PFLICHT)

### Phase A — Setup
Lege ein Wegwerf-Testprojekt an, lass den Bootstrap die drei Files ziehen.

### Phase B — Replay (frischer Kontext)
Zweite Session / Sub-Agent simuliert frische Supervisor-Aufnahme: nur Schaltplan + letzter Handover lesen — reicht das, um zu wissen, was zu tun ist und wo ein Problem sitzt? Wenn nein: Schema nachschärfen.

### Phase C — Adversarial
Trage einen verworfenen Ansatz NUR in den Handover (nicht in den Schaltplan) ein, simuliere Supervisor-Wechsel → Nachfolger darf den Ansatz NICHT erneut starten. Greift die Regel „Dauerhaftes → Schaltplan"? Wenn der Ansatz durchrutscht: Regel/Schema härten.

### Phase D — Cleanup
Testprojekt + Artefakte löschen, Working-Tree-Root-Listing verifiziert Sauberkeit.

---

## Schritt 07 — Commit + Push

Branch: main
Commits getrennt:
1. `refactor(handover): mjolnir → Handover, Umbau auf JSON-Schema`
2. `feat(schaltplan): Projekt-Schaltplan-Template + HTML-Render`
3. `feat(tests): Human-Test-Liste Template + HTML-Render`
4. `docs(kodex): Doku-Pflicht, Routing, Gedächtnis/Staffelstab-Trennung`

Push auf `origin/main`. `$LASTEXITCODE = 0` verifizieren. Bei Fehler → DECISIONS_PENDING.md + Handover BLOCKIERT, auf Deutsch.

---

## Schritt 08 — HANDOVER.json schreiben (neues Format dogfooden)

Schreibe den Abschluss-Handover dieses FR bereits im NEUEN `HANDOVER.json`-Format (STATUS-Kopf + erster Historie-Eintrag). Das ist gleichzeitig der erste echte Praxistest des Schemas.

---

## Wichtige Hinweise

- **JSON für alle Maschinen-/Struktur-Files** (Schaltplan, Handover, Test-Liste). **Prosa/Bibel-Format für Menschen-Files.** Niemals mischen innerhalb einer Datei. HTML ist reine Render-Schicht auf die JSON — keine zweite Wahrheit.
- **Bei Konflikten oder Unklarheiten:** Nicht raten. DECISIONS_PENDING.md + Handover-Verweis.
- **Quellen-Files** (`fabrik_meta_workflow.json`) bleiben unverändert liegen — sie sind DNA-Vorlage, nicht Umbau-Ziel.
- **Absolutpfad-Falle beachten:** mehrere Templates referenzieren Files per hartem Absolutpfad. Wenn die Umbenennung `mjolnir`→`Handover` solche Pfade trifft, ALLE Referenzen mitziehen, sonst brechen Templates.
