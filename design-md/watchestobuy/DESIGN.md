---
version: alpha
name: "WatchesToBuy"
source_url: "https://watchestobuy.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The near-black ground (#0B0B0B) functions the way a watchmaker's velvet tray does — it suppresses ambient distraction so the merchandise reads as the only light source in the room. WatchesToBuy navigates the collector space with a two-temperature palette: institutional deep navy (#003399) anchors every call-to-action and primary link, while brick terracotta (#914941) marks the human edge — the "Sell Your Watch" prompts, the Fair condition badge, the warm counterpoint to an otherwise cold authority. Amber-gold (#ffba00) appears exactly once per page zone as a decorative divider, keeping the watch-dial reference from becoming noise. Raleway carries the display register; its geometric cuts at modest weights (600–700) suit decade-browsing headlines like "1960s Swiss Dress Watches" without competing with the photography. Open Sans handles body and interface copy at 400 weight, legible at small sizes where listing specifications live. Poppins at 600 uppercase with +0.5px tracking handles buttons and badges — compact and readable on dark and light surfaces alike.

  Corners are deliberately squared across the system: `{rounded.xs}` (4px) on inputs and buttons, `{rounded.sm}` (8px) on cards. The result is a platform posture rather than an app one — analogous to the clinical precision of a philatelic catalogue or auction house, where exactness signals expertise. The only softness lives in brand-filter tags, which use `{rounded.full}` pill shapes to signal dismissibility. Product cards carry a faint drop shadow at low opacity to lift them from the light canvas (#fcfbfe) without depth that competes with dial photography. Steel blue-gray (#abb8c3) serves as the midpoint of the dark surfaces: placeholder text in the search bar, sub-copy in the hero band, footer links in their resting state — the functional non-color that keeps dark zones navigable. Antique olive-gold (#958e09) is reserved for special interest tags and patina-era callouts, a nod to aged brass cases. Condition badges run a strict three-tier system — green for Excellent, navy for Good, terracotta for Fair — color-coding that collectors read at a glance across a dense grid without hovering.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99aacc"
  accent: "#914941"
  accent-active: "#7a3836"
  accent-gold: "#ffba00"
  accent-olive: "#958e09"
  ink: "#32373c"
  body: "#515151"
  muted: "#767676"
  hairline: "#d8d8d8"
  canvas: "#fcfbfe"
  surface-soft: "#e9e6ed"
  surface-card: "#ffffff"
  surface-dark: "#0b0b0b"
  surface-dark-soft: "#1e1e1e"
  on-primary: "#ffffff"
  on-dark: "#eeeeee"
  steel: "#abb8c3"
  link: "#2ea2cc"
  danger: "#aa0000"
  condition-excellent: "#008a20"

typography:
  display-xl:
    fontFamily: "'Raleway Custom', Raleway, 'Open Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Raleway Custom', Raleway, 'Open Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Raleway Custom', Raleway, 'Open Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Raleway Custom', Raleway, 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Custom Poppins', Poppins, 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Custom Open Sans', 'Open Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Custom Open Sans', 'Open Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Custom Open Sans', 'Open Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Custom Poppins', Poppins, 'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Custom Poppins', Poppins, 'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Custom Poppins', Poppins, 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Raleway Custom', Raleway, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  badge-label:
    fontFamily: "'Custom Poppins', Poppins, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  maker-label:
    fontFamily: "'Custom Open Sans', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  nav-logo:
    typography: "{typography.display-sm}"
    textColor: "{colors.on-dark}"
  search-bar:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.on-dark}"
    placeholderColor: "{colors.steel}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.steel}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    shadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    aspectRatio: "4/3"
    rounded: "{rounded.xs}"
    backgroundColor: "{colors.surface-soft}"
    overflow: hidden
  product-card-maker:
    typography: "{typography.maker-label}"
    textColor: "{colors.muted}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  condition-badge:
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  condition-badge-excellent:
    backgroundColor: "{colors.condition-excellent}"
    textColor: "{colors.on-primary}"
  condition-badge-good:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  condition-badge-fair:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
  sold-overlay:
    backgroundColor: "rgba(11,11,11,0.72)"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    display: flex
    alignItems: center
    justifyContent: center
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.xxl} {spacing.xl}"
    minHeight: 420px
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subline:
    typography: "{typography.body-md}"
    textColor: "{colors.steel}"
  decade-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
    height: 36px
  decade-filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
  brand-filter-tag:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  brand-filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
  watchmaker-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  olive-era-tag:
    backgroundColor: "transparent"
    textColor: "{colors.accent-olive}"
    typography: "{typography.caption}"
    border: "1px solid {colors.accent-olive}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  gold-accent-rule:
    borderTop: "2px solid {colors.accent-gold}"
    width: 100%
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.steel}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  listing-spec-row:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} 0"
  listing-spec-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    textTransform: uppercase
    letterSpacing: 0.5px

## Components

### Buttons
**`button-primary`** — Deep navy (#003399) fill with white Poppins 600 uppercase text at +0.5px tracking. Handles primary marketplace actions: "Contact Seller", "Make Offer", "Buy Now". Active state darkens to #002277; disabled washes to a muted cornflower (#99aacc). The 4px corner radius (`{rounded.xs}`) reads precise rather than friendly — deliberate for a platform where trust depends on exactness.

**`button-secondary`** — Transparent background with a 2px navy border and matching navy text, identical corner radius and height to the primary. Used for "Save to Watchlist" and "View All". Hover inverts: navy fill, white text. The outline weight (2px) is heavier than typical to hold presence against the light canvas.

**`button-accent`** — Brick terracotta (#914941) fill reserved exclusively for seller-facing calls-to-action: "Sell Your Watch", "List a Piece". Acts as the warm pole of the palette, signaling a human-to-human transaction rather than a platform operation.

### Navigation
**`nav-bar`** — Near-black (#0B0B0B) bar at 64px. Logo left in Raleway 600 display-sm. Navigation links in Poppins 600 14px with +0.2px tracking. A compact `search-bar` embeds inline on desktop, rendered against the slightly lighter surface-dark-soft (#1e1e1e) with a steel-blue (#abb8c3) hairline border to distinguish it from the bar itself. On mobile the search bar collapses to a magnifier icon triggering a fullscreen overlay.

### Search Bar
**`search-bar`** — Dark-on-dark field: background #1e1e1e, placeholder text in steel (#abb8c3), typed text in on-dark (#eeeeee). The 1px steel border provides just enough edge to locate the input field without brightness. Pressing return navigates to the grid results page; no inline autocomplete autocomplete panel was confirmed in extraction.

### Product Card
**`product-card`** — White card on hairline border with a 2px diffuse shadow. The watch photo fills a 4:3 container at top with `{rounded.xs}` corners. Below: maker in all-caps caption 11px muted gray (+0.8px tracking), model name in Poppins 600 (`{typography.title-sm}`), price in Raleway 700 22px navy (`{typography.price-display}`). A condition badge sits absolutely positioned over the photo at top-left. On hover, card lifts shadow from 8px to 14px spread to signal interactivity.

### Condition Badges
**`condition-badge-*`** — Three-tier: Excellent (green #008a20), Good (navy #003399), Fair (terracotta #914941). All rendered in Poppins 700 uppercase 11px with +0.5px tracking at 3×8px padding. Positioned over the card image so the condition reads before the collector's eye reaches the price. On listing detail pages, the badge moves to the header zone beside the model name.

### Sold Overlay
**`sold-overlay`** — A 72%-opacity dark scrim layered over the full card image with centered "SOLD" text in badge-label. Keeps sold listings in the grid for browsable historical reference — collectors use past sales for market context — while making the state instantly legible.

### Hero
**`hero`** — Full-width near-black band at minimum 420px. Headline in Raleway 700 36px white (`{typography.display-xl}`); sub-copy in body-md at steel (#abb8c3) so it recedes behind the headline without disappearing. A button pair (primary + secondary) anchors the CTA block. Hero can accept a full-bleed photography layer at ~35% opacity behind a CSS linear-gradient overlay.

### Decade Filter
**`decade-filter-chip`** — Horizontal row for era browsing: "Pre-1940s", "1950s", "1960s", "1970s", "1980s", "1990s+". Inactive chips are surface-soft (#e9e6ed) with hairline borders; active chip fills navy with white text. The 4px corners (`{rounded.xs}`) keep them squared-off — chips that look like catalog indices, not dismissible pills.

### Era Tags
**`olive-era-tag`** — A small outline tag in antique olive-gold (#958e09) used on listing detail pages to call out specialty era designations: "Gilt Dial Era", "Tropical Patina", "Pre-Regulation". The color reads as aged brass — semantic without being decorative.

### Listing Spec Table
**`listing-spec-row`** — Each row holds a label (all-caps caption, muted) and value (body-sm, body color) separated by a hairline bottom border. Used on watch detail pages for Movement, Case Material, Diameter, Reference Number, Year fields. No alternate-row shading; the hairline alone provides structure.

### Footer
**`footer`** — Matches the header's near-black canvas. Four-column grid on desktop (About, Buy, Sell, Contact). Column headings in Poppins 600 (`{typography.title-sm}`) at #eeeeee; body links in body-sm at steel (#abb8c3). A 2px amber-gold rule (`gold-accent-rule`) separates the logo row from the link columns — the sole warm-color moment in a cold-dark footer.

### Gold Accent Rule
**`gold-accent-rule`** — A 2px horizontal line in amber-gold (#ffba00) used as a structural divider in the footer and optionally beneath section headings on interior pages. Its scarcity is intentional: one rule per page zone keeps the watch-dial gold reference meaningful rather than decorative.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column listing grid; nav search collapses to icon + fullscreen overlay; decade-filter chips scroll horizontally with snap points; hero min-height drops to 280px; product-card price and CTA stack vertically |
| Tablet | 744–1128px | Two-column listing grid; nav shows abbreviated links; hero shifts to 50/50 image-text split; decade-filter shows full row without scroll |
| Desktop | 1128–1440px | Three-column listing grid; full nav with inline search bar; hero full-bleed with left-aligned text overlay; footer 4-column grid |
| Wide | > 1440px | Four-column listing grid; max content width 1400px centered; side margins fill with canvas color; footer remains 4-column |

### Touch Targets
- All decade-filter chips minimum 40px tall on mobile
- Condition badges minimum 28px height for legibility without precise tap
- Product card image area acts as full card tap target on mobile
- Nav icons (search, menu) minimum 44×44px tap well
- All buttons maintain 44px height at every breakpoint

### Collapsing Strategy
- Decade filter: overflow-x scroll with momentum and snap points on mobile; full visible strip on tablet and above
- Nav: hamburger drawer below 744px; full horizontal link row at 744px+; inline search bar at 1128px+
- Listing spec table: two-column label/value at all sizes; no collapse needed given the narrow label column
- Footer: single-column stack on mobile; 2-column at tablet; 4-column at desktop
- Hero CTAs: stacked column on mobile; inline row at tablet+

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- A large portion of extracted hex values (#f78da7, #ff6900, #fcb900, #7bdcb5, #00d084, #8ed1fc, #0693e3, #9b51e0, #cf2e2e) match the WordPress Gutenberg block editor default color palette exactly and likely originate from content blocks, not the brand design system; they are excluded from all component tokens
- Hover and focus ring colors could not be reliably extracted; active-state tokens are derived by darkening the extracted primaries
- FontAwesome is referenced in the font stack and is likely used for UI icons (search, cart, heart, chevron), but no icon grid or sizing system could be confirmed
- Whether the site runs a full dark-canvas layout or applies #0B0B0B only to the header and footer cannot be confirmed from meta theme-color alone; the light canvas (#fcfbfe) assumption for listing grids may need adjustment
- Exact grid column gaps, card padding, and hero internal spacing values are conventional estimates — no computed CSS values were extractable
- Seller dashboard and account pages likely introduce additional surface colors and form states not represented here
- No animation or transition timing values were captured
