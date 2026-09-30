---
version: alpha
name: "Glowforge"
source_url: "https://www.glowforge.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Glowforge calls its laser cutter a "3D laser printer" — a positioning move that reveals the brand's core bet: this machine belongs beside the blender, not in a fabrication shop. Every visual decision shores up that reframe. Hero sections open on deep workshop darks (#0a3036, #000527), a near-black teal that evokes standing in a studio at midnight, watching a beam trace a pattern. Against that darkness the brand's single voltage fires: laser-beam teal (#26b8ce), the precise hue of a blue diode's glow applied to every primary CTA, navigation highlight, and feature icon. It is a literal color — the machine makes that light — which gives the interface a physical grounding most software-adjacent brands lack.

  Three geometric font stacks divide the voice. Space Grotesk carries display headlines with its open apertures and slightly quirky lowercase, reading as confident without shouting. Exo 2 handles model-name badges and technical callouts, lending spec copy a futurist edge that stops short of science fiction. Poppins flows through body copy and UI labels, adding warmth where the other two would harden. No serif surfaces anywhere — this is a brand organized around precision and forward motion.

  The palette layers depth and warmth against each other. Below the primary, a family of dark teals (#0f4b55, #334b4f) structures mid-section backgrounds, reading as shadow rather than neutral gray. A warm cream register (#fdf5e9, #faecd5) appears specifically in project-showcase areas, where finished objects — jewelry boxes, engraved leather, acrylic signage — are photographed against warm grounds. That temperature contrast is structural: the machine is cold precision; its output is warm and human. Radius language stays moderate throughout, with product cards at {rounded.md} and primary buttons at {rounded.sm}. Hero sections run full-bleed and borderless. Spacing is wide at every breakpoint — Glowforge sells a premium physical appliance, and the page allows photography to land before a conversion ask appears. Model-tier badges (Aura, Plus, Pro) sit in tight Exo 2 uppercase, distinguishing the lineup on a single card without a comparison table. The overall system reads as a maker tool that is genuinely proud of what its customers create.

colors:
  primary: "#26b8ce"
  primary-active: "#1e93a5"
  primary-disabled: "#9e9fa1"
  accent-bright: "#00c0d4"
  ink: "#12151a"
  body: "#334b4f"
  muted: "#9e9fa1"
  muted-soft: "#c8cbd0"
  hairline: "#e3e3e3"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-cream: "#fdf5e9"
  surface-cream-soft: "#faecd5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  hero-dark: "#0a3036"
  hero-darkest: "#000527"
  mid-teal: "#0f4b55"
  slate-teal: "#334b4f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.8px
  display-md:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-tech:
    fontFamily: "'Exo 2', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.5px
  model-badge:
    fontFamily: "'Exo 2', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Exo 2', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  price-monthly:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
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
    padding: 14px 28px
    height: 48px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-outline-light:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.on-dark}"
  button-text-light:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    padding: 0
    textDecoration: underline
  button-text-primary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted-soft}"
    borderFocused: "2px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    ctaVariant: button-primary
  nav-bar-transparent:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    imageAspect: "4/3"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    shadow: "0 4px 20px rgba(0,0,0,0.08)"
    borderOnHover: "1px solid {colors.primary}"
  hero-dark:
    backgroundColor: "{colors.hero-dark}"
    textColor: "{colors.on-dark}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.section}"
    accentColor: "{colors.primary}"
    primaryCta: button-primary
    secondaryCta: button-outline-light
  section-mid-teal:
    backgroundColor: "{colors.mid-teal}"
    textColor: "{colors.on-dark}"
    displayTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.section}"
    accentColor: "{colors.accent-bright}"
  model-tier-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.model-badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  model-tier-badge-dark:
    backgroundColor: "{colors.hero-dark}"
    textColor: "{colors.accent-bright}"
    typography: "{typography.model-badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    border: "1px solid {colors.primary}"
  feature-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    iconColor: "{colors.primary}"
    iconSize: 40px
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  feature-tile-dark:
    backgroundColor: "{colors.slate-teal}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    iconColor: "{colors.accent-bright}"
    iconSize: 40px
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  project-showcase-card:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageAspect: "1/1"
    imageRounded: "{rounded.sm}"
    captionTypography: "{typography.caption}"
    labelTypography: "{typography.label-tech}"
    labelColor: "{colors.primary}"
    padding: "{spacing.lg}"
  spec-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    borderBottom: "1px solid {colors.hairline}"
    labelColor: "{colors.ink}"
    labelTypography: "{typography.label-tech}"
    paddingY: "{spacing.md}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.hero-dark}"
    rowVariant: spec-row
  price-block:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    monthlyTypography: "{typography.price-monthly}"
    labelTypography: "{typography.body-sm}"
    muted: "{colors.muted}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
  testimonial-card:
    backgroundColor: "{colors.surface-cream-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    quoteTypography: "{typography.body-md}"
    authorTypography: "{typography.caption}"
    authorColor: "{colors.muted}"
    accentBorder: "3px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.hero-darkest}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    paddingY: "{spacing.xxl}"
    dividerColor: "{colors.slate-teal}"

## Components

### Buttons

**`button-primary`** — The primary CTA uses the laser-beam teal (#26b8ce) fill on an 8px rounded rectangle, 48px tall, with Space Grotesk 600 at 16px. On hover it deepens to `primary-active` (#1e93a5); the color shift is fast (≤150ms) to feel immediate, like the machine responding to input. The disabled state swaps fill to `primary-disabled` (#9e9fa1) with no text-color change, maintaining contrast. This button appears in hero sections, pricing rails, and product-card footers.

**`button-secondary`** — A white fill with a 2px `primary`-colored border and `primary` text, producing a ghost variant that reads as sibling to the primary. Used when a page offers two simultaneous paths of equal weight, most commonly "Buy Now" + "Learn More" stacked in the hero. On dark backgrounds, `button-outline-light` replaces it — transparent fill with a white border and white text — so the hierarchy reads correctly against both canvas and hero-dark surfaces.

**`button-text-light`** and **`button-text-primary`** — Inline text-only actions with no padding, using underline for affordance. The light variant appears on dark sections for secondary micro-actions like "See all materials"; the primary variant appears on white surfaces for "View gallery"-style links within prose.

### Navigation

**`nav-bar`** — Fixed top bar, 72px tall, white background with a 1px `hairline` bottom border. Left holds the Glowforge logomark; center or right holds product-section links in Space Grotesk 500 at 15px; far right anchors a `button-primary` CTA ("Shop"). On hero-dark pages the bar loads as `nav-bar-transparent` (transparent, white text) and transitions to the white `nav-bar` on scroll past the fold, a common Shopify hero pattern that preserves the dark cinematic opening frame.

### Product Card

**`product-card`** — White card at 12px radius with a subtle `0 4px 20px` drop shadow that lifts slightly on hover; a 1px `primary`-colored border also appears on hover to signal the card is interactive. The image occupies a 4:3 aspect ratio at top, followed by a `model-tier-badge`, title in Space Grotesk 600, a brief body description in Poppins 14px, price in `price-display` style, and a `button-primary` at the base. Cards tile in a 3-up grid on desktop, 2-up on tablet, and 1-up on mobile with full-width CTAs.

### Hero — Dark

**`hero-dark`** — The primary entry point for every major product page. The `hero-dark` background (#0a3036) fills the viewport at 100vh, with a large product photograph or video loop overlaid. Headline uses `display-xl` (Space Grotesk 700, 56px) in white; sub-headline drops to `body-md` Poppins at reduced opacity (~80%). Below the copy sit a `button-primary` and a `button-outline-light` side by side. The laser-beam teal (#26b8ce) appears as a glow element, icon tint, or animated underline to reinforce the brand voltage against the dark field.

**`section-mid-teal`** — A secondary dark section using `mid-teal` (#0f4b55), deployed mid-page for feature callouts or material showcases. It uses `accent-bright` (#00c0d4) rather than the primary for highlights, providing a subtle hue shift that signals a different content register without breaking the dark palette.

### Model Tier Badges

**`model-tier-badge`** — A small pill-shaped tag (4px radius, Exo 2 uppercase 700 at 11px, 1px letter-spacing) in `primary` fill with white text, placed above the product name on cards and comparison tables. The dark-background variant (`model-tier-badge-dark`) swaps to a `hero-dark` fill with `accent-bright` text and a `primary`-colored 1px border — used when the card itself sits on a dark section. The three model tiers (Aura, Plus, Pro) each use the same badge style; tier differentiation is handled by copy, not badge color variation.

### Feature Tiles

**`feature-tile`** — A `surface-soft` (#f5f5f5) card at 12px radius, 32px internal padding, carrying a 40px icon in `primary` teal, a `title-md` headline, and `body-sm` description copy. Tiles appear in a 3- or 4-up grid to list machine capabilities (camera alignment, passthrough slot, cloud software). On dark mid-page sections, the dark variant (`feature-tile-dark`) swaps the surface to `slate-teal` (#334b4f) with `accent-bright` icons and white copy, keeping the feature grid readable without switching to a white section.

### Project Showcase Cards

**`project-showcase-card`** — The warmest component in the system, using the cream surface (#fdf5e9) to frame user-made project photography. A 1:1 square image sits at top with 8px radius; below it, a `label-tech` line in Exo 2 names the material or technique ("Baltic Birch Plywood", "Leather Engraving") in `primary` teal, followed by a `caption` description in Poppins 12px. These cards appear in gallery rows or masonry layouts and provide the human, artisan warmth that the dark hero cannot. The warm cream is load-bearing: without it, the site reads as cold product catalog.

### Specification Rows and Tables

**`spec-row`** — A simple two-column row with a `label-tech` left cell (Exo 2 500, ink color) and a `spec-label` right cell (Exo 2 500, `body` color), separated by a 1px `hairline` bottom border. The `spec-table` wraps a set of rows in a `surface-soft` container at 12px radius with a `title-sm` section header in `hero-dark`. Specification tables appear on machine detail pages below the hero, organized by section (Laser, Bed Size, Connectivity, Software).

### Price Block

**`price-block`** — A bordered card at 12px radius (1px `hairline` border, 32px padding) holding the machine price in `price-display` (Space Grotesk 700, 40px), an optional monthly financing note in `price-monthly` (Space Grotesk 500, 20px), a `body-sm` list of included items, and a full-width `button-primary` CTA at the bottom. On desktop, three price blocks for Aura, Plus, and Pro sit side by side in a comparison rail; the featured tier receives a `primary`-colored top border (3px) to signal the recommended option.

### Testimonial Card

**`testimonial-card`** — Cream-soft (#faecd5) background with a 3px `primary` left border accent, 12px radius, and generous 32px padding. The quote runs in Poppins 400 at 16px; the maker's name and project type appear below in `caption` style with `muted` coloring. These cards appear in a horizontal scroll on mobile and a 3-up grid on desktop, positioned between the feature section and the pricing rail to bridge machine capability and human output.

### Footer

**`footer`** — Near-black (#000527) background with Poppins 14px links in white, hover-transitioning to `primary` teal. Column headings use Poppins 600 at 16px in white. A `slate-teal`-colored horizontal rule separates the link columns from the legal strip. The footer avoids the aggressive CTA energy of the hero — it is navigational and calm, a reading surface in the dark.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero copy drops to `display-md` (36px); hero CTAs stack vertically full-width; product cards 1-up; spec tables scroll horizontally; nav collapses to hamburger; project showcase tiles 2-up |
| Tablet | 744–1128px | Two-column product grid; hero copy at `display-lg` (44px); nav links partially visible or hamburger; feature tiles 2-up; price blocks stacked vertically |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at `display-xl` (56px); feature tiles 3- or 4-up; price blocks 3-up side by side |
| Wide | > 1440px | Max-width container (~1280px) centered; hero image gains more breathing room; section padding increases by ~25%; typography unchanged |

### Touch Targets

- All primary CTAs minimum 48px tall, full-width on mobile
- Nav hamburger icon minimum 44×44px touch area
- Product card entire surface is tappable; CTA button within also independently tappable
- Spec-row tap targets padded to minimum 44px height on mobile
- Footer links minimum 40px vertical spacing to reduce mis-taps

### Collapsing Strategy

- Nav collapses to hamburger at ≤ 768px; CTA button persists in header as a small pill
- Hero dual-CTA row stacks to single column at ≤ 600px; secondary CTA reduces to text-only link
- Three-column feature tile grid → two-column → single column with no breakpoint where a tile is hidden
- Horizontal project showcase carousel on mobile replaces the desktop masonry grid; swipe-enabled via Swiper.js (detected in font-family extraction)
- Spec table columns reorder on mobile: label moves above value in a stacked single-column layout rather than horizontal scrolling

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font-size scale for mobile hero headings not extracted; values above are inferred from common Shopify theme patterns
- Animation timing values (laser-glow pulse effects, CTA hover transitions) not visible in static extraction
- Icon library details unknown — likely custom SVG set, not a named open-source library
- Exact box-shadow values for product cards not extracted; values are approximated
- Dark-mode or light-mode toggle behavior not confirmed; site appears light-mode only
- Swiper.js carousel configuration (slides per view, loop behavior, autoplay timing) not extracted
- Model-specific accent colors (if Aura, Plus, Pro use distinct badge tints beyond the shared primary) not confirmed
- Checkout and account pages inherit Shopify defaults; brand customization depth on those surfaces unknown
- #007aff excluded from palette as iOS system UI blue, not a Glowforge brand color
