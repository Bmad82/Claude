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

## Migrations-Roadmap (Phase 3)

1. Pro aktivem Projekt: Gist erzeugen (manuell via gh-CLI von Coda)
2. Pflichtfelder einfüllen aus dem aktuellen Repo-Stand
3. Diesen INDEX-Gist anlegen mit Verweisen auf Projekt-Gists
4. URL in Supervisor-Memories einpflegen (Chat-Setting)
5. CLAUDE_{PROJEKT}.md erweitern um „Live-State-Gist:"-Sektion mit URL
