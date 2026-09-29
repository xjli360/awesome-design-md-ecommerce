---
version: alpha
name: "iCarez"
source_url: "https://www.icarez.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Nine-layer lamination tolerances and device-model specificity are the organizing logic of every iCarez product page — the catalog opens with a compatibility selector, not a mood board. That specification-first posture shapes the entire visual system: dense grid layouts keyed to device family, compact uppercase labels for protection class and installation type, and a canvas that stays deliberately neutral so tempered glass and case photography can do the persuasion work. The brand occupies the precise, reliable end of the protective accessories market, and the interface vocabulary reflects it. Color functions as a navigation and confidence signal rather than an emotional prompt: a deep navy (#1f4d8c) anchors primary actions and carries the brand's quality assurance language, while a warm amber (#e8850a) is reserved for the calls-to-action that require urgency — add-to-cart triggers, limited stock alerts, promotional strip banners. The canvas is an uninterrupted white (#ffffff) with a hairline-soft off-white surface (#f5f6f8) used for filter rails, secondary panels, and specification comparison tables. No custom webfont was detected during extraction, so the system defaults to the native OS stack — a choice that reads as pragmatic precision rather than typographic ambition and that loads instantly for the device-specification queries driving most site traffic. Button radii are kept tight at {rounded.xs}, rather than pill-shaped, echoing the sharp-cornered accuracy of the products themselves — a screen protector fit to within 0.1mm of the camera cutout does not need a softened brand voice. The device-selector sits above the fold on every product page, treated as a primary navigation interface equal in hierarchy to the top nav. Trust badges communicate installation simplicity and warranty terms in compact icon-and-caption format, reinforcing the brand promise without editorial sprawl. A dark navy footer panel ({colors.surface-dark}) grounds the layout and carries secondary navigation and certification logos.

colors:
  primary: "#1f4d8c"
  primary-active: "#163a6b"
  primary-disabled: "#a0b9d9"
  accent: "#e8850a"
  accent-active: "#c96f08"
  accent-disabled: "#f5c98a"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#6b6b6b"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f6f8"
  surface-card: "#ffffff"
  surface-dark: "#1a2e4a"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  on-dark: "#ffffff"
  success: "#2e7d32"
  success-surface: "#e8f5e9"
  warning: "#e65100"
  error: "#c62828"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
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
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 36px
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  device-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderActive: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    imageAspectRatio: "1 / 1"
    gap: "{spacing.sm}"
    hoverBorder: "1px solid {colors.hairline}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  compatibility-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.spec-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 460px
    padding: "{spacing.xxl} {spacing.xl}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
  hero-cta-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  promo-strip:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.spec-label}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.title-sm}"
    hoverBorder: "1px solid {colors.primary}"
  spec-row:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} 0"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    iconColor: "{colors.muted}"
  trust-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separator: "/"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Deep navy (#1f4d8c) fill with white label at 15px/600 weight and a tight 4px radius. At 44px tall with 12px/24px padding, it reads as confident and precise without feeling corporate-large. The active state drops to #163a6b; the disabled state uses #a0b9d9 maintaining legibility while signaling unavailability.

**`button-secondary`** — White fill with a 1.5px navy border, matching height and radius to `button-primary` for optical consistency on side-by-side CTAs such as "Add to Cart / Learn More" pairings on product pages. Uses the same `{typography.button-md}` to keep button labels visually uniform across variants.

**`button-accent`** — Amber (#e8850a) fill used exclusively for high-urgency actions: the primary add-to-cart trigger, limited-stock overlays, and promotional landing page CTAs. Same 44px height and 4px radius as the primary; the active state (#c96f08) darkens by approximately 15% for haptic feedback clarity. Should not appear more than once per viewport to preserve urgency signaling.

**`button-ghost`** — Transparent background with navy text, no border, used for secondary text links in filter panels, "See all devices" prompts, and footer navigation anchors. `{typography.button-sm}` at 13px keeps it visually subordinate.

### Inputs

**`text-input`** — White canvas, 1px hairline border, 4px radius. On focus the border becomes 2px navy, replacing an outline rather than adding to it. Used for quantity fields, gift message inputs, and account forms. Height is 44px to match button heights for row-level alignment on product pages.

**`device-selector`** — Surface-soft (#f5f6f8) background with the same border and focus behavior as `text-input`, differentiated by background tone to signal "this is a filter, not a form field." Rendered as a `<select>` or custom dropdown; active state uses 2px navy border. This is the most prominent input on product pages — always above the fold.

**`search-bar`** — Full-pill radius ({rounded.full}), surface-soft background, with a search icon in `{colors.muted}` at left. Distinguished from `text-input` by its rounded shape and placement in the nav-bar or a dedicated header band. Focus expands the border to 2px navy.

### Navigation

**`nav-bar`** — White canvas, 64px tall, 1px hairline bottom border. Logo at 36px height, left-aligned. Nav links use `{typography.nav-link}` at 14px/600 — lighter than typical nav to leave visual room for the device-selector filter strip that may appear directly beneath. A dark variant (`nav-bar-dark`) with `{colors.surface-dark}` background is used on the homepage hero overlay and campaign landing pages.

**`breadcrumb`** — Caption-size (12px/500), muted gray for ancestor crumbs, ink (#1a1a1a) for the active terminal crumb, separated by forward slashes with 4px gaps. Sits directly beneath the nav-bar on product and category pages to orient device-specific navigation paths.

### Product Cards

**`product-card`** — White surface card, 1px hairline-soft border, 8px radius, 16px padding. Square image aspect ratio (1:1) for product photography consistency across device models. Title uses `{typography.title-sm}` at 15px/600 and price uses `{typography.price-display}` at 22px/700. The hover state darkens the border to `{colors.hairline}` without adding elevation, keeping the grid feel flat and catalogue-like.

**`product-card-badge`** — Navy fill, white spec-label text (11px/700/uppercase/0.6px tracking), 4px radius, 3px/8px padding. Used for product tier labels: "Premium," "2-Pack," "Lifetime Warranty." Sits over the product image at top-left.

**`compatibility-badge`** — Surface-soft fill with hairline border, same spec-label typography in muted gray. Distinguishes compatibility metadata ("Fits iPhone 15 Pro") from product-tier badges without competing for attention.

### Hero and Marketing

**`hero`** — Dark navy surface (#1a2e4a), minimum 460px tall, with `{typography.display-xl}` heading in on-dark white and `{typography.body-md}` subtext. The CTA uses `hero-cta-primary` (amber fill, 14px/24px padding, 48px tall) rather than the standard `button-accent` to allow a larger hit area on the prominent full-width placement.

**`promo-strip`** — Full-width amber (#e8850a) band in spec-label uppercase typography. Used for sitewide promotions, free-shipping thresholds, and time-sensitive offers. Sits above the nav-bar. Should not coexist with `button-accent` in the same visible viewport to preserve amber's urgency signal.

**`category-card`** — Surface-soft background, 1px hairline border, 8px radius, 24px padding. Hover state sharpens to 1px navy border to indicate interactivity without an elevation change. Title in `{typography.title-sm}` at 15px/600. Used for device-family landing tiles (iPhone, Samsung Galaxy, iPad, etc.).

### Specification and Trust

**`spec-row`** — White canvas, 1px hairline-soft bottom border, 8px vertical padding. Label in `{typography.spec-label}` (11px/700/uppercase) in muted gray at left; value in `{typography.body-sm}` at 13px in ink at right. Used for compatibility tables, material spec lists, and hardness rating rows.

**`trust-badge`** — White card, hairline-soft border, 8px radius, 16px padding. Primary-colored icon (navy) paired with `{typography.caption}` label beneath. Used in a horizontal strip to communicate: hardness rating, bubble-free installation, warranty terms, and optical clarity percentage.

### Footer

**`footer`** — Dark navy (#1a2e4a) background, full-width. Column headings in `{typography.title-sm}` (15px/600) in on-dark white; link text in `{typography.body-sm}` (13px/400) in muted-soft (#9e9e9e). 48px vertical padding. Houses device-family quick links, support navigation, social icons, and certification/compliance mark strip.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; device-selector expands to full width; nav-bar collapses to hamburger + logo + cart icon; hero min-height reduces to 320px; promo-strip wraps to two lines |
| Tablet | 744–1128px | Two-column product grid; device-selector renders as a horizontal row of segmented controls when three or fewer options; nav-bar shows top-level categories without mega-menu |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with category dropdowns; device-selector displayed as inline filter strip beneath nav-bar; hero content max-width 640px left-aligned with product image right |
| Wide | > 1440px | Grid stays at four columns max; layout constrained to 1440px max-width with auto side margins; hero image bleeds to viewport edge while text container stays within content column |

### Touch Targets

- All interactive elements maintain a minimum 44px height and 44px width on mobile
- `device-selector` dropdowns use native `<select>` on iOS/Android to leverage OS-native picker sheets
- `product-card` entire surface is tappable, not just the title or image
- `breadcrumb` items receive 8px vertical padding compensation to meet 44px touch target height without visual bloat
- Cart and hamburger icons in the mobile nav-bar are padded to 44×44px tap areas

### Collapsing Strategy

- Nav mega-menus collapse to a slide-in drawer on mobile, with device-family as top-level accordion items
- The trust-badge strip shifts from a horizontal four-column row to a 2×2 grid on mobile, then a scrollable horizontal rail on tablet
- Spec-row tables collapse to a single-column definition list on mobile with the label above the value
- Hero CTA button stacks below the heading paragraph rather than inline on mobile
- `promo-strip` text truncates to a single line with a disclosure chevron on mobile if longer than viewport width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted**: the live site returned zero color tokens during extraction — likely loaded via JavaScript after initial parse or behind bot-mitigation. All palette values in this file are rationally inferred defaults for a precision tech-accessories brand, not observed brand colors. Verify primary, accent, and surface values against the live site before production use.
- **No font stack detected**: zero webfont references were captured. System font stack is assumed. If iCarez loads a custom typeface (common via Shopify theme or Google Fonts), update all `fontFamily` values and re-evaluate type scale sizing.
- **No theme-color meta tag**: the browser chrome accent color is unknown; the navy primary is used as a reasonable default for `<meta name="theme-color">`.
- **Logo asset and dimensions unconfirmed**: `logoHeight: 36px` in `nav-bar` is an informed default; actual logo aspect ratio and clearspace requirements should be measured from the live site.
- **Shopify platform not confirmed**: extraction shows `platform-shopify: False` — the component model assumes a standard e-commerce CMS. If Shopify is actually in use, swap `device-selector` implementation to leverage Shopify's native product option and variant API rather than a custom filter widget.
- **Animation and micro-interaction tokens absent**: no transition timing or easing values were captured. Defaults (200ms ease-out for hover states, 150ms for button active states) should be validated against the live site's motion behavior.
- **Product photography art direction unconfirmed**: image background (pure white vs. light gray) and shadow style are assumed neutral; verify against actual product image assets to ensure `surface-card` and `surface-soft` backgrounds complement rather than clash.
