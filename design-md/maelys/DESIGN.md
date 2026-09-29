---
version: alpha
name: "Maëlys"
source_url: "https://www.maelyscosmetics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Maëlys is a clinically positioned body-solution brand that wraps its science in unabashed romance. The palette is built on a warm, almost blush-toned foundation — `#120d0e` (a near-black ink) grounds the typography, while `#e19aa6` and `#d0597a` serve as the primary and active accents, reading as dusty rose and deeper berry. The canvas is `#f7f4f2`, a soft off-white that avoids the clinical sterility of pure white (`#ffffff` is reserved for meta theme-color and surface cards). Supporting tones like `#968e89` (a warm gray for muted text) and `#ffe0e9` (a whisper-pink for soft surfaces) keep the system feeling tactile and feminine. Typography is a deliberate mix: Larken Medium (a refined serif) for display headlines that whisper luxury, Montserrat and Poppins (in Medium, Regular, and SemiBold weights) for body and UI text, and Morganite for decorative or accent moments. Corners are generous — `{rounded.sm}` (8px) for buttons, `{rounded.md}` (12px) for cards, and `{rounded.full}` for pill-shaped inputs — softening every interaction. The brand leans on `{spacing.lg}` (24px) and `{spacing.xl}` (32px) to create breathing room around product shots and ingredient callouts, and uses `#57539e` (a muted violet) and `#5bbad5` (a pastel teal) as accent badges or category tags. The overall effect is a boudoir-meets-laboratory: clinical claims delivered in a velvet glove.

colors:
  primary: "#e19aa6"
  primary-active: "#d0597a"
  primary-disabled: "#f8dede"
  ink: "#120d0e"
  body: "#5a524d"
  muted: "#968e89"
  muted-soft: "#bcb2ac"
  hairline: "#c4c4c4"
  hairline-soft: "#d9d9d9"
  canvas: "#f7f4f2"
  surface-soft: "#ffe0e9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-violet: "#57539e"
  accent-teal: "#5bbad5"
  accent-amber: "#a86416"
  badge-error: "#c23d3d"
  badge-success: "#5aaf67"
  star-rating: "#b40143"
  scrim: "#000001"

typography:
  display-xl:
    fontFamily: "'Larken Medium', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Larken Medium', Georgia, serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Montserrat', 'Poppins Medium', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins Regular', 'Montserrat', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins Regular', 'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Poppins SemiBold', 'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Poppins Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Poppins SemiBold', 'Montserrat', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.3px

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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.lg}"
    border-bottom: "1px solid {colors.hairline-soft}"
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.md} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the dusty rose `{colors.primary}` (#e19aa6) with white text. On hover or active press, it shifts to the deeper berry `{colors.primary-active}` (#d0597a). The disabled state uses `{colors.primary-disabled}` (#f8dede) with muted text. All primary buttons use `{rounded.sm}` (8px) and `{typography.button-md}` (14px Poppins SemiBold with 0.5px letter-spacing).

**`button-secondary`** — An outlined variant on the `{colors.canvas}` background with `{colors.ink}` text and a 1px `{colors.hairline}` border. Height matches the primary at 44px, but padding is reduced by 1px on each side to accommodate the border. Hover state darkens the border to `{colors.muted}`.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary-active}` (#d0597a) as the text color. Used for "Learn More" or "Shop All" links within product cards and editorial sections.

### Cards
**`product-card`** — A white (`{colors.surface-card}`) card with `{rounded.md}` (12px) corners, containing a product image and text details. The image area shares the same corner radius. Cards use `{spacing.base}` (16px) internal padding. A badge overlay (see `product-card-badge`) sits at the top-left of the image, using `{colors.accent-violet}` (#57539e) for "New" or "Bestseller" labels.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on `{colors.canvas}` background. Navigation links use `{typography.nav-link}` — 13px Poppins Medium with 1px letter-spacing and uppercase transformation. The logo (likely using `{typography.display-md}` in Larken Medium) sits left-aligned. A search icon and cart icon sit right-aligned.

### Forms & Inputs
**`text-input`** — Standard text inputs at 48px height with `{rounded.sm}` (8px) corners, a 1px `{colors.hairline}` border, and `{spacing.md}` (12px) vertical padding. On focus, the border switches to `{colors.primary}` (#e19aa6). Placeholder text uses `{colors.muted}` (#968e89).

**`search-bar-pill`** — A pill-shaped (`{rounded.full}`) search field at 48px height, used in the hero or sticky header. Background is white with a soft `{colors.hairline-soft}` (#d9d9d9) border. Text uses `{colors.body}` (#5a524d) at 14px.

### Hero & Sections
**`hero-section`** — Full-width hero blocks with `{colors.surface-soft}` (#ffe0e9) background, `{spacing.section}` (64px) top and bottom padding, and `{spacing.lg}` (24px) horizontal padding. Headlines use `{typography.display-xl}` (36px Larken Medium). A secondary headline or subtext uses `{typography.body-md}` (16px Poppins Regular).

### Footer
**`footer`** — A dark footer on `{colors.ink}` (#120d0e) background with `{colors.canvas}` text. Links use `{colors.muted-soft}` (#bcb2ac) and `{typography.link}` (14px Poppins Medium). Internal padding is `{spacing.xxl}` (48px) vertical and `{spacing.lg}` (24px) horizontal.

### Badges & Tags
**`badge-new`** — A small pill badge using `{colors.accent-teal}` (#5bbad5) background, white text, and `{rounded.xs}` (4px) corners. Used for "New Arrivals" tags.

**`badge-sale`** — Same shape as `badge-new` but with `{colors.badge-error}` (#c23d3d) background for "Sale" or "Limited Edition" markers.

### Accordion
**`accordion-header`** — Used in FAQ or ingredient detail sections. White background, `{typography.title-md}` (18px Montserrat SemiBold), with a bottom border of 1px `{colors.hairline-soft}`. Padding is `{spacing.base}` vertical and `{spacing.lg}` horizontal.

**`accordion-body`** — The expandable content area below the header, using `{typography.body-md}` (16px Poppins Regular) and `{colors.body}` (#5a524d) text. Padding reduces to `{spacing.md}` vertical.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero padding reduces to `{spacing.xl}` (32px); search-bar-pill moves below hero; footer links stack. |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links (logo, search, cart, hamburger); hero uses `{typography.display-md}` (28px); accordions remain full-width. |
| Desktop | 1128–1440px | Full nav-bar with all links; three-column product grid; hero uses `{typography.display-xl}` (36px); side-by-side hero content (text left, image right). |
| Wide | > 1440px | Max-width container at 1440px; nav-bar and footer span full viewport; product grid expands to four columns; increased whitespace around hero. |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (per Apple HIG).
- Nav-bar links have 48px tap targets (including padding).
- Accordion headers are 48px+ tall for easy tapping.
- Search-bar-pill is 48px tall for comfortable finger input.
- Product card CTAs ("Add to Cart", "Quick Shop") are 44px minimum.

### Collapsing Strategy
- Nav-bar collapses to a hamburger menu at < 744px, hiding all links except logo and cart.
- Footer link columns collapse to a single stacked column on mobile.
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Hero section collapses from side-by-side (desktop) to stacked (mobile), with image below text.
- Accordion behavior remains consistent across all breakpoints.
- Search bar moves from inline in nav (desktop) to below hero (mobile).

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons (border color, background tint) could not be reliably extracted from the live site CSS.
- Error state styling for text inputs (border color, error message typography) is not confirmed.
- Dark mode color overrides are not present in the extracted data; the system assumes light mode only.
- Sub-brand or seasonal palette variations (e.g., holiday collections) are not captured.
- Specific font weights for Larken Medium Italic and Morganite are inferred; exact weight values (e.g., 400 vs 500) may vary.
- Dropdown and select menu styling (native vs custom) is not documented.
- Loading spinner or skeleton screen design tokens are missing.
- Modal/dialog overlay styling (scrim opacity, animation) is not confirmed.
- The `#010101` and `#000001` hex values appear in extracted data but likely represent edge-case or anti-aliasing colors; `{colors.ink}` (#120d0e) is used as the primary dark token.
