---
version: alpha
name: "4AD"
source_url: "https://www.4ad.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A label whose visual identity is built on a trinity of extracted hexes — #e0e1e1 (a cool, almost concrete gray), #343434 (a deep near-black ink), and #bbaf80 (a pale, dusty gold that reads as aged brass or dried wheat). The gold is the brand's true voltage: it appears sparingly — a single accent line, a hover state, a release-year numeral — and carries the entire weight of the label's mystique. The site uses a stark, almost brutalist grid: full-bleed hero images, no rounded corners except `{rounded.sm}` on shop buttons, and a typographic hierarchy that trusts `{typography.display-md}` at 24px in bold Georgia over the more common sans-serif hero. The nav is a single horizontal bar of `{typography.nav-link}` in Roboto Condensed, all-caps, tracking 1.2px, sitting on `{colors.canvas}` (#ffffff) with a `{colors.hairline}` (#d4d4d4) bottom border. The shop section feels like a gallery: product cards are `{colors.surface-card}` (#ffffff) with `{rounded.none}`, `{colors.ink}` (#343434) body text, and `{colors.muted}` (#8a8a8a) prices. The gold `{colors.primary}` (#bbaf80) only appears on the add-to-cart button and the "Buy" link — a deliberate withholding that makes the action feel significant. The footer is a dense block of `{colors.surface-soft}` (#f2f2f2) with `{typography.body-sm}` links in Roboto Condensed, no icons, no social proof — just text and a mailing-list signup. The overall mood is austere, literary, and slightly archival: the site of a label that has been releasing records since 1980 and doesn't need to shout.

colors:
  primary: "#bbaf80"
  primary-active: "#a3946a"
  primary-disabled: "#d6ceb0"
  ink: "#343434"
  body: "#4a4a4a"
  muted: "#8a8a8a"
  muted-soft: "#b0b0b0"
  hairline: "#d4d4d4"
  hairline-soft: "#e0e1e1"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#e0e1e1"
  gold-light: "#d6ceb0"
  gold-dark: "#a3946a"
  hero-overlay: "#000000"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto Condensed', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Roboto Condensed', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.7px
    textTransform: uppercase
  body-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto Condensed', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto Condensed', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Roboto Condensed', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto Condensed', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.7px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Roboto Condensed', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.6px
    textTransform: uppercase
  link:
    fontFamily: "'Roboto Condensed', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto Condensed', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 1.2px
    textTransform: uppercase
  hero-artist:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: -1px

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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-gold-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.primary}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 32px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 0 {spacing.base}
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: 0 {spacing.base}
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.hero-artist}"
    height: 480px
  hero-overlay:
    backgroundColor: "{colors.hero-overlay}"
    opacity: 0.4
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  search-input:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 36px
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  mailing-list-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  mailing-list-submit:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
  release-list-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  release-list-artist:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  release-list-title:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  release-list-year:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    typography: "{typography.body-sm}"
    textColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used exclusively for "Add to Cart" and "Buy Now" actions. Rendered in `{colors.primary}` (#bbaf80) with white text, `{rounded.sm}` corners, and `{typography.button-md}` (14px Roboto Condensed, uppercase, 0.7px tracking). On hover, shifts to `{colors.primary-active}` (#a3946a). Disabled state uses `{colors.primary-disabled}` (#d6ceb0). The gold is the only color that appears on buttons — no secondary fills, no gradients, no pill shapes.

**`button-secondary`** — Used for "View Details" or "Pre-Order" links. White background, `{colors.ink}` text, a 1px `{colors.hairline}` border. Same typography and height as primary. On hover, border shifts to `{colors.ink}`.

**`button-tertiary-text`** — A text-only link styled as a button, used for "Read More" or "Listen" actions. Transparent background, `{colors.ink}` text, no border. On hover, text color shifts to `{colors.primary}`.

**`button-gold-outline`** — An outlined variant for secondary purchase actions (e.g., "Buy on Bandcamp"). Transparent background, `{colors.primary}` text and 1px border. On hover, fills with `{colors.primary}` and white text.

### Navigation
**`top-nav`** — A 56px fixed header with white background and a 1px `{colors.hairline}` bottom border. Contains the 4AD wordmark (Georgia, bold, `{colors.ink}`) and nav links in `{typography.nav-link}` (13px Roboto Condensed, uppercase, 1.2px tracking). Active link uses `{colors.primary}`. No dropdowns, no mega-menus, no search icon in the nav — just text links.

**`nav-link`** — Inline text link with `{spacing.base}` horizontal padding. Hover state: text color shifts to `{colors.primary}`. No underline, no background change.

### Cards
**`product-card`** — A minimal, borderless card for shop items. White background, no rounded corners, `{rounded.none}`. Contains a full-width product image (no border-radius), the artist name in `{typography.title-sm}` (14px Roboto Condensed, uppercase, 0.7px tracking), the release title in `{typography.body-md}` (16px Georgia), and the price in `{typography.body-sm}` (14px Roboto Condensed, `{colors.muted}`). On hover, the image gets a subtle dark overlay and the price shifts to `{colors.primary}`.

**`product-card-badge`** — A small, non-rounded label for "New," "Exclusive," or "Sold Out." Uses `{colors.primary}` background, white text, `{typography.badge}` (11px Roboto Condensed, uppercase, 0.6px tracking). Positioned at the top-left of the product image.

### Hero
**`hero-section`** — A full-bleed, 480px-tall hero for featured artists or releases. Uses `{colors.ink}` as the background with a `{colors.hero-overlay}` scrim at 40% opacity over the background image. Artist name rendered in `{typography.hero-artist}` (48px Georgia, bold, -1px tracking) in white. No CTA button in the hero — just the name and a release date in `{typography.caption}`.

### Search
**`search-bar`** — A simple, non-rounded input field for the shop search. `{colors.surface-soft}` background, 1px `{colors.hairline}` border, `{typography.body-sm}`. No icon, no placeholder styling — just a clean text input. On focus, border shifts to `{colors.primary}`.

### Footer
**`footer-section`** — A dense, text-heavy footer on `{colors.surface-soft}` background. Contains mailing list signup, links to "Artists," "Releases," "Shop," "About," and "Contact." All links use `{typography.link}` (14px Roboto Condensed). The mailing list input uses `{colors.canvas}` background with a `{colors.hairline}` border, and the submit button uses `{colors.ink}` background with white text. No social media icons, no newsletter graphics — just text and a form.

### Release List
**`release-list-item`** — A single row in the chronological release archive. White background, `{spacing.md}` vertical padding, a 1px `{colors.hairline-soft}` bottom border. Contains artist name in `{typography.title-sm}`, release title in `{typography.body-md}`, and year in `{typography.caption}` (`{colors.muted}`). On hover, the entire row gets a `{colors.surface-soft}` background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger menu; hero height reduces to 280px; footer links stack vertically; release list removes year column |
| Tablet | 744–1128px | Two-column product grid; top-nav remains full but with reduced padding; hero height at 360px; footer uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links visible; hero at 480px; footer uses four-column layout |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero at 520px; footer uses four-column layout with increased padding |

### Touch Targets
- All buttons and links: minimum 44px height, 44px width for icon-only targets
- Nav links: 44px tap area (padding extends beyond text)
- Product card images: full-width tap target for navigation
- Search input: 44px height for comfortable tapping
- Mailing list submit: 44px height

### Collapsing Strategy
- Top nav: collapses to hamburger menu below 744px; menu opens as a full-screen overlay with `{colors.canvas}` background and `{colors.ink}` text
- Product grid: collapses from 4 columns to 1 column on mobile
- Footer: collapses from 4 columns to 1 column on mobile; links stack vertically with `{spacing.md}` between items
- Hero: reduces height by 40% on mobile; text scales down proportionally
- Release list: year column hidden on mobile; artist and title remain

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components could not be reliably extracted from static HTML/CSS; the above hover behaviors are inferred from common patterns and the brand's aesthetic
- Error states for forms (mailing list, search) are unknown — no validation styling was found
- Dark mode is not supported; the site uses a light-only palette
- Sub-brand or label-specific color variations (e.g., for different imprints) were not found
- The exact font weight for Georgia could not be confirmed; weights are inferred from common web usage (400 for body, 700 for display)
- The `{colors.hero-overlay}` hex (#000000) is an assumption — the actual overlay color and opacity could not be extracted
- Social media icon colors and styles are unknown; the footer uses text links only
- The mailing list form's success/error messaging styling is unknown
- Product card hover overlay color and opacity are inferred
- The exact spacing for the top-nav padding is estimated from common patterns
- No animation or transition durations were found in the extracted CSS
- The breadcrumb component's separator style is unknown
- Pagination active/hover states beyond color are unknown
