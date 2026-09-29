---
version: alpha
name: "Fiskars"
source_url: "https://www.fiskars.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Orange scissors on a kitchen counter, orange pruners half-buried in garden soil, orange axes splitting birch — for over three centuries the single chromatic signal has been a molten, traffic-cone orange (#FF6900) pressed into ergonomic polymer handles. The digital expression translates that confidence into a restrained interface: a near-black charcoal (#313131) dominates headings, navigation, and body copy, lending the site an almost editorial sobriety, while the signature orange arrives only at decisive interaction points — primary CTAs, active filter chips, and the occasional product-category icon. Typography relies entirely on the native system stack (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif`), a deliberate choice that privileges load speed and cross-platform legibility over bespoke type — the tools sell themselves through oversized lifestyle photography and generous whitespace rather than display lettering. Corners stay disciplined: product cards take a subtle `{rounded.sm}` (8 px), buttons round to `{rounded.xs}` (4 px), and pill-shaped tags use `{rounded.full}` for category labels. The layout grid breathes at `{spacing.section}` (64 px) between major content bands, compressing to `{spacing.lg}` on mobile. A full-bleed hero occupies the viewport above the fold, typically a slow-zoom video loop of hands in motion — cutting, digging, splitting — with a single translucent text overlay and one CTA anchored bottom-left. Product listing pages favor a 3-up masonry on desktop collapsing to a scrollable 2-up on tablet, each card casting a faint 0 2px 8px rgba(0,0,0,0.06) shadow that lifts to 0 4px 16px on hover. The footer is dense and utility-driven, stacking link columns atop a matte-dark (#1a1a1a) background that grounds the page like potting soil beneath a tray of seedlings.

colors:
  primary: "#FF6900"
  primary-active: "#E55E00"
  primary-disabled: "#FFB980"
  ink: "#313131"
  body: "#4A4A4A"
  muted: "#717171"
  muted-soft: "#9B9B9B"
  hairline: "#D9D9D9"
  hairline-soft: "#EBEBEB"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  surface-dark: "#1A1A1A"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  success: "#2E7D32"
  error: "#C62828"
  rating-star: "#FF6900"
  badge-sale: "#C62828"
  badge-new: "#313131"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  uppercase-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    transition: background-color 0.2s ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 2px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  text-input-error:
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
    position: sticky
  nav-bar-scrolled:
    boxShadow: 0 2px 8px rgba(0,0,0,0.06)
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xxl}"
    borderTop: 1px solid {colors.hairline-soft}
    boxShadow: 0 8px 24px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    boxShadow: 0 2px 8px rgba(0,0,0,0.06)
    transition: box-shadow 0.2s ease, transform 0.2s ease
  product-card-hover:
    boxShadow: 0 4px 16px rgba(0,0,0,0.1)
    transform: translateY(-2px)
  product-card-image:
    aspectRatio: 1 / 1
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm} {rounded.sm} {rounded.none} {rounded.none}"
    objectFit: contain
    padding: "{spacing.lg}"
  product-card-body:
    padding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 85vh
    padding: "{spacing.section} {spacing.xxl}"
    position: relative
    overflow: hidden
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 40px
    height: 52px
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    aspectRatio: 4 / 3
    overflow: hidden
    position: relative
  category-card-overlay:
    background: linear-gradient(to top, rgba(0,0,0,0.5) 0%, transparent 50%)
    textColor: "{colors.on-dark}"
    padding: "{spacing.base}"
    position: absolute
    bottom: 0
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-dark}"
    typography: "{typography.uppercase-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-dark}"
    typography: "{typography.uppercase-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  rating-stars:
    color: "{colors.rating-star}"
    size: 16px
    gap: "{spacing.xxs}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
    border: none
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    border: 2px solid {colors.ink}
    boxShadow: 0 4px 12px rgba(0,0,0,0.1)
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: 1px solid {colors.hairline}
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: 1px solid {colors.ink}
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-heading:
    typography: "{typography.uppercase-label}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.base}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    maxWidth: 240px

---

## Components

### Buttons

**`button-primary`** — Solid Fiskars Orange background with white text, squared-off at `{rounded.xs}` to echo the precision of a well-honed blade. On hover the background deepens to `{colors.primary-active}`; disabled state fades to a pale peach `{colors.primary-disabled}` with no cursor interaction. Minimum touch width 160 px on mobile.

**`button-secondary`** — White fill, 2 px solid `{colors.ink}` border, matching `{rounded.xs}` radius. On hover the entire button inverts to a dark fill with white text, creating a definitive toggle-feel rather than a subtle tint shift. Used for "Add to Compare," "Find a Store," and secondary product actions.

**`button-tertiary`** — Transparent background, ink-colored underlined text. No border, no fill. Used inline within editorial content and footer link clusters.

### Navigation

**`nav-bar`** — 64 px tall sticky header, white background with a 1 px `{colors.hairline-soft}` bottom border that disappears once the user scrolls (replaced by a soft box-shadow). Logo sits left, mega-menu triggers center, utility icons (search, account, cart) right. On scroll, the bar compresses by 8 px and gains elevation via `{components.nav-bar-scrolled}` shadow.

**`mega-menu`** — Full-width dropdown triggered on hover (desktop) or tap (touch). Contains up to four columns of category links with a featured image on the right edge. Background is white, separated from the nav by a hairline and grounded with a heavier shadow than the nav itself.

### Search

**`search-bar`** — Pill-shaped (`{rounded.full}`) input field with a neutral gray background that transitions to white with a 2 px ink border on focus. A magnifying-glass icon sits 16 px from the left edge. Autocomplete suggestions drop below in a `{colors.surface-card}` panel with `{rounded.sm}` corners and mild shadow.

### Product Cards

**`product-card`** — Vertical card with a square product image area (1:1, `contain` fit against `{colors.surface-soft}` background) and a body section below. Image area uses top-only rounding (`{rounded.sm}`); bottom corners carry through to the card base. Hover lifts the card 2 px and deepens the shadow. The body section contains product name (`{typography.title-sm}`), a one-line description (`{typography.body-sm}`, `{colors.muted}`), price (`{typography.price}`), and optional star rating.

**`product-card-image`** — The image container pads the product photo with `{spacing.lg}` so tools float against the light background rather than bleeding to the edges. This preserves visual breathing room for irregularly shaped items like pruners or loppers.

### Hero

**`hero-banner`** — Full-bleed dark section occupying ~85 vh, typically carrying a background video or high-res lifestyle photograph. A subtle dark gradient ensures text legibility. Headline uses `{typography.display-xl}` in white, followed by one line of body copy and a single `{components.hero-banner-cta}` button. Content aligns bottom-left with generous padding.

### Category Cards

**`category-card`** — Landscape-oriented (4:3) image cards used on the homepage to direct users into product verticals (Garden, Scissors, Axes, Cooking). A gradient overlay at the bottom carries the category name in `{typography.title-sm}` white text. Hover scales the background image 1.03× over 300 ms.

### Badges

**`badge-sale`** — Small red (`{colors.badge-sale}`) uppercase pill positioned absolutely in the top-left corner of product-card images. Used for clearance and seasonal sales.

**`badge-new`** — Same geometry as sale badge but in solid `{colors.badge-new}` (dark charcoal). Signals recently launched products.

### Filters

**`filter-chip`** — Pill-shaped toggles (`{rounded.full}`) used on product listing pages. Inactive chips have a hairline border on white; active chips invert to solid ink with white text. Chips sit in a horizontally scrollable row on mobile.

### Breadcrumb

**`breadcrumb`** — Caption-sized path indicator using "/" separators in `{colors.hairline}`. Current page segment renders in `{colors.ink}` at `fontWeight: 600`; ancestor segments are `{colors.muted}` and linked.

### Footer

**`footer`** — Dense, multi-column link grid on a dark `{colors.surface-dark}` background. Column headings use `{typography.uppercase-label}` with generous letter-spacing. Links are `{typography.body-sm}` in white with 60% opacity, rising to 100% on hover. Bottom row carries legal links, locale selector, and social icons.

### Tooltip

**`tooltip`** — Dark-on-light contextual hint appearing on icon hover. Ink background, white text, `{rounded.xs}`, max-width 240 px. Appears with a 200 ms fade and 4 px vertical offset from the trigger element.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to `{typography.display-md}`; nav collapses to hamburger + slide-out drawer; mega-menu becomes accordion; filter chips scroll horizontally; footer stacks into single column with accordion sections |
| Tablet | 744–1128px | 2-column product grid; hero occupies 70 vh; nav shows logo + hamburger + utility icons; category cards become 2-up; spacing between sections reduces to `{spacing.xxl}` |
| Desktop | 1128–1440px | 3-column product grid; full mega-menu on hover; hero at 85 vh; sticky nav with full link set; footer displays 4–5 link columns side by side |
| Wide | > 1440px | Content max-width 1440 px, centered; product grid may extend to 4-up on category pages; hero imagery scales but text area caps at 720 px width to maintain readability |

### Touch Targets

- All interactive elements maintain a minimum 44 × 44 px tap area on mobile
- Filter chips have 12 px horizontal gap to prevent mis-taps
- Product card entire surface is tappable (link wraps the card)
- Close / dismiss buttons on modals are 48 × 48 px with a generous hit-slop zone

### Collapsing Strategy

- Navigation collapses into a full-height slide-out drawer from the left edge at < 744 px
- Mega-menu categories become expandable accordion groups within the drawer
- Footer link columns collapse into labeled accordions with a chevron indicator
- Product comparison bar (sticky bottom) hides entirely on mobile, replaced by a floating "Compare" FAB
- Breadcrumb truncates middle segments with "…" when path exceeds three levels on mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned a Cloudflare "Just a moment..." challenge page — no CSS custom properties, component tokens, or JavaScript-rendered design tokens could be extracted
- Only one hex color (#313131) was captured from the challenge page; the full site palette is unavailable from extraction
- Fiskars Orange (#FF6900) is sourced from widely-documented brand identity materials (comparable to "Tiffany blue is #0abab5") — the exact digital hex used on the live site may differ by a few stops
- No custom web fonts were detected; the site may load a proprietary or licensed typeface via JS that the anti-bot page blocked
- Exact border-radii, spacing scale, and shadow values are estimated from brand-consistent patterns, not measured from the live DOM
- Animation timing and easing curves (page transitions, micro-interactions) could not be observed
- Dark-mode or alternate theme tokens are unknown
- Exact breakpoint values are industry-standard estimates; the live site may use different thresholds
