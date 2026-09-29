---
version: alpha
name: "Lululemon"
source_url: "https://lululemon.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Black CTAs against white canvas, no accent color anywhere except markdown red — Lululemon's digital system runs monochromatic by design, and the restraint becomes legible once you notice the only non-neutral chromatic signal in the entire interface is the sale price color (#c8102e) surfacing on "We Made Too Much" pages. Product photography handles all chromatic expression: a Sonic Pink Align tank or a Heritage 365 hoodie in Dark Olive provides the color story the UI refuses to supply itself. Type is set in a clean geometric sans-serif at restrained weights — display heads sit at fontWeight 600 rather than 700–800, maintaining an editorial calm that positions the brand closer to premium outerwear than performance sportswear. Buttons run nearly cornered ({rounded.none}), uppercase-tracked at 0.08em letter spacing, and locked to 48px height — a format that reads as architectural rather than friendly. Navigation carries significant category depth (women's, men's, accessories, footwear, membership, Studio) behind a sticky 60px top bar that refuses to compete with the hero imagery below. Product cards present at 3:4 aspect ratio with no border radius, no card shadow, and 20px circular color swatches ({rounded.full}) inlaid at the bottom edge — a pattern that gives shoppers chromatic preview without opening a PDP. The checkout and membership flows inherit the same vocabulary: black button, white modal, hairline-bordered input at 1px in {colors.hairline} gray. No gradients, no elevation shadows beyond a faint rgba(0,0,0,0.06) scrim on drawer overlays. The brand communicates premium through proportion, negative space, and the confidence to let a $138 legging sell on product description alone — fabric technology names like Luon, Nulu, and Everlux appear as structural UI labels rendered in dedicated {typography.fabric-label} chips, not marketing copy tucked into fine print. The overall effect is a design system that reads like a premium basics house that also makes sportswear, which is precisely the market position the company has pursued in its Power of Three growth strategy.

colors:
  primary: "#000000"
  primary-active: "#1a1a1a"
  primary-disabled: "#aaaaaa"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#767676"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale: "#c8102e"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.5px"
  display-lg:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.3px"
  display-md:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.2px"
  display-sm:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "0"
  title-md:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0"
  title-sm:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: "0"
  body-md:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0"
  body-sm:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0"
  caption:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0"
  label:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0.06em"
    textTransform: uppercase
  badge:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.06em"
    textTransform: uppercase
  fabric-label:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "0.04em"
  price:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0"
  price-sale:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0"
  button-md:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "0.08em"
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.08em"
    textTransform: uppercase
  nav-link:
    fontFamily: "'Lululemon Typeface', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "0"

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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 24px"
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    pointerEvents: none
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "13px 23px"
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
    position: sticky
    zIndex: 100
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    subtitleColor: "{colors.muted}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    padding: "0"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    fabricTypography: "{typography.fabric-label}"
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderUnselected: "2px solid {colors.hairline}"
    gap: "{spacing.xs}"
  size-selector-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    unavailableTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    unavailableDiagonalStrike: true
  quick-add-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    trigger: hover
  hero-banner:
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: "70vh"
    overlayScrim: "linear-gradient(to right, rgba(0,0,0,0.42) 0%, rgba(0,0,0,0) 60%)"
    buttonVariant: "button-primary"
    textAlign: left
    padding: "{spacing.xxl}"
  promo-announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
    linkColor: "{colors.on-primary}"
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  fabric-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.fabric-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  filter-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    width: 320px
    rounded: "{rounded.none}"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    overlayPosition: bottom
  membership-card:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.label}"
    borderTop: none

## Components

### Buttons
**`button-primary`** — Pure black (#000000) 48px block, no border radius, uppercase label in `{typography.button-md}` tracked at 0.08em. Active/pressed state shifts fill to `{colors.primary-active}` (#1a1a1a); disabled collapses to `{colors.primary-disabled}` (#aaaaaa) with pointer-events suppressed. This is used for every hard commerce action: "Add to Bag," "Checkout," "Join Now."

**`button-secondary`** — Outlined variant with 1px `{colors.ink}` border, canvas fill, and identical uppercase typography and 48px height. Used for secondary commerce actions like "Save to Wishlist," "Find in Store," or "See All." Hover/active state fills to `{colors.surface-soft}` (#f7f7f7). The identical sizing to `button-primary` keeps paired button layouts visually balanced.

**`button-text`** — Bare underlined text at `{typography.body-sm}` with no container. Used inline in body copy, footer navigation, and supplementary actions that shouldn't compete with primary CTAs.

### Nav Bar
**`nav-bar`** — Sticky 60px bar in `{colors.canvas}` white, separated from page content by a 1px `{colors.hairline-soft}` bottom stroke. On desktop: wordmark left-aligned, category links in `{typography.nav-link}` centered, bag icon + account icon right-aligned. Category link hover triggers `nav-dropdown` — a full-width flyout with a subtle 0 4px 12px shadow, mega-menu layout grouping subcategories by gender and activity. The `promo-announcement-bar` (40px, black, `{typography.caption}`) stacks above the nav when a promotion is live, pushing the nav down rather than overlapping it.

### Product Card
**`product-card`** — No border radius, no shadow, full-bleed 3:4 portrait image. Below the image: product name in `{typography.title-sm}`, fabric technology in a `fabric-tag` chip using `{typography.fabric-label}`, then price in `{typography.price}`. Marked-down items render the original price struck-through and the new price in `{typography.price-sale}` colored `{colors.sale}` red. Color swatches (`color-swatch`) stack horizontally below — 20px circles at `{rounded.full}`, bordered in `{colors.ink}` when selected, `{colors.hairline}` when unselected. On desktop hover, `quick-add-drawer` slides up from the card bottom exposing size selectors without navigating away.

### Size Selector
**`size-selector-button`** — Square-cornered chips in `{colors.canvas}` with 1px `{colors.hairline}` border; selected state upgrades the border to `{colors.ink}`. Unavailable sizes render the label in `{colors.muted}` with a diagonal strike-through line crossing the entire chip face — a clear, accessible unavailability signal that avoids hidden options. Padding is `{spacing.sm}` × `{spacing.md}`.

### Hero Banner
**`hero-banner`** — Full-width lifestyle photography, minimum height 70vh, with a left-anchored linear scrim fading rightward (rgba(0,0,0,0.42) → transparent at 60%). Headline in `{typography.display-xl}`, subtext in `{typography.body-md}`, followed by a `button-primary` CTA, all left-aligned. On mobile, the gradient recenters and the headline downsizes to `{typography.display-md}`. The scrim approach maintains text legibility without obscuring the product being worn.

### Promo Bar & Sale Badges
**`promo-announcement-bar`** — 40px black bar above the nav carrying promotional copy in `{typography.caption}` white, horizontally centered. Typically dismissible on mobile via a close icon. `sale-badge` is a compact `{colors.sale}` red chip with `{typography.badge}` uppercase text, rendered on product card image corners and PLP tiles when an item is marked down. Sale price in the product detail uses `{typography.price-sale}` directly in the price line rather than a separate badge.

### Fabric Tags
**`fabric-tag`** — `{colors.surface-soft}` chip using `{typography.fabric-label}` in `{colors.body}`, carrying fabric technology identifiers: Luon, Nulu, Everlux, Warpstreme, Swift. Tapping or clicking the chip navigates to the fabric technology education page — a structural UI pattern unique to Lululemon's technical product vocabulary, treating material science as a first-class navigation destination rather than a tooltip.

### Filter Drawer
**`filter-drawer`** — 320px panel for PLP filtering, right-anchored on desktop (sticky sidebar above 1128px), full-screen modal overlay on mobile. Section headings in `{typography.title-sm}`, filter options in `{typography.body-sm}` with checkbox controls in `{colors.ink}`. Hairline right border on desktop. No border radius. Includes a "Clear All" text button and an "Apply" `button-primary` pinned to the drawer foot on mobile.

### Membership Card
**`membership-card`** — Solid `{colors.ink}` background with `{colors.on-dark}` text, `{spacing.xl}` padding, no rounding. Title in `{typography.title-md}`, body in `{typography.body-sm}`. Used on the lululemon membership and Studio pages to present tier benefits. The inverted color block creates a clear visual boundary between content sections without introducing a new color.

### Footer
**`footer`** — `{colors.ink}` full-bleed background. Section headings in `{typography.label}` (uppercase, 0.06em tracked, 11px), links in `{typography.body-sm}` at `{colors.on-dark}`. Four-column grid on desktop collapsing to stacked accordions with `{colors.hairline}` dividers on mobile. No top border — the dark block creates its own visual break from page content above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to wordmark + hamburger + bag icon; hero crops to portrait with centered overlay text and `{typography.display-md}` headline; filter becomes full-screen modal; size selector becomes bottom sheet; quick-add triggers on tap; announcement bar persists |
| Tablet | 744–1128px | Two-column product grid; nav may show wordmark + hamburger at 744px, transitioning to partial links ~900px; hero crops to 16:9; filter drawer appears as slide-in overlay |
| Desktop | 1128–1440px | Three- or four-column product grid; nav fully expanded; filter sidebar inline on PLP; quick-add on card hover |
| Wide | > 1440px | Max-width container (~1440px) centered with `{colors.canvas}` gutters; hero image extends edge-to-edge behind centered container; product grid holds four columns |

### Touch Targets
- All primary and secondary buttons 48px tall, meeting WCAG 2.5.5 minimum
- Color swatches are 20px visible but surrounded by 12px invisible tap-extension padding for ~44px effective target
- Size selector chips minimum 44px tall on mobile via padding expansion
- Nav hamburger and bag icon targets minimum 44 × 44px
- Wishlist heart and close-drawer icons minimum 44 × 44px touch area

### Collapsing Strategy
- Footer four-column grid collapses to stacked accordions with chevron toggles below 744px
- PLP filter sidebar collapses from inline sticky to full-screen modal below 1128px
- Hero headline scales from `{typography.display-xl}` (48px) on desktop to `{typography.display-md}` (28px) on mobile
- Category nav mega-menu collapses to hamburger flyout below ~900px; flyout is full-height with back-navigation for nested categories
- Product card name truncates at two lines with ellipsis; full name always visible on PDP
- Announcement bar is dismissible via close icon on mobile; persists on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All color values are inferred from publicly observable brand usage, not extracted from live CSS** — lululemon.com returned "Access Denied" to the extraction crawler. Primary (#000000), sale (#c8102e), and neutral palette are consistent with observed brand behavior but must be verified against live site tokens or internal design system documentation.
- **Font family unconfirmed** — extraction yielded zero font-family data. The file uses a `'Lululemon Typeface'` placeholder; the actual licensed or proprietary typeface name, CDN URL, and variable font axis ranges require access to live CSS or the brand asset portal.
- **Font weights unverified** — weights (600 for display, 500 for nav) are inferred from visual inspection; precise values may differ, especially if a variable font with non-integer axis positions is in use.
- **Button border-radius** — Lululemon buttons appear nearly square; the actual value may be exactly 0px or a small 2–4px. Assigned `{rounded.none}` pending measurement.
- **Announcement bar color variance** — the promo bar is documented here as `{colors.primary}` black but frequently overridden per campaign (red, white, seasonal colors). The black default is the most commonly observed non-campaign state.
- **Studio and membership design tokens** — lululemon Studio and tiered membership flows may use distinct component tokens not fully covered here.
- **Dark mode / motion preferences** — no data on whether the system respects `prefers-color-scheme` or `prefers-reduced-motion`.
- **Icon library** — Lululemon uses a custom icon set (bag, account, hamburger, wishlist heart, size guide); SVG dimensions, stroke widths, and naming conventions are not documented here.
- **Exact product grid gutter and column widths** — column count and gap values are inferred from visual observation; pixel-precise values require computed layout inspection.
