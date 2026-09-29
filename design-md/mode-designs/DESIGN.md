---
version: alpha
name: "Mode Designs"
source_url: "https://modedesigns.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Ivyora Display headlines share page real estate with monospace specimen text at Mode Designs — an editorial serif sitting alongside a terminal font is a declaration of who the customer is: someone who cares that a stem has exactly 1.5mm of pre-travel and also that the product page reads beautifully. The primary action color, a particular steel-water blue (#338fb1), avoids the navy of enterprise software and the cerulean of consumer electronics — it is closer to the anodized aluminum of a machined top case photographed under diffused studio light. That blue lands against two dark grounds: an obsidian near-black (#121212) used for full-bleed hero sections and the global nav, and a forest-tinged dark green (#1c291f) deployed as a secondary surface layer — a color that reads like PCB soldermask or anodized board layer, which makes it feel native to the hardware rather than decorative. Cool silver-gray (#dedede) handles dividers and disabled states without introducing warmth, keeping the palette's temperature uniformly precise. Ivyora Text carries body copy and product narratives, but the brand interrupts with monospace wherever numbers need to register as technical fact: polling rates, actuation force, stem travel. The collision of elegant serif and clinical mono is the brand's primary typographic gesture — neither mode is decoration, both are load-bearing. Buttons and inputs carry minimal radii ({rounded.sm}, 4px) rather than the pill shapes common in consumer lifestyle brands; the geometry matches the chamfered edges and tight tolerances of the hardware itself. The dark nav persists sitewide, anchoring product photography — typically shot on neutral or gradient backgrounds — against a dark frame that makes anodized finish details pop on first load. Spacing is generous inside product cards but compressed in the nav, giving the layout a magazine quality on wide screens and a clean list feel on mobile.

colors:
  primary: "#338fb1"
  primary-active: "#2a7a9a"
  primary-disabled: "#a8d4e5"
  ink: "#121212"
  body: "#2d2d2d"
  muted: "#6b6b6b"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  dark-canvas: "#121212"
  dark-surface: "#1c291f"
  dark-surface-muted: "#243225"
  on-dark: "#ffffff"
  on-dark-muted: "#9db5a0"
  spec-accent: "#338fb1"

typography:
  display-xl:
    fontFamily: "'ivyora-display', serif"
    fontSize: 60px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'ivyora-display', serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.8px
  display-sm:
    fontFamily: "'ivyora-display', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'ivyora-text', serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'ivyora-text', serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'ivyora-text', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'ivyora-text', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'ivyora-text', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'ivyora-text', serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'ivyora-text', serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'ivyora-text', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  spec-mono:
    fontFamily: "monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.03em
  spec-mono-lg:
    fontFamily: "monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  price:
    fontFamily: "'ivyora-text', serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'ivyora-text', serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 46px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 46px
    border: "1px solid {colors.hairline}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 46px
    border: "1px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 46px
  nav-bar:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid rgba(255,255,255,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageBorderRadius: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    padding: "{spacing.md}"
  hero:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 80vh
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
  spec-row:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-mono}"
    valueColor: "{colors.spec-accent}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  spec-block:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.spec-mono-lg}"
    valueColor: "{colors.on-dark-muted}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.primary}"
    unselectedBorder: "2px solid {colors.hairline}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-sold-out:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    border: "1px solid {colors.hairline}"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 14px"
    border: "1px solid {colors.hairline}"
  sticky-atc:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    height: 64px
    padding: "0 {spacing.base}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark-muted}"
    linkColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.nav-link}"
    borderTop: "1px solid rgba(255,255,255,0.08)"
    padding: "{spacing.xxl} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"

## Components

### Buttons

**`button-primary`** — Uppercase spaced ivyora-text at 13px (0.08em tracking) over steel-water blue (#338fb1), 4px radius corners that read as engineered rather than friendly. Active state drops to #2a7a9a; disabled washes to #a8d4e5 with white text retained. Height 46px matches text-input exactly so CTAs and form rows share a common vertical rhythm.

**`button-secondary`** — White canvas fill, 1px hairline (#dedede) border, ink (#121212) text. Identical geometry to primary — same height, same radius, same typography — so the two can sit as a CTA pair without size discrepancy. Used for secondary configurator actions or "Learn More" contexts alongside a primary purchase CTA.

**`button-ghost`** — Transparent fill with 1px white border and white text, designed exclusively for dark sections (hero, spec-block, footer). Shares primary button typography and radius to keep a consistent system inside dark layouts. Does not appear on light-canvas pages where button-secondary serves the same structural role.

### Text Input

**`text-input`** — White canvas, 2px radius, 1px hairline border. Focus state shifts border to primary blue (#338fb1) with no shadow, keeping the interaction signal minimal. Placeholder in muted gray (#6b6b6b), body text in ink (#121212). Height 46px aligns with both button variants for clean horizontal form rows.

### Navigation

**`nav-bar`** — Full-width obsidian (#121212) bar, 64px tall, uppercase spaced nav-link text in white. Border-bottom at 8% white opacity creates a shelf separation without a hard line. The dark bar persists across all pages — including light-canvas collection pages — asserting the brand's dark ground as a constant frame rather than a section-specific mode.

### Product Card

**`product-card`** — White-near surface (#fafafa) with 1px hairline border and 2px radius. Product image sits flush to the top edge without inner padding; title uses title-sm (ivyora-text 15px medium), price uses the price token (ivyora-text 20px medium). No drop shadow — the thin border is the sole separation signal, keeping grids legible without visual noise. On hover, border color transitions to primary blue (#338fb1).

### Hero

**`hero`** — Full-bleed dark-canvas (#121212), minimum 80vh. Headline uses display-xl at weight 300 — the light stroke against dark is the canonical Mode Designs hero gesture, letting form and photography carry weight rather than heavy type. Subhead in body-md, white. An optional thin rule in primary blue (#338fb1) may appear above the headline as a brand-register marker.

### Spec Row & Spec Block

**`spec-row`** — Each keyboard specification gets a label in caption (12px muted gray) and a value in spec-mono (monospace 12px, primary blue #338fb1). Hairline bottom border, surface-soft (#f4f4f4) background. Deployed in product-page accordion panels for switch data, case dimensions, PCB revision, and layout notation — the blue monospace value signals technical precision rather than marketing language.

**`spec-block`** — Full-width dark-green (#1c291f) surface containing monospace spec summaries in on-dark-muted (#9db5a0). The PCB-green ground makes the technical data feel native to the hardware layer rather than a UI overlay. Used for feature-summary sections between hero and gallery on PDP.

### Color Swatch

**`color-swatch`** — 28px circles with 2px ring border; selected state uses primary blue ring, unselected uses hairline gray. 6px gap between swatches in a row. No inline label — color name appears in an adjacent text node that updates on selection. Selected state is the only place primary blue appears inside the light-canvas product configurator.

### Badges

**`badge-new`** — Primary blue (#338fb1) fill, white uppercase badge text (10px, 0.1em tracking), 2px radius. Positioned upper-left on product card image. **`badge-sold-out`** — Surface-soft fill, muted text, 1px hairline border, same geometry. Neither badge uses a pill shape — the rectangular read matches the hardware's angular aesthetic.

### Collection Filter

**`collection-filter`** — Small rectangular toggle (2px radius) for filtering by size, case material, or switch type. Inactive: white fill, hairline border, ink text. Active: primary blue fill, white text. Row sits beneath the nav on collection pages; on mobile the row becomes horizontally scrollable.

### Sticky Add-to-Cart

**`sticky-atc`** — 64px dark-canvas (#121212) bar that appears on scroll-past-hero on PDP. Product name left-aligned in title-sm, primary blue CTA right-aligned. Maintains the dark-nav aesthetic inside the active purchase flow without introducing a new color mode; on mobile the CTA expands to fill available width.

### Footer

**`footer`** — Dark forest green (#1c291f) ground with on-dark-muted (#9db5a0) body links and full-white heading text in nav-link style (uppercase, spaced). Hairline-white top border at 8% opacity. Three or four columns on desktop collapse to a single stack on mobile. Legal and policy links run as a secondary row beneath the column grid.

### Breadcrumb

**`breadcrumb`** — Caption-scale (12px, ivyora-text), muted gray separators, active node in ink. Sits immediately below the nav-bar on collection and product pages. Low visual weight keeps the navigation path readable without competing with product headline display type.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with dark-canvas full-height drawer; hero headline drops to display-md (40px weight 300); spec-rows stack label above value; sticky-atc CTA goes full-width; collection-filter row horizontally scrollable |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links, secondary overflow in a dropdown; hero at display-md; spec-block collapses to single column; footer two-column |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at display-xl (60px); two-column spec layout on PDP; spec-row accordion open by default alongside product image |
| Wide | > 1440px | Four-column product grid; content capped at ~1400px max-width with auto side margins; hero allows full-bleed background image with centered constrained content column |

### Touch Targets

- Minimum 44×44px for all interactive elements including color swatches (28px visual, 44px hit area)
- Nav links fill the full 64px bar height as their touch target
- Mobile sticky-atc button expands to full available width, minimum 52px height
- Collection filter pills expand horizontal padding on mobile (18px) versus desktop (14px)
- Breadcrumb links padded to 32px vertical touch area despite small visual size

### Collapsing Strategy

- Navigation: hamburger drawer at < 744px; drawer inherits dark-canvas background with full-width stacked uppercase links and 64px row height
- Product card: image aspect ratio locked at 4:3 across all breakpoints; title truncates to one line on grid view, expands fully on PDP
- Spec accordion: collapsed by default on mobile with chevron toggle; panels open by default on desktop where space allows side-by-side with imagery
- Spec-block: full-width on all breakpoints; interior monospace text wraps rather than truncates — line length is the spec's precision, not a display choice
- Footer: four columns → two at tablet → single stack at mobile; policy link row becomes horizontally scrollable on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was set, so nav and status-bar tinting on iOS Safari and Android Chrome is unconfirmed
- Only four hex values were extracted — intermediate grays between #dedede and #121212 and any warm neutrals are inferred, not confirmed from the live site
- Whether #1c291f is used as a sitewide dark-mode canvas or only as a section-level accent (spec-block, footer) is unconfirmed; the extraction does not distinguish context
- Exact font weights available in the ivyora-display and ivyora-text families are unconfirmed; weight 300 is assumed for display sizes based on typical editorial variable-font offerings for ivyora
- The split rule for when ivyora-display vs ivyora-text is used is inferred from naming convention and common editorial practice, not confirmed against live DOM inspection
- Monospace font identity is unconfirmed — may be a loaded web font, system-mono, or a specific coding font chosen to reinforce the keyboard context
- Hover transition durations, easing curves, and animation behavior are not extractable from static hints
- Price formatting conventions (tax, shipping notice, currency switcher) and their typographic treatment are not confirmed
- Product photography art direction (renders vs lifestyle, background treatment) not confirmed from extraction
- Any loyalty, group-buy, or interest-list UI patterns specific to keyboard enthusiast commerce are unverified
