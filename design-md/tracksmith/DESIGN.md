---
version: alpha
name: "Tracksmith"
source_url: "https://www.tracksmith.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A navy-and-brass world where running is treated as a craft, not a sport — #0a1e32 (the deep midnight of a pre-dawn long run) anchors every page, while #9a825c (a burnished brass that could have been pulled from a vintage stopwatch face) provides the single accent voltage. The brand runs on SainteColombe and akzidenz-grotesk-extended, a pairing that feels more like a literary quarterly than an athletic apparel site — serif body text for storytelling, extended grotesk for uppercase section headers that recall old track club letterhead. Product photography is moody and editorial, often shot at golden hour or in rain, with runners who look like they belong to a real club rather than a stock-image agency. The checkout flow uses {rounded.full} buttons in brass on navy, while product cards sit on {colors.canvas} with {colors.hairline} borders and {rounded.sm} corners — the only hard edges are in the typographic grid. Badges appear in {colors.primary} with white text for "New" and "Limited Edition," while sale indicators use a restrained {colors.muted} treatment. The footer is a dense information architecture in {colors.body} on {colors.canvas}, with social links in {colors.muted} that turn {colors.primary} on hover. Every interaction feels deliberate, like a runner checking their split — nothing is rushed, nothing is accidental.

colors:
  primary: "#0a1e32"
  primary-active: "#252c45"
  primary-disabled: "#6c7884"
  ink: "#222222"
  body: "#6f737a"
  muted: "#9ca3af"
  muted-soft: "#c4c0bd"
  hairline: "#ced2d6"
  hairline-soft: "#e6e9eb"
  canvas: "#fefcf9"
  surface-soft: "#f2f3f5"
  surface-card: "#ffffff"
  on-primary: "#fefcf9"
  brass: "#9a825c"
  brass-active: "#857151"
  brass-light: "#cfc2a7"
  accent-red: "#be2624"
  accent-gold: "#e7cf63"
  accent-olive: "#556a63"
  accent-burgundy: "#652631"
  accent-plum: "#45233a"
  accent-navy-light: "#003153"

typography:
  display-xl:
    fontFamily: "'SainteColombe', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'SainteColombe', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'SainteColombe', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'akzidenz-grotesk-extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  title-md:
    fontFamily: "'SainteColombe', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'akzidenz-grotesk-extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'SainteColombe', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'SainteColombe', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'akzidenz-grotesk-extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'akzidenz-grotesk-extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'akzidenz-grotesk-extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  link:
    fontFamily: "'SainteColombe', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'akzidenz-grotesk-extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.5px
    textTransform: uppercase
  badge:
    fontFamily: "'akzidenz-grotesk-extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
  section: 80px

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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-brass:
    backgroundColor: "{colors.brass}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-brass-active:
    backgroundColor: "{colors.brass-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 3px rgba(10, 30, 50, 0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-overlay:
    backgroundColor: "rgba(10, 30, 50, 0.4)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.body}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  social-icon:
    textColor: "{colors.muted}"
  social-icon-hover:
    textColor: "{colors.primary}"
  newsletter-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "10px 24px"
    height: 40px
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The workhorse CTA, a pill-shaped button in deep navy {colors.primary} with white uppercase text set in akzidenz-grotesk-extended. On hover, it shifts to {colors.primary-active} (#252c45) with no border or shadow change — the color darkens subtly, like a runner settling into pace. The disabled state uses {colors.primary-disabled} (#6c7884) with full opacity, signaling unavailability without punishing the eye. Padding is generous at 14px 32px to accommodate the extended grotesk letterforms.

**`button-secondary`** — An outlined variant with a 2px {colors.primary} border on a white canvas. Text matches the border color. On hover, the button fills with {colors.primary} and text flips to white — a clean inversion that feels like crossing a finish line. Same pill shape and typography as primary, but with 13px 31px padding to account for the border.

**`button-brass`** — The accent CTA, used for limited-edition drops, club membership signups, and special collections. Uses {colors.brass} (#9a825c) as background with white text. On hover, it deepens to {colors.brass-active} (#857151). This button is the brand's equivalent of a gold medal — used sparingly, always meaningful.

**`button-text-link`** — A text-only link styled as a button, used in legal text, "Learn More" contexts, and footer navigation. No background, no border, just the serif body type at 16px in {colors.primary}. Underline appears on hover.

### Cards
**`product-card`** — A minimal card with no rounding, no shadow, and no background color beyond white. The product image sits flush to the top edge, full-bleed. Below it, the title appears in akzidenz-grotesk-extended uppercase at 14px, followed by the price in SainteColombe body at 16px in {colors.body}. Badges float over the top-left of the image — {colors.primary} for "New" or "Limited Edition," {colors.accent-red} for sale items. The card has no hover state beyond a subtle opacity shift on the image (0.95). This restraint is intentional: the photography does the selling.

### Navigation
**`nav-bar`** — A 72px white bar with the brand logo left-aligned and nav links in akzidenz-grotesk-extended uppercase at 12px. Links are spaced generously (24px+ gap) and use {colors.primary} as default. On scroll, a faint shadow appears (0 1px 3px rgba(10, 30, 50, 0.08)). The search icon and cart icon sit on the right, both in {colors.primary}. The nav does not collapse into a hamburger until the tablet breakpoint — the brand trusts its typographic density.

### Forms
**`text-input`** — A simple bordered input with 1px {colors.hairline} border, 12px 16px padding, and 48px height. On focus, the border switches to {colors.primary}. Error state uses {colors.accent-red} border. The typography is SainteColombe body at 16px, giving even form fields a literary feel. Placeholder text uses {colors.muted}.

**`newsletter-input`** — A pill-shaped input with {colors.surface-soft} background and {colors.hairline} border, paired with a pill-shaped submit button in {colors.primary}. The input is 48px tall with 12px 24px padding; the submit button is 40px tall with tighter padding. This asymmetry (input taller than button) is a deliberate design choice — the input field is the primary interaction surface.

### Footer
**`footer-section`** — A dense, text-heavy footer with 80px top/bottom padding. Headings use akzidenz-grotesk-extended uppercase at 14px in {colors.ink}. Links use SainteColombe body at 16px in {colors.body}, turning {colors.primary} on hover. Social icons sit in {colors.muted} and turn {colors.primary} on hover. The newsletter signup sits in its own section within the footer, visually separated by a {colors.hairline} divider. Legal text at the bottom uses {typography.caption} in {colors.muted}.

### Badges
**`product-card-badge`** — A small rectangular badge with {rounded.sm} (4px) rounding, 4px 8px padding, and akzidenz-grotesk-extended uppercase at 10px. The default badge uses {colors.primary} background with white text. Sale badges use {colors.accent-red} background. Badges are positioned absolutely over the top-left of product images, with a 8px offset from the edge.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero text reduces to 28px; footer links stack vertically; newsletter becomes full-width |
| Tablet | 744–1128px | Nav remains expanded but with tighter link spacing; product cards in 2-column grid; hero text at 36px; footer in 2-column layout |
| Desktop | 1128–1440px | Full nav with generous spacing; product cards in 3-column grid; hero text at 48px; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px with auto margins; product cards in 4-column grid; hero text at 48px with wider padding |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height
- Nav links have 48px touch area (padding + height)
- Product card tap targets (image, title, price) are the full card width
- Accordion triggers have 48px minimum tap height
- Social icons have 44px touch area

### Collapsing Strategy
- Primary nav collapses to hamburger menu at < 744px
- Product grid reduces columns: 4 → 3 → 2 → 1
- Footer columns collapse: 4 → 2 → 1
- Hero section reduces padding and font size
- Search bar moves from inline to full-width overlay on mobile
- Newsletter input and submit button stack vertically on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (only image opacity shift was extractable; exact transition timing and easing unknown)
- Error message styling for forms (color, typography, icon usage not reliably extracted)
- Focus ring styles (color, width, offset not found in extracted CSS)
- Dark mode palette (no dark mode detected on live site)
- Sub-brand or collection-specific color palettes (e.g., "Twilight" collection may have its own accent)
- Checkout flow styling (Shopify checkout may override brand styles; extracted colors include some checkout-widget colors that were filtered)
- Animation timing and easing curves (no extracted data for transitions or micro-interactions)
- Loading state designs (skeleton screens, shimmer effects not present in extracted data)
- Empty state illustrations or messaging
- Mobile-specific typography adjustments (font sizes may scale differently than desktop)
