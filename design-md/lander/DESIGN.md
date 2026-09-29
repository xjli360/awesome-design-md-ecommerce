---
version: alpha
name: "Lander"
source_url: "https://www.lander.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand that builds gear for the outdoors but refuses to look like it — Lander’s palette opens with a near-black ink (#23211f) that reads as deep shadow, not corporate charcoal, and a warm stone (#908580) that could be trail dust or a city sidewalk. The single voltage is a stop-sign red (#db001c), used sparingly on CTAs and sale badges, while the canvas (#e8e6e5) is a soft, slightly warm off-white that avoids the sterile hospital feel of pure #ffffff. The extracted palette is dominated by system grays and Bootstrap utility colors (alert blues, greens, yellows), suggesting the site leans heavily on Shopify framework defaults for form states and messaging, but the brand’s true identity lives in those three distinctive tones plus a muted slate (#676986) that appears in secondary text and icons. Typography mixes a serif — Bookmania-Semibold, declared with `!important` — for display moments, with system sans for body copy, creating a tension between traditional craftsmanship and modern utility. The red (#db001c) appears on primary buttons and promotional banners, never overwhelming the product photography that carries the real emotional weight. Lander’s design feels like a well-worn canvas tent: functional, slightly textured, and built to last without shouting about it.

colors:
  primary: "#db001c"
  primary-active: "#b30016"
  primary-disabled: "#f5a3ae"
  ink: "#23211f"
  body: "#3d3b39"
  muted: "#676986"
  muted-soft: "#908580"
  hairline: "#c8cbcf"
  hairline-soft: "#dae0e5"
  canvas: "#e8e6e5"
  surface-soft: "#f2f1f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-warm: "#908580"
  badge-sale: "#db001c"
  star-rating: "#23211f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Bookmania-Semibold', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Bookmania-Semibold', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Bookmania-Semibold', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Bookmania-Semibold', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    padding: 14px 0
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    padding: 14px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "top-left"
  hero-section:
    backgroundColor: "{colors.canvas}"
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
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "2px solid {colors.ink}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  quantity-stepper:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with `{colors.primary}` (#db001c) and white text. Used for "Add to Cart", "Shop Now", and checkout entry points. On hover, shifts to `{colors.primary-active}` (#b30016). Disabled state uses `{colors.primary-disabled}` (#f5a3ae) with reduced opacity. Height is 48px with `{rounded.sm}` (4px) corners — intentionally subtle, not pill-shaped, to keep the brand grounded in utility.

**`button-secondary`** — An outlined variant with a 2px `{colors.ink}` (#23211f) border on the `{colors.canvas}` (#e8e6e5) background. Used for "Learn More" and secondary actions. On hover, the button fills solid with `{colors.ink}` and text flips to white. This inversion is the brand's signature interaction — dark fills dark.

**`button-tertiary-text`** — A text-only button with no background or border, used for "View Details" links within product cards and "Cancel" actions in modals. On hover, text color shifts from `{colors.ink}` to `{colors.primary}` (#db001c), creating a subtle red underline effect via the color change alone.

**`button-pill`** — A smaller, fully rounded button (`{rounded.full}`) at 36px height, used for filter chips, category tags, and quick-add actions. Filled with `{colors.primary}` and white text. The pill shape is reserved for secondary or utility actions — the primary CTA stays squared-off.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.md}` (8px) corners and no border — the card floats on the `{colors.canvas}` background. The product image occupies the top with a 1:1 aspect ratio and rounded top corners. Title uses `{typography.title-sm}` (16px, semibold) and price uses `{typography.body-md}` (16px, regular). Sale badges (`{colors.badge-sale}`) are positioned top-left with `{rounded.xs}` (2px) corners and uppercase 11px type.

### Navigation
**`nav-bar`** — A 72px fixed bar on `{colors.canvas}` with a subtle bottom border (`{colors.hairline-soft}`). Navigation links are uppercase 14px medium weight with 0.3px letter spacing. Active links get a 2px bottom border in `{colors.ink}`. The bar is sticky on scroll, maintaining the same background and height.

### Forms
**`text-input`** — Standard input fields at 48px height with `{rounded.sm}` (4px) corners and a 1px `{colors.hairline}` (#c8cbcf) border. On focus, the border thickens to 2px and shifts to `{colors.ink}` (#23211f). Error state uses a 2px `{colors.primary}` (#db001c) border. Placeholder text is `{colors.muted-soft}` (#908580). The select input and textarea follow the same pattern, with the textarea having no fixed height.

### Badges
**`badge-new`** — A small, dark badge (`{colors.ink}` background, white text) used for "New Arrivals" tags. Uppercase 11px bold with 0.5px letter spacing and `{rounded.xs}` (2px) corners. Padding is tight at 2px 8px.

**`badge-sale`** — Same structure as `badge-new` but with `{colors.badge-sale}` (#db001c) background. Used for percentage-off and clearance tags.

### Footer
**`footer-section`** — A dark footer on `{colors.ink}` (#23211f) with white text. Links are `{colors.muted-soft}` (#908580) and shift to white on hover. Padding is generous at 48px vertical and 24px horizontal. The footer contains column-based link lists, social icons, and legal text in `{typography.caption-sm}`.

### Hero
**`hero-section`** — A full-width section on `{colors.canvas}` with large serif display type (`{typography.display-xl}` at 48px). The primary CTA sits below the headline. The hero may include a background image or product shot, but the text and button remain on the soft off-white canvas. Padding is 64px vertical.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), nav collapses to hamburger, hero type drops to `{typography.display-lg}` (36px), buttons go full-width, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid (2 col), nav links visible but condensed, hero type at `{typography.display-lg}` (36px), buttons remain inline |
| Desktop | 1128–1440px | Three-column product grid (3 col), full nav with all links, hero type at `{typography.display-xl}` (48px), standard button sizing |
| Wide | > 1440px | Four-column product grid (4 col), max-width container (1440px) centered, hero type at 56px (scaled), all elements maintain proportional spacing |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40x40px with `{rounded.full}` — the tap target is the full circle, not the icon itself
- Quantity steppers and select inputs are 40px tall with adequate spacing between adjacent controls
- Nav links on mobile have 48px tap targets in the hamburger menu

### Collapsing Strategy
- Primary navigation collapses to a hamburger icon at < 744px, revealing a full-screen overlay menu
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 to 2 at tablet, then to a single stacked column at mobile
- Search bar collapses from a full input with placeholder to an icon-only trigger at mobile, expanding to a full overlay on tap
- Hero section reduces vertical padding from 64px to 40px on mobile, with smaller headline type

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for most components were inferred from common patterns — the extracted CSS did not include `:hover` or `:focus` declarations for buttons, inputs, or links
- Error, success, and warning form states beyond the error border are not documented — the extracted palette includes Bootstrap alert colors (#155724 green, #0c5460 teal, #856404 yellow, #721c24 red) but their specific usage in Lander's forms is unclear
- Dark mode is not present on the live site — no `prefers-color-scheme` media queries or dark palette tokens were found
- The serif font "Bookmania-Semibold" was declared with `!important` in the CSS, suggesting it may be loaded via a third-party service (Typekit, Cloud.typography) — the exact font stack and fallback behavior could not be verified
- Animation and transition durations, easings, and micro-interaction details (button press, card hover lift, nav dropdown) were not extractable from the static CSS
- The extracted hex list is heavily polluted with Shopify framework defaults (Bootstrap alert colors, system grays, social icon colors) — the true brand palette is likely smaller and more intentional than the 30+ colors listed
- Product card hover states (shadow elevation, image zoom, quick-add button reveal) are undocumented
- Modal, drawer, and overlay component styles (backdrop scrim opacity, animation, close button placement) are not available
- The checkout flow uses Shopify's default styling — Lander's brand treatment of the checkout page (if any) could not be determined
- Star rating component (for reviews) is assumed to use `{colors.star-rating}` (#23211f) but the exact implementation (filled vs. empty state, half-star support) is unknown
