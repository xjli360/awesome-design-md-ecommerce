---
version: alpha
name: "Kali Audio"
source_url: "https://www.kaliaudio.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep midnight canvas (#111111) and a single neon accent (#0099e5) define Kali Audio — a pro-audio monitor brand that treats its interface like a recording console: dark, legible, and utterly secondary to the sound. The brand's primary blue (#0099e5) appears sparingly — a CTA button, a product badge, a hover state — never decorative, always functional, like a channel-strip mute button that glows when engaged. Typography runs Montserrat at modest weights (400–600), set at 14–16px for body copy, with display sizes rarely exceeding 24px; the brand trusts product photography and spec sheets over typographic heroics. Cards and buttons use {rounded.sm} (8px) — a subtle softening that keeps the interface approachable without sacrificing the precision implied by studio monitors. The color palette is overwhelmingly dark: three blacks (#111111, #1e1e1e, #272727) create layered depth on surfaces, while #fafafa and #fbfbfb provide high-contrast text on dark backgrounds. Social icons and payment badges introduce a secondary palette of blues (#3b5998, #55acee, #1ab7ea) and a single pink (#f94877) that reads as a third-party widget rather than brand expression. The overall effect is a site that feels like a control room at night — dark, focused, with only the essential controls illuminated.

colors:
  primary: "#0099e5"
  primary-active: "#0077b3"
  primary-disabled: "#66c4f0"
  ink: "#111111"
  body: "#1e1e1e"
  muted: "#aaaaaa"
  muted-soft: "#cccccc"
  hairline: "#272727"
  hairline-soft: "#3a3a3a"
  canvas: "#111111"
  surface-soft: "#1e1e1e"
  surface-card: "#272727"
  on-primary: "#ffffff"
  on-dark: "#fafafa"
  accent-pink: "#f94877"
  accent-facebook: "#3b5998"
  accent-twitter: "#55acee"
  accent-instagram: "#e4405f"
  accent-youtube: "#cc2127"
  accent-spotify: "#84bd00"
  error: "#bd0000"
  error-soft: "#e99292"
  star-rating: "#ff6600"

typography:
  display-xl:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-icon-square:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    height: 44px
    width: 44px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.error}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-sale:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: 80px 0
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  social-icon-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  search-bar-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in {colors.primary} (#0099e5) with white text and {rounded.sm} corners. On hover, shifts to {colors.primary-active} (#0077b3). Disabled state uses {colors.primary-disabled} (#66c4f0). Uppercase Montserrat at 14px/600 weight gives it a precise, professional feel appropriate for audio gear. Height is 44px with 12px/24px padding.

**`button-secondary`** — A dark surface button on {colors.surface-card} (#272727) with a {colors.hairline} (#272727) border that reads as a subtle outline. On hover, the border swaps to {colors.primary} (#0099e5), creating a glow-like effect against the dark background. Same typography and dimensions as primary.

**`button-tertiary-text`** — A text-only button in {colors.primary} (#0099e5) with transparent background. Used for "Learn More" and "View All" links within product cards and sections. No border, no padding — just the blue text on dark canvas.

### Cards
**`product-card`** — A dark card on {colors.surface-card} (#272727) with {rounded.sm} corners and 16px padding. On hover, a 1px {colors.primary} (#0099e5) border appears, creating a subtle selection state. Body text runs {typography.body-sm} (14px) in {colors.on-dark} (#fafafa). Used for monitor product listings, spec summaries, and accessory displays.

**`product-badge`** — A small {rounded.xs} badge in {colors.primary} (#0099e5) with white text. Uppercase 11px/600 weight Montserrat with 0.5px letter-spacing. Used for "NEW", "BEST SELLER", and "IN STOCK" labels. A sale variant uses {colors.accent-pink} (#f94877) for urgency.

### Navigation
**`nav-bar`** — A fixed 72px header on {colors.canvas} (#111111) with uppercase nav links in {colors.on-dark} (#fafafa). Active links switch to {colors.primary} (#0099e5). Inactive links render in {colors.muted} (#aaaaaa). The dark background and uppercase typography create a professional, studio-console aesthetic.

**`nav-link-active`** / **`nav-link-inactive`** — Active links use {colors.primary} (#0099e5) text on transparent background. Inactive links use {colors.muted} (#aaaaaa). Both use {typography.nav-link} (14px/500 weight, uppercase, 0.5px letter-spacing).

### Forms
**`text-input`** — A dark input field on {colors.surface-soft} (#1e1e1e) with a {colors.hairline} (#272727) border and {rounded.sm} corners. On focus, the border switches to {colors.primary} (#0099e5). Error state uses {colors.error} (#bd0000) border. Height is 48px with 12px/16px padding. Body text runs {typography.body-md} (16px).

**`search-bar`** — A compact 40px search input on {colors.surface-soft} (#1e1e1e) with {rounded.sm} corners. Placeholder text in {colors.muted} (#aaaaaa). On focus, a {colors.primary} (#0099e5) border appears. Used for site-wide product search and filter bars.

### Footer
**`footer-section`** — A dark footer on {colors.ink} (#111111) with 48px vertical padding. Links render in {colors.muted} (#aaaaaa) and hover to {colors.primary} (#0099e5). Social icons are 36px circles with {rounded.full} corners, defaulting to {colors.muted} and hovering to {colors.primary}.

**`social-icon`** / **`social-icon-hover`** — Circular 36px icons with transparent background. Default state uses {colors.muted} (#aaaaaa) for the icon color. On hover, switches to {colors.primary} (#0099e5). Used for Facebook, Twitter, Instagram, YouTube, and Spotify links in the footer.

### Accordion
**`accordion-header`** — A clickable header on {colors.surface-soft} (#1e1e1e) with {rounded.sm} corners and 16px padding. Uses {typography.title-sm} (16px/500 weight). The dark background creates clear section breaks in FAQ and product spec lists.

**`accordion-body`** — The expandable content area on {colors.canvas} (#111111) with 16px padding. Uses {typography.body-sm} (14px) for readable spec details and descriptions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to {typography.display-md} (24px); buttons go full-width; footer links stack |
| Tablet | 744–1128px | Two-column product grid; nav links visible (no hamburger); hero uses {typography.display-lg} (28px); side-by-side form fields; footer in 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero uses {typography.display-xl} (36px); multi-column footer; product cards show hover border states |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to 4 columns; hero section uses larger padding (100px); all elements scale proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (WCAG 2.1 touch target compliance)
- Nav links have 44px minimum tap area even when text is smaller
- Social icons are 36px with 44px tap area through padding
- Accordion headers have 48px minimum tap height
- Form inputs are 48px tall for comfortable mobile interaction

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product grid reduces from 3 columns to 2 at tablet, 1 at mobile
- Hero section reduces font size and padding at each breakpoint
- Footer reduces from 4-column to 2-column at tablet, single column at mobile
- Search bar moves from inline to full-width below 744px
- Product badges stack vertically on mobile cards

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary and secondary button hover states could be reliably extracted. Card hover, link hover, and other interactive states are inferred from common patterns.
- **Error styling**: Error state for text inputs is defined but error messages, validation patterns, and form-level error containers are not confirmed from the live site.
- **Dark mode**: The site already uses a dark canvas (#111111), so a separate dark mode may not exist. No light mode variant was detected.
- **Sub-brand palettes**: Kali Audio may have sub-brand or product-line-specific colors (e.g., for the IN-UNF series) that were not extracted.
- **Payment widget colors**: The extracted palette includes many social media and payment gateway colors (#3b5998, #55acee, #1ab7ea, #e4405f, #cc2127, #84bd00) that are not brand colors. These have been noted as accents but their exact usage context is unknown.
- **Typography hierarchy**: Font sizes and weights are inferred from common Montserrat usage patterns. Exact responsive typography scales and line-height variations across breakpoints are not confirmed.
- **Spacing system**: The spacing scale is a standard 4px/8px system. Brand-specific spacing values (e.g., product card gaps, section padding) are approximated from common e-commerce patterns.
- **Animation and transitions**: No transition durations, easing functions, or animation patterns were extracted. Hover states likely use a 150-200ms ease-in-out transition.
- **Focus states**: Keyboard focus indicators and outline styles were not extracted from the live site.
- **Loading states**: Skeleton screens, spinners, and loading indicators are not documented.
