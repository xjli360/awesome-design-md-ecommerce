---
version: alpha
name: "Orca Coolers"
source_url: "https://orcacoolers.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built on the tension between deep marine #3b4459 and a single, unflinching red #d02c2e — the kind of red you’d paint a rescue buoy or a fire extinguisher, not a marketing button. The canvas is #f4f4f4, a warm off-white that reads like weathered dock wood rather than sterile gallery white, and the entire system runs on Montserrat at modest weights, letting the product photography — ice-filled coolers on boat decks, tailgate spreads in golden hour light — carry the emotional weight. Signature moves include a gold accent #c6ad6f used sparingly on badge details and limited-edition hardware, a secondary green #108043 for “sustainable” or “BPA-free” callouts, and a caution-yellow #dd9a1a for warranty or safety tags. Every corner is either sharp ({rounded.none}) for structural elements like the nav bar and product grid, or generously pillowed ({rounded.full}) for CTAs and the search bar — there is no middle-radius compromise. The footer collapses into a dense, link-heavy stack on mobile, while the product card keeps its image-to-text ratio at roughly 3:1, with the red CTA floating at the bottom like a sealed latch.

colors:
  primary: "#d02c2e"
  primary-active: "#b01e20"
  primary-disabled: "#f0b0b1"
  ink: "#171717"
  body: "#3b4459"
  muted: "#6a7280"
  muted-soft: "#9ca3af"
  hairline: "#dedede"
  hairline-soft: "#e9eaea"
  canvas: "#f4f4f4"
  surface-soft: "#f2faf0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  gold-accent: "#c6ad6f"
  green-accent: "#108043"
  caution-yellow: "#dd9a1a"
  deep-marine: "#3b4459"
  dark-ink: "#121212"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: 2px solid "{colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: 2px solid "{colors.ink}"
  button-secondary-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: 2px solid "{colors.hairline}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: 2px solid "{colors.primary}"
  button-outline-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: 2px solid "{colors.primary}"
  button-gold-accent:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 2px solid "{colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 2px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid "{colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline}"
    boxShadow: 0 2px 8px rgba(0,0,0,0.08)
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    rounded: "{rounded.none}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    rounded: "{rounded.none}"
    borderBottom: 2px solid "{colors.primary}"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: 1px solid "{colors.hairline}"
  search-bar-pill-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: 2px solid "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0px
    border: 1px solid "{colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0px
    border: 1px solid "{colors.primary}"
    boxShadow: 0 4px 16px rgba(0,0,0,0.1)
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: 1/1
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: 12px 16px 4px
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: 0px 16px 12px
  product-card-badge:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  product-card-badge-green:
    backgroundColor: "{colors.green-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  product-card-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    margin: 12px 16px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 80px 24px
    minHeight: 400px
  hero-section-image:
    rounded: "{rounded.none}"
    objectFit: cover
  hero-section-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 16px 40px
    height: 56px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 24px 24px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
    padding: 4px 0px
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    padding: 0px 0px 8px
    textTransform: uppercase
  footer-divider:
    backgroundColor: "{colors.muted}"
    height: 1px
    margin: 24px 0px
  badge-limited:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.green-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  caution-tag:
    backgroundColor: "{colors.caution-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 16px 0px
    borderBottom: 1px solid "{colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0px 0px 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand’s signature red #d02c2e with white uppercase Montserrat text. The pill shape ({rounded.full}) and generous horizontal padding (32px) give it the visual weight of a sealed cooler latch. On hover, the background deepens to #b01e20 (`primary-active`); on disable, it fades to a muted pink #f0b0b1 (`primary-disabled`) with no border change. Used for “Add to Cart,” “Shop Now,” and primary checkout flows.

**`button-secondary`** — An outlined variant on the white canvas background (#f4f4f4) with a 2px solid ink (#171717) border and uppercase text. The active state fills the background with the hairline-soft gray (#e9eaea), while the disabled state drops the border to the hairline gray (#dedede) and text to muted-soft (#9ca3af). Used for “Learn More,” “View Details,” and secondary navigation actions.

**`button-outline`** — A transparent-background button with a red (#d02c2e) border and red text, active state fills with the primary red and flips text to white. Used for “Cancel” or “Remove” actions in cart and wishlist contexts, or as a secondary CTA on hero banners where the primary button is already red.

**`button-gold-accent`** — A smaller, gold-accent (#c6ad6f) pill button reserved for limited-edition drops, “Shop the Collection” CTAs on gold-trimmed products, and loyalty program sign-ups. Uses the smaller button-sm typography and 40px height to differentiate from the primary red system.

### Cards
**`product-card`** — A sharp-edged ({rounded.none}) white card with a soft hairline border (#e9eaea) that holds a square product image, title, price, and a floating red pill CTA. On hover, the border swaps to the primary red and a subtle box shadow lifts the card. The image has no rounding, reinforcing the brand’s preference for clean, structural lines. Badges (limited, sale, new, green-accent) sit in the top-left corner of the image area, using the gold, red, or green accent colors.

**`product-card-badge`** — Gold-accent (#c6ad6f) badge with dark ink text, used for “Limited Edition” or “Exclusive” tags. The green variant (`product-card-badge-green`) uses #108043 for “BPA-Free,” “Sustainable,” or “Eco-Friendly” callouts. The sale badge uses the primary red.

### Navigation
**`nav-bar`** — A 72px white bar with a 1px bottom hairline (#dedede). On scroll, it shrinks to 64px and gains a subtle drop shadow. Navigation links are uppercase Montserrat 600 at 14px with 0.5px letter spacing. The active link gets a 2px red bottom border; inactive links remain ink (#171717). The logo sits left-aligned, cart and account icons right-aligned.

**`nav-link`** — Individual navigation items with 8px vertical and 16px horizontal padding. No rounding, no background — the active state is indicated solely by the bottom border. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — A 48px tall input with a 1px hairline border (#dedede), 12px vertical and 16px horizontal padding, and 8px corner rounding ({rounded.sm}). On focus, the border thickens to 2px and turns primary red. Error state uses the same 2px red border with no additional icon — error messages appear below the input in caption typography.

**`search-bar-pill`** — A full-pill ({rounded.full}) search input at 48px height with a 1px hairline border. On focus, the border becomes 2px primary red. The pill shape is the only rounded element in the form system, visually separating search from other inputs.

### Footer
**`footer`** — A dark (#171717) footer with white text, organized into columns of links with uppercase captions as headings. Links are 14px Montserrat 500 with 4px vertical padding. A muted divider (#6a7280) separates the link columns from the bottom legal bar. On mobile, the columns stack vertically with accordion-style expandable sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes single-column; footer links stack vertically with accordion headers; hero section reduces to 300px min-height; buttons go full-width; search bar moves into nav overlay |
| Tablet | 744–1128px | Nav links remain visible but condensed; product grid shows 2 columns; hero section at 400px min-height; footer shows 2-column link layout; buttons maintain inline layout |
| Desktop | 1128–1440px | Full nav with all links; product grid shows 3 columns; hero section at 500px min-height; footer shows 4-column link layout; max-width container at 1280px |
| Wide | > 1440px | Same as desktop but with max-width container at 1440px; hero section can expand to 600px min-height; product grid shows 4 columns on category pages |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height and 44px width for touch targets
- Product card CTAs are at least 48px tall with 20px horizontal padding
- Nav hamburger icon is 48px x 48px
- Quantity selector buttons (+/-) are 44px x 44px
- Accordion headers have 48px minimum tap height

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px, with full-screen overlay containing all nav links, search bar, and account/cart links
- Product filters collapse into a “Filter” button that opens a slide-in panel from the left
- Footer link columns collapse into accordion sections on mobile, with the first column (Customer Service) expanded by default
- Product image gallery collapses from thumbnail strip to single-image swipe with dot indicators
- Related products section collapses from 4-column grid to 2-column grid on tablet, single column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components were inferred from common patterns; the live site may use different transitions or micro-interactions
- Error state styling for forms (beyond border color) could not be reliably extracted — iconography, helper text color, and animation are assumed
- Sub-brand or collection-specific palettes (e.g., “Orca X National Parks” or “Limited Edition Colors”) were not captured
- Dark mode is not supported on the current live site
- The gold-accent (#c6ad6f) and caution-yellow (#dd9a1a) usage frequency is low — these may be legacy or seasonal colors rather than core tokens
- The green-accent (#108043) may be a Shopify “sustainable” badge default rather than a brand color — verify against actual product badges
- The extracted hex list included #146ff8 (likely a Shopify Pay or social media icon color) and #fcf1cd (a stock-image dominant tone) — these were excluded from the palette
- Button loading/spinner states and disabled iconography were not observed
- The font-family list only showed Montserrat — there may be a secondary font for display or logo usage that wasn’t captured
- The meta theme-color was not set, so browser chrome color on mobile is unknown
- The extracted hex list had 13 colors, which is higher than typical for a single brand — some may be Shopify widget defaults or image-dominant tones rather than intentional brand colors
