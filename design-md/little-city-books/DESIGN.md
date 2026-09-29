---
version: alpha
name: "Little City Books"
source_url: "https://www.littlecitybooks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy #003399 and a teal #006b6d form the two-pole voltage of this independent bookstore — the blue carries the primary CTAs and the teal surfaces as a secondary accent on badges and hover states, while a warm off-white #eeeeee canvas keeps the reading experience clean. The typography stack relies on Font Awesome for iconography but the brand’s voice is carried by a restrained body set in #383333, a soft charcoal that reads warmer than pure black, against #232323 for headings. The site uses a generous 48px section spacing and 32px xl padding between content blocks, giving each book cover room to breathe. A distinctive design move: the search bar sits as a full-width pill (#006b6d background, white text) rather than a collapsed icon, signaling that discovery is the primary action — not browsing categories. The footer repeats the navy #003399 as a full-bleed band, with #555555 muted links and #eeeeee text, creating a bookish, grounded feel that prioritizes legibility over decoration. There are no hard corners on interactive elements — buttons and inputs use {rounded.sm} 8px, while the search pill uses {rounded.full} — but the product cards and content panels stay at {rounded.none} to preserve a clean, editorial grid.

colors:
  primary: "#003399"
  primary-active: "#002266"
  primary-disabled: "#b3c6e6"
  ink: "#232323"
  body: "#383333"
  muted: "#555555"
  muted-soft: "#777777"
  hairline: "#cccccc"
  hairline-soft: "#dddddd"
  canvas: "#eeeeee"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#006b6d"
  accent-teal-active: "#004c4e"
  accent-teal-disabled: "#b3d4d4"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0

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
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.accent-teal-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
  button-secondary-disabled:
    backgroundColor: "{colors.accent-teal-disabled}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  text-input-error:
    borderColor: "#cc0000"
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-accent}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  search-bar-pill-placeholder:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-accent}"
    opacity: 0.7
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "#cc0000"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
    textDecoration: underline
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  section-header:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in deep navy #003399 with white text and 8px rounded corners. On hover, it shifts to #002266; when disabled, it fades to #b3c6e6. Used for "Add to Cart", "Checkout", and "Subscribe" actions. Height is 44px with 12px 24px padding.

**`button-secondary`** — The secondary action button in teal #006b6d, used for "Browse Events", "View Details", and "Learn More" links. Active state shifts to #004c4e; disabled fades to #b3d4d4. Same dimensions and rounded corners as primary.

**`button-tertiary`** — A ghost button on the off-white #eeeeee canvas, with #232323 text. On hover, the background shifts to #f5f5f5. Used for "Cancel", "Back to Browsing", and dismiss actions.

### Navigation
**`nav-bar`** — A 64px fixed-height bar on the #eeeeee canvas, with #232323 nav links. The logo sits left-aligned, with primary navigation links centered and a search icon right-aligned. Active links shift to #003399.

**`nav-link`** — Inline text links at 15px weight 500. Active state uses the primary navy; hover adds a subtle underline.

### Search
**`search-bar-pill`** — A full-width pill-shaped search bar in teal #006b6d with white text, using {rounded.full}. The placeholder text is white at 70% opacity. This is the most distinctive component — it sits prominently at the top of the page, signaling that book discovery is the primary action. Height is 48px with 12px 24px padding.

### Cards
**`product-card`** — A white #ffffff card with no rounded corners, containing a book cover image, title, author, and price. On hover, a subtle box-shadow lifts the card. The image area has no rounding, keeping the editorial grid clean.

### Badges
**`badge-new`** — A teal #006b6d badge with uppercase white text at 11px weight 700, using 4px rounded corners and 2px 8px padding. Used for "New Arrival" flags.

**`badge-sale`** — A red #cc0000 badge with white uppercase text, same dimensions as the new badge. Used for "Sale" or "Discount" flags.

**`badge-category`** — A pill-shaped badge in #f5f5f5 with #555555 text, using {rounded.full} and 4px 12px padding. Used for genre tags like "Fiction", "Nonfiction", "Mystery".

### Footer
**`footer`** — A full-bleed navy #003399 band with white text, using 48px vertical padding and 32px horizontal padding. Links are white with underline on hover. The footer contains the store address, hours, newsletter signup, and social links.

### Hero
**`hero-section`** — A full-width section on the #eeeeee canvas with 64px vertical padding and 32px horizontal padding. Contains a headline in display-lg, a subtitle in body-md, and a primary CTA button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; search bar reduces to icon-only pill; product cards stack single-column; hero padding reduces to 32px vertical; footer stacks vertically |
| Tablet | 744–1128px | Nav shows text links; search bar remains full-width but shorter; product cards in 2-column grid; hero padding at 48px vertical |
| Desktop | 1128–1440px | Full nav with all links; search bar at full width; product cards in 3-column grid; hero at 64px vertical padding |
| Wide | > 1440px | Max-width container at 1440px centered; search bar constrained to 800px max-width; product cards in 4-column grid |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links minimum 44px tap area (even if text is smaller)
- Search bar pill minimum 48px height for easy tapping
- Badges minimum 24px height for legibility
- Product card tap area covers entire card

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px
- Search bar collapses to icon-only pill on mobile, expanding to full-width on tap
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer links stack vertically on mobile, horizontal on tablet and above
- Hero section reduces vertical padding by 50% on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for all components were inferred from common patterns; the live site may use different transitions or color shifts
- Error styling for text inputs (border color #cc0000) is an assumption — the actual error color could not be extracted
- Font family declarations only returned Font Awesome variants; the serif and sans-serif stacks (Georgia, Helvetica Neue) are educated guesses based on common bookstore site patterns and the extracted body color
- No dark mode styles were detected; the brand may not support dark mode
- Sub-brand or seasonal color palettes (if any) could not be extracted
- The exact border widths and box-shadow values for product cards are estimated — the live site may use different values
- No extracted data for loading states, skeleton screens, or animation timing
- The meta theme-color was absent, suggesting the brand may not have configured browser chrome color
- No extracted data for form validation states beyond error border color
