# Regex / Pattern-Matching — Bug-Tracker (Zerberus)

## Offen

### RX-001 ZDF-Halluzination nicht vollständig gefangen
**Severity:** Niedrig — kosmetisch
**Betrifft:** whisper_cleaner.json
**Erfasst:** 2026-04-19

Das bestehende Pattern `(?i)untertitelung des zdf \d{4}\.` erwartet einen Punkt am Ende. Die tatsächliche Halluzination kommt auch mit Komma oder ohne Satzzeichen: "Untertitelung des ZDF, 2020".

**Lösung:**
Pattern breiter machen: `(?i)untertitelung des zdf[,\s]*\d{4}[.]?` — und nicht nur am Zeilenanfang matchen sondern auch inline, weil Halluzinationen manchmal mitten im Text auftauchen.

---

## Erledigt

(noch leer)
