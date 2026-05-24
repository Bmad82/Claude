# DESIGN_KINTSUGI.md — Globale Design-Referenz

Die einzige Datei die man braucht um das Kintsugi-Designsystem zu reproduzieren.
Extrahiert aus `zerberus_showcase.html` und `marathon_workflow_showcase.html`.
Bei jedem neuen UI-Projekt: diese Datei mitgeben statt der Showcases.

---

## 1. Philosophie

**Kintsugi** — die japanische Kunst, Zerbrochenes mit Gold zu reparieren. Die Risse werden nicht versteckt, sondern hervorgehoben. Jeder Bruch erzählt eine Geschichte.

**Übersetzt in Design:** Dunkel, still, reduziert — aber mit goldenen Akzenten die Leben zeigen. Keine glatte Corporate-Ästhetik. Kein Material Design. Kein Tailwind-Default. Die Oberfläche atmet wie verwittertes Metall mit Goldadern.

**Tonalität:** Editorial, nicht App. Eher Architekturzeitschrift als Dashboard. Großzügige Weißräume. Wenig spricht, aber was spricht, hat Gewicht.

---

## 2. Farbtokens

### 2.1 Kern-Palette

| Token | Hex | Rolle |
|-------|-----|-------|
| `--void` | `#08080c` | Tiefster Hintergrund. Fast-Schwarz mit kühlem Unterton. |
| `--mist` | `#12121a` | Erhöhte Flächen (Sidebar, Sections mit anderem Rhythmus). |
| `--surface` | `#0f0f16` | Mittlerer Hintergrund (Canvas, Arbeitsflächen). |
| `--border` | `#1e1e2e` | Trennlinien. Subtil, nie dominant. Auch als Grid-Gap-Farbe. |
| `--ember` | `#c4622d` | Warmes Kupferrot. Labels, Eyebrows, Nummerierung, Akzent-Linien. |
| `--gold` | `#d4a843` | DAS Kintsugi-Gold. Highlights, aktive Elemente, Zahlen, Riss-Linien. |
| `--crack` | `#e8c97a` | Helles Gold. Nur für die leuchtendsten Momente (Logo, Hero-Titel-Akzent). |
| `--text` | `#c8c8d8` | Primärer Text. Kein reines Weiß — leicht bläulich-silbern. |
| `--text-dim` | `#6b6b8a` | Sekundärtext, Labels, Meta-Infos. Dezent violett-grau. |
| `--accent` | `#c4622d` | Alias für `--ember`. Semantisch: "hier passiert was". |

### 2.2 Status-Farben

| Token | Hex | Verwendung |
|-------|-----|------------|
| Erfolg | `#4a9e6a` | Erledigte Steps, grüne Badges. Gedämpftes Grün, nie grell. |
| Fehler | `#9e4a4a` | Fehlgeschlagen. Gedämpftes Rot, passend zur Gesamtstimmung. |
| Info | `#4a6a9e` | Neutrale Hinweise, Plan-Status. Gedämpftes Blau. |
| Warnung | `--gold` | Gold IST die Warnfarbe. Kein separates Orange. |

### 2.3 Transparenz-Muster

Hintergrund-Tints werden IMMER als Hex + Alpha-Suffix gebaut, nie als `rgba()`:

```
Background-Tint:  #d4a84308  (Gold, 3% Opacity — hauchzarter Hintergrund)
Border-Tint:      #d4a84320  (Gold, 12% — subtiler Rahmen)
Hover-Tint:       #d4a84311  (Gold, 7% — spürbarer Hover)
Badge-Background: #4a9e6a22  (Grün, 13% — Status-Badge-Füllung)
Badge-Border:     #4a9e6a55  (Grün, 33% — Status-Badge-Rahmen)
Ghost-Text:       #ffffff03  (Weiß, 1% — Wasserzeichen-Buchstaben)
Hairline-Border:  #ffffff06  (Weiß, 2% — kaum sichtbare Linie)
```

---

## 3. Typografie

### 3.1 Font-Stack

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=JetBrains+Mono:wght@300;400;500&family=Crimson+Pro:ital,wght@0,300;0,400;1,300&display=swap" rel="stylesheet">
```

| Font | Rolle | Charakter |
|------|-------|-----------|
| **Playfair Display** | Display, Titel, Zahlen, Zitate | Serif, editorial, dramatisch. Weight 900 für Headlines, 700 für Subtitles, 400 italic für Akzent-Wörter. |
| **JetBrains Mono** | Labels, Code, Meta-Info, Tags | Monospace, technisch, präzise. Weight 300-500. IMMER uppercase + letter-spacing für Labels. |
| **Crimson Pro** | Fließtext, Beschreibungen, Body | Serif, warm, lesbar. Weight 300 (dünn!) als Default, 400 für Betonung. |

### 3.2 Typografie-Regeln

**Hero-Titel:**
```css
font-family: 'Playfair Display', serif;
font-size: clamp(52px, 8vw, 110px);
font-weight: 900;
line-height: 0.92;
letter-spacing: -3px;
```
Akzent-Wort als `<em>` — italic, weight 400, Farbe `--gold`, eigene Zeile via `display: block`.

**Section-Label (Eyebrow):**
```css
font-family: 'JetBrains Mono', monospace;
font-size: 10px;
color: var(--ember);
letter-spacing: 4px;
text-transform: uppercase;
```
Optional mit `::after`-Linie: `height: 1px; width: 48px; background: var(--ember); opacity: 0.4;`

**Section-Titel:**
```css
font-family: 'Playfair Display', serif;
font-size: clamp(36px, 4vw, 56px);
font-weight: 700;
line-height: 1.1;
letter-spacing: -1px;
```
Akzent-Wort wieder als `<em>` in `--gold`.

**Body-Text:**
```css
font-family: 'Crimson Pro', serif;
font-weight: 300;
font-size: 18px;
color: var(--text-dim);
line-height: 1.7;
max-width: 640px;
```
Betonungen als `<strong>` mit `color: var(--text); font-weight: 400;` — nie fett, nur heller.

**Mono-Labels (überall):**
```css
font-family: 'JetBrains Mono', monospace;
font-size: 9-11px;
letter-spacing: 2-4px;
text-transform: uppercase;
color: var(--text-dim);  /* oder --ember für aktive Labels */
```

---

## 4. Dekorative Elemente

### 4.1 Noise-Overlay (Filmkorn)

Liegt über ALLEM. Fixed, pointer-events: none, z-index: 999. Gibt der Oberfläche eine analoge, organische Textur.

```css
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 999;
  opacity: 0.25-0.35;
}
```

### 4.2 Kintsugi-Risse (Hero-Crack-SVG)

SVG-Pfade die wie Goldadern durch die Oberfläche laufen. Absolut positioniert, pointer-events: none.

```svg
<svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice">
  <!-- Hauptriss: vertikal, leicht mäandernd -->
  <path d="M 800 0 Q 820 150 790 250 Q 760 350 800 450 Q 840 550 810 700 Q 790 800 820 900"
        stroke="#d4a843" stroke-width="0.8" fill="none" opacity="0.12"/>
  <!-- Nebenriss: horizontal, abzweigend -->
  <path d="M 790 280 Q 850 310 920 290 Q 990 270 1060 300"
        stroke="#d4a843" stroke-width="0.5" fill="none" opacity="0.08"/>
  <!-- Kupfer-Riss: zweiter Farbton -->
  <path d="M 1100 0 Q 1080 200 1110 350 Q 1140 500 1100 650"
        stroke="#c4622d" stroke-width="0.6" fill="none" opacity="0.07"/>
</svg>
```

Regeln: Quadratische Bézier-Kurven (`Q`), nie gerade Linien. Stroke-Width 0.3-0.8. Opacity 0.06-0.12. Hauptrisse in Gold, Nebenrisse in Ember.

### 4.3 Gold-Divider

Horizontale Trennlinie die in der Mitte leuchtet und zu den Rändern ausfadet.

```css
.gold-divider {
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
  opacity: 0.3;
}
```

### 4.4 Ghost-Text-Wasserzeichen

Riesiger Text hinter dem Inhalt als atmosphärische Textur.

```css
.section::before {
  content: 'KINTSUGI';  /* oder MARATHON, ZERBERUS, ORCHESTRATE */
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-family: 'Playfair Display', serif;
  font-size: clamp(80px, 18vw, 240px);
  font-weight: 900;
  color: #ffffff03;
  white-space: nowrap;
  pointer-events: none;
  letter-spacing: -8px;
}
```

### 4.5 Dashed Crack-Lines (für Panels/Karten)

Subtile goldene Linien als Trennelemente innerhalb von Komponenten.

```svg
<line x1="0" y1="1" x2="800" y2="1"
      stroke="#d4a843" stroke-width="1"
      stroke-dasharray="80 20 40 10 120 30" />
```

---

## 5. Layout-Patterns

### 5.1 Spacing-System

| Kontext | Wert | Verwendung |
|---------|------|------------|
| Section Padding vertikal | `120px` | Desktop-Sektionen |
| Section Padding horizontal | `60px` | Desktop-Seiten |
| Section Padding (Mobile) | `80px / 24px` | Responsive |
| Max-Width Content | `1200px` | Zentrierter Content |
| Element-Abstand nach Label | `72px` | Abstand Section-Label → Inhalt |
| Grid-Gap | `1px` mit `background: var(--border)` | Grid-Cells mit sichtbarem Steg |
| Card Padding | `40px 36px` | Innenabstand Grid-Zellen |
| Nav Padding | `32px 60px` | Header-Bereich |
| Pipeline Step Padding | `36px 0` | Vertikaler Rhythmus |

### 5.2 Grid-Muster: Arch-Grid (Feature-Karten)

```css
.arch-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* 3 Spalten Desktop */
  gap: 1px;
  background: var(--border);  /* Gap-Farbe = Border */
  border: 1px solid var(--border);
}
.arch-cell {
  background: var(--surface);
  padding: 40px 36px;
  transition: background 0.3s;
}
.arch-cell:hover { background: #0f0f1a; }
```

Jede Zelle hat ein Ghost-Number via `data-num` Attribut:
```css
.arch-cell::before {
  content: attr(data-num);
  position: absolute; top: 20px; right: 24px;
  font-family: 'JetBrains Mono', monospace;
  color: #ffffff06;
  font-size: 48px;
}
```

### 5.3 Grid-Muster: Layer-Rows (Daten-Tabelle)

```css
.layer-row {
  display: grid;
  grid-template-columns: 260px 1fr;
  background: var(--void);
  transition: background 0.2s;
}
.layer-row:hover { background: #0c0c12; }
```

### 5.4 Grid-Muster: Stack-Grid (Key-Value)

```css
.stack-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1px;
  background: var(--border);
}
.stack-row {
  display: grid;
  grid-template-columns: 200px 1fr;
}
```

### 5.5 Grid-Muster: Numbers-Grid (Statistiken)

```css
.numbers-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: var(--border);
}
```

Zahlen in Playfair 64px/900/Gold. Labels in JetBrains 10px/uppercase/text-dim.

### 5.6 Pipeline-Steps (Nummerierte Schritte)

```css
.pipeline-step {
  display: grid;
  grid-template-columns: 48-64px 1fr;
  gap: 32px;
  padding: 36px 0;
  border-bottom: 1px solid var(--border);
  opacity: 0.5;
  transition: opacity 0.3s;
}
.pipeline-step:hover { opacity: 1; }
```

### 5.7 Philosophy-Strip (Zitat-Band)

Volle Breite, `--mist` Hintergrund, horizontaler Flex mit Dividers zwischen Zitaten.

```css
.philosophy {
  background: var(--mist);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  padding: 32px 60px;
  display: flex;
  align-items: center;
  gap: 48px;
}
```

Texte in Playfair 18px italic, Akzent-Wörter in Gold. Dividers: 1px × 32px in `--border`.

---

## 6. Komponenten-Muster

### 6.1 Tag/Badge-Varianten

```css
/* Basis */
.tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9-10px;
  letter-spacing: 1-2px;
  text-transform: uppercase;
  border: 1px solid var(--border);
  padding: 2-3px 8-10px;
  display: inline-block;
}

/* Varianten */
.tag-bibel  { border-color: #c4622d30; color: var(--ember); }
.tag-prosa  { border-color: #d4a84330; color: var(--gold); }
.tag-ephemer { border-color: #ffffff15; color: var(--text-dim); }
.tag-code   { background: #d4a84308; border-color: #d4a84320; color: var(--gold); }
```

### 6.2 Status-Badges (für Dashboards)

```css
.status-badge {
  display: inline-block;
  padding: 2px 10px;
  border-radius: 3px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.5px;
}
/* done */    background: #4a9e6a22; border: 1px solid #4a9e6a55; color: #4a9e6a;
/* running */ background: #d4a84322; border: 1px solid #d4a84355; color: #d4a843;
/* pending */ background: #6b6b8a18; border: 1px solid #1e1e2e;  color: #6b6b8a;
/* failed */  background: #9e4a4a22; border: 1px solid #9e4a4a55; color: #9e4a4a;
```

### 6.3 Code-Inline

```css
code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  color: var(--gold);
  background: #d4a84308;
  padding: 2px 8px;
  border-radius: 2px;
}
```

### 6.4 Rule-Example (Zitat-Block mit Seitenlinie)

```css
.rule-example {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--gold);
  background: #d4a84306;
  border-left: 2px solid #d4a84340;
  padding: 10px 14px;
  line-height: 1.8;
}
```

### 6.5 Scroll-Hint (Footer-Navigation)

```css
.scroll-hint {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: var(--text-dim);
  letter-spacing: 3px;
  text-transform: uppercase;
  display: flex;
  align-items: center;
  gap: 12px;
}
.scroll-line {
  width: 60px; height: 1px;
  background: linear-gradient(90deg, var(--ember), transparent);
  animation: scrollPulse 2s ease-in-out infinite;
}
```

### 6.6 Progress-Bar

```css
.progress-bar {
  width: 100%; height: 3px;
  background: var(--border);
  border-radius: 2px;
  overflow: hidden;
}
.progress-bar-fill {
  height: 100%;
  border-radius: 2px;
  background: linear-gradient(90deg, var(--ember), var(--gold));
  transition: width 0.6s ease;
}
```

---

## 7. Animationen

### 7.1 Scroll-Reveal

```css
.reveal {
  opacity: 0;
  transform: translateY(32px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

Stagger für Grid-Zellen: `transitionDelay: ${i * 60-80}ms`.

### 7.2 FadeUp (Hero-Elemente)

```css
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
```
Hero-Elemente: `animation: fadeUp 0.8s ease <delay> forwards;` mit gestaffelten Delays (0.2s, 0.4s, 0.6s, 0.8s).

### 7.3 Scroll-Pulse (Hint-Linie)

```css
@keyframes scrollPulse {
  0%, 100% { opacity: 0.4; }
  50%      { opacity: 1; }
}
```

---

## 8. Interaktions-Regeln

- **Hover auf Karten:** Hintergrund-Shift von `--surface` zu `#0f0f1a` (leicht heller). Nie Border-Highlight.
- **Hover auf Pipeline-Steps:** Opacity von 0.5 → 1. Content "lebt auf" statt "wird umrahmt".
- **Active-State auf Sidebar-Items:** `border-left: 2px solid var(--gold)` + Background `--surface`.
- **Buttons:** Transparent Background + Border in Akzentfarbe. Hover: Background-Tint der Akzentfarbe.
- **Mobile:** `:active` statt `:hover`. Min 44px Touch-Targets. `dvh` statt `vh`.

---

## 9. Thematische Varianten

Das Grundsystem bleibt identisch — was sich ändert ist die **Metapher** die das jeweilige Produkt prägt.

### 9.1 Zerberus — "Die Werkstatt"

Kern-Metapher: Eine Werkstatt voller Werkzeuge. Jedes benannt, jedes mit einer Aufgabe.
Hero: *"Deine eigene KI-Werkstatt."*
Ghost-Text: `ZERBERUS`
Ikonografie: Werkzeug-Emojis (🐺⚙️🦅🛡️🔍🎙️). Mythologische Namen.
Pipeline: Nummerierte Schritte "Von der Sprache zum Ergebnis."

### 9.2 Marathon — "Die Straße"

Kern-Metapher: Eine endlose Straße. Jeder Patch ist ein Kilometer. Der Staffelstab geht weiter.
Hero: *"Der Mensch gibt Ziele. Nicht Rezepte."*
Ghost-Text: `MARATHON`
Ikonografie: 🏗🧠⚙️ (Architekt, Planer, Baumeister). Rollen statt Werkzeuge.
Besonderheit: Philosophy-Strip mit drei Zitaten. Layer-Block für Dateisystem-Schichten.

### 9.3 Orchestrate — "Die Fabrik"

Kern-Metapher: Eine Fabrik mit Fertigungsstraße. Der Architekt zeichnet den Plan, die Worker bauen.
Hero: *"Du orchestrierst. Sie bauen."*
Ghost-Text: `ORCHESTRATE`
Layout: Drei-Panel (Sidebar + Canvas + Log). Desktop-first. Kein Scroll, sondern Panels.
Besonderheit: Live-Daten (Step-Status, Token-Counter, Kosten), Progress-Bars, Step-Cards mit Aufklapp-Output.

### 9.4 Mjölnir — "Das Cockpit"

Kern-Metapher: Industrielles Kontrollzentrum. Schalter, Anzeigen, Status-Lampen.
Besonderheit: Brushed Metal, Rotary Knobs, Segment-Displays (eigenes Sub-Designsystem).
Verbindung zu Kintsugi: Farbpalette bleibt identisch, aber Komponenten-Formen werden kantiger, technischer.

---

## 10. Don'ts

- **Kein Material Design.** Keine abgerundeten Cards mit 16px Border-Radius. Max 2-4px.
- **Kein Tailwind-Default.** Keine `bg-gray-800 text-white`. Jeder Wert ist benannt.
- **Kein Inter/Roboto/System-Font.** Playfair + JetBrains + Crimson, fertig.
- **Kein Purple-Gradient.** Das Gold-Ember-System ist die einzige Akzentachse.
- **Keine Emojis als Design-Element.** Emojis nur als Icons in technischen Karten (Arch-Grid).
- **Nie `hover` allein.** Immer auch `:active` für Mobile. Transition-Duration 0.2-0.3s.
- **Nie harten Kontrast.** Text ist `#c8c8d8`, nicht `#ffffff`. Hintergrund ist `#08080c`, nicht `#000000`.
- **Nie Farben ohne Kontext.** Gold = aktiv/wichtig. Ember = Label/Kategorie. Grün/Rot/Blau = Status.

---

## 11. Responsive-Breakpoints

```css
@media (max-width: 768px) {
  /* Padding: 120px/60px → 80px/24px */
  /* Arch-Grid: 3col → 1col */
  /* Numbers-Grid: 4col → 2col */
  /* Stack-Grid: 2col → 1col */
  /* Philosophy: horizontal scroll oder wrap */
  /* Footer: column statt row */
  /* Dashboard-Panels: Sidebar kollapsiert, Log-Panel als Drawer */
}
```

---

## 12. Quick-Start: Neues Projekt im Kintsugi-Stil

```html
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[PROJEKTNAME]</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=JetBrains+Mono:wght@300;400;500&family=Crimson+Pro:ital,wght@0,300;0,400;1,300&display=swap" rel="stylesheet">
<style>
:root {
  --void: #08080c;
  --ember: #c4622d;
  --gold: #d4a843;
  --crack: #e8c97a;
  --mist: #12121a;
  --surface: #0f0f16;
  --border: #1e1e2e;
  --text: #c8c8d8;
  --text-dim: #6b6b8a;
  --accent: #c4622d;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  background: var(--void);
  color: var(--text);
  font-family: 'Crimson Pro', serif;
  font-weight: 300;
  overflow-x: hidden;
}
/* Noise-Overlay */
body::before {
  content: '';
  position: fixed; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none; z-index: 999; opacity: 0.3;
}
</style>
</head>
<body>
  <!-- Bauen. -->
</body>
</html>
```

---

*Extrahiert: 23. Mai 2026 · Quellen: zerberus_showcase.html, marathon_workflow_showcase.html, orchestrate_dashboard_prototype.jsx*
