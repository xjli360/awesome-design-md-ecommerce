---
version: alpha
name: "Eufy"
source_url: "https://www.eufy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Clean anthracite (#1d1d1f) and near-void black (#080a0f) frame every hero section, throwing product photography into high-contrast relief — a staging technique borrowed from consumer electronics that positions Eufy as a device company selling robovacs and security cameras as premium hardware rather than commodity appliances. The primary interactive blue is #005d8e, deliberately desaturated and deep, sitting closer to a nautical or industrial reference than the cheerful azures most tech brands default to; it imparts authority to CTAs without reading as promotional or urgent. A secondary sky burst at #10b5ec handles animated feature callouts, specification number highlights, and progress indicators, while coral #f84d4f marks sale badges, alerts, and limited-time interrupts — never touching primary navigation. A further sky variant at #00a7e1 appears on hover states and icon accents, extending the blue family across three luminosity bands without introducing a second hue family. Typography runs DINNextLT — a geometric sans drawn from German engineering practice and transit signage — for all interface text and spec tables, lending watt counts, Pascal ratings, and battery runtimes an air of instrumentation rather than marketing copy. The proprietary Mach and Mach Tera families carry display-scale headlines: names evoking speed and scale that reinforce suction-power claims and run-time figures without asking the body copy to perform. Cards and modal surfaces sit on soft #f5f6f7 canvas using tight {rounded.sm} corners — closer to flat than rounded, deliberately resisting the pillowed shapes of consumer-app brands — while the dark-to-light page cadence (hero in near-black, features in warm gray, footer reverting to dark) gives a cinematic pacing unusual in the home robotics category. The system is designed to make hardware specifications feel legible as design values: large numeral callouts in spec-value scale, uppercase DINNextLT labels above each figure, and generous {spacing.section} vertical rhythm let the engineering substance breathe before the next CTA appears.

colors:
  primary: "#005d8e"
  primary-active: "#00486f"
  primary-disabled: "#80aec7"
  accent-sky: "#10b5ec"
  accent-sky-light: "#00a7e1"
  accent-coral: "#f84d4f"
  accent-coral-deep: "#da3c3c"
  success: "#37b679"
  warning: "#fc8037"
  ink: "#1d1d1f"
  body: "#323232"
  muted: "#75787f"
  muted-soft: "#9ca3af"
  hairline: "#d9d9d9"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f6f7"
  surface-card: "#f5f5f7"
  surface-mid: "#eeeeee"
  surface-dark: "#080a0f"
  surface-hero: "#1d1d1f"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Mach Tera', 'Mach', DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.6px
  display-lg:
    fontFamily: "'Mach Tera', 'Mach', DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.13
    letterSpacing: -0.4px
  display-md:
    fontFamily: "'Mach', DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Mach', DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  spec-unit:
    fontFamily: "DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  price:
    fontFamily: "'Mach', DINNextLT, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px

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
    padding: 12px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 26px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "1px solid rgba(255,255,255,0.35)"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 26px
    height: 48px
  button-ghost-dark-active:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.on-dark}"
    border: "1px solid rgba(255,255,255,0.55)"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    position: sticky
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    shadow: "0 2px 12px rgba(0,0,0,0.08)"
    borderBottom: none
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 640px
    padding: "{spacing.section} 0"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadOpacity: 0.75
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 480px
    padding: "{spacing.section} 0"
    headlineTypography: "{typography.display-lg}"
    subheadTypography: "{typography.body-md}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
    shadow: "0 2px 8px rgba(0,0,0,0.05)"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.body-sm}"
  product-card-hover:
    shadow: "0 8px 24px rgba(0,0,0,0.10)"
    border: "1px solid {colors.hairline}"
  spec-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-sky}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.ink}"
    unitTypography: "{typography.spec-unit}"
  spec-callout-dark:
    backgroundColor: "{colors.surface-hero}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.accent-sky}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    labelTypography: "{typography.spec-label}"
    labelColor: "rgba(255,255,255,0.5)"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.on-dark}"
  sale-badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  bestseller-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  feature-icon-tile:
    backgroundColor: "{colors.surface-soft}"
    iconColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.title-sm}"
    captionTypography: "{typography.body-sm}"
  feature-icon-tile-dark:
    backgroundColor: "rgba(255,255,255,0.06)"
    iconColor: "{colors.accent-sky}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.title-sm}"
    captionTypography: "{typography.body-sm}"
    captionOpacity: 0.65
  ecosystem-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    typography: "{typography.caption}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    typography: "{typography.button-sm}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    typography: "{typography.button-sm}"
  rating-row:
    starColor: "#f5a623"
    countColor: "{colors.muted}"
    typography: "{typography.caption}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline-soft}"
    highlightColumnBackground: "rgba(0,93,142,0.05)"
    highlightColumnBorder: "{colors.primary}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
  footer-dark:
    backgroundColor: "{colors.surface-hero}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "rgba(255,255,255,0.45)"
    linkColor: "{colors.accent-sky-light}"
    linkHoverColor: "{colors.accent-sky}"
    borderTop: "1px solid rgba(255,255,255,0.08)"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"

## Components

### Buttons

**`button-primary`** — The primary action button renders at 48px tall with `{rounded.xs}` corners (4px), producing a near-rectangular shape that reads as engineering-grade rather than consumer-app friendly. Background is `{colors.primary}` (#005d8e) in resting state, dropping to `{colors.primary-active}` (#00486f) on press; disabled state lightens to `{colors.primary-disabled}` without changing shape. Used exclusively for top-level purchase and navigation CTAs — "Shop Now", "Add to Cart", "Learn More".

**`button-secondary`** — Outlined at 2px border in `{colors.primary}`, transparent fill, same 48px height and `{rounded.xs}` radius as the primary. Used for secondary CTAs adjacent to a primary, or as the dominant action on light-surface sections where the filled blue would over-compete with product imagery. Active state fills subtly with `{colors.surface-soft}`.

**`button-ghost-dark`** — White-text ghost button for dark hero sections. A 1px semi-transparent white border at 35% opacity preserves legibility against both photography and solid dark backgrounds. Background fills to 10% white on hover. Used when a secondary CTA must sit directly over `{colors.surface-dark}` or `{colors.surface-hero}`.

### Inputs

**`text-input`** — 44px tall, `{rounded.xs}` radius, thin 1px `{colors.hairline}` border at rest. Focus ring upgrades to a 1.5px `{colors.primary}` stroke — no outer glow, matching the sharp engineering aesthetic. Placeholder text in `{colors.muted}`. Applied across search bars, email capture, and order-tracking fields.

### Navigation

**`nav-bar`** — Sticky white bar at 64px height with a 1px `{colors.hairline-soft}` bottom rule visible only at rest. `{typography.nav-link}` at 14px/500-weight in `{colors.ink}` for primary categories. On scroll, the bottom rule lifts and a diffuse 8px shadow grounds the bar against page content. Logo sits left; utility links (search, cart, account) cluster right with icon-button targets.

### Hero Sections

**`hero-banner`** — Dark hero sections at `{colors.surface-dark}` (#080a0f) with minimum 640px height. Headline runs `{typography.display-xl}` at 56px in `{colors.on-dark}`; subhead drops to `{typography.body-md}` at 75% opacity to preserve hierarchy without a color change. Product photography is typically centered or right-weighted with transparent-background renders. `{spacing.section}` vertical padding top and bottom.

**`hero-banner-light`** — A warm-gray variant using `{colors.surface-soft}` (#f5f6f7) for midpage feature sections. Headline uses `{typography.display-lg}` at 40px; same body-md subhead. Gives visual relief between two dark sections without reverting to pure white.

### Product Cards

**`product-card`** — White surface with 1px `{colors.hairline-soft}` border and a barely-perceptible 2px/8% shadow at rest. `{rounded.sm}` (8px) radius. On hover the shadow deepens to 24px/10% and the border darkens to `{colors.hairline}`. Title in `{typography.title-md}`, price in `{typography.price}` (Mach 24px/700), caption specs in `{typography.body-sm}`. Badges overlay top-left: coral `sale-badge` or blue `new-badge`.

### Specification Callouts

**`spec-callout`** — The signature Eufy pattern: a large number in `{typography.spec-value}` (Mach 40px/700), preceded by an uppercase `{typography.spec-label}` in `{colors.muted}`, and followed by a `{typography.spec-unit}` suffix (e.g., "8,000 Pa" or "180 min"). Set on `{colors.surface-soft}` with `{rounded.sm}`. The dark variant `spec-callout-dark` inverts onto `{colors.surface-hero}` with the value in white and label at 50% white opacity — used inside dark hero sections.

### Badges

**`sale-badge`** / **`new-badge`** / **`bestseller-badge`** — All share 10px uppercase DINNextLT at `{typography.badge}`, 3px/8px padding, and `{rounded.xs}` corners. Sale uses coral `{colors.accent-coral}`; New uses deep blue `{colors.primary}`; Bestseller uses `{colors.ink}` for a muted editorial feel. Badges are applied to product card thumbnails and category grid headers, never stacked more than two per card.

### Feature Icon Tiles

**`feature-icon-tile`** — Square-ish tiles on `{colors.surface-soft}` with a centered icon in `{colors.accent-sky}` and label in `{typography.title-sm}` below. Caption body in `{typography.body-sm}`. Used in 4-up or 6-up grids to communicate technology features (LiDAR navigation, HEPA filtration, AI obstacle detection). The dark variant `feature-icon-tile-dark` places the same layout on a frosted-glass-like panel at 6% white fill against the dark hero.

### Ecosystem Badges

**`ecosystem-badge`** — Small 1px-bordered white chips listing platform compatibility ("Works with Alexa", "Google Home", "Apple HomeKit"). White background, `{colors.hairline}` border, `{rounded.sm}`, caption typography. Displayed as a horizontal chip row beneath product hero text — never as standalone section content.

### Category Chips

**`category-chip`** / **`category-chip-active`** — Full-pill (`{rounded.full}`) filter chips used in the product listing page to switch between product lines (Robovacs, Security Cameras, Smart Locks). Resting state in `{colors.surface-soft}` with muted body text. Active state fills to `{colors.primary}` with white text. Chips scroll horizontally on mobile.

### Comparison Table

**`comparison-table`** — Side-by-side product comparison with a soft `{colors.surface-soft}` header row and alternating white rows. The highlighted/recommended column receives a 5% blue tint on `{colors.primary}` and a 1px top border in `{colors.primary}`. Row labels in `{typography.body-sm}`, values in `{typography.title-sm}`. Check marks render in `{colors.accent-sky}`. Applied on product detail pages when 2–4 SKUs are compared.

### Footer

**`footer-dark`** — Near-black `{colors.surface-hero}` footer with a 1px 8%-white top rule. Column headings in `{typography.title-sm}`/white; body links in `{typography.body-sm}` at 45% white opacity, rising to full white on hover. Link accent color is `{colors.accent-sky-light}` (#00a7e1) for external resource links (support, warranty). Social icons and app-store badges render at full white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hamburger nav collapses all categories; hero height reduced to 480px; category chips scroll horizontally; spec callouts stack vertically; product grid is 1-up |
| Tablet | 744–1128px | Two-column product grid; nav expands to show top-level categories inline with overflow menu; hero at 560px; feature tiles in 2×2 grid; comparison table scrolls horizontally |
| Desktop | 1128–1440px | Full sticky nav with all category dropdowns; 3–4 column product grid; hero at 640px+; spec callouts arrange in 4-up horizontal row; feature tiles 4-up or 6-up |
| Wide | > 1440px | Max-width container at 1440px centers content; hero imagery scales up without increasing nav or section padding; product grid remains 4-up with increased card size |

### Touch Targets

- All interactive controls minimum 44×44px; icon buttons in nav reach 44px via padding expansion
- Category chips maintain 36px minimum tap height on mobile despite visual 30px height
- Bottom-of-card CTA buttons expand to full card width on mobile
- Cart and account icons in mobile nav hit 48px tap areas via extended padding

### Collapsing Strategy

- Nav collapses at < 744px to hamburger; category mega-menus become full-screen slide-in drawers
- Comparison table drops to horizontal scroll at < 1128px; on mobile shows maximum 2 products
- Feature tile grids reflow: 6-up → 3-up (tablet) → 2-up (mobile)
- Spec callout rows stack to 2-up at tablet, 1-up at mobile with reduced spec-value font (28px)
- Hero subhead hides at < 375px to preserve headline visibility
- Ecosystem badge chips wrap to two lines on narrow mobile rather than scrolling horizontally

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Mach and Mach Tera font weights, optical sizes, and variable axes are not publicly documented; weight 700 and the Mach Tera/display-Mach distinction are inferred from site rendering
- MontForAnker font stack appears in extraction — likely Montserrat customized for Anker parent brand; not used in visible Eufy UI but may apply to shared Anker-branded pages
- Many extracted colors (#f81ce5, #0070f3, #ff0080, #ff379c, #eb367f, #7928ca, #4c2889) are Next.js/Vercel framework artifact colors (error overlays, dev toolbar), not Eufy brand colors — excluded from palette
- Primary button hover state hex not extracted; #00486f is a derived estimate from the primary
- No motion/animation timing values extracted (easing curves, duration tokens for product hero video transitions)
- Dark-mode variant not confirmed; Eufy's site does not appear to respect prefers-color-scheme at time of extraction
- DINNextLT variant specifics (Pro, W01, Rounded) not confirmed; rendering appears to use DINNextLT Pro or DINNextLT-Regular at standard weights
