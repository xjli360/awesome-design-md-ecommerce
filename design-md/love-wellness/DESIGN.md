---
version: alpha
name: "Love Wellness"
source_url: "https://lovewellness.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A magenta voltage (#bb4192) runs through Love Wellness like a pulse — it’s the color of the brand’s primary CTA buttons, the checkout accent, and the glow behind product photography on a site that otherwise lives in near-black (#1e1814) and warm off-white (#fcfaf9). The palette is deliberately constrained: deep charcoal body text (#121212), a secondary plum (#9f377c) for hover states and badge fills, and a minty teal (#00caaa) that surfaces only in sale badges and promotional banners, creating a rare moment of cool relief. Typography leans on two distinct voices: BentonModDispCond for condensed display headlines that feel editorial and shelf-ready, and FS Kim for body copy — a rounded, humanist sans-serif that keeps the brand from feeling clinical despite its health category. Buttons are pill-shaped (`{rounded.full}`) and tall (48px), with the primary button carrying the full magenta weight and a secondary outlined variant in charcoal. Product cards use a soft shadow on white (`{colors.surface-card}`) with the product image bleeding edge-to-edge and the title set in FS Kim at 14px. The navigation bar is fixed, transparent on scroll-start then snapping to white with a bottom hairline (`{colors.hairline}`). The brand’s signature move is the “Good to Know” accordion on product detail pages — a teal-triggered expandable that reveals ingredient sourcing and usage tips, turning clinical information into a friendly reveal. The footer is dense and two-column, with a newsletter signup that uses the magenta CTA pill and a “Bye, Bye” sign-off in BentonModDispCond display type. The overall feel is confident, warm, and unapologetically pink — a health brand that refuses to be beige.

colors:
  primary: "#bb4192"
  primary-active: "#9f377c"
  primary-disabled: "#fbc6e9"
  ink: "#1e1814"
  body: "#121212"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#e5e5eb"
  hairline-soft: "#f4f4f6"
  canvas: "#fcfaf9"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#00caaa"
  accent-red: "#ff1251"
  badge-plum: "#9c4c9a"
  badge-sage: "#379476"
  star-rating: "#1e1814"

typography:
  display-xl:
    fontFamily: "'BentonModDispCond', 'Parafina Bold S', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'BentonModDispCond', 'Parafina Bold S', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'BentonModDispCond', 'Parafina Bold S', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'FS Kim', 'Inter', -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'FS Kim', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'FS Kim', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'FS Kim', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'FS Kim', 'Inter', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'FS Kim', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'FS Kim', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'FS Kim', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  badge:
    fontFamily: "'FS Kim', 'Inter', -apple-system, sans-serif"
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
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-pill-accent:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-transparent:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.body-sm}"
    fontWeight: 600
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    padding: "0 {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-plum}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-bestseller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  accordion-trigger:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-trigger-active:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: "0 {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, a full-height pill in magenta (#bb4192) with white text. Used for “Add to Cart”, “Subscribe & Save”, and checkout entry points. On hover, shifts to the deeper plum (#9f377c). Disabled state uses a soft pink (#fbc6e9) with white text to indicate inactivity without visual noise.

**`button-secondary`** — An outlined pill in charcoal (#1e1814) with a 2px stroke and transparent fill. Used for secondary actions like “Learn More” or “View Ingredients”. On hover, the fill becomes solid charcoal and text inverts to off-white (#fcfaf9). Maintains the same 48px height as the primary for alignment in form rows.

**`button-tertiary-text`** — A text-only link styled as a button, using the brand magenta (#bb4192) with no background or border. Used for “Read Reviews” and “See Full Routine” links within product cards. No hover background change — only an underline on hover for accessibility.

**`button-pill-accent`** — A smaller pill (36px) in the brand’s accent teal (#00caaa) with dark text. Reserved exclusively for promotional badges and sale banners. The teal is used sparingly across the site, so this button carries a “limited-time” urgency without feeling aggressive.

### Cards
**`product-card`** — A white card with a 1:1 product image bleeding to the top rounded corners (`{rounded.md}`) and a soft shadow. The title sits below in FS Kim 14px/600, with the price in muted gray (#676986). Badges overlay the top-left of the image. The card links to the product detail page with no hover scale — the brand trusts the image and badge to do the work.

**`product-card-image`** — The product photo fills the top half of the card at a 1:1 aspect ratio. Rounded only at the top corners to create a clean break with the white text area below. No border — the image edge meets the card edge directly.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height. On scroll-start, the bar is transparent with white logo and nav links. After a threshold (approximately 80px of scroll), it snaps to a white background (`{colors.canvas}`) with a 1px hairline bottom border (`{colors.hairline}`). The logo is the brand wordmark in BentonModDispCond. Nav links include “Shop”, “About”, “Quiz”, and “Rewards”. A small cart icon with a badge count sits at the far right.

**`nav-bar-transparent`** — The initial state of the navigation on the homepage and collection pages with hero imagery. Text and logo are white to overlay the hero photography. No background or border. Transitions to `nav-bar` on scroll.

### Forms
**`text-input`** — A standard text input with a 1px hairline border (#e5e5eb), 8px rounded corners, and 48px height. On focus, the border thickens to 2px and shifts to brand magenta (#bb4192). Used for search, newsletter email, and account forms. Placeholder text is in muted-soft (#9a9db1).

**`newsletter-input`** — A pill-shaped variant of the text input used exclusively in the footer for email capture. Same 48px height but with full rounding (`{rounded.full}`) to match the adjacent submit button. The input and button sit side by side in a single row.

### Badges
**`badge-sale`** — A teal (#00caaa) badge with uppercase 11px/700 type and dark text. Used for “SALE” and “20% OFF” indicators. The teal is the brand’s only cool accent, making sale badges instantly distinguishable from product information.

**`badge-new`** — A plum (#9c4c9a) badge with white text. Used for “NEW” and “Just Launched” labels. The plum sits between the primary magenta and the ink in saturation, creating a distinct tier of badge.

**`badge-bestseller`** — A magenta (#bb4192) badge with white text. Used for “Bestseller” and “Top Rated” labels. Shares the primary brand color to signal authority and trust.

### Accordion
**`accordion-trigger`** — The expandable header for product detail sections like “Good to Know”, “Ingredients”, and “How to Use”. In its default state, it has a soft gray background (#f7f7f8) and dark text. When active/expanded, the background shifts to teal (#00caaa) — a deliberate color switch that signals the content is open and readable. The trigger includes a plus/minus icon indicator.

**`accordion-content`** — The expandable panel below the trigger. White background with body-sm type. Padding of 16px on all sides. Content can include ingredient lists, usage instructions, and sourcing notes. No border — the teal trigger provides the visual anchor.

### Footer
**`footer-section`** — A dark footer in the brand’s near-black (#1e1814) with white text. Two-column layout: left column has the newsletter signup with the teal-accent pill button, right column has link groups (Shop, Learn, Support, Connect). The brand’s “Bye, Bye” sign-off in BentonModDispCond display type sits at the bottom center. Links are in muted-soft (#9a9db1) for legibility against the dark background.

**`footer-link`** — Footer navigation links in FS Kim 14px/400, colored in muted-soft (#9a9db1). On hover, they shift to white. No underline — the color change is the only hover indicator.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), hamburger menu replaces full nav, footer collapses to stacked layout, hero text reduces to display-md, accordions are always full-width |
| Tablet | 744–1128px | Two-column product grid (2 cards per row), nav links visible but condensed (Shop, About, Quiz), footer remains two-column but with reduced link density, hero uses display-lg |
| Desktop | 1128–1440px | Three-column product grid (3 cards per row), full nav bar with all links, footer two-column with full link groups, hero uses display-xl |
| Wide | > 1440px | Four-column product grid (4 cards per row), max-width container at 1440px with centered content, nav bar spans full viewport width, hero image scales up |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Product card tap targets are the entire card (not just the title)
- Accordion triggers are 48px tall for easy finger targeting
- Nav bar links have 48px tap areas even when text is smaller
- Cart icon has a 44x44px tap area

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Footer link groups collapse into accordion-style expandable sections on mobile
- Hero section reduces from full-bleed image to a smaller banner with text overlay
- Accordion content is always expanded on desktop for product detail pages, collapsible on mobile to save vertical space

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list includes many colors that may be Shopify widget defaults (Klarna pink, Afterpay blue, social icon colors) — the brand’s true palette is likely smaller than the 30+ colors listed. The primary (#bb4192), secondary (#9f377c), ink (#1e1814), and accent teal (#00caaa) are the most confidently identified brand colors.
- Font stack details (exact weights, fallback order) are inferred from the extracted font-family declarations. The site uses BentonModDispCond for display and FS Kim for body, but exact weight-to-size mappings may vary across pages.
- Hover states for buttons and links are based on common patterns (darken primary, invert secondary) but were not directly extracted from the live site CSS.
- Error states for form inputs (red borders, error messages) were not observed in the extraction and are not included.
- Dark mode is not supported by the brand’s current implementation — all surfaces are light with a white or off-white canvas.
- The star-rating component color is inferred from the ink color (#1e1814) as a common pattern for review stars on health/beauty sites.
- Product card shadow values are estimated based on common e-commerce patterns — the exact box-shadow CSS was not extracted.
- The newsletter input pill shape is inferred from the button-primary pill shape — the exact border-radius may differ.
- Sub-brand or collection-specific color variations (e.g., “Bye Bye Bloat” vs. “Good Girl Probiotics”) were not extracted and may use distinct accent colors beyond the core palette.
