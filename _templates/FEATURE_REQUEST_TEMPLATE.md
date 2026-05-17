<!-- TEMPLATE | Kopie als FEATURE_REQUEST_{PROJEKT}.md ins Projekt-Root | Coda arbeitet diese Datei beim Session-Start als Priorität ab -->

# FEATURE_REQUEST: {Auftrags-Titel}

**Datum:** {YYYY-MM-DD}
**Auftraggeber:** Supervisor (Chat-Fenster) | Chris (direkt)
**Empfänger:** Coda
**Kurzname:** {kurz-eindeutig, kein Leerzeichen}
**Erwartete Dauer:** {N Sessions}

---

## Kontext

{Warum dieser Auftrag? 2-5 Sätze. Geschäftsmotivation, nicht „ich hab Lust". Wenn ein Vor-Auftrag existiert: Verweis darauf. Wenn eine Quelle/Konzept-Datei existiert: Pfad nennen.}

Quelle (falls vorhanden): `{Pfad zur Konzept-Datei}`

---

## Akzeptanzkriterien (TL;DR)

- [ ] {Kriterium 1 — binär abprüfbar}
- [ ] {Kriterium 2 — binär abprüfbar}
- [ ] {Kriterium N — binär abprüfbar}
- [ ] Selbsttest A-D durchgelaufen (bei Workflow-Themen Pflicht)
- [ ] Commit + Push erfolgt, `$LASTEXITCODE = 0` verifiziert
- [ ] `mjolnir.md` mit STATUS-Header geschrieben

---

## Schritt 01 — {Titel}

{Beschreibung. Konkrete Done-Definition am Ende.}

---

## Schritt 02 — {Titel}

{...}

---

## Schritt 0N — Selbsttest (Phase A-D, PFLICHT bei Workflow-Themen)

### Phase A — Setup
{Zustand erzeugen, der das neue Pattern triggert}

### Phase B — Replay (frischer Kontext)
{Sub-Agent oder zweite Session simuliert frische Coda-Aufnahme}

### Phase C — Adversarial (Konflikt provozieren)
{Gegnerische Aktion + Prüfung ob Schutz greift}

### Phase D — Cleanup
{Test-Artefakte löschen + Listing der Working-Tree-Root verifiziert Sauberkeit}

---

## Schritt 0M — Commit + Push

Branch: {main | worktree-Name}
Commits idealerweise getrennt:
1. `{feat|fix|refactor}({scope}): {1-Satz}`
2. ...

Push auf `origin/{branch}`. Verifiziere `$LASTEXITCODE = 0`.
Bei Fehler: in mjolnir.md unter BLOCKIERT dokumentieren, auf Deutsch.

---

## Schritt 0L — mjolnir.md schreiben

Überschreibe `{Projekt-Root}/mjolnir.md` mit STATUS-Header (FERTIG | IN_ARBEIT | BLOCKIERT) + Fortschritt + Was-Chris-physisch-tun-muss + Auftragshistorie.

Vorlage: `C:\Users\chris\Python\Claude\_templates\mjolnir_TEMPLATE.md`

---

## Wichtige Hinweise

- **Bibel-Format nutzen** für alle Maschinen-Files. **Prosa nutzen** für alle Menschen-Files. **Niemals mischen** innerhalb einer Datei.
- **Bei Konflikten oder Unklarheiten:** Nicht raten. In `DECISIONS_PENDING.md` festhalten und in mjolnir.md unter BLOCKIERT verweisen.
- **Quellen-Files** bleiben unverändert liegen. Verteilung geschieht über GLOBAL_LESSONS.md, SUPERVISOR_KODEX.md, _templates/ — nicht durch Verschieben der Ursprungsdatei.

---

```
LIFECYCLE|FERTIG: rename zu *_ERLEDIGT.md|IN_ARBEIT: Datei bleibt, mjolnir.md trägt STATUS|BLOCKIERT: Datei bleibt + Grund in DECISIONS_PENDING.md|QUEUED-Fall: neuer FEATURE_REQUEST während IN_ARBEIT → _QUEUED.md
```
