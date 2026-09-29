---
version: alpha
name: "Cocokind"
source_url: "https://www.cocokind.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Cocokind is a clean, sensitive-skin-first skincare brand that feels like a gentle morning ritual — soft, warm, and deeply intentional. The canvas is a creamy off-white (#f7f4ec) that reads more like unbleached cotton than sterile white, while the primary brand voltage comes from a muted terracotta (#cd3b1f) that appears on CTAs, badges, and ingredient callouts without ever feeling aggressive. Supporting accents drift into sage (#2d4e46), blush (#e56b54), and a pale peach (#fcc89b) that echo the brand's plant-based, "skin-cycling" philosophy. Typography runs Aktiv Grotesk Corp for headlines and Libre Franklin for body — both clean, slightly warm humanist sans-serifs that avoid the cold precision of typical beauty brands. Buttons use soft 8px radii (`{rounded.sm}`) and generous padding, while product cards and ingredient badges lean into 12px corners (`{rounded.md}`) that feel tactile but not pillowy. The overall mood is "apothecary meets modern minimalism" — there is no hard black anywhere; even the ink (#121212) is a softened near-black, and the hairline (#dedede) is barely there. Signature moves include a persistent top nav with a search bar that collapses to an icon on mobile, a hero section that pairs a single product shot with a warm gradient overlay (#fdf2d9 to #f7f4e9), and a footer that uses the sage green (#2d4e46) as a grounding anchor. The brand trusts negative space, soft shadows, and ingredient photography over heavy typography or flashy animations.

colors:
  primary: "#cd3b1f"
  primary-active: "#8b0000"
  primary-disabled: "#fcc89b"
  ink: "#121212"
  body: "#282828"
  muted: "#6c757d"
  muted-soft: "#979797"
  hairline: "#dedede"
  hairline-soft: "#ebe6d8"
  canvas: "#f7f4ec"
  surface-soft: "#f5f2eb"
  surface-card: "#fffbf5"
  on-primary: "#ffffff"
  accent-sage: "#2d4e46"
  accent-sage-light: "#3f7467"
  accent-blush: "#e56b54"
  accent-peach: "#fcc89b"
  accent-gold: "#ffce31"
  accent-mint: "#bae1d8"
  star-rating: "#ffce31"
  error: "#dc3545"
  info: "#17a2b8"
  badge-new: "#cd3b1f"
  badge-sale: "#8b0000"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Aktiv Grotesk Corp', 'Libre Franklin', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Aktiv Grotesk Corp', 'Libre Franklin', sans-serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Aktiv Grotesk Corp', 'Libre Franklin', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Aktiv Grotesk Corp', 'Libre Franklin', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Aktiv Grotesk Corp', 'Libre Franklin', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Aktiv Grotesk Corp', 'Libre Franklin', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Libre Franklin', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Aktiv Grotesk Corp', 'Libre Franklin', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Aktiv Grotesk Corp', 'Libre Franklin', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Aktiv Grotesk Corp', 'Libre Franklin', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Aktiv Grotesk Corp', 'Libre Franklin', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
  link:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Aktiv Grotesk Corp', 'Libre Franklin', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
    padding: 14px 28px
    height: 48px
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
    border: "2px solid {colors.hairline}"
    padding: 12px 26px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-sage:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-sage-active:
    backgroundColor: "{colors.accent-sage-light}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
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
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.error}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.error}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    gradient: "linear-gradient(180deg, {colors.accent-peach} 0%, {colors.surface-soft} 100%)"
    padding: "{spacing.section} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    shadow: "0 2px 8px rgba(18, 18, 18, 0.06)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    shadow: "0 4px 16px rgba(18, 18, 18, 0.1)"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-vegan:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} {spacing.base}"
  accordion-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    color: "{colors.on-primary}"
    opacity: 1
  ingredient-list:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  ingredient-highlight:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's terracotta (#cd3b1f) with white text and soft 8px corners. On hover, it deepens to a dark red (#8b0000) for clear feedback. When disabled, it fades to a pale peach (#fcc89b) with muted text, signaling non-interactivity without visual noise. Used for "Add to Cart", "Subscribe", and "Shop Now" actions.

**`button-secondary`** — An outlined variant on the warm canvas background (#f7f4ec) with a thin hairline border (#dedede). On hover, the border thickens to the ink color (#121212) and the background shifts to the soft surface tone (#f5f2eb). Used for "Learn More", "View Ingredients", and secondary checkout actions.

**`button-tertiary-text`** — A text-only button with no background or border, used for "Cancel", "Clear Filters", and "Read More" links within cards and accordions. The text remains the ink color (#121212) and relies on the typography's weight for hierarchy.

**`button-sage`** — A secondary brand button using the sage green (#2d4e46) for actions related to sustainability, subscriptions, or "Our Mission" CTAs. On hover, it shifts to a lighter sage (#3f7467). This button lives primarily in the footer and on product detail pages.

**`button-pill`** — A fully rounded pill button used for filter tags, "Quick Add" on product cards, and mobile sticky CTAs. Uses the primary terracotta with smaller typography and tighter padding.

### Cards
**`product-card`** — The primary product display unit, rendered on a warm white surface (#fffbf5) with a subtle shadow (0 2px 8px rgba(18, 18, 18, 0.06)) and 12px rounded corners. The image area maintains a 1:1 aspect ratio with matching corner radius. On hover, the shadow deepens (0 4px 16px rgba(18, 18, 18, 0.1)) to signal interactivity. Contains the product image, name, price, star rating, and up to two badges.

**`product-badge`** — Small uppercase badges that sit overlaid on product card images. Three variants exist: "NEW" in terracotta (#cd3b1f), "SALE" in dark red (#8b0000), and "VEGAN" in sage (#2d4e46). All use 4px corners, tight padding, and bold 11px type.

### Navigation
**`top-nav`** — A fixed 72px navigation bar on the warm canvas background (#f7f4ec). Contains the brand logo, nav links (Shop, Learn, About, Rewards), a search bar that collapses to an icon on mobile, a cart icon with badge count, and a user account icon. Active nav links are underlined with a 2px terracotta border.

**`search-bar`** — A full-width pill-shaped search input on the soft surface (#f5f2eb) with 44px height. On focus, the background shifts to white and a 2px terracotta border appears. The placeholder text reads "Search products..." in the muted color (#6c757d).

### Forms
**`text-input`** — Standard form inputs with a white background, 1px hairline border (#dedede), and 8px corners. On focus, the border becomes 2px terracotta. Error states use a 2px red (#dc3545) border and the error text appears below in the same red. Used for email signup, checkout forms, and account creation.

**`quantity-selector`** — A compact 40px tall input with minus/plus buttons flanking a numeric display. Uses a thin hairline border and the button-sm typography. The active state highlights the border in terracotta.

### Footer
**`footer`** — A full-width footer anchored in the sage green (#2d4e46) with white text at 85% opacity. Contains four columns: Shop, Learn, Support, and Social. Links lighten to full opacity on hover. The bottom bar includes copyright, privacy policy, and terms of service links. Padding is generous at 48px top/bottom and 24px sides.

### Accordion
**`accordion`** — Collapsible sections used on product detail pages for "Ingredients", "How to Use", and "Shipping & Returns". Each section has a white background, 1px soft hairline border (#ebe6d8), and 8px corners. When expanded, the background shifts to the soft surface (#f5f2eb) and the border becomes terracotta. The header uses title-sm typography with a chevron icon that rotates on open.

### Ingredient List
**`ingredient-list`** — A dedicated component for displaying full ingredient lists on product pages. Uses the soft surface background (#f5f2eb) with 8px corners and body-sm typography. Key ingredients (like "Aloe Vera", "Vitamin C", "Hyaluronic Acid") are highlighted with a mint green (#bae1d8) badge for quick scanning.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), top-nav collapses to hamburger menu, search bar becomes an icon-only button, hero section reduces padding to 32px, footer stacks to single column, accordions are full-width without side padding |
| Tablet | 744–1128px | Two-column product grid (2 cards per row), top-nav shows 4 links with a "More" dropdown, search bar is a compact pill with icon, hero section uses 48px padding, footer shows 2 columns |
| Desktop | 1128–1440px | Three-column product grid (3 cards per row), full top-nav with all links visible, search bar is full-width pill, hero section uses 64px padding, footer shows 4 columns |
| Wide | > 1440px | Four-column product grid (4 cards per row), max-width container at 1440px centered, top-nav and footer have increased horizontal padding to 48px, hero section uses 80px padding |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain a minimum 44x44px touch target on mobile
- Product card tap targets are the entire card surface, not just the CTA button
- Accordion headers are 48px tall for easy tapping
- Quantity selector buttons are 44x44px on mobile
- Bottom nav bar (mobile) uses 56px height for thumb-friendly access

### Collapsing Strategy
- Top nav collapses to a hamburger menu on mobile, with a slide-in drawer from the left
- Search bar collapses to a magnifying glass icon on mobile, expanding to full-screen overlay on tap
- Product filters collapse to a bottom sheet on mobile, with a "Filter" button that shows active count
- Footer columns collapse to a single column on mobile, with accordion-style section headers
- Hero section collapses to a single image with text overlay on mobile, removing the gradient background
- Product image galleries collapse to a single swipeable carousel on mobile, removing thumbnails

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card badges (currently only defined for the card itself)
- Error styling for text-input beyond the border color (no error icon or helper text pattern defined)
- Sub-brand palettes for limited edition collections or seasonal drops
- Dark mode color tokens (the brand currently only operates in light mode)
- Focus ring styles for keyboard navigation (no outline or ring token defined)
- Loading states for buttons (spinner or skeleton pattern not extracted)
- Toast/notification component styling (success, error, warning variants)
- Modal/dialog overlay styling (background scrim opacity and animation)
- Dropdown menu styling for the tablet "More" nav item
- Mobile bottom nav bar styling (icon sizes, active indicator, background color)
- Animation tokens (transition durations, easing curves, transform properties)
- Shopify-specific cart drawer styling (slide-in animation, header, footer with totals)
- Product variant selector styling (swatch circles, dropdown, size picker)
- Review component styling (star rating size, review card layout, pagination)
- Newsletter signup form styling (inline vs stacked, error/success states)
- Accessibility contrast ratios (some muted colors may not meet WCAG AA on certain backgrounds)
