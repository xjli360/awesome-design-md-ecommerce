---
version: alpha
name: "Bannor Toys"
source_url: "https://bannortoys.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A wooden-block warmth radiates from #f3ae5f, the marigold-orange that appears as meta-theme-color and pulses through the brand's primary buttons, sale badges, and footer accents — a color that reads like beeswax and late afternoon sun, not the synthetic neon of mass-market toy brands. The palette is anchored in natural tones: #108474 (a deep pine-green) and #93c8be (a sage-mist) form the secondary system, while #ab8c52 (warm ochre) and #e8d4ae (cream-wood) round out an earth-grounded spectrum. Typography leans on Petrona for display — a serif with gentle contrast that suggests hand-carved letter blocks — paired with Poppins and Nunito Sans for body and UI, giving the site a Montessori-classroom clarity. Product cards float on #fcfbf9 canvas with soft {rounded.sm} corners, while the primary CTA button uses {rounded.full} pill shapes in {colors.primary} with white text, echoing the smooth, sanded edges of the toys themselves. The navigation bar stays minimal: a centered logo, a hamburger on mobile, and a cart icon — no clutter, no carousel noise. The brand's Shopify platform is visible in the checkout-widget colors (#55baa7, #fb8b0b) that appear in the extracted palette, but the core design system remains resolutely analog-feeling: a digital storefront that wants you to touch the wood.

colors:
  primary: "#f3ae5f"
  primary-active: "#e8993a"
  primary-disabled: "#f7d4a8"
  ink: "#212121"
  body: "#393b3a"
  muted: "#555555"
  muted-soft: "#a49c8b"
  hairline: "#d9d9d9"
  hairline-soft: "#e4e4e4"
  canvas: "#fcfbf9"
  surface-soft: "#f7f4ef"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#108474"
  accent-sage: "#93c8be"
  accent-ochre: "#ab8c52"
  accent-cream: "#e8d4ae"
  accent-deep-ink: "#2e2e2e"
  badge-sale: "#f3ae5f"
  badge-new: "#108474"
  star-rating: "#ab8c52"
  footer-bg: "#282c2e"
  footer-text: "#f5f2ec"

typography:
  display-xl:
    fontFamily: "'Petrona', 'Baskerville', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Petrona', 'Baskerville', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Petrona', 'Baskerville', Georgia, serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Petrona', 'Baskerville', Georgia, serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Poppins', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Poppins', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Poppins', 'Helvetica', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Nunito Sans', 'Poppins', 'Helvetica', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Poppins', 'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Nunito Sans', 'Poppins', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Poppins', 'Nunito Sans', 'Helvetica', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.accent-green}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid #c13515"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 0px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.accent-green}"
    fontWeight: 600
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-wood:
    backgroundColor: "{colors.accent-ochre}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.footer-text}"
    rounded: "{rounded.full}"
    height: 36px
  social-icon-hover:
    textColor: "{colors.primary}"
  cart-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  cart-icon-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0px"
  accordion-content:
    padding: "0px 0px {spacing.base} 0px"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The marigold-orange pill that drives every conversion: Add to Cart, Shop Now, Subscribe. Uses `{colors.primary}` fill with `{colors.on-primary}` white text in Poppins 600 at 15px. On hover, shifts to `{colors.primary-active}` (#e8993a). Disabled state drops to `{colors.primary-disabled}` (#f7d4a8). The `{rounded.full}` pill shape echoes the smooth, sanded edges of Bannor's wooden toys — no sharp corners anywhere in the button system.

**`button-secondary`** — An outlined pill for secondary actions (Learn More, View Details). White fill with `{colors.ink}` text and a `{colors.hairline}` border. On hover, the border thickens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`. Same 48px height and `{rounded.full}` as primary.

**`button-tertiary-text`** — A text-only link styled as a button, using `{colors.accent-green}` (#108474) for the pine-green brand accent. Used for "Read Reviews" or "Size Guide" links within product cards.

**`button-pill-accent`** — A smaller pill (10px 20px padding) in `{colors.accent-green}` for secondary CTAs like "Shop Baby Toys" in category strips or the footer newsletter signup.

### Cards
**`product-card`** — A white card with `{rounded.sm}` (8px) corners and a subtle drop shadow (0 2px 8px rgba(0,0,0,0.06)). On hover, the shadow deepens to 0 4px 16px rgba(0,0,0,0.1). The card contains a full-width product photo (no rounded corners on the image itself), followed by the product title in `{typography.title-sm}` and the price in `{typography.body-md}` with `{colors.accent-green}` weight 600. Badges (Sale, New, Wood) overlay the top-left of the photo.

### Navigation
**`nav-bar`** — A 72px white bar with a single `{colors.hairline-soft}` bottom border. The logo sits centered on mobile, left-aligned on desktop. Navigation links use `{typography.nav-link}` (Poppins 500, 14px, uppercase, 0.5px letter-spacing). The active link underlines or colors to `{colors.primary}`. Cart icon sits right-aligned with a `{colors.primary}` badge showing item count.

### Forms
**`text-input`** — A clean input with `{rounded.sm}` corners, `{colors.canvas}` background, and a `{colors.hairline}` border. On focus, the border switches to a 2px `{colors.primary}` stroke. Error state uses a 2px #c13515 border. Padding is 12px 16px with 48px height for comfortable touch targets.

### Footer
**`footer`** — A dark `{colors.footer-bg}` (#282c2e) section with `{colors.footer-text}` (#f5f2ec) for readability. Links in `{typography.link}` (Nunito Sans 14px) that turn `{colors.primary}` on hover. Social icons are 36px circles with `{rounded.full}` that also highlight to `{colors.primary}`. The footer includes accordion-style sections on mobile for link groups.

### Badges
**`badge-sale`**, **`badge-new`**, **`badge-wood`** — Small uppercase labels (11px Poppins 700, 0.5px letter-spacing) with `{rounded.xs}` (4px) corners. Sale uses `{colors.primary}`, New uses `{colors.accent-green}`, and Wood uses `{colors.accent-ochre}` (#ab8c52). Padding is 4px 8px.

### Hero
**`hero-section`** — A full-width section with `{colors.surface-soft}` (#f7f4ef) background, `{spacing.section}` (64px) vertical padding. The title uses `{typography.display-xl}` (Petrona 36px 600) in `{colors.ink}`, with a subtitle in `{typography.body-md}` `{colors.muted}`. A `{rounded.full}` search bar sits below for product discovery.

### Accordion
**`accordion`** — Used in footer link groups and FAQ sections. Each accordion has a `{colors.hairline-soft}` bottom border. The header uses `{typography.title-sm}` with `{spacing.base}` vertical padding. Content area collapses with 0px top padding and `{spacing.base}` bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu; product cards go single-column (full width); hero section reduces padding to 32px; footer accordions expand; search bar moves below hero title; font sizes reduce: display-xl drops to 28px, display-lg to 22px |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links (Shop, About, Contact) with hamburger for rest; hero maintains 48px padding; footer shows two-column link layout; search bar remains visible |
| Desktop | 1128–1440px | Full nav-bar with all links visible; three-column product grid; hero uses 64px padding; footer four-column layout; search bar in hero with larger padding |
| Wide | > 1440px | Max-width container (1440px) centered; product grid expands to four columns; hero content max-width 1200px; all spacing scales proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (48px standard for primary/secondary)
- Cart icon badge is 20px minimum with readable count
- Accordion headers have 16px vertical padding for easy tapping
- Text inputs are 48px tall with 12px internal padding
- Social icons are 36px circles (slightly below 44px but acceptable for footer context)
- Nav links have 8px vertical padding plus 72px nav-bar height for tap area

### Collapsing Strategy
- Navigation links collapse into hamburger menu below 744px
- Footer link groups collapse into accordion sections below 744px
- Product grid collapses from 4 columns (wide) → 3 (desktop) → 2 (tablet) → 1 (mobile)
- Hero search bar moves from inline to below title on mobile
- Badges remain visible but may stack vertically on very narrow cards
- Cart icon badge always visible regardless of breakpoint

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product-card images (zoom, overlay, or color-swap) could not be extracted from static CSS
- Error styling for form validation (beyond the text-input border) is inferred; actual error message typography and iconography not confirmed
- Sub-brand or collection-specific color palettes (e.g., "Montessori" vs "Baby" vs "Toddler" collections) may exist but were not detected
- Dark mode is not implemented on the live site; no dark-mode tokens exist
- The extracted font list includes JudgemeIcons and JudgemeStar — these are third-party review-widget icon fonts, not brand typography
- Checkout-widget colors (#55baa7, #fb8b0b) appear in the extracted palette but belong to Shopify Pay and Klarna integrations, not the brand system
- Stock-image dominant tones (e.g., #a89cc8, #806430) may have been captured from product photography rather than intentional design tokens
- Animation durations, easing curves, and transition properties were not extracted
- Focus-visible outlines and keyboard navigation styles are not documented
- Print stylesheet behavior is unknown
