# Mobile & Touch

- `:hover` funktioniert auf Touch-Geräten nicht → immer `:active` zusätzlich setzen. Bei jedem UI-Patch generellen Sweep machen (Zerberus P85)
- Mindest-Touch-Target: 44px — kleinere Buttons werden mobil verfehlt
- `backdrop-filter` ohne Fallback bricht auf älteren Mobile-Browsern
- Landscape-Modus: `@media (orientation: landscape) and (max-height: 500px)` für Header-/Padding-Reduktion. `100dvh` gegen Keyboard-Overlap, aber Header/Modals fressen sonst die Höhe (Zerberus P90)
- Tailscale + HTTPS Pflicht für mobile LAN-Nutzung — `crypto.randomUUID()` und andere Web-APIs versagen auf HTTP (Zerberus P68)
- MIME-Type-Check schlägt mobil fehl bei Datei-Uploads → nur Dateiendung prüfen (Zerberus P61)
