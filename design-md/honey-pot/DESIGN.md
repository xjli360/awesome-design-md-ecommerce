---
version: alpha
name: "Honey Pot"
source_url: "https://thehoneypot.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, earthy warmth anchors Honey Pot’s digital presence — not the pastel pinks of conventional feminine care, but a rich #252222 ink that grounds every page against a #fdfbf6 canvas that reads like unbleached cotton or sun-dried parchment. The brand’s primary voltage comes from #da532c, a fired-clay orange that appears in CTAs, ingredient callouts, and the signature “plant-derived” badge, while a supporting cast of botanical accents — sage #7bc6b9, petal pink #f7a4d7, lavender #dccdf1, and mint #a7ecd7 — map directly to product variants and ingredient families. Typography is a deliberate hybrid: Rational Display for headlines (a warm, geometric sans with subtle humanist curves) and Syke Mono for data, pricing, and ingredient percentages, creating a system that feels both clinical and nurturing. The site uses generous vertical rhythm — section padding at {spacing.section} — and softens every interactive element with {rounded.full} pill shapes: search bars, add-to-cart buttons, ingredient tags. Product photography is high-contrast and shadow-rich, often set against the #fdfbf6 ground with a single hero product in center frame, the orange #da532c accent appearing only in the CTA strip below. The overall mood is that of an apothecary that happens to sell online: honest, plant-forward, and unapologetically warm.

colors:
  primary: "#da532c"
  primary-active: "#c44a26"
  primary-disabled: "#f0b8a0"
  ink: "#252222"
  body: "#231f20"
  muted: "#6a5e5e"
  muted-soft: "#9e9494"
  hairline: "#dedede"
  hairline-soft: "#d9d9d9"
  canvas: "#fdfbf6"
  surface-soft: "#f7f7f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sage: "#7bc6b9"
  sage-soft: "#d7f0e8"
  pink: "#f7a4d7"
  lavender: "#dccdf1"
  mint: "#a7ecd7"
  dark: "#121212"

typography:
  display-xl:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  mono-data:
    fontFamily: "'Syke Mono', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-data-sm:
    fontFamily: "'Syke Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Syke Mono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
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
    padding: 14px 28px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-pill-sage:
    backgroundColor: "{colors.sage}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-pink:
    backgroundColor: "{colors.pink}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
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
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.mono-data}"
    padding: "{spacing.xs} {spacing.base}"
  ingredient-badge:
    backgroundColor: "{colors.sage-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  ingredient-badge-pink:
    backgroundColor: "{colors.pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  ingredient-badge-lavender:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  ingredient-badge-mint:
    backgroundColor: "{colors.mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subhead:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  accordion-trigger:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button in fired-clay orange (#da532c) with white text. On hover, it deepens to `{colors.primary-active}` (#c44a26). The disabled state uses `{colors.primary-disabled}` (#f0b8a0) — a muted peach that still reads as part of the brand's warm palette rather than a generic gray. Padding is generous at 14px 28px, giving the button a substantial, confident feel.

**`button-secondary`** — An outlined variant using the brand's deep ink (#252222) as both text and a 2px border on the warm canvas background. On hover, the button inverts to a solid ink fill with white text. This is used for "Learn More" and secondary product actions where the orange primary would compete with other orange elements on the page.

**`button-tertiary-text`** — A text-only button with no background or border, using the ink color and standard button typography. Used for "Skip to cart" and other low-emphasis actions. Hover state adds an underline.

**`button-pill-sage` / `button-pill-pink`** — Color-coded pill buttons used for ingredient filters and product variant selectors. The sage (#7bc6b9) and pink (#f7a4d7) variants map directly to product lines (e.g., sage for "Cooling" formulas, pink for "Sensitive" formulas). These are smaller at 8px 20px padding with `{typography.button-sm}`.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on the warm canvas background, with uppercase nav links in `{typography.nav-link}`. The bar is separated from the page content by a thin `{colors.hairline}` border. The active nav link is underlined with a 2px `{colors.primary}` strip and the link text changes to the primary orange.

**`nav-link-active`** — The active navigation state uses the primary orange for text and a 2px bottom border in the same color, creating a clear visual anchor for the current section.

### Forms
**`text-input`** — Standard text inputs use the warm canvas background with a 1px hairline border and 12px 16px padding. On focus, the border thickens to 2px and shifts to the primary orange. Error states also use a 2px orange border — the brand treats errors as a call to attention rather than a red alert, consistent with its warm, non-clinical tone.

### Cards
**`product-card`** — Product cards are white (`{colors.surface-card}`) with `{rounded.md}` corners and no shadow — the brand relies on the contrast between the white card and the warm canvas background for separation. The image sits flush to the top with rounded top corners only, while the title and price sit below with standard padding. The price is set in `{typography.mono-data}` to visually separate it from the product name.

### Badges
**`ingredient-badge`** — Small pill-shaped badges in sage-soft (#d7f0e8) with uppercase monospace text. Used to tag products with ingredient highlights (e.g., "Aloe Vera", "Chamomile"). The brand uses four color variants — sage-soft, pink, lavender, and mint — each corresponding to a different ingredient family or product benefit. The monospace font gives these badges a clinical, trustworthy feel that contrasts with the otherwise warm serif/geometric system.

### Hero
**`hero-section`** — Full-width section on the warm canvas background with `{spacing.section}` vertical padding. The headline uses `{typography.display-xl}` in the deep ink color, while the subhead uses `{typography.body-md}` in the slightly lighter body color. The hero typically features a single product image centered below the text, with the primary CTA button below.

### Footer
**`footer`** — A deep ink (#252222) footer with white text, providing a strong visual closure to the page. Links are set in `{typography.link}` and shift to the primary orange on hover. The footer uses `{spacing.xxl}` vertical padding and typically contains three columns: product categories, customer support, and social links.

### Accordion
**`accordion-trigger`** — Used for FAQ sections and product details. The trigger is a full-width clickable area with `{typography.title-sm}` text and a bottom hairline border. On click, the content panel opens below with `{typography.body-sm}` text and no additional padding at the top (the trigger's bottom padding provides the spacing).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; hero headline drops to 28px; product cards go single-column; ingredient badges stack vertically; footer stacks to single column |
| Tablet | 744–1128px | Nav links remain visible but condensed; hero headline at 32px; product cards in 2-column grid; ingredient badges wrap in 2 rows; footer in 2 columns |
| Desktop | 1128–1440px | Full nav with all links; hero headline at 42px; product cards in 3-column grid; ingredient badges in horizontal scroll strip; footer in 3 columns |
| Wide | > 1440px | Max-width container at 1440px; hero headline scales to 48px; product cards in 4-column grid; extra whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44px height
- Product card images are tappable and link to product detail pages
- Accordion triggers have 48px minimum tap height
- Ingredient badges are 32px minimum tap height with 8px spacing between them

### Collapsing Strategy
- Primary nav collapses to a hamburger menu at < 744px, with the logo centered and cart icon on the right
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Ingredient badge strips collapse from horizontal scroll → wrapped rows → stacked vertical list
- Footer columns collapse from 3 → 2 → 1, with the social links section always at the bottom
- Hero sections reduce vertical padding from 64px to 32px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for ingredient badges and product card images could not be reliably extracted — assumed to use a subtle scale transform (1.02) and shadow lift
- Error styling for form validation beyond the 2px orange border is not documented — error message typography and iconography are unknown
- The exact font weights for Rational Display and Syke Mono beyond what was found in font-face declarations are inferred — the extracted declarations included `domaine_sans_textitalic`, `domaine_sans_textlight`, `domaine_sans_textlight_italic`, and `domaine_sans_textregular`, suggesting a variable or multi-weight family, but the specific weight-to-token mapping is best-guess
- Dark mode is not present on the live site — all pages use the warm canvas (#fdfbf6) as background
- Sub-brand palettes (e.g., for "Cooling" vs "Sensitive" product lines) are inferred from the extracted accent colors but not formally documented in the site's CSS
- The extracted hex list included #121212 (dark) which may be a Shopify checkout or overlay color — it's included as a token but its usage is not confirmed
- Animation timing and easing curves (transitions, hover effects) were not extracted — assumed standard 200ms ease-in-out
- The extracted font list included `inherit` which is a CSS default, not a brand font — it has been excluded from the typography block
