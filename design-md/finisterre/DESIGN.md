---
version: alpha
name: "Finisterre"
source_url: "https://finisterre.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The browser chrome opens at #e7ddbb — a washed dune-sand that signals warmth against cold-water imagery before a single content pixel loads, making this one of the few outdoor retailers that greets users with a desert tone rather than the expected slate or institutional white. Deep ocean navies (#010b13, #384972, #272d45) form a pressurised dark stratum across the UI: hero backgrounds, navigation surfaces, and headline type all draw from this near-black-to-midnight range, giving surf and mountain photography maximum contrast without reaching for pure black. Type runs Helvetica Neue LT W05_55 Roman for body copy and labels; Helvetica Neue LT W05_75 Bold carries display headlines and primary call-to-actions — an austere, functional pairing that resists decorative weight in the same register that cold-water gear resists ornamentation. Warmth appears at pressure points: the sand (#e7ddbb) surfaces behind editorial content blocks and soft-background panels, while cold seafoam accents (#b2f9e9, #00caaa) mark ecological certifications and responsible-material callouts, reading as the colour of an Atlantic wave-face in flat overcast light. Buttons and product cards hold a short radius — {rounded.xs} to {rounded.sm} — keeping the interface structural and tool-like rather than consumer-soft. The spacing system opens wide at section level ({spacing.section}), letting full-bleed photography breathe; interior padding stays tight, with {spacing.base} and {spacing.sm} governing product-card and label contexts. A blue-gray midground (#9a9db1, #676986) handles secondary text and UI chrome, producing a palette that reads as a gradient from near-black to sand without a harsh step. The sustainability ethos surfaces visually through colour restraint: teal (#00caaa) appears only on ecological badges and certification marks, never as a blanket highlight across primary interactions.

colors:
  primary: "#384972"
  primary-active: "#272d45"
  primary-disabled: "#9a9db1"
  ink: "#010b13"
  body: "#2c3e50"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#f4f4f6"
  surface-soft: "#e7ddbb"
  surface-card: "#f7f7f8"
  surface-dark: "#010b13"
  on-primary: "#f4f4f6"
  on-dark: "#f4f4f6"
  accent-teal: "#00caaa"
  accent-teal-deep: "#0e7a82"
  accent-sand: "#e7ddbb"
  scrim: "#010b13"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue LT W05_75 Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue LT W05_75 Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Helvetica Neue LT W05_75 Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue LT W05_55 Roman', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue LT W05_55 Roman', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue LT W05_55 Roman', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue LT W05_55 Roman', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue LT W05_75 Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue LT W05_75 Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue LT W05_55 Roman', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  label-caps:
    fontFamily: "'Helvetica Neue LT W05_75 Bold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
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
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 23px
    height: 48px
  button-secondary-inverse:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 23px
    height: 48px
  button-text:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderRadius: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 12px 16px
    height: 48px
    focus-borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.xl}"
    borderBottom: "none"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "4/5"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    badgeOffset: "{spacing.sm}"
  hero-full-bleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 80vh
    padding: "{spacing.xxl} {spacing.xl}"
    overlayScrim: "linear-gradient(to top, {colors.scrim}99 0%, transparent 60%)"
  sustainability-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  editorial-band:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-teal}"
    padding: "{spacing.section} {spacing.xl}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
    height: 44px
  product-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"
  product-badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"
  material-callout:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    accentIconColor: "{colors.accent-teal}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  category-label:
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    backgroundColor: "transparent"
    hoverColor: "{colors.ink}"
  size-guide-trigger:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    textDecoration: underline
    hoverColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: "1px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Deep ocean navy (#384972) fill with uppercase Bold Helvetica Neue at 14px and 0.5px letter-spacing. Height 48px, {rounded.xs} radius — almost square, deliberate and utilitarian rather than friendly. Active state descends to #272d45; disabled washes to muted blue-gray (#9a9db1), preserving white text throughout.

**`button-secondary`** — Transparent fill with a 1px ink (#010b13) border, same uppercase Bold typography and {rounded.xs} radius as the primary. On dark hero surfaces switches to `button-secondary-inverse`: border and text shift to on-dark (#f4f4f6) so both CTAs remain legible against photography. Horizontal padding 23px to compensate for the border width.

**`button-text`** — No fill, no border; Bold uppercase at 12px with underline decoration. Used for lower-hierarchy actions: size guides, wishlist toggles, "read more" links embedded in editorial bands.

### Text Inputs

**`text-input`** — Canvas (#f4f4f6) background with hairline (#dbdde4) border and {rounded.xs} radius. Fixed 48px height aligns with button height for clean form rows. Focus state promotes border to primary navy (#384972). Placeholder text in muted (#676986); body-md Roman at 16px for entered values.

### Navigation

**`nav-bar`** — Full-width near-black (#010b13) surface at 56px height. Links run Roman Helvetica Neue at 14px in on-dark (#f4f4f6). No bottom border — contrast between the dark bar and the page canvas supplies implicit separation. Logo is centered on mobile inside a hamburger-triggered drawer that preserves the same dark surface colour.

### Product Card

**`product-card`** — Square-cornered ({rounded.none}) cards with a 4:5 image ratio. Title runs title-sm (Roman, 16px); price runs body-sm (14px); both in ink against the surface-card background. Sale and new badges pin to the image top-left at {spacing.sm} offset. No drop shadow — the hairline-soft (#e5e5eb) grid gutter between cards provides visual separation on the light canvas.

### Hero

**`hero-full-bleed`** — Full-viewport panels (min 80vh) over dark or photography backgrounds with a bottom-up gradient scrim. Display XL headline (Bold, 48px, −0.5px tracking) in on-dark (#f4f4f6), body-md subtitle below. Primary and `button-secondary-inverse` buttons pair side by side at desktop, stack at mobile. Text block anchors to the lower-left third, preserving sky and horizon in the upper two-thirds of the frame.

### Sustainability Badge

**`sustainability-badge`** — Cold seafoam (#00caaa) fill with ink (#010b13) text at label-caps scale (11px, +1px tracking, uppercase). Appears on product cards and PDPs adjacent to material descriptors — "Responsible Wool", "Recycled Nylon", "Bluesign Approved". Tight {rounded.xs} keeps the badge reading as a stamp or tag rather than a pill. Never used as a general CTA vessel.

### Collection Header

**`collection-header`** — Warm sand (#e7ddbb) band at full width; display-md headline (Bold, 32px) over a body-md description paragraph. This is the only page-layout context in which the accent-sand appears at section scale, creating a warm transition zone between the dark navigation and the light product grid beneath it.

### Editorial Band

**`editorial-band`** — Sand-surfaced ({colors.surface-soft}) full-width module used for sustainability storytelling: B Corp certification, ocean-conservation partnerships, repair programme messaging. Teal (#00caaa) appears here as icon fill and inline link colour against the sand ground. Section-level padding ({spacing.section}) top and bottom gives editorial paragraphs magazine-like breathing room.

### Material Callout

**`material-callout`** — Small structured card within PDPs listing technical fabric properties: DWR treatment level, GSM weight, recycled-content percentage. Canvas (#f4f4f6) background with hairline border and {rounded.sm} radius. A teal ({colors.accent-teal}) icon precedes each attribute row; body-sm Roman at 14px carries the value text. Padding {spacing.base} on all sides.

### Search Bar

**`search-bar`** — Inline within the nav bar at desktop; expands to a full-width overlay on mobile. Canvas background, hairline border, {rounded.xs}. Muted-soft (#9a9db1) placeholder; ink text on entry. Search icon right-aligned in muted (#676986). Enter key or icon tap fires the query with no separate submit button required.

### Category Label

**`category-label`** — All-caps label-caps typography (11px, +1px tracking) in muted (#676986) on transparent ground. Used above product-grid headings and within faceted filter panels. Hover promotes text to ink with no background change.

### Size Guide Trigger

**`size-guide-trigger`** — Underlined caption-scale (12px Roman) link in muted (#676986). Appears directly below the size-selector row on every PDP. Hover darkens text to ink. On mobile, tap opens a bottom-sheet modal; on desktop, a lightbox overlay.

### Footer

**`footer`** — Near-black (#010b13) footer across full width. Column headings in label-caps (Bold, 11px, +1px tracking); links in body-sm Roman at 14px, muted-soft (#9a9db1) default and on-dark on hover. A 1px primary-navy (#384972) top border separates the footer from the last page section. Newsletter email input sits in a full-width row above the link columns, using the standard text-input component against the dark surface.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline drops to display-md (32px); hero min-height 60vh; horizontal page padding collapses to {spacing.base} |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories inline, secondary in overflow drawer; hero headline at display-xl; collection header padding at {spacing.xl} |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav bar visible; editorial band switches to two-column text-plus-image layout |
| Wide | > 1440px | Four-column product grid; max-width container (~1440px) centres content; hero photography scales to fill but text column stays left-aligned with {spacing.section} left gutter |

### Touch Targets

- Primary and secondary buttons are 48px tall — minimum tap target met on mobile without override
- Nav hamburger icon: 44×44px touch region regardless of rendered icon size
- Product card wishlist icon (top-right of image): 44×44px region with {spacing.sm} padding injection
- Size-guide-trigger link bumped to 32px tap height on mobile via vertical padding
- Filter/facet checkboxes: 44px minimum row height on mobile

### Collapsing Strategy

- Navigation: primary categories visible at tablet and above; sub-navigation collapses into an accordion drawer on mobile; no mega-menu with hover at mobile breakpoint
- Product grid: 4-up → 3-up → 2-up → 1-up as viewport narrows; no horizontal-scroll carousels used in grid context
- Editorial band: side-by-side text and image stacks to image-above-text on mobile; image compresses to a 50vw-equivalent height cap
- Footer columns: 4-column grid collapses to 2 at tablet, single expandable accordion per column on mobile; newsletter row stays full-width at all breakpoints
- Collection header: headline drops one type scale (display-md → title-md) on mobile; description paragraph truncated to 3 lines with expand toggle

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed custom brand typeface — Helvetica Neue LT W05_55 Roman and W05_75 Bold identified from font-family stacks, but whether Light or Medium weights are in use for intermediate UI contexts is unconfirmed
- Several extracted hex values (#eb001b, #e9500e, #ff5f00, #f79e1b, #142688, #003087, #00a2e5, #7375cf) are consistent with Mastercard, Visa, PayPal, Klarna, and Amex payment-icon assets; excluded from the brand palette
- Exact button border-radius unconfirmed — {rounded.xs} (4px) inferred from structural, low-curvature aesthetic; production value may be 0px (square) or 2px
- Sale price / strikethrough price colour treatment unconfirmed; no brand-specific sale-red was isolable from non-payment hex values in the extraction
- Icon system stroke weight and fill-versus-outline convention not determinable from colour/font extraction alone
- Exact nav bar height (56px) is an estimate; sticky-nav shrink-on-scroll behaviour unconfirmed
- #ffcf2a (yellow) and #b2f9e9 (seafoam) appear in extraction but precise usage context — whether badge, alert, or background — could not be confirmed without rendered DOM inspection
- Dark-mode or alternate colour theme support not determinable from static extraction
