lessons whisper-transcription | maschinen-only | schema: wall_signatur | kategorie | fix | kontext | quelle

wall_signatur | user-input per sprache diktiert, intention priorisieren nicht wortlaut, phonetische fehler wortdreher fehlende satzzeichen
kategorie | whisper/transkription
fix | intention priorisieren | bei eindeutigem kontext still korrigieren, bei echter mehrdeutigkeit nachfragen
kontext | sprach-diktierter input
quelle |

wall_signatur | repetitionen in transkription sind whisper-bug nicht user-absicht, bekannte artefakte "Cloud Code"→Claude Code "Stadt"→start.bat
kategorie | whisper/transkription
fix | repetitionen als whisper-bug behandeln | bekannte fehltranskriptionen projektspezifisch dokumentieren
kontext |
quelle |

wall_signatur | whisper halluzinations-loop langes audio >10min verliert faden, ffmpeg -f segment -segment_time 600
kategorie | whisper/chunking
fix | audio vorher in 10-min-chunks splitten: ffmpeg -f segment -segment_time 600
kontext | audio >10min
quelle |

wall_signatur | temperature=0 fakten-transkript weniger decoder-kreativitaet weniger halluzination
kategorie | whisper/params
fix | temperature=0 fuer fakten-transkripte
kontext |
quelle |

wall_signatur | vad no-context n-gram-filter reichen nicht gegen endlosschleife, chunk-splitting zuverlaessigste loesung
kategorie | whisper/chunking
fix | chunk-splitting ist die zuverlaessigste loesung gegen endlosschleifen
kontext | vad+filter allein reichen nicht
quelle |

wall_signatur | audio-format mp4/aac mono 44.1khz bester kompromiss, flac verlustfrei
kategorie | whisper/audio
fix | mp4/aac mono 44.1khz als kompromiss, flac wenn verlustfrei noetig
kontext |
quelle |

wall_signatur | WHISPER_CONDITION_ON_PREVIOUS_TEXT=false verhindert kontamination zwischen chunks
kategorie | whisper/chunking
fix | WHISPER_CONDITION_ON_PREVIOUS_TEXT=false setzen
kontext | chunk-basierte transkription
quelle |

wall_signatur | satz-deduplizierung, wort-repfilter faengt sentence-repetition nicht, zwei-stufig mikro makro detect_phrase_repetition detect_sentence_repetition
kategorie | whisper/dedup
fix | zwei-stufige dedup: mikro (detect_phrase_repetition, n-gramme bis 6 woerter), makro (detect_sentence_repetition, konsekutive saetze via (?<=[.!?])\s+-split) | erst mikro dann makro, case-insensitive, whitespace-collapsed, nicht-konsekutive duplikate erhalten (refrain-safe "A. B. A.")
kontext | whisper sentence-repetition
quelle | Zerberus P102,P113b
