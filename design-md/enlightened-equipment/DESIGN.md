---
version: alpha
name: "Enlightened Equipment"
source_url: "https://enlightenedequipment.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Bebas Neue — the condensed uppercase typeface borrowed from concert posters and streetwear — reappears here over ultralight sleeping quilts, and the collision is intentional. The brand treats visual weight exactly like pack weight: every ornament, gradient, and accent hue that couldn't justify its grams got cut. What survives is a two-anchor palette, charcoal (#444444) and ash (#eeeeee), applied with enough confidence that the absence of a third color reads as a decision rather than an omission. Bebas Neue handles all display work in uppercase at high size — section headers, CTAs, price figures — while body prose drops into a system sans at comfortable weight, the typographic equivalent of a hardshell over a baselayer. Buttons carry no radius to speak of; cards sit on the ash surface with a fine hairline border rather than elevation shadows; the whole system communicates function-first without ever announcing it. The signature interaction is the custom quilt configurator — an in-page selection flow for fill weight, shell fabric, and temperature rating — which demands a clean spec-chip component and a step-panel treatment that can surface dense technical data (fill power, baffle count, draft collar presence) without visual clutter. `{rounded.xs}` is the maximum curvature applied to interactive elements; `{rounded.none}` governs most structural containers. Navigation is low-profile: a single horizontal bar in charcoal on white, Bebas labels at reduced tracking, no mega-menu imagery. The footer inverts to a dark surface (`{colors.surface-dark}`) that creates a bookend to the ash-and-white body, and weight-spec badges — the ultralight community's primary purchase signal — appear as tight monospace chips in `{colors.surface-soft}` with `{typography.spec-label}` uppercase tracking. There is no primary accent beyond charcoal itself; every call to action is the brand color.

colors:
  primary: "#444444"
  primary-active: "#2a2a2a"
  primary-disabled: "#aaaaaa"
  ink: "#1a1a1a"
  body: "#444444"
  muted: "#888888"
  hairline: "#cccccc"
  hairline-soft: "#e4e4e4"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-dark: "#2a2a2a"
  on-primary: "#ffffff"
  on-dark: "#eeeeee"
  spec-chip-bg: "#eeeeee"
  spec-chip-text: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "'Bebas Neue', Impact, 'Arial Narrow', sans-serif"
    fontSize: 80px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: 1.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Bebas Neue', Impact, 'Arial Narrow', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 0.96
    letterSpacing: 1px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Bebas Neue', Impact, 'Arial Narrow', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.8px
    textTransform: uppercase
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.9px
    textTransform: uppercase
  price:
    fontFamily: "'Bebas Neue', Impact, 'Arial Narrow', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Bebas Neue', Impact, 'Arial Narrow', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Bebas Neue', Impact, 'Arial Narrow', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1px
    textTransform: uppercase
  nav-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  configurator-step:
    fontFamily: "'Bebas Neue', Impact, 'Arial Narrow', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.8px
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focus-border: "1.5px solid {colors.primary}"
    placeholder-color: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
    logoColor: "{colors.ink}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    padding: "{spacing.base}"
    imageBg: "{colors.surface-soft}"
  spec-chip:
    backgroundColor: "{colors.spec-chip-bg}"
    textColor: "{colors.spec-chip-text}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
  hero-product:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: button-primary
    minHeight: 560px
    layout: split-50-50
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    stepTypography: "{typography.configurator-step}"
    labelTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    activeStepAccent: "{colors.primary}"
  fill-option-selector:
    backgroundColor: "{colors.surface-soft}"
    selectedBg: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1.5px solid {colors.primary}"
    padding: "12px 16px"
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    selectedRingColor: "{colors.primary}"
    selectedRingWidth: 2px
    selectedRingOffset: 2px
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rowAltBg: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  category-tag:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.spec-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.title-sm}"
    optionTypography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    checkboxAccent: "{colors.primary}"
    width: 220px
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.spec-label}"
    headingColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.surface-soft}"
    borderTop: none
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Solid charcoal (#444444) block with Bebas Neue uppercase labels at 18px and 1.5px letter-spacing; `{rounded.xs}` (4px) is the only curvature applied. On press, background deepens to `{colors.primary-active}` (#2a2a2a) with no scale or shadow animation — the brand avoids motion theater. Disabled state uses `{colors.primary-disabled}` gray and `cursor: not-allowed`.

**`button-secondary`** — White fill with a 1.5px charcoal border and matching Bebas Neue label in `{colors.primary}`; on hover the background shifts to `{colors.surface-soft}` ash. Maintains the same 48px height as primary so the two sit flush in horizontal CTA pairs without alignment math.

**`button-text`** — Transparent background, charcoal text in `{typography.button-sm}`, underlined. Used for secondary actions in the configurator flow (e.g., "Compare fill weights") where a bordered button would crowd the step layout.

### Spec Chips

**`spec-chip`** — The ultralight community reads grams and fill-power numbers before price. These small chips (`{rounded.xs}`, 1px hairline border on `{colors.surface-soft}`) carry labels like "850 FP", "400g", "20°F" in `{typography.spec-label}` uppercase tracking. They cluster beneath product titles on cards and in the sidebar of the configurator panel. Never use a colored background variant — the monochrome treatment preserves scannability across many chips at once.

### Configurator Panel

**`configurator-panel`** — The brand's signature interaction. A full-width step-based selector (no border-radius, plain 1px hairline container) walks the customer through fill weight → shell fabric → size → color, with each active step header rendered in `{typography.configurator-step}` Bebas Neue at 22px. Inactive steps collapse to their spec-label heading. The active fill option uses `fill-option-selector` with charcoal background and white text; unselected options remain ash. No progress bar — steps are numbered in plain `{typography.spec-label}`.

### Navigation

**`nav-bar`** — 60px tall, white background, 1px bottom border in `{colors.hairline}`. The wordmark renders in `{typography.display-sm}` Bebas Neue at ink color — no logomark, no icon, just the condensed uppercase type. Category links use `{typography.nav-label}` system sans at 13px/500 weight. No hover underline animation; a simple color shift to `{colors.primary-active}` on hover.

**`announcement-bar`** — A 36px charcoal strip pinned above the nav carrying shipping thresholds or seasonal notices in `{typography.spec-label}` white uppercase. This is the only branded charcoal surface in the header zone; it creates a strong top-of-page anchor.

### Product Card

**`product-card`** — No drop shadow, no border-radius; a 1px hairline border on a white card against the ash page background defines the container edge. Product image fills the top on `{colors.surface-soft}` (ash, matching the page), maintaining consistent negative-space tone. Title in `{typography.title-md}`, price in `{typography.price}` Bebas Neue at 28px below. Spec chips cluster immediately below the title in a wrapping flex row.

### Hero

**`hero-product`** — Split 50/50 layout: product photography on the left against `{colors.surface-soft}` ash, editorial copy on the right against white canvas. Headline runs `{typography.display-xl}` Bebas Neue at 80px/0.92 line-height — the compressed vertical rhythm is intentional for long product names like "Revelation Quilt 20°". The CTA uses `button-primary` at full width on mobile.

### Footer

**`footer`** — Inverts to `{colors.surface-dark}` (#2a2a2a) with `{colors.on-dark}` ash text; this dark bookend gives the page visual closure without introducing a new brand color. Column headings in `{typography.spec-label}` uppercase; links in `{typography.body-sm}` system sans. No social icon imagery beyond Font Awesome glyphs at `{colors.on-dark}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; hero stacks image above copy; nav collapses to hamburger icon + wordmark; configurator steps go full-width accordion; filter sidebar becomes a bottom-sheet drawer; spec chips wrap freely |
| Tablet | 744–1128px | Product grid shifts to 2-column; hero retains split layout at reduced image proportion (40/60); nav shows top-level categories, hides sub-items behind dropdowns; configurator panel uses 2-column step + preview layout |
| Desktop | 1128–1440px | Full 3–4 column product grid; hero at full 50/50 split with 80px display headline; filter sidebar fixed-left at 220px beside product grid; nav shows all top-level items with hover dropdowns |
| Wide | > 1440px | Max content width capped at ~1400px with auto side margins; hero image expands but copy column stays constrained to ~520px for legibility; section padding increases to `{spacing.section}` |

### Touch Targets

- All interactive controls minimum 44×44px on mobile
- `fill-option-selector` minimum 48px height on touch viewports
- `color-swatch` expands to 36px diameter on touch (from 28px desktop)
- Nav hamburger target area 48×48px with visual icon at 24px

### Collapsing Strategy

- Filter sidebar collapses to a sticky "Filter" button triggering a bottom-sheet at < 744px
- Configurator steps collapse to a single-step accordion; inactive steps show only heading + selected summary value
- Spec chip rows truncate to 3 chips + "+N more" on product cards at mobile widths
- Footer 4-column layout collapses to single-column stacked accordions on mobile; dark background retained

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two hex values were extracted (#444444 and #eeeeee); all mid-tone grays, error states, and hover intermediaries are derived systematically and not confirmed from live site inspection
- Body text font family not identified — Bebas Neue is confirmed for display; body stack assumed to be an unbranded system sans (fallback -apple-system / Roboto); actual webfont may differ
- No accent or alert color was extractable; error and success states are unconfirmed — a standard red/green pair should be verified against the live form validation UI
- No meta theme-color was set, so mobile browser chrome color is unconfirmed
- No confirmed spacing scale, shadow tokens, or z-index layers — all derived from category conventions
- Configurator interaction states (step transitions, selection animations, validation styling) require direct inspection of the live configurator flow
- Dark mode support unknown; no `prefers-color-scheme` media query evidence in extracted data
