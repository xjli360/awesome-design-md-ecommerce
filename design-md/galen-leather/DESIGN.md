---
version: alpha
name: "Galen Leather"
source_url: "https://www.galenleather.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Hand-stitching thread color is selectable at checkout — that granular customization signals everything Galen Leather believes about its customer. Founded in İstanbul, the shop's visual identity anchors on a deep Bosphorus teal (#108474), a color that reads simultaneously as craft-workshop signage and contemporary stationery-brand confidence. Against the near-white (#fafafa) canvas, teal carries all primary CTAs, nav accents, and footer backgrounds with no delegation to the secondary palette. Amber (#ffa303) and warm gold (#fbcd0a) surface at the granular layer — sale badges, star fills, price highlights — without ever rising to brand-primary status. A burnt rust (#c4590c) handles clearance urgency, while lavender (#a89cc8) marks new-arrival callouts, giving the palette a slight unexpected softness that prevents the earth-and-craft reading from feeling predictable.

  Type divides into two clear registers. Baskerville — the only serif on-site — handles product names, section titles, and editorial headers; its roman weight at 36–40px on wide viewports gives the display layer a bookbinder's authority without heavy black. Nunito Sans carries every functional surface: button labels, nav links, form fields, cart totals. The serif-for-content / sans-for-action split is consistent and deliberate. At mobile widths, display type compresses to 24–26px but never trades Baskerville for a sans substitute.

  Geometry is flat-precise: `{rounded.xs}` (4px) on all interactive controls, `{rounded.sm}` (8px) on product cards, hard zero on the nav bar. Spacing inside the product grid is tight — 12px vertical rhythm between thumbnail, title, variant line, and price — while section gutters open to 64px. Photography is boxed at a consistent 1:1 ratio in grid view and bleeds edge-to-edge in the hero, with no overlay scrim on landing imagery. The overall reading is a craft workshop with a disciplined inventory system: confident enough in the product to let leather and paper speak before the interface does.

colors:
  primary: "#108474"
  primary-active: "#0c6b5e"
  primary-disabled: "#c1e6e6"
  accent-amber: "#ffa303"
  accent-gold: "#fbcd0a"
  accent-rust: "#c4590c"
  accent-lavender: "#a89cc8"
  teal-soft: "#edf5f5"
  ink: "#555555"
  body: "#747471"
  muted: "#888888"
  hairline: "#dedede"
  canvas: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  overline:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1:1"
    gap: "{spacing.md}"
    padding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.teal-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    imagePosition: right
    imageWidth: 55%
  badge-handmade:
    backgroundColor: "{colors.teal-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new-arrival:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-clearance:
    backgroundColor: "{colors.accent-rust}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  star-rating:
    starColor: "{colors.accent-gold}"
    emptyStarColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    gap: "{spacing.xs}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    gap: "{spacing.xs}"
  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    buttonSize: 36px
  footer-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    linkColor: "{colors.on-primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The core CTA in deep teal (#108474) with white type at 14px/700 Nunito Sans and 44px height. Used for Add to Cart, Checkout, and Subscribe. The 4px radius (`{rounded.xs}`) signals precision rather than friendliness. On `:active` the fill darkens to #0c6b5e; on `:disabled` it retreats to the extracted light teal (`{colors.primary-disabled}`) with muted gray text and `cursor: not-allowed`.

**`button-secondary`** — Transparent background with a 1.5px teal border and matching teal text; same height and type scale as primary. Used for secondary actions like "View All" or "Add to Wishlist". On hover the interior fills with `{colors.teal-soft}` to confirm interactivity without stealing primary-button weight.

**`button-ghost`** — Transparent, no border, ink-colored Nunito Sans 13px/600. Used for dismiss actions, inline navigation prompts, and tertiary controls where adding a border would over-crowd a surface.

### Inputs

**`text-input`** — 44px height, 4px radius, hairline border (#dedede) at rest that transitions to the primary teal border on focus. Nunito Sans 16px/400 for input text, #888888 placeholder. Labels are static above the field — no floating label animation. Used across search, newsletter signup, and checkout address forms.

### Navigation

**`nav-bar`** — 64px tall on desktop, canvas (#fafafa) background with a 1px hairline border-bottom. Wordmark renders in Baskerville 22px (`{typography.display-sm}`); navigation links in Nunito Sans 14px/600. On scroll, a low-elevation box-shadow replaces the border-bottom without a background color shift. At mobile widths the link row collapses into a right-side drawer toggle; the wordmark remains visible at all breakpoints.

### Product Grid

**`product-card`** — White surface (`{colors.surface-card}`) with 8px radius and 1:1 product image at the top. Title renders in Baskerville 22px/400 (`{typography.display-sm}`), with a variant sub-line in Nunito Sans 14px body-sm and price in Nunito Sans 16px/700 (`{typography.price}`) below. Badges (`badge-handmade`, `badge-sale`, `badge-new-arrival`, `badge-clearance`) stack top-left over the image thumbnail. On hover the image scales to ~103% at 200ms ease; no card shadow is added.

### Hero

**`hero-banner`** — Split layout on desktop: left column contains Baskerville display-xl headline, a body-md subhead, and a `button-primary` CTA against the `{colors.teal-soft}` (#edf5f5) background; the right column holds full-bleed product photography at 55% width with no scrim. On tablet the split compresses to 50/50; on mobile the image stacks above the text column at center alignment.

### Badges

**`badge-handmade`** — Small overline label ("100% HANDMADE") in teal-soft fill (#edf5f5) with primary teal text. Applied to product tiles featuring artisan or limited-run items as a brand-trust signal rather than a promotional label.

**`badge-sale`** — Amber (#ffa303) fill with dark ink text in 10px/700 uppercase overline. Placed top-left over the product image thumbnail on any item with an active discount.

**`badge-new-arrival`** — Lavender (#a89cc8) fill with white text. Applied to items added within the most recent collection window, typically 30 days.

**`badge-clearance`** — Rust (#c4590c) fill with white text. End-of-line and last-chance inventory only; the urgency color is reserved strictly for this context to preserve signal fidelity.

### Ratings

**`star-rating`** — Five-star widget with gold (#fbcd0a) fill for active stars and hairline (#dedede) for empty stars. Review count and score in Nunito Sans 12px/400 (`{typography.caption}`) in muted body color (#747471). Sourced from the Judge.me widget and styled to match the brand palette rather than Judge.me defaults.

### Utility

**`breadcrumb`** — Nunito Sans 12px/400 in muted (#888888) for ancestor links, ink (#555555) for the current page. Chevron separator rendered in hairline color. 4px gap between crumbs. Appears on all collection and product detail pages below the nav bar.

**`quantity-stepper`** — Inline − / quantity / + control inside a surface-soft (#f2f2f2) container with a hairline border and 4px radius. Each button is 36px square; the quantity field itself uses `{typography.body-md}`. Used on both the product detail page and the cart drawer.

### Footer

**`footer-bar`** — Full-width deep teal (#108474) background. Section headings in Nunito Sans 16px/600 (`{typography.title-sm}`) white. Body links and newsletter copy in Nunito Sans 14px/400 (`{typography.body-sm}`) white. Newsletter email input uses a white-background `text-input` variant dropped inside the teal footer with a white `button-primary` override for the subscribe CTA.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero image stacks above text; display-xl compresses to 26px; section padding reduces to 32px; badges stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav retains full links if six items or fewer; hero shifts to 50/50 split with image right |
| Desktop | 1128–1440px | Three- or four-column product grid; full split hero with 55% image column; all nav items visible; 64px section gutters |
| Wide | > 1440px | Max-width container centered at ~1440px; product grid caps at four columns; hero photography expands within the image column only; text column stays fixed width |

### Touch Targets

- All interactive controls (buttons, inputs, steppers, nav links) minimum 44×44px
- Badge tap targets expand via invisible padding to 44px height minimum on mobile
- Star rating widget minimum 44px touch height on product and review surfaces
- Quantity stepper buttons minimum 44×44px on mobile regardless of visual 36px size

### Collapsing Strategy

- Navigation collapses at 744px into a slide-in drawer from the right, retaining full link hierarchy and subnav categories
- Product filters collapse into a bottom-sheet modal on mobile rather than a sidebar panel
- Footer four-column grid collapses to two columns at 744px, single column below 480px
- Hero split layout stacks vertically below 744px with image above the text block and center-aligned CTA

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius for modals, drawers, or overlays — `{rounded.sm}` (8px) assumed based on card radius convention
- Social icon colors (#3b5998 Facebook, #1da1f2 Twitter, #e60023 Pinterest, #0073b1 LinkedIn) are platform-standard and excluded from brand palette; their presence in extraction does not indicate brand use
- Exact Baskerville letter-spacing values at each display scale are not extractable from the live site; values above are typographically reasoned estimates
- No animation or transition timing data available; hover image scale (103%) and 200ms ease are inferred from common Shopify theme patterns, not confirmed
- Product image aspect ratio (1:1) not confirmed from color extraction; assumed from common Shopify grid layout conventions
- Custom icon set details unknown — site likely uses SVG icons bundled with the Shopify theme rather than an icon font; JudgemeIcons and JudgemeStar are review-widget–specific and excluded from the system
- No dark-mode token definitions — site appears light-mode only with no `prefers-color-scheme` variants detected
- Exact nav bar height at tablet breakpoint not confirmed; 64px assumed consistent across desktop and tablet
