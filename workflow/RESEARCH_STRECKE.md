# Research-Strecke — Prompt-Set + Ablauf (komplett)

Die vollständige Strecke der Fabrik von **Projektbrief** bis **workflow-ready aufgebautes Projekt**.
Sechs Stationen, fünf Prompts + ein Mensch-Gate. Alle Prompts model- und domänen-agnostisch:
die Domäne reist in den `{SLOTS}`, nie im Prompt-Text.

Jeder Prompt endet mit einem **Pflicht-Tail** = fester Output, der den Input der nächsten Station bildet.
Wird ein Schritt übersprungen, bricht die Kette (z. B. Roh-Research direkt in die Validation → validiert ins Leere).

> Status: Tabletop-validiert am echten Projekt „Pförtner" für Station 1–4 (Prompts liefen, Contract-Chain hielt).
> Station 5 (HITL) ist Betrieb. Station 6 (Bootstrap-Init) ist neu, strukturell, am echten Projekt noch ungetestet.
> Verfeinert wird die Strecke pro Projekt.

---

## Die Kette auf einen Blick

```
1  re.flach    Research flach      →  FÄDEN
2  re.tief     Research tief       →  ENTSCHEIDUNGSREIFE
3  re.synth    Synthese            →  DRAFT-PLAN + WAIT-Liste      (der früher fehlende Knoten)
4  re.planval  Plan-Validation     →  VALIDIERUNGS-BEFUND + ROUTING
5  re.hitl1    HITL_1 (Mensch)     →  Freigabe / Loopback-Entscheid
6  bo.init     Bootstrap-Init      →  BOOTSTRAP-MANIFEST            (Projekt materialisiert)
```

## Was jede Station tut — Contract-Tabelle

| # | Station | frisst (Input) | liefert (Pflicht-Tail) | läuft automatisch weiter, wenn … | Mensch ran, wenn … (warum) |
|---|---|---|---|---|---|
| 1 | Research flach | Projektbrief | FÄDEN (3–7) | immer | nie |
| 2 | Research tief | Pass-1-Bericht + FÄDEN | ENTSCHEIDUNGSREIFE | immer | nie |
| 3 | Synthese | Tief-Bericht + ENTSCHEIDUNGSREIFE | DRAFT-PLAN + WAIT-Liste | immer | nie |
| 4 | Plan-Validation | DRAFT-PLAN (+ Beleg) | BEFUND + ROUTING | **jeder** Faden = `WEITER` | irgendein Faden ≠ `WEITER` (s. u.) |
| 5 | HITL_1 | BEFUND + ROUTING | Freigabe oder Loopback | — (ist der Mensch) | immer — letztes Tor vor Geld-Ausgabe |
| 6 | Bootstrap-Init | freigegebener DRAFT-PLAN + Asset-Ordner | BOOTSTRAP-MANIFEST | immer (self-sufficient) | nur bei STOPP-Befund (etwas fehlte) |

## Routing-Klassen (vergibt Station 4, pro Faden genau eine)

- **`WEITER`** — hält, oder wackelt-aber-tragbar → läuft automatisch weiter. Kein Mensch.
- **`LOOP_RESEARCH`** — Lücke wäre durch weiteren Research schließbar → **kein Auto-Loop**, ab an HITL. *Warum Mensch: Kosten — fette Research-Läufe sind teuer; ob das Budget fließt, entscheidet der Mensch.*
- **`GATE_MESSUNG`** — Lücke nur durch Messung/Test am Zielsystem schließbar → HITL, harter Halt. *Warum Mensch: physische Realität; kein LLM-Schritt löst das, ein Research-Loop liefe ins Leere.*
- **`GATE_BETREIBER`** — offene Betreiber-/Scope-Entscheidung → HITL. *Warum Mensch: Präferenz, keine technische Frage.*

## Reliability-Invariante

**Die Strecke hat keinen automatischen Rück-Loop.** Alles ≠ `WEITER` hält an und ruft den Menschen.
Eine Endlosschleife ist damit *strukturell* ausgeschlossen — nicht per Zähler gedämpft, sondern per Konstruktion unmöglich.
Die Maschine darf automatisch weiterlaufen, solange jeder Faden `WEITER` ist; sie darf **nicht** Research-Budget selbst auslösen, eine empirische Lücke wegrecherchieren wollen oder bei einem Kill-Shot durchwinken.

---

## 1 — ERST-RESEARCH · DURCHGANG 1 (flach / freies Netz)

*Knoten `re.flach`. Input: Projektbrief. Output: FÄDEN.*

```
ERST-RESEARCH — DURCHGANG 1 (flach / freies Netz)

Haltung: Du machst den allerersten, bewusst oberflächlichen Orientierungs-
Durchgang über ein Vorhaben. Du entscheidest nichts, validierst nichts,
entwirfst nichts. Du kartierst das Gelände — breit, schnell, ergebnisoffen.

[BRIEF]
{hier Bootstrap/Projektbrief einfügen}
[/BRIEF]

Liefere, locker in Prosa, ohne dich festzulegen:

1. Was wird hier eigentlich verlangt? Gib das erkennbare Ziel in eigenen
   Worten wieder — und benenne, was die Person dahinter vermutlich *wirklich*
   will. Markier die Stellen, wo erklärtes Ziel und echtes Bedürfnis
   auseinanderlaufen könnten.
2. Grober Scope-Umriss: was liegt plausibel drin, was draußen, was ist unklar.
   Skizze, keine Vollständigkeit.
3. Das Feld: welche Ansätze, Vorbilder, Muster gibt es für so etwas — breit
   gestreut. Optionen nennen, nicht bewerten, nicht auswählen.
4. Wohin führt das? Erster Eindruck: was ist leicht, was hart, was könnte
   Scope oder Kosten sprengen.

Eine Regel: Geh nirgends in die Tiefe, wähle keine Lösung. Wo du unsicher
bist, sag es offen statt es zu glätten. Nimm keine Domäne, keinen Stack,
keine Technologie als gegeben an.

Schließe mit — und nur das ist Pflicht-Format:

FÄDEN FÜR DIE TIEFBOHRUNG (3–7 Stück): die tragendsten offenen Fragen /
Unbekannten, die ein zweiter, tieferer Durchgang aufmachen soll. Jeder Faden
so formuliert, dass man ihn einem Modell einzeln als Fokus geben kann.
```

---

## 2 — TIEF-RESEARCH · DURCHGANG 2 (tief / Skalpell)

*Knoten `re.tief`. Input: Pass-1-Bericht + FÄDEN. Output: ENTSCHEIDUNGSREIFE.*

```
TIEF-RESEARCH — DURCHGANG 2 (tief / Skalpell)

Haltung: Du bekommst das Ergebnis eines bewusst flachen ersten Durchgangs
plus eine Liste offener Fäden. Du kartierst nichts neu — das Gelände ist grob
bekannt. Du schneidest jeden Faden einzeln auf und denkst ihn so tief durch,
dass danach eine Entscheidung *möglich* wird. Du triffst sie nicht selbst, du
beurteilst den Plan nicht — du legst den Entscheidungsraum offen.

Behandle den ersten Durchgang als vorläufig, nicht als gesetzt. Wo er etwas
selbstsicher behauptet, ist das deine Einladung nachzubohren, nicht es
auszuschmücken.

[ERSTER DURCHGANG]
{vollständiger Bericht aus Durchgang 1 — als Briefing}
[/ERSTER DURCHGANG]

[FÄDEN]
{die Faden-Liste aus Durchgang 1 — deine Arbeitsagenda}
[/FÄDEN]

Pro Faden, der Reihe nach:

1. Die eigentliche Frage: formulier sie schärfer, als der erste Durchgang sie
   gestellt hat. Die harte Frage steckt oft eine Ebene tiefer als die gestellte.
2. Optionsraum: welche ernsthaften Wege gibt es? Echte Alternativen, nicht nur
   die naheliegende. Pro Weg: was er kostet, was er einbringt, wo er bricht.
3. Trade-offs: was gegen was steht. Wo eine Wahl hier eine Wahl woanders
   erzwingt.
4. Was bleibt offen: markier sauber, was sich ohne weiteren Input, ohne den
   Betreiber oder ohne echten Test NICHT klären lässt.

Danach einmal quer über alle Fäden:

- Kollisionen: widersprechen sich Fäden, überschneiden sie sich, fallen welche
  zu einem zusammen? Sag es.
- Neue Fäden: taucht beim Bohren etwas auf, das Durchgang 1 übersehen hat,
  benenn es als *Fund* — aber schmuggle keinen Scope rein.

Regeln (knapp, bindend):
- Bleib in der Recherche-Spur: du sammelst Wissen und legst Optionen frei. Du
  wählst keine Lösung und erklärst keinen Plan für gut oder schlecht. Das
  passiert danach woanders.
- Kalibrier die Tiefe: nicht jeder Faden ist gleich schwer. Triviales oder
  längst Gelöstes hakst du in einem Satz ab und sparst die Bohrkraft für die
  echten Brocken.
- Erfinde keine Zahlen, keinen Stack, keine Fakten, die nicht im ersten
  Durchgang stehen. Wo du spekulierst, sag dass du spekulierst.
- Keine Breite zurück. Nur Tiefe auf den gegebenen Fäden.

Schließe mit — und nur das ist Pflicht-Format:

ENTSCHEIDUNGSREIFE (eine Zeile pro Faden):
[Faden] → entscheidbar JA/NEIN · bei JA: Optionsraum in einem Satz · bei NEIN:
was genau noch fehlt · Flag, wenn es Scope, Kosten oder Machbarkeit berührt.
```

---

## 3 — PLAN-SYNTHESE  (der früher fehlende Knoten)

*Knoten `re.synth`. Füllt die Lücke zwischen `re.tief` und `re.planval`.*
*Input: Tief-Bericht + ENTSCHEIDUNGSREIFE. Output: DRAFT-PLAN + WAIT-Liste.*

> Ohne diesen Knoten springt die Kante direkt von Research auf Validation —
> Research liefert dann nur einen Entscheidungs-RAUM, niemand wandelt Optionen
> in eine Entscheidung. Genau hier sitzt der Wert. (Im Pförtner-Tabletop von
> DeepSeek gespielt — die Datei hieß „Evaluationsplan", ist aber der DRAFT-PLAN.)

```
PLAN-SYNTHESE — Optionsraum → Draft-Plan

Haltung: Du bekommst einen tiefen Research-Bericht und eine Liste mit
Entscheidungsreife pro Faden. Du recherchierst nicht, validierst nicht, baust
nicht. Du klappst den ausgebreiteten Optionsraum in EINEN festgelegten
Draft-Plan zusammen — für die entscheidbaren Fäden. Die nicht entscheidbaren
parkst du sauber als offene Entscheidung. Du schlägst vor; der Betreiber gatet.

[TIEF-DURCHGANG]
{vollständiger Bericht aus Durchgang 2}
[/TIEF-DURCHGANG]

[ENTSCHEIDUNGSREIFE]
{die Entscheidungsreife-Liste aus Durchgang 2}
[/ENTSCHEIDUNGSREIFE]

Aufträge:

1. Pro entscheidbarem Faden (JA): wähl genau eine Option. Nenn die Wahl in
   einer Zeile, plus den Ein-Satz-Grund, warum sie die Alternativen schlägt —
   *gestützt auf die Funde und Trade-offs des Berichts*, nicht auf neue
   Kriterien, die du dir ausdenkst.
2. Halte die fadenübergreifenden Kollisionen ein: wenn eine Wahl hier eine
   Wahl woanders erzwingt oder verbietet, mach die beiden konsistent und
   benenn die Abhängigkeit explizit.
3. Pro nicht entscheidbarem Faden (NEIN): rate nicht. Stell ihn als geparkte
   Entscheidung dar — was genau fehlt (Messung / Betreiber-Input / Test) — und
   nenn einen vorläufigen Default, damit der Build nicht blockiert.
4. Annahmen offenlegen: jede Wahl, die auf einer im Bericht unbewiesenen
   Behauptung ruht, markierst du — die Plan-Validation greift als Nächstes
   genau da an.

Regeln (knapp, bindend):
- Entscheide nur, was als entscheidbar markiert ist. Befördere keinen
  WAIT-Faden zur Wahl, nur damit es vollständig aussieht.
- Kein neuer Scope. Du klappst den gegebenen Raum zusammen, du weitest ihn
  nicht.
- Keine neuen Fakten/Zahlen. Was der Bericht nicht hergibt, ist eine Annahme —
  als solche kennzeichnen.
- Bleib aus dem Build raus: kein Code, keine Task-Zerlegung. Das ist Bootstrap.

Schließe mit — und nur das ist Pflicht-Format:

DRAFT-PLAN (eine Zeile pro Faden):
[Faden] → WAHL / oder GEPARKT · Begründung-in-einem-Satz / oder Was-fehlt ·
ANNAHME-Flag, wenn auf Unbewiesenem ruhend.

OFFENE ENTSCHEIDUNGEN (WAIT-Liste): die geparkten Fäden, je mit „braucht: X" —
das ist das Material für dein HITL_1-Gate.
```

---

## 4 — PLAN-VALIDATION  (adversarial, mit Routing)

*Knoten `re.planval`. Input: DRAFT-PLAN (+ Beleg). Output: BEFUND + ROUTING → HITL_1.*

> Gehärtete Fassung: vergibt pro Faden eine ROUTE-Klasse, damit das „Nein"
> maschinen-routbar wird und ein nicht-haltender Faden nicht die haltenden
> mitblockiert. (Im Pförtner-Tabletop von GPT gespielt; gehärtete ROUTE-Fassung
> noch nicht gegengetestet.)

```
PLAN-VALIDATION — adversariale Plan-Prüfung (mit Routing)

Haltung: Du bekommst einen Draft-Plan, der aus Research synthetisiert wurde —
möglicherweise hat er schon eine Schleife durchlaufen. Beurteile ihn frisch,
nimm keine früheren Fixes als gegeben. Du baust nichts, recherchierst nicht
neu, glättest nichts. Du greifst ihn adversarial an: Bias, blinde Flecken,
Logiklücken, unbelegte Annahmen, innere Widersprüche. Du gehst davon aus, dass
der Plan falsch ist, bis er es überlebt. Neu: für jeden nicht haltenden Faden
vergibst du eine Routing-Klasse, damit ein Overseer das Urteil OHNE Rückfrage
weiterleiten kann. Du lieferst ein Urteil zum Gaten — keinen Neuentwurf.

[DRAFT-PLAN]
{der aktuelle Draft-Plan — bei Loop-Runde: die re-synthetisierte Fassung}
[/DRAFT-PLAN]

[BELEG]
{die volle Evidenzbasis inkl. evtl. zweiter Research-Ergebnisse}
[/BELEG]

Aufträge:

1. Pro Entscheidung: ist die gewählte Option vom Beleg wirklich getragen, oder
   ruht sie auf einer Annahme — egal ob markiert oder stillschweigend
   reingeschmuggelt? Nenn das schwächste Glied.
2. Widersprüche jagen: kollidieren zwei Entscheidungen? Verletzt eine Wahl
   eine Randbedingung, die anderswo im Plan steht?
3. Blinde Flecken: was hat der Plan NICHT entschieden, das er vor dem Build
   entscheiden müsste? Welcher Fehlermodus ist unadressiert?
4. Geparkte Posten stressen: ist der WAIT-Grund echt — und vor allem: ist die
   Lücke RECHERCHIERBAR (ein weiterer Research-Pass schließt sie), EMPIRISCH
   (nur Messung/Test am Zielsystem schließt sie) oder eine BETREIBER-Wahl?
   Diese Unterscheidung bestimmt das Routing.
5. Kill-Shots: gibt es eine einzelne Entscheidung, die — wenn falsch — den
   ganzen Plan versenkt? Am lautesten flaggen.

Regeln (knapp, bindend):
- Du prüfst den PLAN, nicht Code. Keine Implementierung, keine Task-Zerlegung.
- Adversarial, nicht destruktiv: jeder Einwand zeigt konkret auf eine bestimmte
  Entscheidung. Kein vages „könnte problematisch sein".
- Kein Neuentwurf. Du legst das Loch offen, du füllst es nicht.
- Kein Gesamt-Veto per Default: ein tragender Faden, der gatet, blockiert NICHT
  automatisch die Fäden, die halten. Route jeden Faden einzeln.
- Erfinde keine Fakten. Annahme bleibt Annahme, kein erwiesener Fehler.
- Kalibrier: Angriffskraft in die tragenden Entscheidungen.

Routing-Klassen (genau eine pro Faden):
- WEITER          — hält, oder wackelt-aber-tragbar → geht zur nächsten Stufe.
- LOOP_RESEARCH   — Lücke durch einen weiteren Research-Pass schließbar →
                    HITL (kein Auto-Loop: Research ist teuer, Budget = Mensch).
- GATE_MESSUNG    — Lücke nur durch Messung/Test am Zielsystem schließbar →
                    HITL, harter Halt (ein Research-Pass liefe ins Leere).
- GATE_BETREIBER  — offene Betreiber-/Scope-Entscheidung → HITL.

Schließe mit — und nur das ist Pflicht-Format:

VALIDIERUNGS-BEFUND (eine Zeile pro Entscheidung):
[Faden/Entscheidung] → hält / wackelt / fällt · bei wackelt|fällt: der konkrete
Riss in einem Satz · KILL-SHOT-Flag wenn planentscheidend ·
ROUTE: WEITER | LOOP_RESEARCH | GATE_MESSUNG | GATE_BETREIBER

ROUTING-SUMME: wieviele Fäden WEITER, welche in welches Gate/Loop. Ein Satz, ob
der Plan TEILWEISE weiterlaufen kann (welche Fäden) oder ob ein Kill-Shot alles
bis zur Klärung anhält.
```

---

## 5 — HITL_1  (Mensch-Gate, kein Prompt)

*Knoten `re.hitl1`. Input: BEFUND + ROUTING. Output: Freigabe oder Loopback-Entscheid.*

Kein LLM-Schritt — das bist du. Hier landet **alles**, was Station 4 nicht als `WEITER`
durchgewunken hat, ausdrücklich auch `LOOP_RESEARCH`. Du entscheidest pro offenem Faden:

- **KEEP** — Wahl / vorläufigen Default akzeptieren.
- **EDIT** — bewusster Loopback zu Synthese (Wahl ändern, kein neuer Research) oder zu
  Research (du löst den teuren Research-Nachlauf aktiv aus).
- **WAIT** — geparkt lassen bis Messung / Betreiber-Input.

Freigabe an Bootstrap erst, wenn kein Faden mehr blockierend offen ist.

---

## 6 — BOOTSTRAP-INIT  (Projekt materialisieren)

*Knoten `bo.init`. Input: freigegebener DRAFT-PLAN + Asset-Ordner. Output: BOOTSTRAP-MANIFEST.*
*Strukturell gehalten — kein konkretes Ordnerlayout, das kommt später.*

> Das ist der Übergabe-Schritt an der Naht Research → Bootstrap. Er baut aus dem
> freigegebenen Plan den **allerersten Projekt-Schaltplan** + die Roadmap, legt den
> Arbeitsbereich an und zieht alle vom Plan verlangten Templates rein.
> **Abnahmebedingung: er holt sich alles selbst.** Bräuchte er an einer Stelle einen
> Menschen, der ihm etwas reinreicht, wäre genau das die Deus ex machina, die wir nicht
> wollen — also ist Self-sufficiency keine Kür, sondern Prüfkriterium.

```
BOOTSTRAP-INIT — Projekt aus dem freigegebenen Plan materialisieren

Haltung: Du bekommst einen vom Betreiber freigegebenen DRAFT-PLAN und Zugriff
auf den Asset-Ordner (Templates, Lessons, Schaltplan-Template). Du recherchierst
nicht, validierst nicht, entscheidest nichts neu — die Entscheidungen sind
gefallen und stehen im Plan. Dein Job: das Projekt physisch aufbauen,
workflow-ready, und zwar VOLLSTÄNDIG SELBST. Alles, was du brauchst, holst du
dir aus Plan und Asset-Ordner. Du verlangst nichts von einem Menschen. Fehlt
dir etwas, das weder im Plan noch im Asset-Ordner steht, ist das ein STOPP mit
Befund — kein Raten, kein Nachreichen von außen.

[DRAFT-PLAN]
{der freigegebene DRAFT-PLAN aus HITL_1 — getroffene Wahlen + WAIT-Liste}
[/DRAFT-PLAN]

[ASSET-ORDNER]
{Zugriff/Inhalt: Templates, Lessons, Schaltplan-Template}
[/ASSET-ORDNER]

Aufträge:

1. Projekt-Schaltplan bauen: Nimm das Schaltplan-Template als Struktur. Füll es
   mit den Entscheidungen aus dem DRAFT-PLAN — jeder entscheidbare Faden
   (Modellwahl, Frontend, Routing, …) wird zu einem Knoten/Modul mit seiner
   getroffenen Wahl. Die geparkten WAIT-Posten kommen als sichtbar offene
   Knoten rein (nicht weglassen — sichtbare offene Punkte killen Doppelarbeit).
   Das ist der ALLERERSTE Projekt-Schaltplan und ab jetzt das lebende Dokument.
2. Roadmap aufziehen: Aus dem Plan das Hauptziel in einem Satz, darunter die
   Unterziele als geordnete Kette bis Final Review. Das ist der Anker, an dem
   sich der erste Supervisor/Worker orientiert — selbst-erklärend, ohne dass
   jemand mündlich nachhilft.
3. Benötigte Templates ziehen: Welche Modul-Templates das Projekt braucht, sagt
   der DRAFT-PLAN selbst — jeder Faden zeigt auf sein Template. Hol genau die.
   Nicht mehr (kein Vorrat-Horten), nicht weniger.
4. Arbeitsbereich anlegen & befüllen: Leg den Projekt-Arbeitsbereich an und wirf
   rein: Projekt-Schaltplan, Roadmap, die gezogenen Templates, die relevanten
   Lessons. Workflow-ready — der nächste Schritt (Build) findet alles vor.
5. Selbst-Erklärbarkeit sichern: Der Projekt-Schaltplan muss so geschrieben
   sein, dass wer anbaut, ihn weiterführt. Die Fortschreibungs-Pflicht (jeder
   Supervisor schreibt beim Window-Close den Schaltplan weiter) gehört als Regel
   sichtbar an den Plan — sie steht schon in den Workflow-Regeln, hier wird sie
   verankert.

Regeln (knapp, bindend):
- Self-sufficient: Du ziehst dir alles selbst. Kein Mensch reicht dir etwas
  rein. Brauchst du etwas, das weder im Plan noch im Asset-Ordner liegt → STOPP
  mit Befund, kein Erfinden.
- Du entscheidest nichts neu. Der Plan ist die Wahrheit; du materialisierst ihn,
  du re-designst ihn nicht.
- Schaltplan = JSON ist die einzige Wahrheit. Render-Schichten (HTML) sind
  abgeleitet, nie zweite Quelle.
- Kein Code. Du baust das Gerüst (Plan, Roadmap, Arbeitsbereich, Templates),
  nicht die Implementierung. Das ist Build.
- Geparkte Posten bleiben sichtbar offen im Schaltplan — nicht stillschweigend
  mit Defaults zubetonieren.

Schließe mit — und nur das ist Pflicht-Format:

BOOTSTRAP-MANIFEST:
- Projekt-Schaltplan: erzeugt (wo) · Anzahl Knoten · davon offen (WAIT).
- Roadmap: Hauptziel + Anzahl Unterziele.
- Gezogene Templates: Liste (welcher Faden → welches Template).
- Übernommene WAIT-Posten: Liste, je mit „braucht: X" — der erste Supervisor
  weiß damit, wo die offenen Gates sind.
- STOPP-Befunde (falls etwas fehlte): was, und woran es hing. Sonst: keine.
```

---

## Slots auf einen Blick

| Station | Slots zum Füllen |
|---|---|
| 1 Research flach | `{BRIEF}` |
| 2 Research tief | `{ERSTER DURCHGANG}`, `{FÄDEN}` |
| 3 Synthese | `{TIEF-DURCHGANG}`, `{ENTSCHEIDUNGSREIFE}` |
| 4 Plan-Validation | `{DRAFT-PLAN}`, `{BELEG}` |
| 6 Bootstrap-Init | `{DRAFT-PLAN}` (freigegeben), `{ASSET-ORDNER}` |

## Offene Punkte (vor dem Bau zu klären)

- **Karten-Verortung:** Diese Strecke splittet `re.deep` aus dem Meta-Workflow in `re.flach` +
  `re.tief` und schiebt `re.synth` dazwischen. Der Meta-Workflow (`fabrik_meta_workflow.json`)
  weiß davon noch nichts → nachziehen, bevor der Supervisor-Aufbau läuft.
- **Station 4 gehärtet gegentesten:** ROUTE-Fassung am Pförtner-Draft-Plan noch nicht gelaufen.
- **Station 6 erstprüfen:** Bootstrap-Init ist neu und strukturell — am echten Asset-Ordner
  (mit Schaltplan-Template) einmal durchziehen, Manifest prüfen, v. a. ob „self-sufficient" hält.
- **Template-Guss:** Wenn die Strecke am echten Projekt hält, Prompts mit `{SLOTS}` als Templates
  ablegen — erst dann von „läuft im Tabletop" auf „Betrieb".
```
