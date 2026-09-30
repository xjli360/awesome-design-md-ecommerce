---
version: alpha
name: "Secretlab (Office)"
source_url: "https://secretlab.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Near-black zinc (#18181b) dominates Secretlab's canvas the way a carbon-fiber dashboard dominates a cockpit interior — it is not atmosphere but a technical substrate that makes the deep Secretlab crimson (#a72a2f) read as an instrument callout rather than decorative flourish. The chair configurator is the most revealing design surface — color swatches arrive as 28px circles labeled with code names, rendered against a dark card field (#3f3f46), and the chair itself renders at near-photographic quality against a clean background — this is the grammar of automotive interior specification, not furniture retail. DIN 2014 carries all headline and button work at compressed tracking and elevated weight; Soleil handles body copy with a softer stroke and looser leading, providing the breathing room that prevents long-form specification copy from collapsing under its own density. Button labels render in DIN 2014 uppercase at 0.5px tracking — a mark of performance-hardware UI rather than lifestyle commerce. The palette is multi-register and semantically strict — crimson (#a72a2f) owns primary CTAs and active states; a harder red (#dc2626) appears only in urgency contexts — sale indicators, low-stock alerts — preserving the brand crimson from erosion by overuse. Forest green (#117937), amber (#f59e0b), and cyan (#22d3ee) populate model-tier and feature badges (NEO Hybrid, SoftWeave Fabric, TITAN Evo designations) as a coded taxonomy rather than accent decoration. Two gold registers — warm yellow-gold (#e8d087) and desaturated bronze (#baa35b) — surface in premium-material callouts and award iconography without overpromising luxury. Geometry is deliberately compressed — 4px button radii, 4–8px card corners, zero applied ornamentation — with the color-swatch selector as the single soft departure, those full circles ({rounded.full}) standing against rectilinear product cards. Vertical section rhythm is generous (64–96px), internal component gaps tight (8–12px), mirroring the product's own proportions — wide in silhouette, exact in joinery. Crimson confined to action surfaces and zinc neutrals carrying the structural weight is what earns the office positioning — not a palette wash toward beige.

colors:
  primary: "#a72a2f"
  primary-active: "#862226"
  primary-disabled: "#d39597"
  primary-danger: "#dc2626"
  primary-danger-dark: "#bb3338"
  accent-green: "#117937"
  accent-green-light: "#70af87"
  accent-amber: "#f59e0b"
  accent-cyan: "#22d3ee"
  gold-warm: "#e8d087"
  gold-muted: "#baa35b"
  gold-rich: "#623f04"
  ink: "#18181b"
  body: "#27272a"
  muted: "#71717a"
  muted-soft: "#a1a1aa"
  hairline: "#d4d4d8"
  canvas: "#121417"
  canvas-secondary: "#1a1a1a"
  surface-soft: "#27272a"
  surface-card: "#3f3f46"
  surface-raised: "#52525b"
  on-primary: "#ffffff"
  on-dark: "#fafafa"
  light-canvas: "#f2f2f2"
  light-surface: "#f4f4f5"
  cream-soft: "#fdecce"
  error-soft: "#ea7d7d"

typography:
  display-xl:
    fontFamily: "'din-2014', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'din-2014', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.8px
  display-sm:
    fontFamily: "'din-2014', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.4px
  title-md:
    fontFamily: "'din-2014', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-sm:
    fontFamily: "'din-2014', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'soleil', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'soleil', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'soleil', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'din-2014', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'din-2014', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  model-label:
    fontFamily: "'din-2014', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "'din-2014', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: -0.3px
  nav-link:
    fontFamily: "'din-2014', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageRatio: "4:3"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 600px
    padding: "0 {spacing.xxl}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
  model-badge:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.on-dark}"
    typography: "{typography.model-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  model-badge-premium:
    backgroundColor: "{colors.gold-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.model-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  color-swatch-selector:
    size: 28px
    rounded: "{rounded.full}"
    borderWidth: 2px
    borderColor-selected: "{colors.on-dark}"
    borderColor-unselected: "transparent"
    gap: "{spacing.sm}"
  spec-row:
    backgroundColor-odd: "{colors.surface-soft}"
    backgroundColor-even: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    iconColor: "{colors.gold-warm}"
    padding: "{spacing.lg} 0"
  sale-badge:
    backgroundColor: "{colors.primary-danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.model-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  material-tag:
    backgroundColor: "transparent"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    borderWidth: 1px
    borderColor: "{colors.surface-raised}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"

## Components

### Buttons
**`button-primary`** — The primary CTA renders Secretlab crimson (#a72a2f) at full saturation, 4px radius, DIN 2014 uppercase at 48px height — assertive rather than inviting. On hover it deepens to #862226 with no scale or shadow animation; the brand prefers direct state transitions over playful motion. Disabled state mutes to #d39597 with no opacity trick. The secondary variant inverts to a hairline-bordered ghost on the dark canvas, preserving DIN 2014 uppercase so both buttons carry identical typographic authority regardless of fill.

### Text Input
**`text-input`** — Form fields sit on the surface-soft (#27272a) layer at 2px radius with a 1px hairline border that brightens to #a1a1aa on focus. Placeholder text uses muted gray (#71717a) against the near-black field. Height matches buttons at 48px so inline form rows align without override. Error states swap the border to #dc2626 and render an error-soft (#ea7d7d) message below in Soleil caption.

### Navigation
**`nav-bar`** — The top nav is a full-width #121417 bar at 64px height carrying the Secretlab wordmark at far left and model-category links (TITAN, NEO Hybrid, Accessories) in DIN 2014 nav-link at 14px/0.3px tracking. A 1px hairline border separates it from the hero; on scroll it stays flush against the dark page — depth comes from color contrast alone, not shadow. A secondary icon row at far right carries search, wishlist, and cart in 20px stroked icons at #a1a1aa. Mobile collapses to a hamburger at left with the logo centered.

### Product Card
**`product-card`** — Cards float on the #3f3f46 surface against the near-black canvas at 4px radius, chair photography occupying the upper two-thirds at 4:3 ratio against a neutral gradient field. Model name renders in DIN 2014 title-md directly below the image, price in DIN 2014 price-display (24px/700) immediately beneath. Model badges (NEO Hybrid, TITAN Evo) sit as {rounded.xs} chips at the card upper-left; a sale badge at upper-right when applicable. Hover applies a 1px crimson top border without lifting or scaling the card.

### Hero Banner
**`hero-banner`** — Full-bleed canvas (#121417) sections at 600px minimum height carry a hero-lit chair render at right and DIN 2014 display-xl headline copy at left. Body copy runs in Soleil body-md below the headline with 16px separation; the primary CTA button sits 24px below body copy. On wide viewports the hero expands to full viewport height with the chair image filling 50% of the horizontal field at object-fit: cover. Alternate hero modules carry a full-bleed chair photograph with a crimson gradient overlay anchoring headline legibility.

### Announcement Bar
**`announcement-bar`** — A 40px crimson bar anchored above the nav carries promotional text in Soleil body-sm at white on crimson. Inline links use underline-only styling with no color change. The bar is persistent on desktop; on mobile it gains a close icon at far right at 20px tap zone. Text is centered. Multiple messages rotate on a 4-second interval with a fade transition.

### Model Badges
**`model-badge`** / **`model-badge-premium`** — Taxonomy chips in DIN 2014 uppercase at 11px/1px tracking identify chair series and material variants. Standard badges sit on #52525b (surface-raised); premium-material badges (NAPA Leather, SoftWeave Plus) use warm gold (#e8d087) background with dark ink (#18181b) text to signal tier elevation without introducing a third CTA color. Both carry 2px radius to hold precision against dark card backgrounds. Badges stack vertically in the product card when multiple designations apply, with 4px gap.

### Color Swatch Selector
**`color-swatch-selector`** — A horizontal flex row of 28px full-circle swatches at 8px gap maps available upholstery options. The selected swatch carries a 2px white (#fafafa) ring border; unselected swatches have no border and no hover ring — selection state is explicit, not hinted. A text label below the row updates to the selected color code name in Soleil caption at #a1a1aa. Swatches use overflow: hidden with either a solid color fill or a micro-texture image for fabric variants.

### Spec Row
**`spec-row`** — Alternating #27272a / #3f3f46 rows form the technical specification table without an outer border; the color alternation provides full grid structure. The left column renders the spec label in Soleil caption at muted gray (#71717a); the right column renders the value in Soleil body-sm at #fafafa. Row padding is 8px vertical, 16px horizontal. On mobile, the label moves above the value in a single-column layout at the same padding.

### Trust Strip
**`trust-strip`** — A full-width #27272a band below the hero carries industry-award logos and certification marks. Icon glyphs fill at warm gold (#e8d087) at 16px height; label text runs in Soleil caption at muted (#71717a). Items are spaced evenly in a single horizontal row; on mobile they collapse to a 2-column grid with icons stacking above labels.

### Sale Badge
**`sale-badge`** — Urgency signals use #dc2626, not the brand crimson #a72a2f — the semantic distinction is strict. Badges float at the product card's upper-right corner, 2px radius, DIN 2014 uppercase model-label scale. Text reads "SALE" or a percentage string (e.g. "15% OFF"). They never co-appear with the gold premium badge on the same card position; when both apply, sale badge takes priority and the premium designation moves below the product title as a text chip.

### Material Tag
**`material-tag`** — Outlined ghost chips carry material names (SoftWeave Fabric, Premium PU, NAPA Leather) in Soleil caption at #a1a1aa with a 1px #52525b border on transparent background. Used in the configurator beneath the swatch selector row to confirm the active material name without competing with the swatch circles themselves. On hover the border lightens to #71717a.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with logo centered; hero stacks headline above chair image at full width; color swatch row wraps to two rows if more than 6 options; spec table renders label above value in single column |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level category links only, no mega-menu panel; hero splits 50/50 headline-left / image-right; trust strip collapses to 2×N icon grid |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu with model sub-categories on hover; hero at 600px height with right-aligned chair render; trust strip single horizontal row; spec comparison table shows up to 3 chairs side-by-side |
| Wide | > 1440px | Container max-width 1440px centered on wider viewports; hero expands to full viewport height; product grid accommodates four columns for accessories categories; configurator panel widens to show swatch grid rather than swatch row |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch target regardless of visual size
- Color swatch circles are 28px visual diameter but sit inside 44px invisible tap zones
- Spec row tap targets expand to 44px height on mobile for filter and expand interactions
- Nav hamburger and close icon both use 44×44px zones even when icon glyph is smaller

### Collapsing Strategy
- Mega-menu collapses into an accordion within the hamburger drawer; sub-categories indent 16px and expand on tap
- When a product card would carry both a sale badge and a model badge in the same corner, the model badge relocates below the product title as an inline text chip
- Hero text on mobile renders at display-sm (28px) rather than display-xl (56px), with body-sm replacing body-md to preserve hierarchy without overflow
- Trust strip drops text labels entirely on mobile, rendering icon-only at 24px with aria-labels for accessibility
- Announcement bar condenses to a single centered message on mobile; rotation pauses if reduced-motion is set

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus transition timing curves not extractable from static scrape; durations estimated at 150ms ease-out for color transitions
- Exact mega-menu column count and sub-category layout not confirmed
- Office-specific page templates (work-from-home positioning, desk bundles) not distinguished from gaming page templates in extraction
- Mobile navigation drawer background color not directly extracted; assumed to match canvas (#121417)
- DIN 2014 weight axis availability (Light 300, Regular 400, Demi 600, Bold 700, ExtraBold 800) not confirmed; weights inferred from visual hierarchy alone
- Product filter sidebar layout, behavior, and breakpoint at which it converts to a modal sheet not captured
- Checkout flow and account-page color overrides not extracted
- Chair configurator animation behavior (swatch crossfade, camera rotation, material swap) not determinable from static extraction
- Exact hero image crop positions and focal-point anchors at each breakpoint not captured
- Footer column count, link groupings, and background color treatment not extracted
