---
version: alpha
name: "Arcade1Up"
source_url: "https://www.arcade1up.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A neon-lit arcade revival brand that uses deep navy-black (#0d0c1a) as its canvas and a punchy cobalt (#2c56ee) as its primary voltage — the same blue that fires every "Add to Cart" button, PDP accent bar, and category strip. The palette reads like a CRT glow: #006fcf and #3982b6 provide secondary digital depth, while #fb5b75 (a hot pink) cuts through as a limited-edition accent for special-edition cabinets and sale badges. Typography runs Poppins at medium weights (500–600) rather than heavy 700+, letting the product photography — full-bleed cabinet hero shots with neon bezels — carry the visual weight. Buttons are sharp-cornered rectangles (`{rounded.sm}`) with 48px height, a deliberate contrast to the pill-shaped search bars and rounded product cards (`{rounded.md}}`) that soften the experience. The top nav is a fixed 64px bar with a bold logo lockup and category links (Arcade, Pinball, Accessories) in white on the dark canvas, creating a storefront that feels like walking into a Dave & Buster's lobby — bright, loud, and unapologetically nostalgic.

colors:
  primary: "#2c56ee"
  primary-active: "#1a3db5"
  primary-disabled: "#8a9ef5"
  ink: "#0d0c1a"
  body: "#232323"
  muted: "#242424"
  muted-soft: "#3982b6"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-pink: "#fb5b75"
  accent-blue-dark: "#006fcf"
  accent-blue-mid: "#3783c5"
  accent-blue-light: "#3982b6"
  sale-badge: "#fb5b75"
  limited-edition: "#621620"
  dark-bg: "#0d0c1a"
  dark-surface: "#121212"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  price:
    fontFamily: "'Poppins', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-accent-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: "8px {spacing.md}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    height: 44px
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    shadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    shadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.md} {spacing.md} 0"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    padding: "0 {spacing.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-limited:
    backgroundColor: "{colors.limited-edition}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-strip:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: "{spacing.md} {spacing.lg}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: "8px {spacing.md}"
    rounded: "{rounded.sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.md}"
  hero-banner:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
    hoverColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
    marginBottom: "{spacing.md}"
  newsletter-input:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
    padding: "10px 14px"
    height: 44px
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.md} {spacing.base}"
  accordion-content:
    padding: "{spacing.base}"
    typography: "{typography.body-sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a solid cobalt (#2c56ee) rectangle with white text and 8px rounded corners. Used for "Add to Cart", "Pre-Order", and primary PDP actions. On hover, shifts to `{colors.primary-active}` (#1a3db5); disabled state uses `{colors.primary-disabled}` (#8a9ef5). Height is fixed at 48px with 12px vertical padding for comfortable tap targets.

**`button-secondary`** — An outlined variant with a white fill and 2px cobalt border. Used for "Learn More", "View Details", and secondary PDP actions. Active state darkens the border to `{colors.primary-active}`. Matches the primary button's 48px height and 8px radius for visual consistency.

**`button-accent-pink`** — A hot pink (#fb5b75) variant reserved for limited-edition cabinet launches, flash sales, and promotional CTAs. Same dimensions and radius as `button-primary`. Creates urgency without competing with the primary cobalt.

**`button-dark`** — A dark background (#0d0c1a) button with white text, used on light sections or as a secondary CTA in hero banners. Maintains the same 48px height and 8px radius.

### Cards
**`product-card`** — A white card with 12px rounded corners and a subtle shadow (0 2px 8px rgba(0,0,0,0.08)). The image area occupies the top with a 4:3 aspect ratio and rounded top corners. Title uses `{typography.title-sm}` in `{colors.ink}`, price uses `{typography.price}` (22px, bold). Badges overlay the image: sale badges in `{colors.accent-pink}`, limited-edition badges in `{colors.limited-edition}` (#621620). On hover, shadow deepens to 0 4px 16px rgba(0,0,0,0.12).

**`product-card-badge`** — Small uppercase label (11px, 600 weight, 0.5px letter spacing) with 4px rounded corners. Sale badges use the hot pink background; limited-edition badges use a deep maroon (#621620). Positioned absolutely over the product image, typically top-left.

### Navigation
**`nav-bar`** — A fixed 64px bar on a deep navy-black (#0d0c1a) background. Contains the Arcade1Up logo (white, bold) on the left, category links (Arcade, Pinball, Accessories, Sale) in white `{typography.nav-link}` (15px, 600 weight), and a search icon on the right. Active category links get a 2px cobalt underline. The bar uses `{spacing.lg}` horizontal padding.

**`category-strip`** — A secondary navigation strip below the hero, also on dark background. Category tabs are pill-shaped with 8px radius. Active tab fills with `{colors.primary}`; inactive tabs are transparent with white text. Used for filtering product categories on collection pages.

### Forms
**`text-input`** — Standard input field with white background, 1px hairline border (#dedede), and 8px rounded corners. On focus, border thickens to 2px cobalt (#2c56ee). Height is 44px with 10px vertical padding. Used for email capture, search, and form fields.

**`search-bar`** — A pill-shaped (full radius) search input with white background and 1px hairline border. On focus, border switches to 2px cobalt. Height is 44px with 10px vertical padding and 20px horizontal padding for comfortable typing.

**`newsletter-input`** — Dark-themed input for the footer, using `{colors.dark-surface}` (#121212) background and white text. 1px muted border (#242424), 8px radius. Paired with `newsletter-submit` — a cobalt button that matches the input's 44px height.

### Footer
**`footer`** — A full-width dark section (#0d0c1a) with white text. Contains column headings in `{typography.title-sm}` and links in `{typography.link}` (14px, 400 weight). Link hover color shifts to `{colors.primary}`. Includes a newsletter signup row with the dark-themed input and cobalt submit button. Padding uses `{spacing.xxl}` vertical and `{spacing.lg}` horizontal.

### Accordion
**`accordion`** — Collapsible sections with white background, 1px hairline border, and 8px rounded corners. Header uses `{typography.title-sm}` in `{colors.ink}` with `{spacing.md}` vertical padding. Content area uses `{typography.body-sm}` with `{spacing.base}` padding. Used for FAQ sections and product specifications.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 column), hamburger nav replaces category strip, hero banner reduces to 48px padding, product cards stack full-width, footer collapses to single column, search bar becomes icon-only |
| Tablet | 744–1128px | Two-column product grid (2 columns), category strip scrolls horizontally, hero banner uses 32px padding, footer uses 2-column layout, search bar remains full |
| Desktop | 1128–1440px | Three-column product grid (3 columns), full category strip visible, hero banner uses 64px padding, footer uses 4-column layout, full search bar with autocomplete |
| Wide | > 1440px | Four-column product grid (4 columns), max-width container (1440px) centered, hero banner uses 80px padding, footer uses 4-column layout with wider spacing |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (48px preferred for primary actions)
- Product card tap targets (title, price, CTA) are at least 44px tall
- Category tabs in mobile strip have 44px minimum width
- Search bar maintains 44px height across all breakpoints
- Footer links have 44px minimum tap area (padding ensures this)
- Accordion headers are 48px tall for easy tapping

### Collapsing Strategy
- Top nav collapses to hamburger menu on mobile (< 744px), with slide-out drawer for category links
- Category strip becomes horizontally scrollable on tablet and mobile, with arrow indicators
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer collapses from 4 columns to 2 columns on tablet, single column on mobile
- Hero banner reduces vertical padding from 64px to 48px on tablet, 32px on mobile
- Search bar collapses to icon-only on mobile, expanding to full input on tap
- Product card badges stack vertically on mobile if multiple badges exist
- Accordion sections are collapsed by default on all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card badges and footer links were inferred from common patterns; actual hover colors not extracted
- Error styling for form inputs (validation colors, error messages) not observed on live site
- Sub-brand palettes (e.g., Pinball, Accessories) may use distinct accent colors not captured in extraction
- Dark mode variant not present on live site; all pages use light canvas with dark nav/footer
- Loading states (skeleton screens, spinners) not extracted
- Modal/dialog styling (e.g., quick-view, cart drawer) not observed
- Animation timing and easing curves not extracted
- Focus-visible ring styles for keyboard navigation not observed
- Sale badge positioning (exact offset from card edge) not extracted
- Newsletter success/error states not observed
- Mobile nav drawer animation and overlay styling not extracted
- Product card "Compare" or "Wishlist" icon states not observed
- Secondary button hover state (background fill vs. border only) inferred from common patterns
- Price strikethrough styling for sale items not extracted
- Star rating component styling not observed on live site
- Video player styling (for product demos) not extracted
