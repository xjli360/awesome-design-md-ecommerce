---
version: alpha
name: "Dreame"
source_url: "https://www.dreametech.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Dreame anchors its digital identity in #108474 — a deep aquatic teal that sits in the productive gap between tech-green and ocean-blue, giving product pages the measured authority of a laboratory instrument without its coldness. That primary deploys over near-black surfaces (#1f2021, #141414) that form the actual architectural ground of the site: dark-mode by design intent, not by user toggle, a choice that makes precision-engineered product photography float rather than sit on a page. Against those dark volumes, amber gold (#ffaa00) enters selectively — pricing callouts, promotional chips, and star ratings all glow warm, building a two-temperature grammar where teal signals capability and gold signals reward. A warm earth layer — sand (#d1b89c), tan (#a5886b), sienna-gold (#c19c70) — never appears in UI chrome but bleeds into hero gradient overlays and lifestyle photography, keeping the engineering palette from reading as sterile in a kitchen or living room context.

  Type runs AlibabaPuHuiTiM as the brand's primary voice and Inter as its UI support companion, a pairing that reflects Dreame's posture as a Chinese precision-tech company making deliberate moves toward Western design legibility. Display text runs bold and large against dark ground; body copy pulls back to muted slate (#728197) rather than full white, lowering contrast for extended specification reading. Button labels inherit the brand font at weight 700, matching headline authority — this is not a system that softens its calls to action with a gentler weight.

  Corners settle at a decisively moderate register: `{rounded.md}` on product cards, `{rounded.sm}` on primary CTAs, `{rounded.full}` reserved strictly for category chips, search pills, and color swatches. Vertical rhythm between page sections holds at 64px on desktop, wide enough that each product grouping reads as a distinct editorial moment rather than catalog scroll. The sticky navigation — dark-surfaced with the teal brand mark fixed at left — persists across the entire product discovery flow, with cart and search always reachable within one tap, reinforcing the operational readiness that a robotic-cleaning category demands to close purchase decisions.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a0cdc7"
  primary-light: "#edf5f5"
  ink: "#141414"
  body: "#4d4d4d"
  muted: "#728197"
  muted-soft: "#b1b1b3"
  hairline: "#dcdfe5"
  hairline-soft: "#e2e2e2"
  canvas: "#f9fafb"
  surface-dark: "#1f2021"
  surface-darker: "#141414"
  surface-slate: "#4a5464"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-amber: "#ffaa00"
  accent-amber-muted: "#f59e0b"
  accent-orange: "#f16d0e"
  warm-tan: "#d1b89c"
  star: "#ffaa00"
  link: "#0065b3"

typography:
  display-xl:
    fontFamily: "'AlibabaPuHuiTiM', Inter, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'AlibabaPuHuiTiM', Inter, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'AlibabaPuHuiTiM', Inter, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'AlibabaPuHuiTiM', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "'AlibabaPuHuiTiM', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, 'AlibabaPuHuiTiM', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, 'AlibabaPuHuiTiM', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'AlibabaPuHuiTiM', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'AlibabaPuHuiTiM', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  price-display:
    fontFamily: "'AlibabaPuHuiTiM', Inter, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  badge-label:
    fontFamily: "Inter, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.4px
    textTransform: uppercase
  spec-label:
    fontFamily: "Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.46
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.on-dark}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  search-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    position: sticky
    top: 0
    zIndex: 100
    borderBottom: "1px solid {colors.surface-slate}"
  nav-dropdown:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.surface-slate}"
    padding: 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 24px
    border: "1px solid {colors.hairline-soft}"
    hoverShadow: "0 8px 24px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.surface-darker}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subheadingTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    minHeight: 560px
    padding: 80px 48px
  hero-banner-split:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-md}"
    subheadingTypography: "{typography.body-sm}"
    layout: 50/50 image-text
    rounded: "{rounded.none}"
  promo-chip:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  promo-chip-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  feature-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  spec-row:
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: 12px 0
  color-swatch-selector:
    selectedBorder: "2px solid {colors.primary}"
    unselectedBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    size: 28px
    gap: 8px
  rating-display:
    starColor: "{colors.star}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    gap: 4px
  category-nav-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
    salePriceColor: "{colors.accent-orange}"
    originalPriceColor: "{colors.muted}"
    originalPriceDecoration: line-through
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted-soft}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "1px solid {colors.surface-slate}"
    padding: 48px 0 32px

## Components

### Buttons

**`button-primary`** — The primary CTA renders in #108474 teal with white text at 700 weight, 48px tall, and `{rounded.sm}` corners that read as purposeful rather than playful. On hover it deepens to `{colors.primary-active}` (#0d6b5e) with no scale transform — the brand signals confidence, not animation spectacle. The disabled state mutes to `{colors.primary-disabled}`, a desaturated teal that maintains the color family without inviting interaction.

**`button-secondary`** — A white-background outlined button with `{colors.hairline}` border that pairs alongside the primary in two-CTA rows (typically "Buy Now" + "Learn More"). On hover the border shifts to `{colors.primary}` and the background lifts to `{colors.surface-soft}`, providing clear active feedback without adopting the primary color. Height and typography match `button-primary` exactly so the two buttons align flush in horizontal groups.

**`button-ghost`** — Used exclusively on dark hero surfaces where a transparent-background with white outline avoids covering the product photography behind it. Text and border both run `{colors.on-dark}` and the rounded and size specs match the primary button for visual grid alignment.

### Navigation

**`nav-bar`** — The navigation runs on `{colors.surface-dark}` (#1f2021), persistent and sticky, carrying the teal brand mark at far left and cart/search icons at far right. Category links use `{typography.nav-link}` in `{colors.on-dark}` and reveal mega-dropdown panels (`nav-dropdown`) with the same dark background and a subtle slate border to distinguish the overlay layer. The nav height of 64px is compact relative to the product imagery it frames.

### Product Card

**`product-card`** — Cards flip to a white surface (`{colors.surface-card}`) against the site's predominantly dark page background, creating natural figure-ground separation for the product photography without additional framing. Product name runs `{typography.title-sm}`, pricing runs `{typography.price-display}` in `{colors.ink}`, and short descriptor copy drops to `{typography.body-sm}` in `{colors.muted}`. Promo chips (`promo-chip`, `promo-chip-sale`) sit in the top-left corner of the image frame as absolute overlays, not inside the text block. On hover, a soft shadow lifts the card 8px without scaling.

### Hero Banner

**`hero-banner`** — Full-viewport heroes use `{colors.surface-darker}` (#141414) as ground, with product photography composited center-right and headline copy at left in `{typography.display-xl}`. The amber accent (`{colors.accent-amber}`) may appear on a promotional sub-label or countdown badge above the headline — never as a background field. A primary CTA button and a ghost button typically appear as a pair in the lower-left text column.

**`hero-banner-split`** — A narrower 50/50 variant used for secondary product campaigns places photography on one half and a teal or slate-tinted panel on the other, with `{typography.display-md}` headline and a single CTA. This format appears on category landing pages between full-width heroes.

### Promo and Feature Chips

**`promo-chip`** — Amber (#ffaa00) background with dark `{colors.ink}` text in `{typography.badge-label}` — 11px uppercase, 700 weight, pill-shaped via `{rounded.full}`. Used for "LIMITED TIME", "BEST SELLER", and seasonal sale labels on product imagery. The amber color is the warmest element in the system and only appears here and in star ratings, making it a reliable attention signal.

**`promo-chip-sale`** — A hotter orange variant (`{colors.accent-orange}`, #f16d0e) for percentage-off callouts and clearance labels where amber might not read urgent enough. White text (`{colors.on-primary}`) maintains readability against the brighter ground.

**`feature-badge`** — A muted teal-tinted chip (`{colors.primary-light}` fill, `{colors.primary}` text) used to label product differentiators in spec panels — "Auto-Empty", "LiDAR+", "5500 Pa". Distinct from promo chips by color family; where amber marks commercial urgency, teal marks product capability.

### Specifications

**`spec-row`** — Specification tables alternate label (left, `{colors.muted}`, `{typography.spec-label}`) and value (right, `{colors.ink}`, `{typography.body-sm}`) across a hairline-bottom ruled row. The layout avoids full-column background zebra striping in favor of the single border rule, keeping the spec panel visually quiet so values read without interference. Used extensively on product detail pages below the hero fold.

### Color Swatch Selector

**`color-swatch-selector`** — 28px circular swatches with a 2px `{colors.primary}` teal ring on the selected state and a subtle 1px `{colors.hairline}` ring on unselected states. Gap between swatches is `{spacing.sm}`. The teal selection ring creates a consistent "Dreame-colored selection" system that works across all product variant types.

### Rating Display

**`rating-display`** — Star icons fill in `{colors.star}` (#ffaa00), the same amber used in promo chips, binding the reward and social-proof signals to the same color. Review count text runs `{typography.body-sm}` in `{colors.muted}` immediately after the stars. No numeric score badge — the star row and count render inline.

### Category Navigation

**`category-nav-chip`** — A horizontally scrolling row of pill chips appears on category and listing pages. Inactive chips use `{colors.surface-soft}` with `{colors.body}` text; the active chip fills `{colors.primary}` with `{colors.on-primary}` text. This is the only context outside CTAs where the teal fill appears at chip scale.

### Price Tag

**`price-tag`** — Sale prices render in `{colors.accent-orange}` at `{typography.price-display}` weight, with the struck-through original price following immediately in `{colors.muted}`. Non-sale prices display in `{colors.ink}`. The large 700-weight price figure is the dominant number on a product card and is never reduced in size to accommodate longer price strings — layout wraps instead.

### Footer

**`footer`** — Dark-surfaced (`{colors.surface-dark}`) with a top border in `{colors.surface-slate}` to separate it from page content. Section headings use `{typography.title-sm}` in `{colors.on-dark}`; link text uses `{typography.body-sm}` in `{colors.muted-soft}` and lifts to `{colors.on-dark}` on hover. Social icons, payment method logos, and a secondary teal brand lockup sit in the bottom row above the legal text line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text scales to `{typography.display-sm}`; nav collapses to hamburger + brand mark + cart icon; category chips scroll horizontally; spec tables stack label above value; section padding reduces to `{spacing.xl}` |
| Tablet | 744–1128px | Two-column product grid; hero switches to `hero-banner-split` format; nav shows top-level categories with overflow in hamburger; price-tag and CTA stack vertically in product card |
| Desktop | 1128–1440px | Three- to four-column product grid; full sticky nav with mega-dropdown panels; hero runs full `hero-banner` format with side-by-side text and image; spec rows display in two-column side-by-side layout |
| Wide | > 1440px | Layout max-width constrains to ~1440px with additional side margins; hero photography scales up within constrained text column; product grid holds at four columns |

### Touch Targets

- All tappable buttons minimum 48px height with at least 8px vertical padding beyond label
- Color swatches expand tap area to 44×44px via invisible padding despite 28px visual size
- Nav hamburger icon tap target is 48×48px
- Category nav chips minimum 40px height on mobile

### Collapsing Strategy

- Mega-dropdown navigation collapses to full-screen drawer with back navigation on mobile
- Spec tables reflow to single-column (label line, value line) below 744px; horizontal rule separates each pair
- Hero two-column layouts stack to image-above, text-below on mobile; image crops to 16:9 aspect
- Footer column grid (4-up on desktop) collapses to 2-up on tablet and 1-up with accordion toggling on mobile
- Promo chips on product cards remain in absolute image-overlay position at all breakpoints; text does not wrap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom icon or illustration system could be extracted — icon style (line weight, filled vs. outline) and glyph set are unknown
- Modal and overlay background scrim opacity and blur values were not extractable from static HTML
- Animation and transition timings (hover states, drawer open, hero transitions) are JavaScript-driven and could not be captured
- The full AlibabaPuHuiTiM type scale (weight variants: Light, Regular, Medium, Bold) is assumed from the extracted `AlibabaPuHuiTiM` token — specific weight integers for each variant were not confirmed
- Exact product card image aspect ratio (suspected 1:1 or 4:3) was not confirmed from extraction
- Dark/light mode switching behavior: unclear whether the dark-ground design is universal or if a light canvas mode exists for certain page types
- Loyalty or membership badge colors and tier hierarchy are not captured
