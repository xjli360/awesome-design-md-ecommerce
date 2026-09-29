---
version: alpha
name: "Grindhouse Releasing"
source_url: "https://grindhousereleasing.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The brand’s identity is forged from a single, unapologetic voltage: #ff4500, a scorching orange-red that screams from every primary button, badge, and accent element against a battlefield of near-black (#1e1f26) and concrete gray (#444444). This is not a clean white canvas — it’s a grimy, high-contrast arena where #ff4500 acts as the blood-spatter, the neon sign, the single splash of color in a monochrome grindhouse trailer. The typography, set in Source Serif Pro, carries a scholarly weight that feels deliberately out of place — a serious serif for a catalog of cult, horror, and exploitation films, as if Criterion Collection had a fever dream about a 42nd Street grindhouse. Cards and buttons use sharp, minimal rounding ({rounded.sm}), refusing the friendly pill shapes of mainstream commerce; the only softness comes from the occasional #eeeeee surface that breaks up the oppressive dark. The extracted palette is a chaotic mess of social-media blues, payment-widget greens, and stock-image pinks — a digital patina that obscures a simpler, more brutal truth: this site runs on black, white, and that one incendiary orange.

colors:
  primary: "#ff4500"
  primary-active: "#e03e00"
  primary-disabled: "#ffb380"
  ink: "#1e1f26"
  body: "#444444"
  muted: "#6a6a6a"
  muted-soft: "#999999"
  hairline: "#444444"
  hairline-soft: "#666666"
  canvas: "#1e1f26"
  surface-soft: "#2a2b33"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blood: "#e21b24"
  accent-teal: "#1ea0c3"
  star-rating: "#ff9900"

typography:
  display-xl:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}"
  text-input-error:
    borderColor: "{colors.accent-blood}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-blood}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: 80px 24px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: 32px 24px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in #ff4500 with white uppercase serif text. On hover, it shifts to `primary-active` (#e03e00). The disabled state uses `primary-disabled` (#ffb380), a washed-out orange that signals inactivity without losing brand identity. Sharp 4px corners ({rounded.sm}) keep the button feeling aggressive and direct, not friendly.

**`button-secondary`** — A light button on the dark canvas, using `surface-card` (#eeeeee) background with `ink` (#1e1f26) text. Active state inverts to `hairline` (#444444) background. Used for "View Details" or "Learn More" actions where the primary orange would overwhelm.

**`button-tertiary-text`** — A text-only button with transparent background and `primary` text color. No border, no fill — just the orange text on dark or light backgrounds. Used for "Cancel" or "Back to Catalog" links.

### Cards
**`product-card`** — A white (#eeeeee) card with 4px rounding, no padding at the container level (image bleeds edge-to-edge). The title uses `title-sm` in `ink`, while the price is set in `primary` orange using `body-md`. The card sits on the dark canvas, creating a stark film-strip effect.

**`badge-new`** — A tiny orange (#ff4500) pill with white uppercase text, 2px rounding, used to flag new releases. `badge-sale` uses `accent-blood` (#e21b24) for clearance items — a second brand voltage that reads as danger or discount.

### Navigation
**`nav-bar`** — A fixed 64px bar on the dark canvas (#1e1f26) with white uppercase nav links. Active links switch to `primary` orange. No logo background — the brand name is set in `display-md` or a custom wordmark.

**`category-tag`** — Small tags for filtering by genre (Horror, Cult, Exploitation). Default state is dark gray (#2a2b33) with muted text; active state flips to orange background with white text. 4px corners keep the edge.

### Forms
**`text-input`** — A white (#eeeeee) input field with 4px rounding and 44px height. On focus, it gets a 2px orange box-shadow ring. Error state swaps the ring to `accent-blood` (#e21b24). The dark canvas makes these inputs pop like ticket stubs.

### Footer
**`footer`** — A dark section (#1e1f26) with muted gray text (#999999) in `caption` size. Links use `link` typography and turn `primary` on hover. No social icons visible in the extracted palette — the footer is lean, just legal text and a copyright.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text shrinks to `display-lg`; buttons go full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero padding reduces to 48px |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero at 80px padding |
| Wide | > 1440px | Max-width container at 1440px; content centered; hero scales to 100px padding |

### Touch Targets
- All buttons and inputs maintain minimum 44px height for touch accessibility
- Nav links on mobile use 48px touch targets
- Category tags use 36px height with 12px padding for comfortable tapping

### Collapsing Strategy
- On mobile, the top nav collapses to a hamburger menu; the brand wordmark remains visible
- Product cards stack to single column; images scale to full width
- Hero section reduces padding and font size to avoid overflow
- Category tag strip becomes horizontally scrollable with hidden overflow

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is heavily polluted with third-party widget colors (Shopify Pay blue #4280ff, Klarna pink #f00075, Afterpay teal #02e49b, social media blues #0757fe, #0a7aff, #5865f2, etc.). The true brand palette is likely much smaller — black, white, orange, and one or two accent colors. The `primary` choice of #ff4500 is an educated guess based on its distinctiveness and frequency in the list.
- No hover, focus, or active states could be reliably extracted beyond the primary button.
- Font stack is incomplete: only `Source Serif Pro` and `inherit` were found. A fallback stack (Georgia, Times New Roman, serif) is assumed.
- No dark mode or high-contrast mode data available.
- Sub-brand or collection-specific palettes (e.g., for "Cult Classics" vs. "Horror") are unknown.
- No animation or transition timing data (hover fades, card lifts, etc.).
- No iconography or illustration style documented — the site may use custom icons or none.
- No data on error states, success states, or form validation beyond the text-input error ring.
- The `rounded` scale is inferred from the general aesthetic; actual values may vary.
