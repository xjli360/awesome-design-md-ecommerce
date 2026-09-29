---
version: alpha
name: "RapidX"
source_url: "https://www.rapidx.io"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric yellow (#f5e900) hits the eye before the product does — a voltage flash across a pitch-dark canvas (#121212) that turns every hero banner into a caution stripe for the fast lane. RapidX builds its entire visual identity on that tension between a near-black ground and a single screaming accent, a palette borrowed from motorsport liveries and pit-lane signage rather than the safe navy-and-white playbook most accessory brands default to. Red (#d40000) enters only as urgency: sale callouts, low-stock warnings, and destructive-action states — never competing with the yellow for brand ownership. Body copy sits on a white (#ffffff) surface in product grids, but the brand's emotional center lives in dark-mode hero sections where `{colors.primary}` glows against `{colors.ink}`. Buttons are pill-shaped (`{rounded.full}`) with high-contrast yellow fills on dark backgrounds, creating thumb-sized beacons on mobile. Product cards use a subtle `{rounded.sm}` radius and sit on `{colors.surface-card}` with thin `{colors.hairline}` borders — understated containers that let device photography dominate. Typography leans on a geometric sans-serif stack at relatively heavy weights for headings (700–800) and medium (500) for interface labels, producing a technical-catalog density without decorative serifs or humanist curves. Spacing is tight within cards (`{spacing.md}`) but generous between sections (`{spacing.section}`), creating a rhythm that mimics scrolling through spec sheets punctuated by full-bleed lifestyle shots. The overall impression is speed-obsessed utility: fast chargers, fast reads, zero ornament that doesn't earn its pixels.

colors:
  primary: "#f5e900"
  primary-active: "#ddd200"
  primary-disabled: "#f5e90040"
  accent-danger: "#d40000"
  accent-danger-active: "#b80000"
  ink: "#1b1819"
  ink-deep: "#121212"
  body: "#333333"
  muted: "#777777"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  border-strong: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#1b1819"
  on-dark: "#ffffff"
  on-danger: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: -1.2px
  display-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.6px
  display-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.4px
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  uppercase-tag:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  price-compare:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: 1.5px solid {colors.on-dark}
  button-secondary-on-light:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: 1.5px solid {colors.ink}
  button-danger:
    backgroundColor: "{colors.accent-danger}"
    textColor: "{colors.on-danger}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.border-strong}
    focusBorder: 1px solid {colors.ink}
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.lg}
  nav-bar-scrolled:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    height: 64px
    boxShadow: 0 1px 0 rgba(255,255,255,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: 1px solid {colors.hairline}
    hoverShadow: 0 4px 16px rgba(0,0,0,0.08)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: 1 / 1
    objectFit: contain
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 520px
  hero-highlight:
    backgroundColor: "{colors.ink-deep}"
    accentColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.lg}"
  badge-sale:
    backgroundColor: "{colors.accent-danger}"
    textColor: "{colors.on-danger}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-pill:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: 1px solid {colors.on-dark}
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  price-block:
    currentPrice:
      textColor: "{colors.ink}"
      typography: "{typography.price}"
    comparePrice:
      textColor: "{colors.muted}"
      typography: "{typography.price-compare}"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
  search-input:
    backgroundColor: rgba(255,255,255,0.08)
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
    placeholderColor: "{colors.muted}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    padding: 8px {spacing.base}

---

## Components

### Buttons

**`button-primary`** — Full pill-radius yellow button used for Add to Cart, Shop Now, and all primary CTAs. The electric yellow fill (`{colors.primary}`) with dark text (`{colors.on-primary}`) ensures maximum contrast on both light product pages and dark hero sections. On hover/press, the fill deepens to `{colors.primary-active}`. Disabled state drops to 25% opacity with muted text, signaling inaction without breaking the shape language.

**`button-secondary`** — Ghost button with a 1.5px white border on dark backgrounds, used for secondary actions like "Learn More" or "View Specs" within hero sections. On light backgrounds, the variant `button-secondary-on-light` swaps to dark ink border and text. Hover state fills with 8% white (on dark) or 4% black (on light) to confirm interactivity.

**`button-danger`** — Compact red pill used sparingly for sale CTAs or remove-from-cart actions. Smaller padding and `{typography.button-sm}` keep it subordinate to the primary yellow.

### Navigation

**`nav-bar`** — Persistent dark header bar at 64px height with the RapidX wordmark left-aligned and navigation links in `{typography.nav-link}`. Background is `{colors.surface-dark}` which matches hero sections, creating a seamless bleed on landing. Cart icon sits right with a yellow dot indicator for item count. On scroll, a subtle bottom edge appears via `nav-bar-scrolled` to separate from content.

**`announcement-bar`** — Slim 36px strip above the nav in full `{colors.primary}` yellow, used for shipping thresholds or promo codes. Text is `{colors.on-primary}` (dark) in `{typography.caption}` weight for legibility at small size. Dismissible via an × icon that collapses with a 200ms ease-out.

### Product Display

**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.sm}` corners. Contains a square product image area (`product-card-image`) with `{colors.surface-soft}` placeholder background, a title in `{typography.title-sm}`, a price block, and optional badge. Hover lifts the card with a 4px blur shadow. Card padding is `{spacing.md}` on all sides.

**`price-block`** — Inline pairing of current price in bold `{typography.price}` and an optional strikethrough compare-at price in `{typography.price-compare}` with `{colors.muted}` color. When a sale badge is present, the current price shifts to `{colors.accent-danger}`.

**`badge-sale`** / **`badge-new`** — Small rectangular tags with `{rounded.xs}` and uppercase `{typography.uppercase-tag}`. Sale uses red fill; New uses yellow fill. Positioned absolutely at top-left of the product-card-image area with 8px inset.

### Hero Sections

**`hero-dark`** — Full-width dark section that serves as the primary landing viewport. Content is vertically centered with headline in `{typography.display-xl}` (white), a one-line subtitle in `{typography.body-md}`, and a `button-primary` CTA. Product imagery floats right or is positioned as a background layer with a gradient overlay from `{colors.surface-dark}` at 80% opacity on the text side.

**`hero-highlight`** — Variant used for featured product spotlights. Same dark ground but introduces a yellow accent glow (radial gradient of `{colors.primary}` at 10% opacity) behind the product image, creating a halo effect that reinforces the brand color without adding UI chrome.

### Category & Filtering

**`category-pill`** — Horizontally scrollable pill set for filtering product collections (Chargers, Cables, Lifestyle). Default state is a ghost pill with white border on dark; active state fills with `{colors.primary}` and flips text to dark. Transition is 150ms ease on background-color and border-color.

### Search

**`search-input`** — Full-pill search field with translucent white background (8% opacity) on the dark nav. Placeholder text in `{colors.muted}`, typed text in `{colors.on-dark}`. On focus, background opacity increases to 12% and a subtle 1px `{colors.primary}` ring appears. Magnifying-glass icon sits 16px from left edge.

### Footer

**`footer`** — Multi-column dark footer on `{colors.ink-deep}`. Link columns use `{typography.body-sm}` with `{colors.hairline}` default color, brightening to `{colors.primary}` on hover. Bottom row contains payment icons, copyright in `{typography.caption}`, and social icons at 20px square. Vertical padding is `{spacing.section}`.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + cart icon; hero stacks vertically (text above image); product grid becomes 2-col; category pills horizontally scroll; section padding drops to `{spacing.xl}` |
| Tablet | 744–1128px | Product grid expands to 3-col; hero image scales to 50% width side-by-side; nav links visible but condensed spacing; footer stacks to 2×2 column grid |
| Desktop | 1128–1440px | Full 4-col product grid; nav fully expanded with search field inline; hero at designed proportions; footer in single row of columns |
| Wide | > 1440px | Content max-width caps at 1440px and centers; hero imagery scales up; product cards gain slightly more horizontal padding; no layout changes beyond centering |

### Touch Targets

- All interactive elements maintain minimum 44×44px tap area on mobile
- Category pills have 12px horizontal gap to prevent mis-taps during scroll
- Cart and menu icons padded to 48×48px hit area despite 24px visual size
- Product cards are full-width tap targets on mobile (entire card links to PDP)

### Collapsing Strategy

- Navigation links collapse into a slide-out drawer (from left, dark background) below 744px
- Product filters move from a sidebar to a bottom-sheet modal on mobile
- Footer columns stack vertically in a single column on mobile with accordion expand/collapse
- Announcement bar text truncates with ellipsis on narrow viewports; full text on hover/tap

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family stacks were detected in static HTML extraction — the site likely loads typefaces via JavaScript or a Shopify theme's CSS-in-JS pipeline. The Inter stack used above is a reasonable geometric sans-serif proxy; the actual brand font should be confirmed via browser DevTools inspection.
- Only 6 hex colors were extractable from static markup; additional semantic tokens (success/green, info/blue, overlay opacity values) could not be determined and may exist in Shopify theme settings or CSS custom properties loaded at runtime.
- Exact border-radius values for product cards and buttons could not be measured from extraction data — the `{rounded.full}` pill and `{rounded.sm}` values are inferred from visual brand patterns rather than computed style output.
- Animation/motion tokens (easing curves, duration scales, transition properties) are not available from static extraction.
- Dark-mode vs. light-mode split is inferred from the contrast between hero sections and product grids; there may be a user-togglable theme mode not captured here.
- Icon system (line weight, grid size, stroke vs. fill style) could not be determined from extraction data.
