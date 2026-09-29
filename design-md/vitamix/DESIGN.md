---
version: alpha
name: "Vitamix"
source_url: "https://www.vitamix.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Vitamix speaks in the language of professional-grade power and culinary precision, wrapped in a palette that feels both aspirational and approachable. The brand's visual identity is anchored by a deep, confident ink (#222222) that carries headlines and primary navigation, while body text settles into a slightly softer charcoal (#3f3f3f) for extended reading. The canvas is a clean, bright white (#ffffff) that lets product photography and the signature blend of vibrant ingredient colors take center stage. Muted tones (#6a6a6a) and soft hairlines (#dddddd) create subtle structure without competing with the hero imagery of blenders in action. Typography is a deliberate mix of heritage and modernism: Sentinel, a sturdy slab serif, is used for display headings that evoke the brand's 100-year legacy of engineering excellence, while Gotham Narrow provides a clean, efficient sans-serif for body copy and UI elements. The design system relies on generous whitespace, large product imagery, and a restrained use of color — there is no single brand accent color screaming for attention; instead, the system trusts the natural vibrancy of fresh ingredients and the polished stainless steel of the machines themselves. Buttons and interactive elements use the ink color for primary actions, creating a no-nonsense, utilitarian feel that says "this tool means business." Rounded corners are present but modest — `{rounded.sm}` (8px) on cards and `{rounded.md}` (12px) on buttons — never veering into the overly friendly pill shapes of consumer lifestyle brands. The overall mood is one of quiet confidence: this is a brand for serious home cooks and professionals who value performance over flash.

colors:
  primary: "#222222"
  primary-active: "#000000"
  primary-disabled: "#c1c1c1"
  ink: "#222222"
  body: "#3f3f3f"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dddddd"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#c13515"
  accent-green: "#2e7d32"
  badge-new: "#222222"
  badge-sale: "#c13515"
  star-rating: "#222222"
  scrim: "#000000"
  footer-bg: "#222222"
  footer-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Sentinel', 'sentinel-fallback', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Sentinel', 'sentinel-fallback', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Sentinel', 'sentinel-fallback', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Sentinel', 'sentinel-fallback', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Gotham Narrow', 'gotham-narrow-fallback', Helvetica, Arial, sans-serif"
    fontSize: 10px
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
    rounded: "{rounded.none}"
    padding: 16px 32px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 15px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
    height: auto
  button-tertiary-active:
    textColor: "{colors.primary-active}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 36px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    height: 36px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 40px 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 700
  product-card-badge:
    typography: "{typography.badge}"
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 480px
  hero-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "16px 32px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.muted-soft}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.footer-text}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.muted}"
  breadcrumb-link-hover:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    margin: "0 {spacing.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a solid black rectangle with white uppercase Gotham Narrow text. Used for high-commitment actions like "Add to Cart" and "Shop Now." On hover, the background shifts to pure black (`{colors.primary-active}`). The disabled state uses a light gray (`{colors.primary-disabled}`) background with white text, signaling the action is unavailable. No rounded corners — the straight edge reinforces the brand's no-nonsense, professional tool aesthetic.

**`button-secondary`** — An outlined variant with a white fill and a 2px solid black border. Used for secondary actions like "Learn More" or "View Details." On hover, the background fills with the soft surface color (`{colors.surface-soft}`). The disabled state mirrors the primary disabled pattern but with a gray border. The uppercase label maintains the same weight and tracking as the primary button.

**`button-tertiary`** — A text-only link styled as a button, used for low-commitment actions like "Cancel" or "See All." No background or border — just the uppercase label in black. On hover, the text color shifts to pure black. The lack of padding means it can sit inline with body copy or in tight UI spaces.

**`button-pill`** — A fully rounded variant used for filters, tags, and category selectors. Solid black fill with white uppercase text in the smaller button size. The pill shape is the only place where Vitamix uses fully rounded corners, creating a subtle visual distinction for secondary interactive elements.

### Cards
**`product-card`** — The primary content container for product listings, featuring a white background, subtle drop shadow (`{boxShadow}`), and softly rounded corners (`{rounded.sm}`). The card image sits at the top with its own rounded top corners, while the content area below holds the product name in Sentinel display-sm, the price in bold Gotham Narrow, and optional badges. On hover, the shadow deepens to indicate interactivity. Badges are rendered as small black rectangles with white uppercase text, positioned over the top-left of the image.

**`hero`** — A full-width, large-format banner section with a minimum height of 480px. The background uses the soft surface color (`{colors.surface-soft}`) to create contrast for product imagery. Headlines use the Sentinel display-xl typeface at 48px, conveying heritage and authority. A dark scrim overlay (`{colors.scrim}` at 30% opacity) can be applied over background images to ensure text readability. The primary CTA button sits prominently within the hero, using the standard button-primary styling.

### Navigation
**`nav-bar`** — A fixed-height (64px) top navigation bar with a white background and a subtle bottom border. Navigation links use Gotham Narrow uppercase at 14px with 700 weight and 0.5px letter spacing. The active link is indicated by a 2px solid black bottom border. On scroll, the nav bar gains a subtle box shadow (`{boxShadow}`) to create visual separation from the page content. The bar contains the brand logo on the left, primary navigation links in the center, and utility icons (search, account, cart) on the right.

### Forms
**`text-input`** — A standard text input field with a white background, 1px solid hairline border, and no rounded corners. The input uses Gotham Narrow body-md for user-entered text. On focus, the border thickens to 2px solid black. Error states use a 2px solid red border (`{colors.accent-red}`). The height is fixed at 48px to match button heights for consistent form layouts.

**`select-input`** — A dropdown select field that mirrors the text-input styling but includes a 40px right padding to accommodate a custom dropdown arrow icon. The same focus and error states apply.

### Footer
**`footer`** — A full-width dark section with a black background (`{colors.footer-bg}`) and white text. Section padding uses the `{spacing.section}` token (64px) on top and bottom. Column headings use the title-sm uppercase Gotham Narrow style, while links use the standard link typography in white. On hover, footer links fade to the soft muted color (`{colors.muted-soft}`). The footer typically contains brand information, product categories, support links, and legal text.

### Accordion
**`accordion`** — A vertically stacked content disclosure component used for FAQs and product specifications. Each accordion item has a white background, a bottom border separator, and a clickable header using the title-sm uppercase style. The content area collapses and expands with a smooth animation. No rounded corners — the straight lines and sharp edges maintain the brand's professional, industrial feel.

### Badges
**`product-card-badge`** — Small rectangular labels positioned over product images to indicate status (New, Sale, Best Seller). They use the badge typography (10px uppercase Gotham Narrow) with a black background and white text. No rounded corners. The badge is typically placed at the top-left of the product image with 8px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layouts; nav collapses to hamburger menu; product cards stack vertically; hero height reduces to 320px; footer columns stack; accordion becomes default for all content sections; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grids; nav links may wrap to two rows; hero maintains 400px height; footer uses 2-column grid; side panels (cart, search) become slide-in overlays |
| Desktop | 1128–1440px | Three-column product grids; full nav bar visible; hero at 480px; footer uses 4-column grid; product detail pages show two-column layout with images and specs side by side |
| Wide | > 1440px | Max-width container (1440px) centered; product grids expand to 4 columns; hero may include full-bleed imagery; additional whitespace on left and right margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px on mobile devices
- Nav bar hamburger icon is 48x48px for easy tapping
- Product card CTAs are full-width on mobile for easier tapping
- Accordion headers have 48px minimum height for touch interaction
- Filter pills are 36px tall with 24px horizontal padding for comfortable tapping

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Multi-column footers collapse to stacked single-column on mobile
- Product image galleries switch from thumbnails to swipeable dots on mobile
- Side panels (cart, search) become full-screen overlays on mobile
- Breadcrumb trails truncate with "..." on mobile, showing only the current page and parent

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links are inferred from common patterns but not directly extracted from the live site
- Error state styling for forms (colors, icons, message placement) is not confirmed from the live site
- Sub-brand palettes (Vitamix Professional, Vitamix Commercial) may use different accent colors not captured here
- Dark mode styling is not present on the current site and is not defined
- Animation timing and easing curves (transitions, hover effects) are not extracted
- Focus ring styling for keyboard navigation is not confirmed
- Loading states (skeleton screens, spinners) are not defined
- Modal/dialog styling (overlay opacity, close button placement) is not extracted
- Tooltip and popover styling is not present in the extracted data
- The exact shade of accent red (`{colors.accent-red}`) and green (`{colors.accent-green}`) are inferred from common e-commerce patterns rather than extracted from the site
- Star rating component size and spacing are based on standard implementations, not site-specific measurements
- The `{boxShadow}` token values for product cards are estimated based on common design system patterns
