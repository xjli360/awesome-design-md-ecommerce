---
version: alpha
name: "Rhone"
source_url: "https://rhone.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Rhone leads with darkness — not as a recessive background but as the primary surface voltage. The confirmed charcoal #313131 anchors every main CTA, the header bar, and the footer field, which means the brand's visual hierarchy flows from dark confidence outward to white canvas rather than the reverse pattern most athletic labels use. Where competitors reach for saturated primaries to signal energy, Rhone pulls from editorial menswear restraint: a near-black anchor, clean white type (`{colors.on-primary}`), and product photography doing the heavy lifting for color and movement. The typographic voice is lean and upright — system sans-serif at modest weights, sized for scan-readability in a product-dense grid rather than for expressive display. No custom brand typeface was captured from live extraction (the site was behind anti-bot at scrape time), so typography is rendered in the best-match system stack pending font-face confirmation. Buttons carry no soft rounding; `{rounded.xs}` to `{rounded.sm}` reads as precision-engineered rather than friendly, consistent with the brand's performance positioning. Performance-technology badges — callouts for proprietary fabric systems like GoldFusion and DELTA — appear as tight uppercase chips in charcoal against light surface, a signature component that separates Rhone's PDP from generic athleisure stores. The spacing system breathes in sections: generous padding between content rows gives the catalog an unhurried, elevated rhythm that resists the discount-driven density of mass sportswear. Product cards are clean rectangles with model photography cropped to the chest-up or full-body, a hairline border in `{colors.hairline}` optional on hover. The announcement bar at the crown of the page cycles promotional copy in small uppercase at full-width charcoal, inverting the typical light-bar convention. Mobile collapses the four-column grid to a two-column product shelf, preserves the dark nav, and moves the filter/sort controls into a drawer. The overall register is controlled, masculine, editorial — a brand that treats sweat as craft.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#9a9a9a"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#6b6b6b"
  muted-soft: "#9b9b9b"
  hairline: "#e2e2e2"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-dark: "#313131"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-warm: "#c8a96e"
  badge-bg: "#f0f0f0"
  badge-text: "#313131"
  error: "#cc3333"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.04em
  announcement:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  price-sale:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.canvas}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    outline: "2px solid {colors.primary}"
    outlineOffset: 1px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  announcement-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.announcement}"
    height: 40px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    padding: "{spacing.sm}"
    gap: "{spacing.sm}"
    border: none
  product-card-hover:
    border: "1px solid {colors.hairline}"
    imageBehavior: "swap to alt image"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.error}"
    originalPriceDecoration: line-through
    originalPriceColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    layout: full-bleed
    minHeight: 640px
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-primary
    imagePosition: right-half
    textPadding: "{spacing.xxl}"
  category-hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    layout: full-bleed
    height: 400px
    headlineTypography: "{typography.display-lg}"
    textAlign: left
  technology-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    border: none
  technology-badge-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    minWidth: 40px
  size-selector-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
  size-selector-unavailable:
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
    textDecoration: "line-through"
  color-swatch:
    height: 28px
    width: 28px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
  color-swatch-selected:
    border: "2px solid {colors.primary}"
    outline: "2px solid {colors.canvas}"
    outlineOffset: "-3px"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "8px 16px"
    height: 36px
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.accent-warm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    iconColor: "{colors.muted}"

## Components

### Buttons

**`button-primary`** — Solid charcoal (#313131) fill with white uppercase type at 0.08em tracking, 48px tall, nearly-square `{rounded.xs}` corners that signal engineering precision over friendliness. Hover darkens to `{colors.primary-active}` (#1a1a1a); disabled state renders in `{colors.primary-disabled}` (mid-gray). Used for all primary purchase actions: Add to Cart, Checkout, and hero CTAs.

**`button-secondary`** — White canvas background with a 1.5px charcoal border, matching type and height to `button-primary` for optical alignment when the two appear side by side. Hover shifts background to `{colors.surface-soft}`. Carries secondary nav actions and filter resets.

**`button-ghost`** — Transparent fill, white border and type, used exclusively on dark or photographic surfaces such as hero banners and dark-field sections where `button-primary` would disappear.

### Text Input

**`text-input`** — White field, hairline border, 48px height matches button height for inline form parity. Focus ring is charcoal at 2px offset — no color change, just intensification. Placeholder copy renders in `{colors.muted}`.

### Navigation

**`nav-bar`** — White bar, 64px tall, hairline bottom border, charcoal wordmark logo on the left. Nav links in `{typography.nav-link}` (14px/500 weight/0.04em tracking). Cart and account icons on the right; search activates a full-width overlay drawer. Becomes sticky with a soft box-shadow on scroll.

**`announcement-bar`** — Full-width charcoal (#313131) band pinned above the nav, 40px tall, rotating promotional copy in `{typography.announcement}` white uppercase at 0.1em tracking. This dark crown is the most distinctive page-top treatment — no other color appears at this position.

### Product Card

**`product-card`** — Borderless on rest state; a hairline border appears on hover alongside an image swap to the alternate-angle shot. Portrait 3:4 imagery dominates, with title in `{typography.title-sm}` and price in `{typography.price}` below. Sale prices render in `{colors.error}` red with the original struck through in `{colors.muted}`.

### Hero Banner

**`hero-banner`** — Full-bleed, minimum 640px tall. Text block occupies the left half on desktop over a charcoal or photographic field; headline in `{typography.display-xl}` at 700 weight, subhead in `{typography.body-md}`. Primary CTA uses `button-primary` or `button-ghost` depending on background luminosity.

### Technology Badges

**`technology-badge`** — Zero-radius chips in light gray (`{colors.badge-bg}`) carrying proprietary technology names (GoldFusion™, DELTA™, Commuter, SilverTech™) in `{typography.badge}` — 10px/700/0.12em uppercase. Dark variant (`technology-badge-dark`) inverts to charcoal fill for use on light product backgrounds. These chips appear on PDPs below the product title and on collection-page cards as a key Rhone signature.

### Size Selector

**`size-selector`** — 40×40px minimum squares, hairline border, `{rounded.xs}`. Selected state fills with charcoal and flips text to white. Unavailable sizes render struck-through in `{colors.muted-soft}` with a fainter border — not hidden, to preserve grid geometry.

### Filter Pill

**`filter-pill`** — Pill-shaped (`{rounded.full}`) at 36px height for the collection-page filter bar; the only `{rounded.full}` element in the system, providing a soft contrast to the otherwise square-cornered UI. Active state fills charcoal with white type.

### Footer

**`footer`** — Charcoal fill matching `{colors.surface-dark}`, white type, section-level padding. Column headings in `{typography.title-sm}`, links in `{typography.body-sm}`. Link hover shifts to `{colors.accent-warm}` (warm gold), the one moment of chromatic warmth in the system.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart icons; hero text moves below image; filter/sort opens in bottom drawer; announcement bar truncates to single line |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only, sub-menus in flyout; hero reverts to stacked layout with text overlay |
| Desktop | 1128–1440px | Four-column product grid; full nav with mega-menu flyouts; hero text left-half layout; sticky nav activates on scroll |
| Wide | > 1440px | Grid max-width constrained to ~1400px centered; hero imagery scales to fill but content zone stays fixed-width; side whitespace grows symmetrically |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Size selector tiles expand to 48px on touch viewports
- Color swatches minimum 36px with 8px gap between
- Nav hamburger tap target 44×44px regardless of icon visual size
- Filter drawer handles and close buttons minimum 44px

### Collapsing Strategy

- Four-column product grid → two-column at tablet → one-column at mobile
- Mega-menu nav → accordion-style expandable sections inside hamburger drawer on mobile
- Hero split-layout → full-bleed image with text overlay block at tablet, stacked image-above-text at mobile
- Filter sidebar (if present on desktop) → bottom sheet drawer on mobile
- Announcement bar: multi-message cycling maintained on mobile at reduced font size

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Primary brand font unconfirmed**: Live site was behind Cloudflare anti-bot ("Just a moment..."), so no custom `@font-face` declarations were captured. Typography uses best-match system sans-serif stack. Rhone may use a licensed geometric sans-serif (possibly Neue Haas Grotesk, Aktiv Grotesk, or similar) — verify by inspecting `/assets/` network requests on the live site.
- **Color palette extremely sparse**: Only one hex value (#313131) was extracted. All secondary palette entries (surface tones, hairline, accent gold, error red) are inferred from brand knowledge and common athleisure conventions — not confirmed from live CSS variables or design tokens.
- **Accent color unconfirmed**: The warm gold `{colors.accent-warm}` (#c8a96e) is inferred from Rhone's packaging and marketing materials; not extracted from live CSS.
- **No meta theme-color captured**: Browser chrome accent color unknown.
- **Component exact measurements unconfirmed**: Button heights, border widths, card padding, and grid gutters are based on brand-class norms rather than measured from live DOM inspection.
- **Dark mode**: Unknown whether Rhone implements a dark mode variant; no `prefers-color-scheme` data captured.
- **Icon system**: Rhone likely uses a custom icon set for nav, cart, and account — style (stroke vs. fill, weight) not confirmed from extraction.
