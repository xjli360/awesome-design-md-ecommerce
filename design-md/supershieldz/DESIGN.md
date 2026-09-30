---
version: alpha
name: "Supershieldz"
source_url: "https://www.supershieldz.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep violet #221155 — the color of a late-summer Concord grape — is the single brand voltage that runs through every button, badge, and product highlight on Supershieldz. It appears against a stark white canvas (#ffffff) with almost no intermediary grays, creating a high-contrast, no-nonsense visual system that mirrors the brand's value proposition: screen protectors that are cheap, effective, and ship fast. The typography is a single-weight system built on system sans-serif stacks, with no custom font investment — the brand trusts its product photography and price tags to do the selling. Buttons are pill-shaped ({rounded.full}) and generously padded, making the CTA to "Add to Cart" feel like the easiest tap on the page. Product cards use a soft {rounded.md} corner and a clean white surface-card background, letting the protector's own packaging and the phone model it fits dominate the visual field. There is no hero imagery, no lifestyle photography — just rows of SKUs, each with a "Compatible With" label, a price in bold, and a star rating. The navigation is a thin, utilitarian strip: logo left, search bar center, cart icon right. The brand's design language is one of radical simplicity, where the deep violet acts as a signature stamp rather than a decorative accent.

colors:
  primary: "#221155"
  primary-active: "#1a0f44"
  primary-disabled: "#8a7bb5"
  ink: "#221155"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  star-rating: "#f59e0b"
  badge-sale: "#dc2626"
  badge-new: "#221155"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
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
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
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
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline-soft}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 12px
  product-card-image:
    rounded: "{rounded.sm}"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Buy Now", and checkout flows. Rendered as a pill with the deep violet #221155 fill and white text, with a generous 12px 32px padding that makes the button feel substantial. On hover, it shifts to `primary-active` (#1a0f44); when disabled, it fades to `primary-disabled` (#8a7bb5) with no border or shadow change.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Compare". Uses a white fill with a 2px solid `primary` border and `primary` text. On hover, the background shifts to `surface-soft` and the border to `primary-active`. Both primary and secondary buttons share the same 48px height and `{rounded.full}` shape, ensuring visual consistency across the interface.

### Cards
**`product-card`** — The core content unit of the Supershieldz storefront. Each card is a white rectangle with `{rounded.md}` corners and 12px padding, containing a product image (with `{rounded.sm}` corners on a `surface-soft` background), a title in `title-md` weight, a price in the dedicated `price` token (20px bold), and a star rating row. Cards are arranged in a responsive grid with 16px gaps. There is no shadow or elevation — the card relies on the contrast between the white surface and the `hairline-soft` grid background.

### Navigation
**`nav-bar`** — A thin, utilitarian 64px strip with a white background and a subtle `hairline-soft` bottom border. The logo sits left-aligned, a pill-shaped search bar occupies the center, and a cart icon with a badge counter sits right. Navigation links are minimal — typically "Shop All", "Best Sellers", and "About" — rendered in `nav-link` weight (500) at 14px. The search bar uses `surface-soft` as its background, distinguishing it from the nav's white canvas.

### Forms
**`text-input`** — Standard input fields used in checkout and account forms. They have a white background, `hairline` border, `{rounded.sm}` corners, and 44px height. On focus, the border thickens to 2px and turns `primary` (#221155), providing a clear, accessible focus state. Placeholder text uses `muted` (#666666).

### Footer
**`footer`** — A full-width section with a `surface-soft` background, containing columns of links in `muted` gray. Links are styled with `link` typography and turn `primary` on hover. The footer includes standard e-commerce sections: Customer Service, Quick Links, and About Us. No social icons or newsletter signup were observed in the extracted data.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; search bar hidden behind icon; buttons become full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav remains full with search bar visible; buttons retain inline sizing |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; standard button sizing |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; no additional changes |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (buttons at 48px, inputs at 44px)
- Product cards are tappable as a unit, with no smaller touch targets inside the card
- Nav links and cart icon have 44px minimum tap area

### Collapsing Strategy
- Navigation links collapse to a hamburger menu below 744px
- Search bar collapses to a search icon that expands to a full-width input on tap
- Product grid collapses from 4 columns to 1 column on mobile
- Footer columns stack vertically below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#221155) was extracted from the live site — the full palette above is inferred from common e-commerce patterns and may not match the actual site. The brand's true secondary, accent, and surface colors could not be confirmed.
- No font-family declarations were found on the live site — the typography stack uses system fonts as a safe default. The brand may use a custom web font that was not detected.
- Hover, focus, and active states for all components are estimated based on standard accessibility patterns, not extracted from the live site.
- Error states for form inputs (validation, error messages) were not observed and are not defined.
- Dark mode styling is not present on the live site and is not defined.
- The star-rating color (#f59e0b) is a common yellow for ratings and may not be the brand's actual choice.
- Badge colors (sale red, new violet) are inferred from common e-commerce patterns and may not match the live site.
