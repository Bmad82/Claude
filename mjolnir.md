# mjolnir.md — Claude (Meta-Layer)

```
STATUS|FERTIG|AUFTRAG: faulheits-catch-integration|FORTSCHRITT: 1 von 1 Session / alle 8 Schritte durch|NÄCHSTE SESSION: entfällt (FERTIG)
```

**STATUS:** FERTIG
**AUFTRAG:** faulheits-catch-integration
**FORTSCHRITT:** 1 von 1 Session | alle 8 Schritte durch (Schritte 01-08 aus FEATURE_REQUEST_CLAUDE.md)
**NÄCHSTE SESSION:** entfällt (FERTIG)

---

## Was Chris physisch tun muss

- Auf dem Handy nach Push prüfen ob Repo grün ist (1 Klick auf GitHub: https://github.com/Bmad82/Claude)
- Heute Abend: Demo mit Kumpel — Architekt füllt eine `PROJEKT_ANFRAGE.md` für ein neues Projekt aus, legt sie zusammen mit einer Kopie von `PROJECT_BOOTSTRAP_README.md` in einen frischen Ordner, sagt zur Coda-Session „go". Coda baut Skelett auf, fragt 3-5 Architektur-Fragen.

---

## Auftragshistorie

Anlässe & Erkenntnisse während der Session:

- **Schritt 01 (Bestandsaufnahme):** Quelle `Try_Faulheits_catch.md` existiert weder im Working-Tree noch in Git-History. 6 Catches aus existierenden GLOBAL_LESSONS.md (4) + zerberus_lessons.md Commit 08c7e9e (Multi-Session-Status-Header) + FEATURE_REQUEST-Don'ts (Selbsttest) rekonstruiert. Konflikt in `DECISIONS_PENDING.md` dokumentiert. Bestehender `templates/`-Ordner (8 Files, Commit 31b32f5) bleibt parallel zum neuen `_templates/` (4 Files) — auch in DECISIONS_PENDING als offene Frage.
- **Schritt 02 (GLOBAL_LESSONS.md):** 2 neue Catches als neue ## Sektionen angehängt (Multi-Session-Status-Header + Selbsttest-Pflicht), plus Quick-Reference + Selbsttest-Pattern + Bibel-Cheat-Sheet. Existierende 4 Catches unverändert.
- **Schritt 03 (SUPERVISOR_KODEX.md):** neu mit KODEX-Bibel-Header, NIE/IMMER-Listen (4+5), Prompt-Skelett, Eskalations-Regel.
- **Schritt 04 (_templates/):** 4 Templates (mjolnir, FEATURE_REQUEST, CLAUDE_PROJEKT, SUPERVISOR_PROJEKT) mit konsistentem Regel-0-Block + STATUS-Header-Pflicht.
- **Schritt 05 (PROJECT_BOOTSTRAP_README.md):** Anleitung für frische Coda-Sessions mit Verweis auf alle globalen Files.
- **Schritt 06 (Selbsttest A-D):** Phase A Setup (Templates kopiert, alle `{PROJEKT}`-Platzhalter ersetzt durch TESTPROJEKT, `grep -c "{PROJEKT}"` lieferte 0). Phase B Replay (Sub-Agent las README+GLOBAL_LESSONS+SUPERVISOR_KODEX, listete alle 4 Templates, wies `git status`-Anfrage zurück mit Verweis auf Catch #1+#4, kannte STATUS-Header-Logik). Phase C Adversarial (zweite Sub-Agent fand IN_ARBEIT-Status + abweichenden Kurznamen, wendete QUEUED-Pattern korrekt an, `mjolnir.md` blieb unangetastet). Phase D Cleanup (Test-Ordner gelöscht, Listing der Claude-Root zeigt keine Test-Artefakte). Alle 4 Phasen grün.
- **Schritt 07 (Commits + Push):** 4 thematische Commits direkt auf main: GLOBAL_LESSONS+DECISIONS_PENDING, SUPERVISOR_KODEX, _templates/, PROJECT_BOOTSTRAP_README. `git push origin main` exit code 0.
- **Schritt 08 (mjolnir.md):** diese Datei.

Verzeichnisstruktur am Session-Ende (`Claude/`):
```
DECISIONS_PENDING.md       (neu)
DESIGN.md                  (unverändert)
FEATURE_REQUEST_CLAUDE.md  → wird gleich zu _ERLEDIGT.md
GLOBAL_LESSONS.md          (6 Catches + Selbsttest-Pattern + Bibel-Cheat-Sheet)
LESSONS_KONSOLIDIERT.md    (unverändert)
PROJECT_BOOTSTRAP_README.md (neu)
README.md                  (unverändert)
SUPERVISOR_KODEX.md        (neu)
_templates/                (neu, 4 Files)
bugs/                      (unverändert)
lessons/                   (unverändert)
templates/                 (unverändert, 8 Files — bleibt parallel laut DECISIONS_PENDING)
```
