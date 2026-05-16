# LESSONS — Konsolidiert aus allen Supervisor-Chats (Stand: P49, 2026-05-15)

## Plattform / Betriebssystem
- IMMER explizit fragen welches OS bevor Architektur-Entscheidungen. Nie aus Projektkontext schlussfolgern. tmux/bash/systemd=Linux, PowerShell/.bat=Windows. Die Frage muss vom Supervisor kommen. (Linux→Windows-Pivot P22)
- Chris' Rechner ist Windows. Claude Code = Desktop-App + PowerShell CLI. Kein WSL, kein Linux, kein tmux.

## Claude CLI / Drift
- CLI-Drift ist wiederkehrende Falle: Anthropic benennt Flags um (--reasoning→--effort P40) UND rolliert Modell-ID-Snapshots ohne Warnung (P41). Aliase ohne Datum-Suffix (claude-opus-4-7) stabiler als Snapshots (claude-opus-4-7-20260401).
- Sanity-Check beim Server-Start: claude --help auf erwartete Flags parsen + Dummy-Aufruf pro Modell-Alias. (P40+P41)
- Headless-Prozesse (claude -p) brauchen Output-Logging in Datei. Ohne Log ist Debugging unmöglich wenn Prozess still stirbt. (P40)

## Backend / State-Machine
- ERROR_PATTERN-Regex: NUR spezifische Fehlerwörter. Nie generische Begriffe die in Erfolgs-Output vorkommen. "\bAPI\b" matched /api/health URLs → false positive. Schmale Pattern > breite Pattern. (P46)
- error_suspected und delay MÜSSEN visuell getrennt sein. Pulsieren vs statisch — minimale CSS-Änderung, großer UX-Gewinn. Gleiche Lampe für zwei States = Verwirrung. (P46/P47)
- Exit-Code 0 bei OS-Interaktion heißt NUR dass der Befehl nicht gecrasht ist — NICHT dass die App läuft. Get-Process auf Zielprozess prüfen. (P38)

## Frontend / PWA
- Cache-Bust (?v=NN) an CSS/JS-URLs ist PFLICHT bei jedem Frontend-Patch. Ohne das zeigt PWA alten Code. Zwei Stellen in index.html bumpen. (P47+)
- PWA auf 20:9 Phones: viewport-fit=cover + env(safe-area-inset-*) allein reicht nicht. Panel muss insgesamt in Viewport passen. Proportional straffen statt nur Padding draufpacken. (P45-P49)
- Letzte Einstellung (Projekt/Modell/Reasoning) in localStorage persistieren. Try/catch für iOS Private Mode. (P49)
- Sensorische UI-Elemente (Lampen, Timer, Status) IMMER live-polled. Statische Anzeigen ohne Backend-Anbindung sind wertlos. Jede Lampe braucht einen API-Endpunkt. (P49+)
- PWAs brauchen HTTPS. Tailscale-IP über HTTP reicht nicht — nur "Verknüpfung" statt "App installieren". tailscale cert liefert gültige Zertifikate, 90 Tage gültig. (P35/P39)

## Workflow / Supervisor-Coda-Kommunikation
- Supervisor-Chat hat KEINEN Einblick in Coda-Terminal-Sessions. Handover vom Menschen ist Pflicht bei jedem neuen Kontextfenster. Sonst arbeitet Supervisor gegen bereits gelöste Bugs. (P40-Duplikat)
- Gegenmaßnahme: Supervisor soll bei neuem Kontextfenster selbstständig letzte Projekt-Chats durchsuchen UND User nach Patch-Stand fragen. Erst danach Prompts bauen.
- Logfile ist die Wahrheit, nicht die Lampe. Drei Root Causes, selbes Symptom (rot→gelb <10s): P40 Flag-Rename (36B), P41 Modell-ID (159B), P46 Regex false positive. (P40-P46)
- Planung im Chat (billig) → Ausführung in Claude Code (teuer, hat Werkzeuge). Nicht mischen.

## Feature-Request-Workflow
- Dateiname immer mit Projektnamen: FEATURE_REQUEST_{PROJEKTNAME}.md. Nach Abarbeitung umbenennen zu _ERLEDIGT.md, nicht löschen. (P38)
- Reihenfolge: ERST Feature-Request speichern, DANN Session starten. Standardprompt prüft beim Start ob Datei existiert.
- Standardprompt: "Wenn eine FEATURE_REQUEST_{PROJEKTNAME}.md existiert, lies sie zuerst und arbeite sie als Priorität ab. Danach lies MARATHON_WORKFLOW.md und mach weiter."

## Mjölnir-Status-Datei (mjolnir.md)
- Coda schreibt am Session-Ende mjolnir.md ins Projektverzeichnis (5-10 Zeilen). Löscht sie beim nächsten Session-Start nach Einlesen.
- Wenn mjolnir.md nicht existiert: entweder Fehler-Abbruch oder bereits eingelesen.
- Konvention muss in CLAUDE.md jedes Mjölnir-gesteuerten Projekts stehen.

## Design / CSS
- CSS kann 70er-Industriepanel-Optik gut nachbauen (Metallverläufe, Glühbirnen-Glow, 7-Segment, Schrauben) — digitale Hommage, kein Fotorealismus.
- Browser rendern CSS-Effekte unterschiedlich. Chromium vs Firefox bei texturlastigem Design merklich anders.
- Drehregler-Winkelberechnung fehleranfällig — Knob-Rotation muss exakt zu Label-Positionen passen. Visueller Bug den Coda nicht selbst findet.
- Lampenfarbe im Aus-Zustand: Glas muss Farbe behalten (dunkelgrün, dunkelrot), nicht neutral-grau. Sonst Funktion nicht erkennbar.
- Design-Artifacts aus Claude.ai per "Send to local coding agent" kommen manchmal als unlesbare Binärdaten an. Textbeschreibung als Fallback IMMER mitliefern. (P42/P44)
- CSS-Overhaul immer als ZIP mit Original-Code schicken, nie nur Textbeschreibung. Iterationen gehen verloren wenn Coda nur Beschreibung kriegt. (P44)

## Claude Design (Workflow)
- Claude Design für CSS-Overhauls effektiver als Chat-Artifacts. Echter Gewinn ist Live-Preview, nicht Zeichentools.
- Token-effizient nutzen: NICHT im Design-Tool diskutieren. Strategie im Supervisor-Chat, dann mit fertiger Korrekturliste reingehen. Supervisor-Executor-Modell gilt auch hier.
- Claude Design kann CSS-Dateien direkt als Projektdatei aufnehmen (kein Paste nötig). Screenshots + CSS + Brief = vollständiger Kontext.
- Iteratives Design in 3-4 Runden: R1=Grundstruktur+Stil, R2=Sprache+Detail, R3=Feinschliff, R4=Politur. Jede Runde braucht "NICHT ANFASSEN"-Liste, sonst verschlimmbessert er gute Elemente.
- Gemini-generierte Referenzbilder taugen als Ziel-Ästhetik. Bild + "das ist das Ziel" funktioniert als Briefing.

## Sprache / UI
- Deutsche UI konsequent. Eigennamen (RustDesk, KDE Connect) und Fachbegriffe (Reset, YOLO) bleiben. "Session"→"Sitzung", "Active Dir"→"Projektpfad", "AI"→"KI".
- Whisper-Transkriptions-Artefakte in Projektlisten prüfen ("Klauder" statt "Claude"). (P40)

## Worktree / Git
- Claude Code erstellt pro Session neuen Git-Worktree. Alte bleiben liegen → blockieren Branch-Checkouts. Lösung: Am Session-Ende commit→push→merge in main. (P38)
- Wenn Worktree-Checkout blockiert: git worktree prune dann git checkout. Nicht rmdir (PowerShell-Syntax anders als CMD).
- Aufräum-Sequenz in CLAUDE.md als Pflicht-Regel, nicht optional.
- Hauptpfad-Worktree dauerhaft auf main. Merges direkt im Hauptpfad: git -C <pfad> merge --ff-only <branch>. (P38/P39)

## Windows-spezifisch
- PowerShell ≠ CMD. rmdir /s /q → Remove-Item -Recurse -Force.
- RustDesk: C:\Program Files\RustDesk\rustdesk.exe
- KDE Connect: UWP/Store-App, Pfad wandert. Dynamisch via Get-AppxPackage auflösen, nicht hartcoden.
- subprocess + PowerShell: komplexe Befehle mit try/catch als ein String → Probleme. Aufruf-Methode prüfen.
- PYTHONIOENCODING=utf-8 im Startskript setzen, sonst Unicode-Bruch auf cp1252.

## Smoke-Tests
- UI-Elemente die verbunden sind (Drehregler→Anzeige, Button→Lampe) im Smoke-Test auf Verbindung prüfen, nicht nur Einzelteile.
- Headless-Session-Start: nach Start 5s warten, dann PID + Logfile-Größe prüfen. Wenn Log 0 Byte oder <50 Byte → sofort Inhalt lesen statt weiter warten.

## Architektur-Prinzipien
- Start mit vollem Feature-Set und runterschneiden, nicht von MVP hochbauen. Chris' explizite Design-Philosophie.
- Handy first: 48px Touch-Targets (44px Minimum), kein Hover-UI, Split-Screen muss gehen, Portrait UND Landscape.
- YOLO-Modus (--dangerously-skip-permissions) ist immer an.
- Immer prüfen was die Plattform schon kann bevor Custom-Features gebaut werden (Anthropic Remote Control entdeckt → Scope-Pivot).
