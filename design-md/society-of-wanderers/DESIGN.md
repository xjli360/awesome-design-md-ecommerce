---
version: alpha
name: "Society of Wanderers"
source_url: "https://societyofwanderers.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Society of Wanderers is an Australian-born decor brand that translates the quiet romance of French flax into a tactile, sun-bleached world. The palette is grounded in a soft, almost dusty neutrality — `#585458` (a warm charcoal) and `#e6e5e6` (a near-white stone) form the backbone, while `#eee3cc` (a pale, aged parchment) and `#b08770` (a sun-baked terracotta) introduce the warmth of natural linen. This is a brand that trusts texture over flash; the signature `{colors.primary}` is a muted `#585458`, not a saturated hue, and primary CTAs use `{colors.primary}` against `{colors.on-primary}` (`#ffffff`) for a quiet, confident contrast. Accents of `#4469af` (a faded indigo) and `#c8232c` (a restrained poppy) appear sparingly — on sale badges or social icons — never competing with the organic calm. Typography is anchored by OchreRegular, a hand-drawn serif that feels like ink on laid paper, paired with Poppins for clean, modern contrast. The brand’s design moves are deliberate: generous `{spacing.section}` (64px) between product rows, `{rounded.sm}` (8px) on buttons that feel soft but not pill-like, and `{rounded.md}` (12px) on product cards that echo the gentle drape of linen. There is no hard geometry — every corner is slightly eased, every shadow is diffuse. The result is a digital space that feels like a sunlit room: unhurried, textural, and deeply residential.

colors:
  primary: "#585458"
  primary-active: "#3e3a3e"
  primary-disabled: "#b9b9b9"
  ink: "#121212"
  body: "#363636"
  muted: "#696969"
  muted-soft: "#939393"
  hairline: "#dedede"
  hairline-soft: "#e6e5e6"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-indigo: "#4469af"
  accent-red: "#c8232c"
  accent-social-blue: "#00aced"
  accent-social-dark-blue: "#1990c6"
  accent-sale: "#f94c43"
  accent-sale-hover: "#e6554d"
  accent-green: "#307a07"
  accent-parchment: "#eee3cc"
  accent-terracotta: "#b08770"
  accent-warm-gray: "#d8cebb"
  accent-light-pink: "#e4c4c4"
  accent-light-green: "#d2e4c4"
  accent-charcoal: "#585458"
  accent-mid-gray: "#989398"
  accent-dark-gray: "#a1a1a1"
  accent-near-black: "#363636"
  accent-border-light: "#c0c0c0"
  accent-error: "#cb2b2b"

typography:
  display-xl:
    fontFamily: "'OchreRegular', 'Poppins', Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'OchreRegular', 'Poppins', Georgia, serif"
    fontSize: 34px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'OchreRegular', 'Poppins', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'OchreRegular', 'Poppins', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'OchreRegular', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02px
  title-sm:
    fontFamily: "'Poppins', 'OchreRegular', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02px
  body-md:
    fontFamily: "'Poppins', 'OchreRegular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'OchreRegular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'OchreRegular', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02px
  caption-sm:
    fontFamily: "'Poppins', 'OchreRegular', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02px
  badge:
    fontFamily: "'Poppins', 'OchreRegular', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', 'OchreRegular', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Poppins', 'OchreRegular', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Poppins', 'OchreRegular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'OchreRegular', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-sale-hover:
    backgroundColor: "{colors.accent-sale-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.lg}"
  nav-bar-scrolled:
    boxShadow: "0 1px 4px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.none}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 2px 8px rgba(0,0,0,0.04)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "3 / 4"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: 8px
    left: 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-banner-overlay:
    backgroundColor: "rgba(18, 18, 18, 0.15)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(88, 84, 88, 0.1)"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginBottom: "{spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
    padding: "4px 0"
  footer-link-hover:
    color: "{colors.primary}"
  social-icon:
    backgroundColor: "{colors.accent-social-blue}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  social-icon-hover:
    backgroundColor: "{colors.accent-social-dark-blue}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 20px"
    height: 44px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  breadcrumb-link:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link-active:
    color: "{colors.ink}"
  pagination-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  loading-spinner:
    borderColor: "{colors.hairline}"
    borderTopColor: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and key conversion points. It uses the brand's muted charcoal `{colors.primary}` (#585458) on a white background, with uppercase Poppins type at 14px and 0.5px letter-spacing. The `{rounded.sm}` (8px) corners are soft but not pill-like, maintaining a refined, residential feel. On hover, it deepens to `{colors.primary-active}` (#3e3a3e). The disabled state uses `{colors.primary-disabled}` (#b9b9b9) for a low-contrast, inactive appearance.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Save for Later". It shares the same dimensions and typography as `button-primary` but uses a white background with a 1px `{colors.primary}` border. On hover, the background shifts to `{colors.surface-soft}` and the border to `{colors.primary-active}`.

**`button-sale`** — A promotional variant reserved for sale items and clearance events. It uses `{colors.accent-sale}` (#f94c43), a restrained poppy red, to create urgency without disrupting the brand's calm aesthetic. On hover, it shifts to `{colors.accent-sale-hover}` (#e6554d).

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 72px height, using a clean white `{colors.canvas}` background. Navigation links use `{typography.nav-link}` — 13px Poppins in uppercase with 0.5px letter-spacing — for a refined, editorial feel. The active state is indicated by a 2px `{colors.primary}` bottom border. On scroll, a subtle box-shadow (`0 1px 4px rgba(0,0,0,0.08)`) is added.

**`nav-link`** — Individual navigation items with 8px vertical and 12px horizontal padding. They are transparent by default and use `{colors.ink}` (#121212) text. The active state uses `{colors.primary}` with the bottom border indicator.

### Cards
**`product-card`** — The primary product display component, featuring a 3:4 aspect ratio image and text details below. The card uses `{rounded.md}` (12px) corners and a subtle `0 2px 8px rgba(0,0,0,0.04)` shadow that deepens on hover. The image area is rounded at the top corners only (`{rounded.md} {rounded.md} 0 0`). The title uses `{typography.title-sm}` (16px Poppins, medium weight) and the price uses `{typography.body-md}` (16px Poppins, regular weight) in `{colors.body}` (#363636).

**`product-card-sale-badge`** — An absolute-positioned badge at the top-left of the product image, using `{colors.accent-sale}` (#f94c43) background with white uppercase badge typography. It uses `{rounded.xs}` (4px) for a subtle, non-distracting corner.

### Forms
**`text-input`** — Standard text input fields used in checkout, account forms, and address entry. They use a white background with `{colors.ink}` text and a 1px `{colors.hairline}` (#dedede) border. On focus, the border switches to `{colors.primary}`. Error states use `{colors.accent-error}` (#cb2b2b) for the border.

**`newsletter-input`** and **`newsletter-submit`** — The email signup form in the footer. The input uses `{colors.body-sm}` typography with a 1px `{colors.hairline}` border. The submit button uses `{colors.button-sm}` typography (12px uppercase) with `{colors.primary}` background.

### Search
**`search-bar`** — A pill-shaped search bar (`{rounded.full}`) with a 1px `{colors.hairline}` border and 12px/20px padding. On focus, it gains a 3px `rgba(88, 84, 88, 0.1)` ring for a subtle glow effect. The typography is `{typography.body-md}` (16px Poppins).

### Footer
**`footer-section`** — The site footer uses `{colors.surface-soft}` (#f7f7f7) background with `{colors.body}` (#363636) text. Headings use `{typography.title-sm}` (16px Poppins, medium weight) in `{colors.ink}`. Links use `{typography.link}` (14px Poppins) in `{colors.muted}` (#696969), with hover shifting to `{colors.primary}`.

**`social-icon`** — Circular social media icons at 36px, using `{colors.accent-social-blue}` (#00aced) for Twitter/X and `{colors.accent-social-dark-blue}` (#1990c6) on hover. Other social platforms would use their respective brand colors.

### Filters & Navigation Aids
**`filter-chip`** — Used in collection filtering, these are pill-shaped (`{rounded.full}`) chips with a 1px `{colors.hairline}` border and `{typography.caption}` (12px Poppins). The active state fills with `{colors.primary}` and white text.

**`breadcrumb-link`** — Small caption-style links (`{typography.caption}`) in `{colors.muted}` (#696969), with the active/current page using `{colors.ink}` (#121212).

**`pagination-button`** — Square pagination buttons at 36px with `{rounded.sm}` (8px) corners. The active page uses `{colors.primary}` background with white text.

### Loading & Dividers
**`loading-spinner`** — A circular spinner using `{colors.hairline}` for the track and `{colors.primary}` for the animated top segment.

**`divider`** — A 1px horizontal rule using `{colors.hairline-soft}` (#e6e5e6) for subtle section separation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), hamburger navigation replaces top nav, hero banner reduces to 280px min-height, product cards stack vertically, footer collapses to single column, search bar becomes full-width, filter chips wrap to multiple rows |
| Tablet | 744–1128px | Two-column product grid (2 col), top nav remains but with condensed link spacing, hero banner at 360px min-height, footer uses 2-column layout, search bar is 60% width, filter chips show in a horizontal scrollable strip |
| Desktop | 1128–1440px | Three-column product grid (3 col), full top nav with all links visible, hero banner at 400px min-height, footer uses 3-column layout, search bar is 40% width, filter chips in a static grid |
| Wide | > 1440px | Four-column product grid (4 col) with max-width container at 1440px, hero banner at 480px min-height with wider padding, footer uses 4-column layout, search bar is 30% width, all components use max-width centering |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets (title, price, image) are at least 48px tall
- Filter chips and pagination buttons are 36px minimum, but padded to exceed 44px tap area
- Social icons are 36px with 44px tap area via padding
- Quantity selector buttons are 40px x 40px

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer
- Product grid reduces columns from 4 to 1 as viewport narrows
- Footer columns collapse from 4 to 1, stacking vertically on mobile
- Filter sidebar (if present) collapses to a horizontal scrollable chip strip or a toggleable drawer below 744px
- Hero banner text size reduces from `{typography.display-xl}` (42px) to `{typography.display-md}` (28px) on mobile
- Search bar transitions from a centered, fixed-width element to a full-width bar on mobile
- Breadcrumb navigation truncates to show only the last two levels on mobile
- Accordion sections in product descriptions remain collapsed by default on all sizes

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components beyond primary/secondary buttons could not be reliably extracted; many may use subtle opacity or shadow changes not captured in the static CSS
- Error and validation styling for forms (error messages, success states, tooltips) was not observed on the live site
- Dark mode or high-contrast mode variants are not present in the extracted data
- Sub-brand or collection-specific palettes (e.g., "French Flax", "Linen Bedding") may exist but were not distinguishable from the global palette
- Animation durations, easing curves, and transition properties were not consistently extractable
- Focus ring styles (outline, box-shadow) for keyboard navigation are inferred from common patterns but not confirmed
- Dropdown menu styles (mega menu, sub-navigation) were not observed in the extracted markup
- Modal and overlay component styles (lightbox, quick-view, cart drawer) are not documented
- Star rating component styling and interaction states are unknown
- Quantity selector increment/decrement button hover and active states are inferred
- The exact font-weight for OchreRegular is assumed to be 400; the actual weight may vary
- Social icon colors for platforms other than Twitter/X (Instagram, Pinterest, Facebook) are not confirmed
- Sale badge positioning and animation (e.g., pulse, fade-in) are not documented
- The `object-fit: cover` declaration was found frequently on images but exact usage context is inferred
- Monospace font usage was detected but its specific application (code blocks, prices, etc.) is unclear
- The `serif` fallback in font stacks may indicate additional serif typefaces in use beyond OchreRegular
