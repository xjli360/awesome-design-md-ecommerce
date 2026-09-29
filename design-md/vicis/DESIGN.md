---
version: alpha
name: "Vicis"
source_url: "https://vicis.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A football-equipment brand that uses a deep teal (#108474) as its primary voltage — not the expected helmet gray or team-color red, but a cool, medical-grade green that signals protection and precision before aggression. The brand's typographic voice runs on the Shapiro family, a condensed sans-serif with extreme weight variance: Shapiro 95 Super Extd for heroic display headlines that stretch across hero banners, and Shapiro 35 Feather for delicate captions that feel almost weightless. The extracted palette is unusually broad — 30+ colors — but the core system resolves around two grays (#292929 for ink, #323e48 for body), a soft blue-gray (#bbc1e1) for secondary surfaces, and a single alert red (#ff3b3a) that appears only in sale badges and error states. The Shopify platform layer contributes several checkout blues (#409eff, #275efe) and a bright accent green (#03de90) likely from progress indicators. Vicis's design language is clinical and protective: rounded corners are generous ({rounded.md} at 12px on cards, {rounded.lg} at 20px on buttons), whitespace is abundant, and the overall feel is more medical-device than sports-apparel — a helmet company that wants you to think about safety first, team colors second.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d5cb"
  ink: "#292929"
  body: "#323e48"
  muted: "#7b7b7b"
  muted-soft: "#a6a3a3"
  hairline: "#dadada"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  surface-secondary: "#bbc1e1"
  surface-secondary-soft: "#e1e6f9"
  on-primary: "#ffffff"
  alert-red: "#ff3b3a"
  alert-red-soft: "#f5f9ff"
  sale-badge: "#e22120"
  accent-blue: "#409eff"
  accent-blue-active: "#275efe"
  progress-green: "#03de90"
  gold-accent: "#bc9928"
  orange-accent: "#ff8c00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Shapiro 95 Super Extd', 'Shapiro 75 Heavy Extd', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Shapiro 75 Heavy Extd', 'Shapiro 95 Super Extd', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Shapiro 75 Heavy Extd', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Shapiro 45 Welter', 'Shapiro 45 Welter Extd', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Shapiro 45 Welter', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Shapiro 35 Feather', 'Shapiro 35 Feather Text', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  caption-sm:
    fontFamily: "'Shapiro 35 Feather', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 300
    lineHeight: 1.27
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Shapiro 45 Welter', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Shapiro 45 Welter', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Shapiro 45 Welter', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Shapiro 45 Welter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
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
    rounded: "{rounded.lg}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 13px 31px
    height: 48px
  button-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  text-input-error:
    borderColor: "{colors.alert-red}"
    textColor: "{colors.alert-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  product-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 14px 32px
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-active:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion-trigger:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  rating-stars:
    color: "{colors.gold-accent}"
    size: 16px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    fillColor: "{colors.progress-green}"
    rounded: "{rounded.full}"
    height: 6px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand teal (#108474) with generous 20px rounded corners that soften the clinical feel. Text is set in Shapiro 45 Welter at 15px, uppercase, with 0.5px letter spacing for a deliberate, engineered cadence. On hover, the background deepens to `{colors.primary-active}` (#0d6b5d); disabled state uses `{colors.primary-disabled}` (#a3d5cb) with the same uppercase weight.

**`button-secondary`** — A white button with dark ink text, used for secondary actions like "Learn More" or "View Details." Shares the same 20px rounding and uppercase Shapiro 45 Welter typography as the primary, but the active state shifts to `{colors.surface-soft}` (#f9fafb) for a subtle press effect.

**`button-outline`** — A transparent button with a teal text stroke, used for ghost actions in hero sections or on colored backgrounds. The outline is implied by the text color alone — no visible border — relying on the teal typography and the `{rounded.lg}` shape to signal interactivity.

**`button-sale`** — A compact, urgent button in alert red (#e22120) for sale badges and clearance callouts. Uses smaller 13px uppercase text with 8px padding, keeping the footprint tight while maintaining the brand's signature uppercase voice.

### Cards
**`product-card`** — The primary product display unit, a white card with 12px rounded corners and soft shadow on hover. The image sits flush to the top corners (`{rounded.md} {rounded.md} 0 0`), while product info below uses `{typography.body-sm}` for the name and `{typography.title-md}` for the price. Hover state lifts the card with a 4px/12px shadow.

**`product-badge`** — Small uppercase labels that sit on product images, using the brand's badge typography (11px, uppercase, 0.5px letter spacing). Three variants exist: sale (red `{colors.sale-badge}`), sold-out (gray `{colors.muted}`), and new (teal `{colors.primary}`), each with 4px/8px padding and 8px rounded corners.

### Navigation
**`nav-bar`** — A fixed 72px white bar with uppercase nav links in Shapiro 45 Welter at 14px. On scroll, a subtle 1px/3px shadow appears. The bar remains white throughout, relying on the typography's weight and spacing for hierarchy rather than background color changes.

**`search-bar`** — A pill-shaped input field (`{rounded.full}`) with 48px height, white background, and muted placeholder text. On focus, a teal border with a 2px teal-disabled ring appears, maintaining the brand's clinical precision.

### Forms
**`text-input`** — Standard 48px input fields with 8px rounded corners, white background, and 16px padding. Focus state uses a teal border with a 2px `{colors.primary-disabled}` ring. Error state shifts the border and text to `{colors.alert-red}` (#ff3b3a), the only place this red appears in the system.

**`quantity-selector`** — A compact 40px input for cart quantities, with 8px rounded corners and 8px/12px padding. Uses the same body typography as standard inputs but at a smaller footprint.

### Footer
**`footer-section`** — A dark section in `{colors.ink}` (#292929) with white text, using 64px vertical padding. Links render in `{colors.muted-soft}` (#a6a3a3) and shift to white on hover. The footer is the only place the brand inverts its entire color system, creating a clear visual boundary at the page's end.

### Interactive Elements
**`accordion-trigger`** — Expandable sections (FAQ, product details) use a soft gray trigger (`{colors.surface-soft}`) with 8px rounded corners and 16px/24px padding. Content panels below use white background with the same padding, creating a clean accordion stack.

**`rating-stars`** — A 5-star display in gold (#bc9928) at 16px, used on product cards and reviews. The gold is the only warm accent in the palette, standing out against the cool teal and blue-gray system.

**`progress-bar`** — A 6px tall pill-shaped bar in `{colors.hairline}` (#dadada) with a bright green fill (`{colors.progress-green}`, #03de90) for checkout steps or loading states. The green is likely inherited from Shopify's progress components but fits the brand's medical-precision aesthetic.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to `{typography.display-md}` (28px); buttons go full-width; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses `{typography.display-lg}` (36px); search bar shrinks to icon-only |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at `{typography.display-xl}` (48px); search bar full-width |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero text scales up to 56px; additional whitespace in margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product cards have 48px minimum touch area for "Add to Cart" buttons
- Accordion triggers are 48px+ tall for easy tapping
- Nav links on mobile have 48px tap targets

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Search bar collapses to icon-only on tablet, expands on tap
- Product filters collapse to a "Filter" button on mobile, opening a drawer
- Footer link columns stack vertically below 744px
- Hero sections stack image below text on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states for all components** — Only primary button and product card hover states were extractable; secondary, outline, and link hover states are inferred from common patterns
- **Error and validation styling** — Only text-input error state was visible; form-level error banners, success messages, and tooltip styling are unknown
- **Dark mode** — No evidence of dark mode support; the brand's white canvas and dark footer suggest a light-only system
- **Sub-brand palettes** — Vicis may have team-specific or product-line-specific color variants (e.g., ZERO1 vs. TRENCH helmets) that weren't visible
- **Animation and transition tokens** — Duration, easing, and motion patterns were not extractable; the site uses standard CSS transitions
- **Icon system** — No icon set was visible beyond Shopify's default cart and search icons; custom iconography may exist
- **Typography scale gaps** — Font sizes for display-2xl, display-sm, and title-sm were not found; the scale above uses the most common sizes from the live site
- **Checkout-specific styling** — Shopify checkout uses its own theme (#409eff, #275efe, #03de90) that may not reflect Vicis's brand system
- **Rating/review widget** — JudgemeStar font suggests a third-party review system; its exact styling tokens are unknown
- **Print styles** — No print-specific CSS was detected
