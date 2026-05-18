# FEATURE_REQUEST_aufraeumarbeiten-post-catch.md

**Datum:** 2026-05-17
**Auftraggeber:** Supervisor (Chat-Fenster)
**Empfänger:** Coda
**Kurzname:** aufraeumarbeiten-post-catch
**Erwartete Dauer:** 1-2 Sessions
**Vorgänger:** faulheits-catch-integration (FERTIG, alle 8 Schritte durch)

---

## Kontext

Die Faulheits-Catch-Integration ist durch, gepusht, mjolnir.md sauber.
Jetzt ist die Plattform stabil genug für die Aufräumarbeiten die in
`DECISIONS_PENDING.md` geparkt wurden, plus ein paar Folge-Verbesserungen
die der Supervisor beim Lesen der mjolnir.md identifiziert hat.

**Wichtiger Vorab-Hinweis:** Dieser Auftrag enthält bewusst mehrere
unabhängige Teilarbeiten. Jeder Schritt ist atomar — wenn einer
blockiert, dokumentier in `DECISIONS_PENDING.md` und mach mit dem
nächsten weiter. Niemals den ganzen Auftrag wegen einer Teilfrage stoppen.

Dieser Auftrag ist KEINE Workflow-Verschärfung — der Selbsttest aus
Catch 06 ist nicht zwingend pro Teilschritt, aber für Schritt 03 und
Schritt 09 ist er ausdrücklich vorgesehen.

---

## Akzeptanzkriterien (Globale Checkliste)

- [ ] `templates/` vs `_templates/` Konflikt aufgelöst (Schritt 03)
- [ ] `Try_Faulheits_catch.md` Provenienz geklärt (Schritt 04)
- [ ] Naming-Konvention für FEATURE_REQUEST-Dateien dokumentiert + erzwungen (Schritt 05)
- [ ] `PROJECT_BOOTSTRAP_README.md` mit Beispiel-Walkthrough ergänzt (Schritt 06)
- [ ] `README.md` des `Claude/`-Repos modernisiert (Schritt 07)
- [ ] `DESIGN.md` Stand abgeglichen mit aktueller Realität (Schritt 08)
- [ ] Zerberus-Lessons gegen GLOBAL_LESSONS abgeglichen, Dubletten entfernt (Schritt 09 mit Selbsttest)
- [ ] `_drafts_gist/`-Vorbereitungsordner mit Index-Konzept für Phase 3 (Schritt 10)
- [ ] Alle DECISIONS_PENDING-Einträge entweder gelöst ODER bewusst als "verschoben" markiert
- [ ] `mjolnir.md` enthält STATUS=FERTIG-Header mit pro-Schritt-Stand
- [ ] Push auf main mit `$LASTEXITCODE = 0` verifiziert
- [ ] FEATURE_REQUEST_aufraeumarbeiten-post-catch.md → `*_ERLEDIGT.md` umbenannt

---

## Schritt 01 — Bestandsaufnahme (kompakt)

Schnelles Listing des aktuellen Stands:

- `git status` zeigt sauberen Working-Tree (sollte er, nach letzter Session)
- Inhalt von `DECISIONS_PENDING.md` einlesen — wieviele offene Punkte stehen drin?
- Listing von `templates/` (8 Files alt) und `_templates/` (4 Files neu)
- Letzten Commit-Hash auf main festhalten als Rollback-Referenz

Das Ergebnis ist eine kurze Notiz für die Auftragshistorie, kein Output-File.

---

## Schritt 02 — Naming-Konvention für FEATURE_REQUESTs festklopfen

**Beobachtung:** Letzter Auftrag wurde von Coda als `FEATURE_REQUEST_CLAUDE.md`
abgelegt — also Projektname statt Kurzname. Der Kurzname `faulheits-catch-integration`
wäre richtig gewesen.

**Aufgabe:** Konvention dokumentieren und durchsetzen.

**Format der Konvention (in GLOBAL_LESSONS.md als neue Lesson anhängen):**

```
NAMING|FEATURE_REQUEST_{kurzname}.md|kurzname = kebab-case-aus-FEATURE_REQUEST-Frontmatter|niemals Projektname als Filename|bei Umbenennung Lifecycle: kurzname-suffix bleibt erhalten (*_ERLEDIGT.md, *_QUEUED.md)
```

Plus prosaischer Anlass-Block:

> Anlass: faulheits-catch-integration-Session legte Datei als
> `FEATURE_REQUEST_CLAUDE.md` ab. Bei mehreren parallelen Aufträgen
> in einem Projekt wäre die Datei nicht eindeutig identifizierbar.

**Konkret zu tun:**

- GLOBAL_LESSONS.md um diese Lesson erweitern (zwischen Catch 04 und Catch 05 passt thematisch am besten, oder als eigene Sektion „Naming-Konventionen")
- Im `_templates/FEATURE_REQUEST_TEMPLATE.md` einen Kommentar am Anfang
  einfügen: `<!-- Dateiname: FEATURE_REQUEST_{kurzname}.md - NIE Projektname -->`
- Das letzte FEATURE_REQUEST-File (`FEATURE_REQUEST_CLAUDE_ERLEDIGT.md`?)
  prüfen — falls es noch existiert, NICHT umbenennen (Historie wahren),
  aber in der Commit-Message dokumentieren dass das die alte Konvention war.

---

## Schritt 03 — `templates/` vs `_templates/` Konflikt auflösen (mit Selbsttest)

**Situation:** Zwei Template-Verzeichnisse existieren parallel.
- `templates/` — 8 Files, ältere Konvention, Commit 31b32f5
- `_templates/` — 4 Files, neu aus dem Faulheits-Catch-Auftrag

**Aufgabe:** Konsolidierung auf ein Verzeichnis.

**Vorgehen:**

1. Inhalt beider Verzeichnisse listen mit Dateinamen + erster Zeile als Tag
2. Inhaltsabgleich: welche der 8 alten Files haben kein Pendant in den 4 neuen?
   - Falls inhaltlich relevant (z.B. spezielle Templates die fehlen): nach `_templates/` migrieren mit Aktualisierung auf neuen Bibel-Format-Standard
   - Falls obsolet oder ersetzt: in der Commit-Message dokumentieren warum
3. Nach Migration: `templates/` löschen (per `git rm -r`)
4. `_templates/` umbenennen zu `templates/` (Unterstrich war Provisorium für
   die parallel-Existenz, jetzt kann der saubere Name zurück)
5. Alle Verweise in anderen Files auf den neuen Pfad anpassen:
   - `PROJECT_BOOTSTRAP_README.md`
   - `GLOBAL_LESSONS.md` (falls referenziert)
   - `SUPERVISOR_KODEX.md` (falls referenziert)

**Selbsttest (Catch 06 Pattern):**

- **Phase A:** Nach Konsolidierung: Dummy-Projektordner anlegen, `PROJECT_BOOTSTRAP_README.md` reinkopieren, ausführen wie Sub-Agent — findet er alle Templates am neuen Pfad?
- **Phase B:** Sub-Agent simuliert frische Session, soll ein neues Projekt bootstrappen — funktioniert es ohne Pfad-Fehler?
- **Phase C:** Grep nach allen Vorkommnissen von `_templates` und `templates/` im gesamten `Claude/`-Verzeichnis — keine Inkonsistenzen zurückgelassen?
- **Phase D:** Aufräumen aller Test-Artefakte, Listing zur Verifikation.

**Falls Schritt 03 unklar wird** (z.B. nicht klar ob ein altes Template noch
wo referenziert wird): in `DECISIONS_PENDING.md` als „Migration X übersprungen
weil Y" dokumentieren und mit Schritt 04 weitermachen. Nicht hängen bleiben.

---

## Schritt 04 — `Try_Faulheits_catch.md` Provenienz klären

**Situation:** Letzte Session hat festgestellt dass diese Datei weder
im Working-Tree noch in der Git-History existiert. Sie ist aber im
Chat-Projekt-Kontext vorhanden und wurde als Quelle verwendet.

**Vermutung des Supervisors:** Die Datei existiert nur im Anthropic-Chat-
Projekt-Speicher (von Chris hochgeladen), aber nie als Git-File angelegt.

**Aufgabe:** Die Datei dauerhaft auf der Platte verankern, damit sie
nicht nur in Chat-Sessions verfügbar ist.

**Konkret:**

1. `Try_Faulheits_catch.md` als kanonische Datei in `Claude/concepts/`
   anlegen (Verzeichnis ggf. neu erstellen — passt thematisch für
   Konzept-Dokumente die kein operativer Code/Workflow sind).
2. Inhalt aus dem ursprünglichen Try_Faulheits_catch.md
   wiederherstellen — die 6 Catches + Selbsttest-Pattern + Bibel-Cheat-Sheet
   sind bereits in GLOBAL_LESSONS.md migriert, aber das Original ist als
   Konzept-Ursprung wertvoll.
3. Header der Datei ergänzen:
   ```
   # Try_Faulheits_catch.md (Konzept-Ursprung)

   **Status:** Historisches Dokument. Operative Version siehe GLOBAL_LESSONS.md.
   **Eingang:** Mai 2026 als Konzept-Dokument von Chris.
   **Verteilung:** Inhalte sind in GLOBAL_LESSONS.md und SUPERVISOR_KODEX.md migriert.
   ```
4. Commit-Message: `docs(concepts): preserve Try_Faulheits_catch.md as canonical concept origin`

**Falls Chris den Inhalt der Datei nochmal bereitstellen soll:** in
DECISIONS_PENDING dokumentieren als „Volltext fehlt — Chris bitten,
.md erneut hochzuladen". Aber: die Inhalte sind bereits in den
abgeleiteten Files, also kein Substanzverlust.

---

## Schritt 05 — `PROJECT_BOOTSTRAP_README.md` mit Beispiel-Walkthrough

**Aktueller Zustand:** Die Datei erklärt was Coda zu tun hat, aber sie
ist abstrakt. Für eine frische Coda-Session — oder einen menschlichen
Leser der das System verstehen will — fehlt ein konkretes Beispiel.

**Aufgabe:** Einen vollständigen Beispiel-Walkthrough am Ende der Datei
ergänzen — fiktives Projekt, z.B. „Weinkeller-Manager":

```markdown
## Beispiel-Walkthrough

**Szenario:** Chris hat einem Kumpel das Projekt-Anfrage-Template gegeben.
Der Kumpel hat es ausgefüllt für „Weinkeller-Manager — App die mir sagt
welcher Wein zu welchem Essen passt". Datei wird in neuen Ordner
`weinkeller-manager/` gelegt zusammen mit Kopie dieser README.

### Was Coda dann tut:

1. Liest PROJEKT_ANFRAGE.md — versteht: Solo-User, mobil + Browser, ~50 Weine, kein Login
2. Liest GLOBAL_LESSONS.md — versteht: kein Terminal für Chris, mjolnir.md Pflicht
3. Liest SUPERVISOR_KODEX.md — bestätigt: Chat-Instanz wird Prompts liefern, keine Befehle
4. Zieht aus templates/: CLAUDE_PROJEKT_TEMPLATE.md, SUPERVISOR_PROJEKT_TEMPLATE.md, mjolnir_TEMPLATE.md, FEATURE_REQUEST_TEMPLATE.md
5. Ersetzt {PROJEKT} durch „weinkeller-manager" überall
6. Erzeugt Skelettstruktur: src/, tests/, docs/, .gitignore, README.md
7. Erzeugt CLAUDE_weinkeller-manager.md mit Pfaden zu globalen Files
8. Fragt Chris die 3-5 Architektur-Fragen:
   - Tech-Stack: Python+FastAPI Backend, React Frontend? (Standardvorschlag)
   - Datenspeicherung: SQLite (lokal) oder Server-DB?
   - Bildupload für Etiketten ja/nein?
   - LLM-Integration für Wein-Empfehlungen jetzt oder Phase 2?
9. Wartet auf Antworten in mjolnir.md (Chris notiert auf dem Handy)
10. Geht dann mit Patch 001 los

### Was Coda dabei NIE tut:

- Chris bitten `pip install` oder `npm init` selbst auszuführen
- Templates raten statt aus templates/ zu ziehen
- mjolnir.md am Session-Ende vergessen
```

---

## Schritt 06 — `README.md` des Claude-Repos modernisieren

**Aktueller Zustand:** Unbekannt (Coda soll prüfen). Vermutlich veraltet
oder generisch.

**Aufgabe:** README.md so umbauen dass jemand der auf das Repo stößt
in 30 Sekunden versteht was es ist.

**Empfohlene Struktur:**

```markdown
# Claude — Marathon Workflow Knowledge Base

Persönliche Knowledge-Base für den Marathon-Workflow.
Architekt: Chris (@Bmad82)

## Was ist das?

Der Marathon-Workflow ist ein Drei-Rollen-System zur Software-Entwicklung
ohne dass der Architekt selbst Code anfasst:

- **Architekt** (Mensch) gibt Ziele vor
- **Supervisor** (Claude im Chat) plant und schreibt Prompts
- **Coda** (Claude Code) implementiert, testet, committet, pusht

## Kernfiles

- [GLOBAL_LESSONS.md](GLOBAL_LESSONS.md) — Lessons aus echten Incidents, 6 Faulheits-Catches
- [SUPERVISOR_KODEX.md](SUPERVISOR_KODEX.md) — Was Chat-Instanzen nie/immer tun
- [PROJECT_BOOTSTRAP_README.md](PROJECT_BOOTSTRAP_README.md) — Wie neue Projekte starten
- [templates/](templates/) — Bootstrap-Templates für neue Projekte
- [concepts/](concepts/) — Konzept-Dokumente, Ursprünge, Architekturskizzen

## Projekte die mit diesem System arbeiten

- Zerberus Pro 4.0 — Python-Backend, Patch 100+
- (weitere folgen)

## Lizenz

Privates Repo. Inhalte dienen der Selbst-Dokumentation.
```

**Konkret:** Bestehende README.md lesen, schauen was an Inhalten wert
ist erhalten zu bleiben, dann neu strukturieren. Bestehende relevante
Sektionen integrieren.

---

## Schritt 07 — `DESIGN.md` Stand abgleichen

**Aufgabe:** Existierende `DESIGN.md` lesen und prüfen ob sie noch
zum aktuellen System passt oder ob sie veraltet ist.

**Wenn veraltet:** Aktualisierung in derselben Datei, kein Neuanlegen.
Mindestens diese Abschnitte sollten drin sein:

- Drei-Rollen-Modell (Architekt / Supervisor / Coda)
- File-Hierarchie (lokal / Repo / Gists-geplant)
- Bibel-Format vs Prosa-Trennung
- Mjölnir-Round-Trip
- Die 6 Faulheits-Catches (kurz, Verweis auf GLOBAL_LESSONS.md)
- 5h-Fenster-Constraint
- Bootstrap-Prinzip (neues Projekt aus PROJEKT_ANFRAGE + Templates)

**Wenn aktuell:** kurzes Update-Datum am Ende setzen, sonst unverändert lassen.

---

## Schritt 08 — Zerberus-Lessons gegen GLOBAL_LESSONS abgleichen (mit Selbsttest)

**Hintergrund:** Zerberus hat eigene Lessons aus seinen 100+ Patches.
Einige davon wurden ins Globale promoviert (Multi-Session-Status-Header
zum Beispiel — Commit 08c7e9e). Andere sind noch projekt-spezifisch.

**Aufgabe:** Doppelt vorhandene Lessons in Zerberus auf Verweis reduzieren.

**Vorgehen:**

1. `zerberus_lessons.md` lokal lesen (Pfad vermutlich `C:\Users\chris\Python\Zerberus\` oder im Repo des Zerberus-Projekts — Coda findet das selbst)
2. Jede Lesson durchgehen: ist der Inhalt in GLOBAL_LESSONS.md bereits abgedeckt?
3. Wenn ja: Zerberus-Lesson ersetzen durch:
   ```
   ## {Titel} → siehe GLOBAL_LESSONS.md
   Promotiert {Datum}. Originaler Anlass: {kurzer Hinweis auf B-id}.
   ```
4. Wenn nein: Zerberus-Lesson unverändert lassen — die ist projekt-spezifisch.

**Selbsttest:**

- Phase A: Anzahl Lessons in zerberus_lessons.md vor/nach Bearbeitung — Reduktion erwartet, aber keine sollte komplett verschwinden, nur ersetzt durch Verweis.
- Phase B: Sub-Agent simuliert „neue Zerberus-Session liest seine Lessons" — findet er alle Informationen, ggf. durch Folgen der Verweise?
- Phase C: Grep nach Catch-Begriffen in zerberus_lessons.md — sollte nur noch in Verweis-Form vorkommen, nicht volltext.
- Phase D: Aufräumen, Commit im Zerberus-Repo separat von Claude-Repo-Commits.

**Falls Zerberus-Repo nicht erreichbar oder zu komplex:** dokumentiere
in `DECISIONS_PENDING.md` als „Zerberus-Lessons-Konsolidierung in
eigene Session ausgelagert" und überspringe diesen Schritt.

---

## Schritt 09 — `_drafts_gist/` Vorbereitungsordner anlegen

**Hintergrund:** Phase 3 der Roadmap ist die Gist-Migration. Damit das
nicht aus dem Nichts beginnt, soll bereits jetzt ein Vorbereitungs-
verzeichnis entstehen wo Konzept-Files für die spätere Gist-Struktur
liegen.

**Konkret:**

1. Neuer Ordner `Claude/_drafts_gist/` anlegen
2. Darin: `INDEX_GIST_DRAFT.md` mit folgendem Inhalt:

```markdown
# Bmad82-Projects Index (Gist Draft)

**Status:** Konzept-Entwurf für Phase 3 der Roadmap.
Wird zu einem öffentlichen GitHub-Gist wenn Phase 3 aktiv wird.

## Zweck

Single Source of Truth für aktive Projekte. Eine URL, die in
Supervisor-Memories hinterlegt ist. Von hier aus navigieren
frische Chat-Instanzen zu den Projekt-spezifischen Gists.

## Format pro Projekt-Eintrag

```
PROJEKT|Name|Gist-URL|Status (aktiv/pausiert/archiviert)|Letzter-Patch|Tags
```

## Aktive Projekte (Stand: TBD)

- Zerberus Pro 4.0 — Gist-URL: TBD — aktiv — P-100+
- (weitere wenn migriert)

## Pflichtfelder im Projekt-Gist

- `mjolnir_{PROJEKT}.md`
- `SUPERVISOR_{PROJEKT}.md` (Bibel-Format)
- `MARATHON_WORKFLOW_{PROJEKT}.md`
- Freshness-Stempel als erste Zeile:
  `LAST_PATCH: P-XXX | TS: YYYY-MM-DDTHH:MM | PROJECT: XYZ`
```

3. Eine zweite Datei `Claude/_drafts_gist/ZERBERUS_GIST_DRAFT.md` als Beispielmuster für einen Projekt-Gist:

```markdown
# Zerberus Pro 4.0 — Live State (Gist Draft)

LAST_PATCH: P-???  |  TS: TBD  |  PROJECT: Zerberus Pro 4.0

## Files in diesem Gist (wenn aktiv)

- mjolnir_zerberus.md — Round-Trip-Status, was Chris physisch tun muss
- SUPERVISOR_zerberus.md — Bibel-Format-Überblick für Chat-Instanzen
- MARATHON_WORKFLOW_zerberus.md — Operative Workflow-Doku

## Nicht in diesem Gist:

- CLAUDE_zerberus.md (Codas Betriebsanleitung, bleibt lokal + Repo)
- Lessons (separater Lessons-Gist später, ändert sich selten)
- Source-Code (bleibt in eigenständigem Repo)
```

**Wichtig:** Diese Files sind Entwürfe. Sie werden noch nicht zu echten
Gists — das passiert erst in Phase 3. Der Sinn jetzt ist, dass bei
Start von Phase 3 keine Konzept-Arbeit mehr nötig ist, nur noch
Migration und Push.

---

## Schritt 10 — `DECISIONS_PENDING.md` aktualisieren

Am Ende der Session: Alle DECISIONS_PENDING-Einträge die in dieser
Session adressiert wurden, mit Status versehen:

- **Gelöst** → kurze Notiz wie + Commit-Hash
- **Bewusst verschoben** → Begründung + Zielsession
- **Neu aufgetaucht** → neue Einträge an den Anfang

Niemals Einträge stillschweigend löschen — sie sind Historie.

---

## Schritt 11 — Commits + Push

Empfohlene Commit-Aufteilung (alles auf main, keine Worktrees nötig):

1. `feat(naming): enforce FEATURE_REQUEST kebab-case kurzname convention`
2. `refactor(templates): consolidate templates/ and _templates/ → templates/`
3. `docs(concepts): preserve Try_Faulheits_catch.md as canonical origin`
4. `docs(bootstrap): add example walkthrough to PROJECT_BOOTSTRAP_README`
5. `docs: modernize README.md`
6. `docs: align DESIGN.md with current state`
7. `refactor(zerberus): deduplicate lessons against GLOBAL_LESSONS` *(falls Schritt 08 durchgeführt — Zerberus-Repo)*
8. `feat(gist-prep): add _drafts_gist/ with index and project templates`
9. `chore(pending): update DECISIONS_PENDING.md with session outcomes`

Push auf main, `$LASTEXITCODE`-Check, bei Fehler Fehlertext **auf Deutsch**
in mjolnir.md unter BLOCKIERT-Status.

---

## Schritt 12 — mjolnir.md schreiben

Pflicht-Header:

```
STATUS|FERTIG (oder TEIL_FERTIG wenn Schritt 08 ausgelagert)|AUFTRAG: aufraeumarbeiten-post-catch|FORTSCHRITT: {erledigte Schritte} von 12|NÄCHSTE SESSION: entfällt (FERTIG) oder {nächster offener Schritt}
```

Plus prosaisch:

- **STATUS:** FERTIG | TEIL_FERTIG
- **AUFTRAG:** aufraeumarbeiten-post-catch
- **FORTSCHRITT:** X von 12 Schritten
- **NÄCHSTE SESSION:** ...
- **WARNUNG:** (nur wenn TEIL_FERTIG)

### Was Chris physisch tun muss

- Auf dem Handy nach Push prüfen ob Repo grün ist
- Falls TEIL_FERTIG: nächste Session braucht keinen neuen FEATURE_REQUEST, sondern Coda greift den verbleibenden Schritt auf
- DECISIONS_PENDING.md gelegentlich anschauen für Architekt-Entscheidungen

### Auftragshistorie

Pro Schritt 1-3 Zeilen: was wurde gemacht, was war auffällig, was wurde ggf. verschoben.

### Verzeichnisstruktur am Session-Ende

Listing von `Claude/` als finalen Beweis dass alles aufgeräumt ist.

---

## Schritt 13 — FEATURE_REQUEST_aufraeumarbeiten-post-catch.md umbenennen

Bei STATUS=FERTIG: Umbenennen zu `FEATURE_REQUEST_aufraeumarbeiten-post-catch_ERLEDIGT.md`.
Bei STATUS=TEIL_FERTIG: Datei bleibt unverändert, nächste Session greift sie auf.

---

## Wichtige Hinweise

**Atomare Schritte:** Jeder Schritt 02-09 kann unabhängig erfolgreich oder
geparkt sein. Niemals einen späteren Schritt blockieren weil ein früherer
unklar ist — dokumentier in DECISIONS_PENDING und mach weiter.

**Bibel-Format vs Prosa:** Konsequent trennen. Maschine pipe-getrennt,
Mensch in Prosa. Niemals mischen.

**Selbsttest nur wo angesagt:** Schritte 03 und 09 brauchen vollen
A-B-C-D-Selbsttest (Pfad-Änderungen und Lesson-Migration sind beides
Stellen wo subtle Brüche entstehen können). Andere Schritte: einfache
Verifikation per Listing/Grep reicht.

**Keine Worktrees:** Alles direkt auf main, Strukturarbeit braucht keine
Branches.

**Deutsch bei Fehlerausgaben:** Wie immer.

**Wenn etwas wirklich blockiert:** TEIL_FERTIG-Status setzen, klar
dokumentieren was offen ist, mjolnir.md mit Hinweis dass nächste Session
keinen neuen Request braucht.

---

## Ende des FEATURE_REQUEST
