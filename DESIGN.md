# DESIGN.md — Globale Design-Referenz

⚠️ **DIESES REPO IST PUBLIC.** Keine Secrets, Keys, IPs, interne URLs.

Diese Datei ist die zentrale Design-Referenz für alle Projekte.
Sie wird NICHT kopiert — Projekte referenzieren sie direkt aus dem Repo.
Werte die noch nicht festgelegt sind, stehen als `[WERT]`.

Bei jedem UI-Patch: Diese Datei konsultieren. Neue Design-Entscheidungen hier eintragen.

---

## 1. Farbsystem

### 1.1 Kernfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Primär | `--color-primary` | `[WERT]` | Hauptfarbe, Buttons, aktive Elemente, Highlights |
| Primär Hover | `--color-primary-hover` | `[WERT]` | Hover/Active-Zustand der Primärfarbe |
| Primär gedämpft | `--color-primary-muted` | `[WERT]` | Dezente Variante für Hintergründe, Badges |
| Sekundär | `--color-secondary` | `[WERT]` | Ergänzungsfarbe, sekundäre Buttons |
| Sekundär Hover | `--color-secondary-hover` | `[WERT]` | Hover/Active-Zustand der Sekundärfarbe |
| Akzent | `--color-accent` | `[WERT]` | Eyecatcher, sparsam einsetzen (Sterne, Badges, Highlights) |

### 1.2 Hintergrundfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| App-Hintergrund | `--bg-app` | `[WERT]` | Gesamter Seitenhintergrund |
| Flächen-Hintergrund | `--bg-surface` | `[WERT]` | Cards, Panels, Container |
| Flächen-Hintergrund erhöht | `--bg-surface-raised` | `[WERT]` | Modals, Dropdowns, Overlays |
| Sidebar-Hintergrund | `--bg-sidebar` | `[WERT]` | Navigation, Seitenleisten |
| Input-Hintergrund | `--bg-input` | `[WERT]` | Eingabefelder, Textareas |
| Input-Hintergrund Fokus | `--bg-input-focus` | `[WERT]` | Eingabefeld bei Fokus |

### 1.3 Textfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Text primär | `--text-primary` | `[WERT]` | Haupttextfarbe, Fließtext |
| Text sekundär | `--text-secondary` | `[WERT]` | Weniger wichtiger Text, Labels, Timestamps |
| Text deaktiviert | `--text-disabled` | `[WERT]` | Inaktive Elemente, Placeholder |
| Text invertiert | `--text-inverted` | `[WERT]` | Text auf dunklem/hellem Gegenhintergrund |
| Text auf Primärfarbe | `--text-on-primary` | `[WERT]` | Text auf primärfarbigem Hintergrund (Buttons) |
| Link | `--text-link` | `[WERT]` | Hyperlinks, klickbare Textelemente |
| Link besucht | `--text-link-visited` | `[WERT]` | Bereits besuchte Links |

### 1.4 Statusfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Erfolg | `--color-success` | `[WERT]` | Bestätigungen, "gespeichert", grüne Häkchen |
| Erfolg Hintergrund | `--color-success-bg` | `[WERT]` | Hintergrund für Erfolgs-Banner/Badges |
| Warnung | `--color-warning` | `[WERT]` | Hinweise, "Achtung", noch kein Fehler |
| Warnung Hintergrund | `--color-warning-bg` | `[WERT]` | Hintergrund für Warn-Banner |
| Fehler | `--color-error` | `[WERT]` | Fehlermeldungen, Validierung fehlgeschlagen |
| Fehler Hintergrund | `--color-error-bg` | `[WERT]` | Hintergrund für Fehler-Banner |
| Info | `--color-info` | `[WERT]` | Neutrale Hinweise, Tooltips, Erklärungen |
| Info Hintergrund | `--color-info-bg` | `[WERT]` | Hintergrund für Info-Banner |

### 1.5 Randfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Rand Standard | `--border-color` | `[WERT]` | Normale Trennlinien, Card-Rahmen |
| Rand leicht | `--border-color-light` | `[WERT]` | Subtile Trenner, Tabellenlinien |
| Rand Fokus | `--border-color-focus` | `[WERT]` | Eingabefelder bei Fokus, aktive Tabs |
| Rand Fehler | `--border-color-error` | `[WERT]` | Validierungsfehler an Eingabefeldern |

### 1.6 Spezialfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| User-Bubble Hintergrund | `--bubble-user-bg` | `[WERT]` | Chat: Hintergrund der User-Nachrichten |
| User-Bubble Text | `--bubble-user-text` | `[WERT]` | Chat: Textfarbe in User-Nachrichten |
| Bot-Bubble Hintergrund | `--bubble-bot-bg` | `[WERT]` | Chat: Hintergrund der Bot-Nachrichten |
| Bot-Bubble Text | `--bubble-bot-text` | `[WERT]` | Chat: Textfarbe in Bot-Nachrichten |
| Overlay/Backdrop | `--color-overlay` | `[WERT]` | Halbdurchsichtiger Hintergrund hinter Modals |
| Schatten | `--color-shadow` | `[WERT]` | Box-Shadow-Farbe für Elevation |
| Scrollbar Track | `--scrollbar-track` | `[WERT]` | Scrollbar-Hintergrund |
| Scrollbar Thumb | `--scrollbar-thumb` | `[WERT]` | Scrollbar-Griff |

### 1.7 Dark/Light Mode

| Eigenschaft | Beschreibung |
|-------------|--------------|
| Standard-Modus | `[dark / light / system]` |
| Umschaltbar | `[ja / nein]` |
| Speicherung | `[localStorage Key oder WERT]` |
| FOUC-Vermeidung | `[Early-Load-IIFE im <head> / anderer Mechanismus]` |

---

## 2. Typography

### 2.1 Schriftarten

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Hauptschrift | `--font-family-base` | `[WERT]` | Fließtext, UI-Elemente |
| Monospace | `--font-family-mono` | `[WERT]` | Code, Klickpfade, technische Werte |
| Display/Headline | `--font-family-display` | `[WERT]` | Große Überschriften, Titel (optional, kann gleich wie Base sein) |
| Quelle | — | `[Google Fonts / lokal / inline]` | Wie werden Fonts geladen |

### 2.2 Größen-Skala

| Stufe | CSS-Variable | Wert | Einsatz |
|-------|-------------|------|---------|
| XS | `--font-size-xs` | `[WERT]` | Timestamps, Badges, Footnotes |
| SM | `--font-size-sm` | `[WERT]` | Labels, Hilfstexte, Captions |
| Base | `--font-size-base` | `[WERT]` | Fließtext, Inputs, Buttons |
| MD | `--font-size-md` | `[WERT]` | Hervorgehobener Text, Card-Titel |
| LG | `--font-size-lg` | `[WERT]` | Abschnitts-Überschriften (H3) |
| XL | `--font-size-xl` | `[WERT]` | Seitenüberschriften (H2) |
| XXL | `--font-size-xxl` | `[WERT]` | Haupttitel (H1), Hero-Text |

### 2.3 Zeilenhöhen

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Eng | `--line-height-tight` | `[WERT]` | Überschriften, Buttons |
| Normal | `--line-height-base` | `[WERT]` | Fließtext |
| Weit | `--line-height-relaxed` | `[WERT]` | Lesestoff, lange Absätze |

### 2.4 Schriftgewichte

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Normal | `--font-weight-normal` | `[WERT]` | Fließtext |
| Medium | `--font-weight-medium` | `[WERT]` | Labels, leichte Hervorhebung |
| Bold | `--font-weight-bold` | `[WERT]` | Überschriften, starke Hervorhebung |

### 2.5 Schriftgrößen-Presets (User-wählbar)

| Preset | Base-Wert | Beschreibung |
|--------|-----------|--------------|
| Klein | `[WERT]` | Kompakte Ansicht |
| Normal | `[WERT]` | Standard |
| Groß | `[WERT]` | Bessere Lesbarkeit |
| Extra groß | `[WERT]` | Accessibility, ältere Nutzer |

---

## 3. Spacing & Layout

### 3.1 Spacing-Skala

| Stufe | CSS-Variable | Wert | Typischer Einsatz |
|-------|-------------|------|-------------------|
| 2XS | `--space-2xs` | `[WERT]` | Inline-Abstände, Icon-Gaps |
| XS | `--space-xs` | `[WERT]` | Enge Abstände innerhalb von Gruppen |
| SM | `--space-sm` | `[WERT]` | Padding in kleinen Elementen |
| MD | `--space-md` | `[WERT]` | Standard-Padding, Card-Innenabstand |
| LG | `--space-lg` | `[WERT]` | Abstand zwischen Sektionen |
| XL | `--space-xl` | `[WERT]` | Große Sektionsabstände |
| 2XL | `--space-2xl` | `[WERT]` | Seitenränder, Hero-Abstände |

### 3.2 Border-Radius

| Stufe | CSS-Variable | Wert | Einsatz |
|-------|-------------|------|---------|
| Keiner | `--radius-none` | `0` | Scharfe Kanten (bewusst eckig) |
| Klein | `--radius-sm` | `[WERT]` | Buttons, Inputs, Badges |
| Standard | `--radius-md` | `[WERT]` | Cards, Panels |
| Groß | `--radius-lg` | `[WERT]` | Modals, große Container |
| Rund | `--radius-full` | `9999px` | Avatare, runde Buttons, Pills |

### 3.3 Breakpoints

| Name | CSS-Variable | Wert | Beschreibung |
|------|-------------|------|--------------|
| Mobile S | `--bp-mobile-s` | `[WERT]` | Kleine Smartphones (SE, Mini) |
| Mobile | `--bp-mobile` | `[WERT]` | Standard-Smartphones |
| Tablet | `--bp-tablet` | `[WERT]` | Tablets, große Phones im Landscape |
| Desktop | `--bp-desktop` | `[WERT]` | Laptops, Desktops |
| Wide | `--bp-wide` | `[WERT]` | Große Monitore |

### 3.4 Z-Index-Skala

| Ebene | CSS-Variable | Wert | Einsatz |
|-------|-------------|------|---------|
| Basis | `--z-base` | `[WERT]` | Normaler Content |
| Sticky | `--z-sticky` | `[WERT]` | Sticky Header, Tab-Leisten |
| Dropdown | `--z-dropdown` | `[WERT]` | Dropdowns, Autocomplete |
| Modal-Backdrop | `--z-backdrop` | `[WERT]` | Overlay hinter Modal |
| Modal | `--z-modal` | `[WERT]` | Modals, Dialoge |
| Toast | `--z-toast` | `[WERT]` | Benachrichtigungen, Toasts |
| Tooltip | `--z-tooltip` | `[WERT]` | Tooltips, immer oben |

---

## 4. Komponenten

### 4.1 Buttons

| Eigenschaft | Primär | Sekundär | Danger | Ghost |
|-------------|--------|----------|--------|-------|
| Hintergrund | `--color-primary` | `--bg-surface` | `--color-error` | `transparent` |
| Textfarbe | `--text-on-primary` | `--text-primary` | `[WERT]` | `--text-primary` |
| Border | `none` | `1px solid --border-color` | `none` | `none` |
| Border-Radius | `--radius-sm` | `--radius-sm` | `--radius-sm` | `--radius-sm` |
| Padding | `[WERT]` | `[WERT]` | `[WERT]` | `[WERT]` |
| Min-Höhe | `[WERT]` | `[WERT]` | `[WERT]` | `[WERT]` |
| Min-Höhe Touch | `44px` | `44px` | `44px` | `44px` |
| Hover-Effekt | `[WERT]` | `[WERT]` | `[WERT]` | `[WERT]` |
| Active-Effekt | `[WERT]` | `[WERT]` | `[WERT]` | `[WERT]` |
| Disabled | `opacity: [WERT]` | `opacity: [WERT]` | `opacity: [WERT]` | `opacity: [WERT]` |
| Box-Shadow | `[WERT]` | `[WERT]` | `[WERT]` | `none` |
| Übergang | `[WERT]` | `[WERT]` | `[WERT]` | `[WERT]` |

### 4.2 Eingabefelder

| Eigenschaft | CSS-Variable / Wert | Beschreibung |
|-------------|---------------------|--------------|
| Hintergrund | `--bg-input` | Normaler Zustand |
| Hintergrund Fokus | `--bg-input-focus` | Bei Fokus |
| Border | `[WERT]` | Normaler Rand |
| Border Fokus | `[WERT]` | Rand bei Fokus (z.B. Glow, Farbwechsel) |
| Border Fehler | `--border-color-error` | Validierungsfehler |
| Textfarbe | `--text-primary` | Eingegebener Text |
| Placeholder-Farbe | `--text-disabled` | Placeholder-Text |
| Padding | `[WERT]` | Innenabstand |
| Border-Radius | `--radius-sm` | Ecken |
| Min-Höhe | `[WERT]` | Desktop |
| Min-Höhe Touch | `44px` | Mobile |
| Textarea Expand | `[WERT]` | Auto-Expand-Verhalten (min/max Höhe) |
| Textarea Vollbild | `[ja/nein]` | Vollbild-Modal für lange Texte |
| Autocomplete | `off` / `new-password` | Browser-Autofill unterdrücken |

### 4.3 Dropdowns & Selects

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Hintergrund | `[WERT]` | Dropdown-Container |
| Hintergrund Option Hover | `[WERT]` | Hovered Option |
| Hintergrund Option Aktiv | `[WERT]` | Ausgewählte Option |
| Max-Höhe | `[WERT]` | Scroll bei vielen Optionen |
| Border | `[WERT]` | Rand des Dropdown-Containers |
| Box-Shadow | `[WERT]` | Elevation/Schatten |
| Z-Index | `--z-dropdown` | Über dem Content |
| Animation | `[WERT]` | Öffnen/Schließen (z.B. slideDown, fade) |

### 4.4 Modals & Dialoge

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Hintergrund | `--bg-surface-raised` | Modal-Fläche |
| Overlay | `--color-overlay` | Hintergrund-Abdunklung |
| Max-Breite | `[WERT]` | Desktop |
| Max-Breite Mobile | `[WERT]` | Mobile (z.B. 95vw) |
| Max-Höhe | `[WERT]` | Scroll bei langem Inhalt |
| Border-Radius | `--radius-lg` | Ecken |
| Box-Shadow | `[WERT]` | Elevation |
| Z-Index | `--z-modal` | Über Backdrop |
| Animation | `[WERT]` | Öffnen/Schließen |
| Schließen-Button | `[Position, Größe]` | X-Button oben rechts |
| Landscape-Anpassung | `[WERT]` | Höhenanpassung bei flachen Viewports |

### 4.5 Cards & Panels

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Hintergrund | `--bg-surface` | Card-Fläche |
| Border | `[WERT]` | Rand |
| Border-Radius | `--radius-md` | Ecken |
| Padding | `[WERT]` | Innenabstand |
| Box-Shadow | `[WERT]` | Elevation |
| Hover-Effekt | `[WERT]` | Falls klickbar |

### 4.6 Tabs & Navigation

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Tab-Hintergrund | `[WERT]` | Inaktiver Tab |
| Tab-Hintergrund Aktiv | `[WERT]` | Aktiver Tab |
| Tab-Textfarbe | `[WERT]` | Inaktiv |
| Tab-Textfarbe Aktiv | `[WERT]` | Aktiv |
| Unterstrich/Highlight | `[WERT]` | Aktiver-Tab-Indikator (Farbe, Dicke) |
| Sticky | `[ja/nein, top-Wert]` | Fixiert beim Scrollen |
| Scroll Horizontal | `[overflow-x: auto]` | Bei vielen Tabs auf Mobile |
| Touch-Target | `44px` | Minimum Höhe |
| Persistenz | `[localStorage Key]` | Aktiver Tab über Reload merken |

### 4.7 Sidebar / Hamburger-Menü

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Breite | `[WERT]` | Sidebar-Breite |
| Hintergrund | `--bg-sidebar` | Sidebar-Fläche |
| Overlay | `[ja/nein]` | Abdunklung des Hauptinhalts |
| Animation | `[WERT]` | Öffnen/Schließen (slide, fade) |
| Trigger | `[Hamburger-Icon / Swipe / beides]` | Wie wird die Sidebar geöffnet |
| Breakpoint | `[WERT]` | Ab wann permanent sichtbar (Desktop) |

### 4.8 Toast-Benachrichtigungen

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Position | `[top-right / bottom-center / ...]` | Wo erscheinen Toasts |
| Dauer | `[WERT]` | Auto-Dismiss in ms |
| Hintergrund Erfolg | `--color-success-bg` | Erfolgs-Toast |
| Hintergrund Fehler | `--color-error-bg` | Fehler-Toast |
| Hintergrund Info | `--color-info-bg` | Info-Toast |
| Animation | `[WERT]` | Ein-/Ausblenden |
| Z-Index | `--z-toast` | Immer sichtbar |
| Max-Breite | `[WERT]` | Begrenzung auf Mobile |

### 4.9 Tooltips

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Hintergrund | `[WERT]` | Tooltip-Blase |
| Textfarbe | `[WERT]` | Tooltip-Text |
| Border-Radius | `[WERT]` | Ecken |
| Padding | `[WERT]` | Innenabstand |
| Max-Breite | `[WERT]` | Zeilenumbruch |
| Pfeil | `[ja/nein]` | Dreieck-Pfeil zum Trigger |
| Trigger | `[hover / click / both]` | Auslöser (Touch: immer click) |
| Delay | `[WERT]` | Verzögerung vor Anzeige |
| Z-Index | `--z-tooltip` | Ganz oben |

### 4.10 Scrollbars

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Breite | `[WERT]` | Scrollbar-Breite (webkit) |
| Track | `--scrollbar-track` | Hintergrund |
| Thumb | `--scrollbar-thumb` | Griff |
| Thumb Hover | `[WERT]` | Griff bei Hover |
| Border-Radius | `[WERT]` | Abrundung des Griffs |
| Verstecken Mobile | `[ja/nein]` | `scrollbar-width: none` auf Touch |

### 4.11 Ladeindikator / Spinner

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Typ | `[spinner / dots / skeleton / pulse]` | Art des Indikators |
| Farbe | `[WERT]` | Spinner/Dots-Farbe |
| Größe | `[WERT]` | Durchmesser/Breite |
| Typing-Bubble | `[ja/nein]` | Springende Punkte bei Chat/LLM-Antwort |
| Skeleton Screens | `[ja/nein]` | Platzhalter-Blocks beim Laden |

### 4.12 Chat-Bubbles

| Eigenschaft | User | Bot/LLM |
|-------------|------|---------|
| Hintergrund | `--bubble-user-bg` | `--bubble-bot-bg` |
| Textfarbe | `--bubble-user-text` | `--bubble-bot-text` |
| Border-Radius | `[WERT]` | `[WERT]` |
| Max-Breite | `[WERT]` | `[WERT]` |
| Padding | `[WERT]` | `[WERT]` |
| Toolbar | `[Welche Buttons: Copy, Retry, Edit, Timestamp]` | `[Welche Buttons]` |
| Toolbar Sichtbarkeit | `[hover / always / touch: always]` | `[hover / always]` |
| Code-Blöcke | `[Hintergrund, Font, Padding]` | `[Hintergrund, Font, Padding]` |

---

## 5. Icons

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Icon-Set | `[Emoji / Lucide / FontAwesome / Custom SVG / Mix]` | Welches Icon-System |
| Standardgröße | `[WERT]` | Normale Icons in Text/Buttons |
| Große Icons | `[WERT]` | Tab-Icons, Nav-Icons |
| Farbe | `[inherit / --text-primary / --color-primary]` | Standard-Icon-Farbe |
| Touch-Target | `44px` | Klickbereich um Icons herum (unabhängig von Icon-Größe) |

---

## 6. Animationen & Übergänge

| Eigenschaft | CSS-Variable | Wert | Beschreibung |
|-------------|-------------|------|--------------|
| Schnell | `--transition-fast` | `[WERT]` | Hover, Fokus, kleine Zustandswechsel |
| Normal | `--transition-base` | `[WERT]` | Modals, Dropdowns, Panels |
| Langsam | `--transition-slow` | `[WERT]` | Seitenübergänge, große Animationen |
| Easing | `--easing-default` | `[WERT]` | Standard-Easing (ease, ease-out, cubic-bezier) |
| Reduce-Motion | — | `@media (prefers-reduced-motion: reduce)` | Animationen respektieren, auf Minimum reduzieren |

---

## 7. Schatten & Elevation

| Stufe | CSS-Variable | Wert | Einsatz |
|-------|-------------|------|---------|
| Keiner | `--shadow-none` | `none` | Flache Elemente |
| Niedrig | `--shadow-sm` | `[WERT]` | Cards, Buttons mit Tiefe |
| Mittel | `--shadow-md` | `[WERT]` | Dropdowns, erhöhte Panels |
| Hoch | `--shadow-lg` | `[WERT]` | Modals, Toasts |
| Innen | `--shadow-inset` | `[WERT]` | Eingedrückte Inputs, Toggle-Tracks |

---

## 8. Mobile-spezifische Regeln

### 8.1 Touch-Grundregeln
- Minimum Touch-Target: `44px` × `44px` — kleinere Buttons werden verfehlt
- `:hover` funktioniert auf Touch nicht → IMMER `:active` als Alternative
- Toolbar-Sichtbarkeit: auf Touch-Geräten immer sichtbar (leicht opak), nicht nur bei Hover
- `backdrop-filter: blur()` braucht Fallback für ältere Browser
- `-webkit-overflow-scrolling: touch` für flüssiges Scroll-Verhalten
- `scrollbar-width: none` für cleane horizontal-scrollbare Bereiche (Tabs)

### 8.2 Viewport-Handling
| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Höheneinheit | `[dvh / vh / svh]` | Welche Viewport-Höhe (dvh gegen Keyboard-Overlap) |
| Keyboard-Anpassung | `[WERT]` | Verhalten wenn Soft-Keyboard aufgeht |
| Safe-Areas | `[env(safe-area-inset-*)]` | iPhone-Notch/Dynamic-Island |

### 8.3 Landscape-Modus
| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Breakpoint | `@media (orientation: landscape) and (max-height: 500px)` | Wann greifen Landscape-Regeln |
| Header | `[Kompaktierung: Höhe, Padding]` | Header schrumpfen |
| Modals | `[Max-Höhe anpassen]` | Modals kleiner |
| Input-Bar | `[Kompaktierung]` | Chat-Eingabe flacher |

### 8.4 Offline / Shop-Floor
| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Externe Abhängigkeiten | `[CDN erlaubt / alles inline]` | Darf das UI CDN-Ressourcen laden |
| Fonts | `[Google Fonts @import / inline / system]` | Font-Ladestrategie |
| Single-File | `[ja/nein]` | Alles in einer HTML-Datei |

---

## 9. Theme-System

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Themes | `[Liste: z.B. Dark, Light, Hel-Gold, Custom]` | Verfügbare Themes |
| Standard-Theme | `[WERT]` | Default beim ersten Besuch |
| Speicherung | `[localStorage Key]` | Persistenz |
| FOUC-Vermeidung | `[Early-Load-IIFE im <head>]` | Flash-of-Unstyled-Content verhindern |
| CSS-Variablen-Root | `[:root / body.theme-X]` | Wo werden Variablen gesetzt |
| User-Customization | `[Color-Picker / Presets / beides]` | Darf der User Farben anpassen |
| Favoriten-Slots | `[Anzahl]` | Speicherbare Theme-Presets |
| Was wird gespeichert | `[Theme + Bubble-Farben + Schriftgröße + ...]` | Umfang eines Favoriten-Slots |

---

## 10. Accessibility

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Kontrast-Ziel | `[WCAG AA / AAA]` | Mindest-Kontrastverhältnis |
| Fokus-Indikator | `[WERT]` | Sichtbarer Fokus-Ring (Farbe, Breite, Offset) |
| Skip-Link | `[ja/nein]` | "Zum Inhalt springen" für Screenreader |
| Aria-Labels | `[Pflicht auf allen interaktiven Elementen]` | Screenreader-Support |
| Reduce-Motion | `[respektieren]` | Animationen auf Minimum bei User-Präferenz |
| Schriftgrößen-Wahl | `[ja/nein, Anzahl Presets]` | User kann Schriftgröße anpassen |
| Farbblindheit | `[Farbe nie als einziger Informationsträger]` | Immer zusätzlich Icon/Text |

---

## 11. Dokumentations-Stil (für Schulungen / Shop-Floor)

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Farbkodierung Warnungen | Rot: Gefahr, Grün: Tipp, Teal: Hintergrund | Konsistente `border-left` + Hintergrund |
| Click-Path-Format | Monospace mit Pfeilen: `Set Camera → Live-Bild → ...` | Schnell scannbar |
| Profi/Rookie-Toggle | `body.expert-mode .step-detail { display: none }` | Ein Toggle steuert alle Details |
| Reset-Button Position | Ende des Dokuments, nicht Header | Stört nicht den Arbeitsfluss |
| Fortschritts-Persistenz | localStorage pro Dokument | Checkboxen-Stand überleben Reload |

---

## Änderungshistorie

| Datum | Beschreibung |
|-------|--------------|
| 2026-04-24 | Initiale Struktur angelegt (alle Werte als Platzhalter) |
