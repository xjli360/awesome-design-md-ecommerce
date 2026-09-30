---
version: alpha
name: "SanDisk"
source_url: "https://www.sandisk.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A red #e10600 pulse drives SanDisk’s digital-physical identity — the same saturated stop-sign red that fires on every primary CTA, product-badge dot, and category-highlight stripe, set against a near-white canvas #f9f7f6 that reads as warm paper rather than sterile white. The brand lives in the gap between industrial reliability and everyday consumer use: its typography runs a single-weight monospace for technical specs (capacity, read speed, interface) while body copy falls back to a clean sans-serif, creating a deliberate rhythm of machine-precision labels and human-friendly paragraphs. Product cards stack on a soft off-white surface #f5f3ef with subtle shadows, each card carrying a small red accent bar at top — a consistent visual anchor that says “this is a SanDisk product” without needing the logo. The secondary palette is unusually wide for a storage brand: a safety-orange #ff7012 for warranty badges, a deep green #00740c for compatibility checkmarks, a muted purple #824dd8 for software download buttons, and a warm gray #dfdfdf for disabled states. Buttons use a sharp 8px radius (`{rounded.sm}`) — not pill-shaped — suggesting precision over friendliness, while search bars and filter chips round to 32px (`{rounded.xl}`) to contrast against the hard-cornered product grid. The overall mood is confident, technical, and slightly warm: a tool brand that knows its audience reads spec sheets but also buys on Amazon.

colors:
  primary: "#e10600"
  primary-active: "#d21920"
  primary-disabled: "#dfdfdf"
  ink: "#2b2b2b"
  body: "#6a6a6a"
  muted: "#b9b9b9"
  muted-soft: "#d2d2d2"
  hairline: "#e3e3e3"
  hairline-soft: "#efefef"
  canvas: "#f9f7f6"
  surface-soft: "#f5f3ef"
  surface-card: "#fffcf9"
  on-primary: "#ffffff"
  accent-orange: "#ff7012"
  accent-green: "#00740c"
  accent-purple: "#824dd8"
  accent-red-soft: "#f24c4c"
  accent-red-badge: "#d55f56"
  accent-gold: "#b58409"
  success-bg: "#d0ffcf"
  link-blue: "#0074f3"

typography:
  display-xl:
    fontFamily: "monospace, 'SF Mono', 'Consolas', 'Liberation Mono', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "monospace, 'SF Mono', 'Consolas', 'Liberation Mono', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "sans-serif, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "sans-serif, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "sans-serif, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "sans-serif, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "sans-serif, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "sans-serif, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-mono:
    fontFamily: "monospace, 'SF Mono', 'Consolas', 'Liberation Mono', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "sans-serif, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  spec-label:
    fontFamily: "monospace, 'SF Mono', 'Consolas', 'Liberation Mono', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "sans-serif, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "sans-serif, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "sans-serif, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "sans-serif, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
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
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-pill-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xl}"
    padding: 8px 20px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xl}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-accent-bar:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.none}"
  product-card-spec:
    typography: "{typography.spec-label}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  badge-warranty:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-compatibility:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-software:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xl}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  software-download-button:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
  capacity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
    height: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Buy Now", "Add to Cart", and "Shop All" actions. Renders in SanDisk red #e10600 on a white label, with an 8px radius (`{rounded.sm}`) that feels precise rather than playful. On hover, the background shifts to `{colors.primary-active}` (#d21920). Disabled state drops to `{colors.primary-disabled}` (#dfdfdf) with `{colors.muted}` text, signaling the button is inert without removing it from layout.

**`button-secondary`** — An outlined alternative for secondary actions like "Compare" or "Learn More". Uses a white canvas background with a 2px `{colors.hairline}` border. Active state thickens the border to `{colors.ink}` and shifts background to `{colors.surface-soft}`. Height matches primary at 48px for alignment in form rows.

**`button-tertiary`** — A text-only link styled as a button, used for "View Details" or "See Specs" within product cards. Transparent background with `{colors.primary}` text. No border or shadow — relies on the red color and 600-weight font to signal clickability.

**`button-pill-accent`** — A special pill-shaped button reserved for promotional or urgency actions (e.g., "Limited Time Offer", "Free Shipping"). Uses `{colors.accent-orange}` (#ff7012) background with a 32px radius (`{rounded.xl}`). Shorter padding than primary (8px 20px) to fit inline with badges.

### Cards
**`product-card`** — The core product display unit across category pages and search results. A white card (`{colors.surface-card}`) on a `{colors.surface-soft}` background with a 1px `{colors.hairline-soft}` border and `{rounded.sm}` corners. Each card carries a 4px red accent bar at the top — a consistent SanDisk signature that ties the product family together visually. Inside, a product image fills the top half, followed by `{typography.title-sm}` for the product name, `{typography.spec-label}` for capacity/speed specs in monospace, and `{typography.product-card-price}` for pricing. Hover state adds a subtle shadow (not yet tokenized — see Known Gaps).

### Navigation
**`top-nav`** — A fixed 72px header bar on `{colors.canvas}` background. Contains the SanDisk logo (left), primary nav links in `{typography.nav-link}` (Products, Support, About), a search bar, and a cart icon. Active nav link gets a 2px `{colors.primary}` bottom border. On scroll, a 1px `{colors.hairline}` bottom border appears. Mobile collapses to a hamburger menu.

**`nav-link-active`** — The active state for top-level navigation items. Uses `{colors.primary}` text with a 2px solid underline in the same red. No background fill — the underline is the only indicator, keeping the header clean.

### Forms & Inputs
**`search-bar`** — A rounded input field (`{rounded.xl}`) with a 1px `{colors.hairline}` border on `{colors.canvas}` background. Placeholder text in `{colors.body}` (#6a6a6a). On focus, the border thickens to 2px `{colors.primary}` — a subtle but clear focus indicator. Height 44px, with 10px 20px padding for comfortable typing.

**`filter-chip`** — Used in category filters (capacity, interface, price range). A pill-shaped chip (`{rounded.xl}`) with `{colors.canvas}` background and `{colors.body}` text, bordered by `{colors.hairline}`. Active state flips to `{colors.primary}` background with white text. Multiple chips can be active simultaneously.

**`capacity-selector`** — A dropdown-style selector for product variants (e.g., 128GB, 256GB, 512GB, 1TB). Uses `{colors.canvas}` background with `{colors.hairline}` border and `{rounded.sm}` corners. Height 44px to match search bar. Selected option highlighted in `{colors.primary}`.

### Badges
**`badge-warranty`** — Orange badge (#ff7012) for warranty information (e.g., "5-Year Warranty"). Uses `{typography.badge}` (11px, 700 weight, uppercase) with 2px 8px padding and `{rounded.xs}` (4px). Inline with product titles or spec lists.

**`badge-compatibility`** — Green badge (#00740c) for compatibility indicators (e.g., "PS5 Compatible", "Works with iPhone 15"). Same typography and sizing as warranty badge.

**`badge-software`** — Purple badge (#824dd8) for software download prompts (e.g., "RescuePRO Deluxe Included"). Used on product detail pages and in checkout flows.

**`badge-sale`** — Red badge (#d55f56) for promotional pricing (e.g., "Sale", "Save 20%"). Slightly softer red than primary to differentiate from brand accents.

### Footer
**`footer-section`** — A dark footer on `{colors.ink}` (#2b2b2b) background with `{colors.muted-soft}` (#d2d2d2) text. Contains four columns: Product Categories, Support, Company, and Legal. Links use `{typography.link}` and lighten to `{colors.on-primary}` on hover. Section padding is `{spacing.xxl}` vertical, `{spacing.lg}` horizontal.

### Software Download
**`software-download-button`** — A purple button (#824dd8) used exclusively for software download CTAs (e.g., "Download RescuePRO", "Get SanDisk Dashboard"). Uses `{typography.button-sm}` with `{rounded.sm}` corners. This purple is intentionally distinct from the red primary system to signal a different action type — downloading software vs. purchasing hardware.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger; filter chips stack vertically; hero section reduces to 32px padding; product cards stack full-width |
| Tablet | 744–1128px | Two-column product grid; top-nav shows abbreviated links (Products, Support); filter chips wrap in a 2-row strip; hero uses 48px padding |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; filter chips in a horizontal scrollable strip; hero uses 64px padding |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with max-width 1200px; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Filter chips are 36px tall (below 44px) but are grouped with adequate 12px gap to prevent mis-taps
- Search bar height 44px meets touch target minimum
- Nav links have 48px tap area (72px nav height / 2 for each link zone)

### Collapsing Strategy
- Top nav collapses to hamburger at < 744px; all links move to a slide-out drawer
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport narrows
- Filter chips collapse from horizontal scrollable strip to vertical stacked list at < 744px
- Footer columns collapse from 4 → 2 at < 744px, then 2 → 1 at < 480px
- Hero section reduces padding and stacks headline/subhead vertically at < 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Extracted only base colors. Hover/focus/active variants for secondary, tertiary, and link colors are inferred from common patterns — actual SanDisk hover values may differ.
- **Shadow tokens**: Product cards and modals likely use box-shadow values that could not be extracted. Current implementation uses border-based separation.
- **Error states**: Form validation styling (red borders, error message colors) not captured. The `{colors.accent-red-soft}` (#f24c4c) is a candidate for error text but unconfirmed.
- **Dark mode**: No dark mode detected on the live site. All tokens assume light background.
- **Typography stack**: The extracted font-family declarations returned only "monospace, sans-serif". The actual font stack likely includes specific system fonts (SF Mono for monospace, Segoe UI or Helvetica for sans-serif) — these are inferred and should be verified against SanDisk's actual CSS.
- **Spacing scale**: The spacing tokens are a standard scale; actual SanDisk spacing values (especially for product card padding, grid gaps, and section margins) may vary.
- **Component heights**: Button and input heights (48px, 44px) are based on common patterns; actual SanDisk heights may differ by 2-4px.
- **Sub-brand palettes**: SanDisk Professional, SanDisk Gaming, and other sub-brands likely have their own color systems not captured here.
- **Animation/transition**: No timing or easing values extracted. Default to 200ms ease-in-out for hover states.
- **Icon system**: SanDisk uses custom icons (product type icons, download icons, compatibility badges) that are not tokenized here.
