---
version: alpha
name: "BenQ"
source_url: "https://www.benq.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Purple as a primary brand voltage in consumer electronics is almost unheard of — BenQ leans into it without hesitation. The hero palette anchors on #6b53cc, a saturated mid-violet that reads as creative-professional rather than gaming-neon, supported by a deeper #7231c6 on hover states and a luminous #b27aff for gradients and highlights. This violet family does something unusual: it signals both precision engineering and artistic temperament simultaneously, bridging BenQ's dual audience of color-critical photographers and ambient-lighting enthusiasts. A punchy orange-red accent (#e94b20) breaks the coolness for CTAs and promotional urgency — limited-time banners, "Buy Now" triggers — while a warm gold (#cdb889) surfaces on premium product lines like the treVolo speakers and ScreenBar series, lending a material-world warmth against the digital purple. Typography runs Poppins for display and navigational weight — its geometric round terminals echo the soft `{rounded.md}` corners on product cards — while Roboto handles body copy at 400 weight, keeping long spec sheets and comparison tables legible without competing for attention. The layout breathes through generous `{spacing.section}` gaps between product category blocks, each introduced by full-bleed lifestyle photography overlaid with semi-transparent dark scrims and left-aligned display type. Cards use `{rounded.sm}` with subtle elevation, never hard-edged, and the navigation bar runs a clean white surface with purple active-state underlines rather than background fills. Surface tones stay neutral: #f2f2f2 canvas areas, #e6e6f2 lavender-tinted soft panels for feature callouts, and pure white cards. The overall impression is a tech brand that chose a painter's palette over the usual gunmetal-and-blue industrial playbook.

colors:
  primary: "#6b53cc"
  primary-active: "#7231c6"
  primary-deep: "#492582"
  primary-disabled: "#b27aff"
  primary-light: "#8668ff"
  accent: "#e94b20"
  accent-dark: "#ba3c1a"
  gold: "#cdb889"
  gold-light: "#e7d7b5"
  ink: "#222222"
  body: "#424242"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#e5e0df"
  hairline-soft: "#d8cbcb"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-lavender: "#e6e6f2"
  surface-blue: "#dae8f2"
  surface-peach: "#f2dfda"
  surface-cream: "#f2e6da"
  surface-sage: "#e3eae3"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#ed0000"
  warning: "#ffe100"
  success: "#1c3f29"
  highlight-pink: "#ff91f0"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Roboto', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Roboto', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Roboto', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Poppins', 'Roboto', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Poppins', 'Roboto', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Roboto', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Roboto', 'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Roboto', 'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Poppins', 'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Poppins', 'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Roboto', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.1px
  spec-value:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Roboto', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  price-display:
    fontFamily: "'Poppins', 'Roboto', sans-serif"
    fontSize: 24px
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-hover:
    backgroundColor: "{colors.surface-lavender}"
    textColor: "{colors.primary-active}"
    border: 2px solid {colors.primary-active}
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-hover:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
  text-input-focus:
    border: 2px solid {colors.primary}
    boxShadow: 0 0 0 3px rgba(107, 83, 204, 0.12)
  text-input-error:
    border: 2px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-bar-active-indicator:
    backgroundColor: "{colors.primary}"
    height: 3px
    rounded: "{rounded.full}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    boxShadow: 0 8px 32px rgba(0, 0, 0, 0.12)
    border: 1px solid {colors.hairline-soft}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    boxShadow: 0 2px 8px rgba(0, 0, 0, 0.06)
    transition: box-shadow 0.2s ease, transform 0.2s ease
  product-card-hover:
    boxShadow: 0 8px 24px rgba(107, 83, 204, 0.12)
    transform: translateY(-2px)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: 4/3
    objectFit: contain
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 560px
    padding: "{spacing.hero} {spacing.xxl}"
    overlay: linear-gradient(to right, rgba(0,0,0,0.7) 0%, transparent 60%)
  hero-banner-cta:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    aspectRatio: 16/9
  category-card-hover:
    backgroundColor: "{colors.surface-lavender}"
  feature-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  promo-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  gold-badge:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline-soft}
  spec-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  comparison-toggle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  comparison-toggle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px 12px 48px
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: 2px solid {colors.primary}
    boxShadow: 0 4px 16px rgba(107, 83, 204, 0.1)
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  color-accuracy-chip:
    backgroundColor: "{colors.surface-lavender}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  price-tag:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  price-tag-sale:
    typography: "{typography.price-display}"
    textColor: "{colors.accent}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: ">"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: 2px solid {colors.hairline-soft}
  tab-item:
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.lg}"
  tab-item-active:
    textColor: "{colors.primary}"
    borderBottom: 3px solid {colors.primary}

---

## Components

### Buttons

**`button-primary`** — Solid purple (#6b53cc) fill with white text at Poppins 600 weight. Corners use `{rounded.sm}` for a controlled softness that avoids both clinical sharpness and playful pill shapes. Hover deepens to #7231c6 with a subtle lift shadow. Disabled state uses the lighter #b27aff at reduced opacity, maintaining the purple family rather than graying out entirely.

**`button-secondary`** — White fill with a 2px purple border and purple text. On hover, the background shifts to the lavender surface (#e6e6f2) while the border darkens to `{colors.primary-active}`. Used for secondary actions like "Learn More" and "Compare" alongside primary CTAs.

**`button-accent`** — Orange-red (#e94b20) fill reserved for time-sensitive promotions, flash sales, and "Add to Cart" urgency. Hover darkens to #ba3c1a. Never placed adjacent to `button-primary` — the two compete visually; use one or the other per content block.

**`button-ghost`** — Transparent background with dark text, used for tertiary actions like "View All Specs" within content sections. No border, relies on text weight and hover underline for affordance.

### Navigation

**`nav-bar`** — 72px white bar with a faint bottom hairline. Logo sits left, category links center-weighted in Poppins 500 at 15px. Active category receives a 3px purple indicator bar with full-radius ends, positioned at the bottom edge. Right side holds search icon, region selector, and cart. On scroll, the bar gains a 4px drop shadow and reduces to 64px height.

**`mega-menu`** — Drops below nav on category hover with a smooth 200ms ease-in. White panel with generous 32px internal padding, organized in 3-4 column grid. Product subcategories listed with small thumbnail icons (32x32). Subtle outer shadow and 1px hairline border prevent it from floating ambiguously.

### Product Cards

**`product-card`** — White card with `{rounded.sm}` corners and a whisper of box shadow. Product image sits in a light gray (#f2f2f2) container with 4:3 aspect ratio and `contain` fit so no product gets cropped. Below: product name in `{typography.title-sm}`, a one-line feature summary in `{typography.body-sm}`, and price in `{typography.price-display}`. On hover, the shadow takes on a purple tint and the card lifts 2px — a subtle but clear interactive signal.

**`product-card-image`** — Dedicated image area with neutral background ensures monitors and projectors of various aspect ratios display cleanly without awkward whitespace distribution.

### Hero

**`hero-banner`** — Full-width dark background (typically a lifestyle photograph of the product in situ) with a left-anchored gradient overlay fading from 70% black to transparent. Display text in white at `{typography.display-xl}` left-aligned over the dark region. CTA uses the accent orange button to pop against the dark field. Minimum height 560px ensures the hero commands attention without requiring scroll-jacking.

### Spec & Comparison

**`spec-table-row`** — Alternating white and #f2f2f2 rows for readability across BenQ's typically long specification lists (20-40 rows for monitors). Label column in `{typography.spec-label}` muted gray, value column in `{typography.spec-value}` dark ink. Rows have generous 12px vertical padding to prevent the density from feeling oppressive.

**`comparison-toggle`** — Pill-shaped toggle chips for selecting models to compare. Inactive state is light gray surface with body text; active state fills with primary purple and white text. Grouped horizontally with 8px gaps, scrollable on mobile.

### Badges

**`feature-badge`** — Small purple pill for technology labels like "HDRi," "Eye-Care," "Pantone Validated." Uppercase Poppins at 11px keeps them compact but legible beside product thumbnails.

**`promo-badge`** — Orange-red variant for sale tags and limited offers. Same sizing as feature badge but visually distinct through color alone.

**`gold-badge`** — Warm gold (#cdb889) for premium series indicators. Dark text ensures contrast on the lighter background.

### Search

**`search-bar`** — Full-radius pill shape with light gray fill in resting state. Search icon positioned 16px from left edge. On focus, transitions to white fill with a purple border and soft purple-tinted shadow, signaling active input clearly.

### Footer

**`footer`** — Dark ink (#222222) background spanning full width with white and muted-gray text. Organized in 4-column grid: product categories, support links, company info, and social/legal. Links brighten to white on hover. Bottom row contains copyright and region selector in `{typography.caption}`.

### Tabs

**`tab-bar`** — Horizontal tab navigation used on product detail pages to switch between Overview, Specs, Reviews, and Support. Active tab receives a 3px purple bottom border matching the nav active indicator, creating brand consistency across interactive elements.

### Color Accuracy Chip

**`color-accuracy-chip`** — Lavender-tinted pill displaying color certifications (Delta E<2, Pantone, CalMAN). Uses `{typography.caption}` in deep purple text. Placed inline with product specs or as a row beneath the product title.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + slide-out panel; hero reduces to 360px min-height with centered text; spec table scrolls horizontally; mega-menu becomes full-screen overlay; search bar moves into hamburger panel |
| Tablet | 744–1128px | Two-column product grid; nav shows top 4 categories with overflow in "More" dropdown; hero maintains left-align with reduced font sizes (display-lg); comparison toggles wrap to second row |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu on hover; hero at full 560px height; spec comparison shows up to 3 products side-by-side; all nav categories visible |
| Wide | > 1440px | Content max-width caps at 1440px, centered; four-column product grid; hero image extends full bleed while text container stays within max-width; generous lateral whitespace |

### Touch Targets

- All interactive elements maintain minimum 44px touch target on mobile, even when visually smaller
- Product card tap area covers the entire card surface, not just the text or image
- Navigation hamburger icon uses 48px hit area with 12px padding beyond the visible icon
- Tab bar items expand padding to 16px vertical on touch devices
- Comparison toggle chips maintain 12px gap on mobile to prevent mis-taps

### Collapsing Strategy

- Mega-menu categories collapse into accordion groups within the mobile slide-out panel
- Spec tables maintain full row structure but enable horizontal scroll with a fade-edge indicator on the right
- Product comparison stacks vertically on mobile (one product per screen width, swipeable)
- Footer columns collapse into expandable accordion sections with purple chevron indicators
- Hero text stack reduces from display-xl to display-md, and CTA button goes full-width on mobile
- Category cards shift from landscape (16:9) to square (1:1) on mobile for better thumb-scroll browsing

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact border-radius values could not be confirmed from extraction; `{rounded.sm}` (8px) is inferred from visual inspection of product cards and buttons
- BenQ uses Noto Sans variants for CJK locales (Japanese, Korean, Simplified/Traditional Chinese) — exact fallback ordering and weight mappings per locale were not fully extractable
- Animation timing and easing curves for hover states, mega-menu reveals, and page transitions are not captured
- Dark-mode palette (if one exists) was not detected in the extraction
- Icon system details (size grid, stroke width, icon font vs SVG) could not be determined
- The gold (#cdb889) token's exact usage scope is uncertain — it may be limited to specific product sub-brands (ScreenBar, treVolo) rather than a global accent
- Elevation/shadow scale specifics beyond the product card hover state are approximated
- Mobile navigation animation (slide direction, duration, backdrop opacity) was not extractable
