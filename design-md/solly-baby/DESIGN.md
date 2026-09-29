---
version: alpha
name: "Solly Baby"
source_url: "https://sollybaby.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A soft, grounded brand for new parents, built on a warm neutral canvas of #e9e5df and #f8f6f3, with a signature teal #108474 as the primary voltage — a color that reads as calm, organic, and trustworthy rather than clinical or urgent. The palette is deliberately muted: #23221e ink for body text, #4d403c and #40362e for secondary tones, and a range of warm grays (#eeeeee, #f2f2f2, #f9fafb) that keep the interface feeling gentle and uncluttered. Type runs DM Sans and Nunito Sans at moderate weights — display sizes hover around 20-24px in weight 500-600, never shouting, letting the product photography and soft {rounded.lg} card corners do the emotional work. Buttons use {rounded.full} pill shapes in the teal primary, with a secondary palette that includes a muted lavender #a89cc8 and a pale sage #c1e6e6 for badges and accent elements. The brand avoids hard edges: every component from the hero section to the product card uses {rounded.md} or larger, and the generous whitespace (section padding at 64px) gives the interface room to breathe. A single marigold accent #fbcd0a appears sparingly — likely for sale badges or promotional flags — adding a small jolt of warmth without breaking the calm. The overall effect is a digital space that feels like a well-loved nursery: soft, safe, and designed for the exhausted, tender state of early parenthood.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d5cc"
  ink: "#23221e"
  body: "#4d403c"
  muted: "#555555"
  muted-soft: "#7b7b7b"
  hairline: "#dbdbdb"
  hairline-soft: "#e9e9e9"
  canvas: "#e9e5df"
  surface-soft: "#f8f6f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-lavender: "#a89cc8"
  accent-sage: "#c1e6e6"
  accent-marigold: "#fbcd0a"
  warm-brown: "#40362e"
  warm-brown-light: "#4c4a41"
  dark-warm: "#261a16"
  sand: "#d3c3a8"
  sand-light: "#ac9f8b"
  off-white: "#f4f1ea"

typography:
  display-xl:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px

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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-field:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-field-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0px
  product-card-photo:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
    aspectRatio: "3/4"
  product-card-info:
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.surface-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.surface-card}"
    typography: "{typography.title-sm}"
  badge-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-lavender:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid #c13515"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  accordion-body:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a full-pill in the brand's teal #108474. Uses DM Sans at 15px weight 600 with 0.3px letter spacing for a slightly elevated, intentional feel. On hover, shifts to #0d6b5d; disabled state uses #a3d5cc with white text. Padding of 14px 28px and 48px height keeps it substantial but not heavy.

**`button-secondary`** — A outlined pill variant on the warm canvas background, using the ink #23221e for text and a 1px hairline border. Active state fills the border to solid ink. Used for "Learn More" or secondary actions where the teal primary would compete.

**`button-tertiary-text`** — A text-only button in the primary teal, used for links like "View All" or "Read More" within card contexts. No background, no border — just the color and typography doing the work.

**`button-pill-primary`** — A smaller, compact pill (10px 20px padding) used for filter tags, category chips, and quick-action buttons. Same teal fill, smaller type at 13px.

**`button-pill-outline`** — The outlined counterpart to the pill primary, used for inactive filter states or secondary quick actions. Transparent background with a hairline border.

### Cards
**`product-card`** — The core product display unit, a white card with {rounded.lg} corners and no internal padding (padding lives on child elements). The photo area uses a 3:4 aspect ratio with rounded top corners only, creating a clean break between image and info. The info section gets 16px horizontal and 24px bottom padding. Title uses title-sm at 16px weight 600, price uses body-md in the primary teal. A marigold badge overlays the photo for sale items.

**`product-card-badge`** — Small uppercase label in 11px weight 700 with 0.5px letter spacing, set on a marigold #fbcd0a background with dark ink text. Used for "SALE" or "BESTSELLER" flags. Rounded xs (4px) with tight 2px 8px padding.

**`badge-new`** — Same structure as the sale badge but on the sage #c1e6e6 background. Used for "NEW" or "JUST ARRIVED" flags.

**`badge-lavender`** — Same structure on the lavender #a89cc8 background with white text. Used for "LIMITED EDITION" or exclusive collection flags.

### Navigation
**`top-nav`** — A 72px tall bar on the warm canvas background, containing the logo, nav links in DM Sans 14px weight 500, and utility icons (search, account, cart). Active nav links get a 2px teal bottom border. The nav uses generous horizontal spacing (24px between items) and collapses to a hamburger menu on mobile.

**`nav-link-active`** — Active state with the teal underline indicator. The link itself remains in the dark ink color.

**`nav-link-inactive`** — Inactive state in the muted #555555, with hover transitioning to ink.

### Forms
**`text-input`** — Standard text input with white background, 48px height, 12px 16px padding, and {rounded.md} corners. Border is 1px hairline #dbdbdb. Focus state swaps to a 2px teal border. Error state uses a red border (#c13515) — this is an inferred error color as the exact error styling wasn't extractable.

**`search-bar-pill`** — A full-pill search input used in the hero or sticky header, 48px tall with 12px 20px padding. White background with hairline border. The pill shape distinguishes it from standard form inputs and aligns with the brand's soft aesthetic.

**`select-input`** — Matches the text input structure but with a dropdown indicator. Used for size selectors and filter dropdowns.

### Accordion
**`accordion`** — Collapsible sections used for product descriptions, care instructions, and FAQ content. White card with {rounded.md} corners, 16px padding, and a hairline border. Header uses title-sm (16px weight 600), body uses body-sm (14px weight 400) in the warm brown #4d403c. Body content gets 8px top padding to separate from the header.

### Footer
**`footer`** — A dark section on the ink #23221e background with white text. Contains link columns, social icons, and newsletter signup. Links use the surface-soft #f8f6f3 for readability. Section padding is 48px top and bottom with 24px horizontal. Headings use title-sm in white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; product cards stack vertically; hero text reduces to 22px; section padding drops to 32px; search bar moves to sticky header; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (logo, shop, search, cart); hero maintains 24px display text; section padding at 48px; footer uses 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; three-column product grid; hero at 28px display; standard section padding at 64px; footer uses 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid can expand to 4 columns; hero maintains scale with increased whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons use 40px circles (exceeds 44px tap target guideline)
- Product card CTA buttons are 48px tall
- Search bar is 48px tall on all breakpoints
- Nav links have 44px minimum touch area even when text is smaller

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with a slide-out drawer for navigation links
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport shrinks
- Footer columns collapse from 4 to 2 to 1
- Hero section reduces padding and font size on mobile to prevent overflow
- Accordion sections remain single-column on all breakpoints
- Search bar becomes sticky at the top on mobile for persistent access

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Exact hover colors for secondary buttons, text inputs, and links could not be extracted from static CSS. The primary hover (#0d6b5d) is inferred from common darkening patterns. Secondary button hover (border to ink) is an educated guess based on common e-commerce patterns.
- **Error states**: The error color (#c13515) is inferred from common Shopify error patterns. Exact error text, border, and background colors for form validation are not confirmed from the extracted data.
- **Focus states**: Focus ring colors and widths for keyboard navigation are not extractable from static CSS. A 2px teal (#108474) focus ring is assumed based on the primary color.
- **Dark mode**: No dark mode implementation was detected. The brand likely uses light mode exclusively given the warm canvas aesthetic.
- **Sub-brand or seasonal palettes**: The extracted colors include a lavender (#a89cc8) and sage (#c1e6e6) that may belong to seasonal collections or sub-brands rather than the core system. Their exact usage context is unconfirmed.
- **Typography scale**: Font sizes and weights are estimated from common DM Sans and Nunito Sans usage patterns. Exact responsive typography scale (mobile vs desktop sizes) could not be extracted.
- **Spacing scale**: The spacing tokens are based on common 4px/8px grid systems. Exact component-specific spacing (e.g., card padding, section margins) may vary on the live site.
- **Animation/transition**: No transition durations or easing curves were extractable. A default 200ms ease-in-out is assumed for hover/focus states.
- **Checkout components**: Shopify checkout uses its own design system (Shopify Checkout UI) which may override brand styles. The extracted colors may include checkout-specific elements.
- **Review widget**: Judge.me review widget colors (JudgemeIcons, JudgemeStar) appear in the font declarations but their exact styling is not part of the brand's core design system.
- **Marigold accent usage**: The #fbcd0a appears only once in the extracted colors. It may be used for sale badges, promotional banners, or limited-time flags — but its exact role in the system is unconfirmed.
