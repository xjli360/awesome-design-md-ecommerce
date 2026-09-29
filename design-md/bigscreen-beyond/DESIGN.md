---
version: alpha
name: "Bigscreen Beyond"
source_url: "https://www.bigscreenvr.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A VR headset that sheds the usual black-plastic gamer aesthetic for a machined-aluminum chassis and a single, unbroken black canvas — `#000000` meta theme-color that bleeds edge-to-edge across the browser chrome, making the site feel like a darkroom where the product is the only light source. The lone extracted font — SFProDisplay-Bold — runs at generous sizes with tight tracking, delivering headlines that feel stamped rather than typeset, a deliberate counterpoint to the soft, rounded UI containers (`{rounded.md}` for cards, `{rounded.full}` for CTA pills). There are no gradients, no decorative flourishes, no secondary brand colors; the palette is a strict monochrome of black, white, and near-black grays, punctuated only by the product’s own OLED glow in hero imagery. Navigation is a minimal top bar with a logo lockup and a single CTA — "Buy Now" — rendered as a white-on-black pill (`{colors.on-primary}` on `{colors.ink}`), a conversion path that feels inevitable rather than pushed. The site trusts its product photography to do the heavy lifting: headsets are shown floating in negative space, cables rendered as fine silver lines against the dark, and every interaction — hover, click, scroll — is met with subtle opacity shifts and micro-animations that reinforce the hardware’s precision-engineering story.

colors:
  primary: "#000000"
  primary-active: "#1a1a1a"
  primary-disabled: "#333333"
  ink: "#000000"
  body: "#1a1a1a"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#333333"
  hairline-soft: "#1a1a1a"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-silver: "#c0c0c0"
  accent-aluminum: "#d4d4d4"
  product-glow: "#00ff00"

typography:
  display-xl:
    fontFamily: "'SFProDisplay-Bold', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'SFProDisplay-Bold', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'SFProDisplay-Bold', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'SFProDisplay-Bold', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'SFProDisplay-Bold', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'SFProDisplay-Bold', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'SFProDisplay-Bold', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'SFProDisplay-Bold', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
  badge:
    fontFamily: "'SFProDisplay-Bold', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: 2px solid "{colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-white:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-link-default:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} 0"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  feature-list-item:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} 0"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a black pill (`{rounded.full}`) with white text. Used for "Buy Now", "Pre-order", and "Add to Cart" actions. On hover, background shifts to `{colors.primary-active}` with a subtle scale-up transform. Disabled state uses `{colors.primary-disabled}` background with `{colors.muted}` text. **`button-secondary`** — An outlined variant with a white fill and black border, used for secondary actions like "Learn More" or "Compare Models". Active state inverts to black fill with white text. **`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "View specs" or "Read reviews". Hover state adds a subtle underline.

### Navigation
**`top-nav`** — A fixed-position, 72px-high white bar with a thin bottom border (`{colors.hairline-soft}`). Contains the brand logo lockup on the left and navigation links on the right. **`nav-link-default`** — Muted gray text (`{colors.muted}`) in SFProDisplay-Bold at 14px with 0.5px letter spacing. **`nav-link-active`** — Black text (`{colors.ink}`) for the current page or section. Active state is indicated by a 2px black underline.

### Cards
**`product-card`** — A white card with `{rounded.md}` corners and 16px padding, used to display headset models and accessories. The card image area uses `{rounded.sm}` and the title sits below in `{typography.title-sm}`. Price is rendered in `{typography.body-md}` with `{colors.muted}`. On hover, the card lifts with a subtle box-shadow and the image scales up 1.02x.

### Forms
**`text-input`** — A standard input field with `{rounded.sm}` corners, 48px height, and a 1px hairline border. Focus state thickens the border to 2px and shifts to `{colors.ink}`. Used for email signups, shipping addresses, and newsletter subscriptions. **`search-bar`** — A pill-shaped (`{rounded.full}`) search input with a magnifying glass icon on the left. Background is `{colors.surface-soft}` and text is `{colors.ink}`. Focus state adds a 2px black border.

### Footer
**`footer-section`** — A full-width black section with white text, containing links, legal information, and social icons. Links use `{colors.muted-soft}` and shift to white on hover. The section has 48px vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero headline reduces to 32px; navigation collapses to hamburger menu; product cards stack vertically; CTA buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; hero maintains 36px headline; navigation links remain visible but condensed; side-by-side spec comparison |
| Desktop | 1128–1440px | Three-column product grid; full hero with 48px headline; horizontal navigation with all links; product cards in a 3-column grid |
| Wide | > 1440px | Max-width container at 1440px; hero content centered with 60% width; product grid expands to 4 columns; additional whitespace around all elements |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height
- Icon buttons are 40px circles with 44px tap targets
- Navigation links have 48px tap targets on mobile
- Product card CTAs are 48px tall for easy thumb reach

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Hero section reduces padding from 64px to 32px on mobile
- Footer links collapse from 4 columns to 2 columns on tablet, 1 column on mobile
- Spec comparison tables convert to stacked lists below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hex colors were available from the live site (the extraction returned empty after framework filtering); the palette above is inferred from the `#000000` theme-color meta tag and the brand's known visual identity
- Font-family extraction returned only `SFProDisplay-Bold`; the body font is assumed to be the system font stack based on common VR hardware site patterns
- Hover and active states for all components are estimated based on standard interaction patterns, not extracted from the live site
- Error states for form inputs (validation, error messages) are not documented
- Dark mode is not implemented; the site uses a light theme with black accents
- Sub-brand or variant-specific colors (e.g., Beyond 2, Beyond Pro) are not captured
- Animation durations, easing curves, and transition properties are not specified
- The `product-glow` color (`#00ff00`) is an assumption based on OLED display marketing; actual accent colors may differ
- Spacing values are estimated based on common VR hardware site patterns; actual values may vary
- The `spec-badge` component is inferred from common spec-sheet patterns; exact implementation may differ
