---
version: alpha
name: "Nuclear Blast"
source_url: "https://www.nuclearblast.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A heavy metal record label and online shop that wears its darkness as a design principle, not a mood. The near-black canvas of `#020203` — a void just off pure black — serves as the foundational color, making every album cover, band photo, and merchandise mockup float like a stage-lit performance. Against this abyss, the brand's primary red `#de2a2a` strikes with the force of a downstroke: it powers the cart icon, the "Add to Cart" button, and the sale badges that punctuate product grids. The palette is deliberately restrained — `#121212` for secondary surfaces, `#f0f0f0` for body text on dark backgrounds, and `#dedede` for muted copy — so that the real color comes from the artists' artwork. Typography defaults to Arial and Helvetica at modest sizes, never competing with the visual noise of metal album art. The shop runs on Shopify, which means checkout flows inherit a separate color system (the extracted `#1f77b4`, `#ff7f0e`, `#2ca02c` are Shopify Pay and third-party payment widgets, not brand choices). Navigation is a fixed top bar with genre dropdowns, a search icon, and a cart badge that glows `{colors.primary}`. Product cards use `{rounded.sm}` corners on thumbnails, but the overall layout is hard-edged and utilitarian — this is a store built for browsing band merch, not for aesthetic browsing.

colors:
  primary: "#de2a2a"
  primary-active: "#b82222"
  primary-disabled: "#7a1515"
  ink: "#f0f0f0"
  body: "#dedede"
  muted: "#8c8c8c"
  muted-soft: "#6b6b6b"
  hairline: "#333333"
  hairline-soft: "#2a2a2a"
  canvas: "#020203"
  surface-soft: "#121212"
  surface-card: "#1a1a1a"
  on-primary: "#ffffff"
  accent-gold: "#ffbb78"
  badge-sale: "#de2a2a"
  badge-new: "#413389"
  badge-soldout: "#7f7f7f"
  star-rating: "#ffbb78"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-bar-sticky:
    borderBottom: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 40px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-thumbnail:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-soldout:
    backgroundColor: "{colors.badge-soldout}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  cart-icon:
    color: "{colors.primary}"
    height: 24px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
  genre-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the shop. Uses the brand's signature red `#de2a2a` with white uppercase text. Square corners (`{rounded.none}`) reinforce the utilitarian, no-frills aesthetic of a metal merch store. On hover, shifts to `{colors.primary-active}` (`#b82222`). Disabled state uses `{colors.primary-disabled}` (`#7a1515`) with reduced opacity.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Continue Shopping". Transparent background with a `{colors.hairline}` border and `{colors.body}` text. Active state fills with `{colors.surface-soft}` (`#121212`). No border-radius — consistent with the brand's hard-edged approach.

### Cards
**`product-card`** — The core product display unit. A dark canvas (`{colors.canvas}`) container with no border or shadow — the album art or product image does all the visual work. The thumbnail gets `{rounded.sm}` (`4px`) to soften the image edges slightly, but the card itself remains square. Title uses `{typography.title-sm}` in `{colors.ink}`, price in `{colors.body}`. Badges overlay the top-left corner of the thumbnail.

### Badges
**`badge-sale`** — A red `{colors.badge-sale}` (`#de2a2a`) strip with white uppercase text. Square corners, tight padding. Used to flag discounted items. **`badge-new`** uses the purple `{colors.badge-new}` (`#413389`) for new arrivals. **`badge-soldout`** uses `{colors.badge-soldout}` (`#7f7f7f`) for out-of-stock items. All badges share the same `{typography.badge}` style — 10px, bold, uppercase, tight tracking.

### Navigation
**`nav-bar`** — Fixed top bar at 60px height. Background is `{colors.canvas}` (`#020203`), links in `{colors.body}` (`#dedede`). Navigation links use `{typography.nav-link}` — 13px, semibold, uppercase with 0.5px letter spacing. On scroll, gets a `{colors.hairline}` bottom border. The cart icon sits on the right, rendered in `{colors.primary}`.

### Forms
**`text-input`** — Standard form input for search, checkout fields, and newsletter signup. Uses `{colors.surface-card}` (`#1a1a1a`) background with `{colors.hairline}` border. On focus, the border switches to `{colors.primary}` (`#de2a2a`). No border-radius, 44px height for comfortable touch interaction.

### Footer
**`footer`** — Full-width dark footer matching the canvas color. Links in `{colors.muted}` (`#8c8c8c`) with `{typography.link}` styling. A `{colors.hairline}` top border separates it from the main content. Contains genre links, customer service links, and social media icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items per row). Nav collapses to hamburger menu. Search bar moves to a full-screen overlay. Footer stacks vertically. |
| Tablet | 744–1128px | Two-column product grid. Nav shows genre dropdowns inline. Search bar remains in nav. Footer uses 2-column layout. |
| Desktop | 1128–1440px | Three-column product grid. Full nav with all genre links visible. Search bar in nav. Footer uses 3-column layout. |
| Wide | > 1440px | Four-column product grid. Max-width container at 1440px. Nav remains full. |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility.
- Cart icon has 44x44px tap area.
- Genre dropdowns have 44px minimum tap targets.
- Product card thumbnails are linked with minimum 48px tap area.

### Collapsing Strategy
- Genre dropdowns collapse into a single "Shop" menu on mobile.
- Product filters collapse into a slide-out drawer on mobile.
- Footer links collapse into accordion sections on mobile.
- Search bar collapses to an icon on mobile, expanding to full-screen overlay on tap.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site. The `primary-active` and `primary-disabled` values are estimated based on typical darkening patterns.
- Error styling for form inputs (validation states, error messages) was not observed.
- The extracted color list includes several colors (`#1f77b4`, `#ff7f0e`, `#2ca02c`, `#d62728`, `#9467bd`, `#e377c2`, `#7f7f7f`, `#bcbd22`, `#17becf`, `#ffbb78`, `#98df8a`, `#ff9896`) that appear to be Shopify Pay, Klarna, Afterpay, and social media icon colors — these are NOT brand colors and should not be used in the design system. The brand's true palette is the dark monochrome range plus the distinctive red `#de2a2a`.
- Font-family extraction returned only Arial and Helvetica. The brand may use a custom font for headers or logos that is loaded via JavaScript or CSS `@font-face` not captured in the extraction.
- Dark mode is not applicable — the brand already uses a dark canvas as its default.
- Sub-brand or label-specific color palettes (e.g., Nuclear Blast America, Nuclear Blast Europe) were not observed.
- Loading states, skeleton screens, and empty states were not captured.
- Animation durations, easing curves, and transition properties were not extracted.
