---
version: alpha
name: "La Marzocco Home"
source_url: "https://lamarzoccohome.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The first thing you notice is the warmth: #d5ccb4, a color somewhere between aged linen and the pietra forte of a Florentine workshop, spreads across hero panels and product stages with the unhurried certainty of a material that has been handled for decades. This is not a tech-startup blue or a DTC pastel — it is the specific warm champagne of espresso crema caught in afternoon light, and it carries La Marzocco's entire visual identity. Against a clean white canvas, that sand tone fills full-bleed sections, product-detail backdrops, and configurator panels, creating the sense of walking into a showroom where machines sit on warm stone plinths rather than clinical white shelves.

  Deep blue #003399 appears sparingly — in text links, secondary CTAs, and the occasional navigational accent — grounding the warmth with gravitas borrowed from traditional Italian ceramics and enamelwork. A single forest green #236b14 surfaces in availability indicators and sustainability messaging, a nod to the Tuscan hillside without becoming pastoral.

  Typography runs on a clean geometric sans-serif stack at restrained weights; display headings land around 600 weight at 36–48px with tight letter-spacing, trusting the photography of polished steel and walnut accents to carry visual weight. Body copy sits at 16px/1.6 in 400 weight, generous and unhurried. Buttons use `{rounded.sm}` with 8px corners — enough softness to feel approachable without the full pill shape that would undercut the machine-precision ethos. Product cards employ `{rounded.md}` with subtle shadow lifts, and the configurator interface uses squared-off `{rounded.xs}` toggles that echo the engineered faces of the machines themselves.

  Spacing is generous throughout: `{spacing.section}` (64px) between major content blocks, `{spacing.xl}` (32px) between product grid items. The layout breathes like an Italian exhibition catalog — never crowded, always inviting you to linger on one object before moving to the next.

colors:
  primary: "#d5ccb4"
  primary-active: "#c4b99e"
  primary-disabled: "#e8e3d8"
  deep-blue: "#003399"
  deep-blue-active: "#002277"
  forest-green: "#236b14"
  forest-green-soft: "#e6f2e4"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#6b6b6b"
  muted-soft: "#9a9a9a"
  hairline: "#e0ddd7"
  hairline-soft: "#eceae5"
  canvas: "#ffffff"
  surface-soft: "#f8f6f2"
  surface-card: "#ffffff"
  surface-warm: "#d5ccb4"
  surface-dark: "#1a1a1a"
  on-primary: "#1a1a1a"
  on-dark: "#ffffff"
  on-warm: "#1a1a1a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.8px
  display-md:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-lg:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Avenir Next', Avenir, Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px

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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.ink}"
  button-warm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-warm-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.deep-blue}"
    typography: "{typography.button-md}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.ink}"
  text-input-label:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    hoverTransform: "translateY(-2px)"
    hoverShadow: "0 8px 24px rgba(0,0,0,0.08)"
  product-card-warm:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.on-warm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero-section:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.on-warm}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section-lg} {spacing.xl}"
    minHeight: 560px
  hero-section-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section-lg} {spacing.xl}"
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 2px 12px rgba(0,0,0,0.06)"
  configurator-option:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
    selectedBorderWidth: 2px
  configurator-swatch:
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    borderWidth: 2px
    selectedBorderColor: "{colors.ink}"
    selectedOffset: 3px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headerTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-md}"
    rowPadding: "{spacing.base} 0"
    dividerColor: "{colors.hairline-soft}"
  badge-availability:
    backgroundColor: "{colors.forest-green-soft}"
    textColor: "{colors.forest-green}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.deep-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 12px 48px rgba(0,0,0,0.12)"
    inputHeight: 56px
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    thumbnailRounded: "{rounded.xs}"
    thumbnailSize: 64px
    thumbnailGap: "{spacing.sm}"
    selectedBorderColor: "{colors.ink}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px

---

## Components

### Buttons

**`button-primary`** — A solid dark button (#1a1a1a ink background, white text) at 48px height with `{rounded.sm}` corners and `{typography.button-lg}` weight-600 type. Hover shifts to `{colors.body}` (#3d3d3d) for a subtle lift without changing shape. Disabled state drops to `{colors.muted-soft}` with white text, signaling inactivity without fully disappearing. Used for all primary actions: Add to Cart, Configure, and checkout flows.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border, matching the primary's 48px height and `{rounded.sm}` radius. Hover fills with `{colors.surface-soft}` to give tactile feedback. Appears alongside primary buttons for secondary paths like "Learn More" or "Compare Models."

**`button-warm`** — The signature variant using `{colors.primary}` (#d5ccb4) as fill with dark text. Reserved for brand moments: hero CTAs on dark backgrounds, newsletter signups, and promotional cards where the warm sand tone reinforces the Florentine identity. Active state darkens to `{colors.primary-active}`.

**`button-link`** — A text-only button in `{colors.deep-blue}` with no padding or background. Used inline for navigational shortcuts, "View all" links, and breadcrumb-style actions.

### Navigation

**`nav-bar`** — A 72px-tall white bar with a subtle bottom hairline. Logo sits left, navigation links center or right at `{typography.nav-link}` (14px, weight 500, 0.3px letter-spacing). On scroll, the hairline is replaced by a 3px box-shadow for depth. Mobile collapses to a hamburger with a full-screen warm-toned overlay.

**`announcement-bar`** — A thin 36px strip above the nav in `{colors.ink}` with white caption text. Used for shipping thresholds, promotions, or event callouts. Dismissible with an × icon.

### Product Display

**`product-card`** — A `{rounded.md}` container on `{colors.surface-soft}` with `{spacing.base}` internal padding. Product image fills the top zone with `{rounded.sm}` corners. Below: title in `{typography.title-md}`, price in `{typography.price-display}` (24px, weight 600). On hover, the card lifts 2px with an 8px/24px shadow transition (200ms ease). The warm variant (`product-card-warm`) uses `{colors.surface-warm}` for featured/hero product placements.

**`image-gallery`** — Main image in a `{rounded.md}` container with `{colors.surface-soft}` fill. Thumbnail strip below uses 64px squares at `{rounded.xs}`, separated by `{spacing.sm}`. Selected thumbnail gets a 2px `{colors.ink}` border. Supports pinch-zoom on mobile and lightbox on desktop click.

**`spec-table`** — A clean vertical list of specification rows. Label column uses `{typography.spec-label}` (11px, uppercase, 0.8px tracking) in `{colors.muted}`. Value column uses `{typography.body-md}` in `{colors.ink}`. Rows are separated by 1px `{colors.hairline-soft}` lines with `{spacing.base}` vertical padding.

### Configurator

**`configurator-panel`** — The heart of the product experience. A white `{rounded.md}` card with `{spacing.xl}` padding and a soft shadow. Contains option groups (finish, color, accessories) stacked vertically with `{spacing.lg}` gaps.

**`configurator-option`** — Rectangular selection tiles at `{rounded.xs}` with 1px `{colors.hairline}` borders. Selected state swaps to 2px `{colors.ink}` border with no background change — the emphasis is on the border weight shift alone. Text uses `{typography.body-md}`. Each option can include a small thumbnail or color indicator.

**`configurator-swatch`** — Circular 40px color/finish selectors with `{rounded.full}`. Selected swatch gains a 2px `{colors.ink}` ring offset 3px from the edge (achieved via box-shadow or outline-offset). Unselected swatches have a 2px transparent border that transitions on hover.

### Hero & Content Sections

**`hero-section`** — Full-bleed panel in `{colors.surface-warm}` at minimum 560px height. Display text uses `{typography.display-xl}` positioned over or alongside a product image. The warm sand backdrop ensures the machine photography (typically silver/chrome) pops with strong contrast. Dark variant (`hero-section-dark`) inverts to `{colors.surface-dark}` with white text for dramatic product launches.

### Badges

**`badge-availability`** — Small `{rounded.xs}` pill in `{colors.forest-green-soft}` fill with `{colors.forest-green}` text. Communicates "In Stock" or "Ready to Ship" status next to product titles.

**`badge-new`** — Deep blue `{colors.deep-blue}` fill with white text at `{typography.caption}` size. Flags new products or recently launched colorways.

### Search

**`search-overlay`** — A centered modal panel at `{rounded.md}` with a prominent 56px input field and heavy shadow. Background page dims via `{colors.scrim}` at 40% opacity. Results appear below the input in a scrollable list with product thumbnails, titles, and prices.

### Footer

**`footer`** — Full-width dark section (`{colors.surface-dark}`) with white and muted-gray text. Organized in a 4-column grid on desktop collapsing to accordion on mobile. Links use `{colors.muted-soft}` at rest, transitioning to `{colors.on-dark}` on hover. Bottom row contains legal links, language selector, and payment icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger + full-screen overlay. Hero reduces to 360px height with stacked text/image. Product grid becomes 1-col with horizontal scroll for "related" rows. Configurator options stack vertically. |
| Tablet | 744–1128px | 2-column product grid. Configurator sits below product imagery rather than beside it. Nav links may partially collapse into a "More" dropdown. Hero text scales to `{typography.display-md}`. |
| Desktop | 1128–1440px | Full layout: product imagery left, configurator panel right in a 55/45 split. 3-column product grid. Full nav visible. Hero at full 560px+ height. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Generous side margins. Product grid may expand to 4 columns. Hero imagery scales proportionally with viewport. |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch area on mobile
- Configurator swatches space at least `{spacing.md}` (12px) apart for fat-finger tolerance
- Mobile nav links use 48px row height with full-width tap zones
- Close/dismiss icons padded to 44px square even when visually 24px

### Collapsing Strategy

- Desktop side-by-side layouts (image + configurator) stack to image-on-top at tablet breakpoint
- Footer columns collapse to accordions on mobile, one section open at a time
- Spec tables remain full-width but gain horizontal scroll if content exceeds viewport
- Announcement bar text truncates with ellipsis on mobile; full message on desktop
- Product card hover effects are disabled on touch devices; tap goes directly to PDP

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family stacks were extracted from the live site — fonts are likely loaded via JavaScript or a deferred stylesheet. The system stack (`'Avenir Next', Avenir, Montserrat, -apple-system...`) is an educated approximation based on the brand's geometric sans-serif aesthetic; verify against the live site's computed styles before production use.
- Only three hex colors (#d5ccb4, #003399, #236b14) were captured. Derived shades (primary-active, disabled, surface tones, hairlines) are interpolated and should be validated against actual rendered UI.
- No meta theme-color was present; mobile browser chrome color is unconfirmed.
- Exact border-radius values, shadow definitions, and spacing scale could not be measured — the values above reflect the visual impression of moderate rounding and generous whitespace but may differ by 2–4px from the true tokens.
- Animation/transition timing (easing curves, durations) was not extractable and defaults to 200ms ease throughout.
- The site is not on Shopify; CMS-specific component patterns (cart drawer, quick-add, variant pickers) may follow non-standard implementations that differ from the generic components defined here.
