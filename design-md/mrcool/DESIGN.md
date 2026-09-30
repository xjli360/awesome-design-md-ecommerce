---
version: alpha
name: "MrCool"
source_url: "https://mrcool.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The precharged lineset that made DIY mini-split installation a weekend project shows up in the palette as a very particular shade of blue — not the generic tech #0071e3 (present but secondary), but a deeper, more confident #005dcf that carries every primary CTA, header logo, and cart button. Against canvas whites (#f7f8f9, #f5f5f5) and cool gray surfaces (#f1f5f9), that brand blue reads authoritative — the HVAC technician's uniform color, coded for e-commerce. Type is set entirely in Inter (loaded as `interFont`), an unusual move for a brand that could lean utilitarian-grotesque; it signals tech-forward positioning rather than contractor-grade heritage. The cooling metaphor extends past the brand name into the accent palette — thin cyan washes (#ecfeff, #a5f3fc, #7dd3fc) appear in feature callout zones and efficiency-rating chips, evoking conditioned air without becoming illustrative. Amber (#d97706) surfaces almost exclusively for energy-efficiency warnings and SEER-rating labels — the one warm note in an otherwise cold-spectrum palette, reading as "caution: this is technical data" rather than decoration. Green (#22c55e) anchors Energy Star and in-stock confirmations, forming a traffic-light trio with the amber and blue that guides purchasing decisions through spec-heavy product pages. Corner radii stay shallow — 8px on buttons, 12px on cards — keeping the design adjacent to technical documentation without tipping into clinical. Hero sections stack a dark overlay (#111827 at ~65% opacity) over lifestyle photography of installed units and suburban homes, letting the brand blue CTA button float as the sole saturated element in the frame. The product card is the brand's workhorse surface: white fill, a soft hairline border (#e5e7eb), BTU and coverage-area chips in light-blue (#f1f5f9), and a price block in bold #171717 — no gradients, no shadow theatrics, just legible specification density. The footer drops to #282a2b near-black with reversed-out Inter in white and muted gray (#9ca3af), reinforcing the sense that this is a company that sells real hardware to people who read instruction manuals.

colors:
  primary: "#005dcf"
  primary-hover: "#0049bb"
  primary-active: "#0d5daf"
  primary-disabled: "#60a5fa"
  secondary-blue: "#0071e3"
  accent-sky: "#0ea5e9"
  accent-sky-light: "#7dd3fc"
  accent-cyan-soft: "#ecfeff"
  accent-cyan: "#a5f3fc"
  navy-deep: "#075985"
  navy-press: "#0284c7"
  energy-amber: "#d97706"
  success-green: "#22c55e"
  ink: "#171717"
  ink-warm: "#111827"
  body: "#4b5563"
  muted: "#9ca3af"
  muted-mid: "#a3a3a3"
  muted-strong: "#525252"
  hairline: "#e5e7eb"
  hairline-soft: "#d1d5db"
  hairline-mid: "#d4d4d4"
  canvas: "#f7f8f9"
  surface-white: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#f1f5f9"
  surface-warm: "#d6d3d1"
  surface-dark: "#282a2b"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#111827"

typography:
  display-xl:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  label-sm:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-value:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, 'interFont Fallback', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 1.5px
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  button-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.primary}"
  text-input-error:
    borderColor: "#ef4444"
    backgroundColor: "#fef2f2"
  select-input:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    iconColor: "{colors.muted-strong}"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.accent-sky-light}"
    padding: 10px 16px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: "{spacing.base}"
    imageBackground: "{colors.canvas}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    overlayColor: "{colors.scrim}"
    overlayOpacity: 0.65
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
    minHeight: 520px
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    imageAspectRatio: "4/3"
    hoverBorderColor: "{colors.primary}"
    borderWidth: 2px
  spec-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    typography: "{typography.caption}"
    padding: 4px 10px
  efficiency-badge:
    backgroundColor: "{colors.energy-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  eco-badge:
    backgroundColor: "{colors.success-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  diy-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  cyan-callout:
    backgroundColor: "{colors.accent-cyan-soft}"
    textColor: "{colors.navy-deep}"
    borderColor: "{colors.accent-cyan}"
    borderWidth: 1px
    borderLeft: "4px solid {colors.accent-sky}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    typography: "{typography.body-sm}"
  spec-table:
    backgroundColor: "{colors.surface-white}"
    headerBackground: "{colors.canvas}"
    headerTypography: "{typography.caption}"
    headerColor: "{colors.muted-strong}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    altRowBackground: "{colors.canvas}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline-mid}"
    typography: "{typography.caption}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.surface-white}"
    inactiveTextColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.button-sm}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.muted}"
    linkColor: "{colors.accent-sky-light}"
    linkHoverColor: "{colors.on-dark}"
    dividerColor: "#3f4142"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The primary action button runs 48px tall with 12px/24px padding and Inter 600 at 16px on MrCool blue (#005dcf). Hover deepens to #0049bb; active press moves further to #0d5daf; disabled desaturates to a washed sky-blue #60a5fa. The {rounded.sm} (8px) radius stays firm — technical but not harsh. This button appears on every product card, the sticky nav's "Shop Now" link, and the hero CTA.

**`button-secondary`** — White fill with a 1.5px #005dcf border and blue label at the same 48px height. Used for "Learn More," "Compare Models," and dealer-locator CTAs where a full-blue fill would compete with a nearby primary action. On hover a faint {colors.surface-card} bleed reinforces interactivity without breaking the outlined silhouette.

**`button-ghost`** — Transparent background, primary-blue label, no border. Used for text-level actions inside spec callouts, accordion footers, and inline "See All" links. Keeps ink weight low where the surrounding content is already dense.

**`button-small`** — 36px height at 14px Inter 600 with {rounded.xs} (4px). Used on compact listing rows and mobile card footers where the 48px primary would dominate the card. Still uses brand blue fill to maintain CTA hierarchy.

### Inputs

**`text-input`** — 48px tall, 1px {colors.hairline} border at {rounded.sm}, Inter 400 at 16px. Focus transitions the border to #005dcf with no shadow. Error state sets border to #ef4444 and warms the background to #fef2f2. Appears in the zip-code BTU compatibility checker, newsletter signup, and account forms.

**`search-bar`** — 44px, lighter than the full text-input — hairline border, muted placeholder, a search icon in {colors.muted-strong} on the left rail. Drops into the sticky nav on scroll and into the mobile drawer header. The slightly reduced height keeps it visually subordinate to the nav's primary CTA.

### Navigation

**`nav-bar`** — 64px white bar with a 1px bottom hairline. Left: logo mark in #005dcf. Center: category links in {typography.nav-link} Inter 500 at 14px. Right: cart icon plus "Shop Now" in button-primary. A 40px `promo-banner` in brand blue mounts above it for seasonal campaigns, making the total nav stack 104px at desktop. Collapses to hamburger at mobile.

**`nav-bar-dark`** — The same structural 64px nav floated over hero photography. Type and icon colors invert to {colors.on-dark}; the border disappears. Used on landing pages where photography fills the viewport top edge.

### Product Card

**`product-card`** — White card with 1px {colors.hairline} border and {rounded.sm} corners. The image zone occupies roughly the top 55% on a {colors.canvas} (#f7f8f9) background — enough neutral field to make unit photography pop without extra compositing. Below: model name in {typography.title-sm} Inter 600, then a horizontal chip row of spec-chips (BTU, zones, sq ft coverage) in {colors.surface-card} light-blue. The price block in {typography.price} Inter 700 sits above a full-width button-primary. Badges (diy-badge, efficiency-badge, eco-badge) pin to the image's top-left corner at 3px/8px.

### Hero Banner

**`hero-banner`** — Full-bleed lifestyle photography at 520px minimum height with a {colors.scrim} overlay at 65% opacity. White {typography.display-xl} headline and {typography.body-md} subtitle stay legible over any image tone. The CTA button-primary is the only fully saturated element in the frame — every color decision in the overlay pushes toward that single blue anchor. On mobile the hero crops to 360px and the headline degrades to {typography.display-md}.

### Badges

**`spec-chip`** — Rectangular chip in {colors.surface-card} light blue with a 1px {colors.hairline} border at {rounded.xs}. Carries BTU ratings, zone counts, and coverage-area data in {typography.caption}. Display-only — no tap behavior.

**`efficiency-badge`** — Amber (#d97706) filled tag at {rounded.xs} with white {typography.badge} all-caps. Communicates SEER and EER ratings on listing pages and PDPs. The amber is isolated to this context — its warmth against the blue-dominant palette creates immediate visual contrast, functioning as a data signal rather than a brand color.

**`eco-badge`** — Green (#22c55e) version of the badge shape. Used for Energy Star Certified, Eco Mode, and environmental compliance marks. Together with efficiency-badge, it forms a visual shorthand for the brand's efficiency story.

**`diy-badge`** — Brand-blue (#005dcf) badge with white "DIY Install" or "Pre-Charged" copy. Appears on every eligible product card — signals MrCool's defining market claim that no HVAC contractor is required for installation.

### Callouts

**`cyan-callout`** — {colors.accent-cyan-soft} (#ecfeff) background with a 4px left border in {colors.accent-sky} (#0ea5e9). Used for compatibility notes, BTU calculator prompts, and installation prerequisite alerts. The {colors.navy-deep} (#075985) text on the cyan wash reads clearly while staying visually distinct from both standard body text and error states.

### Spec Table

**`spec-table`** — Full-width table on product detail pages. Header row in {colors.canvas} with {typography.caption} uppercase column labels in {colors.muted-strong}. Data rows alternate between white and {colors.canvas} at 1px {colors.hairline} borders — deliberately datasheet-close in presentation. Pairs with the spec-chip row above the fold as a "summary then detail" disclosure pattern.

### Footer

**`footer`** — {colors.surface-dark} (#282a2b) near-black field with a four-column link grid. Column headings in {typography.title-sm} Inter 600 white. Links in {typography.body-sm} Inter 400 at {colors.muted} (#9ca3af), hovering to white. A thin #3f4142 divider separates the link grid from the bottom strip, which carries social icons, payment logos, and a legal line in {typography.caption} {colors.muted}. Footer link hover color uses {colors.accent-sky-light} (#7dd3fc) to maintain a blue throughline even in the dark field.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero crops to 360px, headline drops to display-md; nav collapses to hamburger drawer; spec chips wrap to two-per-row; spec table gets horizontal scroll wrapper |
| Tablet | 744–1128px | Two-column product grid; hero at 420px; promo banner persists; nav shows three primary category links, overflow behind hamburger |
| Desktop | 1128–1440px | Three-column product grid; full nav bar at 64px plus 40px promo banner; hero at 520px; spec table full-width |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered on {colors.canvas}; hero expands to 600px with wider image crop |

### Touch Targets

- All primary and secondary buttons: 48px minimum height
- button-small: 36px height with at least 8px vertical margin above and below to maintain 44px composite tap zone
- Nav hamburger icon: 44×44px tap target
- Product card: entire card surface is a single tap target linking to PDP
- Spec chips and badges are display-only — no minimum tap size
- Pagination items: 40px minimum height

### Collapsing Strategy

- Nav collapses to hamburger at < 744px; drawer slides in from left over a {colors.scrim} scrim, full viewport height, white background
- Product grid: 4-col (wide) → 3-col (desktop) → 2-col (tablet) → 1-col (mobile)
- Spec table wraps in an `overflow-x: auto` container on mobile; column labels stay visible via sticky positioning
- Footer four-column grid stacks to a single-column accordion on mobile; each section collapses under a tappable heading with a chevron toggle
- Promo banner persists at all breakpoints; reduces from 40px to 36px on mobile with truncated copy and a "See Details" link
- Cyan callout blocks stack below associated content on mobile rather than floating inline alongside it
- Category tiles collapse from a 4-across grid to a 2-across grid at tablet and a single horizontal scroll lane at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-specific display typeface detected; Inter (`interFont`) is the sole loaded font — MrCool likely uses no custom type beyond Inter weight variation
- Logo mark SVG and its exact color value could not be extracted; #005dcf is inferred from the dominant primary
- Exact CSS corner-radius values were not present in extracted tokens; 8px (sm) and 12px (md) are inferred from visual inspection
- Box-shadow values absent from extraction; card elevation is assumed to use flat-border styling rather than drop shadows
- Animation easing curves and transition durations are unspecified
- Modal and drawer overlay patterns (cart drawer, video lightbox, filter panel) could not be confirmed from extraction
- Price formatting conventions — MSRP strike-through color, sale price treatment, financing badge — not confirmed
- Mobile menu drawer exact dimensions, transition timing, and secondary nav structure not captured
- Hover state behaviors for category tiles and nav links are inferred, not extracted
