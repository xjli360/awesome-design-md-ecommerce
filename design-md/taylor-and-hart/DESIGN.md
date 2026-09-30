---
version: alpha
name: "Taylor & Hart"
source_url: "https://www.taylorandhart.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  GT Sectra Fine's narrow ink-trap serifs carry display type at sizes where most fine-jewelry brands would reach for a generic didone — that specific editorial serif choice is the clearest signal that Taylor & Hart means bespoke in its typographic grammar as much as in its stones. Every content surface rests on a warm cream (#fcf6ea, #fefcf8) that reads closer to premium paper stock than digital white, setting ring photography against a background that signals physical workshop rather than sterile studio. Navy (#334e80) is rationed to CTA surfaces only — a single confident button color kept clear of the palette's warmer accents, so there is no ambiguity about where to click inside the multi-step ring configurator. Effra, a geometric humanist with open counters, manages the cognitive load of a bespoke flow — metal choice, stone shape, carat, engraving — across form steps that must feel unhurried even while carrying dense decision trees. Accent tokens branch across occasion: gold (#e7d698) and blush (#e5c7c6) for warmth; sage (#d7e0db) and forest (#1b3a2e) for contemporary naturalism; deep mauve (#703952) for intimate ceremony. Crimson (#da0039) appears only for sale callouts and error validation, isolated so its urgency reads instantly. TH Icons — the brand's proprietary glyph set — takes ring-style selector icons out of generic symbol libraries and into a vocabulary that belongs only to this configurator. Radii stay near zero on product cards and form inputs (`{rounded.xs}` at 4px), ensuring ring imagery rather than interface geometry commands attention; filter pills and swatch selectors take `{rounded.full}` to signal interactivity without visual noise.

colors:
  primary: "#334e80"
  primary-active: "#34489b"
  primary-disabled: "#9c9c9a"
  ink: "#4a4e54"
  body: "#4b4a49"
  muted: "#71706f"
  muted-soft: "#9c9c9a"
  hairline: "#c8c8c8"
  hairline-soft: "#eae9e8"
  canvas: "#fefcf8"
  surface-soft: "#f9f9f9"
  surface-card: "#fcfcfb"
  surface-warm: "#fcf6ea"
  surface-cream: "#efeee3"
  on-primary: "#ffffff"
  footer-text: "#dfdfde"
  accent-red: "#da0039"
  accent-gold: "#e7d698"
  accent-blush: "#e5c7c6"
  accent-sage: "#d7e0db"
  accent-forest: "#1b3a2e"
  accent-mauve: "#703952"
  accent-peach: "#efcaad"
  scrim: "#4a4e54"

typography:
  display-xl:
    fontFamily: "'GT Sectra Fine', 'Times New Roman', Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GT Sectra Fine', Georgia, serif"
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT Sectra Fine', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'GT Sectra Fine', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Effra', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Effra', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Effra', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'Effra', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Effra', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  caption-label:
    fontFamily: "'Effra', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 0.8px
    textTransform: uppercase
  step-label:
    fontFamily: "'Effra', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Effra', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Effra', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.4px
  nav-link:
    fontFamily: "'Effra', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0.1px
  price:
    fontFamily: "'Effra', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  price-lg:
    fontFamily: "'GT Sectra Fine', Georgia, serif"
    fontSize: 30px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  testimonial-body:
    fontFamily: "'GT Sectra Fine', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    fontStyle: italic

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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  button-appointment:
    backgroundColor: "{colors.accent-forest}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 24px rgba(74,78,84,0.10)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "1:1"
    padding: "{spacing.base}"
  hero-section:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
  ring-builder-step-indicator:
    activeColor: "{colors.primary}"
    completedColor: "{colors.accent-sage}"
    inactiveColor: "{colors.hairline}"
    labelTypography: "{typography.step-label}"
    labelColor: "{colors.muted}"
    activeLabelColor: "{colors.ink}"
  ring-builder-swatch:
    size: 40px
    rounded: "{rounded.full}"
    activeBorder: "2px solid {colors.primary}"
    inactiveBorder: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  ring-builder-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  price-display:
    typography: "{typography.price-lg}"
    textColor: "{colors.ink}"
    mutedColor: "{colors.muted}"
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  trust-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    iconColor: "{colors.accent-gold}"
    typography: "{typography.caption}"
    titleTypography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 18px"
    border: "1px solid {colors.hairline}"
    activeBg: "{colors.primary}"
    activeText: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  testimonial-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    quoteTypography: "{typography.testimonial-body}"
    attributionTypography: "{typography.caption-label}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  consultation-banner:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.footer-text}"
    headingTypography: "{typography.caption-label}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    borderTop: "2px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Navy (#334e80) fill on {rounded.xs} rounded corners, 48px tall, Effra Medium at 15px with 0.5px letter-spacing for legibility at small sizes. Hover transitions to the slightly deeper #34489b (`button-primary-active`); disabled state drops to the neutral gray (`{colors.primary-disabled}`) to signal unavailability without aggressive visual treatment. Used exclusively for high-commitment actions: "Start Designing," "Add to Cart," "Book Consultation."

**`button-secondary`** — Outlined variant in navy on the warm canvas. A 1px navy border against #fefcf8 gives a presence without competing with product photography. On hover, the border weight increases and background shifts to surface-warm (#fcf6ea) to acknowledge the interaction.

**`button-ghost`** — Underlined text-link style in ink (#4a4e54) for low-commitment actions like "View more," "Read our story," and inline prose calls-to-action. No border, no background — relies on the underline alone.

**`button-appointment`** — Forest green (#1b3a2e) CTA reserved for consultation and appointment booking flows. Visually distinct from the navy primary so users can immediately differentiate transactional from relational actions without reading copy.

### Inputs

**`text-input`** / **`select-input`** — 1px hairline border (#c8c8c8) at rest, 48px height, 4px radius, Effra Regular 16px body type. On focus the border upgrades to navy (`{colors.primary}`) with no fill change, keeping the warm canvas visible throughout the bespoke form flow. Used across ring builder step forms, checkout address fields, and email capture modules.

### Navigation

**`nav-bar`** — 72px warm canvas bar with a whisper-thin bottom border in hairline-soft (#eae9e8). Effra at 14px, 0.1px letter-spacing in ink for nav links. The brand wordmark in GT Sectra Fine sits center or left depending on viewport. A "Start Designing" CTA in `button-primary` anchors the right side on desktop, collapsing to a hamburger on mobile. The `nav-dropdown` appears as a floating panel below the bar with 24px horizontal padding and a subtle shadow, organizing ring categories with editorial imagery at left and text links at right.

### Product Card

**`product-card`** — Near-white (#fcfcfb) surface with a 1px soft hairline border and 4px radius. Square-crop ring image occupies the full card width at 1:1 ratio. Ring name renders in `{typography.title-sm}` (Effra 15px medium), price in `{typography.price}` (Effra 18px regular) directly below. A `sale-badge` in crimson (#da0039) overlays the image top-left when promotional pricing applies — the only time that accent fires in the listing grid.

### Ring Builder

**`ring-builder-step-indicator`** — Horizontal step rail using custom TH Icons glyphs for each configurator stage (silhouette, metal, stone, band, engraving). Active step renders in navy (#334e80), completed steps in sage (#d7e0db), future steps in hairline gray. Step labels in `{typography.step-label}` (Effra 12px, uppercase, 1px tracking) sit beneath each glyph. The rail anchors the top of the configurator viewport and remains sticky on desktop.

**`ring-builder-swatch`** — 40px circular swatches on {rounded.full} for metal color and stone selection. Active state shows a 2px navy border offset from the swatch edge; inactive shows 1px hairline. Swatches are spaced {spacing.sm} apart in a wrapping flex row, with Effra caption-label text beneath each cluster.

**`ring-builder-panel`** — The right-hand configurator drawer on desktop. Surface-soft (#f9f9f9) background with a 1px soft hairline border and 8px radius. Interior padding is {spacing.xl} (32px) on all sides. Panel title in `{typography.title-md}`, selection descriptions in `{typography.body-sm}`. The live price display in `{typography.price-lg}` (GT Sectra Fine 30px) anchors the panel footer above the primary CTA.

### Badges and Trust

**`trust-badge`** — Used in a horizontal trust strip beneath the hero and in the ring builder panel. Warm cream (#fcf6ea) background, custom TH Icon in accent-gold (#e7d698) at left, title in `{typography.title-sm}`, supporting text in `{typography.caption}`. Common instances: "30-Day Returns," "GIA Certified," "Lifetime Resize."

**`sale-badge`** — Crimson (#da0039) on white text, Effra 11px uppercase with 0.8px tracking. Appears sparingly — only over product photography or adjacent to a price when a promotional discount applies. The color's rarity in the UI is intentional: it must read as urgent information, not brand decoration.

### Testimonial Card

**`testimonial-card`** — Warm cream (#fcf6ea) background at {rounded.sm}. Quote in GT Sectra Fine italic (`{typography.testimonial-body}`), 20px at 1.5 line-height — the font's high-contrast strokes give hand-written weight to customer stories. Couple name and wedding date in `{typography.caption-label}` (Effra uppercase). Cards appear in a horizontal carousel with 24px column gaps.

### Consultation Banner

**`consultation-banner`** — Full-width band in surface-cream (#efeee3), title in `{typography.display-md}` (GT Sectra Fine 28px), body in `{typography.body-md}`. A `button-appointment` forest-green CTA sits beneath. Used to promote the in-person design consultation service between collection pages and checkout flows.

### Footer

**`footer`** — Charcoal (#4a4e54) background, footer-text (#dfdfde) for all copy. Column headings in `{typography.caption-label}` (Effra uppercase 11px). Links in `{typography.body-sm}`. A 2px navy border-top marks the footer entry point. Social icons use TH Icons glyphs in footer-text color, softening on hover to full white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column ring grid. Ring builder collapses into a full-screen step-by-step modal — one decision per screen. Nav bar hides all text links behind hamburger. Swatch rows scroll horizontally. Hero headline drops from display-xl to display-lg. Trust strip stacks vertically. |
| Tablet | 744–1128px | Two-column ring grid. Ring builder splits into a sticky sidebar (40%) and media viewer (60%). Nav reveals top-level categories but hides secondary dropdowns behind tap. |
| Desktop | 1128–1440px | Three-column ring grid. Full ring builder with sticky step rail at top, three-column layout (media / options / price panel). Mega-menu dropdown on hover for ring categories. |
| Wide | > 1440px | Grid expands to four columns. Hero content max-width capped at 1280px with auto side margins. Ring builder panel max-width 400px to prevent overstretch on ultra-wide. |

### Touch Targets

- All swatches minimum 40px — confirmed by ring-builder-swatch size definition
- Nav hamburger and close icon minimum 44×44px tap area
- Filter pills minimum 36px tall with 18px horizontal padding meeting 44px combined tap comfort
- Step indicator glyphs padded to 44×44px touch areas despite visual size

### Collapsing Strategy

- Ring builder transitions from split-pane (desktop) → tabbed sections (tablet) → full-screen modal steps (mobile)
- Mega-menu nav collapses to accordion drawer on mobile; top-level items remain visible as tappable rows
- Trust badge strip reflows from horizontal row to 2×2 grid at tablet, single column at mobile
- Testimonial carousel reduces to single-card with swipe gesture on mobile
- Footer four-column layout reduces to two columns at tablet, single accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact CTA radius could not be confirmed from extraction — using 4px (`{rounded.xs}`) based on visible product-card border-radius behavior; may be 0px for a fully sharp edge
- `Parcel` font from the font stack is undocumented publicly; role and usage weight not determinable from extraction alone — omitted from typography tokens
- Hover/focus transition duration and easing curves not extractable; 200ms ease assumed as industry baseline
- Ring builder step-indicator exact glyph set and TH Icons codepoints are proprietary and not publicly documented
- Dark mode or alternate theme variants (if any) not visible from extracted data
- Mobile ring builder modal transition style (slide-up vs. fade) not confirmed
- Grid gap values for ring listing page not extracted — 16px base assumed
