---
version: alpha
name: "Lutron"
source_url: "https://www.lutron.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every Lutron control surface is engineered to vanish — flush-mounted keypads in architectural finishes, dimmers that slide without printed labels, apps that mirror the stillness of a properly lit room. The digital expression carries this same discipline. A near-black navy (#0a0e17) dominates hero sections and system-selector panels, implying the enclosure of a well-appointed room rather than the brightness the products command. Against that dark field, warm amber (#e07830) performs exactly the function of a dimmed sconce: it draws the eye to precisely one thing at a time, appearing only on primary CTAs, active navigation states, and product callout moments. The contrast is architectural — dark ground, warm signal.

  Typography runs in a clean geometric sans-serif at conservative weights. Display headings sit at 48px in fontWeight 300, never the heavy 700+ that consumer electronics reach for; Lutron trusts room-scene photography over typographic aggression. Body copy holds at 16px/400 in mid-gray (#5a6475) against white canvas, legible and unhurried. Navigation links and spec labels use tracked uppercase at 11–12px, a cue borrowed from interior design catalogs rather than e-commerce.

  Shape language is low-radius but precise: product cards use {rounded.sm} (8px), modals sit at {rounded.md} (12px), and the only fully rounded element is the small product-line pill badge used to distinguish Caséta, RA2 Select, and Homeworks QS. There are no soft-blob or bubbly UI patterns; every corner radius reads as precision-manufactured rather than friendly-consumer.

  The professional-residential split governs layout decisions throughout. A persistent system-selector — Homeworks QS, RA2 Select, Caséta Wireless — appears high on every product category page, acting as a faceted filter that narrows the component tree below. Room-scene photography positions Lutron hardware at the vanishing point of a frame rather than center-stage, staging the promise that the product disappears into life. Partner ecosystem logos (Apple Home, Google Home, Amazon Alexa, JOSH.ai) appear in a horizontal lockup with hairline borders and controlled spacing, communicating ecosystem breadth without visual noise.

colors:
  primary: "#e07830"
  primary-active: "#c5611a"
  primary-disabled: "#f0c8a0"
  primary-hover: "#d06820"
  ink: "#0a0e17"
  body: "#2d3340"
  muted: "#5a6475"
  hairline: "#e2e4e9"
  hairline-soft: "#f0f1f3"
  canvas: "#ffffff"
  surface-soft: "#f5f6f8"
  surface-card: "#ffffff"
  surface-dark: "#0a0e17"
  surface-dark-secondary: "#151c2b"
  surface-dark-elevated: "#1e2636"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-muted: "#9da8bc"
  amber-glow: "#f5a623"
  system-caseta: "#5b9bd5"
  system-ra2: "#7c5cbf"
  system-homeworks: "#2a7a5a"

typography:
  display-xl:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  overline:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.36
    letterSpacing: 1.2px
    textTransform: uppercase
  system-label:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.2px
  button-md:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Neue Haas Grotesk', 'Aktiv Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-secondary-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.on-dark}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 0px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageAspectRatio: "4/3"
  system-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.system-label}"
    rounded: "{rounded.none}"
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
    height: 48px
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.on-dark-muted}"
    padding: "80px 0"
  hero-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.muted}"
    padding: "80px 0"
  system-badge-caseta:
    backgroundColor: "{colors.system-caseta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.system-label}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    height: 24px
  system-badge-ra2:
    backgroundColor: "{colors.system-ra2}"
    textColor: "{colors.on-primary}"
    typography: "{typography.system-label}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    height: 24px
  system-badge-homeworks:
    backgroundColor: "{colors.system-homeworks}"
    textColor: "{colors.on-primary}"
    typography: "{typography.system-label}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    height: 24px
  spec-callout:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    valueTypography: "{typography.spec-value}"
    labelTypography: "{typography.overline}"
    labelColor: "{colors.on-dark-muted}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl} {spacing.lg}"
  works-with-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
  feature-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} 0"
  feature-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} 0"
  room-scene-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    overlayGradient: "linear-gradient(to top, rgba(10,14,23,0.85) 0%, transparent 50%)"
    imageAspectRatio: "16/9"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark-muted}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    columnHeaderTypography: "{typography.overline}"
    padding: "{spacing.xxl} 0 {spacing.xl}"

## Components

### Buttons

**`button-primary`** — A flat amber rectangle using {colors.primary} (#e07830) with no border-radius whatsoever. 48px tall, 14px label in fontWeight 600 with slight 0.3px tracking. On hover the fill deepens to {colors.primary-hover} (#d06820); on active press it shifts to {colors.primary-active} (#c5611a). Used for "Shop Now," "Get a Quote," and primary configurator CTAs. On dark hero sections the amber button appears identically — warm light against a dark field, which is the entire brand metaphor made literal.

**`button-secondary`** — Outline-only with 1px solid {colors.ink} border on light backgrounds, same squared geometry and 48px height as primary. The `button-secondary-on-dark` variant flips border and text color to {colors.on-dark} for use against {colors.surface-dark} hero panels. Neither button type uses corner radius — the squared edge communicates precision hardware, not soft consumer apps.

**`button-ghost`** — Text-only in {colors.primary}, no border or fill, 14px/600. Used for secondary actions ("Learn more," "See full specs") inside specification panels where a bordered button would add visual weight to an already-dense information zone.

### Nav Bar

**`nav-bar`** — 72px tall, white {colors.canvas}, {typography.nav-link} (14px/500). The Lutron wordmark sits left-aligned. At desktop widths a mega-menu drops on hover over product category links; no pill or underline active state — a color shift to {colors.primary} amber is the only hover signal. On pages with dark hero sections, `nav-bar-dark` activates: same structure, {colors.surface-dark} background, all text reversed to {colors.on-dark}. The nav never uses a sticky behavior on product-detail pages — it scrolls away and leaves room photography uninterrupted.

**`nav-dropdown`** — A wide mega-panel at full viewport width capped at 1280px, dropping below the nav bar with {rounded.sm} corners and a 12px drop-shadow. Columns organize products by line (Caséta, RA2 Select, Homeworks QS), each headed by a system-badge pill and a short descriptor in {typography.caption}. A right column shows room-category photography thumbnails with {rounded.xs} corner cuts, softening the otherwise grid-rigid layout without breaking the architectural tone.

### Product Card

**`product-card`** — White {colors.surface-card} background, 1px {colors.hairline} border, {rounded.sm} corners. Product image fills a 4:3 zone at top; below sit a system-badge pill, product name in {typography.title-sm}, and a short feature list in {typography.body-sm}/{colors.muted}. On hover, the card lifts with `box-shadow: 0 4px 16px rgba(0,0,0,0.08)`. There is no "Add to cart" button — Lutron sells through professional dealers, so the CTA is always "Learn more" or "Find a dealer," which renders as `button-ghost` rather than `button-primary`.

### System Selector

**`system-selector`** — A horizontal tab strip sitting immediately below the hero on product category pages. Each tab uses {typography.system-label} (12px uppercase, 0.8px tracking). The active tab renders {colors.primary} text with a 2px amber underline; inactive tabs are {colors.muted}. The strip sits flush on {colors.surface-soft} with no card or radius treatment — it reads as a ruled divider from a product specification sheet. Selecting a tab filters the product grid below client-side.

### Hero

**`hero-dark`** — Full-width dark panel using {colors.surface-dark} (#0a0e17). Headline in {typography.display-xl} (48px/300/white); the 300 fontWeight is deliberate — architectural rather than punchy. Subtitle in {typography.body-md} rendered in {colors.on-dark-muted} (#9da8bc). Two CTAs appear side by side: `button-primary` (amber) left, `button-secondary-on-dark` right. Room-scene photography bleeds into the right 50% of the layout at desktop widths. Vertical padding is 80px top and bottom, giving the photography room to breathe.

**`hero-light`** — Same structural rules as `hero-dark` but canvas is {colors.surface-soft} and text flips to {colors.ink}. Used for product-line landing pages where photography is studio-shot against white rather than architectural in situ.

### Spec Callout

**`spec-callout`** — A dark elevated panel using {colors.surface-dark-elevated} (#1e2636), presenting technical metrics: number of zones, supported load types, wattage ranges. Each metric renders with a large {typography.spec-value} (28px/300) in white and a {typography.overline} label in {colors.on-dark-muted} below. Multiple blocks arrange in a 3- or 4-column row separated by thin vertical hairlines at 20% opacity. No radius ({rounded.none}) — the hard edge reinforces a specification-sheet register. This component is unique among DTC lighting brands for treating technical specs as a hero visual element rather than burying them in a table.

### Room Scene Card

**`room-scene-card`** — A 16:9 image container with {rounded.md} corners and a bottom-anchored gradient overlay (linear-gradient from {colors.surface-dark} at 85% opacity to transparent at 50%). Room name and control category appear in {typography.title-md} white over the gradient zone. Used in lifestyle galleries and scene-selection panels within the Lutron app promotional sections. The {rounded.md} here is one of the few places radius softens the UI — indicating consumer aspiration rather than specification rigor.

### Works With Badge

**`works-with-badge`** — A compact white container with 1px {colors.hairline} border showing partner ecosystem logos (Apple Home, Google Home, Alexa, JOSH.ai). Partner name in {typography.caption}/{colors.muted}. Badges arrange in a single horizontal row with {spacing.sm} gap. All partner logos render in grayscale to keep the palette controlled — color appears only on the Lutron amber primary, never on third-party brands within the same view.

### Feature Table

**`feature-table-row`** and **`feature-table-row-alt`** alternate for zebra-striping on product comparison and specification tables. Each row uses {typography.body-sm} at {colors.body}, thin {colors.hairline-soft} border-bottom. The left label cell renders fontWeight 600; the right value cell uses fontWeight 400. Checkmarks render in {colors.primary} amber; X marks render in {colors.muted}. No border-radius on the table — specification tables read as technical documents, not UI cards.

### Footer

**`footer`** — Full-width dark canvas at {colors.surface-dark}. Four-column link grid in {typography.caption}/{colors.on-dark}. Column headers in {typography.overline}/{colors.on-dark-muted}. Legal copy and copyright in {typography.caption} at 80% opacity. The Lutron wordmark repeats in white at the footer's left anchor. Social icons are 24×24px outline-style in {colors.on-dark-muted}, shifting to {colors.on-dark} on hover. No card or box treatment — the footer is a flat dark field that closes the page the same way the hero opens it.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger with full-screen {colors.surface-dark} overlay drawer. System-selector tabs scroll horizontally with touch overflow. Hero stacks image above headline. Spec callout reduces to 2-across with horizontal scroll hint for additional blocks. Product card grid goes 1-column. Works-with badges wrap to 2-row grid. |
| Tablet | 744–1128px | Two-column product card grid. Nav retains wordmark plus compact icon row (no mega-menu, sheet instead). Hero at 60/40 text/image split. Spec callout runs 2-column. System-selector tabs scroll if overflow. |
| Desktop | 1128–1440px | Three-column product card grid. Full mega-menu nav on hover. Hero at 50/50. Spec callout at 4-column. System-selector as full tab strip. |
| Wide | > 1440px | Content capped at 1280px centered. Hero and footer extend edge-to-edge at full dark/soft background; inner content grid stays at 1280px. Product grid holds at 3 columns with increased card padding. Room-scene gallery goes 4-column. |

### Touch Targets

- All buttons minimum 48×48px tap target regardless of visual size
- System-selector tabs minimum 44px height with 16px horizontal padding each side
- Nav hamburger icon minimum 44×44px hit area
- Product card tap target covers the full card surface, not just the label zone
- Works-with badges minimum 36px height; stack vertically if horizontal row causes crowding below 375px viewport width

### Collapsing Strategy

- Mega-menu collapses to full-screen dark drawer at < 1128px; drawer stacks product-line sections vertically with expand/collapse chevrons in {colors.on-dark-muted}
- Hero 50/50 split becomes single-column stacked at < 744px; image moves above headline on mobile for immediate visual context
- Spec callout 4-column → 2-column at tablet → horizontal scroll strip on mobile with each block min-width 160px and snap-scroll behavior
- Feature comparison table gets a horizontal scroll container with the left label column position-sticky at mobile breakpoints
- Footer 4-column → 2-column at tablet → single accordion-style column on mobile with expand/collapse per section; legal row always visible

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted**: lutron.com appears to load design tokens via JavaScript or is behind anti-bot protection; zero colors were captured by the extraction pass. All palette values above derive from brand knowledge and widely-observed visual identity (dark navy hero backgrounds, amber/orange CTAs). Treat as approximate until a live pixel sample is taken.
- **No font stack extracted**: Typography family is inferred from visual inspection of the site as likely Neue Haas Grotesk or a similar precision geometric sans-serif. Actual font name, weights, loading method (WOFF2, Adobe Fonts, self-hosted), and any custom variable-font axes are unknown.
- **System-line brand colors**: The Caséta blue (#5b9bd5), RA2 Select purple (#7c5cbf), and Homeworks green (#2a7a5a) are approximations based on product photography and badge treatments observed on the site. These must be verified against official Lutron brand guidelines before use.
- **Professional portal (myLutron)**: Lutron serves both residential consumers (Caséta) and commercial/high-end residential integrators (Homeworks QS). This design system reflects the consumer-facing marketing site; the authenticated dealer and integrator portal likely carries a distinct component set with denser data tables, project management UI, and a different type hierarchy.
- **In-app UI tokens**: The Lutron Home app (iOS/Android) uses a dark-mode-first interface with animated scene sliders, fade-curve controls, and a time-schedule picker that are brand-distinctive interaction surfaces. Slider, scene-picker, and schedule-timeline tokens are not captured here.
- **Interactive configurator**: The "Which system is right for me?" multi-step product-selector tool on the site has significant UI surface area with step indicators, animated transitions, and conditional branching logic; its specific visual tokens were not extractable from the static pass.
