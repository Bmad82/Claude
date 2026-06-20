# AUFTRAG: Kaltlese & Audit dieses Repos

## Wer du bist
Du bist ein fremder Agent. Du kennst dieses Repository nicht und hast keinen
Kontext außer den Dateien selbst. Genau das ist der Sinn: Du bist der
Stellvertreter für einen Nachfolger, der dieses System zum ersten Mal kalt
lesen muss. Verstehst du den Aufbau allein aus den Dateien, ist die Architektur
lesbar. Wenn nicht, zeigst du genau, wo sie es nicht ist.

**Du arbeitest read-only. Ändere, verschiebe, lösche nichts. Nur lesen,
verstehen, berichten.**

---

## Phase 1 — Kaltlese (Discovery)
Ziel: Den Aufbau allein aus den Dateien rekonstruieren — ohne zu wissen, was
gebaut werden sollte.

> **Sperre für diese Phase:** Die Dateien `FEATURE_REQUEST_*.md` NICHT öffnen.
> Die enthalten die Absicht und würden deinen kalten Blick verfälschen. Erst in
> Phase 2.

Schritte:
1. **Überblick:** Liste alle Dateien, ihren Typ und — soweit erkennbar — ihren
   Zweck.
2. **Flow rekonstruieren:** Was ist der Eintrittspunkt? Welche Datei steuert
   was? Wie hängen die Teile zusammen? Zeichne den Daten- und Steuerfluss nach.
3. **Kernkonzepte benennen:** Welche Rollen tragen die verschiedenen Dokumente
   (Status-Logik, Templates, JSON-Strukturen, Übergabe-/Gedächtnis-Files)?
   Nur, was die Dateien belegen. **Nichts raten.** Wo du raten müsstest, schreib
   ausdrücklich „unklar".

Halte das Ergebnis als eigenes Artifact fest: **„Rekonstruierte Karte"** —
Struktur, Flow, Konzepte, plus eine ehrliche Liste:
*„Was war unklar / wo musste ich raten / welche Datei hat mir am wenigsten
verraten."*

---

## Phase 2 — Audit gegen die Absicht
Erst starten, wenn Phase 1 abgeschlossen und festgeschrieben ist.

Jetzt lies die `FEATURE_REQUEST_*.md`. Das ist, was gebaut werden sollte
(Ordner-Cleanup + Supervisor-Aufbau).

Prüfe:
1. **Abgleich Ist/Soll:** Deckt sich der Repo-Zustand mit den FRs? Was ist
   umgesetzt, was fehlt, was weicht ab? Was noch nicht gebaut ist, melde als
   **„offen"**, nicht als „falsch".
2. **Reihenfolge:** Wurde der Ordner-Cleanup VOR dem Supervisor-Aufbau gemacht?
   Falsche Reihenfolge = der Aufbau landet in Ordnern, die der Cleanup danach
   umsortiert.
3. **Interne Konsistenz:** Widersprüche, Dubletten, tote Referenzen.
4. **Absolutpfad-Falle (gezielt prüfen):** Such nach hart verdrahteten
   Absolutpfaden in Templates / Kodex / FR-Template (u.a. zu `GLOBAL_LESSONS`,
   `SUPERVISOR_KODEX`, `DECISIONS_PENDING`, `PROJECT_BOOTSTRAP_README`,
   `GIST_LINK`). Zeigt nach dem Cleanup noch alles dahin, wo es soll — oder ins
   Leere?

Halte das als zweites Artifact fest: **„Audit"** — getrennt von der Kaltlese.

---

## Output
Zwei klar getrennte Artifacts:
- **„Rekonstruierte Karte"** (kalt, ohne FR-Wissen)
- **„Audit"** (gegen die FRs)

Keine Schönfärberei. Wenn etwas unklar oder widersprüchlich ist, sag es
deutlich. Nichts am Repo verändern.
