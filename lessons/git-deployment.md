lessons git-deployment | maschinen-only | schema: wall_signatur | kategorie | fix | kontext | quelle

wall_signatur | start.bat call venv\Scripts\activate vor uvicorn
kategorie | git-deployment/start
fix | start.bat muss "call venv\Scripts\activate" vor uvicorn enthalten
kontext | windows-venv-start
quelle |

wall_signatur | spacy modell python -m spacy download de_core_news_sm
kategorie | git-deployment/deps
fix | spacy-modell einmalig manuell: python -m spacy download de_core_news_sm
kontext |
quelle |

wall_signatur | grosse dateien >100mb blockieren github-push, .gitignore *.exe *.bin modell-dateien, git filter-repo
kategorie | git-deployment/git
fix | vor erstem push .gitignore sauber aufsetzen (*.exe, *.bin, modelle) | nachtraeglich entfernen: git filter-repo
kontext | >100mb blockiert github-push
quelle | Zerberus Hotfix

wall_signatur | .env nie committen, in .gitignore
kategorie | git-deployment/security
fix | .env in .gitignore, nie committen, nicht in logs
kontext |
quelle |

wall_signatur | git push $LASTEXITCODE verifikation, bei fehler user informieren
kategorie | git-deployment/git
fix | nach jedem git push $LASTEXITCODE pruefen, bei fehler user auf deutsch informieren
kontext | powershell
quelle |

wall_signatur | git config credential.helper vor erstem push pruefen
kategorie | git-deployment/git
fix | vor erstem push einer session git config credential.helper checken
kontext |
quelle |

wall_signatur | powershell kein &&, befehle mit ; trennen oder einzeln
kategorie | git-deployment/powershell
fix | powershell kennt kein && | befehle einzeln oder mit ; trennen
kontext | windows-powershell
quelle |

wall_signatur | raw.githubusercontent cached aggressiv bis 5h+, staler fetch != fehlgeschlagener push
kategorie | git-deployment/github
fix | github-cdn raw.githubusercontent cached bis 5h+ → staler fetch ist kein push-fehler
kontext | raw-link-fetch direkt nach push
quelle |
