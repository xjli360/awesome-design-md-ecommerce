---
version: alpha
name: "Kit & Kin"
source_url: "https://kitandkin.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A protective, earth-toned baby-care brand built on a sage-and-charcoal palette anchored by #8baa99 — a muted, silvery green that appears nowhere in the generic web palette and reads as botanical without being sweet. The brand pairs this with #25282a (near-black ink) and #f6f3ee (warm off-white canvas), creating a system that feels grounded and clinical in the best sense: clean enough for a nursery, serious enough for a parent reading ingredient labels. The extracted hex list is unusually large (25+ colors), but the core story is the green-gray gradient from #8baa99 through #a7bdb1 and #9eafa6 to #d7e0da — a tonal family that replaces the pastel pinks and blues typical of baby care. Accents of #7dc4bc (teal) and #a32138 (crimson) add rare jolts of saturation, the latter likely used for sale badges or error states. Gotham is the declared typeface, a geometric sans-serif with military precision that lends authority to product claims and ingredient lists. The brand uses generous whitespace and soft card corners (`{rounded.lg}` ~20px) to offset the seriousness of the type, and the `{rounded.full}` pill shape appears on CTAs and search inputs, echoing the rounded organic forms of baby bottles and teething rings. The overall mood is "trustworthy modernism" — a brand that knows parents are exhausted and skeptical, and responds with clarity, not cuteness.

colors:
  primary: "#8baa99"
  primary-active: "#7a9a88"
  primary-disabled: "#c4d4c9"
  ink: "#25282a"
  body: "#505759"
  muted: "#6e797c"
  muted-soft: "#979797"
  hairline: "#ccd0d2"
  hairline-soft: "#dedede"
  canvas: "#f6f3ee"
  surface-soft: "#ece8e3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#7dc4bc"
  accent-crimson: "#a32138"
  accent-warm: "#e5dcd5"
  badge-sale: "#d91c1c"
  dark-surface: "#33464e"
  dark-ink: "#121212"

typography:
  display-xl:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "2px solid {colors.ink}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-crimson}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
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
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
  product-card-image:
    rounded: "{rounded.lg}"
    aspectRatio: "1:1"
  product-card-badge:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-old-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    textDecoration: "line-through"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.md} {spacing.lg}"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-eco:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: "1px"
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: "1px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's sage green `{colors.primary}` on a white background. Uppercase Gotham at 15px with 0.5px letter-spacing gives it a confident, no-nonsense tone. On hover, shifts to `{colors.primary-active}` (#7a9a88); disabled state uses `{colors.primary-disabled}` (#c4d4c9). The `{rounded.sm}` (8px) corner is soft but not pill-like — the brand reserves full pills for secondary and utility actions.

**`button-secondary`** — An outlined variant with a 2px `{colors.ink}` border on `{colors.canvas}` background. Same typography and height as primary, but the border-and-fill treatment signals a less urgent action (e.g., "Learn More" or "Add to Registry"). Hover state likely fills with `{colors.ink}` and inverts text to white.

**`button-tertiary-text`** — A text-only link styled as a button, using `{colors.primary}` for the text. No background or border. Used for inline actions like "Clear filters" or "View details" within cards. Hover state likely underlines or darkens to `{colors.primary-active}`.

**`button-pill-primary`** and **`button-pill-outline`** — Pill-shaped variants (`{rounded.full}`) used for subscription toggles, quantity selectors, and mobile CTAs. The pill outline variant echoes the secondary button's border logic but with a fully rounded profile.

### Cards
**`product-card`** — A white card with `{rounded.lg}` (20px) corners, containing a square product image with matching corner radius. The card stacks image, badge (if applicable), title, price, and an optional "Add to Cart" button. The generous corner radius softens the geometric Gotham type, making the shopping experience feel approachable. Cards sit on `{colors.surface-soft}` (#ece8e3) or `{colors.canvas}` (#f6f3ee) backgrounds, creating a warm, layered grid.

**`product-card-badge`** — A small rectangular badge (`{rounded.xs}`, 4px) in `{colors.accent-crimson}` (#a32138) for sale indicators, or `{colors.accent-teal}` (#7dc4bc) for "new" or "eco-friendly" labels. Uppercase Gotham at 11px with tight tracking fits within a 4px vertical padding.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on `{colors.canvas}` background. Logo sits left, nav links center or right, with a search icon and cart icon on the right edge. Nav links use `{typography.nav-link}` — 14px uppercase Gotham with 0.3px letter-spacing — giving the header a crisp, editorial feel. Active state uses `{colors.primary}` text; inactive uses `{colors.muted}` (#6e797c). On scroll, a `{colors.hairline}` bottom border appears.

### Forms
**`text-input`** — A standard input field with `{rounded.sm}` (8px) corners, 1px `{colors.hairline}` border, and 16px inner padding. Focus state thickens the border to 2px and switches to `{colors.primary}` (#8baa99). Error state uses `{colors.accent-crimson}` (#a32138) for the border, with an error message in `{typography.caption-sm}` below. The input height (48px) matches button heights for form alignment.

### Footer
**`footer-section`** — A dark footer on `{colors.ink}` (#25282a) background with white text. Links use `{colors.muted-soft}` (#979797) and lighten to `{colors.canvas}` on hover. The footer typically includes 3-4 columns of links (Shop, Learn, Support, Social), a newsletter signup with a pill-shaped input, and legal text in `{typography.caption-sm}`.

### Accordion
**`accordion-header`** and **`accordion-content`** — Used for FAQ sections and product details. The header is a clickable row with `{typography.title-sm}` (16px, weight 500) and a chevron icon that rotates on expand. Content area uses `{typography.body-sm}` (14px) with `{colors.body}` (#505759) for readability. Padding follows the `{spacing.base}` (16px) rhythm.

### Badges
**`badge-new`**, **`badge-sale`**, **`badge-eco`** — Three badge variants for product cards and category pages. "New" uses teal `{colors.accent-teal}`, "Sale" uses crimson `{colors.badge-sale}` (#d91c1c), and "Eco" uses the primary sage green in a pill shape. All use `{typography.badge}` — 11px uppercase with 0.5px tracking — ensuring badges are legible at small sizes without overwhelming the product image.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to `{typography.display-lg}`; buttons become full-width; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses `{typography.display-xl}` at 28px; footer shows 2 columns |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero at 36px `{typography.display-xl}`; footer 3-4 columns |
| Wide | > 1440px | Max-width container (1440px) centered; product grid may expand to 4 columns; hero background extends full-width |

### Touch Targets
- All buttons and interactive elements minimum 48px height (exceeds Apple's 44px guideline)
- Nav links have 44px minimum tap area on mobile
- Accordion headers have 48px tap target
- Product card CTAs maintain 48px height across breakpoints
- Search bar pill maintains 48px height on all devices

### Collapsing Strategy
- **Mobile (< 744px):** Navigation collapses to a hamburger menu; product grid goes single-column; hero section reduces padding from `{spacing.section}` (64px) to `{spacing.xxl}` (48px); footer links collapse into an accordion pattern; multi-step forms (checkout, subscription) become single-column stacks
- **Tablet (744–1128px):** Navigation shows abbreviated links (icons + short labels); product grid uses 2 columns; hero maintains `{spacing.section}` padding but text scales down
- **Desktop (1128–1440px):** Full layout with all columns visible; nav shows full text links; product grid 3 columns
- **Wide (> 1440px):** Content constrained to max-width container; backgrounds extend full-width; product grid may show 4 columns for category pages

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states:** Only primary button hover (`{colors.primary-active}`) is confirmed. Hover states for secondary buttons, text links, nav links, and product cards are inferred from common patterns but not extracted from the live site.
- **Error and validation styling:** Text input error state (`{colors.accent-crimson}` border) is an assumption based on the presence of #a32138 in the palette. No error messages, success states, or form validation patterns were observed.
- **Dark mode:** No dark mode styles were detected. The brand uses a dark footer (`{colors.ink}`) but the main interface is light (`{colors.canvas}`).
- **Typography scale:** Gotham is confirmed via font-family declarations, but exact sizes, weights, and line heights are inferred from typical Gotham usage at this brand scale. The extracted data did not include specific CSS font-size/line-height values.
- **Spacing system:** The spacing scale is a standard 4px/8px system assumed from the brand's clean aesthetic. No specific spacing tokens were extracted from the live site.
- **Component states:** Disabled states for secondary buttons, loading states for forms, and empty states for cart/search are not documented.
- **Animation and transition:** No timing functions, easing curves, or transition durations were extracted. The brand likely uses subtle fades (200-300ms ease-in-out) but this is unconfirmed.
- **Sub-brand or seasonal palettes:** The extracted hex list may include seasonal or campaign-specific colors (e.g., #efe3ef could be a limited-edition lavender). The core palette documented above focuses on the most frequent and structurally significant colors.
- **Iconography:** No icon set or style guidelines were extracted. The brand likely uses custom line icons matching the geometric Gotham aesthetic, but this is speculative.
