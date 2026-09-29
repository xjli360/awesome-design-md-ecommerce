---
version: alpha
name: "Fear of God"
source_url: "https://fearofgod.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  HelveticaNeueLTPro-Cn — the condensed weight, not the standard cut — sets the register before a single product image loads: tall, compressed letterforms that read as architectural index entries rather than retail copy. The entire UI lives inside a near-monochromatic compression of deep charcoals (#303030, #232323, #1a1a1a) against bleached near-whites (#fbfbfb, #f1f1f1), with corners held at {rounded.none} across every interactive surface — no pill buttons, no softened cards anywhere in the system. The canvas sits at #fbfbfb rather than pure white, giving editorial photography a slightly warmer temperature than the clinical whites favored by luxury competitors. A warm khaki sand (#c9c4ac) surfaces as a selective seasonal token, most visible in palette-adjacent editorial strips rather than persistent UI chrome. Jerry Lorenzo's label communicates through compression: product names run at light condensed weight over minimal metadata, letting oversized portrait shoots do the emotional lifting. The announcement bar inverts — dark #303030 field with #fbfbfb text — before the nav flips back to the light canvas, creating a deliberate clamp at the viewport top. Optima appears selectively against the Helvetica grid as an editorial counterweight, a serif intrusion that reads less like a brand signature and more like a private archival label. Status is communicated through minimal accent injections — #3ed660 for availability indicators, #8b0000 for low-stock and conditional pricing, #ee9441 for clearance thresholds — all constrained in size so they register as data points rather than marketing noise. Navigation runs uppercase and tight, treating the category menu as a directory. The deep navy #0a142f appears in capsule editorial contexts, signaling collection-specific variation rather than a persistent global tone.

colors:
  primary: "#303030"
  primary-active: "#1a1a1a"
  primary-disabled: "#767676"
  ink: "#121212"
  body: "#323232"
  muted: "#616161"
  muted-soft: "#9ea6b1"
  hairline: "#dedede"
  hairline-soft: "#e3e3e3"
  canvas: "#fbfbfb"
  surface-soft: "#f1f1f1"
  surface-card: "#eeeeee"
  surface-dark: "#202223"
  on-primary: "#fbfbfb"
  on-dark: "#f1f1f1"
  khaki-accent: "#c9c4ac"
  status-green: "#3ed660"
  status-red: "#8b0000"
  status-amber: "#ee9441"
  deep-navy: "#0a142f"
  scrim: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "'HelveticaNeueLTPro-Cn', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 80px
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: -2px
    textTransform: uppercase
  display-md:
    fontFamily: "'HelveticaNeueLTPro-Cn', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -1px
    textTransform: uppercase
  display-sm:
    fontFamily: "'HelveticaNeueLTPro-Cn', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  editorial-headline:
    fontFamily: "Optima, 'Optima Nova LT', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0
  title-lg:
    fontFamily: "'HelveticaNeueLTPro-Cn', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'HelveticaNeueLTPro-LtCn', 'HelveticaNeueLTPro-Cn', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  product-name:
    fontFamily: "'HelveticaNeueLTPro-LtCn', 'HelveticaNeueLTPro-Cn', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'HelveticaNeueLTPro-Cn', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  nav-label:
    fontFamily: "'HelveticaNeueLTPro-Cn', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'HelveticaNeueLTPro-Cn', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'HelveticaNeueLTPro-Cn', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase

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
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 23px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    borderBottom: "1px solid {colors.hairline-soft}"
    height: 56px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: 10px 0
  product-card:
    backgroundColor: "{colors.surface-soft}"
    nameTypography: "{typography.product-name}"
    priceTypography: "{typography.price-display}"
    metaTypography: "{typography.caption}"
    nameColor: "{colors.ink}"
    priceColor: "{colors.body}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    ctaBackgroundColor: "{colors.on-dark}"
    ctaTextColor: "{colors.primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.none}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    disabledBackgroundColor: "{colors.surface-soft}"
    disabledTextColor: "{colors.primary-disabled}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    minHeight: 44px
    padding: 10px 14px
  color-swatch:
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: 24px
  category-filter:
    backgroundColor: transparent
    activeBackgroundColor: "{colors.primary}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.on-primary}"
    borderColor: "{colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 6px 14px
  status-badge:
    backgroundColor: "{colors.status-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  status-badge-low-stock:
    backgroundColor: "{colors.status-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  status-badge-sale:
    backgroundColor: "{colors.status-amber}"
    textColor: "{colors.canvas}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    height: 44px
    padding: 0 16px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
  editorial-strip:
    backgroundColor: "{colors.khaki-accent}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.editorial-headline}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    headingTypography: "{typography.nav-label}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Full-width add-to-cart and checkout CTAs set in deep charcoal (#303030) with {typography.button-md}: uppercase condensed Helvetica at 2px letter-spacing, 48px tall. Zero border-radius reinforces the brand's anti-decoration stance; hover darkens to `button-primary-active` (#1a1a1a). Disabled collapses to #767676 fill while preserving the uppercase treatment. The letter-spacing and condensed face together read as a stamped label rather than a soft CTA.

**`button-secondary`** — Outline variant on {colors.canvas} with 1px {colors.primary} border and {colors.ink} text; shares the same condensed uppercase typography and zero radius. Used for secondary purchase paths and "save for later" actions. Active state tightens the border to {colors.primary-active}.

**`button-ghost`** — Transparent background, {colors.ink} text in {typography.button-sm}. Reserved for text-level actions within product pages — size guide links, edit/remove in cart, policy acknowledgments — no border and no radius, just the label.

### Text Input

**`text-input`** — Zero-radius, {colors.canvas} background with {colors.hairline} default border that sharpens to solid {colors.primary} on focus. Placeholder in {colors.muted} at {typography.body-md}; 48px height aligns with button-primary for same-row form layouts. No shadow, no transition easing — a deliberate spareness that matches the wider UI register.

### Navigation

**`nav-bar`** — 56px bar on {colors.canvas} with a hairline-soft bottom divider; category labels in {typography.nav-label} (uppercase condensed, 1.5px tracking) treating the menu as a directory index rather than a marketing surface. Logo sits left on desktop, centered on mobile. Cart and account icons hold {colors.ink}; active state is a simple underline rather than a fill.

**`announcement-bar`** — Inverted stripe that sits above the nav: {colors.primary} fill, {colors.on-primary} text in {typography.caption} at 0.5px tracking. Communicates shipping thresholds, product drops, and store notices. The dark-to-light flip from announcement bar to nav creates a deliberate visual clamp at the top of the viewport.

### Product Card

**`product-card`** — Portrait-ratio (3:4) image on {colors.surface-soft}, zero border-radius. Product name in {typography.product-name} (light condensed, 14px) at {colors.ink} sits {spacing.sm} below the image; price follows in {typography.price-display} at {colors.body}. No hover overlay, no quick-add on the grid view — the editorial stillness is intentional, directing attention to the photography rather than interactive affordances.

### Hero Banner

**`hero-banner`** — Full-viewport dark canvas ({colors.surface-dark}) with headline in {typography.display-xl}: 80px condensed uppercase at -2px tracking, reversed in {colors.on-dark}. Subhead uses {typography.display-sm}. The CTA inverts the primary button pattern — {colors.on-dark} background with {colors.primary} text — to remain legible against the dark ground. Photography fills edge to edge with minimal safe-zone padding.

### Size Selector

**`size-selector`** — Zero-radius tiles in {colors.canvas} with {colors.hairline} border; selected fills to {colors.primary} with {colors.on-primary} label. Sold-out tiles switch to {colors.surface-soft} background with {colors.primary-disabled} text and a diagonal strike rule. Minimum height 44px ensures touch target compliance on mobile; tiles may wrap to a second row on small viewports.

### Status Badges

**`status-badge`** — Minimal rectangles at {rounded.xs} (2px), appearing sparingly at the image corner of product cards. In-stock uses {colors.status-green} (#3ed660); low-stock or pricing conditions use {colors.status-red} (#8b0000); clearance uses {colors.status-amber} (#ee9441). All labels run {typography.micro-label} — 10px uppercase at 1px tracking — in {colors.canvas}, kept visually subordinate to the product photography.

### Editorial Strip

**`editorial-strip`** — Full-bleed content band with {colors.khaki-accent} (#c9c4ac) background, the sole departure from the charcoal/white binary. Headline in {typography.editorial-headline} (Optima, 40px) signals a tonal shift — seasonal lookbook, campaign narrative, or archive context. Body runs {typography.body-md} in {colors.ink}. Used sparingly at section breaks rather than as a recurring layout module.

### Footer

**`footer`** — Dark ground matching {colors.surface-dark} for visual continuity with the hero. Column headings in {typography.nav-label} (uppercase condensed); link rows in {typography.body-sm} at {colors.muted-soft}. Top border in {colors.primary} connects back to the announcement bar's charcoal field. Social icons and legal links sit in a sub-row below the main columns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero headline scales to {typography.display-md}; size selector tiles expand full-width; announcement bar truncates to one offer line |
| Tablet | 744–1128px | Two-column product grid; nav expands inline with condensed labels; editorial-strip switches to two-column text layout |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at {typography.display-xl} 80px; editorial-strip at side-by-side image and text |
| Wide | > 1440px | Four-column product grid; content max-width 1440px centered with margin auto; hero photography bleeds to viewport edges |

### Touch Targets

- Size selector tiles minimum 44px height on all touch viewports
- Color swatches maintain 32px tap region (24px visual swatch + 4px margin each side)
- Nav hamburger icon minimum 44×44px hit area
- Add-to-cart button full-width on mobile for single-thumb reach
- Footer links minimum 40px vertical rhythm for comfortable tapping

### Collapsing Strategy

- Navigation category list collapses to off-canvas slide-in drawer on mobile, preserving uppercase label treatment
- Product filters collapse to a bottom sheet on mobile and a left sidebar panel on tablet and above
- Editorial strip text and image switch from side-by-side to stacked (image first) on mobile
- Footer columns collapse from four-column to two-column at tablet and single-column at mobile
- Hero subhead hides on mobile below 375px to prevent headline truncation

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover states for product cards not confirmed — secondary image swap or quick-add overlay may exist but was not extractable from static crawl
- Cart drawer animation timing, easing curve, and overlay opacity unconfirmed; scrim color derived from extracted #1a1a1a
- HelveticaNeueLTPro-Cn and HelveticaNeueLTPro-LtCn weight distinction treated as separate font files, not a variable font axis — numeric weight values are approximated
- Optima usage scope not fully confirmed; may be limited to specific campaign pages rather than any persistent component
- Exact product grid gap values and page-level horizontal padding not reliably extracted
- Mobile menu transition style (slide vs. fade vs. overlay) not confirmed
- Logo SVG dimensions and clearspace rules not extractable from crawl
- #deep-navy (#0a142f) usage scope limited to inferred seasonal editorial context; no confirmed persistent UI assignment
