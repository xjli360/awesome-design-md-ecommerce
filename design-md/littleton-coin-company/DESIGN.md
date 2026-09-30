---
version: alpha
name: "Littleton Coin Company"
source_url: "https://www.littletoncoin.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The #008063 teal threading through every primary CTA and navigation stripe carries the visual memory of green velvet display trays — the kind dealers line their showcases with. Littleton's palette is built around that single collector-case hue, deepening to #007055 on hover and softening to the mint wash of #dae5e2 for background accents and callout panels. The rest of the palette is deliberate restraint: #43484d and #5e6977 for layered slate grays that handle body copy and muted labels, #b5beca for hairlines and disabled states, and an off-white #f4f4f4 canvas behind product grids rather than stark paper white. Typography runs a no-nonsense Arial/Open Sans stack — the choice signals catalog heritage rather than brand ambition, prioritizing legibility at small sizes for coin specifications and grading notes over typographic personality. Buttons sit on a modest 4px radius, not pill-shaped; the site carries direct-mail DNA and rounded-full forms would feel foreign to a customer base accustomed to decades of printed catalogs. Product cards carry grade badges — labels like MS-65 or PF-70 UC that demand consistent type sizing at `{typography.grade-badge}` — and present coin obverse and reverse photography against neutral #f4f4f4 grounds. The error red #d32f2f appears exclusively for sale badges and out-of-stock warnings, keeping urgency contained and legible. A light blue accent #5bbad5 surfaces in informational callouts, distinct from the primary teal so the two hues don't compete. The entire composition reads as a trustworthy catalog merchant: high information density, low decorative noise, with the #008063 teal doing most of the brand-recognition work across the nav stripe, CTAs, price text, and promotional strips that bracket every page top to bottom.

colors:
  primary: "#008063"
  primary-active: "#007055"
  primary-disabled: "#b5beca"
  error: "#d32f2f"
  accent-info: "#5bbad5"
  ink: "#222222"
  body: "#43484d"
  muted: "#5e6977"
  muted-soft: "#a9a9a9"
  hairline: "#b5beca"
  canvas: "#ffffff"
  canvas-alt: "#f4f4f4"
  surface-soft: "#dae5e2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-strong:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  grade-badge:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  label-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
    typography: "{typography.body-md}"
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 60px
    topStripeBackgroundColor: "{colors.primary}"
    topStripeTextColor: "{colors.on-primary}"
    topStripeHeight: 36px
  search-bar:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 38px
    typography: "{typography.body-md}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-sm}"
    buttonRounded: "{rounded.xs}"
    focusBorder: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imageBackgroundColor: "{colors.canvas-alt}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-sm}"
    ctaRounded: "{rounded.xs}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.12)"
  coin-grade-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.grade-badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  sale-badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.grade-badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  info-callout:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    borderLeftAccent: "3px solid {colors.accent-info}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    minHeight: 360px
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.button-sm}"
    height: 36px
  category-tab:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.canvas-alt}"
    inactiveTextColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: 6px 14px
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — The main call-to-action uses the collector-case teal #008063 fill with white text at `{typography.button-md}` (15px, weight 700). Corners sit at `{rounded.xs}` (4px), preserving the catalog-era directness without sharp 90-degree edges. Hover and active state deepens to #007055 (`{colors.primary-active}`); disabled state drains to `{colors.primary-disabled}` (#b5beca) with white text retained. Height is a consistent 40px across the site, matching the search bar for visual alignment in header contexts.

**`button-secondary`** — A white-fill button bordered in `{colors.primary}` with teal text, used for secondary actions like "View Details" or "Add to Wish List." Border is 1px solid; padding insets by 1px from the primary to maintain identical optical height. Active state fills lightly with the `{colors.surface-soft}` mint wash and deepens the border to `{colors.primary-active}`.

**`button-text-link`** — Inline teal underlined links at `{typography.body-sm}` used throughout product descriptions and policy sections. No background or border; purely text-level affordance for low-hierarchy actions.

### Navigation

**`nav-bar`** — Two-tier structure: a narrow teal top stripe (36px height, `{colors.primary}` background) carries account links, phone number, and cart icon in white `{colors.on-primary}` text; the main nav sits below on white canvas with a `{colors.hairline}` bottom border at 60px total height. Navigation labels use `{typography.nav-link}` at 14px/600 weight. The top stripe ensures the brand green is visible at every scroll position, functioning as a persistent ambient color signal before the user reaches any CTA.

**`search-bar`** — An inline search input with a teal submit button attached flush to its right edge with no gap. Input uses `{typography.body-md}` with a `{colors.hairline}` border and `{colors.muted-soft}` placeholder text; the button carries the same 38px height and `{typography.button-sm}` label. Focus ring shifts the input border to `{colors.primary}`. Placed prominently in the main nav row.

### Product Card

**`product-card`** — Cards use a 1px `{colors.hairline}` border with `{rounded.xs}` corners and a `{colors.canvas-alt}` (#f4f4f4) image well that neutrally grounds coin photography without warm or cool interference. Title renders at `{typography.title-sm}` in `{colors.ink}`; price at `{typography.price-display}` in `{colors.primary}` teal, making the price the most visually dominant text element after the coin image itself. An "Add to Cart" CTA button sits flush at card bottom at `{typography.button-sm}`. A subtle `hoverShadow` lifts the card on pointer-over to signal interactivity.

**`coin-grade-badge`** — Teal rectangular badge (4px radius) overlaid at the top corner of coin images carries grade text like "MS-65" or "PF-70 UC" at `{typography.grade-badge}` — 11px all-caps, weight 700, 0.4px tracking. Grading certification is the collector's primary purchase signal and the badge must remain instantly legible at card thumbnail sizes across all grid breakpoints.

**`sale-badge`** — Error red (#d32f2f, `{colors.error}`) badge in the same shape as the grade badge, reserved for "SALE" labels or percentage-off callouts. Shares `{typography.grade-badge}` metrics so grade and sale badges can coexist at card corner without competing for different visual vocabularies.

### Hero

**`hero`** — Full-width banner with a `{colors.surface-soft}` mint-wash ground (#dae5e2) that echoes the collector-tray palette without competing with coin photography. Headline at `{typography.display-xl}` in `{colors.ink}`, subhead at `{typography.body-md}` in `{colors.body}`. A single primary CTA button sits below the subhead. Minimum height 360px; standard compositions place coin photography right-aligned against the mint ground, with the text column occupying the left 40–50% of the layout.

### Informational Components

**`promo-banner`** — Full-width teal strip (`{colors.primary}`) pinned near the top of the page below the nav, carrying promotional headlines like "Free Shipping on Orders Over $75" in white `{typography.button-md}`. This is the highest-frequency brand color touchpoint across a typical browsing session and reinforces the teal identity even on pages with sparse primary CTAs.

**`info-callout`** — Mint-washed box (`{colors.surface-soft}`) with a 1px `{colors.hairline}` border and a 3px left-edge accent in `{colors.accent-info}` (#5bbad5), visually distinct from the primary teal so informational panels don't read as promotional. Used for grading guides, shipping notices, and authenticity guarantees at `{typography.body-sm}`.

**`breadcrumb`** — Compact path navigation at `{typography.caption}` (12px) in `{colors.muted}`, with the active final segment in `{colors.ink}`. Separators are "/" characters. No background — renders directly on canvas or surface-soft depending on page context. Category hierarchies in the coin market can be four levels deep (e.g., Coins › U.S. Coins › Morgan Dollars › 1878-S) so breadcrumb clarity is load-bearing.

**`pagination`** — Active page uses `{colors.primary}` fill with white numerals; inactive pages are white with `{colors.hairline}` border and `{colors.body}` text. All items use `{rounded.xs}` and `{typography.button-sm}`, 36px height. Consistent visual language with button-secondary so the control strip reads as navigation rather than action.

**`category-tab`** — Horizontal tab strip above collection grids to toggle between coin series, denominations, or date ranges. Active tab fills with `{colors.primary}` teal; inactive tabs sit on `{colors.canvas-alt}` with `{colors.body}` text and a `{colors.hairline}` border. Uses `{typography.body-sm}` at 13px — tight enough to fit 6–8 tabs across a desktop grid row without wrapping.

### Footer

**`footer`** — Dark slate base using `{colors.body}` (#43484d) with a 3px `{colors.primary}` top border acting as a closing brand stripe that mirrors the nav's top stripe, bracketing the page with teal. Column headings use `{typography.title-sm}` in `{colors.on-dark}` white; body links render in `{colors.surface-soft}` mint (#dae5e2) for legibility against the dark ground without full white contrast.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; top stripe reduces to cart badge and account icon only; hero stacks text above coin image; search bar moves to full-width row below collapsed nav |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category labels with overflow dropdown; hero runs side-by-side layout at reduced min-height; promo banner text truncates to single line |
| Desktop | 1128–1440px | Three- to four-column product grid; full two-tier nav with all category labels visible; hero at full 360px min-height with right-side coin imagery; category tab strip fully expanded |
| Wide | > 1440px | Content column max-width ~1280px centered; grid holds at four columns; hero image scales larger; footer expands to five columns |

### Touch Targets

- All primary and secondary buttons maintain 40px height minimum on mobile; invisible tap-area padding extended to 44px
- Navigation hamburger icon: 44×44px touch target
- Product card "Add to Cart" button expands to full card width on mobile for single-thumb reach
- Pagination controls: minimum 36px height per item with 4px gaps, horizontally scrollable on narrow viewports
- Coin grade badges are display-only; no tap affordance required

### Collapsing Strategy

- Primary nav mega-menu collapses to accordion-style drawer at mobile breakpoint, opening over content with `{colors.canvas}` background
- Top stripe hides promotional text at < 480px, retaining only cart count badge and account icon
- Product card grade badge remains visible at all sizes; title truncates to two lines max; price never truncates
- Footer four-column layout reflows to two columns at tablet, single column at mobile with section headings as accordion toggles
- Hero subhead text hides at < 480px to reduce vertical scroll cost before the first product grid appears
- Category tab strip becomes horizontally scrollable at mobile rather than wrapping to multiple rows

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom typeface detected; Arial/Open Sans system stack only — site may load a licensed web font via JavaScript not captured in static extraction
- Exact button border-radius not confirmed from live DOM; 4px inferred from visual conventions consistent with catalog-heritage e-commerce
- Hover shadow values for product cards interpolated from common patterns; exact `box-shadow` not extracted
- Nav mega-menu depth and column count (likely 2–3 column dropdown with series imagery) not captured in extraction
- Mobile breakpoint exact pixel values not confirmed from CSS; 744px and 1128px applied as standard defaults
- Role of #5bbad5 accent blue in body UI beyond favicon/touch-icon context not confirmed; callout border vs. icon fill usage is inferred
- Dark mode palette not detected; site appears light-only
- Exact internal card spacing (image padding, text gutters) not extracted from DOM inspection
- Checkout and account page design systems may diverge from browse/PDP patterns; not assessed
