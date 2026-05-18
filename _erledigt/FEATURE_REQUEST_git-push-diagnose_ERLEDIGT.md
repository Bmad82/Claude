# AUFTRAG: Git-Push-Diagnose (DRINGEND)

## Problem
Drei aufeinanderfolgende Aufträge (repo-inventur, supervisor-briefing, repo-restrukturierung) meldeten "Push verifiziert via $LASTEXITCODE". GitHub zeigt aber weiterhin nur 1 Commit und die alte Repo-Struktur. Die Pushes kommen nicht an.

## Was du tun sollst

Führe ALLE folgenden Befehle aus und gib die **vollständige Ausgabe** jedes einzelnen zurück. Nichts weglassen, nichts zusammenfassen.

```bash
# 1. Aktueller Branch und Status
git status
git branch -vv

# 2. Remote-Konfiguration
git remote -v

# 3. Lokale Commit-Historie (letzte 10)
git log --oneline -10

# 4. Vergleich mit Remote
git fetch origin
git log --oneline origin/main..HEAD

# 5. Tatsächlicher Push-Versuch mit Verbose-Output
git push origin main --verbose 2>&1

# 6. Falls Push fehlschlägt — Credentials/Auth prüfen
git config credential.helper
git config user.name
git config user.email

# 7. Ist das überhaupt das richtige Repo?
pwd
ls -la .git/
cat .git/config
```

## Output
Alle Ausgaben in `GIT_DIAGNOSE.md` im Repo-Root. NICHT pushen (wäre ja sinnlos wenn Push kaputt ist). Stattdessen: Die komplette Ausgabe in mjolnir.md schreiben, damit Chris sie weiterleiten kann.

## Was du NICHT tun sollst
- Nicht raten was das Problem ist
- Nicht selbst fixen
- Nur Daten sammeln und zurückgeben
