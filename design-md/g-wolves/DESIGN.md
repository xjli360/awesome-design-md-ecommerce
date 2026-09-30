---
version: alpha
name: "G-Wolves"
source_url: "https://www.g-wolves.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-performance gaming-mouse brand that builds its entire visual identity around the dark, matte chassis of its own hardware — #282828 is the anchor, a deep charcoal that reads as anodized aluminum or textured ABS plastic, not a background. The brand uses #dedede (a warm silver-gray) for body copy and secondary text, creating a low-contrast, almost monochromatic reading experience that prioritizes the product photography of lightweight honeycomb shells and custom PCB layouts over typographic hierarchy. The third extracted color, #121212, is a near-black reserved for the footer, mega-menu backgrounds, and heavy structural containers — it pushes the canvas into true darkness, making the product shots of white and pastel-colored mice glow. The type system runs Epilogue at display sizes (a geometric sans with sharp, squared-off terminals that echo the angular cutouts of the Hati and Skoll series) and Instrument Sans for body and UI (a more neutral, slightly warmer companion). Buttons are pill-shaped but not soft — the {rounded.full} on CTAs reads as a deliberate industrial detail, like a machined aluminum switch cap. There are no gradients, no decorative flourishes, no hero illustrations: the brand trusts the raw engineering of its mice — screw placements, paracord cables, PTFE feet — as the only ornament. The Shopify checkout button (#282828 on #dedede) and the product-card grid (white on #282828) invert the palette depending on context, but the core tension is always the same: a dark, dense frame around a precise, illuminated object.

colors:
  primary: "#282828"
  primary-active: "#1a1a1a"
  primary-disabled: "#4a4a4a"
  ink: "#121212"
  body: "#dedede"
  muted: "#9e9e9e"
  muted-soft: "#b0b0b0"
  hairline: "#3a3a3a"
  hairline-soft: "#2e2e2e"
  canvas: "#121212"
  surface-soft: "#1e1e1e"
  surface-card: "#282828"
  on-primary: "#dedede"
  on-dark: "#dedede"
  accent: "#dedede"
  badge-new: "#dedede"
  badge-sale: "#dedede"
  star-rating: "#dedede"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Epilogue', 'Instrument Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
  button-pill-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  icon-button-outline:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.body}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.body}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.body}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.link}"
  mega-menu:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  dropdown-trigger:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  dropdown-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
  dropdown-item:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "8px 12px"
    rounded: "{rounded.xs}"
  dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "8px 12px"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.body}"
  text-input-error:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid #e53935"
  select-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
    border: "1px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
  radio:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
    border: "1px solid {colors.hairline}"
  radio-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-thumb:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.body}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.body}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.base}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 36px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  accordion:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.body}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  notification-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 4px"
  loading-spinner:
    color: "{colors.body}"
    size: 24px
  skeleton-loading:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    height: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a dark pill on the dark canvas. Uses `{colors.primary}` (#282828) background with `{colors.on-primary}` (#dedede) text. On hover, the background deepens to `{colors.primary-active}` (#1a1a1a). The disabled state uses `{colors.primary-disabled}` (#4a4a4a) with `{colors.muted}` (#9e9e9e) text. The pill shape (`{rounded.full}`) is a deliberate industrial design cue, echoing the machined feel of the mouse hardware. **`button-secondary`** — An outlined variant with `{colors.surface-card}` background and a `{colors.hairline}` border. Used for secondary actions like "View Details" or "Compare". **`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Cancel" or "Clear filters". **`button-pill-dark`** — A smaller pill button with `{colors.ink}` (#121212) background, used for filter tags and category pills.

### Cards
**`product-card`** — The core product display unit. A `{colors.surface-card}` (#282828) background with `{rounded.md}` (12px) corners. The product image sits in a `{rounded.sm}` container with `{colors.surface-soft}` background. The title uses `{typography.title-sm}` and the price uses `{typography.body-sm}` in `{colors.muted}`. A `{colors.badge-new}` or `{colors.badge-sale}` badge sits in the top-left corner. The card has no shadow — the dark surface against the darker canvas provides enough separation.

### Navigation
**`top-nav`** — A fixed-height (64px) navigation bar on `{colors.canvas}` (#121212) with a subtle `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` (Epilogue, 14px, uppercase, 500 weight) in `{colors.muted}`. The active link switches to `{colors.body}` (#dedede) with a 2px bottom border. **`mega-menu`** — A dropdown panel with `{colors.ink}` background and `{rounded.md}` corners, used for product category navigation. **`search-bar`** — A pill-shaped search input on `{colors.surface-soft}` with a `{colors.hairline}` border. On focus, the border switches to `{colors.body}`.

### Forms
**`text-input`** — Standard text input on `{colors.surface-soft}` with `{rounded.sm}` (8px) corners and a `{colors.hairline}` border. Focus state swaps the border to `{colors.body}`. Error state uses a red border (#e53935). **`select-input`** — Matches the text input styling. **`checkbox`** and **`radio`** — Square and circular inputs respectively, both on `{colors.surface-soft}` with `{colors.hairline}` borders. Checked/selected states fill with `{colors.primary}` and use `{colors.on-primary}` for the indicator. **`toggle`** — A pill-shaped switch with `{colors.hairline}` background and a `{colors.canvas}` thumb. Active state fills with `{colors.primary}`.

### Footer
**`footer`** — A large footer section on `{colors.ink}` (#121212) with `{colors.muted}` text. Links use `{typography.link}` and hover to `{colors.body}`. The footer is divided into columns with `{spacing.xxl}` padding.

### Hero
**`hero-section`** — A full-width section on `{colors.canvas}` with `{spacing.section}` padding. The title uses `{typography.display-xl}` (36px, 700 weight) and the subtitle uses `{typography.body-md}` in `{colors.muted}`. The CTA button (`{colors.primary}` pill) sits below the text.

### Badges & Indicators
**`badge-new`** and **`badge-sale`** — Small uppercase badges on `{colors.badge-new}`/`{colors.badge-sale}` (both #dedede) with `{colors.ink}` text. Used on product cards and category navigation. **`notification-badge`** — A small circular badge on `{colors.primary}` with `{colors.on-primary}` text, used for cart counts. **`star-rating`** — Rendered in `{colors.star-rating}` (#dedede) at 16px.

### Loading & Feedback
**`loading-spinner`** — A simple spinning indicator in `{colors.body}`. **`skeleton-loading`** — Placeholder blocks on `{colors.surface-soft}` with `{rounded.xs}` corners, used while product images or content load. **`tooltip`** — A small dark tooltip on `{colors.ink}` with `{colors.body}` text and `{rounded.xs}` corners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), hamburger menu replaces top nav links, hero section reduces to `{spacing.lg}` padding, search bar collapses to icon-only, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid (2 cards), top nav shows limited links (Shop, Support, Account), hero section uses `{spacing.xl}` padding, search bar remains full but narrower |
| Desktop | 1128–1440px | Three-column product grid (3 cards), full top nav with all links visible, hero section at `{spacing.section}` padding, mega-menu enabled on hover |
| Wide | > 1440px | Four-column product grid (4 cards), max-width container (1440px) centered, hero section at `{spacing.section}` padding with larger display text |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile
- Icon buttons are 36x36px minimum on desktop, 44x44px on mobile
- Dropdown items have 44px minimum height on mobile
- Toggle switches are 44px wide on mobile for easier thumb interaction
- Product card CTAs are 48px tall on mobile

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer for full navigation
- Product grid collapses from 4 columns to 1 column on mobile
- Footer columns collapse to a single column on mobile, with accordion-style expandable sections
- Mega-menu collapses to a simple dropdown on tablet
- Search bar collapses to an icon-only trigger on mobile, expanding to full-width on tap
- Hero section reduces padding and stacks CTA below text on mobile
- Product detail page moves from side-by-side (image + info) to stacked on mobile
- Cart drawer collapses to full-screen overlay on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are limited to three values (#282828, #dedede, #121212) — the brand's true palette may include additional accent colors (e.g., for limited edition mice, software UI, or regional variants) that were not captured in the extraction
- Font-family declarations found (Epilogue, Instrument Sans, sans-serif) but no font weights or specific usage patterns were extracted — the typography block above is an informed reconstruction based on common gaming-brand patterns
- No hover, focus, or active states were extracted for any component — all state variants in the components block are inferred from common design patterns
- Error styling (error text, error borders, validation messages) was not extracted — the error border color (#e53935) is a standard default
- Dark mode is not applicable — the brand already uses a dark canvas (#121212) as its default
- No extracted data for: loading states, skeleton screens, empty states, success messages, or toast notifications
- No extracted data for: sub-brand palettes (e.g., Hati, Skoll, HSK series might have their own color treatments)
- No extracted data for: software companion app UI (G-Wolves software for DPI, polling rate, etc.)
- No extracted data for: promotional banners, sale tags, or limited-edition colorways
- The `meta theme-color` (#282828) matches the primary color, confirming the dark theme is intentional
- Shopify platform detected — checkout button colors may differ from the main site palette (Shopify's default checkout styling may override brand colors)
