---
version: alpha
name: "Made Of"
source_url: "https://madeof.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A baby-care brand that builds its visual identity around a deep teal-green (#108474) — not the pastel pink or powder blue the category defaults to, but a confident, botanical anchor that reads as grown-up and trustworthy. The palette draws from the same naturalist instinct: a warm marigold (#ffcf00) for badges and sale flags, a slate navy (#3c506d) for secondary text and footer blocks, and a soft putty (#f4f2f0) that replaces pure white as the background for product cards and section dividers. The brand uses Fira Sans as its primary typeface — a humanist sans with open apertures and a friendly, legible character — paired with the more decorative Gambado Sans Forte for display headlines and logo marks, giving the site a hand-drawn, editorial feel. Buttons are pill-shaped (`{rounded.full}`), product cards are softly rounded (`{rounded.md}`), and the overall layout breathes with generous padding (`{spacing.lg}` to `{spacing.xxl}`) that keeps the experience calm and uncluttered. The navigation bar sits at 80px with a white canvas and the teal logo, and the search bar mirrors the pill shape of the buttons, creating a consistent, friendly interaction language. The result is a brand that feels less like a baby store and more like a modern home-goods or wellness site — deliberate, warm, and visually sophisticated, with a color story that signals safety and quality without resorting to cliché.

colors:
  primary: "#108474"
  primary-active: "#0d6a5c"
  primary-disabled: "#a3d4c8"
  ink: "#364156"
  body: "#3c506d"
  muted: "#7b7b7b"
  muted-soft: "#dadada"
  hairline: "#eeeeee"
  hairline-soft: "#f9fafb"
  canvas: "#ffffff"
  surface-soft: "#f4f2f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffcf00"
  accent-marigold-active: "#fbcd0a"
  badge-sale: "#ffcf00"
  badge-new: "#108474"
  star-rating: "#ffcf00"
  footer-bg: "#3c516d"
  footer-text: "#edf5f5"

typography:
  display-xl:
    fontFamily: "'Gambado Sans Forte', 'GambadoSansForte', 'Mundial', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Gambado Sans Forte', 'GambadoSansForte', 'Mundial', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0
  title-lg:
    fontFamily: "'Fira Sans', 'Mundial', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Fira Sans', 'Mundial', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Fira Sans', 'Mundial', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Fira Sans', 'Mundial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Fira Sans', 'Mundial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Fira Sans', 'Mundial', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Fira Sans', 'Mundial', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Fira Sans', 'Mundial', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Fira Sans', 'Mundial', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Fira Sans', 'Mundial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Fira Sans', 'Mundial', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.accent-marigold}"
  section-divider:
    backgroundColor: "{colors.hairline}"
    height: "1px"
    margin: "{spacing.section} 0"
  section-heading:
    typography: "{typography.title-lg}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.md}"
  hero-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.base}"
  hero-cta:
    component: "{button-primary}"
    marginTop: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button in the brand's teal-green (#108474). Used for "Add to Cart", "Shop Now", and primary form submissions. On hover, it shifts to a darker shade (`{colors.primary-active}`). The disabled state uses a muted teal (`{colors.primary-disabled}`) with white text, signaling the button is inactive but still visible. The `button-secondary` variant is an outlined pill with a white fill and teal border, used for secondary actions like "Learn More" or "View Details". The `button-accent-marigold` variant uses the warm marigold (#ffcf00) for sale-related CTAs or promotional banners, with dark ink text for contrast.

### Navigation
**`top-nav`** — A fixed 80px white bar with a bottom hairline border. The logo (in `{colors.primary}`) sits on the left, followed by nav links in `{colors.ink}`. Active links switch to `{colors.primary}`. The search bar is a pill-shaped input with a soft putty background (`{colors.surface-soft}`), matching the button shape language. On mobile, the nav collapses into a hamburger menu, and the search bar moves into a dedicated overlay.

### Product Cards
**`product-card`** — A white card with a soft shadow and `{rounded.md}` corners, containing a square product image, title, and price. The image area uses `{rounded.sm}` to create a subtle visual hierarchy. On hover, the shadow deepens to indicate interactivity. Badges like "Sale" (`{badge-sale}`) or "New" (`{badge-new}`) are positioned at the top-left of the image area, using uppercase, bold type on a marigold or teal background.

### Forms & Inputs
**`text-input`** — Standard text inputs use a white background, `{rounded.sm}`, and a `{colors.hairline}` border. On focus, the border shifts to `{colors.primary}`. Labels use `{typography.caption}` in `{colors.muted}`. Error states show a red border (not yet extracted, see Known Gaps) with an inline error message in `{typography.body-sm}`.

### Footer
**`footer`** — A dark slate navy (`{colors.footer-bg}`) section with light text (`{colors.footer-text}`). Links are white and turn marigold on hover. The footer includes columns for customer service, about, and social links, with generous vertical padding (`{spacing.section}`). A thin hairline divider separates the footer from the main content.

### Hero Banner
**`hero-banner`** — A full-width section with a soft putty background (`{colors.surface-soft}`) and `{rounded.md}` corners. The heading uses the decorative display type (`{typography.display-md}`), with a subheading in body type and a primary CTA button below. This pattern is used on the homepage and category landing pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero banner reduces padding; search bar moves to overlay; font sizes scale down (display-xl to 32px, display-md to 24px) |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; search bar remains in header; hero banner uses medium padding |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; search bar in header; hero banner at full width with large padding |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to four columns; hero banner content centered with max-width |

### Touch Targets
- All buttons and interactive elements maintain a minimum height of 48px on mobile.
- Nav links have a minimum tap area of 44x44px.
- Product cards are fully tappable, with the entire card linking to the product page.
- Search bar has a minimum height of 48px on all breakpoints.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- The search bar collapses into a full-screen overlay on mobile, triggered by a search icon.
- Product filters collapse into a "Filter" button that opens a bottom sheet on mobile.
- The footer columns stack vertically on mobile, with each section collapsible via an accordion pattern.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for secondary and tertiary buttons were not fully extracted; the above uses reasonable assumptions based on the primary button's behavior.
- **Error and success states** for forms (red borders, green checkmarks) were not present in the extracted data.
- **Dark mode** is not supported and no dark-mode tokens were found.
- **Sub-brand or seasonal palettes** (e.g., holiday, limited edition) were not extracted.
- **Typography scale** for display sizes is inferred from the presence of Gambado Sans Forte and Fira Sans; exact font sizes and weights for all levels are estimated based on common usage patterns.
- **Spacing tokens** are based on standard e-commerce patterns; the brand may use custom values not captured.
- **Iconography** and illustration styles were not extracted; the brand may use custom illustrations or icon sets.
- **Animation and transition** timings (e.g., button hover, card hover) were not captured.
- **The extracted hex list includes several near-duplicates (#3c506d and #3c516d, #ffcf00 and #fbcd0a) — the primary teal (#108474) is the most distinctive and is used as the brand anchor. The marigold (#ffcf00) is the secondary accent. The slate navy (#3c506d) is used for body text and footer backgrounds. The putty (#f4f2f0) is the soft surface color.
