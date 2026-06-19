# DESIGN.md — Globale Design-Referenz (UI-Layer)

⚠️ **DIESES REPO IST PUBLIC.** Keine Secrets, Keys, IPs, interne URLs.

Diese Datei ist die zentrale UI-/Look-and-Feel-Referenz für alle Projekte (Farben, Typography, Komponenten, Mobile-Regeln, Animationen).
Sie wird NICHT kopiert — Projekte referenzieren sie direkt aus dem Repo.

**Platzhalter-Konvention:** Konkrete Werte (Hex-Codes, Pixel, Schriftgrößen) stehen als `[TODO: aus Projekt-:root]`. Diese Werte sind projektspezifisch und werden beim nächsten UI-Patch direkt aus dem `:root`-CSS-Block des jeweiligen Projekts in DESIGN_{PROJEKT}.md übertragen — diese globale DESIGN.md bleibt selbst leer in den Slots. Die Sektion „Offene Werte" am Ende dieser Datei fasst zusammen, welche Slots beim nächsten UI-Patch zu befüllen sind.

Bei jedem UI-Patch: Diese Datei konsultieren. Neue Design-Entscheidungen hier eintragen.

## Geltungsbereich

Diese DESIGN.md dokumentiert ausschließlich den **UI-Layer** (Visuelles Design, Komponenten, Mobile-Verhalten, UX-Prinzipien für Endnutzer-Oberflächen).

Der **Marathon-Workflow** (Drei-Rollen-Modell Architekt/Supervisor/Coda, File-Hierarchie, Bibel-Format vs Prosa-Trennung, Handover-Round-Trip, Faulheits-Catches, 5h-Fenster-Constraint, Bootstrap-Prinzip) ist KEIN UI-Thema und wird an anderen Stellen dokumentiert:

| Aspekt | Quelle |
|---|---|
| Drei-Rollen-Modell + Projekte-Liste | [README.md](README.md) |
| Die 6 Faulheits-Catches + Bibel-Format + Selbsttest-Pattern + Handover-Round-Trip | [GLOBAL_LESSONS.md](GLOBAL_LESSONS.md) |
| NIE/IMMER-Listen für Chat-Fenster (Supervisor-Rolle) | [SUPERVISOR_KODEX.md](SUPERVISOR_KODEX.md) |
| Bootstrap-Prinzip + Walkthrough für neue Projekte | [PROJECT_BOOTSTRAP_README.md](PROJECT_BOOTSTRAP_README.md) |
| Templates für neue Projekte (CLAUDE_/SUPERVISOR_/HANDOVER_/FEATURE_REQUEST_ u.a.) | [templates/](templates/) |
| Konzept-Ursprünge (Faulheits-Catches, etc.) | [concepts/](concepts/) |
| Offene Architektur-Fragen + dokumentierte Konflikte | [DECISIONS_PENDING.md](DECISIONS_PENDING.md) |

Diese Trennung ist bewusst: UI-Design und Workflow-Architektur sind unterschiedliche Layer mit unterschiedlichen Update-Zyklen und Adressaten. UI-Design ändert sich pro Frontend-Patch — Workflow-Architektur ändert sich nach Faulheits-Catches und Multi-Session-Erfahrung. Diese DESIGN.md bleibt deshalb fokussiert auf das, was zum nächsten UI-Patch gehört.

---

## 1. Farbsystem

### 1.1 Kernfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Primär | `--color-primary` | `[TODO: aus Projekt-:root]` | Hauptfarbe, Buttons, aktive Elemente, Highlights |
| Primär Hover | `--color-primary-hover` | `[TODO: aus Projekt-:root]` | Hover/Active-Zustand der Primärfarbe |
| Primär gedämpft | `--color-primary-muted` | `[TODO: aus Projekt-:root]` | Dezente Variante für Hintergründe, Badges |
| Primär Mittel | `--color-primary-mid` | `[TODO: aus Projekt-:root]` | Basis für LLM-Bubble-Background (rgba-Ableitung) |
| Sekundär | `--color-secondary` | `[TODO: aus Projekt-:root]` | Ergänzungsfarbe, sekundäre Buttons |
| Sekundär Hover | `--color-secondary-hover` | `[TODO: aus Projekt-:root]` | Hover/Active-Zustand der Sekundärfarbe |
| Akzent | `--color-accent` | `[TODO: aus Projekt-:root]` | Eyecatcher, sparsam einsetzen (Sterne, Badges, Highlights). Basis für User-Bubble-Background |

### 1.2 Hintergrundfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| App-Hintergrund | `--bg-app` | `[TODO: aus Projekt-:root]` | Gesamter Seitenhintergrund (Dark-First) |
| Flächen-Hintergrund | `--bg-surface` | `[TODO: aus Projekt-:root]` | Cards, Panels, Container |
| Flächen-Hintergrund erhöht | `--bg-surface-raised` | `[TODO: aus Projekt-:root]` | Modals, Dropdowns, Overlays |
| Sidebar-Hintergrund | `--bg-sidebar` | `[TODO: aus Projekt-:root]` | Navigation, Seitenleisten |
| Input-Hintergrund | `--bg-input` | `[TODO: aus Projekt-:root]` | Eingabefelder, Textareas |
| Input-Hintergrund Fokus | `--bg-input-focus` | `[TODO: aus Projekt-:root]` | Eingabefeld bei Fokus |

### 1.3 Textfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Text primär | `--text-primary` | `[TODO: aus Projekt-:root]` | Haupttextfarbe, Fließtext |
| Text sekundär | `--text-secondary` | `[TODO: aus Projekt-:root]` | Weniger wichtiger Text, Labels, Timestamps |
| Text deaktiviert | `--text-disabled` | `[TODO: aus Projekt-:root]` | Inaktive Elemente, Placeholder |
| Text invertiert | `--text-inverted` | `[TODO: aus Projekt-:root]` | Text auf dunklem/hellem Gegenhintergrund |
| Text auf Primärfarbe | `--text-on-primary` | `[TODO: aus Projekt-:root]` | Text auf primärfarbigem Hintergrund (Buttons) |
| Link | `--text-link` | `[TODO: aus Projekt-:root]` | Hyperlinks, klickbare Textelemente |
| Link besucht | `--text-link-visited` | `[TODO: aus Projekt-:root]` | Bereits besuchte Links |

### 1.4 Statusfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Erfolg | `--color-success` | `[TODO: aus Projekt-:root]` | Bestätigungen, "gespeichert", grüne Häkchen |
| Erfolg Hintergrund | `--color-success-bg` | `[TODO: aus Projekt-:root]` | Hintergrund für Erfolgs-Banner/Badges |
| Warnung | `--color-warning` | `[TODO: aus Projekt-:root]` | Hinweise, "Achtung", noch kein Fehler |
| Warnung Hintergrund | `--color-warning-bg` | `[TODO: aus Projekt-:root]` | Hintergrund für Warn-Banner |
| Fehler | `--color-error` | `[TODO: aus Projekt-:root]` | Fehlermeldungen, Validierung fehlgeschlagen |
| Fehler Hintergrund | `--color-error-bg` | `[TODO: aus Projekt-:root]` | Hintergrund für Fehler-Banner |
| Info | `--color-info` | `[TODO: aus Projekt-:root]` | Neutrale Hinweise, Tooltips, Erklärungen |
| Info Hintergrund | `--color-info-bg` | `[TODO: aus Projekt-:root]` | Hintergrund für Info-Banner |

### 1.5 Randfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Rand Standard | `--border-color` | `[TODO: aus Projekt-:root]` | Normale Trennlinien, Card-Rahmen |
| Rand leicht | `--border-color-light` | `[TODO: aus Projekt-:root]` | Subtile Trenner, Tabellenlinien |
| Rand Fokus | `--border-color-focus` | `[TODO: aus Projekt-:root]` | Eingabefelder bei Fokus, aktive Tabs |
| Rand Fehler | `--border-color-error` | `[TODO: aus Projekt-:root]` | Validierungsfehler an Eingabefeldern |

### 1.6 Spezialfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| User-Bubble Hintergrund | `--bubble-user-bg` | `rgba(236, 64, 122, 0.88)` | Chat: Hintergrund der User-Nachrichten (Akzent-Ableitung mit Alpha) |
| User-Bubble Text | `--bubble-user-text` | `[TODO: aus Projekt-:root]` | Chat: Textfarbe in User-Nachrichten |
| Bot-Bubble Hintergrund | `--bubble-llm-bg` | `rgba(26, 47, 78, 0.85)` | Chat: Hintergrund der Bot-Nachrichten (Primary-Mid-Ableitung mit Alpha) |
| Bot-Bubble Text | `--bubble-bot-text` | `[TODO: aus Projekt-:root]` | Chat: Textfarbe in Bot-Nachrichten |
| Overlay/Backdrop | `--color-overlay` | `[TODO: aus Projekt-:root]` | Halbdurchsichtiger Hintergrund hinter Modals |
| Schatten | `--color-shadow` | `[TODO: aus Projekt-:root]` | Box-Shadow-Farbe für Elevation |
| Scrollbar Track | `--scrollbar-track` | `[TODO: aus Projekt-:root]` | Scrollbar-Hintergrund |
| Scrollbar Thumb | `--scrollbar-thumb` | `[TODO: aus Projekt-:root]` | Scrollbar-Griff |

**Anti-Invariante:** Bubble-Backgrounds dürfen NIE `#000000` oder `transparent` als Default haben — "nie schwarz auf schwarz".
Immer rgba-Werte mit Alpha 0.85–0.88 als Basis verwenden. `resetTheme()` muss `resetAllBubbles()` + `resetFontSize()` mitrufen.

### 1.7 Dark/Light Mode

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Standard-Modus | `dark` | Dark-First — primär ein Dark-Mode-UI |
| Umschaltbar | ja | Theme-Presets via Settings-Modal |
| Speicherung | `localStorage` Keys: `nala_theme`, `nala_last_active_favorite`, `nala_fav_1`…`nala_fav_3` (v2-Schema) | Persistenz über Browser-Neustart |
| FOUC-Vermeidung | Early-Load-IIFE im `<head>` | Prüft `nala_last_active_favorite` → lädt Fav-Slot (v2: Theme + Bubble + fontSize) → wendet CSS-Props an, bevor Body rendert. Fav hat Vorrang vor flachem `nala_theme` |

### 1.8 Hintergrundbild

| Eigenschaft | CSS-Variable | Wert | Beschreibung |
|-------------|-------------|------|--------------|
| Bild-URL | `--bg-image-url` | `none` | Vom User wählbares Hintergrundbild |
| Skalierung | `--bg-image-size` | `cover` | `cover`, `contain`, `stretch`, `tile` — User-wählbar |
| Position | `--bg-image-position` | `center center` | Ausrichtung des Bildes |
| Durchscheinen | `--bg-image-opacity` | `0.15` | Wie stark das Bild durchscheint (0.0–1.0). Default sehr dezent |
| Overlay-Methode | — | `::before` Pseudo-Element mit `--bg-app` + `--bg-image-opacity` | Hintergrundbild liegt unter einem halbtransparenten Overlay der App-Hintergrundfarbe |

---

## 2. Typography

### 2.1 Schriftarten

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Hauptschrift | `--font-family-base` | `[TODO: aus Projekt-:root]` | Fließtext, UI-Elemente |
| Monospace | `--font-family-mono` | `[TODO: aus Projekt-:root]` | Code, Klickpfade, technische Werte |
| Display/Headline | `--font-family-display` | `[TODO: aus Projekt-:root]` | Große Überschriften, Titel (optional, kann gleich wie Base sein) |
| Quelle | — | `[TODO: aus Projekt-:root]` | Wie werden Fonts geladen |

### 2.2 Größen-Skala

| Stufe | CSS-Variable | Wert | Einsatz |
|-------|-------------|------|---------|
| XS | `--font-size-xs` | `[TODO: aus Projekt-:root]` | Timestamps, Badges, Footnotes |
| SM | `--font-size-sm` | `[TODO: aus Projekt-:root]` | Labels, Hilfstexte, Captions |
| Base | `--font-size-base` | `15px` (Default) | Fließtext, Inputs, Buttons |
| MD | `--font-size-md` | `[TODO: aus Projekt-:root]` | Hervorgehobener Text, Card-Titel |
| LG | `--font-size-lg` | `[TODO: aus Projekt-:root]` | Abschnitts-Überschriften (H3) |
| XL | `--font-size-xl` | `[TODO: aus Projekt-:root]` | Seitenüberschriften (H2) |
| XXL | `--font-size-xxl` | `[TODO: aus Projekt-:root]` | Haupttitel (H1), Hero-Text |

### 2.3 Zeilenhöhen

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Eng | `--line-height-tight` | `[TODO: aus Projekt-:root]` | Überschriften, Buttons |
| Normal | `--line-height-base` | `[TODO: aus Projekt-:root]` | Fließtext |
| Weit | `--line-height-relaxed` | `[TODO: aus Projekt-:root]` | Lesestoff, lange Absätze |

### 2.4 Schriftgewichte

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Normal | `--font-weight-normal` | `[TODO: aus Projekt-:root]` | Fließtext |
| Medium | `--font-weight-medium` | `[TODO: aus Projekt-:root]` | Labels, leichte Hervorhebung |
| Bold | `--font-weight-bold` | `[TODO: aus Projekt-:root]` | Überschriften, starke Hervorhebung |

### 2.5 Skalierungssystem (2-Achsen)

Ersetzt feste Font-Presets. Zwei unabhängige Achsen, gesteuert per Stepper (+ / −), sofort sichtbare Änderung ohne Speichern-Button.

| Achse | CSS-Variable | Beschreibung | Min | Max | Schrittweite |
|-------|-------------|--------------|-----|-----|-------------|
| UI-Skalierung | `--ui-scale` | Symbole, Buttons, Touch-Targets, Abstände, UI-Labels. Beeinflusst NICHT den Chat-Content | `0.8` | `1.5` | `0.05` |
| Content-Schriftgröße | `--font-size-base` | Text in Bubbles (User + LLM). Unabhängig von UI-Elementen | `11px` | `24px` | `1px` |

**Interaktion mit System-Einstellungen:**
- Android/iOS-Schriftgröße wirkt auf WebView-Text (multiplikativ). Wenn System "groß" + App "groß" → wird sehr groß. Das ist erwartetes Verhalten, kein Bug.
- Android-Anzeigegröße beeinflusst WebView-Layout proportional.
- SVG/Image-Icons werden von System-Schriftgrößeneinstellungen NICHT beeinflusst. Emoji-Icons als Text-Glyphen dagegen schon.
- UI-Skalierung in der App kompensiert oder verstärkt System-Einstellungen — der User hat die Kontrolle.

**Caps & Schutz:**
- Bei jedem Skalierungsschritt prüfen: überlappen UI-Elemente? Falls ja → Schritt wird nicht ausgeführt, visuelles Feedback.
- Min/Max-Werte sind so gewählt, dass kein Layout bricht, aber ein großer Bereich abgedeckt wird.
- Testbar per Loki/Vidar: Extreme-Skalierung als Testfall.

---

## 3. Spacing & Layout

### 3.1 Spacing-Skala

| Stufe | CSS-Variable | Wert | Typischer Einsatz |
|-------|-------------|------|-------------------|
| 2XS | `--space-2xs` | `[TODO: aus Projekt-:root]` | Inline-Abstände, Icon-Gaps |
| XS | `--space-xs` | `[TODO: aus Projekt-:root]` | Enge Abstände innerhalb von Gruppen |
| SM | `--space-sm` | `[TODO: aus Projekt-:root]` | Padding in kleinen Elementen |
| MD | `--space-md` | `[TODO: aus Projekt-:root]` | Standard-Padding, Card-Innenabstand |
| LG | `--space-lg` | `[TODO: aus Projekt-:root]` | Abstand zwischen Sektionen |
| XL | `--space-xl` | `[TODO: aus Projekt-:root]` | Große Sektionsabstände |
| 2XL | `--space-2xl` | `[TODO: aus Projekt-:root]` | Seitenränder, Hero-Abstände |

### 3.2 Border-Radius

| Stufe | CSS-Variable | Wert | Einsatz |
|-------|-------------|------|---------|
| Keiner | `--radius-none` | `0` | Scharfe Kanten (bewusst eckig) |
| Klein | `--radius-sm` | `[TODO: aus Projekt-:root]` | Buttons, Inputs, Badges |
| Standard | `--radius-md` | `[TODO: aus Projekt-:root]` | Cards, Panels |
| Groß | `--radius-lg` | `[TODO: aus Projekt-:root]` | Modals, große Container |
| Rund | `--radius-full` | `9999px` | Avatare, runde Buttons, Pills |

### 3.3 Breakpoints

| Name | CSS-Variable | Wert | Beschreibung |
|------|-------------|------|--------------|
| Mobile S | `--bp-mobile-s` | `[TODO: aus Projekt-:root]` | Kleine Smartphones (SE, Mini) |
| Mobile | `--bp-mobile` | `[TODO: aus Projekt-:root]` | Standard-Smartphones |
| Tablet | `--bp-tablet` | `[TODO: aus Projekt-:root]` | Tablets, große Phones im Landscape |
| Desktop | `--bp-desktop` | `[TODO: aus Projekt-:root]` | Laptops, Desktops |
| Wide | `--bp-wide` | `[TODO: aus Projekt-:root]` | Große Monitore |

### 3.4 Z-Index-Skala

| Ebene | CSS-Variable | Wert | Einsatz |
|-------|-------------|------|---------|
| Basis | `--z-base` | `[TODO: aus Projekt-:root]` | Normaler Content |
| Sticky | `--z-sticky` | `[TODO: aus Projekt-:root]` | Sticky Header, Tab-Leisten |
| Dropdown | `--z-dropdown` | `[TODO: aus Projekt-:root]` | Dropdowns, Autocomplete |
| Scroll-Nav | `--z-scroll-nav` | `[TODO: aus Projekt-:root]` | Scroll-Navigationsleiste (über Content, unter Modal) |
| Modal-Backdrop | `--z-backdrop` | `[TODO: aus Projekt-:root]` | Overlay hinter Modal |
| Modal | `--z-modal` | `[TODO: aus Projekt-:root]` | Modals, Dialoge |
| Toast | `--z-toast` | `[TODO: aus Projekt-:root]` | Benachrichtigungen, Toasts |
| Tooltip | `--z-tooltip` | `[TODO: aus Projekt-:root]` | Tooltips, immer oben |

### 3.5 Layout-Grundregel

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| LLM-Ausgabe Breite | `100%` | LLM-Antworten nutzen die volle Bildschirmbreite. Kein Avatar-Einzug, kein verschenkter Platz |
| User-Bubble Breite | `100%` | User-Eingaben ebenfalls volle Breite |
| Content Max-Width | `[TODO: aus Projekt-:root]` | Optional: Max-Width auf Desktop um Lesebreite zu begrenzen. Mobile: immer 100% |
| Höheneinheit | `dvh` | `dvh` statt `vh` — respektiert dynamische Viewport-Höhe (Mobile-Keyboard) |

---

## 4. Komponenten

### 4.1 Buttons

| Eigenschaft | Primär | Sekundär | Danger | Ghost |
|-------------|--------|----------|--------|-------|
| Hintergrund | `--color-primary` | `--bg-surface` | `--color-error` | `transparent` |
| Textfarbe | `--text-on-primary` | `--text-primary` | `#ffffff` | `--text-primary` |
| Border | `none` | `1px solid --border-color` | `none` | `none` |
| Border-Radius | `--radius-sm` | `--radius-sm` | `--radius-sm` | `--radius-sm` |
| Padding | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` |
| Min-Höhe | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` |
| Min-Höhe Touch | `44px` | `44px` | `44px` | `44px` |
| Hover-Effekt | `--color-primary-hover` | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` |
| Active-Effekt | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` |
| Disabled | `opacity: 0.5` | `opacity: 0.5` | `opacity: 0.5` | `opacity: 0.5` |
| Box-Shadow | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` | `[TODO: aus Projekt-:root]` | `none` |
| Übergang | `all 0.3s ease` | `all 0.3s ease` | `all 0.3s ease` | `all 0.3s ease` |

### 4.2 Eingabefelder

| Eigenschaft | CSS-Variable / Wert | Beschreibung |
|-------------|---------------------|--------------|
| Hintergrund | `--bg-input` | Normaler Zustand |
| Hintergrund Fokus | `--bg-input-focus` | Bei Fokus |
| Border | `[TODO: aus Projekt-:root]` | Normaler Rand |
| Border Fokus | `[TODO: aus Projekt-:root]` | Rand bei Fokus (z.B. Glow, Farbwechsel) |
| Border Fehler | `--border-color-error` | Validierungsfehler |
| Textfarbe | `--text-primary` | Eingegebener Text |
| Placeholder-Farbe | `--text-disabled` | Placeholder-Text |
| Padding | `[TODO: aus Projekt-:root]` | Innenabstand |
| Border-Radius | `--radius-sm` | Ecken |
| Min-Höhe | `[TODO: aus Projekt-:root]` | Desktop |
| Min-Höhe Touch | `44px` | Mobile |
| Autocomplete | `off` / `new-password` | Browser-Autofill unterdrücken |

### 4.3 Chat-Eingabefeld (Textarea)

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Breite | `100%` | Volle Breite, kein verschenkter Platz |
| Höhe inaktiv | `44px` (eine Zeile) | Kollabiert wenn Fokus verloren. Zeigt letzte eingegebene Zeile |
| Höhe aktiv | `~33dvh` (~1/3 Bildschirm) | Expandiert bei Fokus. Ergibt zusammen mit Tastatur (~1/3) noch ~1/3 sichtbaren Chat |
| Expansion | Sanfte CSS-Transition | Kein harter Sprung, smooth expand/collapse |
| Overflow | `auto` (scroll) | Bei sehr langen Eingaben innerhalb der 1/3-Höhe scrollen |
| Vollbild-Modal | ja | Optionaler Vollbild-Modus für sehr lange Texte (`#fullscreen-modal`) |

### 4.4 Dropdowns & Selects

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Hintergrund | `[TODO: aus Projekt-:root]` | Dropdown-Container |
| Hintergrund Option Hover | `[TODO: aus Projekt-:root]` | Hovered Option |
| Hintergrund Option Aktiv | `[TODO: aus Projekt-:root]` | Ausgewählte Option |
| Max-Höhe | `[TODO: aus Projekt-:root]` | Scroll bei vielen Optionen |
| Border | `[TODO: aus Projekt-:root]` | Rand des Dropdown-Containers |
| Box-Shadow | `[TODO: aus Projekt-:root]` | Elevation/Schatten |
| Z-Index | `--z-dropdown` | Über dem Content |
| Animation | `[TODO: aus Projekt-:root]` | Öffnen/Schließen |

---

## 5. Icons

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Icon-Set | Emoji | Unicode-Emojis als Icon-System (☰ Navigation, 🔧 Settings, 💾 Export, 📌 Pinned, 📋 Sessions) |
| Standardgröße | `[TODO: aus Projekt-:root]` | Normale Icons in Text/Buttons |
| Große Icons | `[TODO: aus Projekt-:root]` | Tab-Icons, Nav-Icons |
| Farbe | `inherit` | Standard-Icon-Farbe |
| Touch-Target | `44px` | Klickbereich um Icons herum (unabhängig von Icon-Größe) |

---

## 6. Animationen & Übergänge

| Eigenschaft | CSS-Variable | Wert | Beschreibung |
|-------------|-------------|------|--------------|
| Schnell | `--transition-fast` | `[TODO: aus Projekt-:root]` | Hover, Fokus, kleine Zustandswechsel |
| Normal | `--transition-base` | `all 0.3s ease` | Modals, Dropdowns, Panels |
| Langsam | `--transition-slow` | `[TODO: aus Projekt-:root]` | Seitenübergänge, große Animationen |
| Sehr langsam | `--transition-ambient` | `all 12s ease-in-out` | Sentiment-Ambient-Farbwechsel (10–15s Fade) |
| Easing | `--easing-default` | `ease` | Standard-Easing |
| Reduce-Motion | — | `@media (prefers-reduced-motion: reduce)` | Animationen respektieren, auf Minimum reduzieren |
| Spinner | — | `@keyframes spin` | Typing-Indicator Spinner-Rad |

---

## 7. Schatten & Elevation

| Stufe | CSS-Variable | Wert | Einsatz |
|-------|-------------|------|---------|
| Keiner | `--shadow-none` | `none` | Flache Elemente |
| Niedrig | `--shadow-sm` | `[TODO: aus Projekt-:root]` | Cards, Buttons mit Tiefe |
| Mittel | `--shadow-md` | `[TODO: aus Projekt-:root]` | Dropdowns, erhöhte Panels |
| Hoch | `--shadow-lg` | `[TODO: aus Projekt-:root]` | Modals, Toasts |
| Innen | `--shadow-inset` | `[TODO: aus Projekt-:root]` | Eingedrückte Inputs, Toggle-Tracks |
| Sentiment | `--shadow-sentiment` | `none` (default) | Dynamisch: wird bei Sentiment-Stufe 2 auf aktuelle Sentiment-Farbe gesetzt |

---

## 8. Chat-Nachrichten — Collapse-System

### 8.1 User-Bubbles

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Auto-Collapse | ja, bei > 2 Zeilen | Nachrichten mit mehr als 2 Zeilen werden automatisch eingeklappt |
| Collapse-Default | eingeklappt | User-Nachrichten sind standardmäßig eingeklappt (sobald gesendet) |
| Preview bei Collapse | letzte Zeile | Zeigt die letzte Zeile des Textes — User weiß wo er zuletzt war |
| Aufklappen | Tap auf Bubble | Tap klappt auf/zu |
| Animation | `--transition-base` | Sanftes Expand/Collapse |

### 8.2 LLM-Ausgaben

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Einklappbar | ja, per Toggle | Dreieck-Icon (▶ eingeklappt / ▼ aufgeklappt) |
| Collapse-Default | aufgeklappt | LLM-Antworten sind standardmäßig sichtbar |
| Preview bei Collapse | erste Zeile | Zeigt den Anfang der Antwort als Orientierung |
| Toggle-Position | links oben an der Nachricht | Dreieck + erste Zeile als Überschrift |
| Breite | `100%` | Volle Bildschirmbreite, kein Avatar-Einzug |

### 8.3 Reasoning-Block

Wird angezeigt wenn das LLM Reasoning/Thinking-Output liefert (z.B. `<think>`-Tags, `thinking`-Parameter).

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Position | über der eigentlichen Antwort | Reasoning kommt zuerst, Antwort folgt darunter |
| Default-Zustand | eingeklappt | User sieht primär die Antwort, kann Reasoning aufklappen |
| Toggle | Dreieck-Icon + Label "Reasoning" / "Gedankengang" | Klickbar zum Auf-/Zuklappen |
| Einrückung | `--space-md` nach rechts | Leicht nach rechts verschoben gegenüber der Antwort |
| Linke Begrenzung | halbtransparenter vertikaler Strich (`--border-color-light`, `opacity: 0.4`) | Visuell eingefasst, "Gedanke, nicht Sprache" |
| Opacity | `0.7–0.8` | Reduzierte Deckkraft — wirkt wie ein Gedanke, nicht ganz stofflich |
| Saturation | reduziert (`filter: saturate(0.7)`) | Dezenter als die eigentliche Antwort |
| Antwort-Reset | Antwort setzt am linken Rand an, volle Opacity | Klarer visueller Bruch: Reasoning → Antwort |

---

## 9. LLM-Icon-Anzeige

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Position | oben links an der LLM-Nachricht, neben dem Collapse-Toggle | Klein, nicht dominant |
| Quelle | OpenRouter Modell-API (`icon`-Feld) oder Provider-Logo | Wird automatisch geladen |
| Fallback | Erster Buchstabe des Modellnamens als Badge | Wenn kein Icon verfügbar |
| Größe | `20–24px` | Klein genug um nicht zu stören, groß genug um erkennbar zu sein |
| Wechsel bei Reasoning | Zeigt das tatsächlich verwendete Modell | Wenn Intent-Router auf Reasoning-Modell switcht → anderes Icon sichtbar |

---

## 10. Sentiment-Ambient-Lighting

Sanfter Farbschimmer der gesamten Oberfläche basierend auf der Stimmung des Users.

### 10.1 Trigger & Datenquelle

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Quelle | nur User-Stimmung | LLM-Ausgaben werden NICHT ausgewertet |
| Bedingung | BERT + Prosodie müssen übereinstimmen (Konsens) | Nur BERT allein → kein Effekt (zu wackelig). Nur bei Prosodie+BERT-Konsens |
| Auswertungsfenster | alle 2 Nachrichten | Gemittelt über die letzten 2–3 User-Nachrichten |
| Abschaltbar | ja | Komplett deaktivierbar in den Einstellungen |

### 10.2 Farbmapping

| Stimmung | CSS-Variable | Farbrichtung | Beschreibung |
|----------|-------------|-------------|--------------|
| Neutral/Ausgeglichen | `--sentiment-neutral` | keiner oder hauchzartes Blau | Kein merklicher Effekt |
| Wut/Frustration | `--sentiment-anger` | Rot-Schimmer | `[TODO: aus Projekt-:root]` — z.B. `rgba(220, 40, 40, ...)` |
| Freude/Begeisterung | `--sentiment-joy` | Warmes Gold/Gelb | `[TODO: aus Projekt-:root]` — z.B. `rgba(255, 200, 50, ...)` |
| Nachdenklich/Philosophisch | `--sentiment-contemplative` | Violett/Indigo | `[TODO: aus Projekt-:root]` — z.B. `rgba(100, 60, 180, ...)` |
| Technisch/Sachlich | `--sentiment-technical` | Kühles Blau | `[TODO: aus Projekt-:root]` — z.B. `rgba(40, 100, 200, ...)` |

### 10.3 Stufen & Verstärkung

| Stufe | Opacity-Bereich | Effekt | Beschreibung |
|-------|----------------|--------|--------------|
| 0 — Neutral | `0%` | Kein Schimmer | Ausgangszustand |
| 1 — Zart | `3–6%` | Hintergrund-Schimmer | Kaum merklich, fällt erst nach 2–3 Prompts auf |
| 2 — Erkennbar | `6–9%` | Hintergrund + Bubble-Schatten nehmen Farbe an | Stimmung hält an → Schimmer verstärkt sich |
| 3 — Deutlich | `9–12%` | Wie Stufe 2, intensiver | Lange konsistente Stimmung (6+ Nachrichten) |
| Max | `15%` | Maximale Intensität, nie überschritten | Deckel. Auch bei 100 konsistenten Nachrichten nie mehr als 15% |

**Verstärkung:** +3% Opacity pro konsistentem Auswertungsfenster (alle 2 Nachrichten). Bei Stimmungswechsel: Abbau über dieselbe Zeitkonstante (10–15s Fade) auf den neuen Wert.

### 10.4 Timing

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Fade-In | `10–15s` (`--transition-ambient`) | So langsam, dass man den Wechsel nicht bewusst wahrnimmt |
| Fade-Out | `10–15s` | Symmetrisch zum Fade-In |
| Kein harter Sprung | CSS-Transition, kein Step-Wechsel | Immer fließend, nie "klack" |
| Effekt-Ort | `--bg-app` bekommt halbtransparentes Overlay in Sentiment-Farbe | Gesamte Chat-Fläche |
| Stufe-2-Zusatz | `--shadow-sentiment` auf Bubble-Shadows | Schatten nehmen Sentiment-Farbe an |

---

## 11. Scroll-Navigationsleiste

Vertikale Navigationsleiste am linken Bildschirmrand mit Ankerpunkten für jede LLM-Antwort.

### 11.1 Aussehen

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Position | linker Bildschirmrand | Außerhalb der Swipe-Back-Zone (iOS) und Daumen-Scroll-Zone (rechts) |
| Opacity | `0.25` (75% transparent) | Dezent, stört den Chat-Content nicht |
| Design | Vertikaler Strich mit Gabelungs-Punkten | Der Strich gabelt sich zu einem kleinen Oval pro LLM-Antwort und führt wieder zusammen — organisch, wie Nervenbahnen |
| Punkt-Abstand | fester Abstand (`[TODO: aus Projekt-:root]`px) | Immer gleiche Abstände, keine Kompression |
| Scrollbar der Leiste | ja, eigenständig scrollbar | Bei vielen Antworten: Touch auf der Leiste scrollt nur die Leiste, nicht den Chat |
| Farbe | `--text-secondary` oder `--border-color-light` | Passt sich dem Theme an |

### 11.2 Verhalten

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Sichtbarkeit | versteckt (default) | Nicht permanent sichtbar |
| Erscheinen | nach ~1s aktivem Scrollen | Bildschirm muss "wackeln" — erst dann Fade-In |
| Fade-In | `--transition-base` (0.3s) | Sanftes Einblenden |
| Fade-Out | nach 2–3s Scroll-Stillstand | Verschwindet wieder wenn nicht gebraucht |
| Klick-Delay | `300ms` | Punkte werden erst nach 300ms Stillstand klickbar — verhindert versehentliche Sprünge |
| Klick-Aktion | Scrollt Chat zu der entsprechenden LLM-Antwort | Smooth-Scroll zum Ankerpunkt |

---

## 12. Sidebar / Hamburger-Menü

### 12.1 Verhalten

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Öffnungs-Methode | Content schiebt zur Seite | KEIN Overlay/Überklappen — der Chat-Content rutscht nach rechts, Sidebar schiebt sich von links rein |
| Animation | `--transition-base` | Sanftes Slide |
| Schließen | Tap außerhalb oder Hamburger-Icon erneut | Standard-Pattern |

### 12.2 Aufbau (von oben nach unten)

| Position | Element | Beschreibung |
|----------|---------|--------------|
| Ganz oben | 🔍 Lupe / Suchfeld | Durchsucht Chat-Historie |
| Darunter | "Neuer Chat" Button | Startet neue Session |
| Darunter | "Projekte" Button | Navigiert zur Projektseite (eigene View) |
| Mitte | Chat-Historie | Liste der bisherigen Chats, scrollbar |
| Unten (fixiert) | Einstellungen + Abmelden | Immer sichtbar, kein Scrollen nötig. 44px Touch-Targets |

---

## 13. Projektseite

Eigene View, erreichbar über Sidebar → "Projekte". NICHT in den Einstellungen.

### 13.1 Projektübersicht

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Suchleiste | oben | Durchsucht Projektnamen |
| Sortierung | wählbar: "Letzter Zugriff" oder "Name" | Toggle oder Dropdown |
| Favoriten | eigene Sektion oben, angepinnt | Folgen derselben Sortierlogik (Zugriff oder Name) untereinander |
| Trennung | Visueller Separator zwischen angepinnten und normalen Projekten | Klar erkennbar |
| "Neues Projekt" | versteckt, Pull-Gesture ganz oben | Nur sichtbar wenn man am oberen Rand nochmal nach unten zieht. Bewusst versteckt (Anti-Clutter) |

### 13.2 Projekt-Detailansicht

| Eigenschaft | Beschreibung |
|-------------|--------------|
| Anweisungen | Projektanweisungen / System-Prompt für das Projekt |
| Ressourcen | Projektdateien, hochgeladene Dokumente |
| Chat-Liste | Alle Chats innerhalb dieses Projekts |
| "Neuer Chat" Button | Startet neuen Chat in diesem Projekt |

---

## 14. UX-Prinzipien

### 14.1 Automatisierung über manuelle Kontrolle

| Prinzip | Beschreibung |
|---------|--------------|
| Kein manueller Reasoning-Toggle | Intent-Router entscheidet automatisch per effort_score ob ein Reasoning-Modell verwendet wird. User spürt keine Reibung |
| Show, don't tell | Modell-Wechsel wird über LLM-Icon sichtbar gemacht, aber nicht per Text/Toast angekündigt |
| Sentiment passiv | Ambient-Lighting reagiert auf den User, ohne dass er es aktivieren muss |

### 14.2 Intent-Router → Reasoning-Mapping (UX-Seite)

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Trigger | `effort_score > [SCHWELLWERT]` | Ab einem bestimmten Effort-Score switcht der Router auf das Reasoning-Modell |
| Modell-Mapping | Config pro Modell | Jedes Modell hat eine optionale `reasoning_variant` — entweder ein separates Modell oder ein API-Parameter |
| Kein Reasoning verfügbar | Standardmodell bleibt | Wenn `reasoning_variant: null` → kein Switch, kein Fehler |
| UI-Feedback | LLM-Icon wechselt | Einziges sichtbares Zeichen des Switches |

### 14.3 Mobile-First-Regeln

| Regel | Beschreibung |
|-------|--------------|
| Touch-Targets | Minimum `44px` auf allen interaktiven Elementen |
| `:active` statt `:hover` | Für alle Touch-Interaktionen. `:hover` nur als Enhancement auf Desktop |
| `dvh` statt `vh` | Dynamische Viewport-Höhe respektiert Mobile-Keyboard |
| Daumen-Zone | Wichtige Aktionen im unteren Bildschirmbereich |
| Swipe-Konflikte vermeiden | Rechter Rand = iOS Swipe-Back. Linker Rand = Sidebar-Swipe. Interaktive Elemente nicht an den äußersten Rändern |

---

## 15. Theme-System

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Themes | Dark (Standard), weitere via Color-Picker | Verfügbare Themes |
| Standard-Theme | Dark | Default beim ersten Besuch |
| Speicherung | `localStorage` Keys: `nala_theme`, `nala_last_active_favorite`, `nala_fav_1`…`nala_fav_3` (v2-Schema) | Persistenz über Browser-Neustart |
| FOUC-Vermeidung | Early-Load-IIFE im `<head>` | Prüft `nala_last_active_favorite` zuerst, liest v2-Slot, wendet CSS-Props an bevor Body rendert |
| CSS-Variablen-Root | `:root` | Wo werden Variablen gesetzt |
| User-Customization | Color-Picker + Presets | User darf Farben anpassen (Theme-Farben + Bubble-Farben separat) |
| Favoriten-Slots | 3 | Speicherbare Theme-Presets |
| Was wird gespeichert | Theme + Bubble-Farben + Schriftgröße + UI-Skalierung (v2-Schema) | Umfang eines Favoriten-Slots |
| Hintergrundbild | im Favoriten-Slot mitgespeichert | URL + Opacity + Skalierung |
| Reset | `resetTheme()` → ruft `resetAllBubbles()` + `resetFontSize()` + `resetUiScale()` mit auf | Vollständiger Reset aller Overrides |

---

## 16. Accessibility

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Kontrast-Ziel | WCAG AA | Mindest-Kontrastverhältnis |
| Fokus-Indikator | `[TODO: aus Projekt-:root]` | Sichtbarer Fokus-Ring (Farbe, Breite, Offset) |
| Skip-Link | nein | Noch nicht implementiert |
| Aria-Labels | Pflicht auf allen interaktiven Elementen | Screenreader-Support |
| Reduce-Motion | respektieren | Animationen auf Minimum bei User-Präferenz. Sentiment-Fade → sofortiger Wechsel |
| Skalierung | 2-Achsen-System (siehe 2.5) | User kann UI und Schrift unabhängig anpassen |
| Farbblindheit | Farbe nie als einziger Informationsträger | Immer zusätzlich Icon/Text. Gilt auch für Sentiment-Schimmer — rein dekorativ, transportiert keine kritische Information |

---

## 17. Dokumentations-Stil (für Schulungen / Shop-Floor)

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Farbkodierung Warnungen | Rot: Gefahr, Grün: Tipp, Teal: Hintergrund | Konsistente `border-left` + Hintergrund |
| Click-Path-Format | Monospace mit Pfeilen: `Set Camera → Live-Bild → ...` | Schnell scannbar |
| Profi/Rookie-Toggle | `body.expert-mode .step-detail { display: none }` | Ein Toggle steuert alle Details |
| Reset-Button Position | Ende des Dokuments, nicht Header | Stört nicht den Arbeitsfluss |
| Fortschritts-Persistenz | localStorage pro Dokument | Checkboxen-Stand überleben Reload |

---

## Offene Werte — Nächster UI-Patch ausfüllen

Die folgenden Werte müssen beim nächsten UI-Patch direkt aus dem `:root`-Block extrahiert werden:

- **1.1 Kernfarben:** Alle Hex-Werte für Primary, Secondary, Accent und deren Hover/Muted-Varianten
- **1.2 Hintergründe:** `--bg-app`, `--bg-surface`, `--bg-surface-raised`, `--bg-sidebar`, `--bg-input`
- **1.3 Textfarben:** `--text-primary`, `--text-secondary`, `--text-disabled`, etc.
- **1.4 Statusfarben:** Success/Warning/Error/Info Hex-Werte
- **1.5 Randfarben:** Alle `--border-color-*` Werte
- **2.1 Fonts:** Font-Familien, Ladestrategie
- **3.1 Spacing:** Gesamte Spacing-Skala
- **3.2 Border-Radius:** `--radius-sm`, `--radius-md`, `--radius-lg`
- **3.4 Z-Index:** Alle Z-Index-Stufen
- **4.x Komponenten:** Padding-Werte, Min-Höhen, Box-Shadows
- **7. Schatten:** Alle `--shadow-*` Werte
- **11.1 Scroll-Nav:** Punkt-Abstand in Pixel

---

## Änderungshistorie

| Datum | Beschreibung |
|-------|--------------|
| 2026-04-24 | Initiale Struktur angelegt (alle Werte als Platzhalter) |
| 2026-04-24 | Erste Befüllung aus Lessons/SUPERVISOR: Bubble-Defaults, Font-Presets, Theme-System, Touch-Regeln, Spinner-Typ, Sidebar-Inhalt, Landscape, Modal-Handling, CDN-Deps, Anti-Invariante dokumentiert. ~40% der Werte befüllt |
| 2026-05-07 | Große Erweiterung: Sentiment-Ambient-Lighting (Sek. 10), Scroll-Nav (11), Sidebar-Aufbau (12), Projektseite (13), UX-Prinzipien (14), Chat-Collapse-System (8), Reasoning-Block-Styling (8.3), LLM-Icon (9), 2-Achsen-Skalierung (2.5), Hintergrundbild (1.8), Chat-Eingabefeld-Verhalten (4.3), Layout-Grundregel (3.5). Font-Presets durch Stepper-System ersetzt. Theme-System um Hintergrundbild + UI-Scale erweitert |
| 2026-05-17 | Geltungsbereich-Sektion am Anfang ergänzt: DESIGN.md ist UI-Layer, Marathon-Workflow (Rollen, Faulheits-Catches, Handover-Round-Trip, Bibel-Format, Bootstrap) ist explizit in README/GLOBAL_LESSONS/SUPERVISOR_KODEX/PROJECT_BOOTSTRAP_README dokumentiert, nicht hier. Werte unverändert |
