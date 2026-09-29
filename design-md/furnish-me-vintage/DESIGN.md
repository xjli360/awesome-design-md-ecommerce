---
version: alpha
name: "Furnish Me Vintage"
source_url: "https://www.furnishmevintage.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The warm golden amber (#efc01d) that surfaces in accents and hover states isn't chosen arbitrarily — it's the color of aged teak, honey walnut, and the patina collectors spend years searching for, pulled directly into the interface. Built on WordPress with an Elegant Themes / Divi foundation (ETmodules icon font, system-first type stacks), Furnish Me Vintage subordinates every design decision to furniture photography: surfaces stay a clean off-white (#f4f4f4, #f3f3f3) and the grid exists primarily as a neutral stage. Transactional controls — navigation links, CTA buttons, price figures — lean into a cool authority blue (#006799, #2ea3f2), the Divi-default hue that anchors the buyer's action layer without competing with the merchandise. The amber warmth (#efc01d, #f0b849) reserves itself for highlights, category chips in active state, and "New Arrival" badge fills, functioning as the visual signature that distinguishes the brand from plain-white auction houses. Text runs Open Sans on near-black (#2f2f2f) — utilitarian typography that makes no aesthetic claim, ceding that space entirely to a well-lit photograph of a Hans Wegner chair or Arne Vodder credenza. Borders and separation layers draw from a tight band of grays (#d9d9d9 to #eeeeee), with a quiet muted blue-gray (#bcc8c9) appearing in soft card dividers and secondary surfaces — the digital equivalent of catalog linen. Rounded corners sit at a modest {rounded.sm} throughout buttons and cards, reading as approachable without the precious roundness of fashion or beauty brands. Sold items take a direct red (#cc1818), unambiguous and urgent. The dark footer (#43454b) provides the one moment of enclosure in an otherwise open layout. The system's restraint is the point: every UI element exists to move the eye toward the inventory, where a single teak sideboard does more brand communication than any color or typographic choice ever could.

colors:
  primary: "#efc01d"
  primary-active: "#d4a800"
  primary-disabled: "#f5e282"
  accent-blue: "#006799"
  accent-blue-hover: "#2ea3f2"
  accent-blue-light: "#52acf8"
  amber-soft: "#f0b849"
  ink: "#2f2f2f"
  body: "#313131"
  muted: "#555555"
  muted-soft: "#aaaaaa"
  hairline: "#d9d9d9"
  hairline-soft: "#eeeeee"
  border-mid: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#f3f3f3"
  surface-mid: "#dadada"
  muted-blue-gray: "#bcc8c9"
  on-primary: "#2f2f2f"
  on-accent-blue: "#ffffff"
  sold-red: "#cc1818"
  dark-overlay: "#43454b"

typography:
  display-xl:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
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
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.accent-blue}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-blue}"
    rounded: "{rounded.sm}"
  button-inquiry:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-accent-blue}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-inquiry-hover:
    backgroundColor: "{colors.accent-blue-hover}"
    textColor: "{colors.on-accent-blue}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.accent-blue}"
    placeholderColor: "{colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 14px 10px 40px"
    iconColor: "{colors.muted-soft}"
    height: 42px
    borderFocus: "1px solid {colors.accent-blue}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 70px
    borderBottom: "1px solid {colors.hairline}"
    linkColor: "{colors.ink}"
    linkHover: "{colors.accent-blue}"
    logoMaxHeight: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "4/3"
    imageFit: cover
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    captionTypography: "{typography.body-sm}"
    captionColor: "{colors.muted}"
    gap: "{spacing.sm}"
  product-card-hover:
    border: "1px solid {colors.muted-blue-gray}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    cursor: pointer
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    padding: "{spacing.section} {spacing.xl}"
    imageOverlay: "rgba(47,47,47,0.25)"
    ctaSpacing: "{spacing.lg}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "6px {spacing.md}"
    border: "1px solid {colors.hairline}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "6px {spacing.md}"
    border: none
  badge-sold:
    backgroundColor: "{colors.sold-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-style:
    backgroundColor: "{colors.amber-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  price-tag:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  price-tag-sold:
    typography: "{typography.price-display}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through
  section-heading:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
    accentUnderlineColor: "{colors.primary}"
    accentUnderlineHeight: 3px
    marginBottom: "{spacing.lg}"
  divider:
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    borderStyle: solid
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.border-mid}"
    linkColor: "{colors.accent-blue}"
    linkHover: "{colors.accent-blue-hover}"
  product-gallery:
    mainImageRounded: "{rounded.sm}"
    thumbRounded: "{rounded.xs}"
    thumbBorderActive: "2px solid {colors.primary}"
    thumbBorderInactive: "2px solid {colors.hairline}"
    backgroundColor: "{colors.surface-soft}"
  inquiry-form:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
    headingTypography: "{typography.title-md}"
    inputGap: "{spacing.md}"
  footer:
    backgroundColor: "{colors.dark-overlay}"
    textColor: "{colors.hairline-soft}"
    linkColor: "{colors.accent-blue-light}"
    linkHover: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — The amber-gold (#efc01d) primary button carries actions like "Add to Cart" and "Shop Now," rendered with uppercase Open Sans at 14px/600 weight and a modest {rounded.sm} corner. On hover the fill deepens to #d4a800; disabled state bleaches to #f5e282 with muted text, preserving the amber hue family without implying interactivity.

**`button-inquiry`** — The blue inquiry button (#006799) handles the dominant conversion action for vintage pieces: "Make an Inquiry" or "Contact About This Item." It sits visually distinct from the amber primary, signaling a different mode — direct seller communication rather than cart checkout. Hover brightens to #2ea3f2.

**`button-secondary`** — White fill with a #006799 border and matching text, used for secondary actions like "View Details" or "Save to Wishlist." Hover background shifts to {colors.surface-soft} to signal activity without color clash. Height and padding match `button-primary` for consistent row alignment.

### Product Card

**`product-card`** — The core browse unit: a light gray (#f3f3f3) card with a 4:3 image at top, 1px hairline border, and {rounded.sm} corners. Title renders in `{typography.title-sm}` (16px/600), price in `{typography.price-display}` (20px/700), and a one-line material/era descriptor in `{typography.body-sm}` muted (#555555). Badge overlays (Sold, New, style tags) float at top-left of the image. Hover elevates with a faint box-shadow and border shifts to the muted blue-gray (#bcc8c9).

### Badges

**`badge-sold`** — Direct red (#cc1818) pill with white uppercase text, overlaid at top-left of the product image. Unambiguous and non-decorative — it stops the eye fast.

**`badge-new`** — Amber-gold (#efc01d) fill with dark text, for recently added inventory. Uses the same {rounded.xs} corner as `badge-sold` to keep badge shapes consistent across the grid.

**`badge-style`** — Amber-soft (#f0b849) fill for style/period labels like "Mid-Century Modern" or "Danish Modern" when used as an overlay tag rather than a filter chip.

### Navigation

**`nav-bar`** — White canvas, 70px tall, bottom hairline border. Logo left, primary nav links centered or left-grouped, search icon and cart right. Nav links at 14px/600 Open Sans, ink color, hover to #006799. On scroll, a subtle box-shadow replaces the hairline to mark the fixed position.

### Search

**`search-bar`** — Inset magnifying glass icon (16px, muted-soft), Open Sans body-md type, 1px hairline border, focus ring shifts to {colors.accent-blue}. Sits in the nav on desktop; expands to full-width on mobile below the logo bar.

### Hero Banner

**`hero-banner`** — Full-width photographic hero with a 25% dark scrim (rgba(47,47,47,0.25)) over inventory photography. Heading in `{typography.display-xl}` (36px/700), subhead in `{typography.body-md}` muted. CTA button cluster uses both `button-primary` and `button-inquiry` side by side at {spacing.lg} gap. On mobile collapses to stacked text with image below.

### Category Chips

**`category-chip`** / **`category-chip-active`** — Horizontal scrolling filter row below hero. Inactive chips: surface-soft fill, hairline border, muted uppercase badge text, {rounded.full} pill shape. Active chips flip to amber-gold (#efc01d) fill with dark text, no border. This is the primary use of the brand amber at UI scale.

### Product Gallery

**`product-gallery`** — Main image at {rounded.sm}, thumbnail row below at {rounded.xs}. Active thumbnail gets a 2px amber (#efc01d) border; inactive thumbnails hold a 2px hairline border. Background of the gallery area is surface-soft to separate it from the white page canvas.

### Inquiry Form

**`inquiry-form`** — Light card ({colors.surface-card}, {rounded.md}, 1px hairline border) containing name, email, phone, and message fields with a full-width `button-inquiry` at bottom. Used on product detail pages for pieces where direct seller communication is the conversion action. Heading runs `{typography.title-md}`.

### Section Heading

**`section-heading`** — Display-sm (22px/600) ink-colored heading with a 3px amber underline accent below the text, spanning approximately 48px. Used to introduce grid sections like "Recently Added" and "Danish Teak Collection."

### Breadcrumb

**`breadcrumb`** — Caption-scale (12px/400) muted text, chevron separators in #bbbbbb, links in #006799 with hover to #2ea3f2. Sits flush-left above product title on detail pages.

### Footer

**`footer`** — Dark charcoal (#43454b) panel with a 3px amber (#efc01d) top accent stripe, the one moment where the amber reads as structural rather than interactive. Heading text in `{typography.title-sm}` at #eeeeee; body copy in `{typography.body-sm}`; links in accent-blue-light (#52acf8) brightening to white on hover. Organized in a 3–4 column grid on desktop, single column stack on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in drawer; hero collapses to text-above / image-below stack; category chip row scrolls horizontally; search bar full-width below logo |
| Tablet | 744–1128px | 2-column product grid; nav condenses to logo + icons (search, cart, hamburger); hero image returns to side-by-side or background treatment; inquiry form moves below gallery |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with text links; hero full-bleed with overlay text; category chip row wraps or scrolls; section headings with amber underline prominent |
| Wide | > 1440px | Max-width container (~1400px) centered on page; 4–5 column grid possible; hero gains more vertical height; footer columns expand with more padding |

### Touch Targets

- All buttons minimum 44px height to meet tap target guidelines
- Category chips minimum 36px height with adequate horizontal padding
- Nav drawer links minimum 48px tall on mobile
- Thumbnail images in gallery minimum 60×60px tap area
- Form inputs 42px height for comfortable mobile entry

### Collapsing Strategy

- Nav collapses to hamburger at < 744px; drawer slides from left with full category tree
- Hero CTA buttons stack vertically on mobile with full width
- Product card image maintains 4:3 ratio at all breakpoints; card becomes full-width column on mobile
- Inquiry form moves from sidebar to below gallery on tablet and mobile
- Footer columns stack to single column on mobile; amber top stripe preserved
- Search expands from icon to full input bar on mobile via tap; no persistent bar at narrow width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed custom brand typeface; Open Sans is the best candidate from extracted stacks but Divi builder often overrides with its own defaults — actual heading font may differ from body
- Color extraction pulled many Gutenberg block editor defaults (#00d084, #4ab866, #f78da7, #cd2653, #cf2e2e, #0693e3) and WordPress admin blues (#0073aa, #007cba) that are unlikely to be brand colors; palette inference relies on the most distinctive non-system hues
- Golden amber (#efc01d, #f0b849) interpreted as brand accent based on distinctiveness; site may use blue (#006799 / #2ea3f2) as the actual primary button color with amber as a secondary accent — actual CTA button color unconfirmed
- No meta theme-color set, reducing confidence in primary brand color signal
- ETmodules icon font is Elegant Themes / Divi proprietary; icon set and sizing are builder-dependent and may not reflect bespoke design decisions
- No extracted animation, transition, or motion tokens — Divi builder defaults (0.3s ease) assumed
- Hover, focus, and active states for product images (zoom, overlay, quick-view) not extractable from static snapshot
- Mobile navigation drawer behavior and animation are Divi builder defaults; custom behavior unknown
