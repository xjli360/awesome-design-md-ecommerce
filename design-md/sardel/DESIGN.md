---
version: alpha
name: "Sardel"
source_url: "https://sardelkitchen.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sardel is a premium cookware brand that speaks in a confident, modern voice — a deep, almost ink-black primary palette of `#1d1e20` and `#36344d` anchors a system that feels both luxurious and approachable. The brand’s signature energy comes from a vibrant coral-pink accent, `#d63163`, which appears on primary buttons, badges, and key interactive elements, often paired with a softer blush `#fc5185` for hover or secondary states. A secondary purple family — from `#2f1c6a` through `#673de6` to `#8c85ff` — adds depth and a touch of the unexpected, used in navigation accents, product highlights, and illustrative elements. The canvas is a warm off-white `#fff8e2`, not a sterile pure white, giving the entire experience a tactile, kitchen-warm feel. Typography relies on DM Sans, a geometric sans-serif with a friendly, humanist character, set at moderate weights (400–600) for body and display, avoiding the heavy-handedness of traditional luxury brands. Cards and buttons use soft, pill-like radii (`{rounded.sm}` for buttons, `{rounded.lg}` for cards), while the overall layout is generously spaced with `{spacing.lg}` and `{spacing.xl}` margins, letting product photography and the brand’s distinctive color blocks breathe. The design system feels like a well-edited kitchen: every element has a purpose, the tools are beautiful but functional, and the warmth comes from the materials, not the decoration.

colors:
  primary: "#d63163"
  primary-active: "#fc5185"
  primary-disabled: "#ffe8ef"
  ink: "#1d1e20"
  body: "#36344d"
  muted: "#727586"
  muted-soft: "#dadce0"
  hairline: "#d8dae0"
  hairline-soft: "#e3ebf9"
  canvas: "#fff8e2"
  surface-soft: "#f2f3f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-purple: "#673de6"
  accent-purple-soft: "#8c85ff"
  accent-purple-light: "#ebe4ff"
  accent-purple-dark: "#2f1c6a"
  accent-blue: "#357df9"
  accent-blue-soft: "#d5dfff"
  accent-blue-dark: "#265ab2"
  accent-teal: "#00b090"
  accent-teal-soft: "#def4f0"
  accent-teal-dark: "#008361"
  accent-gold: "#fea419"
  accent-gold-soft: "#ffd28c"
  accent-gold-dark: "#9f6000"
  badge-new: "#ffcd35"
  badge-sale: "#d63163"
  star-rating: "#fea419"
  scrim: "#1d1e20"
  error: "#d63163"
  success: "#00b090"

typography:
  display-xl:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'DM Sans', Arial, Helvetica, sans-serif"
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
  section: 80px

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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
  button-outline-purple:
    backgroundColor: "transparent"
    textColor: "{colors.accent-purple}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.accent-purple}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-purple}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.lg}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    color: "{colors.accent-purple}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.display-sm}"
    color: "{colors.body}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 56px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "2px solid {colors.accent-purple}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.accent-purple-soft}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-category:
    backgroundColor: "{colors.accent-purple-light}"
    textColor: "{colors.accent-purple-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  icon-button:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: "1px"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the brand’s signature coral `{colors.primary}`. On hover, it shifts to a brighter `{colors.primary-active}` for a playful, energetic feel. The disabled state uses a soft pink `{colors.primary-disabled}` with muted text. All primary buttons use `{rounded.sm}` for a friendly, approachable corner.

**`button-secondary`** — A clean, outlined alternative for less prominent actions. Uses a white canvas background with a subtle `{colors.hairline}` border. On active state, the border deepens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`. Ideal for "Learn More" or secondary CTAs.

**`button-outline-purple`** — A brand-specific variant that leverages the purple accent `{colors.accent-purple}` for actions related to premium or curated content. Transparent background with a 2px solid border. Used for "Explore Collections" or "View Recipe" links.

**`button-pill-primary`** and **`button-pill-secondary`** — Pill-shaped buttons (`{rounded.full}`) used in tight spaces like filter bars, tag clouds, or mobile navigation. The primary pill uses `{colors.primary}`; the secondary uses a white canvas with a hairline border. Both use `{typography.button-sm}` for compact sizing.

### Cards
**`product-card`** — The core product display component, using a white `{colors.surface-card}` background with `{rounded.lg}` for a soft, premium feel. Each card contains a product image (with `{rounded.md}`), a title using `{typography.title-sm}`, and a price in `{colors.primary}`. An optional `{components.product-card-badge}` overlays the image corner for "New" or "Sale" indicators.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height, using the warm canvas `{colors.canvas}`. Links use `{typography.nav-link}` and shift to `{colors.primary}` with a 2px bottom border on the active page. Hover state transitions to `{colors.accent-purple}`. The nav bar includes the brand logo, primary links, a search icon, and a cart icon.

### Forms
**`text-input`** — Standard text input fields for search, newsletter signup, and account forms. Uses `{colors.canvas}` background with a `{colors.hairline}` border. On focus, the border becomes a 2px `{colors.accent-purple}` line. Error state uses a 2px `{colors.error}` border. Height is 48px for comfortable touch interaction.

### Footer
**`footer`** — A dark footer section using `{colors.ink}` as the background, creating a strong visual anchor. Text is in `{colors.muted-soft}` for readability. Links use `{typography.link}` and hover to `{colors.accent-purple-soft}`. The footer includes columns for product categories, support, about, and social links.

### Badges
**`badge-new`** — A bright yellow `{colors.badge-new}` pill badge used to flag newly added products. Uses `{typography.badge}` with uppercase text for a punchy, attention-grabbing label.

**`badge-sale`** — A coral `{colors.badge-sale}` pill badge for sale or discounted items. Uses white text for contrast. Same typography and shape as the new badge.

**`badge-category`** — A softer purple `{colors.accent-purple-light}` badge with dark purple `{colors.accent-purple-dark}` text, used for category tags or dietary labels (e.g., "Non-Stick", "Oven Safe"). Slightly larger padding for readability.

### Hero
**`hero-section`** — The full-width hero area on the homepage, using `{colors.canvas}` background. Contains a large `{typography.display-xl}` heading, a `{typography.display-sm}` subheading, and a prominent `{components.hero-cta}` button. Padding uses `{spacing.section}` for generous vertical breathing room.

### Search
**`search-bar`** — A pill-shaped search bar (`{rounded.full}`) with a white card background and a soft `{colors.hairline-soft}` border. On focus, the border becomes a 2px `{colors.accent-purple}` line. Height is 56px for comfortable typing. Used in the nav bar and on the search results page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero heading reduces to `{typography.display-lg}`; buttons become full-width; footer stacks in a single column |
| Tablet | 744–1128px | Two-column product grid; nav bar shows primary links only; hero uses `{typography.display-lg}`; side-by-side footer columns (2x2) |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero at full `{typography.display-xl}`; four-column footer |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to four columns; hero content centered with larger margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44x44px touch target on mobile
- Icon buttons in the nav bar are 40x40px with 8px padding
- Product card tap targets include the entire card surface
- Filter pills and badges are at least 32px tall with comfortable spacing

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer
- The category filter strip collapses into a horizontal scrollable row on tablet and mobile
- The footer’s multi-column layout collapses to a single column on mobile
- Product image galleries switch from grid to single-image swipe on mobile
- Hero sections reduce vertical padding on mobile to avoid excessive scrolling

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary button states are documented
- Error styling for forms (validation messages, error icons) is inferred from the primary error color
- Dark mode palette is not present on the live site; all tokens assume the light theme
- Sub-brand or seasonal color palettes (e.g., holiday collections) are not documented
- Animation and transition timing values (e.g., button hover speed, card lift) were not extractable
- Specific font weights for DM Sans beyond 400, 500, 600, and 700 are assumed based on common availability
- The exact border-radius for product cards (`{rounded.lg}`) is an estimate based on visual inspection; the live value may be 16px or 24px
- Drop shadow values for cards and modals are not captured; a generic `box-shadow` may need to be added
- The `{colors.surface-card}` token is assumed to be white; the live site may use a slightly off-white for cards
- Accessibility contrast ratios for all color combinations have not been verified
- The `{typography.badge}` text-transform is assumed to be uppercase based on common badge patterns
