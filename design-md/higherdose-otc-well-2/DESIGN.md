---
version: alpha
name: "HigherDose"
source_url: "https://higherdose.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-voltage wellness brand that uses #141414 near-black as its primary canvas, making every product shot and #4efac0 neon-green accent feel like a jolt of energy. The brand’s signature move is pairing deep, almost-ink backgrounds with electric accents — #4efac0 (a minty cyber-lime) appears on CTAs, progress indicators, and hover states, while #ff5742 (a hot coral) and #0018ff (a saturated blue) provide secondary voltage for badges and limited-edition drops. The typography stack runs Brown and Suisse Int’l — two typefaces with serious editorial weight — set at generous sizes that read as confident rather than loud. Product cards use `{rounded.sm}` (8px) corners, a subtle departure from the pill-shaped trend, giving the grid a precise, technical feel. The checkout and cart experience leans on `{colors.canvas}` (#fafafa) with `{colors.hairline}` (#dedede) borders, keeping the purchasing flow clean while the marketing pages stay dark and immersive. The brand’s voice is direct, almost clinical in its claims (“Get a Dose of the High Life”), but the visual system softens that edge with `{rounded.full}` on primary CTAs and a generous `{spacing.section}` (64px) that prevents the dark canvas from feeling oppressive. The extracted palette reveals a heavy reliance on grayscale — #9da1a0, #868a89, #545454, #7e7e7e — suggesting a mature system where color is deployed sparingly as a reward for user action.

colors:
  primary: "#4efac0"
  primary-active: "#3cfecf"
  primary-disabled: "#b6f5e0"
  ink: "#141414"
  body: "#545454"
  muted: "#868a89"
  muted-soft: "#9da1a0"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#141414"
  accent-coral: "#ff5742"
  accent-blue: "#0018ff"
  accent-green: "#00b84a"
  error: "#e61b1b"
  dark-canvas: "#141414"
  dark-surface: "#1a1a1a"
  dark-muted: "#7f8690"

typography:
  display-xl:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  link:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Brown', 'Suisse Int\\'l', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Inter', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase

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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 52px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-dark-active:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xxl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
    height: 60px
  search-bar:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.dark-muted}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    activeColor: "{colors.primary}"
    knobColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
  accordion:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in `{colors.primary}` (#4efac0) with dark text (`{colors.on-primary}`). Uses `{rounded.full}` pill shape and `{typography.button-md}` (Brown, 16px, weight 600, 0.5px letter-spacing). On hover, shifts to `{colors.primary-active}` (#3cfecf); disabled state uses `{colors.primary-disabled}` (#b6f5e0) with `{colors.muted}` text. Height is 52px with 14px/32px padding for comfortable tap targets.

**`button-secondary`** — An outlined variant with transparent background, `{colors.primary}` text, and a 2px solid `{colors.primary}` border. Same pill shape and typography as primary. On hover, fills with `{colors.primary}` and switches text to `{colors.on-primary}`. Used for "Learn More" and secondary product actions.

**`button-dark`** — A dark variant for light-background sections, using `{colors.ink}` (#141414) background with white text. On hover, shifts to `{colors.dark-surface}` (#1a1a1a) with `{colors.primary}` text. Used for checkout flows and cart actions.

### Navigation
**`nav-bar`** — Fixed top navigation on a `{colors.dark-canvas}` (#141414) background, 72px tall. Links use `{typography.nav-link}` (Brown, 14px, weight 500, uppercase, 0.5px letter-spacing) in `{colors.muted-soft}` (#9da1a0). Active links and hover states switch to `{colors.primary}`. The logo sits left-aligned, with cart and account icons right-aligned.

### Cards
**`product-card`** — White surface card (`{colors.surface-card}`) with `{rounded.sm}` (8px) corners — a deliberate choice that feels more technical than friendly. Product images share the same corner radius. Titles use `{typography.title-md}` (Brown, 18px, weight 600) with `{spacing.sm}` top margin; prices use `{typography.body-md}` in `{colors.body}` (#545454). Cards stack in a responsive grid with `{spacing.lg}` (24px) gaps.

### Badges
**`badge-new`**, **`badge-sale`**, **`badge-limited`** — Small uppercase labels using `{typography.badge}` (Inter, 11px, weight 700, uppercase) with `{rounded.xs}` (4px) corners and 2px/8px padding. New items get `{colors.accent-coral}` (#ff5742) background, sale items get `{colors.accent-green}` (#00b84a), and limited-edition drops get `{colors.accent-blue}` (#0018ff). All use white text.

### Forms
**`text-input`** — Standard input field on `{colors.canvas}` (#fafafa) with `{rounded.sm}` (8px) corners, 48px height, and 12px/16px padding. Default border is 1px `{colors.hairline}` (#dedede). On focus, border thickens to 2px `{colors.primary}`. Error state uses 2px `{colors.error}` (#e61b1b). Typography is `{typography.body-md}` (Inter, 16px).

### Hero
**`hero-section`** — Full-width section on `{colors.dark-canvas}` with white text, using `{typography.display-xl}` (Brown, 48px, weight 700, -1px letter-spacing). Padding is `{spacing.section}` (64px) vertically and `{spacing.xxl}` (48px) horizontally. The primary CTA (`hero-cta`) is larger than standard buttons — 60px tall with `{typography.button-lg}` (Brown, 18px, weight 600) and 16px/40px padding.

### Footer
**`footer`** — Dark section matching `{colors.dark-canvas}` with `{colors.muted-soft}` (#9da1a0) body text. Links use `{typography.link}` (Inter, 14px) and shift to `{colors.primary}` on hover. Padding matches hero section for visual symmetry.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; hero typography drops to 32px; product cards stack vertically; buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; nav remains expanded with reduced link spacing; hero maintains 36px display; side-by-side layout for form sections |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 48px display; max-width container at 1128px |
| Wide | > 1440px | Four-column product grid; hero expands to full-width with larger padding; max-width container at 1440px |

### Touch Targets
- All buttons and interactive elements minimum 44px height (primary buttons at 52px, secondary at 52px)
- Nav links have minimum 44px tap area even when text is smaller
- Quantity selector and toggle switches maintain 40px+ height
- Search bar at 48px height for easy tapping

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Hero section reduces padding from 64px to 32px on mobile
- Footer link columns stack vertically below 744px
- Badges remain inline but may wrap on very small screens

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (text-input, nav-links, footer-links) are inferred from common patterns rather than extracted from the live site
- Error state styling for forms (error messages, validation icons) not fully captured
- Dark mode is assumed to be the primary mode given the extracted palette, but light mode variants for some components may exist
- Sub-brand or promotional color palettes (holiday drops, collaborations) not captured
- Animation and transition timing values not extracted
- Dropdown menu styling (for nav, country selector, etc.) not available
- The extracted font list includes "Inter!important" which suggests a specificity override — the exact font stack hierarchy may vary by component
- Shopify checkout widget colors (Klarna, Afterpay, etc.) may be present in the extracted palette but are not part of the brand design system
- The extracted palette contains many grayscale values (#545454, #7e7e7e, #8f8f8f, #c4c4c4, #b6b9b8, #6c706f, #f3f3f3) that may represent specific UI surfaces or text weights not fully mapped
