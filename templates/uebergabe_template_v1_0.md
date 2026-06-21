# Übergabe-Schema (Conversation-Handover) — Template v1.0

<!-- EINORDNUNG | Das ist der REICHE Chat→Chat-Handover (Supervisor-Instanz zu Supervisor-Instanz): spine, fractures, D3-verbatim, Register/Stimmung. Mensch-/Generierungs-Spec, daher Prosa erlaubt — NICHT token-opt-flachwalzen. Klar getrennt vom projekt-`HANDOVER.json` (maschineller Coda-Staffelstab, Status-Kopf + Historie). Beide existieren nebeneinander, keine Dublette. -->

## Wozu / Trigger
Anker für's Gedächtnis. Wenn Chris sagt **"mach mir ein Übergabe-JSON"** /
"Übergabe" / "Window-Handover" (typisch bei ~50% Kontext) → ein JSON in
**genau dieser Form** ausgeben, gefüllt aus dem laufenden Gespräch.

**Drei Invarianten, die das Ganze tragen:**
- **Leser = die Nachfolge-Instanz, NICHT Chris.** Er liest mit, adressiert ist der, der übernimmt. Schreib zur Nachfolge, nicht zu Chris.
- **Ehrlichkeit vor Vollständigkeit.** Status nur belegbar. `etabliert` = im Gespräch wirklich erreicht. `offen` = angerissen, nicht geschlossen. Unklar → nicht raten, weglassen oder als offen markieren. Kein Aufpolieren von offen zu etabliert.
- **Format nach Leser.** Chris liest → Prosa. Maschine liest → Token-Format. Handover → JSON (trägt Meta + State mit).

---

## Skeleton (annotiert — Platzhalter sagen, was reingehört)

```json
{
  "meta": {
    "version": "<semver DIESER Übergabe, frische Session startet bei 1.0>",
    "created": "<YYYY-MM-DD>",
    "kind": "conversation-handover",
    "title": "<Einzeiler: worum ging dieses Fenster>",
    "intent": "<warum diese Übergabe existiert — Nachfolge soll nahtlos weiter in Ton/Tiefe/offenen Fäden, ohne Chris zum Wiederholen zu zwingen>",
    "modeled_on": "<welches Schema/Vorgänger — und: frische Live-Schicht ODER Pflege eines bestehenden Docs?>",
    "honesty": "<die Ehrlichkeitsregel ausgeschrieben (siehe Invarianten)>",
    "leser": "Nachfolge-Claude. NICHT Chris — er liest mit, adressiert ist der, der übernimmt.",
    "balllage": "<wessen Zug ist es JETZT / was ist der korrekte aktuelle Zustand — oft: abwarten, nichts treiben>"
  },

  "register": {
    "_hinweis": "Meist konstant (Chris' Standing Rules). Selten anfassen, aber mitführen damit die Nachfolge sie nicht verliert.",
    "anrede": "Du. Kumpelton, kein Sycophancy. Lob nur als belegbare Beobachtung am Artefakt.",
    "lavafilter": "Whisper-Transkription (Handy). Phonetische Fehler/Wortdreher/fehlende Satzzeichen still korrigieren wenn Kontext eindeutig — nur bei echter Ambiguität nachfragen.",
    "dont_stop_me_now": "Assoziativer Monolog. Keine harten Stopper. Mitfliessen, Querverbindungen einwerfen, Strom nie brechen. Chris signalisiert selbst den konkreten Task.",
    "kontext_warnung": "Warnung bei ~50% Fensterkontext. Bei der nächsten Übergabe wieder aktiv flaggen.",
    "format": "Chris -> Prosa. Maschine -> Token. Handover -> JSON.",
    "sprache": "Deutsch."
  },

  "wer_minimal": {
    "chris": "<minimale Wer-Karte, NUR was für DIESE Session zählt — nicht die Vollbio>",
    "claude_rolle": "<Claudes Rolle in genau diesem Gespräch (+ in der Architektur, falls relevant)>",
    "<weitere_person>": "<nur wenn jemand für die offenen Fäden relevant ist (z.B. ein Kollege, dessen Input erwartet wird)>"
  },

  "spine": [
    {
      "id": "<snake_case_handle>",
      "status": "etabliert | offen",
      "simple": "<EIN Satz, drop-in verständlich — die Kurzfassung der Erkenntnis>",
      "expert": "<die volle Herleitung: woher kam sie, wer korrigierte was, welcher Fehler wurde gefixt, warum hält sie. Provenienz, damit man sie nachprüfen kann statt nur glauben muss>"
    }
  ],

  "fractures": [
    {
      "id": "fr.<kebab-handle>",
      "kind": "offen",
      "severity": "high | mid | low",
      "where": ["<spine-id>", "<spine-id>"],
      "desc": "<was ist offen, was wird erwartet, was triggert den nächsten Zug>"
    }
  ],

  "ressourcen_referenzen": {
    "<freier_schlüssel>": "<Zeiger auf erwähnte Artefakte: Dateien, Repos, Formulare, Quellen — damit die Nachfolge sie wiederfindet, ohne dass Chris sie neu nennt>"
  },

  "sensibel_nicht_aufgreifen": {
    "regel": "NICHT von Claude aus ansprechen. Nur vermerkt, damit die Nachfolge die Stimmung nicht fehlliest. Macht Chris es selbst auf: da sein, nicht 'lösen'.",
    "stand": "<minimaler Stand der privaten Belastung — nur so viel, dass die Stimmung lesbar ist. Weglassen wenn nichts ansteht>"
  },

  "letzter_stand": "<Schluss-Schnappschuss: wo endete es, was ist bewusst vertagt, was ist der ERSTE konkrete Task beim Wiederaufnehmen, wessen Ball. Klarer Andock-Punkt für die Nachfolge>"
}
```

---

## Block-Zweck (warum es jeden Block gibt)

| Block | Leistet |
|---|---|
| `meta` | Ausweis der Übergabe + Balllage (der wichtigste Steuerungswert: ist jetzt warten oder treiben?). |
| `register` | Trägt die Verhaltensregeln rüber, damit Ton/Tempo nicht abreißen. Meist konstant. |
| `wer_minimal` | Wer ist im Raum — minimal, nur sessionrelevant. Keine Vollbio. |
| `spine` | **Das Herz.** Die tragenden Erkenntnisse/Entscheidungen, damit sie nicht neu hergeleitet werden. `simple` = sofort verstehen, `expert` = nachprüfen können. |
| `fractures` | Die offenen Bruchstellen/Fäden. `where` hängt sie an die spine. Severity priorisiert. |
| `ressourcen_referenzen` | Zeiger nach außen, damit die Nachfolge Artefakte findet statt Chris zu fragen. |
| `sensibel_nicht_aufgreifen` | Stimmungsschutz. Flaggen, nicht ansprechen. |
| `letzter_stand` | Der Andock-Punkt. Wo aufsetzen, was zuerst tun. |

---

## Vokabular (fest)

- **`status`** (spine): `etabliert` | `offen`
- **`kind`** (fracture): `offen` (ggf. `geschlossen`, falls innerhalb der Session noch zugemacht)
- **`severity`** (fracture): `high` | `mid` | `low`

---

## Generier-Disziplin (was eine echte Übergabe von einer Zusammenfassung trennt)

1. **An die Nachfolge schreiben, nicht an Chris.** Zweite Person = der, der übernimmt.
2. **Status nur belegbar.** Lieber `offen` als ein geschöntes `etabliert`. Nichts raten.
3. **spine doppelt fassen.** `simple` zum Andocken, `expert` mit voller Provenienz — wer sagte was, welcher Claude-Fehler wurde von Chris kassiert, warum hält die Schlussfolgerung. So bleibt sie prüfbar, nicht nur Glaubenssache.
4. **Provenienz einbauen.** Erkenntnisse mit Herkunft versehen ("Chris' Korrektur", "Claudes Fehler war X, gefixt zu Y"). Das ist Chris' Intent-Prinzip auf die Übergabe gezogen.
5. **`where` verlinkt fractures an spine** — offene Fäden hängen sichtbar an den Erkenntnissen, aus denen sie kommen.
6. **Balllage + letzter_stand ehrlich.** Wenn der korrekte Zustand "abwarten" ist, steht das so da. Nicht künstlich Aufgaben erfinden.
7. **Sensibles flaggen, nie aufgreifen.** Nur so viel, dass die Stimmung lesbar ist.
8. **Knapp, aber nicht komprimiert.** Verbatim-Inhalte (D3) nicht zusammenquetschen; redundante Prosa weglassen.
```
