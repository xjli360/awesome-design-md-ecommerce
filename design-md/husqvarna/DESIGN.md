---
version: alpha
name: "Husqvarna"
source_url: "https://www.husqvarna.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Forest green at #227730 grounds the interface before the first scroll — nav hover states, category chips, and active underlines all draw from the same Swedish-woodland hue that Husqvarna's equipment designers have printed on cutting-deck graphics since the brand's postwar expansion into powered garden tools. The yellow at #f1ce00 arrives as punctuation rather than field fill: it charges every primary CTA, crowns the dealer-locator trigger, and fires across promotional call-outs, doing in two seconds what the brand's signature painted chassis have done on suburban lawns for decades. Husqvarna Gothic — a custom grotesque commissioned for the brand — handles all display text at `{typography.display-xl}` weight 700; its tightly-spaced capitals read structural and precise, the visual equivalent of a torque specification rather than a lifestyle aspiration. Body copy drops to Montserrat for subheadings and Roboto for longer spec-sheets and FAQ prose, stacking three voices without competing. Corner radii stay deliberately low — product cards at `{rounded.sm}`, buttons at `{rounded.xs}` — pushing back against the pill-heavy softness of consumer lifestyle brands in favor of geometry that reads machined rather than friendly. The lime accent at #b1c823 marks battery-powered and Automower lines, threading an eco signal through the catalog without disturbing the primary green. Orange at #d87d2b inherits the thermal-warning language of the machines themselves: it surfaces on promotional sale flags and caution callouts, never on navigation. Charcoal at #575b61 anchors ink and icon chrome so that product photography — morning-dew grass cylinders, soil-encrusted blade assemblies, precision cutting-deck exploded views — carries the full visual weight of the page without competing with UI scaffolding. The layout reads as an engineering catalog restructured into a purchase surface: information-dense, grid-locked, and color-disciplined.

colors:
  primary: "#227730"
  primary-active: "#1a5a24"
  primary-disabled: "#8fbb93"
  accent-yellow: "#f1ce00"
  accent-yellow-active: "#d4b000"
  accent-yellow-disabled: "#f8e980"
  accent-lime: "#b1c823"
  accent-green-bright: "#299b00"
  accent-green-mid: "#5b9d4d"
  accent-orange: "#d87d2b"
  accent-red: "#c21a2e"
  ink: "#575b61"
  body: "#575b61"
  muted: "#979797"
  hairline: "#d0d0d0"
  hairline-soft: "#d2d2d1"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-dark: "#2a2d32"
  on-primary: "#ffffff"
  on-yellow: "#575b61"

typography:
  display-xl:
    fontFamily: "'Husqvarna Gothic', Montserrat, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Husqvarna Gothic', Montserrat, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Husqvarna Gothic', Montserrat, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Montserrat, 'Husqvarna Gothic', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Montserrat, 'Husqvarna Gothic', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Husqvarna Gothic', Montserrat, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  spec-label:
    fontFamily: "Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Husqvarna Gothic', Montserrat, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "Montserrat, 'Husqvarna Gothic', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Montserrat, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Husqvarna Gothic', Montserrat, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  badge:
    fontFamily: "Montserrat, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-yellow}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.accent-yellow-active}"
    textColor: "{colors.on-yellow}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-yellow-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-active-indicator:
    backgroundColor: "{colors.accent-yellow}"
    height: 3px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageAspectRatio: "4/3"
    priceTypography: "{typography.price-display}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaVariant: button-primary
    minHeight: 520px
    overlayOpacity: 0.45
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    borderActive: "2px solid {colors.primary}"
    textColorActive: "{colors.primary}"
  badge-eco:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-warning:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  spec-row:
    backgroundColor: "{colors.surface-soft}"
    altBackgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    padding: 12px 16px
    borderBottom: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    height: 48px
    iconColor: "{colors.muted}"
    submitButtonColor: "{colors.primary}"
  dealer-locator-cta:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-yellow}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 40px
    iconColor: "{colors.on-yellow}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.accent-yellow}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    paddingVertical: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — The primary action trigger uses Husqvarna yellow (#f1ce00) with dark charcoal text (`{colors.on-yellow}`) rendered in all-caps `{typography.button-lg}` with 1px letter-spacing. The near-zero `{rounded.xs}` corner (2px) reads manufactured, not bubbly. Active state shifts to `{colors.accent-yellow-active}` (#d4b000); disabled washes to `{colors.accent-yellow-disabled}` with `{colors.muted}` text. Fixed at 48px height across all breakpoints — the yellow-on-charcoal combination is the brand's clearest action signal and recurs on hero panels, product pages, and the dealer-locator modal trigger.

**`button-secondary`** — Forest green (#227730) fill with white text, identical uppercase `{typography.button-lg}` treatment to `button-primary`. Used for secondary purchase paths, "Compare" actions, and category-level navigation CTAs where yellow already occupies the primary slot. Active deepens to `{colors.primary-active}` (#1a5a24).

**`button-ghost`** — Transparent fill, 2px `{colors.primary}` border, matching green label in `{typography.button-md}`. Applied to supporting actions such as "Learn More" and "View Full Specs" where a three-tier CTA hierarchy is needed. On hover/active the border fills solid `{colors.primary}` and text inverts to `{colors.on-primary}`.

### Product Card

**`product-card`** — Cards clip at `{rounded.sm}` (4px) with a 1px `{colors.hairline}` border, keeping the catalog reading as a parts database rather than a lifestyle grid. Product name uses `{typography.title-sm}` (Montserrat 16px 600), price uses `{typography.price-display}` (Husqvarna Gothic 28px 700), and the short spec summary uses `{typography.body-sm}` Roboto. Battery-powered variants stack a `badge-eco` lime chip below the product name; sale items prepend a `badge-sale` red chip above. Image aspect ratio is locked 4:3 to prevent layout shift across catalog pages with mixed product photography.

### Navigation

**`nav-bar`** — 64px tall white bar with a 1px `{colors.hairline}` bottom border. Top-level links render in `{typography.nav-link}` (Husqvarna Gothic 14px 600). The active category receives a 3px `{colors.accent-yellow}` underline strip via `nav-bar-active-indicator`, borrowing the yellow accent language of CTAs without flooding the nav with color. On desktop, hovering a category opens a full-width mega-menu panel over a `{colors.canvas}` background.

### Hero Banner

**`hero-banner`** — Full-bleed photography panels with `{colors.surface-dark}` (#2a2d32) as the image-fail fallback and a 0.45 opacity scrim over photography. Headline in `{typography.display-xl}` (Husqvarna Gothic 40px 700) reversed to `{colors.canvas}`. Body copy in `{typography.body-md}` Roboto at reduced opacity (0.85). Primary CTA uses `button-primary` yellow — high contrast against both dark photography and the scrim. Minimum height 520px on desktop; mobile reduces to 320px.

### Search

**`search-bar`** — Inline search at 48px height with a 1px `{colors.hairline}` border and `{rounded.xs}` corners. Submit icon color is `{colors.primary}` green. Placeholder and input text in `{typography.body-md}`. On focus, border upgrades to 2px `{colors.primary}`. The search component appears in the nav-bar rail on desktop and expands to full-width on mobile below the hamburger.

### Badges

**`badge-eco`** — Lime (#b1c823) background on `{colors.ink}` text, all-caps 11px Montserrat. Applied to Automower and battery-powered product lines to surface the EPOS/sustainability thread. **`badge-warning`** — Orange (#d87d2b) with `{colors.canvas}` text for caution callouts and accessory compatibility flags, inheriting the thermal-alert color language from the physical machinery. **`badge-sale`** — Red (#c21a2e) with `{colors.canvas}` text, used exclusively during promotional pricing events.

### Spec Table

**`spec-row`** — Alternating `{colors.surface-soft}` / `{colors.canvas}` row fills with `{typography.spec-label}` (uppercase 12px Roboto 500) for the property name in `{colors.muted}` and `{typography.body-sm}` Roboto for the value in `{colors.ink}`. A 1px `{colors.hairline}` bottom rule separates rows. This is the dominant component on individual product pages — riding-mower and robotic-mower detail pages typically run 15–25 spec rows covering cutting width, engine displacement, drive speed, and noise level.

### Category Chips

**`category-chip`** — Softly cornered (`{rounded.sm}`, 8px) gray surface chips for filtering the product grid. All-caps `{typography.button-sm}` label in `{colors.ink}`. Active state adds a 2px `{colors.primary}` border and shifts text to `{colors.primary}`. On mobile the chip row scrolls horizontally with no wrapping.

### Dealer Locator CTA

**`dealer-locator-cta`** — A wide `{colors.accent-yellow}` button with generous horizontal padding (40px) and `{typography.button-lg}` uppercase treatment. Husqvarna's offline dealer network is a primary conversion path — this component recurs in the page footer, product-page sidebar, and as a sticky rail element on desktop product detail pages. Icon (map-pin or arrow) uses `{colors.on-yellow}` for consistent contrast.

### Footer

**`footer`** — `{colors.surface-dark}` (#2a2d32) background with `{colors.canvas}` body text. Section headings in `{typography.title-sm}` Montserrat 600. Navigation links render in `{colors.hairline-soft}` (#d2d2d1) and warm to `{colors.accent-yellow}` on hover. Four-column grid on desktop (Products, Support, About, Country selector) collapses to stacked accordions on mobile. Legal line and copyright in `{typography.caption}` at reduced opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero reduces to 320px min-height; spec rows stack label above value; category chips scroll horizontally with no wrap; footer becomes per-section accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with sub-menus on tap; hero at 400px min-height; spec table returns to two-column inline row layout |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu nav; hero at 520px min-height; sticky sidebar with `dealer-locator-cta` on product detail pages |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered with side gutters; hero scales to 600px min-height; spec table adds optional "compare" toggle column |

### Touch Targets

- All interactive elements minimum 44×44px on touch viewports
- Category chips expand to 12px vertical padding on mobile
- Collapsed nav items are 48px tall full-width list rows
- Product card tap target covers the full card face, not only the text label
- Badge chips on product cards have 8px tap-area padding around visible bounds

### Collapsing Strategy

- Navigation: hamburger at < 744px; full horizontal bar with mega-menu at ≥ 1128px
- Product grid: 1-col → 2-col → 3-col → 4-col at 744 / 1128 / 1440px breakpoints
- Hero headline: `{typography.display-xl}` (40px) on desktop, `{typography.display-lg}` (32px) on tablet, `{typography.display-md}` (24px) on mobile
- Footer: 4-col grid → 2-col grid → accordion at 1128 / 744px breakpoints
- Spec table: label stacks above value within the same row on mobile; returns to inline two-column at ≥ 744px
- Sticky dealer-locator sidebar rail: visible at ≥ 1128px; becomes full-width block above footer on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; browser chrome tint unknown — `{colors.primary}` (#227730) assumed as default
- Exact Husqvarna Gothic weight axis (full variable range vs. discrete 400/700 only) not confirmed; weight 700 used throughout display but lighter display variants may not be licensed for web
- `{colors.surface-soft}` (#f4f4f4) and `{colors.surface-dark}` (#2a2d32) are inferred from the extracted gray cluster — exact footer and off-white fill hex values were not directly observed in extraction
- Animation durations and easing curves for product-card hover lift, mega-menu dropdown, and image carousel transitions not captured
- Whether Husqvarna Gothic downsizes gracefully below 744px or swaps to Montserrat for display text on mobile not confirmed from static extraction
- Mega-menu column count, featured-image slot, and sub-category link density not extracted
- Product comparison table interaction (checkbox selection, sticky header column, side-scroll behavior) not observed
- Automower-specific UI patterns (zone mapping, scheduling interface) likely diverge from the standard catalog components documented here
