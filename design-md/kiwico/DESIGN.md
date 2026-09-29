---
version: alpha
name: "KiwiCo"
source_url: "https://www.kiwico.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A green voltage of #07b261 runs through every primary CTA, subscription badge, and age-bracket pill, while a secondary spark of #d33600 ignites sale banners and urgency markers — the brand uses color as a signal system for action, not just decoration. The typography stack leans on Centra, a geometric sans-serif with a friendly circular 'O' and open apertures, set at moderate weights (500–600) rather than heavy 700+ that would feel too serious for a kids' brand. Product cards float on a #f6fbfe canvas with soft shadows and {rounded.lg} corners, each one displaying a crisp age range badge in the primary green and a playful product name in display type. The subscription flow, the brand's core conversion engine, uses a three-step progress bar with numbered circles filled in #07b261 and a pill-shaped "Get started" button that repeats the same green — no secondary color competes for attention during checkout. Illustrations of smiling molecules, gears, and animals appear throughout category headers and empty states, drawn in a flat vector style with the brand's accent palette (#dbb300 for curiosity sparks, #da532c for energy). The overall feel is that of a clean, well-lit classroom where every corner has something bright to discover — generous whitespace, no hard corners on interactive elements, and a color system that tells you exactly where to tap next.

colors:
  primary: "#07b261"
  primary-active: "#008247"
  primary-disabled: "#b8e6c8"
  ink: "#1a1a2e"
  body: "#3d3d5c"
  muted: "#6b6b8a"
  muted-soft: "#9e9eb5"
  hairline: "#d4d4e0"
  hairline-soft: "#e8e8f0"
  canvas: "#ffffff"
  surface-soft: "#f6fbfe"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#d33600"
  accent-yellow: "#dbb300"
  accent-red: "#da532c"
  badge-green: "#1ab064"
  badge-blue: "#1d5fbf"
  star-rating: "#dbb300"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  micro-label:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.1px
  link:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Centra', 'Helvetica', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 19px
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
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-orange}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
    shadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    shadow: "0 4px 16px rgba(0,0,0,0.12)"
  age-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  age-badge-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 11px
    border: "1px solid {colors.primary}"
  subscription-progress-step:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 32px
  subscription-progress-step-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 32px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  rating-star:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Subscribe," "Get started," and "Add to cart" actions. On hover, the background shifts to `{colors.primary-active}` (#008247) for a clear state change. The disabled state uses `{colors.primary-disabled}` with `{colors.muted-soft}` text, signaling the button is non-interactive without visual noise.

**`button-secondary`** — An outlined variant for secondary actions like "Learn more" or "See all crates." The 2px `{colors.primary}` border sits on a white background, and on hover the border and text shift to `{colors.primary-active}`. Use for actions that are important but not the primary conversion goal.

**`button-accent-orange`** — Reserved for urgency-driven actions: limited-time offers, sale banners, and countdown CTAs. The `{colors.accent-orange}` (#d33600) background creates visual contrast against the green system, drawing the eye to time-sensitive promotions.

**`button-pill-primary`** — A smaller, fully rounded variant used for inline subscription prompts, age-bracket selection, and filter actions. Its `{rounded.full}` shape and compact padding make it feel friendly and non-intrusive, perfect for secondary conversion points within content.

**`button-pill-outline`** — The lightest button variant, used for "Cancel" or "Skip" actions in the subscription flow, or for dismissible tags. The thin `{colors.hairline}` border keeps it present but quiet, and on hover the border thickens to 2px for feedback.

### Cards
**`product-card`** — The primary content container for crate listings, product pages, and subscription plan cards. A white surface with a subtle shadow (`0 2px 8px rgba(0,0,0,0.08)`) and `{rounded.lg}` corners gives each card a lifted, approachable feel. On hover, the shadow deepens to `0 4px 16px rgba(0,0,0,0.12)` for a gentle elevation cue. The card contains a product image (typically a crate photo or illustration), the `age-badge`, the product title in `{typography.title-sm}`, and a short description in `{typography.body-sm}`.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on white background. The logo sits on the left, followed by category links ("Shop," "Subscription," "About," "Gift") using `{typography.nav-link}`. The active page link gets a 2px `{colors.primary}` bottom border and green text. On mobile, the nav collapses into a hamburger menu with a slide-out drawer.

**`nav-link-active`** — The active state for navigation items, distinguished by the green bottom border and green text color. This provides a clear wayfinding signal without relying on background fills or bold weights.

### Badges & Pills
**`age-badge`** — A small, fully rounded badge displaying the recommended age range for each crate (e.g., "Ages 3-4," "Ages 5-8"). The `{colors.primary}` background with white text makes these badges immediately scannable against product card imagery. An outlined variant (`age-badge-outline`) is used on colored or image-heavy backgrounds.

**`category-pill`** — Filter pills used on the shop page to sort crates by age group or interest (e.g., "Science," "Art," "Geography"). Inactive pills use a soft gray background (`{colors.surface-soft}`) with body text; the active pill switches to `{colors.primary}` with white text. The `{rounded.full}` shape and 8px vertical padding make them easy to tap on mobile.

### Forms
**`text-input`** — Standard text input for email signups, search, and checkout forms. A white background with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border becomes 2px `{colors.primary}` for clear focus indication. Error states use `{colors.accent-orange}` border with an error message in `{typography.caption}` below.

### Subscription Flow
**`subscription-progress-step`** — Numbered circles (1, 2, 3) in the subscription setup flow. Inactive steps show a light gray circle with muted text; the active step fills with `{colors.primary}` and white text. A connecting line between steps uses `{colors.hairline}` for incomplete and `{colors.primary}` for completed segments.

### Search
**`search-bar`** — A pill-shaped search input with a soft gray background (`{colors.surface-soft}`) and a magnifying glass icon in `{colors.muted}`. On focus, the background shifts to white with a 2px `{colors.primary}` border. The placeholder text reads "Search crates, activities, or topics..." in `{colors.muted-soft}`.

### Footer
**`footer`** — A dark footer section on `{colors.ink}` background with links in `{colors.muted-soft}`. Links use `{typography.link}` with underline on hover. The footer contains columns for "Shop," "About," "Support," and "Connect," plus social media icons. A thin `{colors.muted}` top border separates it from the main content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to `{typography.display-md}`; age badges become full-width; search bar moves below nav |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses `{typography.display-lg}`; category pills wrap to two rows; subscription flow shows all three steps |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses `{typography.display-xl}`; category pills in a single horizontal strip; subscription flow side-by-side |
| Wide | > 1440px | Max-width container at 1440px; product grid can show four columns; hero has larger imagery; additional whitespace around content sections |

### Touch Targets
- All interactive elements (buttons, links, pills) have a minimum height of 44px for touch accessibility
- Category pills and age badges are at least 40px tall with 16px horizontal padding
- Icon buttons are 40px × 40px circles
- Search bar is 48px tall for easy tapping
- Nav links have 44px minimum tap area even when text is smaller

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu; the slide-out drawer contains all nav links plus a "Subscribe" CTA button
- Category pill strip collapses from horizontal scroll to a two-row wrap on tablet, then to a single-row horizontal scroll on mobile
- Product grid collapses from 4 columns (wide) → 3 (desktop) → 2 (tablet) → 1 (mobile)
- Hero section reduces image size and stacks content vertically on mobile
- Footer columns collapse from 4 columns (desktop) to 2 (tablet) to a single column with accordion sections (mobile)
- Subscription progress steps stack vertically on mobile instead of horizontal

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary button and product card hover states are confirmed
- Error state styling for forms (colors, icons, animation) is inferred from the accent-orange color but not verified
- Dark mode or high-contrast mode variants are not present in the extracted data
- Sub-brand or seasonal color palettes (e.g., holiday promotions, special edition crates) are not documented
- Animation timing and easing curves (button press, card hover, page transitions) are not available
- The exact font stack order for Centra is assumed; the extracted fonts include "Centra" but the full fallback chain is inferred from common web patterns
- Icon set details (SVG vs icon font, specific icon names) are not captured
- Print styles and email template styles are not included
- The `#1877f2`, `#4267b2`, `#007aff` colors in the extraction are likely social media icon colors (Facebook, Apple) and are not part of the brand palette
- The `#f7f7f7` color is likely a generic background tone and may not be a deliberate brand token
