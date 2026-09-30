---
version: alpha
name: "Snow Peak"
source_url: "https://www.snowpeak.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A Japanese titanium cup (#b6b8ba) set on a slab of dark basalt (#141414) — that single image is the Snow Peak system. The brand's palette is drawn from mountain equipment and campfire evenings: a deep near-black ink (#141414) that anchors every header, footer, and product-detail background, paired with a warm silver-gray (#b6b8ba) that reads as raw titanium rather than polished chrome. The primary action color is a forest green (#063b26) that appears on add-to-cart buttons and membership badges, while a restrained red (#a11b1b) surfaces only on sale tags and error states. The canvas is a soft off-white (#f6f6f6) rather than pure white, giving the entire site the patina of well-worn canvas tent walls. Inter runs at 400–600 weight across the system — no heavy 700+ display weights, because the product photography (tents pitched at golden hour, titanium cooksets on granite boulders) carries the emotional weight. Buttons use {rounded.sm} corners that suggest machined metal rather than pill-shaped friendliness; product cards use {rounded.md} that mirrors the radius of a folding camp stool. The typography hierarchy is compressed — display sits at 24px, body at 14px — because the brand trusts negative space and full-bleed hero imagery over typographic volume. Every CTA is a solid rectangle of {colors.primary} with white text, never an outline or ghost button, because Snow Peak sells equipment for the outdoors, not digital services.

colors:
  primary: "#063b26"
  primary-active: "#042a1a"
  primary-disabled: "#8aa89a"
  ink: "#141414"
  body: "#4d4d4d"
  muted: "#6c6762"
  muted-soft: "#9e9a96"
  hairline: "#dedede"
  hairline-soft: "#ededed"
  canvas: "#f6f6f6"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-silver: "#b6b8ba"
  accent-red: "#a11b1b"
  accent-charcoal: "#444444"

typography:
  display-xl:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.24px
  display-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.22px
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.14px
  button-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.12px
  link:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  text-input-error:
    borderColor: "{colors.accent-red}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    minHeight: "80vh"
  hero-overlay:
    backgroundColor: "rgba(20, 20, 20, 0.4)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
  search-bar-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-primary}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "12px 0"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 12px 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 44px
  quantity-selector-button:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 44px
    width: 44px

## Components

### Buttons
**`button-primary`** — A solid forest-green rectangle with white text, the single CTA style across the site. Uses {rounded.sm} (4px) for a machined-metal feel rather than pill softness. On hover, darkens to {colors.primary-active} (#042a1a). Disabled state uses a muted green {colors.primary-disabled} with full opacity — no transparency trickery. The 44px height matches the text-input and quantity-selector heights for form alignment.

**`button-secondary`** — White canvas background with dark ink text and a 1px {colors.hairline} border. Used for "Learn More" and "View All" links that sit alongside primary CTAs. Active state fills to {colors.hairline-soft}. Never used as a standalone primary action — always paired with a `button-primary` in the same row.

**`button-tertiary-text`** — Pure text link with no background or border. Used for "Cancel" actions, "Skip to content" accessibility links, and legal footers. Active state shifts text color to {colors.primary} to signal the action destination.

### Cards
**`product-card`** — A white card with {rounded.md} (8px) corners containing a square aspect-ratio image, product title in {typography.title-sm}, and price in {typography.body-md}. The image container uses the same {rounded.md} as the card, creating a seamless radius flow. Badges (sale, new) sit as small rectangles in the top-left corner with {rounded.xs} (2px). No shadow on the card — the brand relies on the {colors.hairline} border for separation, keeping the visual weight on product photography.

### Navigation
**`nav-bar`** — A 72px white bar with the Snow Peak logo left-aligned and navigation links center-aligned. On scroll, gains a 1px {colors.hairline} bottom border. Active nav links show a 2px {colors.ink} underline. The mobile hamburger menu uses a 32px icon-button with {rounded.full}. Secondary navigation (search, account, cart) sits right-aligned as icon-only buttons.

### Forms
**`text-input`** — A 44px white input with {rounded.sm} and a 1px {colors.hairline} border. Focus state swaps to a 2px {colors.primary} border. Error state uses {colors.accent-red} border with a red error message in {typography.caption} below. Placeholder text uses {colors.muted-soft}. The height matches button heights for inline form layouts.

**`quantity-selector`** — A compact 44px component with a minus button, numeric display, and plus button. Each button is 44px square with {colors.hairline-soft} background. The numeric display uses {typography.button-md} centered. Used on product detail pages and cart line items.

### Footer
**`footer-section`** — A full-width {colors.ink} background section with white text. Links use {colors.muted-soft} and shift to white on hover. The footer is organized in a 4-column grid on desktop, collapsing to a single-column accordion on mobile. Social icons use {colors.muted-soft} with white hover. Legal text uses {typography.caption-sm} in {colors.muted-soft}.

### Hero
**`hero-section`** — A full-viewport-height section with {colors.ink} background and white text. The hero image sits as a background with a 40% black overlay for text readability. Headline uses {typography.display-xl} with generous letter-spacing. A single `button-primary` sits below the headline — no secondary actions compete for attention. On mobile, the hero reduces to 60vh with the headline centered.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack 2 per row; hero reduces to 60vh; footer becomes accordion; search bar moves to sticky header |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero at 70vh; footer in 2-column grid |
| Desktop | 1128–1440px | Full nav with all links; 3-column product grid; hero at 80vh; footer in 4-column grid |
| Wide | > 1440px | Max-width container at 1440px centered; product grid expands to 4 columns; hero content max-width at 720px |

### Touch Targets
- All interactive elements (buttons, inputs, icons) maintain minimum 44px height
- Mobile nav hamburger icon is 44x44px with 8px padding
- Quantity selector buttons are 44x44px
- Product card tap targets (title, image, price) are full card width
- Accordion headers are 44px minimum tap height

### Collapsing Strategy
- Primary nav links collapse into hamburger menu below 744px
- Product card grid reduces from 4 columns to 2 columns on mobile
- Footer multi-column layout collapses to single-column accordion on mobile
- Hero secondary text (subheadline, description) hides on mobile, showing only headline and CTA
- Search bar collapses from inline to icon-only on mobile, expanding on tap
- Product detail page tabs collapse to accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow, scale, or border change) could not be reliably extracted from static CSS
- Error styling for form validation beyond border color (icon placement, message positioning) is inferred from common patterns
- Dark mode implementation status is unknown — the extracted palette suggests no dark mode toggle exists
- Sub-brand palettes (Snow Peak Apparel vs. Snow Peak Camping) may use different accent colors not captured in extraction
- Animation timing and easing curves for transitions (nav scroll, card hover, accordion expand) were not extractable
- Font weight for Inter variable font axes (weight range 300-700) is assumed based on common usage — exact weights for each token may vary
- The extracted hex list includes #e2e2e2, #dedede, #f0f0f0, #f9f9f9 which are likely background/divider variants — the exact mapping to surface tokens is inferred
- Shopify checkout widget colors (Afterpay, Klarna) may be present in extracted palette but were filtered where identifiable
- Icon set (social media, cart, search, account) is not specified — assumed to use custom SVG icons matching {colors.ink} and {colors.muted-soft}
- Print stylesheet and email template styling are not included in this design system
