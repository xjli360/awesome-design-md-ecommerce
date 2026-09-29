---
version: alpha
name: "Jayson Home"
source_url: "https://www.jaysonhome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Jayson Home is a Chicago-born destination for considered living, where the mood is quietly sophisticated and the palette leans into deep, architectural neutrals. The brand's visual identity is anchored by a slate-like navy, `#272d3f`, which appears across primary buttons, navigation bars, and key interactive elements, lending a sense of grounded permanence. This is balanced by a warm, off-white canvas (`#f6f6f5`) and soft surfaces (`#f2f2f2`, `#ebeceb`), creating a backdrop that feels both refined and lived-in. The typographic voice pairs a classic, serifed Noe Display for editorial moments with the clean, utilitarian lines of Source Sans Pro and Helvetica for body and interface text, a combination that echoes the brand's mix of antique and modern. Signature design moves include generous use of soft rounding (`{rounded.sm}` on cards, `{rounded.md}` on buttons) that avoids the clinical feel of hard corners, and a restrained accent palette where a deep teal (`#088f87`) and a muted blue (`#1990c6`) appear sparingly—on sale badges, links, or hover states—to provide quiet moments of contrast. The overall effect is one of tactile warmth and understated luxury; the interface feels like a well-edited room, not a digital storefront.

colors:
  primary: "#272d3f"
  primary-active: "#22262e"
  primary-disabled: "#d9d9d9"
  ink: "#121212"
  body: "#333333"
  muted: "#767676"
  muted-soft: "#adadad"
  hairline: "#dddddd"
  hairline-soft: "#dedede"
  canvas: "#f6f6f5"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#088f87"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  badge-sale: "#088f87"
  star-rating: "#272d3f"
  link-default: "#1990c6"
  link-hover: "#136f99"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Noe Display', Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Noe Display', Georgia, 'Times New Roman', serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Noe Display', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Noe Display', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.15px
  body-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    rounded: "{rounded.md}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-teal}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-sm}"
    color: "{colors.accent-teal}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 480px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.hairline}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.lg} 0"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  category-tile-hover:
    backgroundColor: "{colors.hairline}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep navy (`{colors.primary}`) with white text. Uses a soft 8px rounding (`{rounded.md}`) and uppercase, semi-bold Source Sans Pro. On hover, it shifts to a slightly darker `{colors.primary-active}`. The disabled state fades to a light gray (`{colors.primary-disabled}`) with muted text, signaling non-interactivity without visual noise.
**`button-secondary`** — An outlined variant on a transparent or white canvas, with a 2px solid border in `{colors.primary}`. The active state fills the button with the primary color, inverting the text to white. Ideal for secondary actions like "Save for Later" or "View Details" alongside a primary button.
**`button-tertiary-text`** — A text-only button with no background or border, used for the least emphasized actions such as "Cancel" or "Clear Filters." The text color matches the primary navy and switches to `{colors.primary-active}` on hover.

### Cards
**`product-card`** — A clean, white card with no internal padding, relying on the product image and typography for structure. The image area uses `{rounded.sm}` on the top corners, while the bottom corners remain square to align with the text block. The title uses the semi-bold `{typography.title-sm}` in `{colors.ink}`, and the price is set in `{typography.body-sm}` in `{colors.body}`. Sale prices are rendered in the accent teal (`{colors.accent-teal}`) for immediate visual contrast.
**`category-tile`** — A soft, clickable tile with a light gray background (`{colors.surface-soft}`) that darkens to `{colors.hairline}` on hover. The category name is set in `{typography.title-md}`, creating a clear, scannable grid for browsing departments like "Lighting" or "Pillows."

### Navigation
**`nav-bar`** — A fixed-height, 72px top bar on a white canvas (`{colors.canvas}`). Navigation links are uppercase, semi-bold, and 14px (`{typography.nav-link}`), with the active link colored in the primary navy. On scroll, a subtle box shadow is added to create separation from the page content.
**`nav-link`** — Individual navigation items with generous 12px horizontal padding for easy tapping. The active state uses `{colors.primary}` to indicate the current section, while the default state is the deep `{colors.ink}`.

### Forms
**`text-input`** — A standard input field on the off-white canvas, with a 1px `{colors.hairline}` border and 4px rounding (`{rounded.sm}`). On focus, the border switches to the primary navy. The error state uses the accent teal border, a deliberate choice to maintain the brand's calm aesthetic even in error messaging.
**`search-bar`** — A pill-shaped input (`{rounded.full}`) with a 1px hairline border, designed to feel approachable and integrated into the header. On focus, the border adopts the primary navy, and the placeholder text is set in `{colors.muted}`.

### Badges & Tags
**`badge-sale`** — A small, uppercase badge with a teal background (`{colors.badge-sale}`) and white text, using tight 4px horizontal padding and 2px rounding. It sits in the top-left corner of product images to flag discounted items without overwhelming the visual.
**`badge-new`** — A similar badge but in the primary navy, used to denote new arrivals or exclusive collections.

### Footer
**`footer`** — A full-width, dark navy (`{colors.primary}`) footer with white text and links. The link color is white, with a hover state that lightens to `{colors.hairline}`. The section uses generous vertical padding (`{spacing.xxl}`) to create a comfortable, grounded end to the page.

### Hero
**`hero-banner`** — A large, 480px tall banner with a soft gray background (`{colors.surface-soft}`) and a dark overlay (`{colors.scrim}` at 30% opacity) to ensure text readability over background imagery. The headline uses the largest display type (`{typography.display-xl}`) in the brand's serifed Noe Display.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero height reduces to 320px; section padding reduces to 32px; filter chips stack vertically; footer links stack in a single column. |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but with reduced horizontal padding; hero height at 400px; filter chips wrap in a horizontal row; footer links in two columns. |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero at full 480px height; filter chips in a horizontal scrollable strip; footer links in four columns. |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero may feature full-bleed imagery; additional whitespace around sections. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Nav links on mobile have 48px tap areas to accommodate finger taps.
- Filter chips are 40px tall with 16px horizontal padding for easy selection.
- Product card images link to the product page with a minimum tap area of 120x120px.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu, with the logo and cart icon remaining visible.
- The product filter sidebar collapses into a horizontal scrollable chip strip or a modal overlay.
- The footer's multi-column link layout collapses into a single vertical list.
- Hero banners reduce in height and may crop imagery to focus on the central subject.
- Product grids reduce from 3-4 columns to 1-2 columns, with images scaling proportionally.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all interactive elements (buttons, links, cards) are inferred from the primary-active color and common patterns; exact CSS transitions and box-shadow values were not extracted.
- Error styling for form inputs (validation messages, error icons) was not observed; the error border color is an educated guess based on the accent palette.
- Dark mode or high-contrast mode styles are not present in the extracted data.
- Sub-brand or seasonal palette variations (e.g., holiday collections) are not captured.
- The exact font weights for Noe Display (e.g., 400, 500, 700) are inferred; only "700" was clearly observed.
- The `swiper-icons` font-family declaration suggests a carousel component, but its specific styling (arrow size, color, position) was not extracted.
- Loading states, skeleton screens, and spinner animations are not documented.
- The `#007aff` hex color appears in the extracted data but is likely a system default (iOS link blue) rather than a brand token; it has been omitted from the palette.
- Focus-visible styles (keyboard navigation outlines) are not captured.
- The exact `box-shadow` values for the scrolled nav bar and any card hover effects are missing.
