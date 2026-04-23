# Whisper & Spracheingabe

## Transkriptions-Handling
- User-Input ist oft per Sprache diktiert — Intention priorisieren, nicht Wortlaut
- Phonetische Fehler, fehlende Satzzeichen, Wortdreher: still korrigieren wenn Kontext eindeutig, nachfragen wenn echt mehrdeutig
- Repetitionen in der Transkription sind Whisper-Bugs, nicht User-Absicht
- Bekannte Artefakte projektspezifisch dokumentieren (z.B. "Cloud Code" → Claude Code, "Stadt" → start.bat)

## Technische Lessons
- Halluzinations-Loop bei langem Audio: Whisper verliert bei >10 Min den Faden → Audio vorher in 10-Min-Chunks splitten (`ffmpeg -f segment -segment_time 600`)
- `temperature=0` für Fakten-Transkripte — weniger Decoder-Kreativität = weniger Halluzination
- VAD + no-context + n-gram-Filter reichen nicht immer → Chunk-Splitting ist die zuverlässigste Lösung gegen Endlosschleifen
- Audio-Format: MP4/AAC Mono 44.1kHz als bester Kompromiss. FLAC wenn verlustfrei nötig
- `WHISPER_CONDITION_ON_PREVIOUS_TEXT=false` verhindert Kontamination zwischen Chunks
- Satz-Deduplizierungs-Filter nötig — Wort-RepFilter fängt Sentence-Repetition nicht
- **Zwei-stufige Dedup-Pipeline:** Mikro (`detect_phrase_repetition`, N-Gramme bis 6 Wörter, Patch 102) plus Makro (`detect_sentence_repetition`, konsekutive ganze Sätze via `(?<=[.!?])\s+`-Split, Patch 113b). Erst Mikro, dann Makro — sonst werden Sätze mit internen Phrase-Loops falsch verglichen. Vergleich case-insensitive, whitespace-collapsed. NICHT-konsekutive Duplikate erhalten (Refrain-Safe: "A. B. A." bleibt) (Zerberus P113b)
