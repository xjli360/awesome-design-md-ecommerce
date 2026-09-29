---
version: alpha
name: "Parachute"
source_url: "https://www.parachutehome.com"
captured_at: "2026-09-28T04:10:23.977780+00:00"
evidence_status: "historical_partial_css_evidence"
description: |-
  Parachute is a warm, tactile home brand that speaks in whispers of linen and stone. The canvas is never white — it's `#f8f8f8` or `#f1eee9`, a soft, almost chalky off-white that feels like sun-bleached cotton. The brand's signature mood is built on a muted, earthy palette: `#0c0c0c` for deep ink, `#3b3b3b` for body text, and `#88432a` or `#80422c` for warm terracotta accents that evoke clay and sunset. A quiet sage green (`#aab3a3`) and a deep teal (`#1b5351`) add depth, while `#fffcf1` provides a creamy highlight. The typography leans on Neue Montreal and Suisse Intl, set in clean, generous weights — never heavy, always inviting. Rounded corners are soft but not pillowy: `{rounded.sm}` (8px) for buttons, `{rounded.md}` (12px) for cards, and `{rounded.lg}` (20px) for hero sections. The overall effect is one of calm, considered simplicity — a digital space that feels as soothing as the products it sells.

colors:
  primary: "#0c0c0c"
  primary-active: "#3b3b3b"
  primary-disabled: "#e3dfd7"
  ink: "#0c0c0c"
  body: "#3b3b3b"
  muted: "#6a6a6a"
  muted-soft: "#aab3a3"
  hairline: "#e3dfd7"
  hairline-soft: "#efede7"
  canvas: "#f8f8f8"
  surface-soft: "#f1eee9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-terracotta: "#88432a"
  accent-teal: "#1b5351"
  accent-sage: "#aab3a3"
  accent-cream: "#fffcf1"
  star-rating: "#0c0c0c"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Neue Montreal', 'Suisse Intl', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 600
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
    padding: 14px 32px
    height: 48px
  button-primary-hover:
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
    padding: 14px 32px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.accent-terracotta}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    border-bottom: "2px solid {colors.ink}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.base} 0"
  category-tab-active:
    textColor: "{colors.ink}"
    border-bottom: "2px solid {colors.ink}"
  category-tab-inactive:
    textColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in deep ink (`{colors.primary}`) with white text (`{colors.on-primary}`). On hover, it shifts to a softer charcoal (`{colors.primary-active}`). When disabled, it fades to a muted beige (`{colors.primary-disabled}`) with muted text. The `{rounded.sm}` corners and uppercase lettering give it a tailored, intentional feel.

**`button-secondary`** — A light, outlined variant on the primary canvas (`{colors.canvas}`) with a thin hairline border (`{colors.hairline}`). On hover, the border deepens to ink and the background takes on a soft surface tone (`{colors.surface-soft}`). Used for "Shop Now" or "Learn More" actions alongside primary buttons.

**`button-tertiary`** — A text-only button with no background or border. It relies on the `{typography.button-md}` uppercase styling and sits flush against content. Used for "View All" links or secondary navigation within cards.

### Cards
**`product-card`** — A clean, white card (`{colors.surface-card}`) with `{rounded.md}` corners. The image sits flush to the top corners, while the title and price are padded below. The card has no shadow — it relies on the soft canvas background (`{colors.canvas}`) for separation. On hover, a subtle border or shadow may appear (not captured in extraction).

**`hero-section`** — A large, full-width banner with a soft surface background (`{colors.surface-soft}`). It uses the lightest display weight (`{typography.display-xl}`) and generous padding (`{spacing.section}`). The hero CTA is the primary button, centered or left-aligned depending on layout.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on a white canvas (`{colors.canvas}`). Navigation links use `{typography.nav-link}` with 0.3px letter spacing. The active link is underlined with a 2px ink border; inactive links are muted. The bar has a subtle bottom border (`{colors.hairline-soft}`).

**`category-strip`** — A horizontal scrollable strip of category tabs below the nav. Each tab uses `{typography.button-sm}` uppercase styling. The active tab is underlined with ink; inactive tabs are muted. This strip collapses into a dropdown or hamburger menu on mobile.

### Forms
**`text-input`** — A standard input field with a white background, ink text, and a thin hairline border. On focus, the border turns ink. On error, it turns terracotta (`{colors.accent-terracotta}`). The `{rounded.sm}` corners and 48px height match the button sizing for alignment.

### Badges
**`badge-new`** — A small, pill-shaped badge in deep teal (`{colors.accent-teal}`) with white uppercase text. Used to highlight new arrivals or collections.
**`badge-sale`** — A similar pill badge in terracotta (`{colors.accent-terracotta}`) for sale or clearance items.

### Footer
**`footer`** — A full-width footer in deep ink (`{colors.primary}`) with white text. Links are styled as `{typography.link}` and sit on generous padding. The footer may include columns for customer service, about, and social links.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a white background and hairline border. It sits at 48px height, matching the button height, and uses `{typography.body-md}` for placeholder text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger, hero padding reduces to `{spacing.xl}`, product cards stack vertically, category strip becomes a horizontal scroll |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, hero uses `{typography.display-lg}`, footer columns stack to 2 |
| Desktop | 1128–1440px | Full three-column product grid, expanded nav, hero uses `{typography.display-xl}`, footer in 4 columns |
| Wide | > 1440px | Max-width container at 1440px, centered content, hero may include full-bleed imagery |

### Touch Targets
- All buttons and interactive elements are minimum 48px height for touch accessibility.
- Search bar and text inputs match button height (48px) for consistent tap targets.
- Nav links have a minimum 44px tap area.
- Category strip items are at least 44px wide.

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px.
- Category strip becomes a horizontal scrollable row on mobile.
- Product grid collapses from 3 columns to 2 on tablet, to 1 on mobile.
- Footer columns collapse from 4 to 2 on tablet, to 1 on mobile.
- Hero section reduces padding and font size on mobile.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Hover states for product cards (shadow or border changes) not reliably extracted.
- Error styling for forms beyond border color (error messages, icons) not captured.
- Dark mode palette not present on the live site.
- Sub-brand or collection-specific color variations (e.g., "Linen" vs "Cotton" collections) not extracted.
- Animation and transition timings (ease-in-out durations) not available.
- Specific font weights beyond 300, 400, 500, 600 not confirmed.
- Dropdown menu styles for navigation and filters not captured.
- Modal and overlay styles (e.g., quick-view, cart drawer) not extracted.
- Focus-visible styles for keyboard navigation not reliably detected.
