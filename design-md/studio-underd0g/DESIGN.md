---
version: alpha
name: "Studio Underd0g"
source_url: "https://www.underd0g.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The typographic "0" substituted into "Underd0g" isn't an affectation — it's a declaration of method: a studio that thinks in parts, in codes, and in movements, where the glyph-swap is the first signal that the design language runs on monospace precision rather than luxury-brand serif warmth. The site renders almost entirely on a near-black canvas (#121212, #1c1c1c), where each watch dial colorway becomes its own distinct world — dusty rose (#e0b1a4), soft pink (#dfa7b0), powder blue (#cbe0f3), warm khaki (#d0c18f), sage (#d0d8af) — a chromatic vocabulary borrowed directly from dial photography rather than assigned to an abstract brand palette. These pastel-on-dark contrasts give product pages an almost archival quality, as if each reference number is a pinned specimen. Against the dark field, an orange punch (#ed762b) acts as the alert-state voltage: rare, pointed, and never used decoratively. A deep burgundy-black (#33081c) provides a secondary depth layer that reads richer than plain black for hover states and surface differentiation. Monospace type throughout is the most consequential design decision the brand makes: on a watch micro-brand, this choice signals watchmaker's notation and circuit-board precision rather than editorial lifestyle warmth, and gives specification pages a character that feels credibly independent. `{rounded.sm}` corners on interactive elements — neither pill nor hard-edged — project craft confidence without startup softness. The spacing system is tight and collector-facing: someone who opens a product page wants to read case diameter as data, crown position as fact, not as the opening of a poem. Mid-grays (#777777, #555555) carry supporting copy, and the lightest surface (#dedede) appears only at hairlines and dividers, keeping every content zone anchored to the dark ground.

colors:
  primary: "#e0b1a4"
  primary-active: "#dfa7b0"
  primary-disabled: "#9e7e78"
  accent-orange: "#ed762b"
  accent-burgundy: "#33081c"
  ink: "#dedede"
  body: "#aaaaaa"
  muted: "#777777"
  muted-soft: "#555555"
  hairline: "#2e2e2e"
  canvas: "#121212"
  canvas-raised: "#1c1c1c"
  surface-card: "#191919"
  surface-soft: "#1c1c1c"
  on-primary: "#121212"
  on-dark: "#dedede"
  dial-rose: "#e0b1a4"
  dial-pink: "#dfa7b0"
  dial-blue: "#cbe0f3"
  dial-khaki: "#d0c18f"
  dial-sage: "#d0d8af"

typography:
  display-xl:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.4px
  spec-label:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  spec-value:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  button-md:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  price:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  ref-number:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 9px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 2.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.canvas-raised}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.muted}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas-raised}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderRadius: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    borderColor: "{colors.primary}"
    outlineColor: "{colors.primary}"
    outlineWidth: 1px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-logo:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  product-card:
    backgroundColor: "{colors.canvas-raised}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspect: "1 / 1"
    padding: "{spacing.md}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-ref:
    typography: "{typography.ref-number}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero:
    backgroundColor: "{colors.canvas}"
    minHeight: 100vh
    textColor: "{colors.ink}"
    layout: "split — dial photography left, text block right on desktop; stacked on mobile"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    maxWidth: 480px
  dial-swatch:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.ink}"
    cursor: pointer
  dial-swatch-rose:
    backgroundColor: "{colors.dial-rose}"
  dial-swatch-pink:
    backgroundColor: "{colors.dial-pink}"
  dial-swatch-blue:
    backgroundColor: "{colors.dial-blue}"
  dial-swatch-khaki:
    backgroundColor: "{colors.dial-khaki}"
  dial-swatch-sage:
    backgroundColor: "{colors.dial-sage}"
  spec-table:
    backgroundColor: "{colors.canvas-raised}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  spec-row-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
    minWidth: 140px
  spec-row-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  spec-row-divider:
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.sm}"
  collection-badge:
    backgroundColor: "{colors.accent-burgundy}"
    textColor: "{colors.dial-rose}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  announcement-bar:
    backgroundColor: "{colors.accent-burgundy}"
    textColor: "{colors.dial-rose}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xxl}"
  footer-logo:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"

## Components

### Buttons
**`button-primary`** — Filled with `{colors.primary}` (#e0b1a4 dusty rose) and near-black text (`{colors.on-primary}`), this button reads as a warm accent punching out of the near-black canvas rather than a conventional CTA. The 12px uppercase monospace label at 1.8px letter-spacing (`{typography.button-md}`) and `{rounded.sm}` 4px corners give it a machined, production-part quality rather than a consumer-app glow. Active state steps to `{colors.primary-active}` (#dfa7b0); disabled desaturates to `{colors.primary-disabled}` with canvas-black text.

**`button-secondary`** — Transparent fill, 1px `{colors.ink}` border, same monospace uppercase label. Used wherever the dusty-rose fill would pull attention away from dial photography. Active state fills to `{colors.canvas-raised}` to register as pressed without adding color. Hover shifts border to `{colors.muted}` to signal interactivity at minimal voltage.

**`button-ghost`** — No border, no fill, `{colors.muted}` text in `{typography.button-sm}`. Used for dismiss actions, "Back" links, and inline controls in spec tables where structural weight would crowd the data grid.

### Navigation
**`nav-bar`** — 60px tall on a `{colors.canvas}` ground, separated from content by a single `{colors.hairline}` rule. All links render in `{typography.nav-link}` — 11px uppercase monospace at 1.2px letter-spacing — giving the bar an instrument-panel register rather than editorial warmth. The Studio Underd0g logotype uses `{typography.title-sm}` (13px uppercase, 0.8px tracking). Cart and account icons sit right-aligned; no mega-menu. The `announcement-bar` in `{colors.accent-burgundy}` / `{colors.dial-rose}` sits flush above it for drop dates and shipping notices.

### Product Card
**`product-card`** — Lives on `{colors.canvas-raised}` (#1c1c1c) with `{rounded.sm}` corners and `{spacing.md}` internal padding. A square dial photograph fills the top; below it, a `{typography.title-sm}` model name, a spaced `{typography.ref-number}` reference code in `{colors.muted}`, and a `{typography.price}` price. "Sold Out" and limited-edition states render as `{product-card-badge}`: `{colors.accent-orange}` (#ed762b) fill — the only saturated color on the card, so it registers as a genuine alert rather than a promotional flourish.

### Dial Swatches
**`dial-swatch`** — 32px circles used to select colorways on the PDP. Each variant maps directly to a dial color token (rose, pink, blue, khaki, sage), presenting the palette as a row of pure specimens. Selected state adds a 2px `{colors.ink}` ring; unselected has no border, letting the dial hue read without decoration. On mobile the swatch row scrolls horizontally below the hero image.

### Spec Table
**`spec-table`** — A two-column definition list on `{colors.canvas-raised}` with `{spacing.lg}` padding. Labels use `{typography.spec-label}` (10px uppercase, 1.2px tracking, `{colors.muted}`); values use `{typography.spec-value}` (13px monospace, `{colors.ink}`). Because both columns are monospace, a stack of values like "38.5 mm / 316L steel / 100 m" aligns with ledger-sheet precision. Rows are separated by `{spec-row-divider}` — a `{colors.hairline}` bottom rule plus `{spacing.sm}` vertical padding — with no zebra striping.

### Collection Badge
**`collection-badge`** — Labels limited series ("CHAPTER I", "ARCHIVE", "PROTO"). Deep burgundy background (`{colors.accent-burgundy}`, #33081c) with dusty rose text (`{colors.dial-rose}`), `{rounded.xs}` corners, and 4px/10px padding. It reads as an understated press stamp or edition mark rather than a retail promo callout — the combination of near-invisible background and muted accent text demands close reading.

### Announcement Bar
**`announcement-bar`** — A single-line strip pinned above the nav. `{colors.accent-burgundy}` background, `{colors.dial-rose}` text in `{typography.caption}`. Used sparingly for drop dates, shipping windows, and sell-out alerts. Dismissible with a `{button-ghost}` × icon. The burgundy/rose pairing is shared with `{collection-badge}`, creating a consistent limited-edition signal language across the site.

### Hero
**`hero`** — Full-viewport dark section with `{colors.canvas}` ground. Dial photography fills the left column; the right column holds a `{typography.display-xl}` headline (48px monospace, tight -0.5px tracking), a `{typography.body-md}` subhead in `{colors.muted}` at max-width 480px, and a `{button-primary}` CTA. On mobile the layout collapses to stacked: image first, text below. No autoplay video; any ambient motion is minimal, consistent with the archival product register.

### Footer
**`footer`** — `{colors.canvas}` ground with a single `{colors.hairline}` top rule and `{spacing.xxl}` vertical padding. Copy in `{typography.caption}` at `{colors.muted}`. Three-column desktop layout (brand links / social / legal); single-column on mobile. The logotype repeats in `{typography.nav-link}` at `{colors.ink}`. No decorative elements — the footer is a plain navigation table.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column throughout; dial swatches scroll horizontally below PDP image; spec table full-width with reduced label column; nav collapses to hamburger drawer + centered logo; hero stacked (image → text) |
| Tablet | 744–1128px | Two-column product grid; PDP remains single-column but spec table sits beside main image; full nav bar with overflow menu for secondary links |
| Desktop | 1128–1440px | Three-column product grid; PDP splits — image left, spec block + CTA right; hero runs full split-screen with bleed photography |
| Wide | > 1440px | Max content width 1400px centered with `{colors.canvas}` gutters; hero image bleeds to viewport edge; text block stays within container |

### Touch Targets
- All buttons minimum 48 × 48px
- Dial swatches: 32px visual, padded to 44 × 44px tap area
- Nav links: padded to 44px height on mobile in the drawer
- Cart and account icons: minimum 44 × 44px tap zone

### Collapsing Strategy
- Navigation: hamburger drawer at < 744px; links listed vertically in `{typography.nav-link}` with `{spacing.lg}` row height
- Product grid: 2-col at < 744px; 3-col at 744–1128px; 4-col at > 1128px
- Spec table: full-width at < 744px (label above value, stacked); 2-col definition layout at ≥ 744px
- Dial swatch row: horizontal scroll on mobile; wraps at ≥ 744px
- Footer: single-column stacked on mobile; 3-column grid on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed web font family — site reports `monospace` and `inherit` stacks only; an underlying licensed or custom mono typeface may be loaded via JS or a third-party CDN; all typography tokens use the generic `monospace` fallback
- Exact button corner radius and padding not measured from live DOM; values inferred from the micro-brand register and general Shopify theme conventions
- No hover or transition timing extracted (duration, easing, transform values unknown)
- Light-mode variant unknown — all colors assume dark-canvas default (meta theme-color: #000000)
- Exact nav height and announcement bar height not confirmed from live layout
- Icon set (cart, account, hamburger, social) not identified; glyph source and sizing unconfirmed
- Limited-edition badge copy conventions (series naming format, chapter numbering) inferred from brand positioning, not scraped from live product data
