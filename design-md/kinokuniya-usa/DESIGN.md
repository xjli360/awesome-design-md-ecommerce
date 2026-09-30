---
version: alpha
name: "Kinokuniya USA"
source_url: "https://www.kinokuniya.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A bibliophile’s sanctuary where the page is the primary interface and the brand’s entire visual language defers to the printed object. The canvas is a cool, archival white (#ffffff) — not the warm cream of a cozy indie, but the clinical, respectful white of a gallery or a Japanese stationery shop. There is no extracted primary color from the live site, which is itself a design statement: Kinokuniya USA trusts the infinite color of book covers to provide the palette, and the UI steps back into a restrained system of hairline-thin borders (#e0e0e0), muted body text (#555555), and soft surface cards (#f8f8f8). The only deliberate brand voltage is the deep, ink-black (#111111) of the logo and navigation text — a nod to the weight of printed type. Buttons are minimal, secondary, and pill-shaped ({rounded.full}) with a transparent background and a subtle border, never competing with the product. The search bar is a full-width, pill-shaped field ({rounded.full}) with a magnifying-glass icon, inviting discovery without algorithmic aggression. The typography, though unextracted from the live site, is inferred to be a clean, readable sans-serif like Noto Sans JP or a system font stack — prioritizing legibility for multilingual book titles. The grid is generous and airy, with product cards using {rounded.sm} (4px) corners — a slight softening that prevents the white space from feeling sterile. The overall effect is that of a well-edited shelf: the brand’s personality is not in its chrome but in its restraint, allowing the thousands of book spines to be the true visual heroes.

colors:
  primary: "#111111"
  primary-active: "#333333"
  primary-disabled: "#999999"
  ink: "#111111"
  body: "#555555"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#cc0000"
  accent-gold: "#d4a017"

typography:
  display-xl:
    fontFamily: "'Noto Sans JP', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Noto Sans JP', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Noto Sans JP', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Noto Sans JP', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Noto Sans JP', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Noto Sans JP', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Noto Sans JP', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Noto Sans JP', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Noto Sans JP', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Noto Sans JP', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Noto Sans JP', 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 16px
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  category-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.body}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.primary}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-red}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-red}"
  dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
  radio:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  radio-checked:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action for checkout, add-to-cart, and sign-in flows. Uses a solid black fill (`{colors.primary}`) with white text and a full pill shape (`{rounded.full}`). On hover, the background shifts to `{colors.primary-active}` (#333333). The disabled state uses `{colors.primary-disabled}` (#999999) with white text, signaling an inactive action without visual noise. Padding is 12px vertical and 24px horizontal, giving it a compact but confident footprint.

**`button-secondary`** — The default button for less critical actions like "View Details" or "Cancel". It is an outlined pill with a white fill, black text, and a 1px hairline border (`{colors.hairline}`). On hover, the background becomes `{colors.surface-soft}` and the border shifts to `{colors.primary}`, creating a subtle elevation. This button never competes with the primary; it is the quiet, reliable alternative.

**`button-text`** — A text-only button with no background or border, used for inline actions like "Clear filters" or "See all". It uses `{typography.button-md}` in `{colors.primary}` and relies on the brand's restrained typographic hierarchy for its affordance. Padding is minimal (8px 16px) to keep it flush with surrounding content.

**`button-icon`** — A circular icon button (40px × 40px) for actions like search, cart, or menu toggles. It has no background by default, only a `{colors.body}` icon. On hover, a subtle `{colors.surface-soft}` background appears. This button is the most minimal interactive element in the system, deferring entirely to the icon's meaning.

### Navigation
**`top-nav`** — A fixed-height (64px) white bar with a soft bottom border (`{colors.hairline-soft}`). The logo sits on the left, navigation links in the center, and utility icons (search, account, cart) on the right. The nav uses `{typography.nav-link}` (14px, weight 600) for all text links, with active states underlined by a 2px black border. The cart icon includes a badge for item count, using `{colors.accent-red}`.

**`nav-link-active`** — The active navigation link is distinguished by a 2px solid bottom border in `{colors.primary}` and the text color shifts to `{colors.primary}`. This is the only place in the system where an underline is used as a state indicator, keeping the nav clean and uncluttered.

**`nav-link-inactive`** — Inactive links use `{colors.body}` (#555555) for text, maintaining readability without visual emphasis. There is no background or border, preserving the nav's minimal aesthetic.

**`category-strip`** — A horizontal scrollable strip of category pills, sitting just below the top nav. Each pill is either active (filled black) or inactive (soft gray fill). The strip itself has a white background and a soft bottom border. This component is the primary way users browse genres and departments.

**`category-tab-active`** — Active category pills are filled with `{colors.primary}` and white text, using `{typography.button-sm}` (12px, weight 600). The pill shape (`{rounded.full}`) and compact padding (6px 16px) make them feel like physical tags on a shelf.

**`category-tab-inactive`** — Inactive pills use a `{colors.surface-soft}` background with `{colors.body}` text. On hover, the background darkens slightly to `{colors.hairline}`. They are the same pill shape and size as the active state, ensuring consistent visual rhythm in the strip.

### Cards
**`product-card`** — The core product display unit, a white card with a 1px soft border (`{colors.hairline-soft}`) and 4px rounded corners (`{rounded.sm}`). Padding is 16px (`{spacing.base}`) on all sides. The card contains a 3:4 aspect ratio image placeholder, a title using `{typography.title-md}`, and a price using `{typography.body-md}`. On hover, the background shifts to `{colors.surface-soft}` and the border becomes `{colors.hairline}`, providing a gentle interactive cue without animation or shadow.

**`product-card-hover`** — The hover state of the product card. The background changes to `{colors.surface-soft}` (#f8f8f8) and the border to `{colors.hairline}` (#e0e0e0). This is the only visual change — no scale, no shadow, no color shift on text. The restraint is intentional: the book cover image is the hero, and the card frame should never distract.

**`product-card-badge`** — A small, red badge (`{colors.accent-red}`) with white uppercase text, used for "New", "Sale", or "Exclusive" labels. It sits in the top-left corner of the product card image, using `{typography.badge}` (11px, weight 700) and `{rounded.sm}` corners. The badge is compact (2px 8px padding) and high-contrast, the only spot of color on an otherwise monochrome card.

### Forms
**`text-input`** — A standard text input field for search, checkout forms, and account settings. It has a white background, 1px hairline border, `{rounded.sm}` corners, and 44px height. On focus, the border changes to `{colors.primary}` (#111111). Error states use a red border (`{colors.accent-red}`) and red text for the error message. The placeholder text uses `{colors.muted}` (#888888).

**`dropdown`** — A select dropdown styled identically to the text input: white background, hairline border, `{rounded.sm}` corners, and 44px height. The dropdown arrow is a custom icon in `{colors.muted}`. On focus, the border shifts to `{colors.primary}`.

**`checkbox`** — A 20px × 20px square checkbox with `{rounded.xs}` (2px) corners. Unchecked: white fill with a hairline border. Checked: black fill (`{colors.primary}`) with a white checkmark icon. The label uses `{typography.body-sm}` (14px) and sits 8px to the right.

**`radio`** — A 20px × 20px circular radio button. Unchecked: white fill with a hairline border. Checked: white fill with a black inner dot (8px diameter) and a `{colors.primary}` border. The label uses `{typography.body-sm}`.

### Footer
**`footer`** — A full-width footer with a `{colors.surface-soft}` background and a 1px top border (`{colors.hairline}`). It contains columns of links, social icons, and legal text. Padding is 48px (`{spacing.xxl}`) vertical and 64px (`{spacing.section}`) horizontal on desktop. Links use `{typography.link}` (14px, weight 400) in `{colors.body}`, with hover states shifting to `{colors.primary}`.

**`footer-link`** — Standard footer link using `{typography.link}` in `{colors.body}`. No underline by default. On hover, the text color changes to `{colors.primary}` and an underline appears, providing a clear interactive signal.

### Hero
**`hero-banner`** — A full-width hero section used on the homepage and category landing pages. It has a `{colors.surface-soft}` background, `{typography.display-xl}` (32px, weight 700) for the headline, and `{typography.body-md}` for the subtitle. Padding is 64px (`{spacing.section}`) vertical and 24px (`{spacing.lg}`) horizontal. The hero may contain a single `button-primary` for a call-to-action.

### Breadcrumbs
**`breadcrumb`** — A horizontal list of navigation links using `{typography.caption}` (12px) in `{colors.muted}` (#888888). The current page is rendered as plain text in `{colors.primary}`. Separators are a simple ">" character in `{colors.muted-soft}`. This component sits above the page title on product and category pages.

### Pagination
**`pagination-button`** — A numbered page button for search results and category listings. It is a 1px hairline-bordered square with `{rounded.sm}` corners, using `{typography.button-sm}` (12px, weight 600) in `{colors.body}`. The active page uses a black fill (`{colors.primary}`) with white text. Previous/Next arrows follow the same styling.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; category strip becomes a single-row scroll; product cards go to 2-column grid; footer stacks vertically; hero banner reduces padding to 32px vertical; search bar moves to a persistent bottom bar or hidden behind an icon. |
| Tablet | 744–1128px | Top nav shows limited links (Home, Books, Stationery, More); category strip is fully visible; product cards in 3-column grid; footer shows 2-column link layout; hero banner uses 48px vertical padding. |
| Desktop | 1128–1440px | Full top nav with all links; category strip is fully visible; product cards in 4-column grid; footer shows 4-column link layout; hero banner uses 64px vertical padding. |
| Wide | > 1440px | Content max-width of 1440px with auto margins; product cards in 5-column grid; hero banner may include a larger image or additional content block; footer remains 4-column but with increased horizontal padding. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target guidelines.
- Icon buttons are 40px × 40px, with a 44px tap area via padding or a transparent hit area.
- Category pills have 6px vertical padding, resulting in a ~24px height — acceptable for touch on mobile due to the horizontal scroll context, but ideally increased to 32px for better accessibility.
- Product cards have no minimum height, but the entire card is tappable, with a minimum tap area of 48px for the title/price region.

### Collapsing Strategy
- **Top navigation**: On mobile, all links collapse behind a hamburger menu icon. The logo and cart icon remain visible. The search icon becomes a toggle for an overlay search bar.
- **Category strip**: On mobile, the strip becomes a horizontally scrollable row with no visible scrollbar. The active category is always visible at the start of the scroll.
- **Product grid**: On mobile, the grid collapses from 4 columns to 2. On very small screens (< 480px), it may collapse to a single column.
- **Footer**: On mobile, the multi-column footer collapses into a single vertical stack with expandable sections (accordion pattern) to save vertical space.
- **Hero banner**: On mobile, the hero reduces padding and may hide the subtitle or secondary CTA to fit the viewport. The headline font size reduces to 24px.
- **Search bar**: On mobile, the persistent search bar collapses into an icon in the top nav. Tapping the icon opens a full-width overlay search bar with auto-focus.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No extracted primary color**: The live site did not yield a distinctive brand color from HTML/CSS extraction. The primary color (#111111) is inferred from the logo and navigation text, which is the most consistent visual element across pages. This may not match the brand's official color guidelines.
- **No font-family declarations found**: The typography block uses a best-guess font stack (Noto Sans JP, Noto Sans, system fonts) based on the brand's Japanese heritage and the need for multilingual support. The actual brand font may be different (e.g., a custom typeface or a different Google Font).
- **No hover/active/focus states extracted**: All interactive states (hover, active, focus) are inferred from common design patterns and may not match the live site's exact implementation.
- **No error or validation styling**: Error states for forms (text-input-error) are based on standard red-border patterns, not extracted from the live site.
- **No dark mode**: The design system assumes a light theme only. Dark mode colors and adjustments are not defined.
- **No animation or transition values**: Timing, easing, and duration for hover states, dropdowns, and page transitions are not specified.
- **No sub-brand or promotional palette**: Seasonal campaigns, special collections, or partnered promotions may introduce additional colors (e.g., holiday reds, limited-edition golds) that are not captured here.
- **No accessibility contrast ratios**: While the chosen colors (black on white, dark gray on white) likely pass WCAG AA, specific contrast ratios have not been verified.
- **No extracted spacing or rounded values**: The spacing and rounded tokens are based on common design system conventions (8px grid, standard border radii) and may not reflect the exact values used on the live site.
- **No extracted component dimensions**: Button heights, card padding, and nav heights are estimated from common e-commerce patterns and may differ from the live implementation.
- **No extracted icon set**: The design system assumes a standard icon library (e.g., Feather, Material Icons) but does not specify the exact icon set or custom icons used by the brand.
