---
version: alpha
name: "Devolver Digital Store"
source_url: "https://merch.devolverdigital.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A chaotic, self-aware merch storefront that treats its own brand identity like a glitchy CRT monitor — #ff00ff (magenta) and #000073 (deep navy) clash against a #222222 ink background, while #eb9e48 (a hot marigold) and #55dd99 (neon mint) stab through the #f3f3f3 canvas like arcade cabinet decals. The store runs on Shopify but refuses to look like one: Roboto Mono in monospaced blocks for product titles, Rubik for body copy, and a #dedede hairline that feels more like scanline interference than a border. Buttons snap into #334fb4 (a charged cobalt) with #fffff0 text, then switch to #dc4144 (warning red) for sale badges — the palette is a deliberate collision of early-web safety colors and late-90s game packaging. The #e6e6fa lavender and #c8a2c8 lilac in the footer suggest a softer underbelly, but the #4b0082 indigo and #8b008b dark magenta in hover states pull it back into punk territory. Every product card uses {rounded.sm} corners — just enough to feel intentional, not friendly — and the search bar floats in a #242833 surface-soft well, typed in Roboto Mono at 14px. The brand’s design language is less “clean ecommerce” and more “cassette tape sold at a convention where everyone’s wearing black and one person has a CRT monitor for a backpack.”

colors:
  primary: "#334fb4"
  primary-active: "#4169e1"
  primary-disabled: "#888888"
  ink: "#222222"
  body: "#444444"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f3f3f3"
  surface-soft: "#242833"
  surface-card: "#ffffff"
  on-primary: "#fffff0"
  accent-magenta: "#ff00ff"
  accent-marigold: "#eb9e48"
  accent-mint: "#55dd99"
  accent-red: "#dc4144"
  accent-lavender: "#e6e6fa"
  accent-lilac: "#c8a2c8"
  accent-indigo: "#4b0082"
  accent-dark-magenta: "#8b008b"
  accent-teal: "#008080"
  accent-cyan: "#00ffff"
  accent-peach: "#ffdab9"
  accent-sand: "#fad6a5"
  accent-beige: "#e4caab"
  accent-blue: "#5566ff"
  accent-brown: "#7a4a38"
  accent-amber: "#c9802b"
  accent-mint-soft: "#e6f5f5"
  accent-green: "#7bdea7"
  accent-navy: "#000073"

typography:
  display-xl:
    fontFamily: "'Roboto Mono', 'Courier New', monospace"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Roboto Mono', 'Courier New', monospace"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Rubik', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Rubik', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Rubik', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Rubik', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Rubik', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Roboto Mono', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Rubik', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Roboto Mono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 6px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-magenta:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
  nav-link-active:
    textColor: "{colors.accent-marigold}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-sold-out-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  search-bar-focus:
    borderColor: "{colors.accent-magenta}"
    boxShadow: "0 0 0 2px {colors.accent-magenta}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.accent-lavender}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-lilac}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  category-tag:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  category-tag-active:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 36px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-cyan}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline-soft}"
    height: 2px

## Components

### Buttons
**`button-primary`** — The default call-to-action button, rendered in {colors.primary} (#334fb4) with {colors.on-primary} (#fffff0) text. Uses {typography.button-md} at 16px/600 weight with 0.5px letter spacing for a slightly tighter, more deliberate feel. Corners are {rounded.sm} (6px) — not pill-shaped, not sharp. On hover, shifts to {colors.primary-active} (#4169e1). Disabled state drops to {colors.primary-disabled} (#888888).

**`button-secondary`** — Outlined-style button on {colors.canvas} (#f3f3f3) background with {colors.ink} (#222222) text. Same dimensions and typography as primary. Used for "View Details" or "Cancel" actions where the primary blue would be too aggressive.

**`button-accent-magenta`** — High-voltage variant using {colors.accent-magenta} (#ff00ff) — the brand's most distinctive color. White text (#f3f3f3). Used for limited drops, pre-order CTAs, or anything that needs to scream "now." Hover state darkens to {colors.accent-dark-magenta} (#8b008b).

**`button-accent-marigold`** — Warm accent button in {colors.accent-marigold} (#eb9e48) with dark text (#222222). Used for "Add to Cart" on special-edition items or as a secondary CTA in hero sections. Hover shifts to {colors.accent-amber} (#c9802b).

**`button-accent-red`** — Sale or clearance CTA in {colors.accent-red} (#dc4144) with white text. Only appears on discounted products. Hover darkens slightly (no extracted hex for hover, see Known Gaps).

### Text Inputs
**`text-input`** — Standard form field on {colors.canvas} background with {colors.ink} text. Uses {typography.body-md} (Rubik 16px/400). Padding 10px 16px, height 44px, {rounded.sm} corners. Focus state gains a 2px {colors.primary} box-shadow ring. Used for email signup, search queries, and checkout forms.

### Navigation
**`nav-bar`** — Full-width top navigation bar at 64px height, set on {colors.ink} (#222222) with white text. Links use {typography.nav-link} (Rubik 14px/500). Active link shifts to {colors.accent-marigold} (#eb9e48). The bar is sticky on mobile and collapses to a hamburger menu below 744px.

**`nav-link`** — Standard nav link in white. **`nav-link-active`** — Active/current page link in marigold.

### Cards
**`product-card`** — White card ({colors.surface-card}) with {rounded.sm} corners. Contains an image (also {rounded.sm}), a title in {typography.display-md} (Roboto Mono 24px/600), and a price in {typography.body-md} (Rubik 16px/400, muted gray). Sale items get a {colors.accent-red} badge; sold-out items get a {colors.ink} badge. Cards have no shadow — the brand avoids depth in favor of flat, pixel-art honesty.

**`product-card-sale-badge`** — Small red badge (2px 8px padding, {rounded.xs}) with uppercase Roboto Mono 11px/700. **`product-card-sold-out-badge`** — Same dimensions but black background, white text.

### Search
**`search-bar`** — Dark search field on {colors.surface-soft} (#242833) background with white text. Uses {typography.body-sm} (Rubik 14px/400). Height 40px, {rounded.sm} corners. Focus state gains a magenta (#ff00ff) ring — the only place the brand's most aggressive color appears in a functional UI element.

### Footer
**`footer`** — Full-width dark section on {colors.ink} background. Links in {colors.accent-lavender} (#e6e6fa) with hover to {colors.accent-lilac} (#c8a2c8). Typography is {typography.body-sm} (Rubik 14px/400). Contains legal text, social links, and a newsletter signup.

### Hero
**`hero-section`** — Full-width hero on {colors.surface-soft} (#242833) with white text. Title uses {typography.display-xl} (Roboto Mono 32px/700). CTA button is {colors.accent-magenta} with 14px 32px padding and 48px height. The hero may also feature a secondary CTA in {colors.accent-marigold}.

### Category Tags
**`category-tag`** — Pill-shaped tag in {colors.accent-marigold} (#eb9e48) with dark text. Uses {typography.badge} (Roboto Mono 11px/700 uppercase). Padding 4px 12px, {rounded.full}. Active state switches to {colors.accent-mint} (#55dd99). Used for filtering product categories (e.g., "T-Shirts", "Vinyl", "Posters").

### Icon Buttons
**`icon-button`** — Transparent circular button (36px) with white icon. Hover fills with {colors.surface-soft} and icon shifts to {colors.accent-cyan} (#00ffff). Used for cart, account, and social media icons.

### Dividers
**`divider`** — 1px line in {colors.hairline} (#dedede). **`divider-strong`** — 2px line in {colors.hairline-soft} (#eeeeee). Used sparingly — the brand prefers whitespace over rules.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero text reduces to 24px; search bar moves below nav; footer links stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav remains horizontal but links shrink to 13px; hero CTA buttons stack if two are present |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero uses full display-xl size; search bar in nav |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to 4 columns; hero section may include video background |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (Apple HIG compliance).
- Icon buttons are 36px — slightly below the 44px ideal, but acceptable for secondary actions.
- Category tags are 28px tall — touch-friendly on mobile with adequate spacing.
- Search bar is 40px tall — borderline; consider increasing to 44px on mobile.

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px.
- Product grid collapses from 3 columns → 2 columns → 1 column as viewport shrinks.
- Footer link columns collapse to single vertical stack at < 744px.
- Hero section may hide secondary CTA on mobile to avoid visual clutter.
- Category tag strip scrolls horizontally on mobile (no collapse, just overflow-x: auto).

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most accent buttons (magenta, marigold, red) are inferred from brand patterns — exact hex values not extracted from live site.
- Error styling for form validation (border colors, error message typography) not observed.
- Dark mode / high-contrast mode not detected — the brand's default is already dark-ink-heavy, but no explicit dark mode toggle exists.
- Sub-brand or collection-specific palettes (e.g., "Devolver Bootleg" vs. "Serious Sam" merch) may use different accent colors — not captured.
- Checkout flow styling (Shopify checkout override) not extracted — may use default Shopify colors.
- Loading states, skeleton screens, and empty states not observed.
- Animation timing and easing curves not extracted.
- Focus-visible styles for keyboard navigation not confirmed.
- The extracted color list includes many low-frequency colors (#008080, #00ffff, #ffdab9, etc.) that may be stock image tones or social icon defaults — only the most frequent and distinctive ones were used in the palette.
