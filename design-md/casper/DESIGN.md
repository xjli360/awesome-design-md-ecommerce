---
version: alpha
name: "Casper"
source_url: "https://casper.com"
captured_at: "2026-09-28T04:10:40.945444+00:00"
evidence_status: "historical_partial_css_evidence"
description: |-
  A sleep-first brand that wraps its promise of better rest in a palette of deep, trustworthy blues and warm, accent-driven energy. The primary blue `#1e306e` reads like a midnight sky — confident, calm, and premium — while `#4e63df` adds a brighter, more electric secondary voltage for interactive moments. Accents of `#8533fc` (a vivid purple) and `#ffce33` (a warm, buttery yellow) punctuate the interface like bedside lamps or sunrise glints, preventing the navy-heavy system from feeling cold or corporate. The canvas is pure white `#ffffff`, with soft surfaces in `#dedede` and `#d5dae3` that keep the experience airy and approachable. Typography leans on Calibre for clean, modern body and button text, while the NewKansas family — in Medium, Regular, SemiBold, and Thin weights — brings a refined, editorial serif voice to display headlines and product titles. The system uses generous `{rounded.sm}` (8px) and `{rounded.md}` (12px) corners on cards and inputs, with `{rounded.full}` reserved for pill-shaped CTAs and search bars, echoing the soft, rounded geometry of a mattress edge. The overall mood is serene but not sleepy — a digital bedroom that feels both luxurious and accessible, where every `{colors.primary}` button and `{colors.ink}` text block is designed to guide you toward a purchase without urgency.

colors:
  primary: "#1e306e"
  primary-active: "#0d0d2a"
  primary-disabled: "#d4d8ef"
  ink: "#121212"
  body: "#242445"
  muted: "#acacac"
  muted-soft: "#d5dae3"
  hairline: "#dedede"
  hairline-soft: "#d5dae3"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-purple: "#8533fc"
  accent-yellow: "#ffce33"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  star-rating: "#ffce33"

typography:
  display-xl:
    fontFamily: "'NewKansas-Medium', 'NewKansas-Regular', Georgia, serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'NewKansas-Medium', 'NewKansas-Regular', Georgia, serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'NewKansas-Medium', 'NewKansas-Regular', Georgia, serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'NewKansas-Medium', 'NewKansas-Regular', Georgia, serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Calibre', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Calibre', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Calibre', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Calibre', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Calibre', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Calibre', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Calibre', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Calibre', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Calibre', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Calibre', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
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
    padding: 14px 24px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-purple}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
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
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 32px"
    height: 56px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.on-primary}"
  accordion-trigger:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Casper experience. Rendered in the brand's deep navy `{colors.primary}` with white text, it uses `{typography.button-md}` at 600 weight with subtle letter-spacing for a clean, confident feel. On hover or active, it shifts to `{colors.primary-active}` for a darker, more grounded state. When disabled, it fades to `{colors.primary-disabled}` with muted text, signaling unavailability without visual noise.

**`button-secondary`** — An outlined alternative for less prominent actions. White background with a 2px `{colors.primary}` border and navy text. On active, the border and text deepen to `{colors.primary-active}` and the background shifts to `{colors.surface-soft}`. Ideal for "Learn More" or "Compare" links alongside primary CTAs.

**`button-pill`** — A fully rounded, compact CTA used for promotional banners, sticky footers, and mobile navigation. Uses `{rounded.full}` for a friendly, approachable silhouette. The outline variant (`button-pill-outline`) uses a thin `{colors.hairline}` border and dark text for secondary promotions.

### Cards
**`product-card`** — The core product display unit for mattresses, pillows, and bedding. A white card with `{rounded.md}` corners and `{spacing.base}` padding. The image area uses `{rounded.sm}` to soften the photography. The title uses `{typography.title-sm}` in `{colors.ink}`, while the price is set in `{typography.body-md}` in `{colors.body}`. A `product-card-badge` in `{colors.accent-yellow}` with uppercase `{typography.badge}` text can overlay for promotions like "20% Off" or "Best Seller."

**`review-card`** — A bordered card for customer testimonials. White background with a soft `{colors.hairline-soft}` border and `{rounded.md}` corners. Contains star ratings in `{colors.star-rating}` (the warm yellow `#ffce33`), a short quote in `{typography.body-sm}`, and optional reviewer attribution. Padding is generous at `{spacing.lg}` for comfortable reading.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on white `{colors.canvas}`. Links use `{typography.nav-link}` at 15px with 500 weight. On scroll, a subtle `boxShadow` appears for depth. The bar contains the Casper logo (left), nav links (center), and utility icons (cart, account — right). Mobile collapses to a hamburger menu.

**`footer-section`** — A dark footer using `{colors.primary-active}` as the background, with white text and muted `{colors.muted-soft}` links. Links lighten to `{colors.on-primary}` on hover. The section uses `{spacing.section}` padding top and bottom, with columns for product links, support, and legal.

### Forms
**`text-input`** — Standard input fields for forms (newsletter signup, checkout, contact). White background, `{rounded.sm}` corners, 48px height, and a `{colors.hairline}` border. On focus, the border thickens to 2px `{colors.primary}`. Error states use a 2px `{colors.accent-purple}` border for clear, accessible feedback.

### Search
**`search-bar`** — A pill-shaped search bar with `{rounded.full}` corners, used on the product listing and help pages. White background with a thin `{colors.hairline}` border. On focus, the border becomes a 2px `{colors.primary}` stroke. Height is 56px for comfortable tap targets on mobile.

### Hero
**`hero-section`** — The primary brand hero, typically featuring a full-width background in `{colors.primary}` with white text. Uses `{typography.display-xl}` for the headline. The hero CTA (`hero-cta`) is a pill button in `{colors.accent-yellow}` with dark text, creating high contrast against the navy backdrop. Padding is `{spacing.section}` top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger; hero font scales down to `{typography.display-md}`; product cards stack vertically; search bar becomes full-width; footer columns stack |
| Tablet | 744–1128px | Two-column grid for product cards; nav-bar shows limited links (Shop, Learn, Support); hero scales to `{typography.display-lg}`; side-by-side review cards |
| Desktop | 1128–1440px | Full nav-bar with all links; three-column product grid; hero at full `{typography.display-xl}`; multi-column footer; search bar centered in nav |
| Wide | > 1440px | Max-width container (1440px) centered; hero background extends full-width; product grid can show 4 columns; increased whitespace around sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for mobile tap targets
- `button-primary`, `button-secondary`, `text-input` all use 48px height
- `search-bar` uses 56px height for comfortable thumb access
- Nav links have 44px minimum tap area, even if text is smaller
- Product card CTAs are at least 44px tall

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, hiding all links except logo and cart icon
- Product grid collapses from 3 columns (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 (desktop) to 2 (tablet) to 1 (mobile), with accordion-style expanders on mobile
- Hero section reduces font size and padding on mobile; CTA remains full-width
- Review cards switch from side-by-side (tablet+) to stacked (mobile)
- Search bar moves from inline in nav (desktop) to a full-width element below the nav (mobile)

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Hover and focus states for all components beyond primary/secondary buttons could not be reliably extracted; assume standard opacity shifts (e.g., 0.9 on hover) where not specified
- Error styling for forms (validation messages, error icons) was not observed; `text-input-error` border color is inferred from accent palette
- Sub-brand or seasonal color palettes (e.g., for "Casper Glow" or "Casper Dog Bed") were not captured
- Dark mode tokens are not present; the system appears to be light-mode only
- Animation durations and easing curves (transitions, hover effects) were not extractable; recommend 200ms ease-in-out as default
- Specific font sizes for `display-xl` and `display-lg` are estimated based on typical editorial serif usage; actual values may vary
- `product-card-badge` positioning (top-left, top-right) and z-index were not determined
- Footer link hover color is inferred from contrast needs; actual value may differ
- Star rating component size (16px) is a reasonable default; actual SVG dimensions may vary
- `nav-bar-scrolled` boxShadow value is a common pattern; exact spread and opacity not confirmed
