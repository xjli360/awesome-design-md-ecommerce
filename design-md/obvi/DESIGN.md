---
version: alpha
name: "Obvi"
source_url: "https://myobvi.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A vibrant, body-positive supplement brand that wraps its purple core (#492f8b) in a confetti of hot pink (#fc89e2), coral (#ffb0d3), peach (#ffd3bc), and marigold (#ffca56), creating a visual language that feels more like a beauty brand than a vitamin company. The deep violet primary sits on a near-white canvas (#fbfaff) with a soft lavender glow (#e9ccff) used as surface washes and badge backgrounds, while a sharp red (#ff2857) cuts through as the accent for urgency badges, sale tags, and limited-edition drops. The typography runs Poppins at 500–700 weight — a geometric sans-serif with generous apertures that reads friendly at small sizes and confident at display scale — with ITC Avant Garde Gothic Pro appearing in hero headlines and badge labels for a retro-modern editorial feel. Buttons are pill-shaped (`{rounded.full}`) with 48px height and 24px horizontal padding, the primary CTA sitting in deep purple with white text, while secondary actions invert to white with purple text and a 1.5px hairline border. Product cards use a white surface (`{surface-card}`) with soft shadow and `{rounded.lg}` corners, each containing a circular swatch ring for flavor variants and a bold price badge in the accent red. The brand leans heavily on gradient overlays — purple-to-pink (#492f8b → #fc89e2) on hero imagery, and a warm coral-to-peach (#ffb0d3 → #ffd3bc) on testimonials — giving the site a glossy, editorial energy that feels closer to Glossier or ColourPop than to traditional supplement retailers like GNC or Thorne. The footer stacks four columns of links in `{body-sm}` on a deep purple background (#492f8b) with white text, punctuated by social icon circles in the brand pink (#fc89e2). Every interaction — hover, active, focus — is accompanied by a subtle scale transform (1.02x) and a 200ms ease-out, making the interface feel responsive and playful without being distracting.

colors:
  primary: "#492f8b"
  primary-active: "#3f2021"
  primary-disabled: "#d3d3d3"
  primary-error-text: "#e22120"
  ink: "#1f2937"
  body: "#3f2021"
  muted: "#707070"
  muted-soft: "#d1d5db"
  hairline: "#d3d3d3"
  hairline-soft: "#f2f2f2"
  canvas: "#fbfaff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-pink: "#fc89e2"
  accent-coral: "#ffb0d3"
  accent-peach: "#ffd3bc"
  accent-marigold: "#ffca56"
  accent-red: "#ff2857"
  accent-lavender: "#e9ccff"
  accent-green: "#33dfab"
  accent-teal: "#10c6c6"
  accent-burgundy: "#8e001f"
  accent-gold: "#bc8100"
  accent-forest: "#10694e"
  accent-deep-purple: "#7800bf"
  accent-sky: "#f0f9ff"
  accent-warm-gray: "#ee907b"
  accent-dark-bg: "#0d0819"
  star-rating: "#ffca56"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'ITC Avant Garde Gothic Pro', 'Poppins', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Poppins', 'ITC Avant Garde Gothic Pro', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'ITC Avant Garde Gothic Pro', 'Poppins', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
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
    rounded: "{rounded.full}"
    padding: 12px 24px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.primary-active}"
  button-accent-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  button-pill-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1.5px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary-error-text}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.primary-error-text}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    height: 64px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0px
    boxShadow: "0 4px 12px rgba(73,47,139,0.08)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 8px 24px rgba(73,47,139,0.12)"
    transform: "scale(1.02)"
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.sm}"
  flavor-swatch-ring:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  flavor-swatch-ring-selected:
    border: "2px solid {colors.primary}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-bestseller:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    gradient: "linear-gradient(135deg, {colors.primary} 0%, {colors.accent-pink} 100%)"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subheadline:
    typography: "{typography.display-sm}"
    textColor: "{colors.on-primary}"
    opacity: 0.9
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.06)"
  testimonial-card-accent:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    borderLeft: "4px solid {colors.accent-coral}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1.5px solid {colors.hairline}"
  search-bar-focus:
    border: "1.5px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(73,47,139,0.15)"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
    opacity: 0.85
  footer-link-hover:
    opacity: 1
  social-icon-circle:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    width: 40px
    height: 40px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.full}"
    height: 40px
    padding: "0 4px"
  quantity-button:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.full}"
    width: 32px
    height: 32px
  accordion-trigger:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "0 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a full pill in deep purple (#492f8b) with white text in Poppins 600 at 16px. On hover, the background shifts to a darker burgundy (#3f2021) with a subtle scale transform (1.02x) over 200ms ease-out. The disabled state drops to gray (#d3d3d3) with muted text, signaling non-interactivity. Used for "Add to Cart", "Subscribe & Save", and "Shop Now" actions.

**`button-secondary`** — An inverted pill with white fill, purple text, and a 1.5px purple border. Active state darkens the border and text to the burgundy active color. Used for "Learn More", "View Details", and secondary checkout options. Maintains the same 48px height and 24px horizontal padding as the primary for visual consistency.

**`button-accent-pink`** — A hot pink (#fc89e2) pill with dark text for playful, brand-forward CTAs like "Get the Glow" or "Try the Bundle". Shares the same dimensions as primary but uses the brand's signature pink as its fill color, often appearing in hero sections and promotional banners.

**`button-accent-red`** — A smaller, urgent pill in sharp red (#ff2857) with white text, used exclusively for limited-time offers, flash sales, and countdown-driven CTAs. At 36px height with 8px vertical padding, it's intentionally compact to fit within price badges and announcement bars.

### Cards
**`product-card`** — The primary product display unit, a white card with soft rounded corners (`{rounded.lg}`) and a subtle purple-tinted shadow (rgba(73,47,139,0.08)). The card contains a square aspect-ratio image at the top with rounded top corners, followed by the product title in `{typography.title-sm}`, the price in bold `{body-md}`, and a row of circular flavor swatch rings. On hover, the shadow deepens and the card scales up 1.02x, creating a tactile lift effect. The image area may also display a gradient overlay on hover showing the product name in white.

**`testimonial-card`** — A white card with `{rounded.lg}` and standard shadow for customer reviews. An accent variant adds a 4px coral (#ffb0d3) left border to visually distinguish featured or verified-purchase testimonials. Star ratings render in marigold (#ffca56) at 16px.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on a near-white canvas (#fbfaff) with a soft bottom border. Contains the brand logo (typically the Obvi wordmark in purple or a stylized "O" icon), a center-aligned row of nav links in Poppins 500 at 15px, and right-aligned icons for search, account, and cart. On scroll, the bar shrinks to 64px, gains a white background, and picks up a subtle drop shadow. The cart icon displays a badge count in the accent red (#ff2857).

### Forms
**`text-input`** — Standard input fields with white fill, 1.5px gray border, and `{rounded.md}` corners. On focus, the border shifts to purple (#492f8b) with a 3px purple glow ring (rgba(73,47,139,0.15)). Error state shows a red border (#e22120) with red text for the error message below. Disabled inputs use a soft gray background (#f7f7f7) with muted text. Used across checkout, account forms, and the search bar.

### Badges
**`badge-sale`** — A compact red (#ff2857) badge with white uppercase text in ITC Avant Garde Gothic Pro at 10px. Used for percentage-off or "SALE" labels on product cards and collection pages. Rendered with `{rounded.sm}` and 2px vertical padding.

**`badge-new`** — A green (#33dfab) badge with dark text for new product arrivals. Shares the same typography and dimensions as the sale badge but uses the brand's accent green to signal freshness rather than urgency.

**`badge-bestseller`** — A lavender (#e9ccff) badge with purple (#492f8b) text for top-selling products. This badge uses the brand's softest accent color to avoid competing with the primary purple while still drawing attention.

### Footer
**`footer`** — A full-width deep purple (#492f8b) section with white text, organized into four columns of links in `{body-sm}`. Each link has 0.85 opacity at rest and full opacity on hover. Social media icons sit in hot pink (#fc89e2) circles at 40px diameter, creating a vibrant punctuation at the bottom of the page. The footer also contains the brand's tagline, copyright notice, and legal links in smaller caption text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav replaces full nav links, hero text shrinks to 28px, footer collapses to single column, buttons go full-width |
| Tablet | 744–1128px | Two-column product grid, nav links condensed to 4 items, hero maintains 36px headline, footer splits to 2 columns |
| Desktop | 1128–1440px | Three-column product grid, full nav links visible, hero at 48px headline, footer at 4 columns |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero may include full-bleed imagery |

### Touch Targets
- All interactive elements maintain minimum 44px height for touch accessibility
- Product card tap targets (swatch rings, add-to-cart) are at least 48px
- Nav bar hamburger icon is 48x48px
- Quantity selector buttons are 40x40px
- Social icon circles are 40x40px

### Collapsing Strategy
- Top nav links collapse into a hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Footer columns stack to single column below 744px
- Hero section reduces vertical padding from 64px to 32px on mobile
- Multi-step checkout collapses to single-page accordion on mobile
- Product image gallery switches from thumbnail strip to swipeable carousel on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components were inferred from common patterns; exact extracted values for `:hover`, `:focus`, and `:active` states are not available from the static extraction
- Error state styling for forms (validation messages, error icons) was not extracted — red hex (#e22120) is present in the palette but its exact usage context is assumed
- Dark mode is not supported and no dark-mode-specific colors were found in the extraction
- Sub-brand or collection-specific palettes (e.g., "Obvi Collagen", "Obvi Greens") may exist but were not distinguishable from the single-site extraction
- Animation timing values (200ms ease-out scale transform) are based on observed behavior, not extracted CSS
- The gradient overlay hex values for hero sections (#492f8b → #fc89e2 and #ffb0d3 → #ffd3bc) are inferred from the palette; exact gradient stops and angles were not extracted
- Shopify checkout widget colors (Klarna, Afterpay, Shop Pay) were filtered from the palette but may appear in the live site's checkout flow
- The `ITC Avant Garde Gothic Pro` font family was found in the extraction but its exact usage weight and size contexts (likely hero headlines and badges) are assumed based on industry patterns
- Star rating component color (#ffca56) is assumed from the marigold accent; exact rating display component structure was not extracted
- Quantity selector and accordion component details are based on common supplement e-commerce patterns, not extracted markup
