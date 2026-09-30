---
version: alpha
name: "Kobo Audiobooks"
source_url: "https://www.kobo.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep red anchor (#bf0000) cuts across a predominantly white and serif-heavy reading experience, marking every primary action — the “Buy Now” button on a book detail page, the progress bar in the reading interface, the active tab in the navigation. This is a brand built for long-form reading, not quick scanning: body copy runs Georgia at 16px with generous leading (1.6), and display headings use Trebuchet MS at 24–32px in weight 600, a choice that reads as earnest and slightly academic rather than trendy. The top navigation is a clean horizontal bar with dropdown menus for “Books”, “eReaders”, “Audiobooks”, and “Blog”, each link set in Trebuchet MS at 14px weight 400 with 12px padding — no pill shapes, no rounded search bars, no decorative icons. Product cards in the grid use a simple white background with a soft shadow, a cover image, and title/author in Georgia body-sm (14px), with the price and a “Add to Cart” button in the brand red. The overall mood is that of a serious bookstore — the red is the only color that breaks the monochrome, and it does so with the confidence of a university press logo. Buttons are rectangular with 4px rounding (`{rounded.xs}`), not pill-shaped; the search bar is a simple input field with a magnifying-glass icon, not a floating orb. The system trusts typography and whitespace over illustration or photography — there are no hero images, no lifestyle shots, only book covers and text.

colors:
  primary: "#bf0000"
  primary-active: "#a00000"
  primary-disabled: "#f2b3b3"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#bf0000"
  link-hover: "#a00000"
  star-rating: "#f5a623"
  badge-new: "#bf0000"
  badge-sale: "#bf0000"

typography:
  display-xl:
    fontFamily: "'Trebuchet MS', Trebuchet, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Trebuchet MS', Trebuchet, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Trebuchet MS', Trebuchet, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Trebuchet MS', Trebuchet, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Trebuchet MS', Trebuchet, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  body-lg:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Trebuchet MS', Trebuchet, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "'Trebuchet MS', Trebuchet, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  link:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "'Trebuchet MS', Trebuchet, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  badge:
    fontFamily: "'Trebuchet MS', Trebuchet, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.xs}"
    padding: 8px 0
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  product-card-author:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-card-price:
    typography: "{typography.button-md}"
    color: "{colors.ink}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
    rounded: "{rounded.full}"
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  tab-active:
    color: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    color: "{colors.muted}"
    typography: "{typography.nav-link}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for “Add to Cart”, “Buy Now”, and “Subscribe”. A solid red rectangle with 4px rounding (`{rounded.xs}`) and white text in Trebuchet MS weight 600 at 15px. On hover, the background shifts to `{colors.primary-active}` (#a00000). The disabled state uses `{colors.primary-disabled}` (#f2b3b3) — a pale pinkish-red that still reads as the brand but signals inactivity. Height is 40px, padding 10px 20px.

**`button-secondary`** — A white button with a 1px hairline border (`{colors.hairline}`) and dark text. Used for “Learn More”, “View Details”, and secondary checkout actions. On hover, the background fills with `{colors.surface-soft}` (#f5f5f5). Same 40px height and 4px rounding as the primary, maintaining a consistent button system.

**`button-tertiary-text`** — A text-only link styled as a button, used for “Cancel”, “Remove”, and “Back to Search”. No background, no border, red text (`{colors.primary}`) in Trebuchet MS weight 600. On hover, the text shifts to `{colors.primary-active}`.

### Text Inputs
**`text-input`** — The standard input field for search, login, and checkout forms. White background, 1px hairline border, Georgia body text at 16px, 4px rounding. On focus, the border becomes a 2px solid red (`{colors.primary}`). On error, the same red border appears — the brand uses its single accent color for both focus and error states, relying on helper text to disambiguate. Height 40px, padding 10px 12px.

### Navigation
**`nav-bar`** — A fixed top bar at 56px height, white background with a soft bottom border (`{colors.hairline-soft}`). Contains the Kobo logo (left), a horizontal list of nav links (Books, eReaders, Audiobooks, Blog), a search icon, and a user account dropdown. Nav links are Trebuchet MS at 14px weight 400 with 12px padding. The active page is indicated by a 2px red underline (`{colors.primary}`). Dropdown menus (`{nav-dropdown}`) are white with 4px rounding and 8px vertical padding.

**`breadcrumb`** — A simple text-only breadcrumb trail in caption size (13px Arial) with muted gray color. The current page is rendered in `{colors.ink}`. No arrows or separators — just spaces and the active state.

### Cards
**`product-card`** — A white card with 4px rounding and 12px padding, containing a book cover image (full width), the title in `{title-md}` (18px Trebuchet MS weight 600), the author in `{body-sm}` (14px Georgia, muted gray), and the price in `{button-md}` (15px Trebuchet MS weight 600, ink color). On hover, a subtle box shadow appears (`0 2px 8px rgba(0,0,0,0.08)`). No border, no background color — the card relies on the white canvas and the shadow to lift off the page.

### Badges
**`badge`** — A small uppercase label used for “NEW”, “SALE”, and “BESTSELLER”. Red background (`{colors.primary}`), white text, 11px Trebuchet MS weight 700 with 0.5px letter spacing, 4px rounding, 2px 6px padding. Always positioned at the top-left corner of the product card image.

### Progress Bar
**`progress-bar`** — Used in the reading interface to show book completion. A 4px tall, fully rounded (`{rounded.full}`) track in `{colors.hairline-soft}` with a red fill (`{colors.primary}`) of the same height and rounding. No text, no percentage label — just a visual indicator.

### Tabs
**`tab-active`** — The selected tab in a horizontal tab strip (e.g., “Books”, “Audiobooks”, “eBooks”). Red text (`{colors.primary}`) with a 2px red underline. Nav-link typography (14px Trebuchet MS weight 400). Inactive tabs use `{colors.muted}` with no underline.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; search bar moves to top of page; breadcrumbs hidden; footer links stack vertically |
| Tablet | 744–1128px | Nav bar shows 3–4 links; product cards in 2-column grid; search bar in nav; breadcrumbs visible; footer in 2 columns |
| Desktop | 1128–1440px | Full nav bar with all links; product cards in 3–4 column grid; search bar in nav; breadcrumbs visible; footer in 4 columns |
| Wide | > 1440px | Max-width container at 1440px; product cards in 5-column grid; all other elements remain same as desktop |

### Touch Targets
- All buttons and links: minimum 44px height, 44px width (icon-only)
- Search bar: 40px height, full width on mobile
- Nav hamburger icon: 44px x 44px tap area
- Product card: entire card is tappable, minimum 120px height
- Rating stars: 24px per star, 44px total tap area for the row

### Collapsing Strategy
- Nav links collapse to hamburger menu at < 744px
- Breadcrumbs hidden at < 744px
- Footer columns collapse from 4 to 2 to 1 as viewport shrinks
- Product card grid collapses from 5 to 4 to 3 to 2 to 1 columns
- Search bar moves from nav bar to a full-width row below the nav on mobile
- Category filter strip (if present) collapses to a horizontal scrollable row on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#bf0000) was extracted from the live site — the rest of the palette (ink, body, muted, hairline, canvas, etc.) is inferred from common web patterns and may not match the exact brand values. A full design audit is needed to confirm grays, whites, and secondary accents.
- No font-family declarations beyond the system fallbacks (Arial, Georgia, Helvetica, Trebuchet MS, Verdana, serif, sans-serif) were found. Kobo likely uses a custom font (possibly a web font like “Kobo” or a licensed serif), but it was not extractable from the HTML. The typography block uses Trebuchet MS and Georgia as the closest available matches.
- Hover, focus, active, and disabled states for all components are assumed based on common patterns — the live site may use different colors, durations, or effects.
- Error styling for forms (border color, error message typography, icon placement) could not be extracted.
- Dark mode: not detected on the live site; no dark-mode palette is defined.
- Sub-brand palettes (Kobo Plus, Kobo eReaders, Kobo Audiobooks) may exist but were not extractable.
- The star-rating color (#f5a623) is a common yellow and may not be the brand’s actual rating color — a visual check is needed.
- Spacing and sizing values (padding, height, font sizes) are estimated from common e-commerce patterns and may not match the exact Kobo implementation.
