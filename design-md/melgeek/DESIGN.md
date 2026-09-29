---
version: alpha
name: "MelGeek"
source_url: "https://www.melgeek.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A keyboard brand that wears its marigold (#fac832) like a shopkeeper’s apron — warm, unpretentious, and impossible to miss. That single yellow carries the primary CTA, the badge on a new product drop, and the highlight on a spec callout, while the rest of the palette stays deliberately restrained: ink-black (#121212) for body text, near-white (#f6f6f6) for canvas, and a soft charcoal (#1e1e1e) for surface cards. The brand leans on Replica Pro, a monospaced-inspired geometric sans, for display heads and button labels — a typographic nod to terminal keyboards and hacker nostalgia without veering into gamer cliché. Buttons are pill-shaped (`{rounded.full}`) and tall (48px), built for fat-finger confidence on a mobile-first Shopify storefront. Product cards use a gentle `{rounded.md}` and sit on a `{surface-soft}` canvas, letting the keyboard renders — often backlit or color-swapped — do the selling. A secondary accent of electric blue (#899df1) appears on secondary CTAs and filter toggles, while a sharp red (#d32f2f) is reserved for sale badges and inventory warnings. The overall mood is workshop-meets-webstore: clean enough to trust with a credit card, but with enough personality (that yellow, those terminal fonts) to feel like a brand run by people who actually build things.

colors:
  primary: "#fac832"
  primary-active: "#e6b42a"
  primary-disabled: "#fdeba0"
  ink: "#121212"
  body: "#1e1e1e"
  muted: "#4e2a2a"
  muted-soft: "#dedede"
  hairline: "#e7e7e7"
  hairline-soft: "#f6f6f6"
  canvas: "#f6f6f6"
  surface-soft: "#ffffff"
  surface-card: "#1e1e1e"
  on-primary: "#121212"
  accent-blue: "#899df1"
  accent-orange: "#ff6b35"
  accent-red: "#d32f2f"
  sale-badge: "#d32f2f"
  new-badge: "#fac832"
  link-blue: "#007cba"

typography:
  display-xl:
    fontFamily: "'Replica Pro', 'Replica', 'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Replica Pro', 'Replica', 'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Replica Pro', 'Replica', 'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Replica Pro', 'Replica', 'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Replica Pro', 'Replica', 'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Replica Pro', 'Replica', 'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Replica Pro', 'Replica', 'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Replica Pro', 'Replica', 'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Replica Pro', 'Replica', 'Instrument Sans', Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-pill-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge-new:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.title-sm}"
    textColor: "{colors.sale-badge}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    height: 32px
  filter-tag-active:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    height: 32px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px

## Components

### Buttons
**`button-primary`** — The marigold pill (`{colors.primary}`) that drives every primary action: Add to Cart, Pre-order, Subscribe. Full-width on mobile, auto-width on desktop. On hover, darkens to `{colors.primary-active}`; disabled state fades to `{colors.primary-disabled}` with muted text. The `{rounded.full}` shape and 48px height ensure a generous, confident tap target.
**`button-secondary`** — White pill with `{colors.ink}` text used for secondary actions like "View Details" or "Learn More". Outline variant (`button-secondary-outline`) uses a 1px `{colors.hairline}` border for visual separation on light backgrounds.
**`button-accent-blue`** — Electric blue (`{colors.accent-blue}`) pill reserved for utility actions: "Compare", "Customize", or filter resets. Same shape and sizing as primary, but signals a different intent tier.
**`button-pill-small`** — Compact marigold pill (36px) for inline actions like "Quick Add" on product cards or "Apply" in filter drawers.

### Navigation
**`nav-bar`** — Fixed top bar at 64px, white background (`{colors.surface-soft}`), housing the logo, nav links, search icon, and cart. Nav links are uppercase `{typography.nav-link}` with `{colors.ink}` text; active page or hover state shifts to `{colors.primary}`. On mobile, the nav collapses into a hamburger menu with a slide-in drawer.
**`nav-link-active`** — Active nav link styled with the brand yellow (`{colors.primary}`) to indicate current section. No underline or background — pure color change.
**`nav-link-inactive`** — Default state, `{colors.ink}` text. Hover transitions to `{colors.primary}`.

### Cards
**`product-card`** — White card (`{colors.surface-soft}`) with `{rounded.md}` corners, housing a product image, title, price, and optional badges. The image area is also `{rounded.md}`. Cards sit on the `{colors.canvas}` background with `{spacing.lg}` gap in a responsive grid. On hover, a subtle shadow lifts the card (shadow not tokenized here — see Known Gaps).
**`product-card-badge-new`** — Small marigold (`{colors.new-badge}`) uppercase badge with `{typography.badge}`. Positioned top-left on the product image. Indicates a recent drop.
**`product-card-badge-sale`** — Red (`{colors.sale-badge}`) uppercase badge for discounted items. Same sizing and placement as new badge.
**`product-card-price`** — Standard price in `{typography.title-sm}` with `{colors.ink}`. Sale price uses `{colors.sale-badge}` and is typically accompanied by a strikethrough original price (strikethrough not tokenized).

### Forms & Inputs
**`text-input`** — Standard text field with `{colors.surface-soft}` background, `{rounded.sm}` corners, and 48px height. Used for email signups, search queries, and checkout fields. Focus state adds a 2px `{colors.primary}` border (not tokenized — see Known Gaps).
**`quantity-selector`** — Compact 40px input for adjusting cart quantities. `{rounded.sm}` with `{colors.surface-soft}` background. Contains minus/plus buttons and a centered numeric value.

### Search
**`search-bar`** — Full-width pill (`{rounded.full}`) on mobile, narrower on desktop. White background with `{colors.ink}` placeholder text. Often placed in the nav bar or as a hero element on collection pages. Focus state triggers a dropdown with suggested products (dropdown not tokenized).

### Footer
**`footer`** — Dark section (`{colors.ink}` background) with white text (`{colors.surface-soft}`). Contains link columns, social icons, and legal text. Links use `{colors.muted-soft}` and hover to white. Section padding is `{spacing.section}`.

### Hero
**`hero-section`** — Full-width banner on collection and landing pages. `{colors.canvas}` background with `{typography.display-xl}` headline. The `{hero-cta}` button sits centered below the headline. On product launch pages, the hero may feature a full-bleed keyboard render instead of a solid background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; buttons go full-width; hero text scales to `{typography.display-lg}`; search bar moves into nav drawer |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; hero retains `{typography.display-xl}` but with reduced padding |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero has max-width container; search bar is inline in nav |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with generous whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) meet or exceed 44px height for mobile tap targets.
- `button-primary`, `button-secondary`, `text-input`, and `search-bar` are all 48px tall.
- `button-pill-small` and `filter-tag` are 36px and 32px respectively — these are the only sub-44px elements and are used sparingly in non-critical contexts.
- Nav hamburger icon is 44x44px minimum.

### Collapsing Strategy
- On mobile (< 744px), the full nav link list collapses into a slide-in drawer triggered by a hamburger icon. The cart icon remains visible in the top bar.
- Product card grids collapse from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Hero sections reduce vertical padding by 50% on mobile and stack CTA below headline.
- Filter tags collapse into a "Filters" button that opens a modal on mobile; on desktop they remain inline.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for buttons and cards were not reliably extracted. The `primary-active` color is an approximation based on darkening the primary by ~10%. Actual hover transitions (duration, easing) are unknown.
- **Focus states** for inputs and buttons (e.g., `:focus-visible` ring color and width) were not observed. A 2px `{colors.primary}` outline is assumed but unconfirmed.
- **Error styling** for form validation (border color, error message typography) was not extracted. The extracted list includes `#d32f2f` which may serve as error red, but no form error UI was captured.
- **Dark mode** — no evidence of a dark mode toggle or alternate palette was found on the live site.
- **Shadow tokens** — box-shadow values for cards, modals, and dropdowns were not extractable from the CSS crawl. Product cards likely have a subtle hover shadow, but values are unknown.
- **Typography scale gaps** — The exact font sizes for `display-xl` through `caption-sm` are inferred from common Shopify patterns and the brand's visual weight. The extracted font-family list includes "Replica Pro italic" and "Replica Pro normal" variants, but italic and normal weights were not mapped to specific tokens.
- **Spacing scale** — The `spacing` block uses a standard 4px/8px scale common to Shopify themes. Actual site spacing may vary slightly (e.g., `section` could be 80px on some pages).
- **Checkout-widget colors** — The extracted list includes `#007cba` (likely Shopify Pay blue) and `#ff6b35`/`#ff5500` (possibly Klarna or Afterpay accents). These are not brand colors and have been excluded from the primary palette. `#007cba` is retained as `link-blue` for potential use in legal links or external references.
- **Stock-image dominant tones** — `#4e2a2a` (a deep brown) appeared in the extraction and may be a dominant tone from keyboard product photography rather than a deliberate brand color. It is used as `muted` but should be validated against actual brand guidelines.
- **Sub-brand or collection-specific palettes** — No evidence of alternate color schemes for limited editions or collaborations (e.g., custom keycap sets). The palette above represents the global site default.
