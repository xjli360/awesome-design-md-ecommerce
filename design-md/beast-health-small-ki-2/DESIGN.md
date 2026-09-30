---
version: alpha
name: "Beast Health"
source_url: "https://thebeast.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Searing orange (#ff5601) detonates against a charred-black viewport (#121212)—the entire first screen is a single blender, matte-black housing fading into darkness, with only the CTA and the speed-ring graphic carrying that orange voltage. Beast Health treats its homepage like a product shoot with scroll-triggered reveals rather than a Shopify collection page, and the restraint works: warm stone tones (#cdc3b5, #c9c5bf) and cream panels (#f8f3ec, #f0eee3) surface only when the site shifts from desire to information—specs, nutritional breakdowns, recipe carousels. Typography pairs Sofia Pro at weight 700 for display headings with DM Sans for body and UI copy, a geometric sans that stays legible at 14–16px against both the dark hero grounds and the lighter content sections. Buttons refuse to round off: `{rounded.xs}` at 4px keeps every CTA squared and machined, mirroring the blender's own chamfered housing lines rather than the soft pills that most wellness-adjacent DTC brands reach for. A secondary gold (#ffd45d) appears on star ratings and limited-run callouts, adding analog warmth to the otherwise industrial palette without competing with the primary orange. The nav runs dark (#121212) with minimal links—three or four at most—and a single cart icon, collapsing to a full-screen overlay on mobile rather than a slide-out drawer. Product cards land on warm cream (`{colors.surface-card}`) with `{rounded.sm}` corners, stacking a square product image above a tight cluster of name, single descriptor line, and price in `{typography.price-display}`. A dark teal (#364748) anchors the footer, providing a cooler counterweight to the warm neutrals above. The overall grid caps at 1440px with generous `{spacing.section}` vertical rhythm, and the site trusts full-bleed photography and inline video loops over illustration, letting the physical product's sculptural form carry visual interest across every breakpoint.

colors:
  primary: "#ff5601"
  primary-active: "#ff5500"
  primary-disabled: "#ffab80"
  ink: "#121212"
  ink-soft: "#232323"
  body: "#303030"
  muted: "#63615e"
  muted-warm: "#65605a"
  hairline: "#cfcfcf"
  hairline-soft: "#dedede"
  canvas: "#fffdfc"
  canvas-dark: "#121212"
  surface-soft: "#f8f3ec"
  surface-card: "#f0eee3"
  surface-dark: "#232323"
  surface-stone: "#c4beb4"
  on-primary: "#fffdfc"
  on-dark: "#fffdfc"
  warm-taupe: "#cdc3b5"
  warm-stone: "#c9c5bf"
  accent-gold: "#ffd45d"
  teal-dark: "#364748"
  steel-blue: "#809cb3"
  neutral-mid: "#5f6062"
  neutral-cool: "#c0c2c6"
  neutral-warm: "#cccbc9"
  star-rating: "#ffd45d"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Sofia Pro', 'DM Sans', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Sofia Pro', 'DM Sans', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "'Sofia Pro', 'DM Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Sofia Pro', 'DM Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Sofia Pro', 'DM Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Sofia Pro', 'DM Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Sofia Pro', 'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Sofia Pro', 'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Sofia Pro', 'DM Sans', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.25px
  badge:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 52px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 52px
    border: 1px solid {colors.on-dark}
  button-secondary-on-light:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 52px
    border: 1px solid {colors.ink}
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 48px
    height: 56px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  text-input-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.muted}
    borderFocus: 1px solid {colors.on-dark}
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.lg}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    height: 56px
    borderBottom: 1px solid {colors.surface-dark}
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    imageAspectRatio: 1 / 1
    bodyPadding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
  product-card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  hero-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: button-primary
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 90vh
  hero-lifestyle:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    overlay: "linear-gradient(to right, {colors.scrim}cc, transparent)"
    minHeight: 80vh
  feature-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxl}"
  comparison-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
    gap: "{spacing.xxs}"
  footer:
    backgroundColor: "{colors.teal-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.link}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.lg}"
  newsletter-input:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.muted}
  section-divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.section} 0"
  toast-notification:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    shadow: "0 4px 24px rgba(0,0,0,0.3)"
---

## Components

### Buttons

**`button-primary`** — A squared-off, industrial-feeling button with `{rounded.xs}` corners and Beast's signature orange (#ff5601) fill. Text is set in `{typography.button-lg}` with uppercase tracking, white on orange. Hover darkens to #ff5500 with a near-instantaneous transition; disabled state fades to a pale salmon (#ffab80) with reduced-opacity text. The minimal border-radius echoes the blender's own machined housing lines—no pill shapes, no softness.

**`button-secondary`** — Ghost button with a 1px white border on dark backgrounds, switching to an ink-colored border on light sections via the `button-secondary-on-light` variant. Same squared `{rounded.xs}` radius and uppercase type treatment as primary. Hover fills the interior with white at roughly 10% opacity. Used for secondary actions like "Learn More" or "Watch Video" alongside a primary CTA.

**`button-add-to-cart`** — Full-width variant of the primary button, taller at 56px to anchor the product detail page's buy zone. Same orange fill and uppercase treatment as primary; sits below quantity selectors and variant pickers. On mobile, this button becomes sticky at the viewport bottom with a subtle top shadow for separation from scrolling content.

### Inputs

**`text-input`** — Clean 48px-tall input with a 1px `{colors.hairline}` border that sharpens to `{colors.ink}` on focus. The dark variant (`text-input-dark`) reverses the scheme for newsletter signup and account forms rendered on dark backgrounds, using `{colors.surface-dark}` fill with a muted border. Placeholder text uses `{colors.muted}` at `{typography.body-md}` weight.

**`newsletter-input`** — Transparent-background input designed for the footer's dark teal surface, with a 1px `{colors.muted}` border. Pairs inline with a primary button to form the email capture row. Text and placeholder render in `{typography.body-sm}` white on the teal ground.

### Navigation

**`nav-bar`** — A 64px-tall dark bar (#121212) carrying the Beast wordmark left-aligned and sparse navigation links in `{typography.nav-link}`. Cart icon sits right-aligned with an orange dot badge for item count. On scroll, the bar compresses to 56px (`nav-bar-scrolled`) with a subtle bottom border of `{colors.surface-dark}` for visual separation from hero content beneath.

**`announcement-bar`** — A 40px strip of solid orange (#ff5601) pinned above the nav, displaying promotional copy in white `{typography.caption}`. Dismissible with an × icon; typically used for free-shipping thresholds or limited-time bundle offers. The bar's full-orange treatment ensures it reads as a deliberate brand moment rather than a generic Shopify banner.

### Product Display

**`product-card`** — Warm cream (`{colors.surface-card}`, #f0eee3) card with `{rounded.sm}` corners. A square 1:1 product image fills the top half edge-to-edge, followed by `{spacing.base}` padded body containing the product name in `{typography.title-sm}`, a one-line descriptor in `{typography.body-sm}`, and price in `{typography.price-display}`. Hover lifts the card with a subtle shadow and slight upward translate. The dark variant (`product-card-dark`) reverses onto `{colors.surface-dark}` for sections built on the charred canvas.

**`comparison-badge`** — Small orange badge using `{typography.badge}` uppercase text at 11px, positioned on product cards or comparison table headers to flag "Best Seller" or "Most Popular." Uses `{rounded.xs}` to stay consistent with the brand's squared-edge language rather than the pill badges most DTC sites default to.

**`star-rating`** — Five gold (#ffd45d) star icons at 16px with `{spacing.xxs}` gaps between them. Partially filled stars use a clip-path gradient fill. Pairs with a review count in `{typography.caption}` immediately to the right, rendered in `{colors.muted}` on light backgrounds or `{colors.warm-stone}` on dark.

### Hero Sections

**`hero-dark`** — Full-viewport dark panel (#121212) with centered or left-aligned copy. Heading in `{typography.display-xl}` at 56px, supporting body text in `{typography.body-md}`, and a primary orange CTA button. Background typically carries a looping video of the blender in action or a high-contrast product still against pure darkness. Generous `{spacing.section}` padding separates the hero from subsequent content blocks, and a subtle scroll indicator sits at the bottom center.

**`hero-lifestyle`** — Photo-driven hero with a gradient scrim overlay fading from opaque black on the text side to transparent over the imagery. Heading scales to `{typography.display-lg}` (40px) with body text in `{typography.body-md}`. Used for recipe and lifestyle content pages where the photography needs to breathe without sacrificing text legibility.

### Content Blocks

**`feature-callout`** — Warm cream (`{colors.surface-soft}`, #f8f3ec) panel with `{rounded.sm}` corners and generous `{spacing.xxl}` internal padding. Heading in `{typography.display-md}`, body in `{typography.body-md}`, often paired with a product cutaway rendering or icon row illustrating blender specs. Used to communicate motor power, blade material, jar capacity, or health benefit claims in a structured, scannable format.

**`section-divider`** — A 1px `{colors.hairline-soft}` horizontal rule with `{spacing.section}` vertical margin on each side, used to separate content blocks on light backgrounds. On dark sections, this element is either omitted entirely or replaced by a shift in background tone from `{colors.canvas-dark}` to `{colors.surface-dark}`.

### Footer

**`footer`** — Dark teal (#364748) footer providing a cooler counterweight to the warm tones above. Four-column layout on desktop: brand story column with a condensed mission statement, shop links, support links, and newsletter signup with the `newsletter-input` component. Column headings in `{typography.title-sm}`, links in `{typography.link}`. Below the columns sits a full-width divider, then a copyright bar with social icons and payment method badges.

### Feedback

**`toast-notification`** — Dark surface card (#232323) that slides up from the bottom-right on desktop and bottom-center on mobile. White text in `{typography.body-sm}` with `{rounded.sm}` corners and a pronounced 24px-blur drop shadow. Used for add-to-cart confirmations, form submission feedback, and out-of-stock alerts. Auto-dismisses after four seconds with a fade-out transition.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero headline drops to `{typography.display-md}` (32px); nav collapses to hamburger + cart icon; product cards stack vertically at full width; add-to-cart button becomes sticky at viewport bottom; announcement bar text truncates with ellipsis; footer columns stack to single-column accordion |
| Tablet | 744–1128px | Two-column product grid; hero headline uses `{typography.display-lg}` (40px); nav shows condensed link set with hamburger for overflow; feature callouts shift to side-by-side image + text layout; footer columns compress to 2×2 grid |
| Desktop | 1128–1440px | Three-column product grid; full nav link set visible; hero at full `{typography.display-xl}` (56px); feature callouts use 60/40 image-text split; comparison tables display all columns without horizontal scroll |
| Wide | > 1440px | Content max-width capped at 1440px and centered; additional horizontal padding at `{spacing.xxl}`; product grid may expand to four columns on collection pages; hero imagery extends full-bleed behind the centered content container |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch target on mobile, even when visually smaller
- Cart and hamburger icons in the mobile nav use 48×48px tap areas with invisible padding extensions
- Product card tap target covers the entire card surface, not just the image or title text
- Star ratings in review summaries are display-only on mobile; tapping opens a review filter sheet rather than targeting individual stars

### Collapsing Strategy
- Navigation links collapse into a full-screen dark overlay matching `{colors.canvas-dark}` at the mobile breakpoint, with large `{typography.title-lg}` link text and `{spacing.lg}` vertical rhythm between items
- Footer columns collapse to a single-column accordion with `{typography.title-sm}` headers that toggle open/closed; the newsletter section remains always visible at the bottom of the stack
- Product comparison tables switch from a multi-column layout to a horizontally scrollable card carousel below 744px, with peek-through partial cards indicating scroll affordance
- Feature callout blocks shift from side-by-side to stacked layout, with the image appearing above the text block at full width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was detected; the dark nav (#121212) is assumed but not confirmed as the intended browser chrome color
- Exact font weights for Sofia Pro could not be verified from static extraction — weights 600 and 700 are inferred from typical DTC heading usage and may differ from the live theme's CSS custom properties
- Hover and focus transition durations (likely 150–250ms ease-out) were not extracted and should be confirmed from the live stylesheet or Shopify theme settings
- Form validation states (error red, success green) were not present in the extracted palette; these likely exist as Shopify theme CSS variables but could not be captured
- The steel-blue (#809cb3) appeared in extraction but its specific application is unclear — possibly used in informational UI, tooltip backgrounds, or a secondary link state not encountered during color sampling
- Mobile sticky add-to-cart shadow treatment and backdrop blur values could not be confirmed from static extraction
- Icon set style (custom SVG sprite, inline SVGs, or icon font), stroke weight, and sizing conventions are unknown
- Exact content max-width breakpoint is inferred as 1440px from layout patterns but was not confirmed from the theme's CSS
- Video autoplay behavior in hero sections (muted, loop, poster frame) could not be characterized from color/font extraction alone
