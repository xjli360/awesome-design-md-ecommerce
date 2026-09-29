---
version: alpha
name: "Bullard"
source_url: "https://www.bullard.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The yellow hard hat — Bullard's factory-floor constant since 1898 — acts as the single organizing principle for everything downstream in the interface. Accent amber (#F5A800) carries every primary CTA, navigation hover state, and category edge marker just as the helmet carries the visual weight on a job site; no competing hue takes primary action weight, and secondary actions simply reverse to white with an ink outline. Ubuntu runs the entire UI text stack — a humanist sans with enough x-height to survive field tablets in daylight — while Berthold anchors display headings in an industrial authority that the lighter body copy earns by contrast. Together they produce a typographic ladder that descends cleanly from full-bleed hero callouts through product specification sheets without a redundant step.

  Interface corners are kept square-to-slight: {rounded.sm} on buttons and cards, {rounded.xs} on input borders, nothing softer than {rounded.md} on pill badges. This is deliberate — when corners soften past a threshold, PPE equipment begins to read as consumer wellness, and Bullard's buyers are procurement managers who audit compliance certifications before aesthetic considerations. The palette doubles as a hazard-communication vocabulary: danger red (#D32F2F) for critical safety alerts, primary amber for CTAs and cautions, and safety green (#388E3C) for compliance confirmations — all colors that field workers parse instantly from actual signage without cognitive translation.

  Spec tables and compliance badges operate as first-class design objects, not content afterthoughts. Part numbers carry their own typography scale with monospace-adjacent tracking so procurement systems can scan them in a grid. The top navigation organizes by product type — Hard Hats, Respiratory, Thermal, Fall Protection — in a structured mega-menu, with no lifestyle photography displacing the category hierarchy. The footer drops to a deep navy (#1A2033) ground for the "Since 1898" heritage lockup and regional distributor links, the brand's sole moment of warmth in an otherwise strictly functional surface system.

colors:
  primary: "#F5A800"
  primary-active: "#D48E00"
  primary-disabled: "#FAD98B"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#6B6B6B"
  hairline: "#DCDCDC"
  hairline-soft: "#EFEFEF"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  on-primary: "#000000"
  navy: "#1A2033"
  navy-active: "#0D1322"
  on-navy: "#FFFFFF"
  danger: "#D32F2F"
  danger-soft: "#FFEBEB"
  danger-text: "#B71C1C"
  safe: "#388E3C"
  safe-soft: "#E8F5E9"
  caution: "#FFC107"
  caution-soft: "#FFF8E1"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Berthold', 'Berthold Akzidenz Grotesk', Arial, Helvetica, sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Berthold', 'Berthold Akzidenz Grotesk', Arial, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Berthold', 'Berthold Akzidenz Grotesk', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  nav-category:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  part-number:
    fontFamily: "'Ubuntu Mono', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  compliance-badge:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  hero-eyebrow:
    fontFamily: "'Ubuntu', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 2px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 10px 22px
    height: 44px
  button-secondary-amber:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    border: none
    padding: 10px 4px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "3px solid {colors.primary}"
    logoHeight: 36px
    padding: "0 {spacing.xl}"
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    categoryHeadingTypography: "{typography.nav-category}"
    linkTypography: "{typography.nav-link}"
    border: "1px solid {colors.hairline}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xl}"
    columnGap: "{spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    partNumberTypography: "{typography.part-number}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    accentBar: "3px solid {colors.primary}"
    accentBarPosition: top
    imageBackground: "{colors.surface-soft}"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.primary}"
    hoverAccent: "4px solid {colors.primary}"
    accentPosition: left
    padding: "{spacing.lg}"
    iconSize: 48px
  compliance-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.compliance-badge}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "4px 8px"
    certifiedVariant:
      backgroundColor: "{colors.safe-soft}"
      textColor: "{colors.safe}"
      border: "1px solid {colors.safe}"
  safety-alert:
    danger:
      backgroundColor: "{colors.danger-soft}"
      textColor: "{colors.danger-text}"
      typography: "{typography.body-sm}"
      border: "1px solid {colors.danger}"
      rounded: "{rounded.sm}"
      padding: "{spacing.base}"
      iconColor: "{colors.danger}"
    caution:
      backgroundColor: "{colors.caution-soft}"
      textColor: "{colors.ink}"
      typography: "{typography.body-sm}"
      border: "1px solid {colors.caution}"
      rounded: "{rounded.sm}"
      padding: "{spacing.base}"
      iconColor: "{colors.caution}"
    safe:
      backgroundColor: "{colors.safe-soft}"
      textColor: "{colors.safe}"
      typography: "{typography.body-sm}"
      border: "1px solid {colors.safe}"
      rounded: "{rounded.sm}"
      padding: "{spacing.base}"
      iconColor: "{colors.safe}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    headerTextColor: "{colors.muted}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.body}"
    partNumberTypography: "{typography.part-number}"
    borderColor: "{colors.hairline}"
    rowHoverBackground: "{colors.surface-soft}"
    altRowBackground: "{colors.canvas}"
    rounded: "{rounded.none}"
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    eyebrowTypography: "{typography.hero-eyebrow}"
    eyebrowColor: "{colors.primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaButton: "{components.button-primary}"
    padding: "{spacing.section}"
    minHeight: 520px
    imageOverlay: "rgba(26,32,51,0.55)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: "0 14px"
    submitButtonBackground: "{colors.primary}"
    submitButtonColor: "{colors.on-primary}"
    submitButtonRounded: "{rounded.none}"
  part-number-lookup:
    backgroundColor: "{colors.surface-soft}"
    inputTypography: "{typography.part-number}"
    labelTypography: "{typography.spec-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    accentColor: "{colors.primary}"
  distributor-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "6px 10px"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.nav-category}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.section} {spacing.xl}"
    heritageTypography: "{typography.display-sm}"
    heritageColor: "{colors.primary}"

## Components

### Buttons

**`button-primary`** — Amber (#F5A800) fill with black text, 44px tall, {rounded.sm} corners, uppercase 14px Ubuntu Bold with 0.8px letter-spacing. The high-contrast black-on-amber pairing is required by safety industry readability conventions rather than stylistic choice. Active state deepens to #D48E00; disabled washes to #FAD98B with muted text. This button anchors every product page CTA and quote-request form submission.

**`button-secondary`** — White fill with a 2px solid black border and matching uppercase typography. Used for secondary actions like "Download Spec Sheet" or "Find a Distributor" alongside a primary CTA. The `button-secondary-amber` variant swaps border and text to primary amber for placement on dark surfaces.

**`button-ghost`** — Transparent background with amber text, no border, used for inline text-link-style CTAs ("View All Hard Hats →") within category sections. Keeps the amber brand connection without visual weight competing with card grids.

### Text Input & Search

**`text-input`** — White canvas, 1px hairline border at rest, 1px amber border on focus. {rounded.xs} to match the industrial squared-off aesthetic. Used in contact forms, RFQ flows, and filter panels. Placeholder sits in muted gray (#6B6B6B).

**`search-bar`** — Full-width at mobile; constrained to ~480px in desktop header. Submit button is amber-filled with no radius to butt flush against the input's right edge, forming a single compound control. The `part-number-lookup` variant uses monospace input typography and is placed on the product catalog pages for direct SKU entry.

### Navigation

**`nav-bar`** — 64px tall, white background, anchored at the top with a 3px amber bottom border that serves as a persistent brand signal across all scroll states. Logo sits left; primary category links (Hard Hats, Respiratory, Thermal, Fall Protection) run center-right in Ubuntu Medium 14px. A utility row above carries phone number, distributor locator, and language selector in caption-size type.

**`nav-mega-menu`** — Drops on hover/focus for each primary category. Organizes sub-categories in 3–4 columns with uppercase spec-label headings and plain nav-link items below. A 3px amber top border echoes the nav-bar signature. Product imagery thumbnails appear in a right-side column. Closes on outside click or Escape.

### Product Cards

**`product-card`** — White surface with 1px hairline border and a 3px amber accent bar across the top. Image sits in a light gray (#F5F5F5) square at top; product name in title-sm below, part number in part-number typography (monospace), and a compliance badge strip near the bottom. Hover lifts box-shadow slightly and deepens the accent bar to primary-active amber. Cards appear in 3-col desktop grids, 2-col tablet, 1-col mobile.

**`category-card`** — Used on the category landing pages and homepage product-type grid. Icon (48px) + category name in title-md + short descriptor in body-sm. Left accent bar (4px amber) appears on hover, transitioning from hairline border. Larger format than product-card — fills a wider column slot.

### Compliance & Safety Indicators

**`compliance-badge`** — Compact pill-shaped tags reading "ANSI Z89.1", "ISEA 200", "NIOSH", etc. Default is surface-soft background with muted gray text. `certifiedVariant` flips to safe-green background for "Certified" or "Compliant" status. Font is compliance-badge: 10px Ubuntu Bold, uppercase, 0.8px tracking.

**`safety-alert`** — Three severity variants (danger/caution/safe) that directly map to hazard-communication color codes. Danger uses #D32F2F on #FFEBEB; caution uses amber (#FFC107) on #FFF8E1; safe uses #388E3C on #E8F5E9. Each carries an icon slot, a bold heading, and body-sm body copy. Used in product warning panels and installation instruction callouts.

### Spec Table

**`spec-table`** — The primary content unit on product detail pages. Header row on surface-soft (#F5F5F5) with spec-label typography (uppercase, tracked). Data cells in body-sm; part numbers in part-number (monospace) font. No border radius. Alternating row backgrounds are disabled by default (single color for cleaner scan). Horizontal scroll at < 744px rather than collapsing columns — spec data must remain intact.

### Hero

**`hero-banner`** — Full-bleed panel on navy (#1A2033) ground with a dark overlay (rgba 55% opacity) over product photography. Eyebrow label in hero-eyebrow typography, colored in primary amber, runs above the headline. Headline in display-xl Berthold, white. Body copy in body-md, white at reduced opacity. Primary CTA button sits below. Min-height 520px; taller on desktop wide. Used on homepage and primary category entrances.

### Footer

**`footer`** — Navy (#1A2033) background with a 4px amber top border. Column layout: Products, Support, Company, Contact. Headings in nav-category typography (uppercase, amber on hover). Links in body-sm white at 80% opacity, brightening to amber on hover. "Since 1898" heritage lockup renders in display-sm Berthold in amber, left-anchored. Social icons and certifications strip at the very bottom in a slightly darker navy band.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout. Hamburger menu replaces top nav; mega-menu becomes full-screen drawer. Spec tables scroll horizontally. Product grid drops to 1 column. Hero min-height 320px. Search bar full-width in drawer. |
| Tablet | 744–1128px | 2-column product grid. Mega-menu collapses to 2 columns. Nav utility row hidden; phone number moves to hamburger drawer. Hero at 420px min-height. Spec tables remain full-width with scroll. |
| Desktop | 1128–1440px | 3-column product grid. Full mega-menu at 4 columns. Nav bar shows all primary links. Hero full spec. Spec tables at natural width inside content max-width container. |
| Wide | > 1440px | Max content width ~1360px, centered. Product grids can expand to 4 columns on category pages. Hero full-bleed background, content capped. Footer columns spread with more gap. |

### Touch Targets

- All buttons minimum 44×44px regardless of visual size
- Navigation items in mobile drawer minimum 48px tall with full-width tap zones
- Compliance badge taps expand to 36px tall on mobile for filter interactions
- Spec table row height minimum 40px on mobile for scrollable row selection

### Collapsing Strategy

- Top nav utility row (phone, distributor locator) hides at < 1128px; moves into mobile drawer
- Mega-menu columns collapse from 4 → 2 at tablet, then to full-drawer list at mobile
- Spec table columns never collapse — horizontal scroll is mandatory to preserve data integrity
- Category card icon-only view at < 744px; text label wraps below icon in 2-col grid
- Footer columns collapse from 4 → 2 at tablet, then → 1 stacked at mobile with accordion section toggles

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — The Bullard site returned an anti-bot challenge page ("Just a moment...") during extraction; zero brand hex values were captured. All color tokens above are derived from widely documented brand knowledge (safety amber, navy ground, hazard-communication red/yellow/green) and should be verified against the live site's CSS or brand guidelines before production use.
- **Primary amber exact value unconfirmed** — #F5A800 is an approximation of Bullard's known amber/yellow brand color; official brand guidelines may specify a Pantone-matched hex that differs.
- **No theme-color meta tag found** — Common on headless or JS-heavy commerce sites; confirms no reliable browser-chrome brand color is declared.
- **Berthold variant unspecified** — "Berthold" in the font stack could refer to Akzidenz Grotesk, Block, or another face in the Berthold library; the specific variant couldn't be confirmed from extraction.
- **Font weight availability** — Actual loaded font weight variants for both Berthold and Ubuntu were not confirmed; bold/700 assumed available for both.
- **Logo lockup dimensions** — Exact SVG/image dimensions of the Bullard wordmark not captured; logoHeight: 36px is a typical industry estimate.
- **E-commerce vs. catalog** — It is unclear from extraction whether Bullard operates a transactional Shopify/commerce layer (platform-shopify: False) or purely a product catalog with distributor redirect; components like cart and checkout are omitted pending confirmation.
- **Dark mode** — No evidence of dark-mode support found; no dark-mode tokens defined.
