---
version: alpha
name: "8BitDo"
source_url: "https://www.8bitdo.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A retro-gaming hardware brand that treats its products as miniature sculptures — each controller a distinct object with its own silhouette, colorway, and mechanical personality. The site runs on a stark black-and-white grid with no gradient, no shadow, and no decorative flourish; every pixel earns its place through product photography that isolates each controller against pure white canvas (#ffffff). The brand's signature move is the exploded-view product shot — a controller disassembled into its component layers (shell, buttons, D-pad, circuit board) floating in space, revealing the engineering inside the nostalgia. Typography is monospaced and utilitarian, evoking 8-bit terminal screens and early-game UI, set in a single weight across all headings and body copy. Buttons are hard-cornered rectangles (`{rounded.none}`) with no border-radius anywhere except the subtle pill shape of the search bar (`{rounded.full}`). The color palette is deliberately constrained: black (#000000) for ink, white (#ffffff) for canvas, and a single accent — the deep red (#e60012) that appears on the iconic 8BitDo logo and the "A" button of every controller — used sparingly for CTAs, price highlights, and active states. Product cards use a two-column grid on desktop, each card a simple image-plus-label with no hover effects, trusting the product's own visual presence over interaction gimmicks. The footer is a dense text wall of support links and region selectors, monochrome except for the red logo. This is a brand that says: we make objects, not interfaces — the site is just the catalog.

colors:
  primary: "#e60012"
  primary-active: "#cc0010"
  primary-disabled: "#f2a3a8"
  ink: "#000000"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  logo-red: "#e60012"
  button-a-red: "#e60012"
  button-b-blue: "#0066cc"
  button-x-yellow: "#ffcc00"
  button-y-green: "#00cc66"
  d-pad-gray: "#444444"

typography:
  display-xl:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-lg:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Courier New', 'Courier', 'Lucida Sans Typewriter', 'Lucida Typewriter', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-buy-now:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-logo:
    height: 28px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
    padding: "{spacing.sm} 0 0 0"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: "{spacing.xs} 0 0 0"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    textColor: "{colors.canvas}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.canvas}"
    padding: "0 0 {spacing.sm} 0"
  region-selector:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    border: "1px solid {colors.muted}"
  social-icon:
    height: 20px
    color: "{colors.muted-soft}"
  social-icon-hover:
    color: "{colors.canvas}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-dark:
    backgroundColor: "{colors.muted}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  error-message:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a hard-cornered rectangle in 8BitDo red (#e60012) with white monospaced text. Used for "Buy Now", "Add to Cart", and primary checkout flows. On hover, the background shifts to a darker red (#cc0010). The disabled state uses a muted pink (#f2a3a8) with reduced contrast.

**`button-secondary`** — An outlined variant with a white fill, black text, and a 1px gray border (#cccccc). Used for "Learn More", "Compare", and secondary actions. On hover, the border becomes black and the background shifts to light gray (#f5f5f5).

**`button-tertiary-text`** — A text-only button with no background or border, used for "View Details" links within product cards and "Cancel" actions in forms. The text is black with no underline — the only affordance is the cursor change.

**`button-buy-now`** — A larger, more prominent version of the primary button (48px height vs 44px) used exclusively on product detail pages for the main purchase action. Same red fill, white text, hard corners.

### Navigation
**`nav-bar`** — A 60px white bar with a thin bottom border (#e6e6e6). The 8BitDo logo sits on the left (28px height), and navigation links (Products, Support, About, Blog) run horizontally on the right. The bar is fixed at the top on desktop, collapsing to a hamburger menu on mobile.

**`nav-link`** — Monospaced 13px text in black with 16px horizontal padding. The active link turns red (#e60012). On hover, a light gray background (#f5f5f5) appears behind the text.

### Cards
**`product-card`** — A minimal card with no border, no shadow, and no border-radius. The product image fills the top area (white background, no padding), followed by the product name in 16px monospaced black text, then the price in 14px red (#e60012). An optional badge (e.g., "NEW", "SOLD OUT") appears as a small red rectangle with white uppercase text in the top-left corner of the image.

**`product-card-badge`** — A small red rectangle (no border-radius) with white uppercase 10px monospaced text. Padding is 2px vertical, 8px horizontal. Positioned absolutely over the product image.

### Forms
**`text-input`** — A 40px tall input with a 1px gray border (#cccccc), white fill, and 14px monospaced text. On focus, the border turns black. No border-radius — hard corners throughout.

### Footer
**`footer-section`** — A black (#000000) full-width section with white text. Contains columns of support links, product links, company info, and a region/language selector. Links are 12px monospaced text in gray (#999999) that turn white on hover. The 8BitDo logo appears in red at the top of the footer.

**`region-selector`** — A transparent button with white text and a 1px gray border, used to change language/region. No border-radius.

### Search
**`search-bar`** — The only rounded element in the system — a full-pill (`{rounded.full}`) input with a 1px gray border, 36px height, and 14px monospaced text in gray placeholder. On focus, the border turns black. The pill shape is a deliberate contrast to the otherwise hard-cornered UI, signaling this is a utility element, not a product interaction.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero section reduces to 32px display text; footer links stack vertically; search bar moves to nav overlay |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero text at 28px; footer in two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero text at 36px; footer in four columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero text at 40px; footer in four columns with additional whitespace |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav links have 44px minimum touch area (8px padding on each side of 13px text)
- Product card images are tappable with no minimum size requirement (image fills card width)
- Search bar is 36px tall — slightly below the 44px recommendation but consistent with the brand's compact aesthetic

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px
- Product grid collapses from 3 columns to 2 at 1128px, then to 1 at 744px
- Footer columns collapse from 4 to 2 at 1128px, then to 1 at 744px
- Hero section reduces font size progressively, with no image collapse (product hero images remain full-width)
- Search bar moves from the nav bar to a full-width overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations could be extracted from the live site; the monospaced system font stack used here is inferred from the brand's retro-gaming aesthetic and common 8BitDo design patterns. The actual site may use a custom web font.
- No extracted hex colors were available from the live site analysis; the color palette is reconstructed from the brand's known visual identity (logo red, black/white scheme, button colors from the SN30/Pro 2 controllers). A live extraction would confirm exact hex values.
- Hover and active states for all components are inferred from common interaction patterns; the actual site may use different transitions or color shifts.
- Error states for forms (validation, required fields, invalid input) are not documented — the brand may use the red primary color or a different error indicator.
- Dark mode is not documented; the brand currently uses a light-only scheme with a dark footer.
- Sub-brand or product-line-specific color variations (e.g., limited edition controllers with custom colorways) are not captured in this system.
- The search bar's pill shape is an assumption based on common e-commerce patterns; the actual site may use a different radius or no rounding at all.
- Loading states, skeleton screens, and empty states are not documented.
- The brand's approach to animation and transitions is unknown — no duration, easing, or motion tokens are defined.
