---
version: alpha
name: "Brooks"
source_url: "https://www.brooksrunning.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A performance running brand that uses a restrained palette anchored on a deep, confident blue (#1a2b4c) as its primary voltage — not the electric neons of competitors, but a saturated navy that reads as endurance and precision. The brand's canvas is a clean white (#ffffff), with body text in a near-black (#1a1a1a) that keeps readability high across product detail pages and training guides. Brooks trusts a single accent — a vibrant energy orange (#ff6b35) — to drive CTAs and highlight performance metrics, creating a visual system that feels more like a technical lab than a lifestyle magazine. Typography runs on a geometric sans-serif (likely a proprietary or licensed face like "Brooks Standard" or a close relative of DIN or Trade Gothic) at moderate weights — display headlines sit at 32px weight 600, body copy at 16px weight 400, and button labels at 14px weight 500 — prioritizing clarity over personality. Cards and buttons use a gentle 8px radius (`{rounded.sm}`), while hero sections and feature panels employ a more generous 16px (`{rounded.md}`) to soften the technical edge. The product grid uses a 4-column layout on desktop, collapsing to 2 on tablet and 1 on mobile, with each card featuring a 3:4 aspect ratio image, a bold product name in 18px weight 600, and a subdued price in 14px weight 400. The brand's signature design move is the "Run Happy" badge — a small, pill-shaped tag (`{rounded.full}`) in the primary blue with white text, applied to shoes that meet the brand's cushioning and support standards. Navigation is a fixed top bar with a logo lockup on the left, a centered search bar with a 40px height and 8px radius, and utility icons (account, cart) on the right. The footer is dense with links in 14px weight 400, organized under 16px weight 600 category headers, all on a light gray surface (#f5f5f5). The overall mood is athletic but serious — the brand doesn't shout; it performs.

colors:
  primary: "#1a2b4c"
  primary-active: "#0f1d33"
  primary-disabled: "#a0a8b8"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d0d0d0"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#ff6b35"
  accent-orange-active: "#e05520"
  accent-green: "#2ecc71"
  badge-blue: "#1a2b4c"
  badge-text: "#ffffff"
  star-rating: "#ff6b35"
  error: "#d32f2f"
  success: "#2ecc71"

typography:
  display-xl:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Brooks Standard', 'DIN 2014', 'Trade Gothic', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
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
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-image:
    aspectRatio: "3:4"
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    position: "absolute"
    top: "12px"
    left: "12px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: "400px"
  hero-banner-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: "300px"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  badge-run-happy:
    backgroundColor: "{colors.badge-blue}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and "Find Your Fit". Rendered in the brand's deep blue (`{colors.primary}`) with white text (`{colors.on-primary}`) and an 8px radius (`{rounded.sm}`). On hover, shifts to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}` with white text. All primary buttons are uppercase per `{typography.button-md}`.

**`button-secondary`** — Used for "Learn More" and "View Details" actions. A white button (`{colors.canvas}`) with a 2px solid blue border (`{colors.primary}`) and blue text. Same 8px radius and uppercase treatment as primary. Hover state fills the background with `{colors.primary}` and flips text to white.

**`button-accent`** — The energy orange variant (`{colors.accent-orange}`) reserved for high-impact CTAs like "Get Started" or "Join Run Happy". Follows the same sizing and radius as primary. Hover shifts to `{colors.accent-orange-active}`.

**`button-pill`** — A compact, fully rounded pill button (`{rounded.full}`) used for secondary actions like "Filter" or "Sort". Smaller typography (`{typography.button-sm}`) and tighter padding (8px 20px) make it suitable for inline use.

### Cards
**`product-card`** — The core product display unit, a white card (`{colors.surface-card}`) with a subtle drop shadow. The image occupies the top portion at a 3:4 aspect ratio with rounded top corners (`{rounded.sm}`). Below, the product name uses `{typography.title-sm}` (16px, weight 600) and the price uses `{typography.body-md}` (16px, weight 400). A "Run Happy" badge (`{badge-run-happy}`) overlays the top-left of the image for qualifying products.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, white background (`{colors.canvas}`) with a subtle bottom border (`{colors.hairline-soft}`). The logo sits left-aligned, a centered search bar (`{search-bar}`) provides product discovery, and utility icons (account, cart) sit right-aligned. Active nav links show a 2px bottom border in `{colors.primary}`.

**`search-bar`** — A 40px tall input on a light gray background (`{colors.surface-soft}`) with an 8px radius. On focus, the border thickens to 2px and turns `{colors.primary}`. Placeholder text uses `{typography.body-sm}` in `{colors.muted}`.

### Forms
**`text-input`** — Standard form input at 44px height with 12px 16px padding. White background, 1px hairline border (`{colors.hairline}`), 8px radius. Focus state uses a 2px `{colors.primary}` border. Error state uses a 2px `{colors.error}` border.

**`select-input`** — Same dimensions and styling as text input, used for dropdowns like size and quantity. Includes a custom chevron icon in `{colors.muted}`.

### Badges & Tags
**`badge-run-happy`** — A small, fully rounded pill (`{rounded.full}`) in the brand blue (`{colors.badge-blue}`) with white uppercase text (`{typography.badge}`). Applied to product cards and detail pages to indicate cushioning or support level. Padding is 4px 12px.

**`filter-chip`** — A pill-shaped filter option (`{rounded.full}`) with white background and 1px hairline border. Active state fills with `{colors.primary}` and removes the border. Used in category and search result filtering.

### Hero
**`hero-banner`** — Full-width hero section with a minimum height of 400px, using `{colors.primary}` as background and `{colors.on-primary}` for text. The headline uses `{typography.display-xl}` (32px, weight 600). A variant (`{hero-banner-accent}`) uses `{colors.accent-orange}` for promotional or seasonal campaigns.

### Footer
**`footer`** — A dense footer section on `{colors.surface-soft}` background. Links use `{typography.link}` (14px, weight 400) in `{colors.muted}`, while category headings use `{typography.title-sm}` (16px, weight 600) in `{colors.ink}`. Organized in a 4-column grid on desktop, collapsing to 2 columns on tablet and 1 on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, stacked footer, hamburger navigation, search bar collapses to icon |
| Tablet | 744–1128px | 2-column product grid, 2-column footer, nav links collapse to icon-only, search bar remains visible |
| Desktop | 1128–1440px | 4-column product grid, 4-column footer, full nav links, centered search bar |
| Wide | > 1440px | Max-width container at 1440px, centered content, same as desktop with increased whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum height of 44px for touch accessibility
- Filter chips and badges are at least 36px tall for comfortable tapping
- Nav bar icons have a 44x44px tap area even when the visual icon is smaller
- Product card images link to detail pages with a minimum 48px tap area on mobile

### Collapsing Strategy
- Navigation links collapse to a hamburger menu below 744px
- The search bar collapses to a search icon that expands to a full-width input on tap below 744px
- The product grid collapses from 4 columns to 2 at 1128px, and to 1 at 744px
- The footer collapses from 4 columns to 2 at 1128px, and to 1 at 744px
- Hero banners stack content vertically below 744px, with text above imagery

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hex colors were available from the live site due to an "Access Denied" page being served. The color palette above is based on the brand's known visual identity from public marketing materials and should be verified against the actual production site.
- No font-family declarations were extracted. The typography stack uses a best-guess combination of proprietary Brooks fonts and common geometric sans-serif fallbacks. Actual font names and weights should be confirmed from the live site's CSS.
- Hover and focus states for all components are inferred from common patterns and should be validated against the production site.
- Error and success states for forms are assumed and may differ in actual implementation (e.g., error message placement, icon usage).
- The "Run Happy" badge and its placement logic (which products receive it) is based on public knowledge of the brand's cushioning classification system (DNA Loft, BioMoGo DNA, etc.) and may not reflect the current site's implementation.
- Dark mode styling is not defined; the brand may not support it.
- The brand's sub-brand or collection-specific palettes (e.g., "Ghost", "Glycerin", "Adrenaline" series) are not captured here.
- Animation and transition timings (ease-in-out durations, micro-interactions) are not specified.
- The site may use a custom icon set (for shoes, apparel, accessories categories) that is not documented here.
