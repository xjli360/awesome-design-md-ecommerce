---
version: alpha
name: "Stockfisch Records"
source_url: "https://www.stockfisch-records.de"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep black canvas (#080808) that feels less like a website and more like a listening room with the lights dimmed — the brand's entire visual system is built around the premise that the music, not the interface, should be the only thing you see. The four extracted grays (ink #4b4b4b, body #888888, muted #696969) form a restrained ladder that never competes with album artwork; text sits in Georgia and Times New Roman at modest sizes, evoking the typographic authority of a high-end audio magazine rather than a digital storefront. Navigation is a thin, almost invisible strip — no hero carousel, no promotional banners, just a sparse header with the label's logo and a handful of links. Product cards use `{rounded.none}` corners and `{spacing.base}` padding, as if to say the music inside needs no decorative frame. The primary action — adding an album to the cart — appears as a small, unassuming button in `{colors.primary}` (#080808) with white text, a deliberate anti-pattern in an ecommerce world of bright CTAs. The site reads as a direct translation of the label's physical catalog: black-and-white, precise, and utterly confident that the product (direct-to-disc audiophile recordings mastered by Pauler Acoustics) will speak for itself.

colors:
  primary: "#080808"
  primary-active: "#1a1a1a"
  primary-disabled: "#4b4b4b"
  ink: "#4b4b4b"
  body: "#888888"
  muted: "#696969"
  muted-soft: "#999999"
  hairline: "#4b4b4b"
  hairline-soft: "#696969"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#080808"
  link-hover: "#4b4b4b"
  error: "#cc0000"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'Times New Roman', Times, Georgia, serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Times New Roman', Times, Georgia, serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Arial', 'Helvetica', Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Arial Narrow', 'Arial', 'Helvetica', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Arial Narrow', 'Arial', 'Helvetica', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  link:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Arial Narrow', 'Arial', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Arial Narrow', 'Arial', 'Helvetica', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
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
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 32px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 7px 15px
    height: 32px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 36px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 0 16px
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 36px
    border: 1px solid "{colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 24px 16px
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    height: 32px
    border: 1px solid "{colors.hairline}"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: 12px 0
    border-bottom: 1px solid "{colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — A small, unassuming black rectangle (`{rounded.none}`) with white uppercase text in Arial Narrow. The button is deliberately understated — 32px tall with 8px 16px padding — so it never competes with album artwork. On hover, the background shifts to `{colors.primary-active}` (#1a1a1a). The disabled state uses `{colors.primary-disabled}` (#4b4b4b) with no border change. **`button-secondary`** — An outlined variant with a white background, black text, and a 1px black border. Same dimensions and typography as primary, used for "View Details" or "Learn More" actions where the primary action would be too heavy. **`button-tertiary-text`** — A text-only link styled as a button, used for "Cancel" or "Back to Catalog" actions. No background, no border, just the `{typography.button-md}` uppercase Arial Narrow in `{colors.primary}`.

### Navigation
**`nav-bar`** — A thin, 48px white strip at the top of every page. Navigation links use `{typography.nav-link}` — 12px uppercase Arial Narrow with 1.5px letter spacing — giving the header the density of a print magazine's table of contents. The active link is distinguished only by color (`{colors.primary}` vs `{colors.ink}`). No dropdowns, no mega-menus, no search bar in the header — the navigation is intentionally sparse. **`breadcrumb`** — A secondary navigation element in `{typography.caption}` (12px Arial) with `{colors.muted}` text. The active breadcrumb uses `{colors.primary}`. Separators are simple forward slashes with no additional spacing.

### Product Cards
**`product-card`** — A zero-radius white card with no shadow, no border, and no padding on the image. The album cover fills the full width of the card, and the title (`{typography.title-sm}`, 16px Georgia in `{colors.primary}`) sits directly below with `{spacing.sm}` gap. Price appears in `{typography.body-sm}` (13px Georgia, `{colors.muted}`). **`product-card-badge`** — A small black rectangle (`{rounded.none}`) with white uppercase text in 10px Arial Narrow, used for "NEW" or "SACD" format indicators. The badge sits in the top-left corner of the card image, overlapping the artwork.

### Forms
**`text-input`** — A 36px tall white input with a 1px `{colors.hairline}` border and `{rounded.none}`. On focus, the border switches to `{colors.primary}` (#080808). Placeholder text uses `{colors.muted-soft}` (#999999). **`search-bar`** — Identical to `text-input` in dimensions and styling, but used exclusively for the search function. No icon inside the input — search is triggered by pressing Enter. **`quantity-selector`** — A 32px tall input with a 1px `{colors.hairline}` border, used on the cart page for adjusting item quantities. The input is flanked by minus/plus buttons that are simple text characters in `{colors.primary}`.

### Footer
**`footer`** — A full-width black (`{colors.primary}`) band at the bottom of every page. Text is white in `{typography.body-sm}` (13px Georgia). Links use `{typography.link}` (14px Georgia) and are also white. The footer is divided into columns for "Shop", "About", "Contact", and "Newsletter" — the newsletter signup is a simple email input with a "Subscribe" button in `{colors.on-primary}` text on `{colors.primary-active}` background. No social media icons, no payment method logos — just text links and the label's address.

### Cart
**`cart-item`** — A single row in the cart, with the album cover thumbnail, title, format (e.g., "SACD", "Vinyl"), price, quantity selector, and remove link. Each item is separated by a 1px `{colors.hairline-soft}` border. The remove link uses `{typography.link}` in `{colors.muted}` — no red "Remove" button, just an understated text link.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row). Navigation collapses to hamburger menu. Footer stacks vertically. Search bar moves to top of page. |
| Tablet | 744–1128px | Two-column product grid. Navigation remains horizontal but with reduced padding. Footer displays in two columns. |
| Desktop | 1128–1440px | Three-column product grid. Full navigation with all links visible. Footer in four columns. |
| Wide | > 1440px | Four-column product grid. Maximum content width of 1440px with centered layout. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 32px and minimum width of 44px for touch targets.
- Navigation links have 48px touch targets (full height of the nav bar).
- Quantity selector buttons (minus/plus) are 32px × 32px.
- Product card images are tappable and link to the product detail page.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu. The menu overlay is full-screen with a white background and black text.
- The product grid collapses from 3–4 columns on desktop to 2 columns on tablet and 1 column on mobile.
- The footer collapses from 4 columns on desktop to 2 columns on tablet and 1 column on mobile.
- The search bar, which is hidden on desktop (accessible via a small icon), becomes a persistent full-width element on mobile.
- Breadcrumbs are hidden on mobile to save space; only the current page title is shown.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site. The `button-primary-active` and `text-input-focus` tokens are best guesses based on common patterns.
- Error styling (form validation, empty cart, 404 page) is not present in the extracted data. The `error` color (#cc0000) is a standard web convention, not a brand-specific value.
- The brand's sub-palette for different product formats (SACD, Vinyl, CD, Digital Download) could not be determined. The `product-card-badge` component uses the primary black, but the site may use color-coded badges.
- Dark mode is not supported. The site uses a white canvas with black text exclusively.
- The extracted font list includes "Comic Sans MS" and "cursive" — these are almost certainly fallback declarations in the site's CSS stack, not intentional brand fonts. The primary serif stack (Georgia, Times New Roman) and sans-serif stack (Arial Narrow, Arial, Helvetica) are the brand's actual choices.
- The extracted hex colors (#080808, #4b4b4b, #888888, #696969) are all grays — no accent color was found. This is consistent with the brand's minimalist, monochrome aesthetic, but it means there is no secondary or tertiary color in the system. The `error` and `success` colors are standard web defaults, not brand-specific.
- The site's use of `{rounded.none}` for all components is intentional and consistent — no rounded corners were found anywhere in the extracted CSS.
- The `button-primary` height of 32px is unusually small for ecommerce; this was confirmed by the extracted CSS and is a deliberate design choice to keep the interface unobtrusive.
