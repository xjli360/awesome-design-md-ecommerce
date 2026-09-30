---
version: alpha
name: "MOO"
source_url: "https://www.moo.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The country-selector landing page immediately reveals something peculiar about MOO's design philosophy — even a purely functional routing screen gets the full brand treatment: rounded type, open whitespace, and a single `#00ac73` teal-green that pulses against a near-paper-white `#ecefed` canvas. That green, warmer than clinical mint and more saturated than sage, is MOO's chromatic signature: it appears wherever the interface needs to invite action, from primary CTAs to hover states, carrying the brand's argument that print-on-demand can feel joyful rather than transactional.

  MOO commissions two proprietary typefaces that define the brand's entire tonal register. Bryant MOO Pro — a rounded grotesque with soft terminals and generous ink traps — anchors display and headline work, resisting the stiffness of geometric sans-serifs without tipping into the casualness of a handwritten face. Avenir Next Rounded Pro picks up at UI scale, continuing the rounded-terminal logic through labels, navigation, and body copy. The result is a type system where nothing has a hard corner; even at the smallest caption size, the letterforms suggest that something crafted and physical is nearby.

  The ink color carries a barely perceptible forest-green undertone at `#07120c`, distinct from pure carbon black and harmonically related to the primary green. Body text resolves at `#1d1d1b`, which reads as black but warms the reading experience by a fraction. The mid-range neutral is `#97a39c`, a sage-meets-grey that holds hierarchy together in muted text, dividers, and secondary labels without competing with the green. Dark-section backgrounds anchor in `#122e1d`, a deep forest that grounds the palette in something earthlike rather than technological.

  Interactive geometry leans round: primary buttons sit at `{rounded.full}`, product cards at `{rounded.lg}`. MOO treats its UI components the way it treats its print products — edges finished, surfaces smooth. The spatial system is generous; whitespace is a structural element, echoing the card stock the brand manufactures. Photography of actual printed products does the heavy selling, so the UI steps back, keeps the grid clean, and lets a single spot of brand green tell users exactly where to go next.

colors:
  primary: "#00ac73"
  primary-active: "#007f54"
  primary-mid: "#008558"
  primary-disabled: "#97a39c"
  ink: "#07120c"
  body: "#1d1d1b"
  muted: "#97a39c"
  hairline: "#e6e7e7"
  hairline-soft: "#dfe3e7"
  canvas: "#ffffff"
  surface-paper: "#ecefed"
  surface-soft: "#f3f3f3"
  surface-card: "#ecefed"
  surface-dark: "#122e1d"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Bryant MOO Pro Medium', 'Bryant MOO Pro Regular', Geneva, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Bryant MOO Pro Medium', 'Bryant MOO Pro Regular', Geneva, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Bryant MOO Pro Medium', Geneva, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Avenir Next Rounded Pro Medium', 'Avenir Next Rounded Pro Regular', Trebuchet MS, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Avenir Next Rounded Pro Medium', Trebuchet MS, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Avenir Next Rounded Pro Regular', Trebuchet MS, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir Next Rounded Pro Regular', Trebuchet MS, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir Next Rounded Pro Regular', Trebuchet MS, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Bryant MOO Pro Medium', Geneva, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Bryant MOO Pro Medium', Geneva, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "'Avenir Next Rounded Pro Medium', Trebuchet MS, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  price:
    fontFamily: "'Bryant MOO Pro Medium', Geneva, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "'Avenir Next Rounded Pro Medium', Trebuchet MS, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  country-label:
    fontFamily: "'Avenir Next Rounded Pro Regular', Trebuchet MS, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
    focusBorder: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    activeLinkColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    hoverBoxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  hero:
    backgroundColor: "{colors.surface-paper}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingBlock: "{spacing.section}"
    ctaButton: button-primary
  finish-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    selectedBackground: "{colors.surface-paper}"
  paper-selector:
    backgroundColor: "{colors.canvas}"
    selectedBorder: "2px solid {colors.primary}"
    selectedBackground: "{colors.surface-paper}"
    unselectedBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    labelTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"
    accentColor: "{colors.primary}"
  country-selector-tile:
    backgroundColor: "{colors.canvas}"
    hoverBackgroundColor: "{colors.surface-paper}"
    textColor: "{colors.body}"
    typography: "{typography.country-label}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  print-preview:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    linkHoverColor: "{colors.primary}"
    captionTypography: "{typography.caption}"
    paddingBlock: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — The principal CTA rendered in MOO's signature `#00ac73` green on a fully rounded pill (`{rounded.full}`, 48px height). On hover or active state, the background deepens to `#007f54` with no shape change — the pill geometry holds at every state. On disabled, the fill shifts to the sage neutral `#97a39c`, which reads as "unavailable" while preserving the rounded form so the affordance remains legible.

**`button-secondary`** — White fill with a 2px `#00ac73` border and matching green text, same full-pill geometry. Used for co-equal CTAs where a second action needs prominence without overriding the visual hierarchy; the green border echoes the primary's fill without competing for the same eye weight.

**`button-ghost`** — Transparent background, `#1d1d1b` body text, no visible border, `{rounded.full}` shape. Lighter padding than the two button-variants above. Reserved for tertiary flows — "Learn more" links embedded in copy blocks, dismissals, or breadcrumb-level navigation.

### Inputs

**`text-input`** — White fill, 1px `#e6e7e7` border, `{rounded.md}` (12px), height 48px to align naturally with button pairings in inline search layouts. Placeholder text renders in `#97a39c`. On focus, the border upgrades to 2px `#00ac73` — the primary green returns here as an attention signal rather than a fill, maintaining hierarchy while making the active field unmistakable.

### Navigation

**`nav-bar`** — White canvas background, 64px tall, 1px `#e6e7e7` bottom border. Links use `{typography.nav-link}` (Avenir Next Rounded Pro Medium, 15px). The active category and hovered items shift to `#00ac73`. MOO logo anchors left; account and cart icons sit right. The nav trusts category legibility over exhaustive listings — no mega-menu sprawl.

### Product Cards

**`product-card`** — White fill, `{rounded.lg}` (20px) corners, 1px hairline border, 4px/0.08-opacity box-shadow on hover that lifts the card without dramatizing it. Titles in `{typography.title-md}` (Avenir Next Rounded Pro Medium, 18px), pricing in `{typography.price}` (Bryant MOO Pro Medium, 20px). Interior padding at `{spacing.lg}` mirrors the macro whitespace philosophy — negative space is treated as product real estate, not waste.

### Finish Badge

**`finish-badge`** — Small rectangular chip at `{rounded.xs}` (4px) carrying finish names such as "Spot UV", "Soft Touch", or "Matte". Typography in `{typography.badge-label}` (Avenir Next Rounded Pro Medium, 11px, uppercase, +0.5px tracking). Default state: `#f3f3f3` fill, `#e6e7e7` border. Selected state: 2px `#00ac73` border, `#ecefed` surface-paper fill. The chip never changes size — selection signal is purely chromatic.

### Paper Selector

**`paper-selector`** — Grid of named tiles or material swatches used in the product customisation flow. Unselected: white fill, 1px `#e6e7e7` border, `{rounded.sm}`. Selected: 2px `#00ac73` border, `#ecefed` fill. Tile labels in `{typography.title-sm}`; secondary descriptors (weight, texture) in `{typography.caption}`. Touch-friendly tile sizing (minimum 80px) keeps finger accuracy high on mobile without breaking the grid.

### Quantity Selector

**`quantity-selector`** — Inline stepper on a `#f3f3f3` pill background, `{rounded.md}`, with `+` and `−` controls rendered in `#00ac73`. The current quantity displays in `{typography.title-md}`. Reactive pricing updates below the stepper as the user adjusts, displayed in `{typography.price}`. The green accent on the stepper controls creates a micro-CTA rhythm that nudges quantity upward.

### Country Selector Tile

**`country-selector-tile`** — Grid card used on MOO's routing landing screen to direct international visitors. White fill, `{rounded.sm}`, 1px soft-hairline border. On hover, fill shifts to `#ecefed`. Country name in `{typography.country-label}` (Avenir Next Rounded Pro Regular, 13px, `#1d1d1b`). Flag imagery dominates the tile interior; MOO brand colors frame rather than compete with national identities.

### Hero

**`hero`** — `#ecefed` warm off-white background, full-width, `{spacing.section}` vertical padding. Headline in `{typography.display-xl}` (Bryant MOO Pro Medium, 48px). Supporting body copy in `{typography.body-md}`. Primary CTA uses `button-primary`. Photography of physical print products typically appears right-of-center or bleeds to the canvas edge; the warm background provides enough contrast that no text overlay scrim is needed.

### Print Preview

**`print-preview`** — A constrained-width display panel, `{rounded.md}`, floated on a `#f3f3f3` surface with a 32px/0.12-opacity drop shadow that simulates a physical card resting on a desk. Used in product detail pages and the design editor to give users spatial confidence in how their order will look in hand — the shadow depth is non-trivial because it does selling work, not just decoration.

### Footer

**`footer`** — Deep forest `#122e1d` background, white `{colors.on-dark}` text. Column headings in `{typography.title-sm}`. Body links in `{typography.body-sm}` with `#00ac73` hover state — the primary green reappears against the dark ground as a wayfinding accent. Social links and legal copy in `{typography.caption}`. `{spacing.xxl}` vertical padding; the generous breathing room continues the macro-whitespace logic even inside the dark section.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero headline drops to `{typography.display-md}`; `paper-selector` scrolls horizontally; `product-card` interior padding reduces to `{spacing.base}` |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links, secondary overflow to menu; hero runs two columns (text left, image right) |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav visible with all category links; hero at full `{typography.display-xl}` |
| Wide | > 1440px | Content constrained to ~1280px max-width and centred; grid expands to five columns on browsing pages; footer columns spread across full row width |

### Touch Targets

- All buttons minimum 48px height and 44px minimum tap width
- `quantity-selector` stepper `+`/`−` controls padded to a minimum 44×44px invisible hit area
- `country-selector-tile` minimum 80px height with 8px gap between tiles for fat-thumb targeting
- Nav icons (account, cart, search) minimum 44×44px with transparent hit-area extension beyond visible bounds
- `paper-selector` tiles minimum 72px wide on mobile with 8px gap

### Collapsing Strategy

- Navigation: hamburger at mobile, partial link row at tablet, full flat nav at desktop
- Product grid: 1 → 2 → 3–4 → 4–5 columns across breakpoints
- Hero: stacked layout (text above image) at mobile; side-by-side split at tablet and above
- Footer: single-column stacked at mobile; four-column grid at desktop and wide
- Finish and paper selectors: horizontal scroll container on mobile, wrapping grid on tablet and above
- Print preview panel: full-width at mobile, constrained to 50% of content column at desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Palette extracted from a country-selector page; a large subset of hex values (`#e52420`, `#cc2229`, `#b32335`, `#3c3b6e`, `#33348e`, `#203c89`, `#ffcc0c`, `#009246`, etc.) are almost certainly national flag colors, not MOO brand tokens
- No meta theme-color set on the page; `#00ac73` as primary is inferred from MOO's well-documented brand identity and corroborated as the most distinctive non-flag green in the extraction
- Exact button border-radius not confirmed from live DOM extraction — `{rounded.full}` inferred from rounded brand character and font system
- Font weights for Bryant MOO Pro not confirmed beyond the "Medium" and "Regular" variants found in the stack extraction; bold and light cuts unknown
- Dark mode palette entirely unextracted; `surface-dark` (`#122e1d`) is speculative, derived from the darkest extracted green
- No icon system, illustration style, or motion/animation data captured
- Exact nav bar height (64px assumed) not confirmed from extraction
- Hover and focus transition durations and easing curves not captured
- Print preview shadow values are approximated — exact elevation system not observable from extraction alone
