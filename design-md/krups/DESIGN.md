---
version: alpha
name: "Krups"
source_url: "https://www.krupsusa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Burnt orange (#f38230) — the precise shade of crema crowning a double shot — marks every primary action surface on the Krups storefront, from "Add to Cart" buttons to promotional banners and category highlights. It is a deliberate departure from the cool blues and silvers that dominate competitor appliance sites, signaling heat, extraction, and kitchen authority rather than clinical precision. The palette backs this warmth into a near-black (#2a2622) that carries the density of a cast-iron boiler housing, a tone warmer than pure black and far more textured on screen. Body copy drops to #555555 while a family of cool grays (#948e88, #9599a4, #bebdbd) handles muted labels, breadcrumbs, and spec metadata. Surfaces layer three depths: the white canvas, a pale #f5f5f5 soft surface for feature strips, and #eaeeef panels that separate editorial zones from commerce. Typography pairs two distinct sans-serif voices — EurostileNextLTPro, a geometric face with squared apertures and a distinctly European-industrial DNA, handles hero headlines and product names; Gotham, toggling between its Black and Light cuts, manages subheads and navigational elements; Sofia Sans fills in at body scale, lending a slightly narrower, web-native rhythm to paragraph text and spec lists. Corner radii stay restrained: product cards use `{rounded.sm}`, buttons sit at `{rounded.xs}`, and only search inputs and pill badges reach `{rounded.full}`. The overall spatial cadence is generous at section level (`{spacing.section}` = 64px between content blocks) but compact within product grids, where `{spacing.md}` gutters keep appliance imagery large and dominant. A secondary blue (#0088cc) surfaces in link text and informational badges but never competes with the orange for primary CTA attention.

colors:
  primary: "#f38230"
  primary-active: "#d96e1f"
  primary-disabled: "#f9c9a5"
  accent-blue: "#0088cc"
  accent-blue-active: "#0077b3"
  ink: "#2a2622"
  body: "#555555"
  muted: "#948e88"
  muted-soft: "#9599a4"
  border-mid: "#bebdbd"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-panel: "#eaeeef"
  surface-dark: "#222222"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#ee5f5b"
  error-dark: "#b94a48"
  success: "#62c462"
  warning: "#f89406"
  warning-soft: "#fbb450"
  info: "#5bc0de"
  scrim: "#040404"

typography:
  display-xl:
    fontFamily: "'EurostileNextLTPro-Regular', 'Gotham-Black', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'EurostileNextLTPro-Regular', 'Gotham-Black', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'EurostileNextLTPro-Regular', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Gotham-Black', 'EurostileNextLTPro-Regular', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham-Black', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Sofia Sans', 'Gotham-Light', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Sofia Sans', 'Gotham-Light', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Gotham-Black', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham-Black', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gotham-Black', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Sofia Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.4px
    textTransform: uppercase
  promo-tag:
    fontFamily: "'Gotham-Black', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.6px
    textTransform: uppercase
  price-lg:
    fontFamily: "'Gotham-Black', Arial, Helvetica, sans-serif"
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: 2px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-sm}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: 1px solid {colors.border-mid}
    focusBorder: 1px solid {colors.primary}
  text-input-error:
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xl}"
    borderTop: 3px solid {colors.primary}
    boxShadow: 0 8px 24px rgba(0,0,0,0.12)
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 520px
    padding: "{spacing.section} {spacing.xl}"
    ctaTypography: "{typography.button-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.xs}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.primary}
    hoverBoxShadow: 0 4px 16px rgba(0,0,0,0.08)
    imageAspectRatio: 1 / 1
    priceTypography: "{typography.price-lg}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.promo-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.promo-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    hoverBackgroundColor: "{colors.hairline-soft}"
    imageAspectRatio: 4 / 3
  spec-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    borderBottom: 1px solid {colors.hairline}
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-md}"
    headerBackgroundColor: "{colors.surface-soft}"
    cellPadding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.hairline}
    highlightBorder: 2px solid {colors.primary}
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    iconColor: "{colors.muted}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.border-mid}"
    padding: "{spacing.md} 0"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.primary}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: 4px solid {colors.primary}
  newsletter-signup:
    backgroundColor: "{colors.surface-panel}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl} {spacing.lg}"
    inputHeight: 44px
    inputRounded: "{rounded.xs}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
  rating-stars:
    filledColor: "{colors.primary}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: "{spacing.xxs}"
  alert-banner:
    backgroundColor: "{colors.warning-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    iconColor: "{colors.warning}"

---

## Components

### Buttons

**`button-primary`** — The main conversion surface across the Krups storefront. A solid fill of `{colors.primary}` (#f38230) with white uppercase text set in Gotham-Black at 14px with 0.5px letter-spacing. Corners are tight at `{rounded.xs}` (4px), reflecting the brand's industrial-appliance vocabulary — no pills, no soft curves. On hover, the background darkens to `{colors.primary-active}` (#d96e1f) with a subtle inset shadow. Disabled state desaturates to `{colors.primary-disabled}` (#f9c9a5) at 70% opacity.

**`button-secondary`** — A 2px solid `{colors.ink}` border on white fill, inverting to a solid ink background with white text on hover. Same uppercase Gotham-Black treatment as primary. Used for secondary actions like "View Details", "Compare", and filter toggles where orange would create visual competition with the primary CTA.

**`button-link`** — A text-only action trigger in `{colors.accent-blue}` (#0088cc) with no background or border. Typically used inline within spec tables and support content. On hover, text color shifts to `{colors.accent-blue-active}` (#0077b3) with an underline.

### Navigation

**`nav-bar`** — A 64px-tall white bar anchored at the top of every page with a single-pixel `{colors.hairline}` bottom border. The Krups logo sits left; category links run horizontally in `{typography.nav-link}` — uppercase Gotham-Black at 14px. Active category is underlined with a 3px `{colors.primary}` bottom border. A utility strip above (shipping notice, account, cart) may appear in the dark variant `nav-bar-dark` using `{colors.surface-dark}` (#222222) background with white text.

**`mega-menu`** — Triggered on category hover, this dropdown panel has a distinctive 3px `{colors.primary}` top border that brands the interaction. Interior layout uses a multi-column grid with product subcategory links in `{typography.body-sm}` and a featured product image on the right. Closes on mouse-out with no transition delay.

**`breadcrumb`** — Positioned below the nav in `{typography.caption}` scale, showing the category path in `{colors.muted}` with the current page in `{colors.ink}`. Slash or chevron separators in `{colors.border-mid}`.

### Hero

**`hero-banner`** — Full-width promotional banners with a minimum height of 520px and a dark background (#222222 or product photography). Headline text is set in `{typography.display-xl}` — EurostileNextLTPro at 40px, weight 800 — which gives the hero the brand's distinctive squared-letterform impact. A single CTA button sits below in `{colors.primary}` with `{rounded.xs}`. Content is typically left-aligned with the product image composited on the right or covering the full bleed.

### Product

**`product-card`** — White cards with a 1:1 square product image on top, 1px `{colors.hairline-soft}` border, and `{rounded.sm}` corners (8px). Product name in `{typography.title-md}` (Gotham-Black 16px) sits below the image, followed by price in `{typography.price-lg}` (Gotham-Black 22px). On hover, the border shifts to `{colors.primary}` and a subtle box shadow appears, signaling interactivity. Promo badges (`product-badge`) are absolutely positioned in the top-left corner of the image area.

**`product-badge`** — Small rectangular labels in `{colors.primary}` with white uppercase text at 11px (`{typography.promo-tag}`). Used for "NEW", "BEST SELLER", and percentage-off callouts. Informational badges (`product-badge-info`) swap the background to `{colors.info}` (#5bc0de) for non-promotional labels like "FREE SHIPPING".

**`category-tile`** — Larger rectangular cards in `{colors.surface-soft}` with a 4:3 product category image, a bold title in `{typography.title-lg}`, and `{rounded.sm}` corners. Background lightens to `{colors.hairline-soft}` on hover. Used on the homepage and category landing pages to group product families (Coffee Makers, Espresso, Grinders, etc.).

### Specifications & Comparison

**`spec-row`** — Alternating rows with a `{colors.surface-soft}` background and a bottom hairline border. The label column uses `{typography.spec-label}` — Sofia Sans 11px, uppercase, `{colors.muted}` — while the value column uses `{typography.body-sm}`. Padding is compact at `{spacing.sm}` vertical / `{spacing.base}` horizontal to keep spec lists scannable on product detail pages.

**`comparison-table`** — A structured grid for side-by-side product comparison. Column headers use `{typography.title-md}` on a `{colors.surface-soft}` background. Cell padding is `{spacing.md}` / `{spacing.base}`. The currently-selected or recommended product column is highlighted with a 2px `{colors.primary}` border on all four sides.

### Search

**`search-bar`** — A pill-shaped (`{rounded.full}`) input field with a `{colors.surface-soft}` background, magnifying-glass icon in `{colors.muted}`, and placeholder text in `{typography.body-md}`. On focus, the background shifts to white and a 1px `{colors.primary}` border appears. Height matches standard interactive elements at 44px.

### Footer

**`footer`** — A dark block in `{colors.surface-dark}` (#222222) with a thick 4px `{colors.primary}` top border — the same orange accent that brands the mega-menu, creating a visual frame. Links are set in `{colors.hairline-soft}` (#eeeeee) and shift to `{colors.primary}` on hover. Content is organized in a 4-column grid: Product Categories, Support, About Krups, and Social/Newsletter. Section headings use `{typography.title-md}` in white.

### Newsletter & Alerts

**`newsletter-signup`** — A contained panel in `{colors.surface-panel}` (#eaeeef) with `{rounded.sm}` corners, holding a short headline, body text in `{typography.body-md}`, an email input with `{rounded.xs}`, and a submit button in `{colors.primary}`. Typically placed in the footer or as a mid-page interstitial.

**`alert-banner`** — Used for shipping notices, sale countdowns, or stock warnings. Background is `{colors.warning-soft}` (#fbb450) with dark text and a `{colors.warning}` icon. Rounded at `{rounded.xs}`, padded at `{spacing.md}`.

### Rating

**`rating-stars`** — Five-star display using `{colors.primary}` (#f38230) for filled stars and `{colors.hairline}` for empty, at 16px size with `{spacing.xxs}` gaps. The orange-filled stars unify ratings with the broader brand color system rather than introducing a separate gold.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text drops to 28px; nav collapses to hamburger menu with full-screen overlay; mega-menu becomes accordion; comparison table scrolls horizontally; footer stacks to single column; search bar moves into hamburger overlay |
| Tablet | 744–1128px | Two-column product grid; hero text at 32px; nav remains horizontal but may truncate to top-level categories with "More" dropdown; footer in 2×2 grid; category tiles 2-up |
| Desktop | 1128–1440px | Three- to four-column product grid; full mega-menu on hover; hero at full 40px display; comparison table fits 3 products side-by-side; footer in full 4-column layout |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid may expand to 4–5 columns; hero image scales to fill with content pinned left; generous section spacing at 80px+ |

### Touch Targets
- All interactive elements maintain a minimum 44px touch target on mobile, matching iOS HIG
- Product card tap areas extend to the full card surface, not just the text or image
- Nav hamburger icon is 48×48px minimum
- Inline links in spec tables receive 8px vertical padding boost on mobile for tap accuracy

### Collapsing Strategy
- Product grid collapses from 4 → 2 → 1 columns across breakpoints
- Spec tables switch to a stacked label-above-value layout on mobile
- Comparison table becomes horizontally scrollable with a fixed first column (product names)
- Footer columns stack vertically with accordion-style section toggles
- Hero CTA button expands to full-width on mobile
- Mega-menu transitions from hover-triggered overlay (desktop) to tap-triggered accordion (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font files and weight mappings for EurostileNextLTPro could not be confirmed beyond the "Regular" cut; additional weights (Bold, Medium) may exist in the live CSS but were not extracted
- Gotham-Black and Gotham-Light appear in font-family declarations but specific usage contexts (which elements use which weight) could not be mapped precisely from static extraction
- Many of the extracted colors (#ee5f5b, #62c462, #5bc0de, #fbb450, #b94a48, #51a351, #bd362f, #0044cc, #468847, #c09853) are Bootstrap 2.x framework defaults rather than brand-chosen tokens — they are included as alert/status colors but may not reflect intentional brand decisions
- No meta theme-color was set, so mobile browser chrome color is unknown
- The site is not Shopify-based; the underlying platform could not be identified, which limits assumptions about component structure
- Icon font `icokrups` glyph inventory and naming convention were not extractable
- Transition/animation timings (hover durations, menu open speeds) were not captured
- Exact max-width container value could not be confirmed — 1440px is estimated from typical appliance-site patterns
- Whether Sofia Sans serves as the primary body font or a secondary/fallback could not be verified from CSS extraction alone
