---
version: alpha
name: "Garmin"
source_url: "https://www.garmin.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Oswald, the condensed geometric sans that feels engineered rather than set, anchors every headline across garmin.com — a deliberate compression that reads as athlete-brief rather than marketing-sprawl. The palette runs on industrial restraint: #d8d8d8 hairlines, #f2f2f2 surface panels, and #727272 body gray that keeps spec copy legible without competing with product photography. Two colors break the monotone — #0e58ed, a high-voltage electric blue that fires on every primary CTA and interactive state, and #ff9b00, an amber-orange reserved for performance metrics, active-route callouts, and GPS-state highlights. Neither is timid; both feel pulled from the device face rather than assembled by a brand committee.

  Product cards sit in {rounded.xs} containers — Garmin avoids the soft pill curves that lifestyle brands default to, preferring angular surfaces that echo the bezel geometry of their watches. Navigation scrolls horizontally across sport verticals (Running, Cycling, Swimming, Outdoor, Golf, Aviation), each tab rendered in Roboto Condensed at tight letter-spacing. The comparison table — a true Garmin signature — stacks model tiers in dense rows of spec data, using alternating {colors.surface-soft} zebra stripes and {typography.spec-label} at 12–13px to pack satellite-band counts, battery-life hours, and heart-rate sensor specs into a scannable grid without losing hierarchy.

  Hero sections toggle between dark-canvas and white-canvas treatments based on device colorway: black Forerunners and Fenix models photograph against near-black backdrops with {colors.accent-orange} callout text; silver and white devices sit on {colors.canvas} with {colors.primary} accent lines. This responsive backdrop logic treats product pigment as a layout input, unusual at Garmin's catalog scale. Oswald runs from 56px display down to 20px section titles, always weight 600–700 and always near-zero tracking — the condensed form carries the brand voice without requiring color to do extra work. Roboto handles all body copy, form labels, and table content, keeping the dense spec architecture legible. The footer drops to a near-black panel that creates a definitive visual full-stop beneath each product page — the sole place the canvas inverts completely.

colors:
  primary: "#0e58ed"
  primary-active: "#0040c0"
  primary-disabled: "#a8c4f8"
  accent-orange: "#ff9b00"
  accent-orange-dark: "#d97c00"
  ink: "#111111"
  body: "#3a3a3a"
  muted: "#727272"
  hairline: "#d8d8d8"
  canvas: "#ffffff"
  canvas-dark: "#111111"
  surface-soft: "#f2f2f2"
  surface-card: "#eeeeee"
  footer-bg: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-orange: "#ffffff"

typography:
  display-xl:
    fontFamily: "Oswald, 'Roboto Condensed', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Oswald, 'Roboto Condensed', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0px
  display-sm:
    fontFamily: "Oswald, 'Roboto Condensed', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0px
  title-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0px
  title-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0px
  body-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0px
  body-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px
  spec-label:
    fontFamily: "'Roboto Condensed', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  category-tab:
    fontFamily: "'Roboto Condensed', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 26px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "2px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 26px
    height: 44px
  button-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-orange}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-orange-active:
    backgroundColor: "{colors.accent-orange-dark}"
    textColor: "{colors.on-orange}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 60px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  hero-module:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.accent-orange}"
    minHeight: 520px
  hero-module-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    bodyTextColor: "{colors.body}"
    accentColor: "{colors.primary}"
    minHeight: 520px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headerColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    zebraStripe: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    cellPadding: "{spacing.sm} {spacing.base}"
  comparison-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  category-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.category-tab}"
    activeBorderBottom: "3px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  activity-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-orange}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    separator: "/"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Solid #0e58ed fill with white uppercase Roboto text at weight 700 and 0.5px letter-spacing, 4px radius, 44px height. Transitions to `button-primary-active` (#0040c0) on hover; `button-primary-disabled` (#a8c4f8) renders non-interactively. This is the dominant CTA across product pages, dealer locators, and cart flows.

**`button-secondary`** — White canvas background with a 2px #0e58ed border and matching blue text; same uppercase Roboto treatment as primary. Used for secondary actions alongside primary CTAs, such as "Compare" adjacent to "Buy Now."

**`button-ghost`** — Transparent background, 2px #d8d8d8 border, dark ink text. Used for tertiary actions and on-card controls where blue would disrupt visual hierarchy — common on spec-detail expandable rows.

**`button-orange`** — #ff9b00 amber fill with white uppercase text; reserved for promotional modules, accessories cart-add CTAs, and sale event pages where the orange functions as an urgency signal. Transitions to `button-orange-active` (#d97c00) on press.

### Inputs
**`text-input`** — 1px #d8d8d8 border, 2px radius, 44px height. Focus ring upgrades to 2px solid #0e58ed with no transition delay. Muted #727272 placeholder text. Used for global search, dealer/retailer locator, and support ticket forms.

### Navigation
**`nav-bar`** — 60px white bar with 1px #d8d8d8 bottom border. Garmin wordmark logo sits left; top-level category links render in 14px Roboto with hover-triggered mega-menu dropdowns that expose sub-categories and featured devices. Search icon and cart icon align right with 44×44px tap targets.

**`category-filter`** — Horizontal scroll tab strip gating sport/product subcategories beneath section headers. Inactive tabs render in #727272 uppercase Roboto Condensed; the active tab receives a 3px solid #0e58ed underline and #0e58ed text. No background fill change — the underline alone carries selection state.

### Cards
**`product-card`** — White canvas background, 1px #d8d8d8 border, 2px radius. Product image at top full-width, model name in `display-sm` Oswald, one-line key-spec summary in `body-sm` Roboto in #727272, MSRP in `title-md` Roboto at weight 500, then a `button-primary` pinned at bottom. Hover lifts a box-shadow from none to 0 4px 16px rgba(0,0,0,0.10).

### Hero
**`hero-module`** — Full-width near-black (#111111) backdrop with Oswald `display-xl` headline in white, body copy in Roboto `body-md` in #d8d8d8, and a `button-primary` or `button-orange` CTA. Performance callouts (GPS accuracy, battery duration, satellite bands) appear as #ff9b00 superscript-tagged stat strings. Dark hero is the default treatment for black, slate, and titanium device colorways.

**`hero-module-light`** — White canvas version for silver, white, and light-band device colorways. Headline switches to #111111, accent elements render in #0e58ed, body copy in #3a3a3a. Same Oswald `display-xl` / Roboto `body-md` structure — the typography remains identical; only the background and accent palette invert.

### Data Display
**`spec-table`** — Full-width table with Roboto Condensed `spec-label` cells at 13px, alternating #f2f2f2 zebra rows, and 1px #d8d8d8 row borders. Header cells use ink color at weight 700. Checkmark present features render in #0e58ed; absent features render as em-dashes in #727272. Sticky first-column on horizontal scroll preserves model identity.

**`comparison-row`** — Slim 44px row variant used inside the model-comparison module. #f2f2f2 background, spec label left-aligned in `spec-label` Roboto Condensed, value right-aligned, separated by 1px #d8d8d8 bottom border. Enables dense stacking of 20+ spec rows without visual fatigue.

### Badges & Labels
**`activity-badge`** — Compact #ff9b00 tag (2px radius) with 12px Roboto white caption text. Marks device cards by primary activity category (Running, Trail, Swim, Dive, Golf, Aviation). On dark hero sections the badge reads as a performance alert glyph; on white product cards it reads as a category classifier.

### Utility
**`breadcrumb`** — 14px Roboto in #727272 with slash separators; the final active crumb renders in #111111. Appears directly below the nav-bar on product detail and support pages to signal catalog depth.

**`footer`** — Full-width #1a1a1a panel. Four-to-five link columns in 14px Roboto with #d8d8d8 link text; column headings in 12px Roboto caption at weight 700 in white. Regional selector, social icon row, and legal copy appear in #727272 at the base. The footer is the only sustained dark surface on the site outside of dark hero modules.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category-filter scrolls horizontally with 8px momentum; nav collapses to hamburger drawer; hero drops to display-md (36px) Oswald and 340px min-height; spec-table scrolls horizontally with first column pinned |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links but hides tertiary sub-items; hero retains full-bleed imagery but headline scales to display-md; comparison table visible in abbreviated three-model form |
| Desktop | 1128–1440px | Three- or four-column product grid; full mega-menu nav with featured device callouts; full spec-table and comparison module; hero at full display-xl with side-by-side image and text layout |
| Wide | > 1440px | Content constrained to ~1280px max-width centered on canvas; hero imagery allowed to bleed edge-to-edge while text block stays within the 1280px grid column |

### Touch Targets
- All interactive controls minimum 44px height on mobile
- Category-filter tabs minimum 44px tap height with horizontal padding to prevent miss-taps
- Nav hamburger icon target 44×44px
- Product card full surface is a tappable link; button at bottom is a distinct, redundant tap target
- Spec-table rows have 44px minimum height for expandable accordion rows on mobile

### Collapsing Strategy
- Mega-menu nav collapses to a full-screen slide-in drawer with accordion-expanded sport categories on mobile
- Spec table becomes a horizontal scroll container below 744px; the device name column is pinned left
- Model comparison module is hidden below 744px and replaced by individual spec-tables per device with a "compare" toggle
- Hero image switches from side-by-side layout to stacked (image above, text below) at < 744px
- Footer four-column link grid collapses to single-column accordion sections on mobile; headings become tappable expanders

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit dark-mode token surface extracted; dark hero backgrounds inferred from product photography patterns rather than a documented dark-mode palette
- Exact nav-bar height and mega-menu grid layout dimensions not confirmed from live extraction; 60px is an estimate
- Garmin Connect app health-dashboard palette (activity rings, HR graph colors, sleep stage colors) is app-internal and not reflected here
- Orange #ff9b00 usage boundary between promotional, performance-state, and alert contexts not definitively confirmed; current token assignments are best inference from product page layout conventions
- Footer background color (#1a1a1a) is inferred; exact hex not present in extracted color list
- Near-black body and ink text colors (#111111, #3a3a3a) are inferred; no dark text hex extracted — site likely delivers these via CSS custom properties not captured in static extraction
- Prompt font-family purpose unknown; may be Thai-locale variant only and not part of the English/Japanese brand type system
- Superscripts-Oswald and Superscripts-Roboto variants are footnote/legal-disclaimer typefaces; no specific size or weight scale was extractable
