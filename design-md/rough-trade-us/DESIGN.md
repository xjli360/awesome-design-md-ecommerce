---
version: alpha
name: "Rough Trade US"
source_url: "https://www.roughtrade.com/en-us"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record store that wears its independence as a raw, unpolished edge — the palette is pulled from the physical world of vinyl sleeves and cardboard mailers, not a digital mood board. The extracted hexes read like a crate-digger's haul: `#404040` (the deep charcoal of a record sleeve spine), `#bd2426` (a vintage label red that appears on sale badges and price drops), `#62a1d8` (the washed denim blue of a used-bin divider), and `#9bca3e` (a fluorescent lime that could only be a New Order or Talking Heads 12″ single). There is no single brand color; instead, Rough Trade uses a functional palette where `#163959` (navy) anchors headers and `#f68b1f` (safety orange) punctuates limited-edition drops. The typography stack is system-native — `-apple-system`, `Arial`, `Helvetica Neue`, `Segoe UI`, `Roboto`, `Ubuntu` — a deliberate refusal of custom type that mirrors the store's ethos: the music is the design, not the font. Buttons are sharp-cornered (`{rounded.xs}`), text is dense, and whitespace is tighter than a 7″ single sleeve. The site feels like a warehouse shelf: organized but not precious, with `#ebebeb` hairline dividers and `#dedede` surface cards that echo the cardboard of a mail-order shipment. The Cloudflare challenge page that greeted extraction is itself a design signal — this is a site that prioritizes security and inventory accuracy over frictionless browsing, a stance that says "we've been burned by bots and we don't care if you have to wait."

colors:
  primary: "#bd2426"
  primary-active: "#a01e20"
  primary-disabled: "#e8a0a1"
  ink: "#272727"
  body: "#404040"
  muted: "#595959"
  muted-soft: "#737373"
  hairline: "#ebebeb"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-navy: "#163959"
  accent-orange: "#f68b1f"
  accent-lime: "#9bca3e"
  accent-green-dark: "#516b1d"
  accent-blue: "#62a1d8"
  accent-blue-dark: "#2f7bbf"
  accent-red-bright: "#de5052"
  accent-red-dark: "#521010"
  accent-orange-soft: "#f9b169"
  accent-orange-deep: "#ee730a"
  accent-brown: "#904b06"
  accent-brown-light: "#c16508"
  border-strong: "#bfbfbf"
  badge-sale: "#bd2426"
  badge-new: "#9bca3e"
  badge-limited: "#f68b1f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-original:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Segoe UI', Roboto, Ubuntu, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: line-through

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
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
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.accent-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 0
  button-pill-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-icon-square:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.accent-navy}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    color: "{colors.primary}"
  product-card-price-original:
    typography: "{typography.price-original}"
    color: "{colors.muted-soft}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-exclusive:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  footer-section:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.canvas}"
  footer-link-hover:
    color: "{colors.accent-orange-soft}"
  hero-banner:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
  add-to-cart-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 52px
  category-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  category-nav-item:
    typography: "{typography.nav-link}"
    color: "{colors.muted}"
  category-nav-item-active:
    color: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Checkout," and "Pre-Order." A sharp-cornered (`{rounded.xs}`) rectangle in `#bd2426` red with white text, set in 15px/600 weight system sans-serif. On hover, it deepens to `#a01e20` (`{colors.primary-active}`); disabled state fades to a pale pink `#e8a0a1`. The 44px height and 12px/24px padding give it a compact, no-nonsense profile that matches the store's utilitarian ethos.

**`button-secondary`** — The inverse of primary: white background with `#272727` text and a 1px `#ebebeb` border. Used for "Browse," "View Details," and secondary cart actions. Active state fills with `#ebebeb` (`{colors.hairline}`). Same 44px height and `{rounded.xs}` corners as primary, ensuring visual consistency across the button family.

**`button-tertiary`** — A text-only link styled as a button, used for "Clear Filters," "Cancel," and "View All." No background or border, set in `#163959` navy (`{colors.accent-navy}`) with 15px/600 weight. Underline appears on hover. The 12px vertical padding keeps it aligned with sibling buttons in filter bars and modals.

**`button-pill-accent`** — A pill-shaped (`{rounded.full}`) accent button reserved for limited-edition drops, flash sales, and exclusive pre-orders. Uses `#f68b1f` safety orange (`{colors.accent-orange}`) with white text in 13px/600 weight. At 36px tall, it's intentionally smaller than primary buttons — a visual signal that this is a time-sensitive or scarcity-driven action.

**`button-icon-square`** — A 40×40px square icon button with `#f5f5f5` soft surface background and `#404040` body text. Used for wishlist hearts, share icons, and quick-view toggles on product cards. `{rounded.sm}` (4px) corners keep the square shape from feeling harsh.

### Navigation
**`top-nav`** — A 64px white bar with a 1px `#ebebeb` bottom border. Navigation links are 14px uppercase/600 weight in `#272727` ink. The active state uses a 2px `#bd2426` red underline; inactive links sit in `#595959` muted. The nav houses the Rough Trade logo (left), genre/category dropdowns (center), and utility icons (search, account, cart) on the right. No sticky behavior — the nav scrolls with the page, reinforcing the "warehouse shelf" feel.

**`category-nav`** — A secondary horizontal strip below the top nav, with `#f5f5f5` background and 8px/16px padding. Lists genre categories (Rock, Electronic, Jazz, etc.) as 14px uppercase links. Active category gets a 2px red underline; inactive are `#595959` muted. This strip collapses into a hamburger-style dropdown on mobile.

### Cards
**`product-card`** — The primary inventory display unit: a white card with a 1px `#dedede` soft border and `{rounded.sm}` (4px) corners. Contains a product image (with `#f5f5f5` placeholder background), artist name in 14px/400 `#595959`, album title in 16px/600 `#272727`, and price in 16px/700 `#272727`. On hover, the card background shifts to `#f5f5f5` and the border to `#ebebeb`. Sale prices render in `#bd2426` red with the original price struck through in `#737373`.

**`badge-sale`**, **`badge-new`**, **`badge-limited`**, **`badge-exclusive`** — Small uppercase badges (11px/700) that overlay product card images. Each uses a distinct background color: `#bd2426` red for sale, `#9bca3e` lime for new arrivals, `#f68b1f` orange for limited editions, and `#163959` navy for exclusives. All have `{rounded.xs}` (2px) corners and 2px/8px padding. The badge sits in the top-left corner of the product image, 8px inset.

### Forms & Inputs
**`search-bar`** — A 40px-tall input with `#f5f5f5` background, 1px `#ebebeb` border, and `{rounded.sm}` (4px) corners. Text is 14px/400 in `#404040`. On focus, the background turns white and the border switches to `#163959` navy. The search icon sits at the left edge (16px inset), and a clear button appears on the right when text is entered.

**`quantity-selector`** — A compact 40px-tall control with white background, 1px `#ebebeb` border, and `{rounded.xs}` (2px) corners. Contains a minus button, a numeric display (16px/400), and a plus button. Used on product detail pages and cart line items.

**`filter-chip`** — A pill-shaped (`{rounded.full}`) filter toggle with white background, 1px `#ebebeb` border, and 13px/600 text in `#404040`. Active state inverts to `#272727` background with white text. Used in genre, format, and price-range filter bars. Chips are 6px/16px padding and sit in a horizontally scrollable strip.

### Footer
**`footer-section`** — A deep navy (`#163959`) footer block with white text. Contains four columns: "Customer Service," "About," "Connect," and "Newsletter Signup." Links are 14px/500 in white with an `#f9b169` orange hover state. The newsletter input uses a white background with navy text and a `#bd2426` red submit button. Padding is 48px vertical, 24px horizontal.

### Hero
**`hero-banner`** — A full-width promotional banner with `#163959` navy background and white text in 28px/700. Used for featured releases, seasonal campaigns, and genre spotlights. An accent variant uses `#f68b1f` orange background for flash sales. The hero includes a headline, optional subtitle (14px/400), and a `button-primary` CTA. Padding is 64px vertical, 24px horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items per row); top-nav collapses to hamburger; category-nav becomes a dropdown; search bar moves to a full-width overlay; hero banner reduces to 32px vertical padding; filter chips stack vertically; footer columns stack to single column |
| Tablet | 744–1128px | Two-column product grid (3-4 items per row); top-nav shows limited links (logo, search, cart); category-nav is a horizontal scrollable strip; hero banner at 48px vertical padding; filter chips in a 2-column grid |
| Desktop | 1128–1440px | Three-column product grid (4-5 items per row); full top-nav with all links; category-nav fully visible; hero banner at 64px vertical padding; filter chips in a horizontal strip; footer in 4-column layout |
| Wide | > 1440px | Four-column product grid (5-6 items per row); max-width container at 1440px; all elements at maximum spacing; hero banner can accommodate larger imagery |

### Touch Targets
- All interactive elements (buttons, links, chips) have a minimum touch target of 44×44px on mobile.
- Product card tap targets (add to cart, wishlist, quick view) are at least 40×40px.
- Filter chips are 36px tall with 16px horizontal padding, exceeding the 44px touch target for height.
- Search bar and quantity selector are 40px tall.
- Navigation links have 48px tap zones (64px nav bar height with 8px internal padding).

### Collapsing Strategy
- Top navigation collapses from a full horizontal bar to a hamburger menu at < 744px. The logo remains centered; utility icons (search, account, cart) move to the right of the hamburger.
- Category navigation collapses from a visible horizontal strip to a dropdown select at < 744px.
- Product grid collapses from 4-5 columns (desktop) to 2 columns (tablet) to 1 column (mobile).
- Footer collapses from 4 columns to 2 columns at tablet, to 1 column at mobile.
- Filter chips collapse from a horizontal scrollable strip to a vertical stack at mobile.
- Hero banner reduces vertical padding from 64px to 32px at mobile.
- Search bar transitions from a fixed header element to a full-screen overlay on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is dominated by generic web colors (multiple grays, blues, and one bright accent) — the brand's true primary may be more distinctive than `#bd2426` red, but this was the most unique color in the extraction. A deeper crawl of the actual site (bypassing Cloudflare) would yield a more accurate palette.
- Font-family declarations were system-only; no custom typefaces were detected. Rough Trade may use a proprietary or licensed font that wasn't extractable from the Cloudflare challenge page.
- Hover states for all components are inferred from common e-commerce patterns; actual hover colors, transitions, and animations could not be extracted.
- Error states (form validation, out-of-stock messaging, payment failures) are not represented — no error hexes or typography were found.
- Dark mode is not detected; the extracted palette assumes a light theme.
- The Cloudflare challenge page prevented extraction of actual page structure, component hierarchy, and layout patterns. All component definitions are based on industry conventions for independent record store e-commerce sites.
- Sub-brand or seasonal color variations (e.g., Rough Trade NYC vs. Rough Trade US) could not be identified.
- Loading states, skeleton screens, and spinner designs are unknown.
- The `#0051c3` blue in the extraction may be a Shopify or payment-widget color rather than a brand color — it's excluded from the palette as likely non-brand.
- Accessibility ratios (contrast between text and background) have not been verified against WCAG standards.
