---
version: alpha
name: "Level Up Video Games"
source_url: "https://levelupvideogames.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A neon-green #48dd21 voltage against a deep purple #221155 canvas — the brand reads like a retro arcade cabinet that somehow also sells tabletop games and used NES cartridges. That electric green is the primary CTA color, the price-tag badge, the "Add to Cart" pulse, and the only saturated hue in a palette otherwise built from grays (#dfdfdf, #989898, #454545) and blacks (#1a1a1a, #252525). The purple background is the brand's signature atmospheric move: it wraps the entire site in a dark, moody glow that makes the green pop like a CRT monitor in a dimly lit basement. Product cards sit on #f7f7f7 or #ffffff surfaces with {rounded.sm} corners, while category badges use that same green on white for instant scanability. The typography system is unknown (no font-family declarations found on the live site), but the visual hierarchy relies on weight contrast against the dark canvas — white or light-gray text on purple, green accents drawing the eye to actions. The overall effect is less "clean retail" and more "gaming den that happens to have a checkout flow."

colors:
  primary: "#48dd21"
  primary-active: "#3ab81a"
  primary-disabled: "#a5e896"
  ink: "#1a1a1a"
  body: "#454545"
  muted: "#757575"
  muted-soft: "#989898"
  hairline: "#dfdfdf"
  hairline-soft: "#e8e8e8"
  canvas: "#221155"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-green: "#8bc34a"
  badge-green: "#48dd21"
  error-red: "#d14343"
  link-blue: "#4496f6"
  dark-surface: "#2d2d2d"
  dark-muted: "#4f4f4f"

typography:
  display-xl:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  button-lg:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-outline-active:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    shadow: "0 0 0 3px rgba(72, 221, 33, 0.2)"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 48px
  search-bar-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    shadow: "0 4px 12px rgba(0, 0, 0, 0.1)"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-badge-sold-out:
    backgroundColor: "{colors.error-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  price-display:
    textColor: "{colors.primary}"
    typography: "{typography.title-md}"
  price-display-sale:
    textColor: "{colors.error-red}"
    typography: "{typography.title-md}"
  category-tag:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-active:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in electric green #48dd21 on white text. Used for "Add to Cart," "Checkout," and primary purchase flows. On hover, shifts to `{colors.primary-active}` (#3ab81a) for a subtle darkening. Disabled state uses `{colors.primary-disabled}` (#a5e896) to signal inactivity without losing brand identity. Height is 44px with `{rounded.sm}` corners.

**`button-secondary`** — An inverted variant on the dark purple canvas: transparent background with green text. Used for secondary actions like "View Details" or "Continue Shopping." Active state fills with `{colors.dark-surface}` (#2d2d2d) to provide a hover target. Same 44px height and `{rounded.sm}` as primary.

**`button-outline`** — A bordered variant for actions on the dark canvas, like "Sign In" or "Wishlist." Uses a 1px solid white border on transparent background, white text. Active state fills with `{colors.dark-surface}`. Useful for low-emphasis actions that still need a visible boundary.

### Cards
**`product-card`** — The standard product display card on white `{colors.surface-card}` background. Contains product image, title in `{typography.body-sm}`, price in `{typography.title-md}` green, and an optional `{product-badge}`. Corners are `{rounded.sm}`. On hover, elevates with a subtle box-shadow (0 4px 12px rgba(0,0,0,0.1)) to signal interactivity.

**`product-badge`** — Small green pill badges for condition labels like "New," "Used," or "Pre-owned." Uses `{typography.badge}` (11px, bold, uppercase) on green background. Sold-out items switch to `{product-badge-sold-out}` with red `{colors.error-red}` background.

**`category-tag`** — Dark-surface pills for filtering by console or category (e.g., "Nintendo," "PS5," "Board Games"). Active state switches to green background for clear selection feedback. Uses `{rounded.full}` for a pill shape.

### Navigation
**`nav-bar`** — The persistent top navigation bar on the deep purple `{colors.canvas}` background. Height 64px, contains logo, category links, and search icon. Links use `{typography.nav-link}` in white, with active state switching to green `{colors.primary}`. The bar is fixed or sticky on desktop, collapsing to a hamburger on mobile.

**`nav-link-active`** — Active navigation link in green. No background fill — just text color change to `{colors.primary}`. Inactive links remain white.

### Forms
**`text-input`** — Standard text input on white background with `{rounded.sm}` corners and 44px height. On focus, gains a green border and a subtle green box-shadow ring (0 0 0 3px rgba(72, 221, 33, 0.2)) for accessibility.

**`search-bar`** — A full-rounded pill input for the site search, 48px tall. White background, `{rounded.full}`, with a magnifying glass icon. On focus, border shifts to green. Used prominently in the header or hero area.

### Footer
**`footer`** — Full-width footer on the dark purple canvas. Contains link columns, social icons, and copyright text. Links use `{colors.muted-soft}` (#989898) for subtle contrast against the dark background. Typography is `{typography.body-sm}` for text and `{typography.link}` for links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; search bar moves to expandable overlay; category tags stack vertically; footer links collapse to accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only; search bar remains visible but smaller; category tags wrap in a horizontal scroll |
| Desktop | 1128–1440px | Three-column product grid; full nav with all categories; search bar in header; category tags in a horizontal strip |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; nav and search remain as desktop |

### Touch Targets
- All buttons and interactive elements minimum 44px height (buttons, inputs, nav links)
- Icon buttons 40px × 40px minimum
- Category tags 32px minimum height
- Search bar 48px height on all breakpoints
- Product card tap target includes entire card area

### Collapsing Strategy
- Navigation links collapse to hamburger menu on mobile (< 744px)
- Search bar collapses to icon-only on mobile, expands on tap
- Footer link columns collapse to accordion sections on mobile
- Category tag strip collapses to horizontal scroll on tablet and mobile
- Product grid reduces columns progressively (4 → 3 → 2 → 1)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found on the live site; the typography system uses Inter as a reasonable modern sans-serif fallback, but the actual brand font is unknown
- Hover and focus states for many components are inferred from common patterns rather than extracted from live CSS
- Error states for form inputs (validation, error messages) are not documented
- Dark mode is not present on the live site; all pages use the purple canvas
- Sub-brand or promotional color variants (e.g., holiday themes, clearance sales) are not captured
- The extracted hex list includes many grays that may be from third-party widgets or checkout integrations; the true brand palette is likely smaller
- Animation and transition timing values (e.g., button hover duration, card elevation speed) are not documented
- Loading states (skeleton screens, spinners) are not specified
- The checkout flow (Shopify or custom) is unknown; payment button styles may differ
- Accessibility contrast ratios between green text on purple background should be verified
- The specific shade of purple (#221155) may vary in different contexts (e.g., footer vs. header)
