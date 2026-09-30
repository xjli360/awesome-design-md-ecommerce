---
version: alpha
name: "Buffy"
source_url: "https://buffy.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Buffy is a bedding brand that treats sleep as a foundational act of care, and its design system mirrors that ethos with a palette drawn from nature, comfort, and quiet confidence. The brand’s primary color, a deep forest green `#1f3f39`, anchors the experience — it appears on primary buttons, key headlines, and the site’s meta-theme bar (`#445958`), creating a consistent, grounding presence. This is balanced by a warm off-white canvas (`#fbf9f6`) that feels softer than pure white, and a secondary accent of terracotta (`#dc582a`) that adds a touch of warmth without disrupting the calm. The typography pairs a refined serif for display — Recoleta Bold — with Inter for body and UI, giving the brand a editorial-meets-modern feel. Rounded corners are generous but not cartoonish: primary buttons use `{rounded.sm}` (8px), while cards and containers use `{rounded.md}` (12px) to feel approachable. The overall mood is one of deliberate softness — muted grays like `#666666` and `#aeaeae` handle secondary text and borders, while the occasional pop of `#b1edd8` (a minty green) or `#b6db6e` (a pale lime) appears in illustrations and badges, reinforcing the natural, eco-conscious identity. Every design decision — from the pill-shaped search bar to the generous padding on product cards — whispers “rest,” not “sell.”

colors:
  primary: "#1f3f39"
  primary-active: "#1a3530"
  primary-disabled: "#8ba8a2"
  ink: "#19191a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#aeaeae"
  hairline: "#dedede"
  hairline-soft: "#eaeaea"
  canvas: "#fbf9f6"
  surface-soft: "#f6f5fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#dc582a"
  accent-mint: "#b1edd8"
  accent-lime: "#b6db6e"
  accent-blue: "#135bbf"
  error: "#cc0a0a"
  success: "#25b900"
  star-rating: "#19191a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Recolta Bold', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Recolta Bold', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Recolta Bold', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Recolta Bold', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
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
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 0"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-eco:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} 0"
  accordion-body:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: "0 {spacing.sm}"
  color-swatch:
    rounded: "{rounded.full}"
    size: 32px
    border: "2px solid transparent"
  color-swatch-selected:
    border: "2px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for “Add to Cart,” “Shop Now,” and key conversion points. Filled with the brand’s deep forest green (`{colors.primary}`) and white text (`{colors.on-primary}`), it uses `{rounded.sm}` (8px) for a soft but not pill-like corner. On hover, it shifts to `{colors.primary-active}` (#1a3530), and when disabled, it fades to `{colors.primary-disabled}` (#8ba8a2). The button uses `{typography.button-md}` (15px, 600 weight) with 0.3px letter spacing for a slightly elevated, intentional feel.

**`button-secondary`** — An outlined variant for less prominent actions, such as “Learn More” or “View Details.” It uses a transparent background with a 2px solid `{colors.ink}` border on `{colors.canvas}`. On hover, the background fills with a subtle `{colors.surface-soft}` tint. This button maintains the same `{rounded.sm}` and `{typography.button-md}` as the primary.

**`button-tertiary`** — A text-only link styled as a button, used for inline actions like “See all” or “Read reviews.” It has no background or border, uses `{colors.primary}` for the text, and underlines on hover. This keeps the UI clean while maintaining a clear interactive state.

**`button-pill`** — A smaller, fully rounded button (`{rounded.full}`) used for filters, category tags, or quick-select options. It uses `{colors.primary}` background with white text and `{typography.button-sm}` (13px, 600 weight). Its compact 40px height makes it ideal for horizontal strips.

### Cards
**`product-card`** — The primary container for product listings, used on collection pages and search results. It has a white background (`{colors.surface-card}`), `{rounded.md}` (12px) corners, and 16px padding. The card image sits at the top with `{rounded.sm}` (8px) corners, followed by the product title in `{typography.title-sm}` and the price in `{typography.body-sm}` with `{colors.muted}` text. On hover, the card gains a subtle shadow (not captured in tokens) to indicate interactivity.

### Navigation
**`nav-bar`** — The top navigation bar, fixed at 72px height with a `{colors.canvas}` background and a thin bottom border (`1px solid {colors.hairline-soft}`). It contains the brand logo, navigation links using `{typography.nav-link}`, and utility icons (search, account, cart). The bar is sticky on desktop and collapses into a hamburger menu on mobile.

**`nav-link`** — Individual navigation items with no background, `{colors.ink}` text, and 8px vertical padding. The active state adds a 2px bottom border in `{colors.primary}` and changes text color to the primary green, signaling the current page or section.

### Forms
**`text-input`** — Standard text input fields used in checkout, account forms, and search. They have a `{colors.canvas}` background, `{rounded.sm}` (8px) corners, 12px/16px padding, and a 1px `{colors.hairline}` border. On focus, the border thickens to 2px and turns `{colors.primary}`. Error states use a 2px `{colors.error}` border with an accompanying error message in `{colors.error}` text.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a `{colors.surface-soft}` background and a subtle border. It’s 48px tall with 12px/20px padding, using `{typography.body-md}` for the input text. A search icon sits on the left, and the placeholder text uses `{colors.muted-soft}`.

### Badges
**`badge-new`** — A small, fully rounded pill badge used to indicate new arrivals. It has a mint green background (`{colors.accent-mint}`) with dark green text (`{colors.primary}`), using `{typography.badge}` (11px, 700 weight, uppercase) for a compact, attention-grabbing label.

**`badge-sale`** — Similar in shape to the new badge but with a warm terracotta background (`{colors.accent-warm}`) and white text, used for promotional pricing or clearance items.

**`badge-eco`** — A lime green badge (`{colors.accent-lime}`) with dark text, used to highlight sustainable materials or eco-friendly certifications, reinforcing Buffy’s brand values.

### Hero Section
**`hero-section`** — The full-width hero banner on the homepage and key landing pages. It uses `{colors.canvas}` as the background with `{typography.display-xl}` (48px Recoleta Bold) for the headline. The section has generous padding (`{spacing.section}` top/bottom, `{spacing.lg}` sides) to create breathing room. The primary CTA (`hero-cta`) is a larger 56px-tall button with 16px/32px padding, using the same `{rounded.sm}` and `{colors.primary}` styling.

### Footer
**`footer`** — A full-width footer with a `{colors.primary}` background and white text. It contains columns of links, social icons, and legal text. Footer links use `{typography.link}` with 0.8 opacity, which increases to 1.0 on hover. The footer has `{spacing.xxl}` vertical padding and `{spacing.lg}` horizontal padding.

### Accordion
**`accordion`** — Used for FAQ sections and product details. Each accordion item has a white background, `{rounded.sm}` (8px) corners, and a 1px `{colors.hairline-soft}` border. The header uses `{typography.title-sm}` and the body uses `{typography.body-sm}` with `{colors.body}` text. A chevron icon rotates on open/close states.

### Color Swatch
**`color-swatch`** — A circular 32px swatch used on product detail pages to show available colors. Each swatch has a 2px transparent border by default. When selected (`color-swatch-selected`), the border changes to `{colors.ink}` (2px solid) to indicate the chosen option.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to `{spacing.xl}`; typography scales down (display-xl becomes 32px); search bar becomes full-width; footer links stack in single column |
| Tablet | 744–1128px | Two-column grid for product cards; nav-bar shows limited links with “More” dropdown; hero section uses `{spacing.xxl}` padding; typography scales moderately (display-xl becomes 40px) |
| Desktop | 1128–1440px | Full multi-column layout; nav-bar shows all primary links; product cards in 3–4 column grid; hero section uses `{spacing.section}` padding; typography at full size |
| Wide | > 1440px | Max-width container (1440px) centered; increased whitespace; product cards in 4-column grid; hero section may include larger imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons and swatches are at least 32px with 44px touch area via padding
- Accordion headers have 48px minimum height for easy tapping
- Navigation links have 44px minimum touch area

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Product filters collapse into a slide-out drawer on mobile
- Multi-column footers collapse into a single column below 744px
- Accordion sections remain collapsed by default on all breakpoints
- Hero section reduces padding and font size progressively on smaller screens

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons (exact color shifts not extracted)
- Focus ring styles and keyboard navigation indicators
- Error state styling for forms beyond border color (error message typography, icon placement)
- Dark mode or high-contrast mode variants
- Sub-brand or collection-specific color palettes (e.g., limited edition drops)
- Animation and transition timing values (ease-in-out durations)
- Shadow and elevation tokens for cards, modals, and dropdowns
- Modal, tooltip, and popover component specifications
- Loading states and skeleton screen patterns
- Checkbox, radio button, and toggle switch styling
- Dropdown select menu styling (native vs custom)
- Video player and media gallery component details
- Print stylesheet specifications
- Accessibility-specific tokens (focus-visible, reduced motion)
