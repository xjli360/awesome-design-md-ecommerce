---
version: alpha
name: "Haand"
source_url: "https://haand.us"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Haand is a slow, tactile brand rooted in the earthy warmth of handmade porcelain pottery, crafted in North Carolina, USA. The brand's visual language is a study in quiet contrast, where the raw, organic feel of clay meets a refined, almost monastic palette. The dominant canvas is a soft, warm off-white (`#fcfafa`), a shade that feels like unglazed porcelain, providing a gentle backdrop for the rich, earthy accents that define the brand. The primary voltage comes from a deep, fired-clay brown (`#915a05`), used sparingly but powerfully on key calls-to-action and navigation elements, evoking the kiln's heat and the earth from which the pieces are born. This is balanced by a range of muted, natural tones: the deep charcoal of unglazed stoneware (`#1c1b1b`), the soft sage of a weathered glaze (`#75867e`), and the warm terracotta of a sunset-fired pot (`#b74205`). Typography is set in a clean, utilitarian sans-serif (Arial, Helvetica), chosen for its neutrality and legibility, allowing the organic forms of the pottery to take center stage. The brand's signature design moves include generous whitespace that mimics the breathing room of a gallery, soft rounded corners (`{rounded.sm}`) that echo the gentle curves of a hand-thrown bowl, and a consistent use of hairline-thin borders (`{colors.hairline}`) that define product cards and sections without adding visual weight. The overall feeling is one of grounded sophistication — a brand that trusts the beauty of its materials and the skill of its makers, communicating through subtlety rather than volume. The palette includes a deep, almost-black ink (`#333333`) for body text, ensuring readability against the warm canvas, while a muted gray (`#777777`) handles secondary information and captions, keeping the hierarchy calm and uncluttered. Accents of a vibrant, almost-glowing orange (`#ee682f`) and a deep, oceanic blue (`#1990c6`) appear in limited, strategic moments — perhaps for sale badges or special edition markers — adding a touch of unexpected energy to the otherwise restrained system.

colors:
  primary: "#915a05"
  primary-active: "#7a4b04"
  primary-disabled: "#ccb999"
  ink: "#333333"
  body: "#1c1b1b"
  muted: "#777777"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#dedede"
  canvas: "#fcfafa"
  surface-soft: "#f5f2f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-terracotta: "#b74205"
  accent-sage: "#75867e"
  accent-orange: "#ee682f"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  accent-green: "#1f5329"
  accent-dark: "#1a202e"
  badge-sale: "#ee682f"
  badge-new: "#1990c6"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.3px
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
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
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.accent-terracotta}"
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.05)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1:1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.canvas}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
    marginBottom: "{spacing.md}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.lg} 0"
  accordion-trigger:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.md} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 28px
    width: 28px
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature fired-clay brown (`{colors.primary}`). On hover, it deepens to `{colors.primary-active}` for a subtle tactile response. When disabled, it fades to a muted tan (`{colors.primary-disabled}`), signaling unavailability without visual noise. The uppercase, letter-spaced typography (`{typography.button-md}`) gives it a deliberate, crafted feel, while the soft 8px rounding (`{rounded.sm}`) echoes the gentle curves of the pottery.

**`button-secondary`** — An outlined alternative that sits quietly on the warm canvas (`{colors.canvas}`). The 1px hairline border (`{colors.hairline}`) keeps it light and airy. On active state, the border switches to the deep ink (`{colors.ink}`) and the background takes on a soft surface tone (`{colors.surface-soft}`), providing a clear but understated hierarchy.

**`button-tertiary`** — A text-only button with no border or background, used for less prominent actions like "Cancel" or "Learn More." On hover, it gains a subtle background (`{colors.surface-soft}`) for affordance, but never competes with primary or secondary actions.

### Cards
**`product-card`** — The core container for displaying individual pottery pieces. A clean white background (`{colors.surface-card}`) with a soft hairline border (`{colors.hairline-soft}`) and gentle rounding (`{rounded.sm}`). On hover, the border subtly darkens to `{colors.hairline}` and a light shadow lifts the card, signaling interactivity without breaking the calm grid. The product image sits in a 1:1 aspect ratio with its own rounding (`{rounded.xs}`), while the title and price stack below with generous spacing.

**`badge-sale`**, **`badge-new`**, **`badge-sold-out`** — Small, uppercase, tightly-spaced labels that appear on product cards to denote status. The sale badge uses the vibrant accent orange (`{colors.badge-sale}`) for urgency, while the new badge uses the oceanic blue (`{colors.badge-new}`) for freshness. Sold-out items are marked with a neutral gray (`{colors.muted-soft}`), keeping the visual hierarchy calm even when communicating unavailability.

### Navigation
**`nav-bar`** — A fixed-height top bar (72px) on the warm canvas (`{colors.canvas}`), separated from the page content by a thin, almost imperceptible border (`{colors.hairline-soft}`). Navigation links are set in uppercase, letter-spaced type (`{typography.nav-link}`), with the active state marked by a 2px underline in the brand brown (`{colors.primary}`). Inactive links recede into a muted gray (`{colors.muted}`), ensuring the active page is immediately clear.

**`breadcrumb-link`** and **`breadcrumb-current`** — A secondary navigation pattern for deep product categories. Links are set in small, muted type (`{typography.caption}`), with the current page rendered in the brand's ink (`{colors.ink}`) for clarity.

### Forms
**`text-input`** — A standard input field with a hairline border (`{colors.hairline}`) and soft rounding (`{rounded.sm}`). On focus, the border switches to the primary brown (`{colors.primary}`), providing a clear but gentle state change. Error states use the terracotta accent (`{colors.accent-terracotta}`) for the border, paired with a caption-style label (`{typography.caption}`) in the muted tone (`{colors.muted}`).

**`quantity-selector`** — A compact, bordered container for adjusting item quantities. The central value is displayed in the body type (`{typography.body-md}`), flanked by two small, square buttons (`{colors.surface-soft}`) for increment and decrement. The overall feel is utilitarian and clean, matching the brand's no-nonsense approach.

### Footer
**`footer-section`** — A deep, dark footer (`{colors.ink}`) that grounds the page. Links are set in a muted gray (`{colors.muted-soft}`) and lighten to the canvas white (`{colors.canvas}`) on hover. Section headings use the title type (`{typography.title-sm}`) in white, creating clear visual hierarchy against the dark background.

### Other Components
**`hero-section`** — A full-width, tall section (min-height 400px) on the warm canvas (`{colors.canvas}`), used for landing pages and collection headers. The title uses the lightest display weight (`{typography.display-xl}`) with generous letter-spacing, while the subtitle sits in the body type (`{typography.body-md}`) in the muted tone (`{colors.muted}`). The overall effect is spacious and editorial, letting the photography do the heavy lifting.

**`accordion-trigger`** and **`accordion-content`** — Used for product details, shipping information, and FAQ sections. The trigger is a simple title (`{typography.title-sm}`) on the canvas, separated by a hairline border. The content area uses the smaller body type (`{typography.body-sm}`) and appears with a smooth animation, maintaining the brand's calm, unhurried pace.

**`pagination-button`** — A simple bordered square for navigating product lists. The active page is filled with the primary brown (`{colors.primary}`) and white text, while inactive pages remain transparent with a hairline border. The design is minimal and functional, never distracting from the product grid.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger menu; hero section reduces padding and font sizes; footer links stack vertically; search bar becomes full-width; quantity selector reduces padding |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links with "More" dropdown; hero section maintains two-column layout; footer uses two-column grid; search bar remains in nav but collapses to icon |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; hero section uses full typography scale; footer uses four-column grid; search bar is fully expanded |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centers content; hero section may use wider imagery; footer grid expands to five columns for additional link groups |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px on mobile and tablet.
- Product card tap targets extend to the full card area, not just the title or price.
- Quantity selector buttons are 28x28px minimum, with additional padding to ensure comfortable tapping.
- Nav-bar hamburger icon is 44x44px with generous padding.

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger menu, with all links hidden behind a slide-out drawer.
- The search bar collapses to a magnifying glass icon, expanding to full-width on tap.
- Product filters collapse into a "Filter" button that opens a modal or drawer.
- The footer link columns collapse to a single vertical stack, with section headings acting as accordion triggers.
- Multi-column hero layouts collapse to a single column, with text stacking below the image.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card images (zoom effect, secondary image reveal) could not be reliably extracted.
- Error styling for form validation (inline error messages, error iconography) is inferred from the general palette but not confirmed.
- Sub-brand or collection-specific palettes (e.g., seasonal releases, limited editions) are not captured.
- Dark mode tokens are not available; the brand appears to use a light-only scheme.
- Animation timing and easing curves (transition durations, hover effects, accordion animations) are not specified.
- Focus ring styles (outline color, offset, width) for keyboard navigation are not documented.
- The exact font stack for headings vs. body text could not be differentiated; both use Arial/Helvetica fallbacks.
- Dropdown menu styles (mega menu, sub-navigation) for the nav-bar are not captured.
- Loading states (skeleton screens, spinner styles) are not defined.
- Print styles and accessibility contrast ratios are not verified.
