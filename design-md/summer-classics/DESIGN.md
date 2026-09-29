---
version: alpha
name: "Summer Classics"
source_url: "https://summerclassics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Loretta Display headlines sit above a visual hierarchy built on deep botanical sage (#475942) — a color that functions as a ground tone rather than an accent, the way paint on a conservatory wall recedes behind the objects arranged in front of it. Neue Haas Unica carries navigation, body copy, and specification text with the clean reserve of a Swiss grotesque that knows its support role. The brand positions itself explicitly for interior designers and trade professionals, which reshapes every UI decision: product pages present finish codes, lead times, and SKU variants with the density of a material schedule; image galleries favor full-bleed lifestyle photography over isolated product shots on white; and a trade login with wholesale pricing access holds a fixed position in the global navigation. Primary CTAs run with {rounded.xs} corner radius — the near-flat geometry signals material confidence rather than the consumer-DTC friendliness of a pill button. Color application is restrained: #475942 appears on primary actions, active nav indicators, and the footer fill, while the white canvas (#ffffff) and a warm off-white surface-soft (#f8f7f5) carry most of the visible space. Display type climbs to 64px on hero sections, letting Loretta Display's ink-trap serifs resolve at full size before stepping through a disciplined scale down to 11px uppercase captions on material finish labels. No urgency mechanics appear anywhere on the site — no countdown timers, no low-stock badges, no promotional banners interrupting editorial flow — only the unhurried authority of a catalogue organized by collection, material, and trade category. Outdoor dining is treated with the same editorial gravity a shelter magazine brings to a room: season-lit tables set for eight on stone terraces, teak and powdercoat and resin wicker presented as durable choices rather than seasonal trends, the implicit promise that this furniture outlasts the terrace it furnishes.

colors:
  primary: "#475942"
  primary-active: "#324030"
  primary-disabled: "#8fa48b"
  ink: "#1c1c1c"
  body: "#3a3a3a"
  muted: "#717171"
  hairline: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f8f7f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sage-light: "#d4dcd2"
  warm-stone: "#c8b89a"
  footer-bg: "#475942"
  footer-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Loretta Display', Georgia, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Loretta Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Loretta Display', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Neue Haas Unica', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Neue Haas Unica', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Neue Haas Unica', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Haas Unica', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Haas Unica', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-caps:
    fontFamily: "'Neue Haas Unica', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0.10em
    textTransform: uppercase
  button-md:
    fontFamily: "'Neue Haas Unica', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Neue Haas Unica', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Neue Haas Unica', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0

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
    rounded: "{rounded.xs}"
    padding: 14px 28px
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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.sage-light}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-trade:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 36px
  hero-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  trade-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    height: 36px
    textAlign: center
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 40px
    padding: 0 16px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspect: "4/3"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
  product-card-collection-label:
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 640px
    overlay: "linear-gradient(to bottom, rgba(28,28,28,0.2) 0%, rgba(28,28,28,0.55) 100%)"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.xxl} 0"
  material-swatch:
    size: 40px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.primary}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
  finish-tag:
    backgroundColor: "{colors.sage-light}"
    textColor: "{colors.primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-collection:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Filled sage (#475942) with white uppercase label in Neue Haas Unica tracked at 0.08em; {rounded.xs} corners keep the geometry architectural rather than friendly. Active state deepens to #324030; disabled state desaturates to #8fa48b. At 48px height, the button aligns flush with text inputs in form rows.

**`button-secondary`** — Transparent fill with a 1px sage border and matching sage text. On active the background fills with sage-light (#d4dcd2) for state feedback without disrupting the label color. Uppercase tracking and letter spacing are identical to the primary label, so the two buttons can sit side-by-side without typographic dissonance.

**`button-trade`** — A compact 36px ink-filled button reserved for trade-account utility actions: "Trade Login," "Apply for Trade Pricing," and "Request a Quote." The smaller height and tight button-sm typography prevent it from competing with primary product CTAs.

**`hero-cta`** — Inverts the primary treatment — white fill, ink text — for legibility over dark hero imagery. Sage green is reserved for below-the-fold product and collection actions, so the hero CTA reads as a distinct entry point rather than a repeated pattern.

### Navigation

**`nav-bar`** — 72px tall, white canvas with a 1px {colors.hairline} bottom border. Neue Haas Unica nav-link at 14px carries collection category names, a trade login link, and a search trigger icon. On desktop, top-level collection items open megamenu panels organized by collection family and material type. Active items underline with a 2px {colors.primary} rule.

**`trade-banner`** — A 36px announcement bar pinned above the nav-bar, ink background with white label-caps text. Used to surface trade program messaging ("Apply for Trade Pricing," "Free Shipping on Orders Over $X"). Collapses on mobile to preserve vertical space.

**`search-bar`** — A 40px {colors.surface-soft} input with no border at rest; a 1px {colors.primary} border appears on focus. Placeholder in {colors.muted}. On mobile the nav search trigger expands to a full-width input overlay.

### Product & Collection

**`product-card`** — No rounding ({rounded.none}), white canvas background. Product name in title-md (Neue Haas Unica 16px 500); collection attribution in label-caps ({colors.muted}) sits above the name as a superscript category identifier. Image crops to a 4:3 aspect ratio. Non-authenticated visitors see a "Login for Pricing" prompt in the caption zone rather than a retail price.

**`collection-header`** — A full-width {colors.surface-soft} band housing the collection name in display-md (Loretta Display 36px) and a 2–3 sentence editorial description in body-md. The {spacing.xxl} vertical padding gives the serif headline breathing room before the product grid begins beneath it.

**`material-swatch`** — 40px circular discs ({rounded.full}) showing finish colors or fabric textures. A 2px transparent border at rest becomes a 2px {colors.primary} ring when selected, providing clear selection state without introducing a new color. Caption typography labels each swatch with its finish code name below.

**`finish-tag`** — A small sage-light background label ({rounded.xs}, 4px 8px) in label-caps using {colors.primary} text. Appears on collection headers and editorial pages to identify material families — "TEAK," "WICKER," "CAST ALUMINUM," "POWDERCOAT." Decorative, not interactive.

**`badge-collection`** — A zero-radius rectangular chip in {colors.primary} with {colors.on-primary} label-caps text. Used sparingly to flag "NEW COLLECTION" or editorial category labels on hero overlays and landing page modules. The sharp corner distinguishes it from the material-swatch visual language.

### Forms & Inputs

**`text-input`** — White background, 1px {colors.hairline} border, {rounded.xs} corner. Focus shifts the border to {colors.primary}. Placeholder in {colors.muted}. At 48px height it aligns with button-primary for consistent row composition. Appears in trade application forms, quote request flows, and newsletter capture modules.

### Footer

**`footer`** — Full-width {colors.footer-bg} (sage #475942) with {colors.footer-text} (white). Column headings in label-caps (11px, 0.10em tracking, uppercase); navigation links in body-sm Neue Haas Unica. A hairline-separated sub-row at the bottom carries legal copy, social icons, and a brief brand attribution line. The inverted sage footer makes the brand primary serve double duty as both CTA color and structural container — closing the page with the same tone that opens the primary action hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to logo + hamburger; trade-banner hidden; hero headline drops to display-sm (24px); material swatches scroll horizontally in a single row |
| Tablet | 744–1128px | 2-column product grid; nav shows logo, search icon, and hamburger; collection-header headline at display-sm; trade-banner visible |
| Desktop | 1128–1440px | 3-column product grid; full horizontal nav with megamenu; trade-banner visible; collection-header at full display-md (36px) |
| Wide | > 1440px | 4-column product grid; content max-width 1440px centered; hero min-height increases to 760px; whitespace margins widen proportionally |

### Touch Targets

- All primary and secondary buttons minimum 48px height
- Trade button (36px) appears only in utility nav zones above 744px breakpoint
- Material swatches are 40px diameter with 4px gap — meets minimum touch target with margin
- Nav items in mobile drawer accordion: minimum 48px row height
- Text inputs hold at 48px height across all breakpoints, full-width on mobile

### Collapsing Strategy

- Trade-banner collapses entirely below 744px to reclaim vertical space
- Desktop megamenu becomes a slide-in left drawer with accordion-expanded collection groups on mobile
- Material swatch rows switch from wrapping grid to horizontal scroll lane below 744px
- Collection-header editorial body text truncates to 2 lines with a "Read more" inline expansion trigger on mobile
- Product card "Login for Pricing" prompt persists across all breakpoints for unauthenticated visitors
- Footer columns stack to a single column with accordion-toggled link groups on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two hex colors were extracted (#475942 and #007aff); #007aff matches iOS/system blue and was excluded as a framework default — all neutral and surface colors (ink, body, muted, hairline, surface-soft) are derived from luxury brand conventions rather than confirmed site values
- sage-light (#d4dcd2) and warm-stone (#c8b89a) are inferred from the primary sage and typical outdoor furniture material palettes, not extracted
- No dark-mode or alternate surface tokens confirmed — the brand likely runs light-only, but this is unverified
- Font weights for Loretta Display are unconfirmed; display entries use weight 400 (regular), consistent with editorial serif display conventions, but the live site may use a different optical size or weight
- No confirmed icon system details — icon style (line, filled, bespoke glyph), sizing, and stroke weight are unknown
- Hover transition durations, easing curves, and animation properties were not extractable from the live site
- Trade-pricing gate behavior (what non-authenticated users see vs. trade-account holders) is inferred from brand positioning, not confirmed from direct extraction
- Mobile megamenu structure and number of navigation tiers are estimated from outdoor furniture category conventions
