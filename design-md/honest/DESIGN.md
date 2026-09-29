---
version: alpha
name: "Honest"
source_url: "https://honest.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A sage-warm palette anchored on #bad0c9 — a muted celadon that reads as clean without clinical white, found across backgrounds, badges, and product imagery — paired with a cream canvas of #fff6ee that softens every edge. The brand's secondary voltage comes from #899df1, a periwinkle accent used sparingly on interactive elements and illustrations, while #f2b136 adds a marigold pop for sale tags and promotional badges. Typography runs Assistant at moderate weights (300–600) with neue-haas-grotesk-display for display headlines, creating a gentle contrast between rounded geometric headlines and the airy, humanist body copy. Product cards use generous whitespace and {rounded.md} corners, with CTAs rendered in the sage primary on cream backgrounds — never aggressive, always inviting. The checkout flow carries Shopify's default widget colors (#1795a7 teal, #b76d7b rose) which sit slightly outside the brand palette, suggesting a pragmatic platform integration rather than a curated design choice. Navigation is minimal: a sticky top bar with the Honest wordmark, search icon, and account/cart links, all in #201f1d ink on the cream canvas. The overall feeling is that of a well-edited nursery — soft, safe, and deliberately un-loud.

colors:
  primary: "#bad0c9"
  primary-active: "#a3bfb7"
  primary-disabled: "#d4e3de"
  ink: "#201f1d"
  body: "#3a3a38"
  muted: "#6b6b69"
  muted-soft: "#9a9a98"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#fff6ee"
  surface-soft: "#f3e6db"
  surface-card: "#ffffff"
  on-primary: "#201f1d"
  accent-periwinkle: "#899df1"
  accent-marigold: "#f2b136"
  accent-sage: "#70b19b"
  accent-teal: "#1795a7"
  accent-rose: "#b76d7b"

typography:
  display-xl:
    fontFamily: "'neue-haas-grotesk-display', 'Assistant', sans-serif"
    fontSize: 42px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'neue-haas-grotesk-display', 'Assistant', sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'neue-haas-grotesk-display', 'Assistant', sans-serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'neue-haas-grotesk-display', 'Assistant', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-lg:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  link:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-periwinkle:
    backgroundColor: "{colors.accent-periwinkle}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-rose}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    margin: "{spacing.sm} 0 {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
  badge-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-periwinkle}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-eco:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.body}"
  footer-link-hover:
    textColor: "{colors.primary}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary CTA, rendered in sage (#bad0c9) with dark ink text. Used for add-to-cart, subscribe, and checkout actions. On hover, shifts to a slightly deeper sage (#a3bfb7). Disabled state uses a lighter sage (#d4e3de) with muted text. Height is 44px with 12px vertical padding and 24px horizontal.

**`button-secondary`** — An outlined variant on the cream canvas with a 1px hairline border. Used for "Learn More" and secondary product actions. Active state fills with the soft surface (#f3e6db). No border on hover to keep the interaction subtle.

**`button-accent-periwinkle`** — A periwinkle (#899df1) filled button with cream text. Used sparingly for featured promotions, loyalty program CTAs, and illustration-linked actions. Same 44px height as primary for visual consistency.

**`button-accent-marigold`** — A compact marigold (#f2b136) button with dark ink text. Used exclusively for sale badges and promotional tags. Smaller at 36px height with 8px vertical padding — designed to sit inline with product card content.

### Cards
**`product-card`** — A white card with 16px padding and 12px corner radius. Contains an image with 8px radius, a title in title-sm (16px, 600 weight), and a price in body-md (16px, 600 weight). Cards sit on the cream canvas with generous spacing between them (24px). No shadow — the brand relies on the card's white surface against the warm background for separation.

**`hero-section`** — A full-width section with the soft surface background (#f3e6db), large display typography (42px), and a prominent CTA button. Padding is 64px top/bottom with 24px sides. The hero image typically bleeds to the edge or sits as a full-width background.

### Navigation
**`nav-bar`** — A sticky top bar at 64px height on the cream canvas. Contains the Honest wordmark (left), search icon, account link, and cart icon (right). Navigation links use uppercase Assistant at 14px with 600 weight and 0.3px letter spacing. Active state highlights in the sage primary.

**`nav-link`** — Individual navigation items with 8px vertical and 12px horizontal padding. Hover state adds a subtle underline or color shift to primary. No background fill — the brand keeps navigation minimal.

### Forms
**`text-input`** — A cream canvas input with 1px hairline border and 12px corner radius. Focus state gains a 2px sage border. Error state uses a 2px rose (#b76d7b) border. Height is 44px with 12px vertical and 16px horizontal padding. Placeholder text uses muted (#6b6b69).

### Badges
**`badge-sale`** — A marigold (#f2b136) badge with dark ink text, 11px uppercase bold. Used on product cards to indicate discounts. 2px vertical and 8px horizontal padding with 4px corner radius.

**`badge-new`** — A periwinkle (#899df1) badge with cream text. Used for new product launches. Same sizing as sale badge but distinct color to avoid confusion.

**`badge-eco`** — A sage (#70b19b) badge with cream text. Used for eco-friendly or sustainable product attributes. Same sizing as other badges.

### Footer
**`footer-section`** — A full-width footer on the soft surface background (#f3e6db). Contains link columns, social icons, and legal text. Links use body-sm (14px) with hover state shifting to sage primary. Padding matches the hero section at 64px top/bottom.

### Accordion
**`accordion-header`** — Used for FAQ sections and product details. Title-sm typography (16px, 600 weight) with 16px vertical padding. No background — sits directly on the cream canvas. Click toggles the accordion content.

**`accordion-content`** — Body-md typography (16px, 400 weight) with 16px bottom padding. Content fades in with a smooth transition. No border or divider — spacing alone creates the separation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, stacked hero content, hamburger nav, reduced heading sizes (display-xl drops to 28px), buttons full-width |
| Tablet | 744–1128px | Two-column product grid, side-by-side hero, expanded nav links, 32px section padding |
| Desktop | 1128–1440px | Three-column product grid, full hero with image bleed, all nav links visible, 64px section padding |
| Wide | > 1440px | Max-width container at 1440px, centered content, four-column product grid, additional whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets are the full card surface, not just text
- Accordion headers are 44px minimum touch area
- Nav links have 44px minimum tap area (8px padding on 28px text)
- Badges are kept small (22px height) but sit within larger card tap targets

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1
- Hero section stacks vertically below 744px (text above image)
- Footer link columns collapse to accordion below 744px
- Search bar collapses to icon-only below 744px, expanding on tap
- Product card details (description, reviews) collapse to accordion below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components beyond primary/secondary buttons could not be reliably extracted
- Error state styling for forms (beyond border color) is inferred from common patterns, not extracted
- Sub-brand or collection-specific palettes (e.g., Honest Beauty vs. Honest Baby) were not distinguishable from the extracted data
- Dark mode styling is not present on the live site and could not be extracted
- Animation and transition timing values (ease curves, durations) were not extractable from static CSS
- The extracted color list includes Shopify checkout widget colors (#1795a7 teal, #b76d7b rose) and social icon colors that may not be part of the intentional brand palette — these are noted as accent-teal and accent-rose but should be validated against brand guidelines
- Font weight values for display faces (neue-haas-grotesk-display) are inferred from common usage; the exact weight range may vary
- Spacing values for section padding are estimated from layout patterns and should be verified against design files
- Component heights for buttons and inputs are estimated from common e-commerce patterns and extracted CSS; exact values may vary by context
