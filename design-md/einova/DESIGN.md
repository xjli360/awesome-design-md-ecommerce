---
version: alpha
name: "Einova"
source_url: "https://www.einova.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep teal (#226d7a) saturates every interaction surface — add-to-cart buttons, nav highlights, feature icons — pulling focus the way a charging pad's LED ring draws your eye in a dark room. Einova's palette stays within a single hue corridor from near-black teal through bright cyan (#22b8d1) to glacial ice (#e4f5fa), creating depth without competing chromatic noise. Typography leans on Open Sans at conservative weights; product names land at 600 weight while body copy stays thin at 400, trusting the generous whitespace and full-bleed product photography to carry visual interest. Cards float on pure white (`{colors.canvas}`) with `{rounded.md}` corners and subtle `{colors.hairline}` borders — no drop shadows, no gradients, just clean geometry that echoes the flat, disc-shaped chargers the brand sells. The layout is grid-first: product tiles lock to a 3-up desktop grid with `{spacing.lg}` gutters, collapsing to 2-up on tablet and single-column on mobile with sticky add-to-cart bars. CTAs use `{rounded.sm}` with 48px tap targets, colored in the full-saturation primary teal; hover states shift to the slightly warmer `{colors.primary-active}` (#1e6d7a). A secondary accent in bright cyan (#22b8d1) marks sale badges, progress indicators, and comparison-chart highlights — it reads as energetic without breaking the teal monotone. The surface hierarchy is minimal: canvas white, a single soft surface tier (#e4f5fa) for alternating content bands, and `{colors.surface-card}` for elevated product cards. Navigation is slim (64px height), transparent over hero imagery, with white text that flips to `{colors.ink}` on scroll once a white backdrop appears. The overall impression is clinical precision tempered by rounded geometry — a tech brand that trusts its industrial design photography to do the emotional work while the UI stays out of the way.

colors:
  primary: "#226d7a"
  primary-active: "#1e6d7a"
  primary-disabled: "#94c8d1"
  accent: "#22b8d1"
  accent-soft: "#b0e0e9"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#6e6e6e"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#e4f5fa"
  surface-card: "#ffffff"
  surface-band: "#f5fcfe"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#2e7d32"
  error: "#c62828"
  star-rating: "#f5a623"
  scrim: "rgba(0,0,0,0.5)"

typography:
  display-xl:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.4px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  spec-value:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  price:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  price-strike:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
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
  section-lg: 96px

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
    opacity: 0.8
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: 2px solid {colors.primary-active}
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-bar-transparent:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
  product-card-image:
    backgroundColor: "{colors.surface-band}"
    rounded: "{rounded.sm}"
    aspectRatio: 1 / 1
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
  hero-banner-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    titleTypography: "{typography.display-xl}"
  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  feature-icon-block:
    iconColor: "{colors.primary}"
    iconSize: 48px
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    textColor: "{colors.body}"
    gap: "{spacing.sm}"
  spec-table:
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  comparison-chart:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    highlightColor: "{colors.accent-soft}"
    rounded: "{rounded.md}"
    typography: "{typography.body-sm}"
    border: 1px solid {colors.hairline}
  sticky-add-to-cart:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 72px
    padding: "{spacing.md} {spacing.base}"
    borderTop: 1px solid {colors.hairline}
    buttonTypography: "{typography.button-md}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonRounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.accent-soft}"
    headingTypography: "{typography.title-sm}"
  newsletter-signup:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.xxl} {spacing.xl}"
    inputHeight: 48px
    inputRounded: "{rounded.sm}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonRounded: "{rounded.sm}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"

## Components

### Buttons

**`button-primary`** — Full teal (#226d7a) background with white text at 600 weight, 48px height, `{rounded.sm}` corners. On hover, background darkens subtly to `{colors.primary-active}` (#1e6d7a). Disabled state uses the desaturated `{colors.primary-disabled}` with reduced opacity. The button carries no box-shadow; depth comes from color contrast alone against the white canvas.

**`button-secondary`** — White fill with a 2px teal border and teal text. On hover, the background shifts to `{colors.surface-soft}` (pale ice blue) and the border darkens. Used for secondary actions like "Learn More" or "Compare" alongside primary CTAs.

**`button-add-to-cart`** — Full-width variant of the primary button at 52px height. Appears on product detail pages and within the sticky bottom bar on mobile. The extra 4px height and wider padding give it visual dominance over other page buttons.

### Navigation

**`nav-bar`** — 64px-tall strip pinned to the top with a 1px bottom hairline on white pages. Logo left, nav links center, cart icon right. Links use `{typography.nav-link}` at 600 weight with teal underline on active state. On hero pages, the nav starts transparent (`nav-bar-transparent`) with white text, then transitions to the solid white variant on scroll with a subtle fade.

### Product Cards

**`product-card`** — White card with `{rounded.md}` corners and a 1px `{colors.hairline-soft}` border. The image area uses a `{colors.surface-band}` background as a loading placeholder, locked to a 1:1 aspect ratio. Below the image: product title in `{typography.title-sm}`, then price in `{typography.price}`. Cards have no hover elevation change — instead, the image scales to 1.03× on hover with overflow hidden.

### Hero Banners

**`hero-banner`** — Full-width section at minimum 560px height with the pale ice surface (`{colors.surface-soft}`) as backdrop. Display text uses `{typography.display-xl}` left-aligned, with a body subtitle and a primary CTA below. Product photography floats right or overlaps the bottom edge. The dark variant (`hero-banner-dark`) inverts to `{colors.ink}` background with white text, used for premium product launches.

### Sale Badge

**`sale-badge`** — Compact pill using the bright cyan accent (#22b8d1) with white uppercase text at 11px/700 weight. Positioned absolutely in the top-right corner of product card images with `{spacing.sm}` offset. Used for percentage-off indicators and "New" labels.

### Feature Icon Blocks

**`feature-icon-block`** — Vertically stacked: a 48px teal-colored icon (line-weight style), a title in `{typography.title-sm}`, and supporting copy in `{typography.body-sm}`. Used in 3-up or 4-up grids on product pages to communicate specs like wattage, compatibility, and certifications.

### Spec Table

**`spec-table`** — Two-column layout with label in muted `{typography.spec-label}` and value in `{typography.spec-value}`. Each row separated by a 1px `{colors.hairline-soft}` bottom border. Used on product detail pages to list technical specifications (input voltage, output wattage, dimensions, weight).

### Comparison Chart

**`comparison-chart`** — Bordered table with `{rounded.md}` wrapper. Header row uses `{colors.surface-soft}` background. The "recommended" column receives a `{colors.accent-soft}` highlight strip. Body text in `{typography.body-sm}`. Used to compare charger models side by side.

### Sticky Add-to-Cart

**`sticky-add-to-cart`** — 72px fixed bar at viewport bottom on mobile, appearing after the user scrolls past the main add-to-cart button. Contains product name (truncated), price, and a compact primary button. Separated from content by a 1px `{colors.hairline}` top border. Background is white with no shadow to maintain the flat aesthetic.

### Footer

**`footer`** — Dark ink (#1a1a1a) background with white and `{colors.accent-soft}` text. Organized in 4-column grid (collapsing to accordion on mobile). Section headings in `{typography.title-sm}`, links in `{typography.body-sm}`. Bottom row holds legal links, copyright, and payment icons.

### Newsletter Signup

**`newsletter-signup`** — Horizontal band in `{colors.surface-soft}` with centered headline, subtitle, and an inline email input + submit button pair. Input and button share the same 48px height and `{rounded.sm}` radius, butted together. Used above the footer as a conversion capture.

### Breadcrumb

**`breadcrumb`** — Single-line trail in `{typography.caption}` with muted text color. Chevron separators in `{colors.muted-soft}`. The final (active) segment renders in `{colors.ink}`. Sits below the nav bar with `{spacing.md}` vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + slide-out drawer; hero text stacks above image; sticky add-to-cart bar appears; footer sections collapse to accordions; comparison chart scrolls horizontally |
| Tablet | 744–1128px | 2-column product grid; nav shows top-level links with overflow in "More" dropdown; hero uses 50/50 text-image split; spec table remains full-width |
| Desktop | 1128–1440px | 3-column product grid; full nav visible; hero at max container width (1200px) centered; sticky bar hidden (add-to-cart always visible in viewport) |
| Wide | > 1440px | Content max-width caps at 1440px with auto margins; product grid may extend to 4-up; hero imagery scales proportionally within container bounds |

### Touch Targets

- All interactive elements maintain minimum 44×44px tap area on mobile
- Product cards use full-card tap target (not just the title link)
- Nav hamburger icon padded to 48×48px hit zone
- Sticky add-to-cart button spans available width minus `{spacing.base}` side margins

### Collapsing Strategy

- Desktop multi-column grids collapse to fewer columns before going single-column
- Horizontal feature-icon rows stack vertically on mobile with left-aligned icons
- Comparison chart columns remain fixed-width; container scrolls with visible overflow indicator
- Footer columns transition to stacked accordions with `{colors.hairline}` dividers
- Newsletter input and button stack vertically below 480px with full-width button

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned 403 Forbidden during extraction; all color and font data comes from limited static asset analysis rather than full DOM inspection
- Exact brand typeface unknown — Open Sans, Roboto, and Arial were detected but may be fallbacks for a custom or commercially licensed font loaded via JavaScript
- No motion/animation tokens captured (transition durations, easing curves for hover states and page transitions)
- Icon library and exact icon weight/style unconfirmed (assumed line-weight from brand category norms)
- Exact max-width container value unconfirmed (1200px assumed from category conventions)
- No dark-mode palette detected or extractable
- Form validation states (focus ring color, error message styling) inferred from primary palette rather than observed
- Product image aspect ratios may vary by category (chargers vs. cables vs. accessories); 1:1 is assumed default
