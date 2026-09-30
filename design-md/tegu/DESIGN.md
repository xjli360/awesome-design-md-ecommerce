---
version: alpha
name: "Tegu"
source_url: "https://tegu.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Four wooden blocks — lime, coral, sky, and amber — telegraph the entire color system before any CSS loads, because Tegu's #8dc63f green is not a brand color painted onto toys but the toy color elevated to brand infrastructure: every primary CTA, hover ring, and hero accent arrives pre-loaded with the sensory memory of magnets clicking into alignment. The near-black ground (#232323) pushes those saturated primaries into sharp contrast without resorting to flat white, giving the storefront a display-case authority unusual in children's gifting — the parent browsing at midnight reads "premium object" while the child sees a candy-bright playground. Coral (#ef6454), electric cyan (#06bfe2), and amber (#ffbb49) cycle through badges, promotional labels, and age-range chips exactly as those hues appear on the physical product line, collapsing the gap between what lands on screen and what lands in the box. The palette's logic is additive rather than neutral: nothing recedes to gray when it can carry a hue, with the near-white canvas (#f8f8f8) and mid-gray (#5f6062) body text functioning as breathing room between color blocks rather than as dominant surfaces. Product cards sit on that soft ground with generous padding ({spacing.base}), letting photographed blocks dominate without compositional competition. No proprietary typeface was captured in extraction, but the site's rhythm reads as a geometric sans-serif in the Futura / Montserrat register — rounded apertures, optically even strokes, a voice legible to adults while staying accessible to early readers. Buttons favor {rounded.md} corners rather than pill shapes, sitting between the hard-edged geometry of Montessori materials and the inflated bubbles of mass-market toy retail. Section spacing is generous ({spacing.section}), letting photography breathe and preventing the rainbow palette from overwhelming the grid.

colors:
  primary: "#8dc63f"
  primary-active: "#6fa832"
  primary-disabled: "#c5e49a"
  ink: "#232323"
  ink-deep: "#121212"
  body: "#5f6062"
  muted: "#5f6062"
  hairline: "#dedede"
  canvas: "#f8f8f8"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-coral: "#ef6454"
  accent-cyan: "#06bfe2"
  accent-amber: "#ffbb49"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Futura', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge-label:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 11px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  age-chip:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Montserrat', 'Futura', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.ink}"
    padding: 12px 26px
    height: 48px
  button-ghost-coral:
    backgroundColor: transparent
    textColor: "{colors.accent-coral}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.accent-coral}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderRadius: "{rounded.md}"
    typography: "{typography.body-md}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    imageAspect: "1 / 1"
    gap: "{spacing.sm}"
    shadow: "0 2px 12px rgba(0,0,0,0.07)"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    ctaComponent: "button-primary"
    accentBar: "4px solid {colors.primary}"
  color-swatch-block:
    shape: "{rounded.sm}"
    swatchSize: 28px
    gap: "{spacing.xs}"
    activeRing: "2px solid {colors.ink}"
  age-range-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.age-chip}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    border: "1px solid {colors.hairline}"
  promo-badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  gift-finder-cta:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg} {spacing.xl}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    hoverBackgroundColor: "{colors.primary-disabled}"
    imageAspect: "4 / 3"
  education-section:
    backgroundColor: "{colors.canvas}"
    headlineColor: "{colors.ink}"
    bodyColor: "{colors.body}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    accentBar: "4px solid {colors.primary}"
    paddingVertical: "{spacing.section}"
  promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
    paddingHorizontal: "{spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    paddingVertical: "{spacing.xxl}"
    borderTop: "4px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — Lime (#8dc63f) fill with white label and {rounded.md} corners, 48px tall. Carries all primary purchase and navigation actions; on hover backgroundColor transitions to {colors.primary-active} (#6fa832). Disabled state desaturates to {colors.primary-disabled} and drops pointer-events, preserving the green visual signal without creating a false affordance.

**`button-secondary`** — Transparent background with a 2px solid {colors.ink} border and matching ink label, 48px tall. Used in dual-CTA hero rows alongside `button-primary`; the outlined treatment keeps the lime accent undiluted for the primary action and reads cleanly on both dark hero backgrounds and light canvas grids.

**`button-ghost-coral`** — Transparent with a 2px {colors.accent-coral} border and coral label, 44px tall. Deployed on sale or urgency-adjacent CTAs where lime would signal confirmation rather than excitement — "Shop Sale" banners and seasonal clearance entries.

### Form Inputs
**`text-input`** — White fill ({colors.surface-card}), 1px {colors.hairline} border, {rounded.md}, 48px height to stay optically level with adjacent buttons. Focus ring shifts borderColor to {colors.primary}, giving green confirmation feedback without the anxiety-signal of red in a children's gifting context. Placeholder text renders in {colors.muted}.

### Navigation
**`nav-bar`** — White surface ({colors.surface-card}), 64px tall, with a 1px {colors.hairline} bottom border. Links render in {typography.nav-link} at fontWeight 600. The Tegu wordmark anchors left on desktop; on mobile the bar collapses to hamburger + centered logo. Cart and search icons sit right-aligned at all breakpoints, padded to 44px tap targets.

### Product Cards
**`product-card`** — White card with {rounded.lg} corners and a subtle drop shadow (0 2px 12px rgba(0,0,0,0.07)), lifted off the {colors.surface-soft} page ground. A 1:1 image crop dominates the upper half; title renders in {typography.title-md}, price in {typography.price-display} at fontWeight 700. `color-swatch-block` appears below the title when multiple colorways exist. A `promo-badge` overlays the image top-left when applicable.

### Age Range Chip
**`age-range-chip`** — Pill-shaped ({rounded.full}) in {colors.surface-soft} with a 1px {colors.hairline} border. Displays "Ages 3+" or "1–99" in {typography.age-chip} at fontWeight 700. The neutral styling distinguishes it from the coral `promo-badge`, functioning as developmental metadata rather than promotional pressure.

### Promo Badge
**`promo-badge`** — Coral (#ef6454) filled label with {rounded.xs} corners, {typography.badge-label} in uppercase white. Positioned absolute top-left over product-card images. Reserved for SALE, NEW, and BEST SELLER callouts — coral contrasts against the lime CTA system so neither color dilutes the other's meaning.

### Gift Finder CTA
**`gift-finder-cta`** — Amber (#ffbb49) background panel with {colors.ink} text and {rounded.lg} corners. Designed as a full-width or half-column editorial block pointing shoppers toward the curated gift-guide flow. Amber reads warm and occasion-forward without triggering the urgency association of coral or the confirmation signal of lime.

### Category Tiles
**`category-tile`** — {colors.surface-soft} background with {rounded.md} corners and a 4:3 image crop showing stacked blocks in context. Label in {typography.title-sm} at {colors.ink}. On hover, background shifts to {colors.primary-disabled} — a pale lime — confirming interactivity without underlines. Used in the shop-by-collection grid (Sets, Starters, Accessories, Gifts).

### Hero Banner
**`hero-banner`** — Full-bleed {colors.ink} (#232323) ground or high-contrast photography backdrop. Headline in {typography.display-xl} in {colors.canvas}; a 4px horizontal {colors.primary} accent bar runs beneath the headline as a lime signature stroke. CTA renders `button-primary`. The dark hero grounds the bright color system and signals premium gifting intent to adult buyers scanning after hours.

### Promo Strip
**`promo-strip`** — Full-width {colors.primary} band, 40px tall, running above or anchored below the `nav-bar`. Carries site-wide free-shipping thresholds or seasonal headlines in {typography.body-sm} white. The lime strip is the most compact possible brand-color impression on the page and serves as a visual leader into the nav.

### Education Section
**`education-section`** — {colors.canvas} background with a left-side 4px {colors.primary} vertical accent bar anchored beside the block headline. Headline in {typography.display-md} at {colors.ink}; body in {typography.body-md} at {colors.body}. Used for "Why Tegu?", safety-certification copy, and developmental-benefit storytelling where tone shifts from shop to inform.

### Footer
**`footer`** — {colors.ink} (#232323) background with a 4px {colors.primary} top border. Column headings in {colors.canvas} at {typography.title-sm}; links in {colors.hairline} at {typography.body-sm}. Newsletter input sits inline with a `button-primary`. The dark footer closes the visual bracket opened by the dark hero, bookending pages with brand-ink weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered wordmark; hero headline scales to display-md; gift-finder-cta stretches full-width; promo-strip clips to one line with overflow hidden |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links with tap-to-open dropdowns; hero splits text left / image right; category tiles go 3-up |
| Desktop | 1128–1440px | Three- or four-column product grid; sticky nav at 64px; hero goes full-bleed at display-xl headline; promo-strip always visible |
| Wide | > 1440px | Grid caps at 1440px with auto side margins in {colors.canvas}; hero image extends edge-to-edge but text column stays within a 1200px inner rail |

### Touch Targets
- All interactive elements meet a minimum 44×44px tap target on mobile
- Color swatches and age-range chips maintain at least 8px gap between adjacent targets to prevent mis-taps
- Hamburger icon padded to 44px square regardless of rendered glyph size
- Cart, search, and account nav icons padded symmetrically to 44px horizontal width

### Collapsing Strategy
- Product grid collapses: 4-col → 2-col → 1-col across Desktop → Tablet → Mobile
- Category-tile rows collapse: 4-up → 3-up → 2-up → horizontal scroll carousel on Mobile
- Footer three-column layout collapses to single accordioned column on Mobile
- Education section two-column layout (image + text) stacks image above text on Mobile
- Dual-CTA hero button rows stack vertically with full-width buttons on Mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No web fonts detected**: Font-family extraction returned empty — Tegu's typeface loads via Shopify theme JS or a font CDN that blocked extraction. Typography tokens above use Montserrat/Futura as a plausible geometric sans placeholder; verify and replace with DevTools before production use.
- **No meta theme-color set**: Mobile browser chrome color is unknown; PWA manifest behavior is unconfirmed.
- **primary-active and primary-disabled are manually derived**: #6fa832 and #c5e49a are lightness-shifted estimates from #8dc63f; measure actual hover and disabled states in DevTools.
- **surface-card white (#ffffff) is inferred**: The extractor returned #f8f8f8 as the lightest captured surface; product cards likely sit on true white but this was not directly confirmed.
- **Icon set unknown**: Navigation and UI icons were not captured; Tegu may use a proprietary SVG set or a Shopify theme icon font.
- **Animation and motion tokens absent**: Hover transition durations, easing curves, and scroll or parallax behaviors on hero sections were not extracted.
- **Sale price color treatment unknown**: Whether discounted prices render in {colors.accent-coral} or a dedicated token was not confirmed.
- **Accent-cyan (#06bfe2) usage context unclear**: This color appears in the extracted palette but its specific UI role — block colorway, promotional banner, iconography — was not identified from extraction.
