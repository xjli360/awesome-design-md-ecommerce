---
version: alpha
name: "Revival Rugs"
source_url: "https://www.revivalrugs.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Revival Rugs is a brand that feels like a well-loved heirloom — intentional, warm, and grounded in craft. The palette is anchored by a deep, almost ink-like navy (`#1f3041`) that appears on primary buttons, navigation bars, and key typographic moments, lending a sense of quiet confidence. This is balanced by a rich, earthy terracotta (`#b04e2d`) that surfaces in secondary accents, badges, and hover states — a nod to the natural dyes and handwoven textures of the rugs themselves. The canvas is a soft, off-white parchment (`#fcfaf5`) that avoids the sterility of pure white, while a slightly warmer surface (`#ece8e0`) is used for cards and soft UI containers. Typography leans on a mix of Inconsolata for monospaced, editorial moments and P22UndergroundBook for body text, with P22UndergroundHeavy reserved for bold headlines and button labels. The brand's signature design moves include generous use of `{rounded.sm}` (8px) on buttons and cards, a consistent `{spacing.base}` (16px) grid, and a `{spacing.section}` (64px) rhythm that gives each product page room to breathe. The overall feeling is one of curated simplicity — nothing feels rushed or over-designed, and every color, corner, and spacing choice reinforces the idea of "better rugs, made with intention."

colors:
  primary: "#1f3041"
  primary-active: "#1e3042"
  primary-disabled: "#6a6c77"
  ink: "#1f3041"
  body: "#525252"
  muted: "#6b6d76"
  muted-soft: "#c7cace"
  hairline: "#dddddd"
  hairline-soft: "#ededed"
  canvas: "#fcfaf5"
  surface-soft: "#ece8e0"
  surface-card: "#e8e6db"
  on-primary: "#fcfaf5"
  accent-terracotta: "#b04e2d"
  accent-terracotta-light: "#b04f2d"
  accent-amber: "#994422"
  link-blue: "#007aff"

typography:
  display-xl:
    fontFamily: "'P22UndergroundHeavy', 'P22UndergroundBook', Inconsolata, monospace, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'P22UndergroundHeavy', 'P22UndergroundBook', Inconsolata, monospace, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'P22UndergroundBook', Inconsolata, monospace, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'P22UndergroundBook', Inconsolata, monospace, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'P22UndergroundBook', Inconsolata, monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'P22UndergroundBook', Inconsolata, monospace, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'P22UndergroundHeavy', 'P22UndergroundBook', Inconsolata, monospace, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'P22UndergroundBook', Inconsolata, monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'P22UndergroundBook', Inconsolata, monospace, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  badge:
    fontFamily: "'P22UndergroundHeavy', 'P22UndergroundBook', Inconsolata, monospace, sans-serif"
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
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-accent:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
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
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  link-inline:
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
  link-nav:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and key conversion points. Rendered in the deep navy (`#1f3041`) with white text and 8px rounded corners. On hover, shifts to `primary-active` (`#1e3042`). Disabled state uses `primary-disabled` (`#6a6c77`) with reduced opacity if needed. Text is set in P22UndergroundHeavy, uppercase, with 0.5px letter spacing for a deliberate, crafted feel.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Save for Later". Uses the same typography and sizing as primary but with a transparent background, navy text, and a 1px solid navy border. Hover state fills the background with a subtle tint of the primary color.

**`button-accent`** — A warm terracotta (`#b04e2d`) variant reserved for promotional CTAs, limited-time offers, or highlighting a special collection. Shares the same structural tokens as `button-primary` but swaps the background to the accent color.

**`button-tertiary-text`** — A text-only button for minimal interactions like "Cancel" or "Learn More". No background, no border, just the navy text in uppercase heavy weight. Hover adds a subtle underline or opacity shift.

### Cards
**`product-card`** — The core product display unit on collection pages and search results. Uses a warm off-white surface (`#e8e6db`) with 8px rounded corners. The product image sits at the top with matching rounded corners, followed by the rug name, size, and price in `body-sm`. A subtle shadow or border (`hairline`) separates the card from the canvas. On hover, the card may lift with a gentle box-shadow.

**`hero-banner`** — The full-width hero section on the homepage and landing pages. Background is the soft surface (`#ece8e0`), with the display headline in P22UndergroundHeavy at 48px. Padding is generous (`section` top/bottom, `base` sides) to allow the hero image to breathe. The hero may include a `button-primary` or `button-accent` CTA.

### Navigation
**`nav-bar`** — The top navigation bar, fixed at 72px height on desktop. Background is the canvas (`#fcfaf5`), with nav links in `nav-link` typography (P22UndergroundBook, 14px, 0.3px letter spacing). The logo sits on the left, links in the center, and utility icons (search, account, cart) on the right. On scroll, a subtle bottom border (`hairline`) appears.

**`link-nav`** — Standard navigation link styling. No background, no rounded corners, just the ink color and nav-link typography. Active state may use a bottom border or bolder weight.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and checkout forms. White background, 44px height, 8px rounded corners, and a 1px hairline border. On focus, the border transitions to the primary navy (`#1f3041`). Placeholder text uses `muted-soft` (`#c7cace`).

**`search-bar`** — A pill-shaped search input (`rounded.full`) used in the nav bar and mobile search. 48px height, white background, 1px hairline border, and body-md typography. The search icon is placed on the left, and a clear button appears on text entry.

### Badges
**`badge-new`** — A small terracotta badge (`#b04e2d`) used to flag new arrivals. 2px vertical padding, 8px horizontal, 4px rounded corners, and uppercase heavy typography at 11px.

**`badge-sale`** — An amber badge (`#994422`) for sale or markdown items. Same structural tokens as `badge-new` but with the amber background.

### Footer
**`footer`** — The site footer, a full-width block in the primary navy (`#1f3041`) with white text. Contains columns for customer service, about links, social icons, and a newsletter signup. Typography is `body-sm` for links and `caption` for headings. Padding is `xxl` (48px) top/bottom and `base` (16px) sides.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger nav, product cards stack vertically, hero text reduces to `display-md` (32px), footer collapses to stacked links |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, search bar collapses to icon-only, hero maintains two-column layout |
| Desktop | 1128–1440px | Full three-column product grid, expanded nav with all links, search bar visible, hero with side-by-side text and image |
| Wide | > 1440px | Max-width container (1440px) centered, product grid expands to four columns, hero uses larger imagery and wider text block |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Nav bar links have a minimum 48px tap target on mobile.
- Product card CTAs are at least 44px tall with 16px horizontal padding.
- Search bar is 48px tall for easy thumb access.
- Icon buttons (cart, account, search) are 44x44px minimum.

### Collapsing Strategy
- On mobile, the top nav collapses to a hamburger menu with a slide-out drawer.
- The product filter sidebar collapses to a bottom sheet or modal on mobile.
- The footer link columns stack vertically on mobile, with accordion-style expand/collapse for each section.
- The hero banner reduces from two-column to single-column, with the image stacking below the text.
- Product image galleries collapse from thumbnails to a single swipeable carousel.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons could not be reliably extracted — assumed to use a subtle background tint or opacity shift.
- Error styling for form inputs (border color, error message typography) was not observed on the live site.
- Dark mode or high-contrast theme tokens are not present in the extracted data.
- Sub-brand or collection-specific palettes (e.g., "Outdoor", "Vintage") may exist but were not captured.
- The exact font weights for P22UndergroundBook and P22UndergroundHeavy were inferred from naming conventions; actual `font-weight` values may vary.
- The `link-blue` (`#007aff`) was observed in the CSS but its exact usage context (inline links vs. legal links) is assumed.
- The `swiper-icons` font-family declaration suggests a third-party carousel library is in use, but its styling tokens are not included.
- The `SofiaProMedium` font-family was found in the CSS but appears to be a fallback or unused declaration; it is not included in the typography system.
