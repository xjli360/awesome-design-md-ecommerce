---
version: alpha
name: "Staud"
source_url: "https://staud.clothing"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every call-to-action on staud.clothing glows in amber (#f59e0b) — a single warm voltage inside an editorial shell built almost entirely from near-blacks and off-white. Three near-identical darks (#141414, #1f1f1f, #121212) layer the type hierarchy from display to caption, their contrast delta so compressed that the UI reads as monochromatic from a distance; only the amber CTA and the brand's saturated photography interrupt that grayscale register. The amber at #fbbf24 appears as a secondary hover tone, giving the primary action color a one-step warmth shift rather than a simple darken. Inter, the Swiss-neutral system sans-serif, carries all type: display headers sit at weight 300 with open line-height, uppercase nav labels are set at 500 with measured letter-spacing, and the gap between them is bridged by a tightly controlled scale. No custom typeface is used; letter-spacing and weight alone separate editorial from functional.

  Rounded corners are functionally absent. The design system is architecturally rectilinear — {rounded.none} on all buttons and product cards, reflecting the geometric bag silhouettes that define Staud's physical product language. Inputs accept {rounded.xs} to signal interactability without softening the overall register. The single pill-shaped element is the color swatch ({rounded.full}), which uses circular geometry to mimic the physical object being selected. Product cards follow an equally spare grammar: a 3:4 portrait image, hover-swap to a second shot, product name and price in Inter body-sm below, and 16px dot swatches at the foot of the card. No review stars, no urgency mechanics on standard inventory. When sale or new-arrival badges appear, they run reversed — amber-on-dark or near-black-on-light — with tight uppercase label-uppercase type flush to the image corner, zero border-radius.

  Hero modules for collection launches are full-bleed and text-free: no overlay, no gradient scrim, just image to the viewport edge with headline and CTA sitting below the fold. The footer flips to the near-black surface (#121212), creating a clean bookend — off-white canvas (#f6f6f6) at the top, editorial dark at the bottom — with amber as the single color that crosses both zones. The email-signup module inherits that inverted palette and uses a stacked centered layout: large sans-serif headline, single email input, amber or inverted CTA. The overall design argument is restraint in surface, full investment in product image.

colors:
  primary: "#f59e0b"
  primary-active: "#d97706"
  primary-disabled: "#fcd34d"
  amber-warm: "#fbbf24"
  ink: "#141414"
  body: "#1f1f1f"
  muted: "#545454"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#f6f6f6"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#f6f6f6"

typography:
  display-xl:
    fontFamily: "Inter, sans-serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "Inter, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-uppercase:
    fontFamily: "Inter, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.07em
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  button-inverted:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.body-sm}"
    gap: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
    position: "absolute top-left"
  product-card-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    imageLayout: "full-bleed-above-text"
    ctaSpacing: "{spacing.lg}"
  color-swatch:
    size: 16px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderUnselected: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  size-swatch:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "6px 10px"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.label-uppercase}"
    borderBottom: "1px solid {colors.hairline}"
    height: 48px
  email-signup:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.title-lg}"
    inputBorderColor: "{colors.hairline-soft}"
    padding: "{spacing.xxl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    linkTypography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — Solid amber (#f59e0b) fill, white text, zero border-radius, uppercase Inter 14px/500 with 0.06em letter-spacing. Hover darkens to `{colors.primary-active}` (#d97706); disabled state bleaches to `{colors.primary-disabled}` with `cursor: not-allowed`. Height is fixed at 48px to give the CTA consistent visual weight across product, cart, and checkout surfaces.

**`button-secondary`** — Transparent fill with a 1px solid `{colors.ink}` border and ink-colored uppercase text. On hover, the fill inverts to near-black with `{colors.on-dark}` text — reversing polarity without changing border geometry. Used for secondary CTAs like "Add to Wishlist" or "View More" when a primary amber CTA is also present.

**`button-ghost`** — Transparent, no border, underlined uppercase text in `{colors.ink}`. Reserved for tertiary actions (Size Guide links, editorial navigation anchors) where a bordered button would add visual noise to an already sparse layout.

**`button-inverted`** — Near-black (`{colors.surface-dark}`) fill with `{colors.on-dark}` off-white text. Appears within footer and email-signup sections to maintain contrast hierarchy inside inverted modules without switching back to the amber primary register.

### Text Input
**`text-input`** — White fill with a 1px `{colors.hairline}` border sharpening to 1px `{colors.ink}` on focus. `{rounded.xs}` (2px) is the sole curvature in the input system — just enough to distinguish the field from a raw div without softening the rectilinear register. Fixed at 48px height to align flush with adjacent button stacks in inline email capture layouts.

### Navigation
**`nav-bar`** — Off-white canvas (#f6f6f6) background at 64px height, separated from page content by a single hairline rule. All labels run in `{typography.nav-link}`: Inter 13px/500/0.07em letter-spacing/uppercase — compact enough to fit eight categories horizontally at 1280px without crowding. On mega-menu open state the bar locks in place and a full-width dropdown panel extends below without border-radius.

**`nav-dropdown`** — Full-width panel dropping below the nav-bar with zero rounding, canvas background, and a bottom hairline border. Category links are `{typography.body-sm}` weight 400; column headers use `{typography.label-uppercase}`. A featured editorial image occupies the rightmost column for high-priority categories such as Bags and Swim.

### Product Card
**`product-card`** — Strict 3:4 portrait image with zero rounding; on hover the image crossfades to an alternate shot with no scale transform. Below the image: product name left-aligned in `{typography.body-sm}` and price right-aligned in the same scale, both in `{colors.ink}`. Color swatches appear on hover as a row of `color-swatch` dots. No star ratings are shown in the grid view.

**`product-card-badge`** — Near-black chip absolutely positioned at the top-left image corner, `{typography.label-uppercase}` reversed to `{colors.on-dark}`, zero border-radius. Sale variants swap the fill to `{colors.primary}` amber. Both variants use identical zero-radius geometry that reinforces the rectilinear card frame.

### Swatches
**`color-swatch`** — 16px diameter filled circle at `{rounded.full}`. Unselected: 1px `{colors.hairline}` border. Selected: 2px `{colors.ink}` border with no scale change. Circular geometry is the design system's only pill shape — it exists to index the physical color chip, not for decorative softness.

**`size-swatch`** — Rectangular text chip at `{rounded.none}`, 1px border defaulting to `{colors.hairline}` and switching to `{colors.ink}` when selected. Out-of-stock sizes render with a diagonal CSS strikethrough over the chip. `{typography.caption}` at 12px keeps the size grid compact across full size runs.

### Hero
**`hero-editorial`** — Full-bleed image above a text block with no overlay, no scrim, no text-on-image. The headline (`{typography.display-xl}`, weight 300) sits below the image, followed by a subhead in `{typography.body-md}` and a `button-primary` CTA. This below-image layout keeps brand photography completely unobstructed and is used on all major collection launch heroes.

### Filters
**`filter-bar`** — 48px horizontal bar with `{typography.label-uppercase}` filter chips for category, size, color, and price. A 1px bottom hairline separates it from the product grid. Active filters display an inline "×" dismiss control. On mobile the entire bar collapses into a single "Filter + Sort" modal trigger.

### Email Signup
**`email-signup`** — Inverted dark module (`{colors.surface-dark}` background, `{colors.on-dark}` text) with centered layout: `{typography.title-lg}` headline, single `text-input` email field, and a `button-inverted` CTA. Used as the above-footer module and as a mid-collection interstitial.

### Footer
**`footer`** — Full-width near-black panel with a four-column link grid at desktop. Column headers in `{typography.label-uppercase}` on dark; links in `{typography.caption}`. Social icons are inline SVG at 20px with no fill background. The Staud wordmark sits bottom-left in `{colors.on-dark}` at a reduced optical scale.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger + wordmark + bag icon; hero image stacks full-width above text block with display-xl reduced to ~28px; filter-bar becomes modal trigger; footer collapses to single-column accordion |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows wordmark + condensed horizontal links + bag icon; filter-bar scrolls horizontally; hero layout maintained |
| Desktop | 1128–1440px | Three- or four-column product grid; full mega-menu nav-bar at 64px; hero at full display-xl 52px; footer four-column layout |
| Wide | > 1440px | Max-width container ~1400px centered with generous outer gutters; product grid stays at four columns; hero image can bleed beyond the text container to viewport edge |

### Touch Targets
- All interactive elements minimum 44×44px on touch viewports
- Color swatches scale from 16px to 24px diameter on mobile for hit-area compliance
- Size swatch chips minimum 44px wide × 36px tall on mobile
- Nav hamburger icon touch target 44×44px regardless of glyph size
- Full product card area is tappable, not only the text metadata below the image

### Collapsing Strategy
- Nav: full horizontal link row → hamburger drawer with stacked links, account, and search
- Product grid: 4 col → 3 col → 2 col → 1 col across breakpoints
- Filter bar: horizontal chip row → full-screen "Filter + Sort" modal at < 744px
- Footer: 4-column link grid → single-column accordion with expand/collapse per section
- Hero headline: display-xl 52px → ~28px on mobile; CTA button stretches to full width
- Mega-menu: full-width desktop panel → full-screen drawer on mobile with back-navigation per category level

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No `meta theme-color` extracted; mobile browser chrome tint color unconfirmed — likely `#f6f6f6` canvas or `#141414` ink
- `surface-card: "#ffffff"` is inferred — white was filtered as a Shopify framework default and did not appear in the extracted palette
- Font extraction returned only Inter/sans-serif; Staud may load a secondary editorial typeface (possibly a serif or custom display cut) for campaign headers via JS — not confirmed from static extraction
- Exact button and input border-radius unconfirmed; `{rounded.none}` inferred from the brand's rectilinear visual language and geometric product silhouettes
- Hover animation durations and easing curves not extractable from static color/font extraction
- Exact product grid gap values and outer page margin widths not captured
- Dark-mode or theme-toggle support unknown; `surface-dark` tokens (#121212) appear only in footer/email sections and are not confirmed as a full system-level color scheme
