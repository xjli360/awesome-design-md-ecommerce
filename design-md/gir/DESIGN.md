---
version: alpha
name: "GIR"
source_url: "https://getgir.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  GIR (Get It Right) is a kitchen-tools brand that speaks in a single, confident voice — a deep, almost charcoal gray (`#313131`) that reads as serious, durable, and quietly premium. There is no bright primary color here; the brand trusts the weight of its ink, the precision of its silicone spatulas, and the honesty of its materials. The entire visual system is monochrome, leaning on a warm off-white canvas and a tight `{spacing.sm}` to `{spacing.lg}` grid that gives every product room to breathe. Typography runs the system font stack — `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `Roboto`, `Helvetica Neue`, `Arial`, `Noto Sans`, `sans-serif` — at modest weights (400 for body, 600 for display), never shouting. Buttons are softly rounded (`{rounded.sm}`), product cards use `{rounded.md}`, and the overall feel is that of a well-edited kitchen drawer: nothing unnecessary, everything in its place. The brand's signature move is the absence of a signature move — no gradients, no badges, no decorative flourishes. GIR's design system is a quiet assertion that good tools don't need to be loud.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#7a7a7a"
  muted-soft: "#a0a0a0"
  hairline: "#d0d0d0"
  hairline-soft: "#e5e5e5"
  canvas: "#f9f9f9"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#2e7d32"
  accent-red: "#c62828"
  badge-new: "#313131"
  badge-sale: "#c62828"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.25px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 6px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
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
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-secondary-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-disabled}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-disabled}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-tertiary-active:
    textColor: "{colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  select:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    typography: "{typography.badge}"
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textDecoration: underline
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.lg} 0"
  badge:
    typography: "{typography.badge}"
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Uses the brand's signature dark gray (`{colors.primary}`) background with white text (`{colors.on-primary}`) and a soft 6px radius (`{rounded.sm}`). On hover, the background deepens to `{colors.primary-active}` (#1a1a1a). When disabled, it fades to `{colors.primary-disabled}` (#a0a0a0) with white text, signaling non-interactivity without changing shape.

**`button-secondary`** — An outlined variant with a white canvas background, dark gray text, and a 2px solid border in `{colors.primary}`. Hover state darkens the border and text to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}` for both border and text. Padding is 11px 23px to account for the border thickness, keeping total height at 48px.

**`button-tertiary`** — A text-only button with no background or border. Uses `{colors.primary}` text and `{typography.button-md}`. Hover state shifts to `{colors.primary-active}`. Padding is 12px 0 for vertical alignment. Used for less prominent actions like "Cancel" or "Learn more."

### Cards
**`product-card`** — The primary container for product listings. White background (`{colors.surface-card}`), 12px radius (`{rounded.md}`), 16px padding, and a subtle `{colors.hairline-soft}` border. On hover, the border strengthens to `{colors.hairline}` and a soft box shadow appears (`0 4px 12px rgba(0,0,0,0.08)`). The product image inside uses a 1:1 aspect ratio and `{rounded.sm}`. Title uses `{typography.title-sm}`, price uses `{typography.body-md}` in `{colors.ink}`. Badges (e.g., "NEW") sit at the top-left of the image area.

### Navigation
**`nav-bar`** — A fixed-height (64px) top bar with white background and a thin bottom border (`{colors.hairline-soft}`). Navigation links use `{typography.nav-link}` — 14px, 500 weight, uppercase with 0.5px letter spacing. Active links show `{colors.primary}` text with a 2px bottom border in the same color. Inactive links use `{colors.muted}`. The bar is sticky on scroll.

### Forms
**`text-input`** — Standard single-line input with white background, 6px radius, 12px 16px padding, and a `{colors.hairline}` border. On focus, the border becomes 2px solid `{colors.primary}`. Error state uses a 2px `{colors.accent-red}` border. Disabled state uses `{colors.surface-soft}` background and `{colors.muted}` text. Height is 48px for touch accessibility.

**`textarea`** — Multi-line input matching the text-input styling but without a fixed height. Uses `{typography.body-md}` and `{rounded.sm}`.

**`select`** — Dropdown selector matching the text-input dimensions (48px height, 6px radius, 12px 16px padding) with a `{colors.hairline}` border. Background is white, text is `{colors.ink}`.

### Search
**`search-bar`** — A pill-shaped (`{rounded.full}`) search input with white background, 12px 20px padding, 48px height, and a `{colors.hairline}` border. On focus, the border becomes 2px solid `{colors.primary}`. Used in the nav bar and on the search results page.

### Footer
**`footer`** — A full-width footer with `{colors.primary}` background and white text. Uses `{typography.body-sm}` for body content and `{typography.link}` for links. Links underline on hover. Padding is `{spacing.xxl}` (48px) vertically and `{spacing.lg}` (24px) horizontally.

### Badges
**`badge`** — Small uppercase label (11px, 600 weight, 0.5px letter spacing) with `{colors.badge-new}` background and white text. 2px 8px padding, 2px radius (`{rounded.xs}`). Used for "NEW" indicators. **`badge-sale`** uses `{colors.badge-sale}` (#c62828) for sale/discount labels.

### Hero
**`hero`** — A full-width section with `{colors.surface-soft}` background, `{typography.display-xl}` heading, and `{spacing.section}` (80px) vertical padding. The call-to-action button (`hero-cta`) is `button-primary` with extra horizontal padding (32px) and `{spacing.lg}` margin above.

### Quantity Selector
**`quantity-selector`** — A compact input (40px height) with white background, 6px radius, 8px 12px padding, and a `{colors.hairline}` border. Uses `{typography.body-md}`. Found on product detail pages for adjusting cart quantities.

### Accordion
**`accordion`** — A vertically stacked disclosure component. Each item has a `{typography.title-sm}` header with `{colors.ink}` text and a bottom border (`{colors.hairline-soft}`). Content area uses `{typography.body-sm}` in `{colors.body}` with `{spacing.sm}` padding. Used for product descriptions, shipping info, and FAQs.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid for product cards (1 column). Nav bar collapses to hamburger menu. Hero padding reduces to 40px vertical. Footer stacks links vertically. Search bar moves into a slide-out drawer. |
| Tablet | 744–1128px | Two-column product grid. Nav bar shows top-level links only (no dropdowns). Hero uses `{typography.display-lg}`. Footer links in two columns. |
| Desktop | 1128–1440px | Three-column product grid. Full nav bar with dropdowns. Hero uses `{typography.display-xl}`. Footer links in four columns. |
| Wide | > 1440px | Max-width container at 1440px, centered. Product grid can expand to four columns. Hero uses larger padding (100px vertical). |

### Touch Targets
- All interactive elements (buttons, inputs, links) have a minimum height of 48px.
- Icon-only buttons (e.g., cart, search) are 44x44px minimum.
- Nav links have 44px tap targets even if text is smaller.
- Quantity selector buttons are 40x40px minimum.

### Collapsing Strategy
- Nav bar: On mobile (< 744px), the full nav collapses into a hamburger menu. The logo and cart icon remain visible.
- Product grid: Drops from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Footer: Links collapse from 4 columns to 2 to 1 as viewport shrinks.
- Hero: Image and text stack vertically on mobile; side-by-side on tablet and above.
- Search: Full search bar in nav on desktop; icon-only on mobile that opens a full-screen overlay.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components (only primary/secondary buttons and product cards have defined hover styles).
- Focus-visible styles (keyboard accessibility outlines) are not extracted.
- Error styling for forms beyond border color (no error message typography or iconography).
- Dark mode or high-contrast mode variants.
- Sub-brand or seasonal color palettes (e.g., holiday collections).
- Animation and transition timing values (e.g., button hover duration, card lift speed).
- Loading and skeleton states for product cards and images.
- Empty state designs (e.g., empty cart, no search results).
- Tooltip and popover styling.
- Rating or review component styling (stars, numeric scores).
- Video player or media gallery component details.
- Print stylesheet considerations.
- Specific Shopify or platform-specific overrides (the site does not appear to be on Shopify).
