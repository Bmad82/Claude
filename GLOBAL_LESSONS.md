# GLOBAL_LESSONS — Marathon-Workflow

Universelle Lessons für ALLE Projekte, die den Marathon-Workflow nutzen (Coda + Supervisor + Mjölnir).
Projekt-spezifische Lessons gehören in `lessons/<projekt>_lessons.md`. Diese Datei nur für projektübergreifend gültige Regeln.

Format: jede Lesson eine `##` Sektion mit Datum + Anlass-Patch im Titel. Inhalt in Pipe-Format (`|`-getrennte Punkte), ggf. mit Begründung darunter. Nicht löschen — historische Lessons bleiben, neue oben anhängen.

---

## Gist-Sync (Schritt 12) ist gleichrangige Session-End-Pflicht (2026-05-21, Zerberus Gist-Drift)

Vier Sessions in Folge übersprangen Schritt 12 (Gist-PATCH) des Session-Zyklus|Local-Commit + Push wurden gemacht, Gist-PATCH fiel aus|Gist-Stand fror auf Stand B-aufraeumen (2026-05-18) ein, drei große Sessions später vollständig veraltet|Supervisor (Chat-Instanz) kann Raw-Links nicht fetchen — nur Gists — also ist Mjölnir-Round-Trip auf Supervisor-Seite kaputt sobald Gist-Sync ausfällt|Identisches Anti-Pattern-Profil wie B-072 (mjolnir.md): Pflicht-Schritt am Ende der Session-Liste → Token-knapp-Risiko-Zone → wird als erster gestrichen

**Anlass:** Zerberus, FEATURE_REQUEST_ZERBERUS-Folge-Session 2026-05-21. Chris-Nachtrag im FEATURE_REQUEST: „Gists stehen auf 2026-05-18. Letzte Session hat Schritt 12 NICHT ausgeführt. Pflichtaufgabe vor allem anderen: prüfen warum, Gists aktualisieren, Verstoß als Lesson dokumentieren." Audit per `git log` + Vergleich mit Raw-URLs: vier Sessions hintereinander (B-074, Frontend-Separation, Hel-Separation, FEATURE_REQUEST Teil-Lieferung) hatten Local-Push gemacht, aber den Gist-PATCH unterlassen. Faulheits-Catch #2 (mjolnir.md PFLICHT) ist die naheliegende Wurzel — Gist-Sync ist genauso ein End-of-Session-Schritt und hat genauso wenig Inertia gegen Token-Druck.

**Lösung:** (1) Aktuelle Sync-Lieferung — Gist-PATCH für Projekt-Gist + Claude-KB-Gist mit den jeweiligen aktuellen Files. (2) Lesson-Eintrag projektspezifisch (lessons_ZERBERUS.md) UND projektübergreifend (diese). (3) Workflow-Text in MARATHON_WORKFLOW (sowohl Claude-Master als auch projektspezifisch) verschärft Schritt 12: „PFLICHT, gleichrangig mit HANDOVER (Schritt 8) und mjolnir.md (Schritt 10) — kein optional, kein 'wenn Token übrig'".

**Lesson generalisierbar:** Pflicht-Schritte am Ende der Session-Liste sind systematisch unterbelichtet. Sobald **ein** End-Pflicht-Schritt einmal stillschweigend ausfällt, etabliert sich das Pattern und alle anderen End-Pflicht-Schritte sind als nächstes gefährdet. Schutz: explizite Gleichrangigkeit aller End-Pflichten im Workflow-Text (kein „und dann noch" als Suffix), Anti-Pattern-Block mit konkretem Beispiel, **eigene Lesson** jedes Mal wenn ein End-Pflicht-Schritt ausfällt. Faustregel: wenn der Round-Trip auf Supervisor-/Mjölnir-Seite kaputt geht, weil ein Schritt am Session-Ende übersprungen wurde, ist die Lesson **immer** beim Workflow-Text zu verankern, nicht beim einzelnen Coder. Aktuelle End-Pflicht-Schritte für Coda: HANDOVER (Schritt 8), mjolnir.md (Schritt 10), REPO_INDEX falls geändert (Schritt 11), Push + sync_repos + verify_sync + **Gist-PATCH** (Schritt 12) — alle vier in einem Atemzug, kein „und ggf. noch".

---

## OBERSTES GEBOT (2026-05-16, Zerberus P-umzug)

Chris terminalisiert NICHTS was Coda kann|NIEMALS git/pytest/pip/robocopy/npm-Befehle an Chris delegieren|Coda merged Branches SELBST auf main + pusht SELBST vor Session-Ende|mjolnir.md enthält NUR was physisch unmöglich ist (Touch-Test, echtes Gerät, Docker Desktop UI)|Supervisor (Chat-Fenster) gibt KEINE Terminal-Befehle sondern baut Coda-Prompts (.md)|Verstoß = sofortige Korrektur

**Anlass:** Zerberus P-umzug 2026-05-16 — die vorige Coda-Session hatte den Worktree-Merge + Robocopy + Venv-Aufbau in `mjolnir.md` an Chris delegiert. Klassischer Coda-Faulheits-Verstoß. Das OBERSTE GEBOT zementiert die Trennung: mechanische Terminal-Arbeit ist Coda-Pflicht, mjolnir.md ist nur für Touch/Mikrofon/echtes-Gerät/externe-App-Tests.

**Backstop pro Projekt:** Als Regel 0 in `CLAUDE_<PROJEKT>.md` (vor jeder anderen Regel) plus als erste Sektion in `lessons_<PROJEKT>.md`.

---

## mjolnir.md ist PFLICHT am Session-Ende (2026-05-16, Zerberus B-072)

mjolnir.md wird am Ende JEDER Session überschrieben — ausnahmslos|Alte Version wird IMMER ersetzt|Ohne mjolnir.md-Update ist der Mjölnir-Round-Trip kaputt|Chris kann sonst nicht erkennen ob ein Auftrag abgeschlossen ist|Session-Zyklus Schritt 10 ist NICHT optional|Wenn Schritt 10 fehlt hat Schritt 11 (Push) auch keinen Wert weil Chris nichts davon erfährt

**Anlass:** Zerberus B-072 (Huginn Voice-to-Whisper) 2026-05-16 — Code + Tests + Commit + `_ERLEDIGT.md`-Audit waren komplett, aber `mjolnir.md` wurde nicht überschrieben. Chris hat über den ZUSAMMENFASSUNG-Button die alte P-umzug-Datei gefetcht und konnte B-072 nicht als erledigt sehen.

**Single-Slot vs Audit-Log:** `mjolnir.md` ist Single-Slot-State (genau EINE aktuelle Session-Zusammenfassung) — wird beim nächsten Session-Start eingelesen und gelöscht. `_ERLEDIGT.md` ist Audit-Log (akkumuliert, bleibt bis User es löscht). Beide Datei-Typen haben unterschiedliche Pflege-Regeln und dürfen nicht verwechselt werden.

---

## Worktree-Branches selbst auf main mergen (2026-05-16, Zerberus B-061)

Coda merged Worktree-Branches SELBST auf main vor Session-Ende|NIEMALS einen ungemergten Branch als "Schritt 0" in mjolnir.md an Chris delegieren|Das ist Terminal-Arbeit und fällt unter das OBERSTE GEBOT|Wenn ff-merge nicht möglich: rebase selbst durchführen oder Merge-Commit erstellen

**Anlass:** Zerberus B-061 (Pfad-Audit + Sync-Scripts) 2026-05-16 — Worktree-Branch lag fertig, vorige Coda-Session hatte den Merge nicht gemacht und Chris in `mjolnir.md` darum gebeten. Die nachfolgende Session musste den Merge im Hauptcheckout selbst durchführen plus den eigenen Worktree-Branch rebasen.

**Pattern:** `git stash push` für uncommitted Edits → `git merge --ff-only` → `git stash pop` → eigenen Worktree-Branch per `git rebase main` aktualisieren → ff-merge → push. Konfliktfrei wenn die Edits unterschiedliche Zeilen treffen.

---

## Supervisor-Verhalten: Coda-Prompts statt Terminal-Befehle (2026-05-16, Zerberus)

Wenn Chris ein Problem schildert das Coda lösen kann: Supervisor baut einen Coda-Prompt (.md-Datei) statt Chris Terminal-Befehle zu geben|Auch "nur ein Befehl" ist einer zu viel|Die Frage ist immer: "Kann Coda das selbst?" — Antwort ist in 95% der Fälle ja

**Anlass:** Zerberus 2026-05-16 — die Trennung Supervisor (plant, prüft, promptet) vs Coda (implementiert, testet) wird brüchig, wenn der Supervisor "nur einen kleinen Befehl" an Chris gibt. Das OBERSTE GEBOT gilt für beide Rollen: weder Coda-im-Code noch Supervisor-im-Chat delegieren Terminal-Arbeit an Chris.

**Konkretes Pattern für Supervisor:** wenn ein Schritt mehr als "Browser öffnen, klicken, sehen" verlangt → Coda-Prompt als `.md`-Datei (FEATURE_REQUEST oder Mjölnir-Auftrag), nicht ein Inline-PowerShell-Snippet im Chat.

---

## Multi-Session-Status-Header für mjolnir.md (2026-05-17, Zerberus B-mjolnir-multisession)

mjolnir.md hat IMMER einen STATUS-Header als ERSTEN Block|STATUS = FERTIG | IN_ARBEIT | BLOCKIERT|Pflichtfelder: STATUS, AUFTRAG, FORTSCHRITT, NÄCHSTE SESSION|Bei IN_ARBEIT: WARNUNG-Block fett oben + FEATURE_REQUEST NICHT umbenennen|Conditional Lifecycle: Rename FEATURE_REQUEST → _ERLEDIGT.md nur bei STATUS=FERTIG|QUEUED-Pattern: neuer FEATURE_REQUEST während IN_ARBEIT → _QUEUED.md, alter bleibt|Schlüsselwort-Whitelist ist maschinell auswertbar

**Anlass:** Lange Mjölnir-Aufträge brauchen oft mehrere Coda-Sessions (Token-Limit ~400k). Ohne sichtbaren Status-Block am Anfang der mjolnir.md kann Chris nicht zwischen Teil-Erfolg ("Phase X erledigt") und Komplett-Abschluss unterscheiden. Folge-Risiko: Chris sieht "Phase X erledigt", denkt "fertig", schickt neuen Request über Mjölnir → überschreibt den noch laufenden FEATURE_REQUEST → alter Auftrag bleibt halb fertig liegen.

**Lösung in drei Schichten:** (1) Pflicht-Status-Header als ERSTER Block — Chris sieht beim ZUSAMMENFASSUNG-Fetch sofort `STATUS: IN_ARBEIT` und weiß: noch nicht durch, kein neuer Request. (2) Conditional Lifecycle für FEATURE_REQUEST — nur bei STATUS=FERTIG umbenennen zu _ERLEDIGT.md, sonst unverändert lassen damit die nächste Session ihn erneut aufnimmt. (3) Überschreibungs-Schutz beim Session-Start — wenn neuer FEATURE_REQUEST + alter mit STATUS=IN_ARBEIT + abweichender Kurzname: neuer Request wird zu _QUEUED.md, alter aus mjolnir.md rekonstruiert, alter zuerst fertig, dann QUEUED.

**Lesson generalisierbar:** Wenn ein Single-Slot-State-File mehrere Iterationen über mehrere Sessions tragen muss, braucht es einen sichtbaren Lifecycle-Marker als ersten Block — nicht im Body versteckt, weil Body je nach Token-Budget gekürzt wird. Pflicht-Format mit Schlüsselwort-Whitelist (FERTIG | IN_ARBEIT | BLOCKIERT) macht das maschinell auswertbar. Conditional Lifecycle-Aktionen (Rename nur bei FERTIG) verhindern, dass ein abgebrochener Auftrag fälschlich als erledigt erscheint.

---

## Selbsttest-Pflicht für Workflow-Änderungen (2026-05-17, Try_Faulheits_catch)

Workflow-Änderungen brauchen dreiphasigen Selbsttest VOR Push|Phase A: Pattern in der Quelle erzeugen|Phase B: zweite Session/Sub-Agent simuliert frische Coda-Aufnahme|Phase C: Konflikt provozieren und prüfen ob Schutz greift|Phase D: Aufräumen + Listing|Auf "Coda hat es ja so geschrieben" zu hoffen ist KEIN Selbsttest|Hoffnung ≠ Verifikation

**Anlass:** Wiederholte mjolnir-Bugs (B-072, B-mjolnir-fix, B-mjolnir-fix-2, B-mjolnir-multisession) zeigen: Workflow-Regel im Text reicht nicht — Coda muss in derselben Session das Pattern selbst durchspielen, sonst klatscht der nächste Bug zurück mit derselben Wurzelursache. „Es steht doch im MARATHON_WORKFLOW" reicht nicht, wenn die nächste Session unter Token-Druck genau die Stelle überspringt.

**Phase-Schema (generalisierbar):** A = Setup (Datei/Zustand erzeugen, der das Pattern triggert), B = Replay (frischer Kontext liest+macht weiter, simuliert per Sub-Agent oder neuer Session), C = Adversarial (gegnerische Aktion, prüft ob Schutz greift — z.B. zweiter FEATURE_REQUEST während IN_ARBEIT), D = Cleanup (alle Test-Artefakte weg, Listing verifiziert Sauberkeit). Ohne C ist der Test lediglich Happy-Path und übersieht genau die Lücke, die der Bug ursprünglich ausgenutzt hat.

**Backstop:** Bei jedem Workflow-relevanten FEATURE_REQUEST steht „Selbsttest-Pflicht" als eigener Schritt im Auftrag. Bei Lessons-Sync für Workflow-Themen ebenfalls. Wenn Selbsttest nicht möglich (z.B. echtes Multi-Session-Verhalten nur über Tage prüfbar), Surrogat per Sub-Agent dokumentieren — kein Skip.

---

## Naming-Konvention für FEATURE_REQUEST-Dateien (2026-05-17, aufraeumarbeiten-post-catch)

```
NAMING|FEATURE_REQUEST_{kurzname}.md|kurzname = kebab-case-aus-FEATURE_REQUEST-Frontmatter|niemals Projektname als Filename|bei Umbenennung Lifecycle: kurzname-suffix bleibt erhalten (*_ERLEDIGT.md, *_QUEUED.md)
```

**Anlass:** Die faulheits-catch-integration-Session legte ihren Auftrag als `FEATURE_REQUEST_CLAUDE.md` ab — also Projektname statt Kurzname. Bei mehreren parallelen Aufträgen in einem Projekt (insbesondere bei QUEUED-Pattern, wenn ein zweiter Request während IN_ARBEIT eintrifft) wäre die Datei nicht eindeutig identifizierbar. Der Frontmatter-Kurzname (z.B. `faulheits-catch-integration`, `aufraeumarbeiten-post-catch`) ist die kanonische Quelle.

**Regel:** Filename folgt strikt dem Pattern `FEATURE_REQUEST_{kurzname}.md` (kebab-case, kein Leerzeichen, keine Großbuchstaben). Beim Lifecycle-Übergang bleibt der Kurzname-Teil erhalten: `FEATURE_REQUEST_{kurzname}_ERLEDIGT.md` bei STATUS=FERTIG, `FEATURE_REQUEST_{kurzname}_QUEUED.md` bei Konflikt mit laufendem IN_ARBEIT-Auftrag. Projektname (`CLAUDE`, `ZERBERUS`, ...) gehört NIEMALS in den Filename — das Verzeichnis sagt das Projekt, der Filename sagt den Auftrag.

**Backstop:** Kommentar-Header im `templates/FEATURE_REQUEST_TEMPLATE.md` und Hinweis in `SUPERVISOR_KODEX.md` Sektion „Was Supervisor IMMER muss". Bestehende Files mit alter Konvention (z.B. `FEATURE_REQUEST_CLAUDE_ERLEDIGT.md`) bleiben unangetastet — Historie wahren, nicht rückwirkend umbenennen.

---

## Die 6 Faulheits-Catches — Quick Reference

Kanonische Liste (Stand 2026-05-17, faulheits-catch-integration). Jeder Catch verweist zurück auf die ausführliche Sektion oben.

1. **OBERSTES GEBOT** — Coda terminalisiert nichts was Coda kann. Kein git/pytest/pip/robocopy/npm an Chris.
2. **mjolnir.md PFLICHT am Session-Ende** — Single-Slot-Round-Trip, ausnahmslos, gleichrangig mit HANDOVER und Push.
3. **Worktree-Branches selbst auf main mergen** — Kein „Schritt 0 für Chris", Coda macht ff-merge oder rebase selbst.
4. **Supervisor baut Coda-Prompts statt Terminal-Befehle** — Auch „nur ein Befehl" im Chat ist einer zu viel.
5. **Multi-Session-STATUS-Header + QUEUED-Pattern** — mjolnir.md mit STATUS-Block als erster Zeile, FEATURE_REQUEST während IN_ARBEIT wandert zu _QUEUED.md.
6. **Selbsttest-Pflicht für Workflow-Änderungen** — Dreiphasig (A Setup, B Replay, C Adversarial, D Cleanup). Hoffnung ≠ Verifikation.

Anlass-Blöcke + Lesson-Generalisierungen siehe oben in den jeweiligen Sektionen.

---

## Selbsttest-Pattern (Phase A/B/C/D — prosaisch)

Workflow-Änderungen sind erst dann „durch", wenn ihr Pattern in derselben Session einmal end-to-end gegen sich selbst antritt. Vier Phasen, fest:

**Phase A — Setup.** Erzeuge in `%TEMP%\<auftragsname>_test\` (oder `/tmp/...`) den Zustand der den neuen Schutz auslösen müsste. Beispiel: lege eine `mjolnir.md` mit STATUS=IN_ARBEIT an, kopiere ein Dummy-FEATURE_REQUEST hinein, ersetze alle `{PLATZHALTER}`. Verifiziere per Listing+Read, dass Setup wirklich den gewünschten Zustand zeigt — keine Platzhalter mehr, alle Pflichtfelder gefüllt.

**Phase B — Replay (frischer Kontext).** Starte einen Sub-Agent oder eine zweite Coda-Instanz mit dem Auftrag „du bist eine frische Session in diesem Verzeichnis, lies das Bootstrap-README und führe die Standardschritte aus". Beobachte ob:
- die globalen Files (GLOBAL_LESSONS, SUPERVISOR_KODEX) erkannt werden,
- die Templates gefunden+verstanden werden,
- keine Terminal-Befehle an Chris vorgeschlagen werden,
- bei vorhandenem STATUS=IN_ARBEIT der laufende Auftrag korrekt rekonstruiert wird statt überschrieben.

**Phase C — Adversarial (Konflikt provozieren).** Erzeuge gegen den frischen Zustand eine gegnerische Aktion. Beispiel: lege während IN_ARBEIT einen zweiten FEATURE_REQUEST mit anderem Kurznamen ab. Prüfe ob der Schutz greift (z.B. neuer Request landet in `_QUEUED.md`, alter bleibt unangetastet). Wenn Schutz NICHT greift, ist die Workflow-Änderung nicht fertig — zurück zu Setup, Lücke schließen.

**Phase D — Cleanup.** Lösche das gesamte Test-Verzeichnis. Verifiziere per Listing der Working-Tree-Root, dass kein `*_test*`, `bootstrap_test/`, `*_QUEUED.md` von Phase C übrig ist. Test-Artefakte dürfen nicht in den Commit wandern.

Surrogat-Regel: wenn echtes Multi-Session-Verhalten nur über Tage testbar ist (z.B. Token-Reset, Cache-TTL), dokumentiere das Surrogat (Sub-Agent simuliert Token-Reset) — aber kein Skip.

---

## Bibel-Format Cheat Sheet

„Bibel-Format" = Maschinen-lesbares Pipe-Format für Lessons, Templates, Status-Header. Eine Zeile pro Lesson, Felder mit `|` getrennt. Anlass+Begründung+Generalisierung in **fett-prosaischen Folge-Absätzen** darunter — Maschine ignoriert Prosa, Mensch findet Kontext.

**Pipe-Zeile Aufbau (Lessons):**
```
{Kerne Regel als Imperativ}|{Negativ-Anti-Pattern}|{Pattern/Recipe}|{Backstop-Location}|{Konsequenz bei Verstoß}
```

**Pipe-Zeile Aufbau (Status-Header mjolnir.md, erste Zeile):**
```
STATUS|{FERTIG|IN_ARBEIT|BLOCKIERT}|{AUFTRAG}|{FORTSCHRITT X von Y}|{NÄCHSTE SESSION}
```

**Pipe-Zeile Aufbau (KODEX-Zeile, Datei-Header):**
```
KODEX|für {Rolle}|gilt für {Scope}|{Verstoßes-Reaktion}
```

**Was Pipe-Format kann:**
- maschinell parse-bar (split auf `|`)
- kompakt — eine Lesson = eine Zeile + 2-4 Prosaabsätze
- visuell sortier-bar (greppen nach `OBERSTES GEBOT|`, `KODEX|`, `STATUS|`)

**Was Pipe-Format NICHT kann:**
- ausführliche Geschichte erzählen (dafür gibt's die Anlass-Absätze)
- bedingte Logik (if/else gehört in Prosa)
- Mensch-freundlich für Whisper-Eingabe (dafür Prosa-Files wie BOOTSTRAP_README.md)

**Regel:** Bibel-Format für Files die Maschinen UND Menschen lesen (GLOBAL_LESSONS.md, mjolnir.md, KODEX-Files). Reine Prosa für Files die NUR Menschen lesen (BOOTSTRAP_README.md, FEATURE_REQUEST-Anhänge). Niemals mischen innerhalb einer Datei — entweder Pipe-Format-Zeile oder Prosa-Absatz, klar getrennt.
