---
version: alpha
name: "Pixio"
source_url: "https://www.pixiogaming.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A performance-first gaming monitor brand that communicates through a language of dark, almost-black backgrounds (#222428) and a single, urgent accent: a neon-lime #c8ff00 that appears nowhere else in the extracted palette — not as a primary CTA, but as a voltage spike used sparingly on spec badges, sale flags, and the occasional underline. The brand's true primary is #108474, a deep teal that reads as cool and technical, anchoring the checkout flow and secondary actions while the lime green and a safety-orange #ff4200 handle the high-energy moments. The canvas is a near-black #121212, not pure #000, giving the UI a slight atmospheric depth that prevents eye strain during long sessions. Type is split between a geometric sans (Instrument Sans) for body and UI, and Playfair Display for hero headings — an unusual choice for gaming hardware that signals a tilt toward premium, editorial presentation rather than gamer-argot. Rounded corners are minimal: buttons use {rounded.sm} (8px), cards use {rounded.md} (12px), and only the search bar and avatar hit {rounded.full}. The extracted palette is unusually large (25+ colors), suggesting heavy use of Shopify checkout widgets, social icons, and stock-image dominant tones — the brand's true identity is a tighter set: #121212 canvas, #222428 surface, #108474 primary, #c8ff00 and #ff4200 as dual accents, and a warm #ee9441 for sale badges. The overall feel is that of a dark cockpit: controlled, high-contrast, with every color chosen for legibility under low-light conditions.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#7bbfb0"
  ink: "#121212"
  body: "#222428"
  muted: "#7b7b7b"
  muted-soft: "#9f9f9f"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#121212"
  surface-soft: "#222428"
  surface-card: "#f9fafb"
  on-primary: "#ffffff"
  accent-lime: "#c8ff00"
  accent-orange: "#ff4200"
  accent-amber: "#ee9441"
  badge-red: "#ea222b"
  badge-green: "#3ed660"
  badge-dark-green: "#006400"
  badge-dark-red: "#8b0000"
  star-rating: "#c8ff00"
  sale-flag: "#ee9441"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  price-display:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
    textDecoration: line-through

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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-accent-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-pill-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 1px solid "{colors.hairline-soft}"
  text-input-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    border: 1px solid "{colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    border: 1px solid "{colors.badge-red}"
    rounded: "{rounded.sm}"
  select-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: 1px solid "{colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    borderBottom: 1px solid "{colors.surface-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.accent-lime}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 20px rgba(0,0,0,0.3)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: 16/9
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.on-primary}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    textColor: "{colors.muted-soft}"
  product-card-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 480px
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
    marginTop: "{spacing.base}"
  hero-cta:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  spec-badge-accent:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: 1px solid "{colors.hairline-soft}"
  search-bar-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    border: 1px solid "{colors.primary}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
    borderTop: 1px solid "{colors.surface-soft}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-lime}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
  cart-button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    height: 32px
  badge-new:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.badge-dark-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-in-stock:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  rating-stars:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
    gap: "{spacing.xxs}"
  divider:
    backgroundColor: "{colors.surface-soft}"
    height: 1px
    marginVertical: "{spacing.base}"
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
    marginVertical: "{spacing.base}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
    marginBottom: "{spacing.xl}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  filter-chip-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  pagination-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  pagination-button-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.7
  modal-content:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  modal-close-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: 1px solid "{colors.surface-soft}"
  accordion-header-active:
    backgroundColor: transparent
    textColor: "{colors.accent-lime}"
    borderBottom: 1px solid "{colors.surface-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
    borderBottom: 1px solid "{colors.surface-soft}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.accent-lime}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.accent-lime}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  tab-hover:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    borderBottom: 2px solid "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The primary action button, rendered in deep teal (#108474) on the dark canvas. Used for add-to-cart, checkout progression, and affirmative actions. On hover, shifts to `{colors.primary-active}` (#0d6b5d). Disabled state uses `{colors.primary-disabled}` (#7bbfb0) with reduced contrast. Text is white `{colors.on-primary}`.

**`button-secondary`** — A dark-on-dark alternative, using `{colors.surface-soft}` (#222428) as background. Used for secondary actions like "View Details" or "Compare." On hover, deepens to `{colors.ink}` (#121212). Maintains the same 44px height and `{rounded.sm}` corners as primary.

**`button-accent-lime`** — The high-energy CTA, using `{colors.accent-lime}` (#c8ff00) background with dark text (#121212). Reserved for the most urgent actions: "Shop Now," "Limited Offer," or hero-section CTAs. The lime against the dark canvas creates the brand's signature visual pop.

**`button-accent-orange`** — Safety-orange (#ff4200) variant for clearance, final-sale, or exit-intent actions. White text. Used sparingly to avoid visual noise.

**`button-ghost`** — Transparent background with white text, used for tertiary actions in dense layouts. On hover, gains a `{colors.surface-soft}` background to indicate interactivity.

**`button-pill-lime`** — A smaller, fully rounded (`{rounded.full}`) variant of the lime accent button, used for filter chips, tag actions, and compact CTAs. 36px height, 8px/20px padding.

### Cards
**`product-card`** — The primary product display unit, built on a `{colors.surface-soft}` (#222428) background with `{rounded.md}` (12px) corners. Contains a 16:9 image area with `{rounded.sm}`, title in `{typography.title-sm}`, price in `{typography.price-display}`, and optional sale badge. On hover, gains a subtle drop shadow (0 4px 20px rgba(0,0,0,0.3)) to lift off the canvas. Sale prices use `{typography.price-sale}` with line-through decoration in `{colors.muted-soft}`.

**`product-card-badge`** — Amber (#ee9441) pill for sale flags, positioned top-right on the card image. Uses `{typography.badge}` (12px uppercase, bold) with `{rounded.xs}` (4px). Other badge variants (`badge-new`, `badge-sold-out`, `badge-in-stock`) follow the same shape but swap background colors.

### Navigation
**`nav-bar`** — Fixed top bar at 72px height, using `{colors.canvas}` (#121212) background. Navigation links are uppercase `{typography.nav-link}` (14px, weight 600, 0.3px letter spacing). Active link uses `{colors.accent-lime}`; inactive uses `{colors.muted-soft}` (#9f9f9f). On scroll, gains a 1px bottom border from `{colors.surface-soft}` to visually separate from content.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input at 44px height, using `{colors.surface-soft}` background with a `{colors.hairline-soft}` border. On focus, border shifts to `{colors.primary}` (#108474). Placeholder text in `{colors.muted}` (#7b7b7b).

### Forms
**`text-input`** — Standard text input at 44px height with `{rounded.sm}` corners. Background is `{colors.surface-soft}`, border is 1px `{colors.hairline-soft}`. Focus state swaps border to `{colors.primary}`. Error state uses `{colors.badge-red}` (#ea222b) border. Typography is `{typography.body-md}` (16px).

**`select-input`** — Matches text-input dimensions and styling, with a custom dropdown arrow in `{colors.muted-soft}`.

**`quantity-selector`** — A compact 40px height input for cart quantities, with `{rounded.sm}` corners and `{colors.surface-soft}` background. Increment/decrement buttons are transparent with `{rounded.xs}`.

### Badges & Tags
**`spec-badge`** — Small rectangular tags (4px/10px padding) for displaying monitor specifications (resolution, refresh rate, panel type). Default uses `{colors.surface-soft}` background with `{colors.on-primary}` text. Accent variant uses `{colors.accent-lime}` background with `{colors.ink}` text for highlighted specs.

**`filter-chip`** — Pill-shaped (`{rounded.full}`) filter toggles at 32px height. Default state uses `{colors.surface-soft}` background. Active state uses `{colors.primary}`. Hover state uses `{colors.ink}`.

### Footer
**`footer`** — Full-width footer at `{colors.canvas}` background, separated from content by a 1px `{colors.surface-soft}` top border. Links use `{typography.link}` (14px, weight 500) in `{colors.muted-soft}`. On hover, links shift to `{colors.accent-lime}`. Section headings use `{typography.title-sm}` in `{colors.on-primary}` with `{spacing.base}` bottom margin.

### Modal
**`modal-overlay`** — Full-screen scrim at 70% opacity black (#000000). `modal-content` uses `{colors.surface-soft}` background with `{rounded.md}` (12px) corners and `{spacing.xl}` (32px) padding. Close button is a 32px circle with `{rounded.full}`, transparent by default, gaining `{colors.ink}` background on hover.

### Tabs & Accordion
**`tab-bar`** — Horizontal tab strip with `{colors.canvas}` background and 1px `{colors.surface-soft}` bottom border. Active tab uses `{colors.accent-lime}` text with a 2px lime underline. Inactive tabs use `{colors.muted-soft}`. Hover state shows white text with a `{colors.muted-soft}` underline.

**`accordion-header`** — Clickable header row with `{colors.on-primary}` text and a `{colors.surface-soft}` bottom border. Active state shifts text to `{colors.accent-lime}`. Content area uses `{typography.body-sm}` in `{colors.muted-soft}` with `{spacing.sm}` top padding and `{spacing.base}` bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu. Product cards go single-column. Hero section reduces to 320px min-height with 32px padding. Filter chips wrap to two rows. Footer stacks vertically. Search bar reduces to icon-only. |
| Tablet | 744–1128px | Nav-bar shows condensed links (no labels, only icons). Product cards display in 2-column grid. Hero section maintains 400px min-height. Filter chips show in a horizontal scrollable strip. Footer shows 2-column layout. |
| Desktop | 1128–1440px | Full nav-bar with uppercase labels. Product cards in 3-column grid. Hero section at 480px min-height with full display-xl typography. Filter chips in a wrap layout. Footer shows 3-column layout. |
| Wide | > 1440px | Max-width container at 1440px, centered. Product cards in 4-column grid. Hero section may show additional content (specs strip, secondary CTA). Footer shows 4-column layout. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility.
- Filter chips and spec badges are 32px minimum — acceptable for desktop but may need 40px on mobile.
- Icon-only buttons (cart, search, menu) use 44px x 44px touch targets.
- Quantity selector buttons are 32px — consider increasing to 40px on mobile.

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px.
- Product card grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows.
- Filter chip strip becomes horizontally scrollable on tablet and mobile.
- Footer columns collapse: 4 → 3 → 2 → 1.
- Hero section reduces padding and font size on mobile (display-xl drops to 32px).
- Search bar collapses to icon-only on mobile, expanding to full input on tap.
- Tab labels may truncate or show only icons on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font-family declarations extracted as obfuscated identifiers (Font-1767735084823, etc.). Actual font names inferred from "Instrument Sans" and "Playfair Display" found in the list — these may be the brand's true fonts, but the obfuscated names suggest a font-loading system (possibly Shopify Fonts or a custom loader). The exact font stack for each weight is uncertain.
- Hover and active states for most components are inferred from common patterns, not extracted from the live site. The extracted palette includes many colors that may be hover states (e.g., #006400, #8b0000) but their exact usage is unknown.
- Error states for forms (text-input-error) are assumed to use #ea222b based on its presence in the palette, but the actual error styling (icon, message placement, animation) is not confirmed.
- Dark mode is the default (canvas is #121212), but there may be a light mode variant that wasn't extracted. The presence of #f9fafb and #f9f9f9 in the palette suggests light surfaces exist somewhere (possibly checkout or admin).
- The extracted palette is unusually large (25+ colors), indicating heavy contamination from Shopify widgets, social icons, and stock images. The brand's true palette is likely smaller — the colors selected as primary, accents, and badges are best guesses based on frequency and distinctiveness.
- Checkout flow styling is not extracted — Shopify's default checkout may override brand colors.
- Animation durations, easing curves, and transition properties are not available.
- Focus-visible ring styles (outline color, width, offset) are not extracted.
- Loading states (spinner, skeleton) are not documented.
- The brand may use a secondary dark teal or dark green that wasn't clearly isolated from the palette noise.
- Star rating component assumes #c8ff00 based on its presence as a distinctive accent, but actual rating color may vary.
