---
version: alpha
name: "SodaStream"
source_url: "https://sodastream.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Fizz rendered as interface — SodaStream's digital presence translates the upward rush of carbonation into a vertical scroll rhythm where oversized product hero shots float against generous white expanses, punctuated by a signature teal (#00b4b1) that appears only at decisive interaction moments: add-to-cart triggers, promotional banners, and the sticky nav CTA. The teal is not pastel or muted; it carries the same visual snap as a bubble breaking the surface, bright enough to read against both `{colors.canvas}` white and dark lifestyle photography overlays. Typography leans on a geometric sans-serif stack (likely a Gotham/Proxima Nova descendant loaded via JS bundle) set at relatively restrained weights — headlines at 600 rather than 800, body at 400 — trusting product photography and motion to carry drama rather than typographic mass. Cards use a soft `{rounded.md}` radius that echoes the cylindrical form of the carbonation machines themselves, while primary buttons push further to `{rounded.full}` pill shapes, reinforcing the bubble metaphor without illustrating it literally. The spacing system breathes generously: section gaps of 64–80px separate content blocks like the pause between sips, and product grid gutters sit at 24px to keep the catalog scannable without density fatigue. A secondary navy-charcoal (#1a2b3b) anchors the footer and trust-signal regions, grounding the effervescent teal with authority. Promotional modules — limited-edition flavors, bundle deals, sustainability impact counters — arrive as full-bleed color bands in the teal or a warm off-white (#f5f7f2), breaking the vertical monotony of the white canvas. The overall impression is a kitchen-appliance brand that refuses to look like one, borrowing the clarity of a wellness DTC while retaining the conversion architecture of a CPG powerhouse.

colors:
  primary: "#00b4b1"
  primary-active: "#009a97"
  primary-disabled: "#b3e6e5"
  secondary: "#1a2b3b"
  secondary-active: "#0f1e2d"
  accent-warm: "#f5f7f2"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f7f2"
  surface-card: "#ffffff"
  surface-dark: "#1a2b3b"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-surface-dark: "#e0e7ef"
  success: "#22c55e"
  error: "#ef4444"
  promo-band: "#00b4b1"
  badge-new: "#ff6b35"
  star-rating: "#f59e0b"

typography:
  display-xl:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  uppercase-tag:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Gotham', 'Proxima Nova', Montserrat, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
    textDecoration: line-through

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
  section-lg: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
    transition: background-color 0.2s ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: 2px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-dark:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    boxShadow: 0 2px 8px rgba(0,0,0,0.06)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 0
    overflow: hidden
    boxShadow: 0 1px 3px rgba(0,0,0,0.05)
    transition: box-shadow 0.2s ease, transform 0.2s ease
  product-card-hover:
    boxShadow: 0 8px 24px rgba(0,0,0,0.1)
    transform: translateY(-2px)
  product-card-image:
    aspectRatio: 1/1
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md} {rounded.md} {rounded.none} {rounded.none}"
  product-card-body:
    padding: "{spacing.base}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    minHeight: 600px
    padding: "{spacing.section} {spacing.xl}"
    textAlign: center
    display: flex
    alignItems: center
    justifyContent: center
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  hero-subline:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
    maxWidth: 560px
    marginBottom: "{spacing.xl}"
  promo-banner:
    backgroundColor: "{colors.promo-band}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
    height: 40px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sustainability-counter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg} {spacing.xl}"
    border: 1px solid {colors.hairline}
    textAlign: center
  sustainability-number:
    typography: "{typography.display-xl}"
    textColor: "{colors.primary}"
  flavor-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: 1px solid {colors.hairline}
  flavor-chip-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: 1px solid {colors.primary}
  comparison-table:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: 1px solid {colors.hairline}
    overflow: hidden
  comparison-table-header:
    backgroundColor: "{colors.surface-soft}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  comparison-table-cell:
    padding: "{spacing.md} {spacing.lg}"
    borderBottom: 1px solid {colors.hairline-soft}
    typography: "{typography.body-sm}"
  bundle-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    border: 2px solid {colors.hairline}
    transition: border-color 0.2s ease
  bundle-card-selected:
    border: 2px solid {colors.primary}
    boxShadow: 0 0 0 1px {colors.primary}
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-surface-dark}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.base}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.on-surface-dark}"
    opacity: 0.8
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: 1px solid {colors.hairline}
    boxShadow: 0 2px 8px rgba(0,0,0,0.04)

---

## Components

### Buttons

**`button-primary`** — Full pill-shaped CTA in the brand teal, used for add-to-cart, checkout, and hero CTAs. On hover, background darkens to `primary-active`; on disabled states (out of stock, form incomplete), the teal fades to `primary-disabled` with reduced opacity. Minimum width of 160px on desktop to maintain visual weight in product grids.

**`button-secondary`** — White fill with a 2px ink border and pill radius, used for secondary actions like "Learn more," "Compare models," or "View details." On hover, the button inverts to solid ink with white text, creating a satisfying toggle effect. Never appears alongside another secondary button without at least 12px gap.

**`button-dark`** — Navy-charcoal pill used exclusively in dark-context regions: the footer, dark hero modules, and promotional overlays. Maintains the same dimensions as `button-primary` for visual consistency in mixed layouts.

### Navigation

**`nav-bar`** — Fixed top navigation at 64px height on a white canvas with a subtle bottom hairline. Logo sits left, nav links center (Products, Flavors, Sustainability, Accessories), and cart icon + CTA right. On scroll, the hairline gives way to a soft drop shadow via `nav-bar-scrolled`. Mobile collapses to hamburger + logo + cart triplet.

**`promo-banner`** — Thin 40px teal band above the nav bar announcing free shipping thresholds, seasonal promos, or sustainability milestones. White text at `body-sm` weight, optionally with a dismiss X. Disappears on scroll past first viewport on mobile to reclaim space.

### Product Display

**`product-card`** — Square image container over a text body with product name (`title-sm`), brief descriptor (`body-sm` in muted), and price (`price`). The card uses `rounded.md` corners and lifts on hover with increased shadow and -2px Y translation. Image area uses the warm off-white `surface-soft` as placeholder background during lazy load.

**`flavor-chip`** — Pill-shaped selectors for flavor variants (Original, Lemon, Berry, etc.) arranged in a horizontal scroll row beneath product images. Selected state flips to teal background with white text; unselected maintains a thin hairline border. Touch targets are minimum 40px tall on mobile despite the visual compactness.

**`bundle-card`** — Larger card format for starter kits and multi-item bundles. Features a 2px hairline border that transitions to teal on selection, with an outer glow ring reinforcing the active state. Contains product thumbnail cluster, bundle name at `title-md`, savings badge, and price breakdown.

### Comparison & Education

**`comparison-table`** — Structured table for comparing carbonation machine models. Header row uses `surface-soft` background; cells alternate clean white with soft hairline separators. Checkmark and X icons indicate feature presence. Rounds the outer container at `rounded.md` with hidden overflow.

**`sustainability-counter`** — Rounded container displaying real-time or milestone metrics (bottles saved, CO2 reduced). The headline number renders in teal at `display-xl` weight, with a descriptor line beneath in `body-md`. Used in both hero contexts and inline content blocks.

### Search

**`search-bar`** — Full-width pill input with subtle outer shadow, used on the accessories and flavors catalog pages. Placeholder text in `muted` color, active border transitions to `primary` on focus. Magnifying glass icon sits 16px from left edge at 20px size.

### Footer

**`footer`** — Dark navy block with four-column link grid (Shop, Support, Company, Connect), email signup input, and social icons. Heading text in bright white, link text in the slightly dimmed `on-surface-dark` at 80% opacity, increasing to full on hover. Legal row at bottom uses `caption` size.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, hero text at `display-md` scale, promo banner hides on scroll, full-bleed section backgrounds, bottom-sticky add-to-cart bar on PDP |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed spacing, hero split layout (text left, product right), comparison table scrolls horizontally |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links + CTA, hero at maximum `display-xl` scale, side-by-side comparison table, 64px section spacing |
| Wide | > 1440px | Content max-width capped at 1440px and centered, section spacing increases to 80px, product grid can expand to four columns for catalog pages |

### Touch Targets

- All interactive elements maintain 44px minimum touch target on mobile, even when visually compact (flavor chips, nav icons)
- Product cards have full-surface tap area, not just the text or image region
- Bottom-sticky CTA bar on mobile PDP uses 56px height for comfortable thumb reach
- Spacing between adjacent tappable elements never drops below 8px

### Collapsing Strategy

- Desktop mega-menu with product category previews collapses to slide-in drawer on mobile
- Footer four-column layout stacks into accordion sections on mobile with chevron toggles
- Comparison table becomes horizontally scrollable with sticky first column on screens below 1128px
- Hero split layouts (image + text side by side) stack to image-above-text on mobile
- Bundle cards shift from horizontal row to vertical stack below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors could be extracted from automated site crawl — the site likely loads its design tokens via JavaScript bundles or uses anti-bot protection. Colors listed above are based on widely-observed SodaStream brand materials (teal primary, navy secondary) but exact hex values may differ from current production site.
- No font-family stacks were detected in static HTML — the geometric sans-serif used is loaded dynamically. The Gotham/Proxima Nova approximation reflects the visual style but the actual licensed typeface may differ.
- No meta theme-color was present, suggesting the mobile browser chrome color is not explicitly set.
- Exact border-radius values on production components could not be measured; the rounded scale uses standard increments that visually approximate the observed softness.
- Animation/motion tokens (easing curves, duration scales) were not extractable and are not specified here.
- Dark mode treatment is not documented — the site does not appear to offer a system-preference dark mode at time of analysis.
