---
version: alpha
name: "Missoma"
source_url: "https://missoma.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  IvyPresto Headline arrives at Missoma with the authority of a fashion-magazine masthead: high-contrast bracketed serifs, pronounced stroke modulation, and a self-possession that makes even a sale callout feel intentional. Set against a near-black canvas (#121212), these display cuts occupy the page the way a statement piece occupies a wrist — there is no negotiating with them. The secondary typographic voice is Neue Haas Grotesk Text, an unadorned grotesque that absorbs product names, filter labels, and pricing without drawing attention to itself, leaving the visual field clear for gold on skin.

  The palette is anchored by darkness with one chromatic interruption: cobalt #334fb4, held back for CTAs and interactive states against the near-black #121212 and navy-charcoal #242833. This blue is not decorative — it functions as a directional signal, the single non-neutral in a field of metals and ivory product photography. The neutral scale eases through #dedede at the hairline and #f3f3f3 at the softest surface, creating enough separation to frame cards and drawers without a hard border competing for attention.

  Corner radii stay deliberately minimal: `{rounded.xs}` on card containers, `{rounded.sm}` on inputs, `{rounded.full}` reserved for filter tag pills — the only place circular geometry is applied systematically, echoing the ring and hoop shapes in the product range without overclaiming the language. Product images run at a 3:4 portrait ratio, giving chain and pendant photography vertical room to breathe and reinforcing the upright proportion of the brand.

  An announcement bar in full ink (#121212) with uppercase overline type carries the 10%-off first-order offer — a single horizontal stripe above the nav that delivers the conversion prompt without disturbing the editorial register below. Section cadence is generous: 64px minimum between content blocks lets campaign imagery and editorial product modules read as intentional compositions rather than a feed scroll.

colors:
  primary: "#334fb4"
  primary-active: "#1f3a9e"
  primary-disabled: "#a0aed8"
  ink: "#121212"
  body: "#242833"
  muted: "#6b6f7a"
  hairline: "#dedede"
  canvas: "#f3f3f3"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#f3f3f3"
  announcement-bg: "#121212"
  announcement-text: "#f3f3f3"
  overlay-scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'ivypresto-headline', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ivypresto-headline', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ivypresto-headline', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'ivypresto-headline', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  overline:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-item:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'neue-haas-grotesk-text', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.4px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  announcement-bar:
    backgroundColor: "{colors.announcement-bg}"
    textColor: "{colors.announcement-text}"
    typography: "{typography.overline}"
    height: 40px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-item}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  product-card-name:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    minHeight: 600px
    paddingX: "{spacing.xl}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.on-dark}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    height: 36px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 44px
  editorial-module:
    backgroundColor: "{colors.surface-soft}"
    paddingY: "{spacing.section}"
    gap: "{spacing.xl}"
    rounded: "{rounded.md}"
  wishlist-icon:
    textColor: "{colors.ink}"
    activeColor: "{colors.primary}"
    size: 20px
  cart-drawer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    width: 420px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons
**`button-primary`** — Flat cobalt (#334fb4) fill, zero border radius, white uppercase Neue Haas Grotesk at 14px with 0.5px tracking, 48px height. Active state shifts to #1f3a9e; disabled washes to the pale #a0aed8. The square-cornered form keeps CTAs in the same sharp-edged grammar as the photography frames and grid lines throughout the site.

**`button-secondary`** — #f3f3f3 canvas fill with a 1px #121212 border, matching type treatment and 48px height. Used for secondary actions such as "Add to Wishlist" and drawer-level cancel flows. On dark-background hero sections it inverts: `{colors.on-dark}` fill, `{colors.canvas}` border to remain legible without importing the cobalt.

**`button-dark`** — #121212 fill with `{colors.on-dark}` label text; reserved for hero CTAs and the product-detail add-to-bag action where the cobalt reads too vibrant against editorial campaign imagery. Same 48px height and zero-radius form as primary.

### Text Input
**`text-input`** — White card surface, 1px #dedede border that sharpens to 1px #121212 on focus. Minimal 2px radius (`{rounded.xs}`). Placeholder renders in `{colors.muted}`. Appears in email capture modules, account sign-in, address fields at checkout, and the search overlay.

### Navigation
**`nav-bar`** — 60px fixed bar in `{colors.canvas}` with a 1px `{colors.hairline}` underline. Logo centers on mobile; on desktop primary category links in 13px Neue Haas Grotesk sit left-aligned, cart and account icons right-aligned. The bar is topped by the 40px `announcement-bar`, a full-ink stripe delivering the 10%-off first-order offer in uppercase overline type. No mega-dropdown animations visible on scroll; the bar remains sticky throughout.

### Product Card
**`product-card`** — Borderless, zero-radius, white fill with 3:4 image ratio. Product name in `{typography.body-sm}` sits directly beneath the image; price renders in `{typography.price}` on the next line. Hover on desktop typically swaps to a second product image or reveals a quick-add interaction. `product-badge` chips (NEW, SALE, LOW STOCK) sit upper-left in flat ink-black `{rounded.none}` tags with `{typography.badge}` uppercase type.

### Hero Section
**`hero-section`** — Full-width dark modules, either solid #121212 or a campaign photograph behind an `{colors.overlay-scrim}` at ~0.4 opacity. `hero-headline` in IvyPresto at 56px anchors the composition; `hero-subhead` in 16px Neue Haas provides the supporting line. CTA is `button-dark` or `button-primary` depending on whether contrast requires the blue signal. Minimum 600px height on desktop; full-viewport on mobile.

### Filter Chips
**`filter-chip`** — Pill-shaped `{rounded.full}` tags, 36px tall, 1px hairline border that upgrades to full ink on active state. Caption typography at 12px. The only zone in the UI where `{rounded.full}` is applied systematically; used in PLP filter rows and category navigation sub-rows.

### Search Bar
**`search-bar`** — 44px tall, `{rounded.sm}` radius, surface-soft fill with hairline border. On mobile lives inside a full-screen overlay triggered by a nav icon. On desktop may appear inline as a compact input in the nav row. Focus state transitions border to `{colors.ink}`.

### Editorial Module
**`editorial-module`** — Full-width `{colors.surface-soft}` strip with 64px vertical padding and `{rounded.md}` container on interior card surfaces. Typically a two-column image–text layout with an IvyPresto display heading, body-md paragraph, and a `button-secondary` link. Used for brand-story sections, gifting callouts, and campaign breaks between PLP rows.

### Footer
**`footer`** — Full ink-black (#121212) panel. Section headers in `{typography.overline}`, links in `{typography.body-sm}` colored `{colors.hairline}`, a newsletter input paired with a `button-primary` at the top of the footer column. Social icons, legal links, and payment-method badges occupy a `{colors.hairline}`-divided bar at the bottom.

### Cart Drawer
**`cart-drawer`** — 420px right-side panel with `{colors.surface-card}` fill and a `{colors.hairline}` left border. Line items show a 3:4 thumbnail, name in `{typography.title-sm}`, price in `{typography.body-sm}`. A sticky bottom bar holds the checkout CTA rendered as `button-dark`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column PLP grid; hamburger drawer navigation; hero goes full-viewport height; filter chips scroll horizontally in a single row; cart drawer becomes a full-screen modal from the bottom |
| Tablet | 744–1128px | 2-column PLP grid; horizontal nav with abbreviated category labels; hero 500px min-height; editorial module stacks image above text vertically |
| Desktop | 1128–1440px | 3–4 column PLP grid; full horizontal nav with hover mega-dropdown; hero 600px min-height; editorial module renders 50/50 image–text split |
| Wide | > 1440px | Content max-width ~1440px centered; PLP stays at 4 columns; hero imagery scales within a 1800px source cap; generous lateral padding preserves reading line length |

### Touch Targets
- All tappable elements maintain a minimum 44×44px touch zone on mobile regardless of visual icon size
- Filter chips expand to 40px height on mobile for reliable tapping within horizontal scroll rows
- Cart, wishlist, and account icons in the nav bar receive 48px tap zones even when the glyph is 20px
- Swipe-right gesture dismisses the cart drawer; tapping the scrim closes the search overlay

### Collapsing Strategy
- Navigation collapses to a hamburger icon below 744px; mega-dropdown panels become full-height accordion drawers inside the slide-in menu
- Announcement bar persists at all breakpoints; on mobile it reduces to a single marquee scroll line
- Footer columns stack 2-up on tablet and single-column on mobile, with section headers as accordion toggles
- Quick-add hover interactions on product cards are suppressed on touch devices; the add action moves to the product detail page

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed warm-metal or gold accent token extracted; Missoma's product photography relies heavily on gold tones but no swatch was derivable from the CSS extraction
- Exact announcement-bar background may be #000000 (meta theme-color) rather than #121212; values are visually near-identical but the precise token could not be confirmed
- IvyPresto axis variant (Display vs. Headline vs. Text) and available weight range could not be confirmed; using the "headline" stack as extracted
- Hover and focus states for the mega-dropdown navigation are inferred from Shopify-theme conventions, not directly extracted
- No modal backdrop opacity value extracted; 0.4 assumed from visual convention
- Sale-price and strike-through color could not be confirmed from the extracted palette; a muted or primary-error tone is likely but unverified
- Checkout and account page typography treatment was not visible at extraction time
- Secondary product-image hover swap behavior on cards is inferred, not confirmed from DOM inspection
