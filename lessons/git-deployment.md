# Git & Deployment

- `start.bat` muss `call venv\Scripts\activate` vor uvicorn enthalten
- spaCy-Modell einmalig manuell: `python -m spacy download de_core_news_sm`
- Große Dateien (>100 MB) blockieren GitHub-Push — vor dem ersten Push `.gitignore` sauber aufsetzen (*.exe, *.bin, Modell-Dateien). Nachträglich entfernen: `git filter-repo` (Zerberus Hotfix)
- `.env` niemals committen — in `.gitignore` und im Kopf behalten
- Git-Push-Verifikation: `$LASTEXITCODE` nach jedem Push prüfen, bei Fehler User informieren
- Git-Credential-Prüfung: `git config credential.helper` vor erstem Push in einer Session checken
- PowerShell: kein `&&` — Befehle einzeln oder mit `;` trennen
- GitHub CDN (`raw.githubusercontent.com`) cached aggressiv (bis 5+ Stunden) — staler Fetch ≠ fehlgeschlagener Push
