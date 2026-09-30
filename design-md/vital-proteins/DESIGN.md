---
version: alpha
name: "Vital Proteins"
source_url: "https://www.vitalproteins.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clean, clinical wellness brand built on a deep navy anchor (#183f86) that reads as medical-grade trust rather than lifestyle pastel. The brand lives in the tension between that authoritative blue and a bright cyan accent (#12abe3) that signals vitality, energy, and the "glow" promise of collagen. The body copy runs in a warm charcoal (#393d40) on an almost-blue-white canvas (#ecf0f3), creating a cool, crisp atmosphere that feels like a clean kitchen or a spa treatment room. Buttons and CTAs lean heavily on the navy with white text (`{colors.on-primary}`), while secondary actions and badges use the cyan as a highlight color. The brand avoids hard corners — cards and buttons use `{rounded.sm}` (8px) to `{rounded.md}` (12px) radii, softening the clinical edge into something approachable. The Shopify platform underpins a direct-to-consumer experience that prioritizes subscription flows, product education, and before/after imagery over heavy editorial typography. There is no custom font declaration beyond a swiper-icons fallback, suggesting a system-font approach or a loaded web font not captured in extraction — the brand trusts its color system and product photography to carry the emotional weight. The overall feel is trustworthy, results-oriented, and slightly aspirational, with the navy anchoring the serious science of collagen peptides and the cyan adding the "beauty from within" lift.

colors:
  primary: "#183f86"
  primary-active: "#122f65"
  primary-disabled: "#8ba3c9"
  ink: "#393d40"
  body: "#393d40"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#d1d5db"
  hairline-soft: "#e5e7eb"
  canvas: "#ecf0f3"
  surface-soft: "#f3f6f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#12abe3"
  accent-cyan-active: "#0e8bb8"
  accent-cyan-soft: "#d4f0fc"
  badge-green: "#10b981"
  badge-warning: "#f59e0b"
  star-rating: "#f59e0b"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
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
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
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
    letterSpacing: 0.3px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
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
  price:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
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
    padding: 14px 28px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-cyan-active:
    backgroundColor: "{colors.accent-cyan-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-pill-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-warning}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(24,63,134,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-cyan-soft}"
    textColor: "{colors.accent-cyan}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    marginTop: "{spacing.base}"
  hero-cta:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  footer-heading:
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-best-seller:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-toggle-active:
    backgroundColor: "{colors.accent-cyan-soft}"
    textColor: "{colors.accent-cyan}"
    border: "1px solid {colors.accent-cyan}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe & Save", and checkout flows. Rendered in the brand navy (#183f86) with white text, 8px rounded corners, and 48px height for comfortable touch targeting. On hover, it deepens to `{colors.primary-active}` (#122f65). The disabled state uses a muted blue-gray `{colors.primary-disabled}` (#8ba3c9) to signal non-interactivity while maintaining brand recognition.
**`button-secondary`** — An outlined variant used for secondary actions like "Learn More" or "View Details". Features a 2px navy border on a white background, matching the primary button's height and padding. On hover, it fills with the navy to become a solid primary button, providing a clear visual hierarchy.
**`button-cyan`** — The energetic accent button using `{colors.accent-cyan}` (#12abe3), deployed for promotional CTAs, limited-time offers, and "Shop Now" badges. It carries the same sizing and rounded corners as the primary button but signals urgency and excitement through the bright cyan hue.
**`button-ghost`** — A text-only button with transparent background, used for less prominent actions like "Cancel" or "Skip". Maintains the navy text color and button-md typography but removes the background fill, relying on hover state to add a subtle background tint.
**`button-pill-primary`** — A pill-shaped variant (9999px radius) of the primary button, used for subscription plan selectors and filter chips. Shorter at 40px with tighter padding, it fits inline within product grids and comparison tables.

### Cards
**`product-card`** — The core product display component, a white card with 12px rounded corners and 16px padding. Contains a product image with 8px rounded corners, a title in `{typography.title-sm}`, and a bold price in `{typography.price}`. On hover, it elevates with a navy-tinted shadow (`rgba(24,63,134,0.12)`) to indicate interactivity. Badges like "NEW" or "Best Seller" appear as small cyan or green labels in the top-left corner.
**`hero-section`** — Full-width promotional banners using the navy background with white text. The headline uses `{typography.display-xl}` (36px bold) with a subtitle in `{typography.body-md}`. A white CTA button with navy text sits below, creating a clean, high-contrast entry point. A cyan variant (`hero-section-cyan`) exists for more energetic promotions.

### Navigation
**`nav-bar`** — A fixed 72px white header containing the brand logo, product category links, and utility icons (search, account, cart). Navigation links use 14px medium-weight type with 0.2px letter spacing. The active link is underlined with a 2px navy border. On scroll, a subtle shadow (`0 2px 8px rgba(0,0,0,0.08)`) appears to separate the nav from page content.
**`nav-link-active`** — The active navigation state, distinguished by navy text color and a 2px bottom border in the same navy. This creates a clear "you are here" indicator without relying on background fills.
**`nav-link-hover`** — On hover, navigation links shift from `{colors.ink}` to `{colors.primary}`, providing a subtle color cue that the link is interactive.

### Forms
**`text-input`** — Standard text input fields with white background, 8px rounded corners, 48px height, and a 1px hairline border. On focus, the border thickens to 2px and turns navy. Error states use a 2px amber border (`{colors.badge-warning}`) to draw attention without the alarm of pure red.
**`select-input`** — Dropdown selectors matching the text-input styling, used for product variant selection (flavor, size) and subscription frequency. The dropdown arrow is styled in `{colors.muted}`.
**`textarea`** — Multi-line text input for custom messages or special instructions, matching the text-input styling but without a fixed height constraint.
**`quantity-selector`** — A compact 40px component for adjusting product quantities, with a hairline border and 8px rounded corners. Contains minus/plus buttons flanking the current quantity value.
**`subscription-toggle`** — A segmented control for choosing between one-time purchase and subscription options. The active segment uses a cyan background (`{colors.accent-cyan-soft}`) with a cyan border, while inactive segments use a soft gray background.

### Badges
**`badge-new`** — A small cyan label (11px uppercase bold) used to flag new products or formulations. Rendered with 4px rounded corners and tight 2px/6px padding.
**`badge-sale`** — An amber badge (`{colors.badge-warning}`) for promotional pricing or limited-time offers. Uses the same sizing and typography as the new badge.
**`badge-best-seller`** — A green badge (`{colors.badge-green}`) highlighting top-performing products. Consistent sizing with other badges but uses green to signal popularity and trust.
**`product-card-badge`** — An inline badge variant that sits directly on product card images, using a soft cyan background with cyan text for a subtle, integrated look.

### Footer
**`footer-section`** — A full-width navy footer with white text, containing brand information, customer service links, and social media icons. Links use 80% opacity by default, increasing to full opacity on hover. Section headings use `{typography.title-sm}` with 16px bottom margin for clear hierarchy.

### Accordion
**`accordion-header`** — Collapsible section headers used for product FAQs and ingredient details. Uses a soft gray background (`{colors.surface-soft}`) with 8px rounded corners and 16px/24px padding. The header includes a chevron icon that rotates on open.
**`accordion-content`** — The expandable content area below accordion headers, using a white background with standard body typography and 16px/24px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text reduces to `{typography.display-md}`; buttons become full-width; footer links stack in single column |
| Tablet | 744–1128px | Two-column product grids; nav shows limited links with "More" dropdown; hero uses `{typography.display-lg}`; side-by-side form layouts possible |
| Desktop | 1128–1440px | Full nav with all links visible; three-column product grids; hero uses `{typography.display-xl}`; multi-column footer layout; maximum content width of 1128px centered |
| Wide | > 1440px | Maximum content width of 1440px with generous side margins; four-column product grids possible; hero may include background imagery at full width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets (Add to Cart, variant selector) are at least 48px tall
- Navigation hamburger icon is 44x44px with adequate surrounding padding
- Quantity selector buttons are 40x40px with clear hit areas
- Accordion headers are 48px tall for easy tapping on mobile

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer containing all links
- Product filters collapse into a "Filter" button that opens a modal overlay on mobile
- Multi-column footer collapses to a single column on mobile, with accordion-style section headers
- Product image galleries collapse from thumbnail strip to swipeable dots on mobile
- Hero sections collapse from side-by-side text/image to stacked layout below 744px
- Subscription toggle collapses from horizontal segments to stacked radio buttons on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font family could not be confirmed — extraction only returned "swiper-icons" as a declared font. The system assumes Inter as the primary font family based on common Shopify wellness brand usage, but the actual brand font may differ
- Hover states for buttons and cards are inferred from common patterns — exact transition durations, shadow depths, and color shifts may vary
- Error styling for forms (validation messages, error icon placement) was not extractable from the static analysis
- Dark mode or high-contrast mode variants are not present in the extracted data
- Sub-brand or seasonal color palettes (e.g., limited edition flavors, holiday campaigns) are not captured
- Animation timing and easing curves for transitions, micro-interactions, and page loads are unknown
- Spacing values for specific components (e.g., exact padding within product cards, gap between grid items) are estimated based on common Shopify patterns
- The `#007aff` hex color extracted from the site may be a system default (iOS link color) rather than a deliberate brand token — it is not included in the color palette above
- Typography scale for mobile (reduced sizes, adjusted line heights) is not confirmed from the extraction
- Focus ring styles for keyboard navigation (color, width, offset) are not available
- Loading states (skeleton screens, spinner designs) for dynamic content are not documented
- Cart and checkout flow specific components (cart drawer, checkout button, shipping calculator) are not fully captured
