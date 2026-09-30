---
version: alpha
name: "Radtec"
source_url: "https://www.radtec.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Electric yellow (#ffff00) against deep ocean blue (#02537e) — the palette reads like a gas flame against twilight, and that deliberate thermal tension runs through the entire Radtec system. The primary blue anchors navigation, hero overlays, and footer backgrounds with the solidity of powder-coated steel, while the yellow fires every CTA, sale badge, and hover state with the urgency of infrared heat. Typography pairs Montserrat for headings (weight 700, tight letter-spacing, all-caps on category labels) with Roboto for body copy at comfortable 16px/1.6 — a workmanlike stack that loads fast and renders cleanly on product spec tables dense with BTU ratings and clearance dimensions. Corners are kept tight: buttons sit at `{rounded.xs}` (4px), cards at `{rounded.sm}` (8px), and only promotional badges push to `{rounded.full}` pill shapes. Spacing is generous vertically — hero sections breathe at 80–120px padding — but the horizontal grid compresses to a dense 3-up or 4-up product layout where thumbnail-heavy cards show burners, reflectors, and patio setups without wasted gutter. The nav bar runs a solid `{colors.primary}` band across the top with white wordmark and yellow accent on hover, giving the site the feel of industrial equipment branding rather than lifestyle retail. Product cards carry a subtle 1px `{colors.hairline}` border on white backgrounds, letting photography (stainless cylinders, glowing glass tubes, flame mushroom tops) do the selling. Footer stacks dense link columns on the same deep blue canvas, reinforcing brand recognition bookend-style. The overall system trusts bold color contrast and clean geometry over texture or illustration — every surface is flat, every shadow functional rather than decorative.

colors:
  primary: "#02537e"
  primary-active: "#013f60"
  primary-disabled: "#8fb5cb"
  accent: "#ffff00"
  accent-active: "#e6e600"
  accent-muted: "#fff566"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f7f9"
  surface-card: "#ffffff"
  surface-dark: "#02537e"
  on-primary: "#ffffff"
  on-accent: "#1a1a1a"
  on-dark: "#ffffff"
  success: "#2e7d32"
  error: "#c62828"
  star-rating: "#ffab00"

typography:
  display-xl:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-lg:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-uppercase:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Roboto', monospace, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "'Roboto', monospace, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Montserrat', arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
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
  hero: 96px

components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
    textTransform: uppercase
  button-primary-hover:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-dark-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
  text-input-focus:
    border: 2px solid {colors.primary}
    backgroundColor: "{colors.canvas}"
  text-input-error:
    border: 2px solid {colors.error}
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: 0 {spacing.xl}
  nav-bar-link-hover:
    textColor: "{colors.accent}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
    shadow: 0 4px 16px rgba(0,0,0,0.08)
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.hero} {spacing.xl}"
    minHeight: 520px
    overlay: linear-gradient(rgba(2,83,126,0.7), rgba(2,83,126,0.85))
  hero-cta:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 36px
    height: 52px
    textTransform: uppercase
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    shadow: none
    transition: box-shadow 0.2s ease
  product-card-hover:
    shadow: 0 4px 12px rgba(0,0,0,0.1)
    border: 1px solid {colors.hairline}
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: 1/1
    objectFit: contain
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.hairline-soft}
    stripeColor: "{colors.surface-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    opacity: 0.8
  footer-link-hover:
    textColor: "{colors.accent}"
    opacity: 1
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: 1px solid {colors.hairline}
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  newsletter-signup:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  heat-output-indicator:
    backgroundColor: "{colors.accent-muted}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.xs}"
    padding: 4px 10px

---

## Components

### Buttons

**`button-primary`** — High-voltage yellow (#ffff00) background with dark text, uppercase Montserrat at weight 600. Tight 4px radius keeps the industrial character. On hover, yellow deepens to #e6e600 with no scale transform. Disabled state drops to gray hairline background with muted text. Used for all conversion-critical actions: "Add to Cart," "Shop Now," "Get Quote."

**`button-secondary`** — Transparent background with a 2px solid primary-blue border and blue text. On hover, fills completely with `{colors.primary}` and flips text to white — a full inversion that signals interactivity without competing with the yellow primary CTA. Used for secondary actions like "View Details," "Compare," and filter toggles.

**`button-dark`** — Deep blue background (#02537e) with white text at medium size. Serves in-content CTAs on light backgrounds where yellow would clash with product photography. Commonly appears inside spec panels and comparison tools.

### Navigation

**`nav-bar`** — Full-width solid blue bar at 72px height. White wordmark left-aligned, navigation links in Montserrat 500 weight spaced with `{spacing.xl}` gaps. Hover state flips link text to yellow. On mobile, collapses to a hamburger icon (white, 24px) that triggers a full-screen blue overlay with stacked links.

**`mega-menu`** — Drops below nav on category hover. White background, light bottom shadow, organized in a 3-column grid showing product categories with small thumbnail images. Category headings use `{typography.title-sm}`, sub-links use `{typography.body-sm}` with muted color until hovered.

### Hero

**`hero-banner`** — Full-bleed image section at minimum 520px height with a blue-tinted gradient overlay (70–85% opacity). Display text sits in white at `{typography.display-xl}` with the yellow CTA button (`hero-cta`) centered or left-aligned depending on layout variant. The overlay ensures text legibility over product photography showing flames and outdoor settings.

### Product Cards

**`product-card`** — White card with 1px `{colors.hairline-soft}` border and `{rounded.sm}` corners. Contains a square product image (contain-fit on soft gray background), title in `{typography.title-sm}`, and price in `{typography.price}` colored primary blue. On hover, a subtle box-shadow rises (0 4px 12px) and border sharpens to full hairline. No rating stars appear on grid view — only on detail pages.

**`product-card-image`** — Square aspect ratio with `object-fit: contain` on a `{colors.surface-soft}` background. Products (heaters, fire pits) are shown on white/transparent backgrounds, so the soft gray container provides consistent framing.

### Badges

**`category-badge`** — Pill-shaped (`{rounded.full}`) with primary blue background and white uppercase text at 11px. Applied to product cards for type classification: "Fire Pit," "Tower Heater," "Infrared."

**`sale-badge`** — Same pill shape but in yellow with dark text. Positioned absolute top-right on product card images. Communicates clearance, percentage-off, or "New" status.

### Specification Table

**`spec-table`** — Alternating white/soft-gray rows with product specifications. Label column uses `{typography.spec-label}` (medium weight), value column uses `{typography.spec-value}` (regular weight). Monospace-influenced font stack ensures BTU numbers, dimensions, and weights align cleanly. Rows separated by `{colors.hairline-soft}` borders.

### Heat Output Indicator

**`heat-output-indicator`** — Small inline badge showing BTU or wattage rating in muted yellow with dark text and uppercase caption styling. Appears on product cards and listing grids as a quick-scan metric for comparing heating power across products.

### Footer

**`footer`** — Deep blue background matching the nav bar, creating a bookend frame. Four-column link layout with headings in `{typography.title-sm}` white and links at 80% opacity that brighten to yellow on hover. Bottom row contains payment icons, certifications, and copyright in `{typography.caption}`.

### Search

**`search-bar`** — Standard text input styling with 44px height and subtle border. Positioned inside the nav on desktop (inline with links) and expands to full-width on mobile. Magnifying glass icon in `{colors.muted}` sits inside the input left-padded.

### Newsletter Signup

**`newsletter-signup`** — Soft gray panel with `{rounded.sm}` corners and `{spacing.xl}` padding. Contains a heading, brief copy, email input, and yellow submit button side-by-side. Typically placed above the footer or mid-page between product grids.

### Breadcrumb

**`breadcrumb`** — Horizontal text trail using caption-size type with "/" separators. Muted gray for ancestor links, full ink color for current page. Sits below the nav bar with `{spacing.md}` vertical padding.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen blue overlay; hero text drops to `{typography.display-md}`; spec tables scroll horizontally; footer stacks to single column with accordion sections |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but tighter spacing; hero maintains full height but text centers; mega-menu becomes two-column |
| Desktop | 1128–1440px | Three or four-column product grid; full mega-menu with thumbnails; hero text left-aligned with CTA; side-by-side spec comparison enabled |
| Wide | > 1440px | Content max-width caps at 1440px centered; additional breathing room in hero padding; four-column grid with larger card thumbnails |

### Touch Targets

- All interactive elements minimum 44px tap target on mobile
- Product card entire surface is tappable, not just the title link
- Nav hamburger icon padded to 48×48px hit area
- Footer accordion headers use full-width 48px tap rows
- Quantity steppers in cart sized at 44×44px with clear +/− icons

### Collapsing Strategy

- Desktop mega-menu becomes a stacked accordion on mobile, grouped by category
- Product filter sidebar becomes a bottom-sheet modal on mobile triggered by a sticky "Filter" button
- Spec tables gain horizontal scroll with a subtle fade-out gradient on the right edge
- Hero dual-CTA layouts stack vertically with `{spacing.md}` gap
- Newsletter email + button row stacks to full-width input above full-width button
- Footer four-column grid collapses to expandable sections with chevron toggles

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two colors extracted (#02537e, #ffff00); additional neutrals, grays, and status colors are inferred from standard patterns rather than measured from live CSS
- No CSS custom properties or design-token JSON could be retrieved — site may load styles via JavaScript bundles or server-rendered inline styles
- Exact border-radius values for buttons and cards are estimated from visual convention; no computed styles were captured
- Shadow values for hover states and dropdowns are approximated — no box-shadow declarations were extracted
- Icon system (style, stroke width, size grid) could not be determined from extraction
- Exact nav-bar height and hero min-height are estimated from category norms for industrial/outdoor brands
- No motion/transition tokens extracted — durations and easing functions are defaults (0.2s ease)
- Platform is not Shopify; CMS and component framework are unknown, which may affect implementation patterns
