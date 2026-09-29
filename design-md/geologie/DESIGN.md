---
version: alpha
name: "Geologie"
source_url: "https://geologie.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep teal #108474 anchors every primary CTA, subscription toggle, and product badge, while a marigold #fbcd0a appears sparingly as a second brand voltage — often on sale tags or limited-edition callouts — creating a confident, clinical-meets-warm palette that feels more like a precision skincare lab than a men's grooming brand. The canvas is near-white #f9fafb with card surfaces at #ffffff, and the ink #131416 is almost black, giving body text a sharp, no-nonsense readability. Buttons and inputs use {rounded.sm} (8px) — a subtle softening that keeps the interface approachable without sacrificing the clinical edge. The top navigation is a fixed white bar with the teal logo mark, and product cards stack on a soft #f9f9f9 background with {rounded.md} corners. The brand trusts its teal as the single signal for interactivity: every "Add to Cart," "Subscribe," and "Take the Quiz" CTA is filled #108474 with white text, and the hover state deepens to #088f87. The marigold accent is never used on primary actions — it's reserved for price drops, bundle savings, and the star-rating system, a deliberate restraint that keeps the teal from feeling cold. The overall mood is that of a dermatologist's office that happens to sell direct: clean, bright, and quietly authoritative, with no visual noise beyond the product photography and the occasional badge.

colors:
  primary: "#108474"
  primary-active: "#088f87"
  primary-disabled: "#dadada"
  ink: "#131416"
  body: "#1e2023"
  muted: "#7b7b7b"
  muted-soft: "#eeeeee"
  hairline: "#dadada"
  hairline-soft: "#efefef"
  canvas: "#f9fafb"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#fbcd0a"
  accent-marigold-active: "#f0c000"
  badge-teal-light: "#edf5f5"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.badge-teal-light}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-marigold-active:
    backgroundColor: "{colors.accent-marigold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
  text-input-focused:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  quiz-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 56px
  subscription-toggle:
    backgroundColor: "{colors.badge-teal-light}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  subscription-toggle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  star-rating:
    color: "{colors.accent-marigold}"
    size: 16px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with teal #108474 and white text. Used for "Add to Cart," "Subscribe," and "Continue" actions. On hover, the background shifts to #088f87 with no border change. Disabled state uses #dadada with muted text, signaling the action is unavailable without error styling.

**`button-secondary`** — An outlined variant with a white fill and teal border, used for "Learn More" or secondary subscription options. The active state fills the background with a light teal tint (#edf5f5) and deepens the border to #088f87. This button sits alongside the primary in subscription toggle groups.

**`button-accent-marigold`** — A warm accent button reserved for sale callouts, limited-time offers, and promotional banners. Uses marigold #fbcd0a fill with dark ink text. Active state shifts to #f0c000. Never used for primary purchase flows — its presence signals urgency or savings.

### Cards
**`product-card`** — A white card with 12px rounded corners, no shadow, and a clean borderless layout. The product image fills the top with matching corner radius, and text content sits below with 16px padding. Badges overlay the image at the top-left corner.

**`product-card-badge`** — A small teal label (11px uppercase, bold) pinned to the product image, used for "Best Seller," "New," or "Top Rated." The sale variant uses marigold background instead, signaling discount.

### Navigation
**`nav-bar`** — A fixed 72px white bar with a thin bottom border (#efefef). Logo sits left-aligned, nav links centered or right-aligned. Active link state uses teal text with a 2px teal bottom border. Mobile collapses to a hamburger menu with a slide-out drawer.

### Forms
**`text-input`** — Standard 48px input with 8px rounded corners, white background, and a light gray border (#dadada). On focus, the border thickens to 2px and turns teal. Placeholder text is muted gray (#7b7b7b). Used for email capture, shipping forms, and quiz responses.

### Quiz CTA
**`quiz-cta`** — A large, pill-shaped button (full rounded) used exclusively for the "Take the Quiz" entry point. Taller than standard buttons at 56px, with extra horizontal padding. This is the brand's primary lead-generation element, appearing in the hero and as a sticky bottom bar on mobile.

### Subscription Toggle
**`subscription-toggle`** — A pill-shaped toggle for one-time purchase vs. subscribe-and-save. Inactive state is a light teal background with teal text; active state fills solid teal with white text. Used in product detail pages and cart.

### Footer
**`footer`** — A dark ink (#131416) footer with muted-soft text (#eeeeee). Links are 14px weight 500, and the layout includes columns for product categories, company info, and social links. The background provides strong contrast against the otherwise light site.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; quiz CTA becomes sticky bottom bar; subscription toggles stack vertically; hero text reduces to 24px |
| Tablet | 744–1128px | Nav links visible; product cards in 2-column grid; quiz CTA remains inline; subscription toggles side-by-side |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero uses 36px display; footer columns expand to 4 |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with larger margins |

### Touch Targets
- All buttons and interactive elements minimum 48px height
- Nav links have 44px touch area (padding extends beyond text)
- Quiz CTA at 56px for easy thumb access on mobile
- Subscription toggles at 36px height with 44px touch area

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 3 to 2 to 1
- Footer columns collapse from 4 to 2 to 1 (accordion-style on mobile)
- Hero section reduces padding and font size on mobile
- Quiz CTA becomes sticky bottom bar on mobile (fixed position)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font family could not be reliably extracted beyond "JudgemeStar" (a review widget font). The typography block above uses Inter as a reasonable assumption for a modern DTC brand, but this should be verified against the live site's CSS.
- Hover and focus states for text inputs (beyond the focus border) are inferred from common patterns, not extracted.
- Error states (form validation, out-of-stock badges) were not visible in the extracted data.
- Dark mode is not supported by the current site (no `prefers-color-scheme` media queries found).
- The marigold accent (#fbcd0a) usage rules (when to use vs. teal) are inferred from visual hierarchy, not documented.
- Dropdown menus, modal dialogs, and tooltip styling were not captured.
- The extracted color list included #007aff (likely a Shopify checkout widget default) — this is not a brand color and should be ignored.
- Star rating size (16px) is an estimate based on typical product card layouts.
- The "Take the Quiz" flow (multi-step form) styling beyond the CTA button is unknown.
