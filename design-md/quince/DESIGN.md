---
version: alpha
name: "Quince"
source_url: "https://www.quince.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Quince is a direct-to-consumer essentials brand that delivers luxury-quality goods at radically low prices by cutting out middlemen. The brand's visual language is anchored on a clean, off-white canvas (`#f7f7f5`) that feels tactile and warm, not sterile. Signature moves include a restrained palette where a deep, almost-black ink (`#21201f`) provides high contrast against soft neutrals like `#eeeeec` and `#dfdace`, while a single accent red (`#af3535`) and a muted sage green (`#d0d3bb`) add subtle, earthy notes. Typography leans heavily on serif display faces like Grosa and IvyPresto Headline for editorial headings, paired with a clean sans-serif for body text, creating a sophisticated, magazine-like feel. The design trusts generous whitespace, soft rounded corners (`{rounded.sm}` on cards, `{rounded.full}` on buttons), and high-quality product photography over heavy ornamentation. A secondary warm accent (`#ffa273`) and a deep brown (`#85351b`) appear in lifestyle imagery and badges, reinforcing the brand's natural, understated luxury. The overall mood is calm, trustworthy, and quietly premium — a direct counterpoint to the loud, discount-driven aesthetic of fast fashion.

colors:
  primary: "#21201f"
  primary-active: "#363940"
  primary-disabled: "#d9d9d9"
  ink: "#21201f"
  body: "#363940"
  muted: "#757575"
  muted-soft: "#8f8f8f"
  hairline: "#d3d2d2"
  hairline-soft: "#e9e9e9"
  canvas: "#f7f7f5"
  surface-soft: "#eeeeec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#af3535"
  accent-red-light: "#d24343"
  accent-warm: "#ffa273"
  accent-warm-soft: "#ff8181"
  accent-green: "#2d822b"
  accent-sage: "#d0d3bb"
  accent-brown: "#85351b"
  accent-beige: "#dfdace"
  accent-beige-light: "#e5ccbc"
  accent-blue-light: "#c8d3f1"
  accent-blue-soft: "#e3e9f8"
  off-white: "#fffff0"
  surface-strong: "#f5f5f5"
  border-strong: "#bdbdbc"
  star-rating: "#21201f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Grosa', 'IvyPresto Headline', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Grosa', 'IvyPresto Headline', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Grosa', 'IvyPresto Headline', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Grosa', 'IvyPresto Headline', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Grosa', 'IvyPresto Headline', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Grosa', 'IvyPresto Headline', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'IvyText', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'IvyText', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'IvyText', Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  button-md:
    fontFamily: "'Grosa', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Grosa', Georgia, 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'IvyText', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Grosa', Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Grosa', Georgia, 'Times New Roman', serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-accent:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 36px
  icon-button-circle:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-red}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-red}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-card-rating:
    typography: "{typography.caption}"
    color: "{colors.star-rating}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
  badge-new:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  badge-sustainable:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  footer-heading:
    typography: "{typography.nav-link}"
    color: "{colors.on-primary}"
    marginBottom: "{spacing.md}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button with a deep ink (`#21201f`) background and white text. On hover, it shifts to a slightly lighter dark (`#363940`). The disabled state uses a light gray (`#d9d9d9`) background with muted text (`#757575`). All primary buttons use uppercase Grosa type at 14px with 0.5px letter spacing.

**`button-secondary`** — An outlined variant with a white (`#f7f7f5`) background, ink text, and a 1px ink border. On hover, the background fills with the soft surface tone (`#eeeeec`). Used for "Add to Bag" alternatives and secondary actions.

**`button-tertiary-text`** — A text-only button with no background or border, used for links like "View All" or "Learn More." Inherits the primary ink color and uppercase Grosa styling.

**`button-pill-accent`** — A smaller, accent-driven pill button using the brand red (`#af3535`) for promotional badges or limited-time offers. Uses 12px uppercase Grosa.

### Cards
**`product-card`** — The core product display unit, a white card with soft 8px rounding (`{rounded.sm}`) and 8px padding. Contains a square product image with 4px rounding, a title in 18px serif, a muted price, and a star rating. Cards sit on the off-white canvas (`#f7f7f5`) with generous spacing between them.

### Navigation
**`top-nav`** — A fixed 64px header on the off-white canvas, with a 1px soft hairline bottom border. Navigation links use 13px uppercase Grosa with 0.3px letter spacing. The active state underlines with a 2px ink border. The nav includes a search bar pill and a cart icon button.

### Forms
**`text-input`** — Standard input fields with a white background, 8px rounding, and a 1px hairline (`#d3d2d2`) border. On focus, the border switches to ink (`#21201f`). Error states use the accent red (`#af3535`) border and text.

**`search-bar`** — A full-rounded pill input on a soft surface (`#eeeeec`) background with a hairline border. On focus, it expands to a white background with an ink border.

### Footer
**`footer`** — A deep ink (`#21201f`) footer section with white text. Links are underlined on hover. The footer uses 14px body text for links and 13px uppercase Grosa for section headings. Padding is generous at 64px top/bottom.

### Badges
**`badge-new`** — A small red (`#af3535`) pill badge with white text, used for "New Arrivals" tags. Uses 10px uppercase Grosa with tight padding (4px 8px).

**`badge-sale`** — A warm peach (`#ffa273`) pill badge with ink text, used for sale or markdown items.

**`badge-sustainable`** — A sage green (`#d0d3bb`) pill badge with ink text, used for sustainable or eco-friendly product tags.

### Hero Banner
**`hero-banner`** — A full-width section on a soft surface (`#eeeeec`) background, featuring a large serif headline (36–48px) and a primary CTA button. Padding is 64px on top/bottom and 24px on sides. The banner may include lifestyle imagery behind the text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, collapsed nav into hamburger menu, reduced hero padding to 32px, smaller display fonts (28px), search bar moves to expandable overlay |
| Tablet | 744–1128px | Two-column product grid, nav links partially visible, hero padding at 48px, display fonts scale down slightly |
| Desktop | 1128–1440px | Three-column product grid, full nav visible, standard hero padding (64px), full display typography |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero may use full-bleed imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile.
- Icon buttons (cart, search, menu) are 40x40px minimum.
- Product card tap targets are the full card area.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px).
- Product grid collapses from 4 columns to 1 column on mobile.
- Footer link columns stack vertically on mobile.
- Hero banner text and CTA stack on mobile, with reduced padding.
- Search bar becomes a full-screen overlay on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components beyond primary/secondary buttons could not be reliably extracted.
- Error state styling for forms (validation messages, error icons) is inferred but not confirmed.
- Dark mode palette is not present; the site uses a light-only theme.
- Sub-brand or seasonal color palettes (e.g., holiday, limited edition) are not captured.
- Specific animation durations and easing curves (e.g., button hover transitions, card hover lifts) are not documented.
- Dropdown and modal component styling (background scrim opacity, padding, border-radius) is not fully extracted.
- Checkbox and radio button styling is not captured.
- The exact font-weight mapping for IvyText and Grosa (e.g., 400 vs 500) is inferred from common usage patterns.
- Star rating icon size and spacing is not precisely measured.
- Product card hover state (e.g., image zoom, shadow lift) is not documented.
