# Try_Faulheits_catch.md (Konzept-Ursprung)

**Status:** Historisches Dokument. Operative Version siehe GLOBAL_LESSONS.md.
**Eingang:** Mai 2026 als Konzept-Dokument von Chris.
**Verteilung:** Inhalte sind in GLOBAL_LESSONS.md und SUPERVISOR_KODEX.md migriert.

---

## Hintergrund

Diese Datei war der Konzept-Ursprung für die Faulheits-Catches. Im Mai 2026 hat Chris die Liste der Catches plus Selbsttest-Pattern und Bibel-Cheat-Sheet als Konzept-Dokument eingebracht. Die ursprüngliche `Try_Faulheits_catch.md` existierte nur im Anthropic-Chat-Projekt-Speicher und wurde nie als Git-File angelegt — sie tauchte weder im Working-Tree noch in der Git-History auf, als die `faulheits-catch-integration`-Session sie suchte. Coda hat damals die 6 Catches aus existierenden Quellen rekonstruiert: 4 aus `GLOBAL_LESSONS.md` (OBERSTES GEBOT, mjolnir-Round-Trip, Worktree-Self-Merge, Supervisor-Prompts), 1 aus `lessons/zerberus_lessons.md` Commit `08c7e9e` (Multi-Session-Status-Header), 1 aus den Don'ts der FEATURE_REQUEST selbst (Selbsttest-Pflicht).

Diese kanonische Datei in `concepts/` verankert den Konzept-Ursprung dauerhaft auf der Platte, damit er nicht nur in Chat-Sessions verfügbar ist.

---

## Die 6 Faulheits-Catches (rekonstruierter Stand)

1. **OBERSTES GEBOT — Coda terminalisiert NICHTS was Coda kann.** Kein git/pytest/pip/robocopy/npm an Chris. Mechanische Terminal-Arbeit ist Coda-Pflicht.

2. **mjolnir.md PFLICHT am Session-Ende.** Single-Slot-Round-Trip, ausnahmslos. Ohne mjolnir.md-Update ist der Round-Trip kaputt — Chris sieht nicht ob ein Auftrag durch ist.

3. **Worktree-Branches selbst auf main mergen.** Kein „Schritt 0 für Chris". Coda macht ff-merge oder rebase selbst.

4. **Supervisor baut Coda-Prompts statt Terminal-Befehle.** Auch „nur ein Befehl" im Chat ist einer zu viel. Wenn ein Schritt mehr als „Browser öffnen, klicken, sehen" verlangt → Coda-Prompt als `.md`.

5. **Multi-Session-STATUS-Header + QUEUED-Pattern.** mjolnir.md mit STATUS-Block (FERTIG | IN_ARBEIT | BLOCKIERT) als erster Zeile. FEATURE_REQUEST während IN_ARBEIT wandert zu `_QUEUED.md` statt zu überschreiben.

6. **Selbsttest-Pflicht für Workflow-Änderungen.** Dreiphasig (Phase A Setup, B Replay, C Adversarial, D Cleanup). Hoffnung ≠ Verifikation. „Es steht doch im MARATHON_WORKFLOW" reicht nicht, wenn die nächste Session unter Token-Druck genau die Stelle überspringt.

---

## Selbsttest-Pattern (Phase A/B/C/D)

Workflow-Änderungen sind erst dann „durch", wenn ihr Pattern in derselben Session einmal end-to-end gegen sich selbst antritt. Vier Phasen, fest:

- **Phase A — Setup.** Zustand erzeugen, der den neuen Schutz auslösen müsste. Verifizieren per Listing+Read, dass das Setup wirklich den gewünschten Zustand zeigt.
- **Phase B — Replay (frischer Kontext).** Sub-Agent oder zweite Coda-Instanz mit dem Auftrag „du bist eine frische Session in diesem Verzeichnis, lies das Bootstrap-README und führe die Standardschritte aus". Beobachten ob globale Files, Templates und Schutz-Pattern erkannt werden.
- **Phase C — Adversarial (Konflikt provozieren).** Gegen den frischen Zustand eine gegnerische Aktion (z.B. zweiter FEATURE_REQUEST während IN_ARBEIT). Prüfen ob der Schutz greift. Wenn nicht: zurück zu Setup, Lücke schließen.
- **Phase D — Cleanup.** Test-Verzeichnis löschen. Listing der Working-Tree-Root verifiziert: kein `*_test*`, kein `*_QUEUED.md` von Phase C übrig.

Surrogat-Regel: wenn echtes Multi-Session-Verhalten nur über Tage testbar ist (z.B. Token-Reset, Cache-TTL), Surrogat per Sub-Agent dokumentieren — kein Skip.

---

## Bibel-Format Cheat Sheet

„Bibel-Format" = Maschinen-lesbares Pipe-Format für Lessons, Templates, Status-Header. Eine Zeile pro Lesson, Felder mit `|` getrennt. Anlass+Begründung+Generalisierung in fett-prosaischen Folge-Absätzen darunter — Maschine ignoriert Prosa, Mensch findet Kontext.

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

**Regel:** Bibel-Format für Files die Maschinen UND Menschen lesen (GLOBAL_LESSONS.md, mjolnir.md, KODEX-Files). Reine Prosa für Files die NUR Menschen lesen (BOOTSTRAP_README.md, FEATURE_REQUEST-Anhänge). Niemals mischen innerhalb einer Datei — entweder Pipe-Format-Zeile oder Prosa-Absatz, klar getrennt.

---

## Hinweis

Diese Datei ist **historisch**. Operative Updates der Faulheits-Catches, Selbsttest-Schemata oder Bibel-Format-Regeln erfolgen in `GLOBAL_LESSONS.md`. Wenn die Originalquelle (`Try_Faulheits_catch.md` aus Chris' Konzept-Pool) jemals als Volltext nachgeliefert wird, kann diese Datei mit dem Original abgeglichen werden — bis dahin ist sie die kanonische rekonstruierte Fassung.
