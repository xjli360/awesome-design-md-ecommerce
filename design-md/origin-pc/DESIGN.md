---
version: alpha
name: "Origin PC"
source_url: "https://www.originpc.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Red cuts through black like a heat sink glowing under load — #cc181e is the single voltage that powers every call-to-action, configurator "Add" button, and promotional banner across Origin PC's dark-canvas interface. The site defaults to a near-black (#0d0d0d) ground, positioning itself closer to a cockpit HUD than a retail storefront; product photography floats on void, and spec tables read like telemetry. Heading type runs in Avalanche, a condensed geometric sans that compresses wide characters into narrow columns — ideal for system names like "CHRONOS" and "MILLENNIUM" where syllable count outpaces available horizontal space. Body copy shifts to Azo Sans Web at weight 400, offering clean legibility against dark surfaces at 15–16px without the personality overhead of the display face. A third voice, FF Basic Gothic Pro, appears in navigation links and micro-labels at weight 500/600, providing a utilitarian middle register between the cinematic Avalanche headlines and the workmanlike Azo body. Corners stay aggressive: buttons carry only `{rounded.xs}` (4px) or `{rounded.none}`, rejecting the pill-shaped friendliness of consumer marketplaces in favor of precision rectangles that echo chassis bezels and heat-vent geometry. Spacing is dense — product cards pack tightly in 12–16px gutters, while section padding remains generous (`{spacing.section}`) to let hero photography breathe. The near-white #fafafa serves double duty as primary text and surface highlight, its slight warmth preventing the harshness of pure white on OLED-targeted imagery. Interactive states lean on opacity shifts and red underlines rather than background swaps, maintaining the dark atmosphere even during hover and focus. The configurator — the brand's revenue engine — uses red step-indicators and highlighted selection borders to guide users through CPU, GPU, cooling, and aesthetic choices without breaking the immersive, spec-forward tone.

colors:
  primary: "#cc181e"
  primary-active: "#a81216"
  primary-disabled: "#661012"
  primary-glow: "rgba(204,24,30,0.25)"
  ink: "#fafafa"
  body: "#d4d4d4"
  muted: "#8a8a8a"
  muted-soft: "#5c5c5c"
  hairline: "#2a2a2a"
  hairline-soft: "#1e1e1e"
  canvas: "#0d0d0d"
  surface-soft: "#141414"
  surface-card: "#1a1a1a"
  surface-elevated: "#222222"
  on-primary: "#ffffff"
  on-dark: "#fafafa"
  success: "#2ecc40"
  warning: "#ffb400"
  error: "#cc181e"
  scrim: "rgba(0,0,0,0.75)"
  configurator-highlight: "#cc181e"
  badge-new: "#cc181e"
  badge-sale: "#ffb400"

typography:
  display-xl:
    fontFamily: "'Avalanche', 'ff-basic-gothic-pro', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Avalanche', 'ff-basic-gothic-pro', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
    textTransform: uppercase
  display-md:
    fontFamily: "'Avalanche', 'ff-basic-gothic-pro', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.2px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Avalanche', 'ff-basic-gothic-pro', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
    textTransform: uppercase
  title-lg:
    fontFamily: "'ff-basic-gothic-pro', 'azo-sans-web', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'ff-basic-gothic-pro', 'azo-sans-web', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'ff-basic-gothic-pro', 'azo-sans-web', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'azo-sans-web', 'azo-sans-uber', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'azo-sans-web', 'azo-sans-uber', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-uppercase:
    fontFamily: "'ff-basic-gothic-pro', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  spec-label:
    fontFamily: "'ff-basic-gothic-pro', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.4px
    textTransform: uppercase
  spec-value:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  button-md:
    fontFamily: "'azo-sans-uber', 'ff-basic-gothic-pro', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'azo-sans-uber', 'ff-basic-gothic-pro', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.17
    letterSpacing: 0.6px
    textTransform: uppercase
  button-lg:
    fontFamily: "'azo-sans-uber', 'ff-basic-gothic-pro', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'ff-basic-gothic-pro', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Avalanche', 'ff-basic-gothic-pro', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  price-sm:
    fontFamily: "'azo-sans-uber', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
    transition: "background-color 0.15s ease"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 0
    border: none
    borderBottom: "2px solid {colors.primary}"
  button-configure:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 40px
    height: 56px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  text-input-label:
    typography: "{typography.caption-uppercase}"
    textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
    transition: "border-color 0.2s ease"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 20px {colors.primary-glow}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section-lg} {spacing.xl}"
    minHeight: 600px
    backgroundSize: cover
    backgroundPosition: center
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 560px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 18px 48px
    height: 56px
  configurator-step:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  configurator-step-active:
    border: "2px solid {colors.configurator-highlight}"
    boxShadow: "0 0 12px {colors.primary-glow}"
  configurator-option:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  configurator-option-selected:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-elevated}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    rowBorder: "1px solid {colors.hairline-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.md} {spacing.base}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid transparent"
    padding: "{spacing.md} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"

---

## Components

### Buttons

**`button-primary`** — Solid red (#cc181e) rectangle with 4px radius, uppercase Azo Sans Uber at weight 700 with wide letter-spacing. Hover darkens to `{colors.primary-active}` via a 150ms background transition; no scale or shadow effects. Disabled state drops opacity to 0.6 and mutes the red to `{colors.primary-disabled}`. Used for all revenue-critical actions: "Configure Now," "Add to Cart," and checkout progression.

**`button-secondary`** — Transparent fill with a 1px white border and white uppercase text. On hover, the fill inverts to white with black text, creating a stark flash that draws attention without competing with the primary red. Used for secondary actions like "Learn More," "Compare," and "View Gallery."

**`button-ghost`** — No background or border; text in `{colors.primary}` with a 2px red bottom border acting as an underline. Used inline within content blocks for "See all specs" and "Read reviews" style links that need CTA weight without button chrome.

**`button-configure`** — An oversized variant of primary (56px height, wider padding) placed exclusively on product landing heroes. The larger touch target and heavier padding signals the start of the configurator funnel.

### Text Input

**`text-input`** — Dark card-surface fill (#1a1a1a) with a subtle hairline border. On focus, the border swaps to `{colors.primary}`, providing a red glow that matches the configurator's selection language. Labels sit above in uppercase caption style at `{colors.muted}`. Placeholder text uses `{colors.muted-soft}`.

### Navigation

**`nav-bar`** — 64px tall, full-bleed black bar with a single-pixel hairline bottom border. Logo sits left; nav links in FF Basic Gothic Pro uppercase at 13px weight 500 with 0.5px letter-spacing. Dropdown menus emerge as dark cards with hairline borders, no shadow — depth is communicated through border contrast rather than elevation.

**`category-tab-active`** / **`category-tab-inactive`** — Horizontal tab row below the nav for product categories (Desktops, Laptops, Workstations). Active tab has a 2px red bottom border; inactive tabs show transparent borders with muted text. Transition on hover fades text to `{colors.ink}`.

### Product Card

**`product-card`** — Dark card (#1a1a1a) with hairline border and 4px radius. On hover, the border transitions to `{colors.primary}` and a subtle red glow (`{colors.primary-glow}`) appears as a box-shadow, creating a "powered on" effect. Product image occupies the top 60% of the card; below sits the system name in `{typography.title-md}`, a one-line spec summary in `{typography.body-sm}`, and the starting price in red `{typography.price-sm}`. Cards maintain a fixed aspect ratio within grid layouts.

### Hero Section

**`hero-section`** — Full-viewport-width dark section with a dramatic product photograph (often a three-quarter angle of a lit chassis) as background. Headline in Avalanche uppercase at 48px sits left-aligned over a subtle gradient scrim. Subheadline in `{typography.body-md}` at max-width 560px prevents line lengths from exceeding comfortable reading. The hero CTA (`hero-cta`) sits below with generous top margin.

### Configurator

**`configurator-step`** — Vertical step panels representing build stages (Chassis, Processor, Graphics, Memory, Storage, Cooling). The active step receives a 2px red border and glow shadow; completed steps show a small red checkmark icon. Each step expands to reveal `configurator-option` cards in a grid.

**`configurator-option`** / **`configurator-option-selected`** — Individual component choices within a step. Selected state gains a 2px primary border and slightly elevated background. Option cards display the component name, a thumbnail, key spec, and price delta.

### Spec Table

**`spec-table`** — Alternating-row table used on product detail pages to display full system specifications. Labels in uppercase muted text, values in standard ink. Rows separated by `{colors.hairline-soft}` single-pixel borders. Entire table sits on `{colors.surface-soft}` with inner padding.

### Badges

**`badge-new`** — Small red pill (4px radius) with "NEW" in uppercase caption text. Applied to recently launched systems in navigation and product cards.

**`badge-sale`** — Amber/gold variant for promotional pricing, using `{colors.badge-sale}` to distinguish from the permanent-red brand language.

### Footer

**`footer`** — Full-width dark section separated by a hairline top border. Four-column layout with category headings in `{typography.title-sm}` and link lists in `{typography.body-sm}` at muted color. Bottom row contains copyright, legal links, and social icons.

### Search

**`search-bar`** — Dark-fill input matching `text-input` dimensions but placed in the nav context. Search icon in `{colors.muted}` sits left-inset. On focus, border highlights in red consistent with all input focus states.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; hero headline drops to `{typography.display-md}`; product grid becomes single-column; configurator steps stack vertically with accordion expansion; hero CTA stretches full-width |
| Tablet | 744–1128px | Product grid shifts to 2-column; nav shows top-level links with overflow in hamburger; configurator shows 2-column option grid; hero subhead constrained to 420px |
| Desktop | 1128–1440px | Full nav exposed; product grid at 3 columns; configurator shows 3-column option grid; hero photography at full bleed with text overlay |
| Wide | > 1440px | Content max-width caps at 1440px centered; product grid allows 4 columns; additional whitespace flanks content; hero image scales proportionally |

### Touch Targets

- All interactive elements maintain 44px minimum touch target on mobile
- Nav hamburger icon uses 48×48px tap area
- Configurator option cards have minimum 48px height with full-card tap area
- Product cards are fully tappable (entire card surface)
- Close/dismiss buttons (modals, drawers) use 44×44px tap zones

### Collapsing Strategy

- Navigation: full link bar → hamburger with slide-out drawer below 744px
- Product grid: 4-col → 3-col → 2-col → 1-col at each breakpoint
- Configurator: horizontal step bar → vertical accordion on mobile
- Spec tables: remain full-width but gain horizontal scroll on narrow viewports
- Hero text: left-aligned overlay → centered stacked layout below image on mobile
- Footer: 4-column grid → 2-column → single stacked column with accordions

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two hex colors extracted (#cc181e, #fafafa); the full dark palette (canvas black, surface grays, hairline values) is inferred from brand convention rather than directly extracted — actual values may differ by 5–15% lightness
- Avalanche font metrics (exact weight range, available styles) could not be confirmed from extraction; the font may be a custom subset with limited weights
- Azo Sans Uber vs. Azo Sans Web distinction (where each is applied) is inferred from naming convention — "uber" likely indicates bolder weights for UI elements
- No extracted border-radius values; the 4px default is based on the aggressive/angular gaming aesthetic observed in similar brands
- Configurator interaction patterns (animations, step transitions, price update behavior) are not captured in static extraction
- No theme-color meta tag found; dark-mode may be the only theme or a light variant may exist behind JS toggling
- Bootstrap Icons dependency detected but icon sizing, stroke width, and color application rules are not extractable from CSS alone
- Promotional banner/ticker behavior (rotation speed, dismissibility) not captured
