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
| Primär Mittel | `--color-primary-mid` | `[WERT]` | Basis für LLM-Bubble-Background (rgba-Ableitung) |
| Sekundär | `--color-secondary` | `[WERT]` | Ergänzungsfarbe, sekundäre Buttons |
| Sekundär Hover | `--color-secondary-hover` | `[WERT]` | Hover/Active-Zustand der Sekundärfarbe |
| Akzent | `--color-accent` | `[WERT]` | Eyecatcher, sparsam einsetzen (Sterne, Badges, Highlights). Basis für User-Bubble-Background |

### 1.2 Hintergrundfarben

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| App-Hintergrund | `--bg-app` | `[WERT]` | Gesamter Seitenhintergrund (Dark-First) |
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
| User-Bubble Hintergrund | `--bubble-user-bg` | `rgba(236, 64, 122, 0.88)` | Chat: Hintergrund der User-Nachrichten (Akzent-Ableitung mit Alpha) |
| User-Bubble Text | `--bubble-user-text` | `[WERT]` | Chat: Textfarbe in User-Nachrichten |
| Bot-Bubble Hintergrund | `--bubble-llm-bg` | `rgba(26, 47, 78, 0.85)` | Chat: Hintergrund der Bot-Nachrichten (Primary-Mid-Ableitung mit Alpha) |
| Bot-Bubble Text | `--bubble-bot-text` | `[WERT]` | Chat: Textfarbe in Bot-Nachrichten |
| Overlay/Backdrop | `--color-overlay` | `[WERT]` | Halbdurchsichtiger Hintergrund hinter Modals |
| Schatten | `--color-shadow` | `[WERT]` | Box-Shadow-Farbe für Elevation |
| Scrollbar Track | `--scrollbar-track` | `[WERT]` | Scrollbar-Hintergrund |
| Scrollbar Thumb | `--scrollbar-thumb` | `[WERT]` | Scrollbar-Griff |

**Anti-Invariante:** Bubble-Backgrounds dürfen NIE `#000000` oder `transparent` als Default haben — "nie schwarz auf schwarz". Immer rgba-Werte mit Alpha 0.85–0.88 als Basis verwenden. `resetTheme()` muss `resetAllBubbles()` + `resetFontSize()` mitrufen.

### 1.7 Dark/Light Mode

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Standard-Modus | `dark` | Dark-First — Nala ist primär ein Dark-Mode-UI |
| Umschaltbar | ja | Theme-Presets via Settings-Modal |
| Speicherung | `localStorage` Keys: `nala_theme`, `nala_last_active_favorite`, `nala_fav_1`…`nala_fav_3` (v2-Schema) | Persistenz über Browser-Neustart |
| FOUC-Vermeidung | Early-Load-IIFE im `<head>` | Prüft `nala_last_active_favorite` → lädt Fav-Slot (v2: Theme + Bubble + fontSize) → wendet CSS-Props an, bevor Body rendert. Fav hat Vorrang vor flachem `nala_theme` |

---

## 2. Typography

### 2.1 Schriftarten

| Rolle | CSS-Variable | Wert | Beschreibung |
|-------|-------------|------|--------------|
| Hauptschrift | `--font-family-base` | `[WERT]` | Fließtext, UI-Elemente |
| Monospace | `--font-family-mono` | `[WERT]` | Code, Klickpfade, technische Werte |
| Display/Headline | `--font-family-display` | `[WERT]` | Große Überschriften, Titel (optional, kann gleich wie Base sein) |
| Quelle | — | `[WERT]` | Wie werden Fonts geladen |

### 2.2 Größen-Skala

| Stufe | CSS-Variable | Wert | Einsatz |
|-------|-------------|------|---------|
| XS | `--font-size-xs` | `[WERT]` | Timestamps, Badges, Footnotes |
| SM | `--font-size-sm` | `[WERT]` | Labels, Hilfstexte, Captions |
| Base | `--font-size-base` | `15px` (Preset "Normal") | Fließtext, Inputs, Buttons |
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
| Klein | `13px` | Kompakte Ansicht |
| Normal | `15px` | Standard |
| Groß | `17px` | Bessere Lesbarkeit |
| Extra groß | `19px` | Accessibility, ältere Nutzer |

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
| Textfarbe | `--text-on-primary` | `--text-primary` | `#ffffff` | `--text-primary` |
| Border | `none` | `1px solid --border-color` | `none` | `none` |
| Border-Radius | `--radius-sm` | `--radius-sm` | `--radius-sm` | `--radius-sm` |
| Padding | `[WERT]` | `[WERT]` | `[WERT]` | `[WERT]` |
| Min-Höhe | `[WERT]` | `[WERT]` | `[WERT]` | `[WERT]` |
| Min-Höhe Touch | `44px` | `44px` | `44px` | `44px` |
| Hover-Effekt | `--color-primary-hover` | `[WERT]` | `[WERT]` | `[WERT]` |
| Active-Effekt | `[WERT]` | `[WERT]` | `[WERT]` | `[WERT]` |
| Disabled | `opacity: 0.5` | `opacity: 0.5` | `opacity: 0.5` | `opacity: 0.5` |
| Box-Shadow | `[WERT]` | `[WERT]` | `[WERT]` | `none` |
| Übergang | `all 0.3s ease` | `all 0.3s ease` | `all 0.3s ease` | `all 0.3s ease` |

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
| Textarea Vollbild | ja | Vollbild-Modal für lange Texte (`#fullscreen-modal`) |
| Autocomplete | `off` / `new-password` | Browser-Autofill unterdrücken (Firefox-Fix Patch 101) |

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
| Max-Breite Mobile | `95vw` | Mobile |
| Max-Höhe | `[WERT]` | Scroll bei langem Inhalt |
| Border-Radius | `--radius-lg` | Ecken |
| Box-Shadow | `[WERT]` | Elevation |
| Z-Index | `--z-modal` | Über Backdrop |
| Animation | `[WERT]` | Öffnen/Schließen |
| Schließen-Button | `[WERT]` | X-Button oben rechts |
| Landscape-Anpassung | Max-Höhe reduziert bei `max-height: 500px` | Höhenanpassung bei flachen Viewports |
| Backdrop-Close | Zentraler IIFE-Handler am Script-Ende | Klick neben Modal schließt es (`#settings-modal`, `#export-modal`, `#fullscreen-modal`, `#pw-modal`). `#ee-modal` hat eigenen Handler |

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
| Sticky | `[WERT]` | Fixiert beim Scrollen |
| Scroll Horizontal | `overflow-x: auto` + `scrollbar-width: none` | Bei vielen Tabs auf Mobile |
| Touch-Target | `44px` | Minimum Höhe |
| Persistenz | `[WERT]` | Aktiver Tab über Reload merken |

### 4.7 Sidebar / Hamburger-Menü

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Breite | `[WERT]` | Sidebar-Breite |
| Hintergrund | `--bg-sidebar` | Sidebar-Fläche |
| Overlay | ja | Abdunklung des Hauptinhalts |
| Animation | `[WERT]` | Öffnen/Schließen (slide, fade) |
| Trigger | Hamburger-Icon (☰) in Top-Bar | Wie wird die Sidebar geöffnet |
| Breakpoint | `[WERT]` | Ab wann permanent sichtbar (Desktop) |
| Inhalt | Sessions-Liste (📌 Angepinnt oben, 📋 Letzte Chats unten) + Abmelden | Pinned Sessions via `localStorage` (Migration aus sessionStorage in Patch 101) |

### 4.8 Toast-Benachrichtigungen

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Position | `[WERT]` | Wo erscheinen Toasts |
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
| Pfeil | `[WERT]` | Dreieck-Pfeil zum Trigger |
| Trigger | Touch: immer click | Auslöser (Touch: immer click, kein Hover) |
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
| Verstecken Mobile | ja | `scrollbar-width: none` auf Touch |

### 4.11 Ladeindikator / Spinner

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Typ | `spinner` | Spinner-Rad (Patch 102: von springenden Punkten auf Spinner umgestellt) |
| Farbe | `[WERT]` | Spinner-Farbe |
| Größe | `[WERT]` | Durchmesser |
| Typing-Bubble | ja, Spinner-Rad + `@keyframes spin` | Zustandsanzeige bei Chat/LLM-Antwort |
| Zustandsmaschine | `setTypingState('running' \| 'timeout' \| 'error')` | Visuelles Feedback: normal / 45s-Timeout / Fehler mit Retry-Button |
| Skeleton Screens | nein | Kein Platzhalter-Block-System |

### 4.12 Chat-Bubbles

| Eigenschaft | User | Bot/LLM |
|-------------|------|---------|
| Hintergrund | `--bubble-user-bg` = `rgba(236, 64, 122, 0.88)` | `--bubble-llm-bg` = `rgba(26, 47, 78, 0.85)` |
| Textfarbe | `--bubble-user-text` | `--bubble-bot-text` |
| Border-Radius | `[WERT]` | `[WERT]` |
| Max-Breite | `[WERT]` | `[WERT]` |
| Padding | `[WERT]` | `[WERT]` |
| Toolbar | Copy, Retry, Timestamp | Copy, Retry, Timestamp |
| Toolbar Sichtbarkeit | Touch: always (leicht opak) | Touch: always (leicht opak) |
| Code-Blöcke | `[WERT]` | `[WERT]` |
| Error-Bubble | — | `showErrorBubble()` bei NetworkError + Retry-Button. SSE-Fallback prüft `/archive/session/{id}` vor echtem Retry (Patch 109) |

---

## 5. Icons

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Icon-Set | Emoji | Unicode-Emojis als Icon-System (☰ Navigation, 🔧 Settings, 💾 Export, 📌 Pinned, 📋 Sessions) |
| Standardgröße | `[WERT]` | Normale Icons in Text/Buttons |
| Große Icons | `[WERT]` | Tab-Icons, Nav-Icons |
| Farbe | `inherit` | Standard-Icon-Farbe |
| Touch-Target | `44px` | Klickbereich um Icons herum (unabhängig von Icon-Größe) |

---

## 6. Animationen & Übergänge

| Eigenschaft | CSS-Variable | Wert | Beschreibung |
|-------------|-------------|------|--------------|
| Schnell | `--transition-fast` | `[WERT]` | Hover, Fokus, kleine Zustandswechsel |
| Normal | `--transition-base` | `all 0.3s ease` | Modals, Dropdowns, Panels |
| Langsam | `--transition-slow` | `[WERT]` | Seitenübergänge, große Animationen |
| Easing | `--easing-default` | `ease` | Standard-Easing |
| Reduce-Motion | — | `@media (prefers-reduced-motion: reduce)` | Animationen respektieren, auf Minimum reduzieren |
| Spinner | — | `@keyframes spin` | Typing-Indicator Spinner-Rad (Patch 102) |

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
- `:hover` funktioniert auf Touch nicht → IMMER `:active` als Alternative (Sweep seit Patch 85)
- Toolbar-Sichtbarkeit: auf Touch-Geräten immer sichtbar (leicht opak), nicht nur bei Hover
- `backdrop-filter: blur()` braucht Fallback für ältere Browser
- `-webkit-overflow-scrolling: touch` für flüssiges Scroll-Verhalten
- `scrollbar-width: none` für cleane horizontal-scrollbare Bereiche (Tabs)
- Primäre Nutzer: Jojo (iPhone via Tailscale), Chris (Android) — Mobile-First ist Pflicht

### 8.2 Viewport-Handling
| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Höheneinheit | `dvh` | Dynamische Viewport-Höhe gegen Keyboard-Overlap |
| Keyboard-Anpassung | `[WERT]` | Verhalten wenn Soft-Keyboard aufgeht |
| Safe-Areas | `env(safe-area-inset-*)` | iPhone-Notch/Dynamic-Island |

### 8.3 Landscape-Modus
| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Breakpoint | `@media (orientation: landscape) and (max-height: 500px)` | Wann greifen Landscape-Regeln (Patch 86, N-F10) |
| Header | Kompaktierung: reduzierte Höhe + Padding | Header schrumpfen |
| Modals | Max-Höhe anpassen | Modals kleiner |
| Input-Bar | Kompaktierung | Chat-Eingabe flacher |

### 8.4 Offline / Shop-Floor
| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Externe Abhängigkeiten | CDN erlaubt (jsPDF, Chart.js, chartjs-plugin-zoom, Hammer.js) | Nala lädt CDN-Ressourcen |
| Fonts | `[WERT]` | Font-Ladestrategie |
| Single-File | ja | Nala-HTML wird als Python-String in nala.py inline ausgeliefert |

---

## 9. Theme-System

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Themes | Dark (Standard), weitere via Color-Picker | Verfügbare Themes |
| Standard-Theme | Dark | Default beim ersten Besuch |
| Speicherung | `localStorage` Keys: `nala_theme`, `nala_last_active_favorite` | Persistenz |
| FOUC-Vermeidung | Early-Load-IIFE im `<head>` | Prüft `nala_last_active_favorite` zuerst, liest v2-Slot, wendet CSS-Props an bevor Body rendert |
| CSS-Variablen-Root | `:root` | Wo werden Variablen gesetzt |
| User-Customization | Color-Picker + Presets | User darf Farben anpassen (Theme-Farben + Bubble-Farben separat) |
| Favoriten-Slots | 3 | Speicherbare Theme-Presets |
| Was wird gespeichert | Theme + Bubble-Farben + Schriftgröße (v2-Schema seit Patch 86) | Umfang eines Favoriten-Slots |
| Reset | `resetTheme()` → ruft `resetAllBubbles()` + `resetFontSize()` mit auf | Vollständiger Reset aller Overrides (Patch 109) |

---

## 10. Accessibility

| Eigenschaft | Wert | Beschreibung |
|-------------|------|--------------|
| Kontrast-Ziel | WCAG AA | Mindest-Kontrastverhältnis |
| Fokus-Indikator | `[WERT]` | Sichtbarer Fokus-Ring (Farbe, Breite, Offset) |
| Skip-Link | nein | Noch nicht implementiert |
| Aria-Labels | Pflicht auf allen interaktiven Elementen | Screenreader-Support |
| Reduce-Motion | respektieren | Animationen auf Minimum bei User-Präferenz |
| Schriftgrößen-Wahl | ja, 4 Presets (13/15/17/19px) | User kann Schriftgröße anpassen |
| Farbblindheit | Farbe nie als einziger Informationsträger | Immer zusätzlich Icon/Text |

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

## Offene Werte — Nächster UI-Patch ausfüllen

Die folgenden Werte müssen beim nächsten UI-Patch direkt aus dem `:root`-Block in `nala.py` extrahiert werden:

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

**Methode:** Claude Code Patch-Block mit `grep -n 'root\|--color\|--bg-\|--text-\|--border\|--radius\|--shadow\|--font\|--space\|--z-' zerberus/app/routers/nala.py | head -80` → Werte hierher übertragen.

---

## Änderungshistorie

| Datum | Beschreibung |
|-------|--------------|
| 2026-04-24 | Initiale Struktur angelegt (alle Werte als Platzhalter) |
| 2026-04-24 | Erste Befüllung aus Lessons/SUPERVISOR: Bubble-Defaults, Font-Presets, Theme-System, Touch-Regeln, Spinner-Typ, Sidebar-Inhalt, Landscape, Modal-Handling, CDN-Deps, Anti-Invariante dokumentiert. ~40% der Werte befüllt, Hex-Werte aus `:root` stehen aus |
