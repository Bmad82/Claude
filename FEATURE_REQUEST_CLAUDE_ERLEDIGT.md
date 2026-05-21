# FEATURE_REQUEST — Session-Auffüll-Regel

**Kurzname:** session-auffuell-regel
**Projekt:** Claude (Meta-Repo) + alle aktiven Projekte (Zerberus, Sága)
**Priorität:** HOCH
**Datum:** 2026-05-21

---

## Kontext für Coda

Coda-Sessions schließen aktuell ab sobald der primäre Auftrag erledigt ist — egal wie viel Token-Budget noch übrig ist. Bei kleinen Aufträgen (3 CSS-Selektoren) verbrennt die Session ~100k Tokens für Bootstrapping + Doku, liefert aber nur ~500 Tokens echte Arbeit. Overhead-Ratio: 200:1.

**Beweis:** Kintsugi-Migration (N+1 bis N+10): 3 Sessions à ~120k statt 1 Session à ~360k. Mega-Patch-Ära (P122–P152): 16 Patches in einem Fenster bei 383k — 24k/Patch statt 100k+.

**Technische Basis:** Kontextfenster ist 1M Token. Degradation (Lost in the Middle, Vergessen) beginnt ab ~50% = ~500k. Chris' Stopp-Marke liegt bei ~400–450k. Die Auffüll-Regel nutzt den Raum zwischen Patch-Ende und Stopp-Marke.

---

## Auftrag

Implementiere die **Session-Auffüll-Regel** in allen relevanten Dateien. Zwei Stufen: erst Templates (kanonische Quelle), dann bestehende Projekte (vorsichtig patchen).

---

## Stufe 1 — Templates im Claude-Repo (`C:\Users\chris\Python\Claude\`)

### 1.1 `templates/MARATHON_WORKFLOW_TEMPLATE.md`

Finde die **Stopp-Regeln**-Sektion. Füge DIREKT DANACH eine neue Sektion ein:

```markdown
## Session-Auffüll-Regel (2026-05-21)

Primärer Auftrag erledigt UND Token-Stand < 300k → NICHT abschließen, weiterarbeiten.

Auffüll-Reihenfolge:
1. Weitere Punkte im selben FEATURE_REQUEST (z.B. N+3, N+4... bei Multi-Session-Plänen)
2. Offene Items in MARATHON_WORKFLOW mit Status OFFEN + keine Abhängigkeiten
3. BACKLOG-Items mit Status OFFEN, sortiert nach Priorität (Sofort > Mittelfristig > Nice-to-have)
4. Bekannte Test-Schulden (pre-existing Failures fixen)
5. Doku-Hygiene (veraltete Stand-Anker, README-Drift, Lessons-Konsolidierung)

Stopp-Schwelle: ~350k Token (50k Reserve für sauberen Doku-Abschluss).

Ausnahmen — NIE als Auffüller:
- Destruktive Operationen (DB-Migration, Auth-Refactor, FAISS-Switch)
- Items die Chris-Entscheidung brauchen (DECISIONS_PENDING)
- Items die externe Ressourcen brauchen (Docker-Pull, Modell-Download > 1 GB)
- Items die die Test-Suite fundamental ändern (neues Framework, Fixture-Umbau)

Doku-Pflicht bei Auffüll-Patches:
- Eigener `git commit` pro Folge-Patch (mit Patch-Nummer/Name)
- Lesson-Eintrag falls nötig
- KEIN separater HANDOVER/SUPERVISOR/Gist-Update pro Zwischen-Patch
- Am Session-Ende: EIN HANDOVER der ALLE Patches zusammenfasst

Anti-Pattern: "Patch fertig bei 120k → Doku → Handover → STOPP" — verbrennt 80% des Budgets für Overhead.
```

### 1.2 `templates/CLAUDE_PROJEKT_TEMPLATE.md`

Finde die Marathon-Workflow-Sektion (oder die Stelle wo Stopp-Regeln referenziert werden). Füge im **Bibel-Format** ein:

```
## Session-Auffüll-Regel (2026-05-21, Kintsugi-Migration Token-Audit)
Primärer Auftrag erledigt UND < 300k Token verbraucht → weiterarbeiten, nicht abschließen|Auffüll-Reihenfolge: (1) FEATURE_REQUEST Restpunkte (2) MARATHON_WORKFLOW offene Items (3) BACKLOG (4) Test-Schulden (5) Doku-Hygiene|Stopp bei ~350k (50k Reserve für Doku)|Zwischen-Patches: eigener Commit, ABER kein separater HANDOVER — ein HANDOVER am Session-Ende für alle|AUSNAHME: destruktive/riskante Patches NIE als Auffüller|Anti-Pattern: "Patch fertig bei 120k → Doku → STOPP" = 80% Overhead
```

### 1.3 `lessons/LESSONS_KONSOLIDIERT.md` (oder `lessons.md` im Claude-Repo — die konsolidierte Lessons-Datei)

Neue Lesson einfügen:

```
## Session-Auffüll-Regel (2026-05-21, Kintsugi-Migration Token-Audit)
Sessions schlossen bei ~120k ab obwohl 300k+ Budget frei war|3 Sessions à 120k statt 1 à 360k = 200k verschwendet|Mega-Patch-Ära (P122–P152) bewies: 24k/Patch bei Auffüll-Logik vs 100k+/Patch ohne|Fix: Primärer Auftrag fertig UND < 300k verbraucht → nächstes Item nehmen, Stopp bei ~350k|Nur sichere unabhängige Items als Auffüller, destruktive Ops nie|Ein HANDOVER am Ende statt pro Zwischen-Patch

Anlass: Kintsugi-Migration CSS-Patches. 10 kleine Sub-Tasks über 3 Sessions verteilt, jede mit vollem Bootstrap-Overhead. Hätten in eine einzige Session gepasst.
```

### 1.4 `WORKFLOW_SUMMARY.md` im Claude-KB-Gist (`48b997e53ff331eeefef53c810ee7331`)

Der Session-Zyklus hat 12 nummerierte Schritte. Finde **Schritt 8:**
> "8. Arbeit ausführen — Tests, Commit, Push selbst ($LASTEXITCODE verifizieren)"

Füge DIREKT NACH Schritt 8 einen neuen Schritt ein (bisherige 9–12 werden 10–13):
> "9. **Auffüll-Check:** Auftrag erledigt UND < 300k Token verbraucht → nächstes Item aus MARATHON_WORKFLOW oder BACKLOG nehmen. Stopp bei ~350k (50k Reserve für Doku). NUR sichere, unabhängige Items — destruktive Ops nie als Auffüller."

### 1.5 `GLOBAL_LESSONS.md` im selben Claude-KB-Gist

Die GLOBAL_LESSONS.md lebt SOWOHL lokal im Claude-Repo ALS AUCH im Claude-KB-Gist. Beide müssen die gleiche Lesson bekommen. Füge die Lesson aus 1.3 OBEN ein (neueste Lessons stehen oben, nach dem Header-Block und vor "## OBERSTES GEBOT").

---

## Stufe 2 — Bestehende Projekte (VORSICHTIG)

### WICHTIG: Individuelle Regeln nicht überschreiben

Jedes Projekt hat möglicherweise projektspezifische Stopp-Regeln oder Eigenheiten in der CLAUDE_{PROJEKT}.md. Die Auffüll-Regel wird **hinzugefügt**, nicht ersetzt. Bestehende Regeln bleiben unverändert.

### WICHTIG: Gist-Updates

Sowohl der Claude-KB-Gist (`48b997e5...`) als auch die Projekt-Gists müssen aktualisiert werden. Nutze `gist_publisher.py` aus `workflow/` im Claude-Repo für API-basierte Updates. Die Dateien WORKFLOW_SUMMARY.md und GLOBAL_LESSONS.md im Claude-KB-Gist müssen die gleichen Änderungen wie die lokalen Kopien bekommen.

### 2.1 Zerberus (`C:\Users\chris\Python\Zerberus\`)

**Datei: `CLAUDE_ZERBERUS.md`**
- Finde die Marathon-Workflow / Stopp-Regeln-Sektion
- Füge die Auffüll-Regel im Bibel-Format NACH den bestehenden Stopp-Regeln ein (gleicher Text wie 1.2)
- KEINE bestehenden Regeln löschen oder ändern

**Datei: `MARATHON_WORKFLOW_ZERBERUS.md`** (falls vorhanden)
- Stopp-Regeln-Sektion um Auffüll-Pfad ergänzen (gleicher Text wie 1.1)

**Datei: `lessons_zerberus.md`** (falls vorhanden)
- Lesson-Eintrag hinzufügen (gleicher Text wie 1.3)

### 2.2 Sága (`C:\Users\chris\Python\Saga\`) — falls aktiv

Gleiche Schritte wie 2.1, angepasst auf `CLAUDE_SAGA.md` etc.
Falls Sága noch kein aktives Marathon-Workflow-Setup hat: ÜBERSPRINGEN.

---

## Stufe 3 — Showcase-Anpassung

### 3.1 `marathon_workflow_showcase.html` (im Zerberus-Repo ODER Claude-Repo — wo sie lebt)

Finde den Session-Zyklus-Abschnitt (Schritt 05 oder äquivalent). Ergänze die Auffüll-Regel als sichtbaren Punkt. Beispieltext:

> **Auffüll-Regel:** Patch fertig und < 300k verbraucht? Nächstes Item nehmen. Stopp bei ~350k. Destruktive Ops nie als Auffüller.

---

## Akzeptanzkriterien

- [ ] `templates/MARATHON_WORKFLOW_TEMPLATE.md` enthält Auffüll-Regel nach Stopp-Regeln
- [ ] `templates/CLAUDE_PROJEKT_TEMPLATE.md` enthält Auffüll-Regel im Bibel-Format
- [ ] Konsolidierte Lessons-Datei enthält Lesson mit Kintsugi-Anlass
- [ ] `WORKFLOW_SUMMARY.md` im Claude-KB-Gist: neuer Schritt 9 (Auffüll-Check) nach bisherigem Schritt 8, Umnummerierung 9→10, 10→11, 11→12, 12→13
- [ ] `GLOBAL_LESSONS.md` im Claude-KB-Gist: Lesson eingefügt (oben, nach Header)
- [ ] `GLOBAL_LESSONS.md` lokal im Claude-Repo: identischer Lesson-Eintrag
- [ ] `CLAUDE_ZERBERUS.md` enthält Auffüll-Regel (Bibel), bestehende Regeln unverändert
- [ ] `MARATHON_WORKFLOW_ZERBERUS.md` (falls vorhanden) enthält Auffüll-Regel
- [ ] `lessons_zerberus.md` (falls vorhanden) enthält Lesson
- [ ] Sága geprüft und ggf. gepatcht ODER explizit übersprungen mit Begründung
- [ ] Showcase-HTML aktualisiert
- [ ] Jede Datei: `git diff` zeigt NUR Additions, keine Deletions bestehender Regeln
- [ ] Alle Änderungen in einem Commit (oder logisch gruppiert: Templates-Commit + Projekte-Commit)

## Selbsttest

Nach Implementierung:
1. `grep -r "Auffüll" . --include="*.md"` im Claude-Repo — Erwartung: mindestens 4 Treffer (Template MW, Template CLAUDE, Lessons lokal, Workflow Summary lokal)
2. `grep -r "Auffüll" . --include="*.md"` im Zerberus-Repo — Erwartung: mindestens 2 Treffer (CLAUDE_ZERBERUS, lessons_zerberus)
3. Gist-Verifikation: `gist_publisher.py` Dry-Run oder manueller Fetch von WORKFLOW_SUMMARY.md und GLOBAL_LESSONS.md aus dem Claude-KB-Gist — Erwartung: "Auffüll" kommt in beiden vor
4. Wenn < erwartete Treffer: nachpatchen

## Was dieser Patch NICHT tut

- Keine Änderung an der Stopp-Marke (bleibt ~400–450k)
- Keine Änderung am Bootstrap-Prozess
- Keine Änderung an der HANDOVER-Mechanik (nur: ein HANDOVER statt mehrere)
- Keine Änderung an der Feature-Request-Priorisierung (Feature-Request bleibt #1)

---

*Erstellt vom Supervisor, 2026-05-21. Anlass: Token-Audit der Kintsugi-Migration.*

---

## AUDIT (Coda, 2026-05-21, STATUS=FERTIG)

**Stufe 1 — Templates im Claude-Repo:** alle fünf Akzeptanzpunkte erledigt.
- `templates/MARATHON_WORKFLOW_TEMPLATE.md` — neue Sektion „Session-Auffüll-Regel" + Session-Zyklus Schritt 9 ergänzt (Auffüll-Check).
- `templates/CLAUDE_PROJEKT_TEMPLATE.md` — neue Sektion „Session-Auffüll-Regel" im Bibel-Format nach Stopp-Regeln.
- `LESSONS_KONSOLIDIERT.md` — neue Lesson oben (Kintsugi-Migration Token-Audit, 2026-05-21).
- `GLOBAL_LESSONS.md` (lokal) — neue Lesson nach Header, vor Gist-Sync-Lesson. Vollständige Bibel-Zeile + Anlass + Lösung + Generalisierung.
- `workflow/MARATHON_WORKFLOW.md` — Session-Zyklus von 12 auf 13 Schritte (neuer Schritt 9 Auffüll-Check, 9→10..12→13 umnummeriert) plus neue Sektion „Session-Auffüll-Regel".

**Stufe 1 — Claude-KB-Gist (`48b997e53ff331eeefef53c810ee7331`):** PATCH erfolgreich (`updated_at=2026-05-21T10:28:54Z`).
- `WORKFLOW_SUMMARY.md` — neuer Schritt 9 Auffüll-Check eingefügt, alte 9–12 umnummeriert auf 10–13.
- `GLOBAL_LESSONS.md` — Lesson-Spiegel identisch zur lokalen Kopie.

**Stufe 2 — Zerberus-Repo (`C:\Users\chris\Python\Zerberus\`):** alle drei Punkte erledigt, keine bestehenden Regeln gelöscht.
- `CLAUDE_ZERBERUS.md` — Session-Auffüll-Regel im Bibel-Format zwischen Marathon-Workflow- und HANDOVER-Autonomie-Sektion.
- `MARATHON_WORKFLOW_ZERBERUS.md` — neue Sektion „Session-Auffüll-Regel" nach „Stopp-Regeln", vor „Mjölnir-Konventionen".
- `lessons_ZERBERUS.md` — Lesson-Eintrag oben (Bootstrap-Overhead-Argumentation, Verweis auf Kintsugi-Anlass).

**Stufe 2 — Zerberus-Gist (`7f5af9dd878a6a9d664f062976b27ae8`):** `LESSONS.md` PATCH erfolgreich (`updated_at=2026-05-21T10:28:55Z`).

**Stufe 2 — Sága:** Pfad `C:\Users\chris\Python\Saga\` existiert nicht im Filesystem. Saga-Repo entweder nicht angelegt oder anderer Pfad. **Explizit übersprungen** mit dieser Begründung — kein aktives Marathon-Workflow-Setup für Sága gefunden, keine Patches möglich.

**Stufe 3 — Showcase-HTML:** Kein `marathon_workflow_showcase.html` im Claude-Repo, im Zerberus-Repo oder unter `C:\Users\chris\Python\` insgesamt gefunden (Glob-Search auf `**/*showcase*.html` und `**/marathon*.html` lieferte beide null Treffer). **Explizit übersprungen** — Datei existiert nicht; Showcase-Update entfällt.

**Selbsttest:**
- `grep Auffüll` im Claude-Repo: 7 Treffer (Erwartung ≥ 4) — `templates/MARATHON_WORKFLOW_TEMPLATE.md`, `templates/CLAUDE_PROJEKT_TEMPLATE.md`, `GLOBAL_LESSONS.md`, `LESSONS_KONSOLIDIERT.md`, `workflow/MARATHON_WORKFLOW.md`, `_drafts_gist/WORKFLOW_SUMMARY.md`, dieses ERLEDIGT-File.
- `grep Auffüll` im Zerberus-Repo: 3 Treffer (Erwartung ≥ 2) — `CLAUDE_ZERBERUS.md`, `MARATHON_WORKFLOW_ZERBERUS.md`, `lessons_ZERBERUS.md`.
- Gist-Verifikation: `Auffüll` 1× in `WORKFLOW_SUMMARY.md`, 4× in `GLOBAL_LESSONS.md` (Claude-KB-Gist), 4× in `LESSONS.md` (Zerberus-Gist) — alle drei Files via Fresh-Fetch verifiziert.

**Was dieser Patch NICHT angefasst hat:** Stopp-Marke (bleibt ~400k), Bootstrap-Prozess, HANDOVER-Mechanik (außer „ein HANDOVER statt mehrere"), Feature-Request-Priorisierung (FR bleibt Priorität 1). Keine destruktiven Operationen, keine Test-Suite-Änderung, kein Schema-Update.

**Diff-Hygiene:** Alle Edits sind reine Additions (keine bestehenden Regeln gelöscht, keine Umnummerierung außer der erforderlichen 9→10..12→13 im Session-Zyklus). Logische Gruppierung: zwei Commits (Claude-Repo: Templates + Lessons + Workflow + Showcase-Drafts. Zerberus-Repo: drei Doku-Dateien).
