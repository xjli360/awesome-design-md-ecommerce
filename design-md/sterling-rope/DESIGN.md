---
version: alpha
name: "Sterling Rope"
source_url: "https://sterlingrope.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A climbing rope manufacturer that wears its technical confidence in a near-black #130c0d canvas and a single, unapologetic signal of #f3ce00 — a marigold yellow that appears on rope sheaths, safety warnings, and primary CTAs with the same functional urgency as a rescue whistle. The brand lives in a world of high-contrast utility: #130c0d ink against #f5f1e2 warm-cream surfaces, with #343741 charcoal as the secondary structural color for nav bars and footer blocks. Yellow (#f3ce00) is never decorative — it marks the actionable, the critical, the "pull here" moment. Typography runs on neue-haas-grotesk-text, a clean neo-grotesk that reads as precise but not cold, set at modest weights (400–600) with generous line-height to preserve readability in low-light or gloved conditions. Rounded corners are restrained — {rounded.xs} on buttons, {rounded.sm} on cards — suggesting molded plastic hardware rather than soft UI. The extracted palette includes outlier tones (#accef7, #d14343, #1a5632) that likely belong to partner badges, safety icons, or seasonal collections; the core system is disciplined around the black-yellow-cream triad. Product imagery dominates over illustration, with rope cross-sections and carabiner macro-shots doing the work of texture. The brand feels like a piece of gear: every element has a job, nothing is ornamental.

colors:
  primary: "#f3ce00"
  primary-active: "#d4b000"
  primary-disabled: "#f5e68a"
  ink: "#130c0d"
  body: "#343741"
  muted: "#757575"
  muted-soft: "#949494"
  hairline: "#e5e5e5"
  hairline-soft: "#ececec"
  canvas: "#f5f1e2"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#130c0d"
  on-dark: "#ffffff"
  accent-red: "#d14343"
  accent-blue: "#002fe1"
  accent-green: "#1a5632"
  rope-yellow: "#f3ce00"
  rope-yellow-bright: "#ffe600"
  charcoal: "#343741"
  near-black: "#130c0d"

typography:
  display-xl:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-strong:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
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
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.ink}"
    padding: 10px 26px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-eco:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    height: 48px
  footer:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  rope-swatch:
    backgroundColor: "{colors.rope-yellow}"
    rounded: "{rounded.full}"
    height: 24px
  rope-swatch-charcoal:
    backgroundColor: "{colors.charcoal}"
    rounded: "{rounded.full}"
    height: 24px
  rope-swatch-blue:
    backgroundColor: "{colors.accent-blue}"
    rounded: "{rounded.full}"
    height: 24px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in Sterling's signature marigold yellow (#f3ce00) against near-black (#130c0d) text. Used for "Add to Cart", "Shop Now", and "Explore Ropes". On hover, the yellow deepens to #d4b000; the disabled state fades to a pale #f5e68a with muted text. The 4px corner radius (`{rounded.xs}`) echoes the molded edges of climbing hardware — never pill-shaped, never soft.

**`button-secondary`** — An outlined button with a 2px near-black (#130c0d) border on a white surface. Used for secondary actions like "Learn More" or "Compare Models". On hover, the fill swaps to near-black with white text, maintaining the brand's high-contrast ethos. Same 44px height and 4px radius as primary.

**`button-ghost`** — A text-only button with no background or border, used in navigation dropdowns and filter panels. Relies on the brand's 600-weight button typography and 16px horizontal padding for touch target compliance.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with 8px rounded corners (`{rounded.sm}`) containing a product image, title, price, and optional badges. The image area uses top-only rounding to sit flush against the card body. Cards sit on the warm cream canvas (`{colors.canvas}`) with no shadow — the brand prefers flat layering over elevation.

**`product-badge`** — Small uppercase labels (11px, 600 weight, 0.5px letter-spacing) applied to product cards. The default badge is yellow (`{colors.primary}`) for "New" or "Best Seller". A red variant (`{colors.accent-red}`) marks sale items, and a green variant (`{colors.accent-green}`) flags ECO Rope products — the brand's sustainability line. All badges use 4px radius and 2px vertical padding.

### Navigation
**`nav-bar`** — A 64px fixed-height bar on the warm cream canvas (`{colors.canvas}`). Navigation links are 14px uppercase with 600 weight and 0.5px letter-spacing — a deliberate choice that reads as technical and direct rather than friendly. The active link state uses a 2px yellow underline (`{colors.primary}`). The logo (typically the Sterling Rope wordmark) sits left-aligned in near-black.

**`nav-link-active`** — The active navigation state, distinguished by yellow text and a 2px bottom border in the same yellow. No background fill — the brand uses underlines over highlight boxes.

### Forms
**`text-input`** — A white input field with a 1px hairline border (#e5e5e5) and 4px radius. On focus, the border thickens to 2px and switches to yellow (`{colors.primary}`). Used for search, newsletter signup, and account forms. The 44px height matches button dimensions for consistent form rows.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input with a white background and 1px hairline border. Despite the brand's general preference for small radii, the search bar uses full rounding — a practical concession for a component that often lives in the hero or sticky nav. 48px height for comfortable thumb access.

### Footer
**`footer`** — A dark footer block on charcoal (`{colors.charcoal}`) with white body text and muted (#949494) link text. Links use 14px weight-500 type with no underline until hover. The footer contains three columns: product categories, company info, and a newsletter signup with the yellow primary button. 48px vertical padding top and bottom.

### Rope Swatches
**`rope-swatch`** — Small circular color indicators (24px diameter, `{rounded.full}`) used on product detail pages to show available rope colors. The primary swatch is yellow (`{colors.rope-yellow}`), with charcoal (`{colors.charcoal}`) and blue (`{colors.accent-blue}`) as secondary options. These are the brand's most tactile component — they mimic the actual rope cross-section.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to 28px; search bar moves to sticky header |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains 32px display type |
| Desktop | 1128–1440px | Three-column product grid; full nav with uppercase links; hero at 42px display type |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; hero centered with wider margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch compliance.
- Product card tap targets (image, title, price) are independently tappable with 48px minimum hit area.
- Search bar is 48px tall on all breakpoints.
- Footer links have 24px minimum line height for finger targeting.

### Collapsing Strategy
- Primary navigation collapses to a hamburger icon at 743px and below.
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport narrows.
- Hero section reduces padding from 64px to 32px on mobile.
- Footer columns stack vertically below 744px.
- Rope swatches remain inline but reduce to 20px diameter on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components are inferred from common patterns; actual extracted hover colors were not available.
- Error states for form inputs (validation colors, error message styling) are not documented.
- The brand's dark mode palette (if any) was not extracted.
- Sub-brand palettes (ECO Rope, specific product lines) may have additional accent colors beyond the green (#1a5632) noted here.
- The exact font stack for neue-haas-grotesk-text (whether it loads as variable font or static weights) is unknown.
- Button loading states (spinner placement, disabled opacity) are not specified.
- The extracted color list includes several blues (#accef7, #4496f6, #002fe1, #007dc6) that may belong to third-party widgets (Shopify Pay, Klarna) rather than the brand; only #002fe1 is included as a brand accent.
- The red (#d14343) and pink (#f8bfb5) tones may be seasonal or collection-specific rather than core system colors.
- No extracted data for modal, tooltip, or dropdown component styling.
