---
version: alpha
name: "Bevel"
source_url: "https://getbevel.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bevel is a men's grooming brand built for the modern man who values precision, performance, and a clean aesthetic. The brand's visual language is anchored on a deep, almost-black ink (`#1c1c1c`) and a stark canvas (`#fafafa`), with a signature electric blue (`#0066ff`) that serves as the primary voltage for all CTAs, interactive elements, and key accents. This blue, paired with a secondary deep teal (`#1990c6`) and its darker variant (`#136f99`), creates a palette that feels both authoritative and approachable — a nod to barbershop precision and tech-forward thinking. The typography relies on DinPro and DinProCondensed, geometric sans-serif families that convey strength, clarity, and a slight industrial edge. Display sizes are set in DinProCondensed for a compact, impactful headline presence, while body copy uses DinPro for readability. The system uses generous whitespace and a restrained set of rounded corners — from sharp `{rounded.none}` for form fields to soft `{rounded.sm}` for buttons and `{rounded.md}` for cards — ensuring every interaction feels deliberate. The muted palette (`#777777`, `#6d6d6d`, `#a4a4a4`) provides a quiet backdrop for product photography, while the hairline (`#dedede`, `#dddddd`) and soft hairline (`#c6c6c6`) define structural boundaries without adding visual noise. The overall mood is confident, clean, and premium — a grooming brand that treats its digital presence with the same care as its product formulations.

colors:
  primary: "#0066ff"
  primary-active: "#0052cc"
  primary-disabled: "#b3d4ff"
  ink: "#1c1c1c"
  body: "#494949"
  muted: "#777777"
  muted-soft: "#a4a4a4"
  hairline: "#dedede"
  hairline-soft: "#c6c6c6"
  canvas: "#fafafa"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  teal: "#1990c6"
  teal-dark: "#136f99"
  dark-surface: "#121212"
  dark-ink: "#050505"
  badge-new: "#0066ff"
  badge-sale: "#1990c6"
  star-rating: "#1c1c1c"
  error: "#d32f2f"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'DinProCondensed', 'DinPro', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DinProCondensed', 'DinPro', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DinProCondensed', 'DinPro', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'DinProCondensed', 'DinPro', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'DinPro', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'DinPro', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'DinPro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DinPro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DinPro', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'DinPro', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'DinPro', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'DinPro', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'DinPro', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'DinPro', sans-serif"
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-tertiary-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
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
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    border-bottom: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,102,255,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    typography: "{typography.badge}"
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-section-dark:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    border-bottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  tab-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for add-to-cart, subscribe, and key conversion points. It uses the brand's signature blue (`#0066ff`) with white text and a soft 8px radius. On hover, it shifts to a deeper blue (`#0052cc`), and when disabled, it fades to a light blue (`#b3d4ff`). The uppercase button label with 0.5px letter-spacing reinforces the brand's precise, confident voice.

**`button-secondary`** — An outlined alternative for less prominent actions, featuring a 2px solid ink border on a white canvas. On hover, the button inverts to a solid ink fill with white text, providing a clear visual hierarchy. The disabled state uses a muted-soft border and text, signaling non-interactivity.

**`button-tertiary`** — A text-only button with no background or border, used for secondary links like "Learn More" or "View Details." It uses the primary blue for text, with a darker active state. This button is ideal for inline actions where a full button would be visually overwhelming.

**`button-pill`** — A fully rounded pill variant used for filters, tags, and compact actions. It uses the primary blue with a smaller uppercase label and tighter padding, making it suitable for horizontal strips and mobile interfaces.

### Text Inputs & Forms
**`text-input`** — A clean, border-bottom style input with no border-radius, reflecting the brand's preference for sharp, precise lines. The default state uses a 1px hairline border, which thickens to 2px primary blue on focus. Error states switch to a red border (`#d32f2f`). The 48px height ensures comfortable touch targets on mobile.

**`select-input`** — Shares the same base styling as text-input, with a custom dropdown arrow in the ink color. The no-radius treatment maintains consistency across all form elements.

**`textarea`** — A multi-line input that follows the same border-bottom pattern, with a minimum height of 120px and resizable only vertically to preserve layout integrity.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on a white canvas, with a single hairline bottom border. The nav links use uppercase DinPro at 14px with 0.5px letter-spacing. On scroll, the bar shrinks to 56px and gains a subtle box-shadow for depth. The active link is indicated by a 2px primary blue bottom border.

**`nav-link-active`** — The active navigation state, which uses the ink color and a primary blue underline. This provides a clear, minimal indicator of the user's current section.

**`nav-link-inactive`** — Inactive links use the muted gray (`#777777`) to create visual hierarchy, ensuring the active section stands out without relying on heavy visual treatments.

### Product Cards
**`product-card`** — A white card with a 1px hairline border and 12px rounded corners, containing a square product image, title, price, and optional badges. On hover, the border shifts to primary blue with a subtle blue box-shadow, creating a clear interactive state. The card uses 16px padding for content breathing room.

**`product-card-badge`** — A small, uppercase label positioned at the top-left of the product image, used for "NEW" or "SALE" indicators. It uses the primary blue background with white text and a 4px radius, keeping it compact and legible.

### Hero Section
**`hero-section`** — A full-width hero area with a white canvas and large display typography. The primary CTA is a 56px tall button with 32px horizontal padding, providing a strong visual anchor. A dark variant (`hero-section-dark`) uses the near-black surface (`#121212`) for contrast sections, with white text for readability.

### Search
**`search-bar`** — A fully rounded pill-shaped search input with a 1px hairline border. On focus, the border thickens to 2px primary blue. The 48px height and 20px horizontal padding provide a comfortable, accessible search experience.

### Footer
**`footer-section`** — A dark footer using the near-black surface (`#121212`) with white text and muted-soft links. The section uses 64px vertical padding to create a substantial closing section. Links lighten to full white on hover, providing clear interactivity.

### Badges
**`badge-new`** and **`badge-sale`** — Compact, uppercase labels used to highlight product attributes. The "NEW" badge uses primary blue, while "SALE" uses the teal variant (`#1990c6`), allowing for visual differentiation without introducing additional colors.

### Tabs
**`tab-active`** and **`tab-inactive`** — Tab navigation uses the same uppercase, letter-spaced typography as nav links. Active tabs have an ink color and primary blue underline, while inactive tabs use muted gray. Tab panels use the body typography with 24px padding for content.

### Accordion
**`accordion-header`** — A clickable header with a title-sm typography and a hairline bottom border. The accordion content uses body-md typography with 8px top and 16px bottom padding, creating a clean, expandable content pattern.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero typography reduces to display-md; search bar moves to sticky bottom; footer links stack; section padding reduces to 32px |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links with "More" dropdown; hero uses display-lg; side-by-side form layouts; section padding at 48px |
| Desktop | 1128–1440px | Full nav-bar with all links; three-column product grid; hero uses display-xl; multi-column footer; standard section padding at 64px |
| Wide | > 1440px | Max-width container at 1440px; centered layout with generous margins; four-column product grid; expanded hero with larger imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px touch target height
- Icon buttons are 40x40px with 48px touch area via padding
- Nav links have 48px touch height on mobile
- Product card CTAs are 48px tall for easy tapping
- Accordion headers have 48px touch height

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px, with full-screen overlay menu
- Product grid collapses from 4 columns to 2 columns at tablet, then 1 column at mobile
- Footer link columns collapse to single column below 744px
- Hero section reduces padding and font size progressively
- Search bar becomes sticky at bottom of viewport on mobile
- Multi-step forms collapse to single-step on mobile
- Tab navigation becomes horizontal scrollable strip on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns; exact transition durations and easing curves not extracted
- Error state styling for forms (error messages, validation icons) not reliably captured
- Dark mode palette not present on the live site; dark-surface and dark-ink values are inferred
- Sub-brand or promotional palettes (seasonal, limited edition) not documented
- Animation and motion specifications (duration, easing, stagger) not extracted
- Loading states (skeleton screens, spinners) not captured
- Focus-visible styles for keyboard navigation not reliably identified
- Specific icon set and icon sizing guidelines not documented
- Dropdown menu and mega-menu patterns not fully captured
- Modal and dialog component specifications not extracted
- Tooltip and popover styling not documented
- Rating component exact star sizing and spacing not captured
- Quantity selector component not documented
- Color contrast ratios not verified against WCAG standards
- Print stylesheet not available for extraction
