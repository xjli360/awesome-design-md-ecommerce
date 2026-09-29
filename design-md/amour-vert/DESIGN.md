---
version: alpha
name: "Amour Vert"
source_url: "https://amourvert.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every garment carries a swing tag that functions as a tree-planting receipt — the founding gesture that quietly governs the entire visual system. The palette leans into the deep end of a forest at dusk: the primary tonal anchor is a submerged teal-green (#004a59), a color that reads simultaneously as canopy shadow and ocean depth, held against a white canvas that lets textured fabric photography carry the atmospheric weight. Charcoal ink (#32373c) replaces true black throughout, softening the contrast curve and keeping the brand register literary rather than corporate. A muted sage (#67a671) enters as a secondary signal for ecological messaging — planted-tree counters, fiber-origin callouts — where it reads as foliage rather than logo. Warm cream (#fafae1) surfaces in editorial blocks and sustainability storytelling panels, adding a hand-pressed paper quality that reinforces slow-fashion positioning. Corners are square or nearly so throughout (`{rounded.none}` on all primary interactive elements), a restrained choice that communicates material confidence over packaging theater. Buttons are sentence-case, never all-caps, and carry no gradient or shadow elevation. Spacing is generous: product grids breathe at 24–32px gutters, hero blocks push to `{spacing.section}` top and bottom, and the announcement bar above the nav compresses to a single teal strip (#004a59) carrying tree-planting milestones in small uppercase. The tree counter itself — a modest teal block in footer and PDP — is the brand's single most persistent conversion signal, implying that every purchase directly funds the ecological offset visible on the tag. Typography leans serif at display scale (modest weight, wide leading, negative tracking) with a clean humanist sans-serif for body and UI; no bold slabs, no condensed headline styles. Motion is absent as a deliberate choice — hover states swap images via a direct cross-fade, and CTA states shift color without translate or scale.

colors:
  primary: "#004a59"
  primary-active: "#003540"
  primary-disabled: "#80a4ac"
  ink: "#32373c"
  body: "#444444"
  muted: "#6b7280"
  hairline: "#d9d9d9"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-warm: "#fafae1"
  on-primary: "#ffffff"
  sage: "#67a671"
  sage-light: "#7bdcb5"
  near-black: "#313131"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.03em
  label-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  footer-heading:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.1em
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
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    height: 36px
    paddingX: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    gap: "{spacing.md}"
  product-card-title:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-badge:
    typography: "{typography.label-sm}"
    backgroundColor: "{colors.sage}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    paddingY: "{spacing.section}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    imageOverlayScrim: "rgba(0,0,0,0.15)"
  sustainability-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.sage}"
    padding: 4px 12px
  tree-counter:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  collection-filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    borderColorActive: "{colors.primary}"
    backgroundColorActive: "{colors.canvas}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.ink}"
    height: 40px
    width: 40px
  editorial-panel:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.footer-heading}"
    paddingY: "{spacing.xxl}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px

## Components

### Buttons

**`button-primary`** — Square-cornered (`{rounded.none}`) fill button in deep teal (#004a59) with white text rendered at `{typography.button-md}` (14px/500 weight, sentence-case). On hover, the fill shifts to `{colors.primary-active}` (#003540) with no transform or shadow; the brand refuses kinetic decoration. Disabled state uses `{colors.primary-disabled}` (#80a4ac) — a blue-green desaturated tint — to preserve brand hue even in unavailable states rather than collapsing to neutral gray.

**`button-secondary`** — Identical geometry (square corners, 48px height) with a 1px `{colors.ink}` border and white fill. Hover background shifts to `{colors.surface-soft}`. Used alongside primary on PDPs for secondary actions like "Add to Wishlist" and "Find in Store."

**`button-ghost`** — Transparent background, underlined `{colors.ink}` text at `{typography.button-md}`. No border, no padding box. Reserved for dismissals, "Read more" expansions, and secondary navigation text links within editorial content.

### Navigation

**`nav-bar`** — White canvas with a single 1px `{colors.hairline}` bottom border. 64px tall, with the wordmark positioned left or centered and utility icons (account, search, cart) right-aligned. Nav links at `{typography.nav-link}` shift to `{colors.primary}` on hover; no underline appears at rest. Desktop nav expands to a full-width mega-menu on hover, featuring category imagery and editorial subheadings.

**`announcement-bar`** — A 36px single-line strip in `{colors.primary}` sitting above the nav bar. White uppercase `{typography.label-sm}` text carries tree-planting milestones ("We've planted X million trees") or promotional thresholds. Pinned at top on scroll until the nav itself becomes sticky.

### Product Card

**`product-card`** — No border-radius, no shadow, no card border. Images run 3:4 portrait at full card width; on hover a secondary image cross-fades in without any translate or zoom. Title below in `{typography.body-md}` and `{colors.ink}`, price in `{typography.price}`. A sage-green `product-card-badge` with rounded-full pill shape may overlay the top-left corner on new arrivals, certified sustainable items, or sale pieces.

### Hero

**`hero`** — Full-width editorial block with `{spacing.section}` vertical padding. Heading in `{typography.display-xl}` (Georgia serif, 42px, 400 weight) with subtext in `{typography.body-md}` below. Light scenes keep ink text on white canvas; when a dark photographic background is used, a 15%-opacity black scrim ensures legibility. Primary CTA uses `button-primary` at the close of the text block.

### Sustainability Badge and Tree Counter

**`sustainability-badge`** — Pill-shaped token with `{colors.surface-warm}` background, `{colors.primary}` text, and a 1px sage border. Used inline on PDPs near fiber-origin messaging ("Certified Organic Cotton", "TENCEL™ Lyocell") and in editorial sustainability pages.

**`tree-counter`** — A compact block in `{colors.primary}` displaying cumulative trees planted, rendered in `{typography.body-sm}` white. Appears in the footer, on PDPs, and occasionally as a sidebar element on collection pages. Functions as a persistent brand-integrity signal rather than a marketing element.

### Editorial Panel

**`editorial-panel`** — A warm cream (`{colors.surface-warm}`) content block with generous `{spacing.xxl}` vertical and `{spacing.xl}` horizontal padding. Heading in `{typography.display-md}` (serif, 28px), body in `{typography.body-md}`. Used for mission statements, sustainability deep-dives, and fiber-origin storytelling between product grids.

### Collection Filter

**`collection-filter-pill`** — Rounded-full pills for size, color, material, and feature facets. Inactive: `{colors.surface-soft}` fill, `{colors.ink}` text. Active: white fill with `1px solid {colors.primary}` border. Text at `{typography.button-sm}`. Scroll horizontally on mobile in a flush-edge overflow container.

### Size Selector

**`size-selector`** — 40×40px square tile with `{rounded.none}`. `{colors.hairline}` border at rest; `{colors.ink}` border when selected. Sold-out tiles render at 50% opacity with a diagonal CSS strike-through line. No radio button styling — tiles are direct touch targets.

### Footer

**`footer`** — Near-black (#313131) background with white body copy at `{typography.body-sm}` and uppercase `{typography.footer-heading}` column labels. Social icons (Font Awesome) in white at 20px. A bottom strip carries legal text and policy links in `{typography.caption}` at reduced opacity. The tree-counter total is repeated here in a small teal block as a closing brand statement.

### Search

**`search-input`** — Square-cornered, `{colors.surface-soft}` background input at full width in the search drawer. Placeholder in `{colors.muted}`, committed text in `{colors.ink}`, typed at `{typography.body-md}`. No search button visible — submission triggered by Enter key or a minimal right-aligned icon.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with slide-in drawer; announcement bar becomes a scrolling ticker; hero heading steps down to `{typography.display-md}`; hero image fills full viewport height; filter pills scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav links visible (up to 5) with hamburger overflow; hero asymmetric: text at 45%, image at 55%; filter drawer replaces pill row |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu nav on hover; hero 50/50 split; editorial panels rendered as two-column text+image |
| Wide | > 1440px | Layout capped at 1440px centered; gutters grow in product grid; hero image extends beyond text container edge; no new breakpoints |

### Touch Targets
- All primary and secondary buttons minimum 48px height
- Nav icon buttons (cart, search, account) padded to 44×44px tap target on mobile
- Size selector tiles minimum 44px on mobile (extended from 40px desktop)
- Collection filter pills minimum 36px height with 8px horizontal gaps
- Announcement bar close/arrow taps minimum 44px

### Collapsing Strategy
- Nav: full link row with mega-menu on desktop → hamburger slide-in drawer at < 744px, accordion sub-navigation inside drawer
- Product grid: 3-column → 2-column at tablet → 1-column at mobile
- Announcement bar: static centered text → auto-scrolling ticker at < 744px
- Footer: 4-column link grid → 2-column at tablet → 1-column stacked accordion at mobile
- Hero: side-by-side split layout → stacked (image above, text below) at < 744px
- Filter UI: pill row → bottom-sheet drawer triggered by a filter button at ≤ tablet

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Web fonts not captured**: only Font Awesome icon fonts and the inherited system stack were detected; the brand's actual display typeface (likely a named serif) and body sans-serif load via deferred JS or a third-party CDN and were not caught. Typography tokens above use system font fallbacks and may not match production.
- **Gutenberg palette bleed**: the majority of extracted hex values (#00d084, #0693e3, #fcb900, #ff6900, #cf2e2e, #7a00df, #fcb900, etc.) match WordPress Gutenberg block editor defaults precisely and are likely editor UI artifacts, not brand-applied colors. Only #004a59, #67a671, #32373c, #313131, #eeeeee, and #fafae1 are treated as potentially brand-intentional; all Gutenberg defaults are excluded from the palette.
- **Primary color confidence**: #004a59 (deep teal) is used as primary based on ecological brand alignment and absence from the Gutenberg standard palette. A CSS custom property or design token audit of the production stylesheet would confirm or revise this choice.
- **Hover and focus ramps**: no explicit hover/focus color tokens were captured; active states are inferred from 15–20% luminance reduction of the primary. Actual interactive state colors may differ.
- **Motion tokens**: no transition durations, easing curves, or animation specs were observable; the brand's zero-animation posture is inferred from visual inspection rather than confirmed from code.
- **Mega-menu structure**: desktop navigation appears to include an editorial mega-menu with imagery columns, but exact column count, image aspect ratios, and hover trigger behavior could not be confirmed.
- **Ecommerce platform**: site does not run on Shopify; the underlying CMS or commerce layer (possibly WooCommerce or a custom stack) was not identified, which may affect how component names map to actual template files.
