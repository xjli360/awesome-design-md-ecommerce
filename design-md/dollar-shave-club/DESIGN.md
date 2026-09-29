---
version: alpha
name: "Dollar Shave Club"
source_url: "https://www.dollarshaveclub.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A direct-to-consumer grooming brand that weaponizes a high-voltage orange #fe5000 against a deep navy #142978, creating a visual tension that mirrors the brand's irreverent, no-BS voice. The palette is intentionally noisy — a lime green #7fb800, a cyan #52c9ff, a yellow #ffb400 — all competing for attention on a mostly white canvas, as if the brand can't be bothered to curate. Type runs Assistant at modest weights, with the occasional "DSC Specter" headline that feels like a flex, a proprietary move that signals "we're not just another subscription box." Buttons are pill-shaped ({rounded.full}), product cards are softly rounded ({rounded.md} ~12px), and the entire system reads as approachable, slightly chaotic, and deliberately un-precious. The navy #142978 anchors the footer and secondary CTAs, while the orange #fe5000 is the primary voltage — the "Join" button, the "Shop Now" trigger, the accent that says "click here, you know you want to." There's a warmth to the palette that feels more like a clubhouse than a corporate brand, and the typography follows suit: clean, readable, but never stiff.

colors:
  primary: "#fe5000"
  primary-active: "#f6511d"
  primary-disabled: "#dadada"
  ink: "#121212"
  body: "#242833"
  muted: "#404040"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5ecdf"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  navy: "#142978"
  navy-dark: "#15263f"
  navy-light: "#1c2f80"
  cyan: "#52c9ff"
  cyan-light: "#83d8ff"
  cyan-dark: "#1990c6"
  cyan-deeper: "#136f99"
  lime: "#7fb800"
  yellow: "#ffb400"
  yellow-light: "#fde74c"
  yellow-bright: "#ffe31b"
  yellow-muted: "#e2ca23"
  yellow-dark: "#d49600"
  beige: "#efe0ca"
  beige-light: "#f5ecdf"
  burgundy: "#82163f"
  lavender: "#be92be"
  gray-light: "#cacaca"
  gray-soft: "#e2e2e2"
  blue-bright: "#03a9f4"
  blue-muted: "#dbebf5"

typography:
  display-xl:
    fontFamily: "'DSC Specter', Assistant, -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DSC Specter', Assistant, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DSC Specter', Assistant, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'DSC Specter', Assistant, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "Assistant, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Assistant, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Assistant, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Assistant, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Assistant, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Assistant, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-lg:
    fontFamily: "Assistant, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-md:
    fontFamily: "Assistant, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Assistant, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "Assistant, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "Assistant, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "Assistant, sans-serif"
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
    textColor: "{colors.navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.navy}"
  button-secondary-active:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.navy}"
    typography: "{typography.button-md}"
  button-cta-large:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 18px 40px
    height: 56px
  button-pill-cyan:
    backgroundColor: "{colors.cyan}"
    textColor: "{colors.navy}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-lime:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.navy}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.navy}"
    borderBottom: "2px solid {colors.navy}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  product-card-badge-sale:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  product-card-badge-new:
    backgroundColor: "{colors.cyan}"
    textColor: "{colors.navy}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-cta:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 18px 40px
    height: 56px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.navy}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.cyan-light}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.cyan}"
  badge-accent:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-accent-bright:
    backgroundColor: "{colors.yellow-bright}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-accent-dark:
    backgroundColor: "{colors.yellow-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-burgundy:
    backgroundColor: "{colors.burgundy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-lavender:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.full}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} 0"
  category-tab-active:
    textColor: "{colors.navy}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.navy}"
  category-tab-inactive:
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.md} {spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature orange #fe5000 with white text and a pill shape ({rounded.full}). Used for "Join DSC", "Shop Now", and "Get Started" actions. On hover, shifts to a slightly deeper orange #f6511d. Disabled state uses a muted gray #dadada with muted text.

**`button-secondary`** — An outlined variant with a navy #142978 border and text on a white background. Used for secondary actions like "Learn More" or "View Details". On hover, fills with navy and inverts to white text. Maintains the same pill shape and height as the primary button for visual consistency.

**`button-cta-large`** — A larger, more prominent version of the primary button, used in hero sections and high-visibility conversion points. Uses 18px bold type and increased padding (18px 40px) for a 56px height. Always orange #fe5000 with white text.

**`button-pill-cyan`** and **`button-pill-lime`** — Smaller accent buttons used for promotional badges, category filters, or secondary CTAs. Cyan #52c9ff and lime #7fb800 respectively, both with navy or white text. These add the brand's playful, slightly chaotic energy to the interface.

### Cards
**`product-card`** — The primary product display unit, a white card with 12px rounded corners ({rounded.md}) and 16px padding. Contains a square image (1:1 aspect ratio, 8px rounded), product name, price, and a navy CTA button. On hover, lifts with a subtle box-shadow (0 4px 12px rgba(0,0,0,0.08)).

**`product-card-badge`** — Small pill-shaped badges overlaid on product cards. Three variants: standard orange (#fe5000) for general promotions, lime (#7fb800) for sale items, and cyan (#52c9ff) for new arrivals. All use 11px bold uppercase type.

### Navigation
**`nav-bar`** — A fixed top navigation bar, 64px tall, white background with a subtle bottom border. Contains the DSC logo, nav links in 15px semi-bold, and a cart icon. Active nav links are underlined with a 2px navy border. The bar collapses to a hamburger menu on mobile.

**`category-strip`** — A horizontal scrollable strip of category tabs (e.g., "Razors", "Shave", "Hair", "Skin") below the nav bar. Active tab is underlined in navy; inactive tabs are muted gray. On mobile, this strip scrolls horizontally with touch.

### Forms
**`text-input`** — Standard text input with white background, 8px rounded corners, and a 1px hairline border. On focus, gains a 2px navy border. Error state uses a 2px orange border. Used for email signups, search, and account forms.

**`search-bar`** — A pill-shaped search input with 48px height, used in the nav bar and hero sections. On focus, the border switches to navy. Placeholder text is muted gray.

### Footer
**`footer`** — A full-width navy (#142978) footer with white text and cyan (#52c9ff) links. Contains columns for product categories, company info, support, and social links. Links hover to a brighter cyan. The footer uses 14px body text and generous padding (48px top/bottom).

### Badges
**`badge-accent`** — Yellow (#ffb400) badges used for limited-time offers, flash sales, or promotional tags. A brighter variant (#ffe31b) is used for high-visibility promotions, and a darker variant (#d49600) for more subdued labels. All use 11px bold uppercase type with pill shapes.

**`badge-burgundy`** and **`badge-lavender`** — Additional accent badges for special collections or limited editions. Burgundy (#82163f) and lavender (#be92be) add variety to the badge system while maintaining the brand's playful, slightly chaotic palette.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger nav, stacked product cards (2 columns), reduced hero padding, search bar moves to nav overlay |
| Tablet | 744–1128px | Two-column product grid, expanded nav links, hero section with side-by-side content, category strip scrollable |
| Desktop | 1128–1440px | Three-column product grid, full nav bar, hero with large imagery, multi-column footer |
| Wide | > 1440px | Max-width container (1440px) centered, four-column product grid, expanded whitespace |

### Touch Targets
- All buttons and interactive elements minimum 44px height (48px standard)
- Icon buttons minimum 40px height
- Product card CTAs minimum 40px height
- Nav links minimum 44px tap area
- Category strip tabs minimum 44px height

### Collapsing Strategy
- Nav bar collapses to hamburger menu below 744px
- Product grid collapses from 4 columns to 3 to 2 to 1 (mobile)
- Footer columns collapse to stacked layout below 744px
- Category strip becomes horizontally scrollable on mobile
- Hero section stacks content vertically below 744px
- Search bar collapses to icon-only on mobile, expands on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards and buttons are inferred from common patterns; exact box-shadow values and transition durations not extracted
- Error styling for forms (text-input-error) is assumed based on brand colors; actual error messages and validation patterns not observed
- Dark mode is not implemented; no dark palette tokens exist on the live site
- Sub-brand or collection-specific palettes (e.g., limited edition drops) not captured
- Exact font weights for "DSC Specter" are inferred; the font family was found with `!important` in CSS but specific weight declarations were not extracted
- Animation durations, easing curves, and micro-interactions not documented
- Loading states, skeleton screens, and empty states not observed
- Modal, tooltip, and dropdown component styles not extracted
- Accessibility contrast ratios not verified against WCAG standards
- The meta theme-color was not set, suggesting no browser chrome color customization
- Some hex colors (e.g., #03a9f4, #dbebf5) may be used in specific promotional contexts rather than core system tokens
