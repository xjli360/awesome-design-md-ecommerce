---
version: alpha
name: "Gaggia"
source_url: "https://www.gaggia-usa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Crimson and cobalt — #ac1a1a pressed against #002391 — is not the palette a morning-ritual brand selects; it belongs to machine manufacturers where engineering credibility matters more than lifestyle warmth. Gaggia deploys both colors without apology: the deep crimson carries every primary call-to-action and pricing accent, while the cobalt navy stakes its claim across navigation and secondary interactive states, the combination reading closer to a European racing-marque identity than anything from the soft-focus coffee-ritual category. The typographic engine is Poynter Gothic Text with its condensed sibling Poynter Gothic Text Condense — a newspaper-descended gothic that lends long Italian model names (Classic Pro, Brera, Accademia, Cadorna) the mechanical authority of a technical specification sheet rather than the aspirational warmth of lifestyle brand display faces. Long model designations that would force a line break in rounded consumer display fonts sit on a single line in the condensed weight, preserving the marque's naming precision. The site navigates between two surface registers: dark-field sections where #121212 and #1f1f1f grounds suspend polished chrome machines as if photographed in a studio void, and lighter product planes where a stepped gray staircase (#e4e5e6, #dedede, #c7c7c7, #bcbcbc) separates card fields from hairlines without reaching for pure white. Corner geometry stays deliberate — `{rounded.xs}` on form inputs, `{rounded.sm}` on product cards — never exceeding `{rounded.md}` in any primary purchase flow. This radius restraint signals precision manufacturing rather than consumer-friendly approachability. The footer compresses into the condensed type stack, dense with category links, certification seals, and regulatory text that reads more like a machine manual index than a lifestyle brand's promise.

colors:
  primary: "#ac1a1a"
  primary-active: "#d90101"
  primary-disabled: "#7a1212"
  secondary: "#002391"
  secondary-active: "#001a6e"
  ink: "#0c0c0d"
  body: "#1f1f1f"
  muted: "#bcbcbc"
  hairline: "#c7c7c7"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  canvas-dark: "#121212"
  surface-soft: "#e4e5e6"
  surface-card: "#dedede"
  surface-dark: "#1f1f1f"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  on-dark: "#e4e5e6"

typography:
  display-xl:
    fontFamily: "'poynter-gothic-text-condense', sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  display-md:
    fontFamily: "'poynter-gothic-text-condense', sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-sm:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'poynter-gothic-text-condense', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  badge:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-label:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  footer-link:
    fontFamily: "'poynter-gothic-text-condense', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  micro-label:
    fontFamily: "'poynter-gothic-text', sans-serif"
    fontSize: 10px
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
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "13px 31px"
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "13px 31px"
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "12px 16px"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    logoColor: "{colors.primary}"
    borderBottom: "1px solid {colors.surface-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleColor: "{colors.ink}"
    bodyColor: "{colors.body}"
    priceColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.xs}"
  hero-machine:
    backgroundColor: "{colors.canvas-dark}"
    headlineColor: "{colors.on-dark}"
    subheadColor: "{colors.muted}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaButton: "button-primary"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
  machine-badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  award-seal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.full}"
    size: 64px
  spec-row:
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "12px 0"
  category-filter:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.caption}"
    activeBorderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 56px
    width: "100%"
  footer-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.muted}"
    linkTypography: "{typography.footer-link}"
    captionTypography: "{typography.caption}"
    borderTop: "1px solid {colors.surface-dark}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The main purchase action renders in deep crimson (#ac1a1a) with white uppercase Poynter Gothic Text at 15px/600 weight and 0.5px tracking, giving it a stamp-like authority suited to a brand that sells machines, not subscriptions. On hover/active the background shifts to #d90101. The disabled state darkens to #7a1212 at 0.6 opacity. Corner radius stays at 4px (`{rounded.xs}`) — barely perceptible, not friendly.

**`button-secondary`** — Transparent background with a 1px crimson border and crimson text; used for secondary actions like "Learn More" and "Compare Models." Maintains the same uppercase button-md typography as the primary for consistent type hierarchy.

**`button-ghost`** — Transparent with a 1px `{colors.on-dark}` border and on-dark text, reserved for dark hero and promotional sections where the crimson primary would compete with the brand's dark photography.

### Navigation

**`nav-bar`** — A 72px near-black (#121212) bar with the Gaggia wordmark in primary crimson on the left. Navigation links in `{typography.nav-link}` (14px/500) span the center or right. A 1px `{colors.surface-dark}` bottom border separates it from the hero section below. The dark nav persists across all breakpoints, giving the site a consistent dark frame regardless of whether the page body is light or dark.

### Product Card

**`product-card`** — A `{colors.surface-card}` (#dedede) card with `{rounded.sm}` radius. Contains a product image at top, model name in `{typography.title-md}`, a brief series descriptor in `{typography.body-sm}` at `{colors.body}`, and a price in `{typography.price-display}` (condensed, 24px/700) in primary crimson. A `machine-badge` may overlay the image corner. The bottom row aligns price left with a compact add-to-cart trigger right.

### Hero

**`hero-machine`** — Full-viewport dark-field composition on #121212. Machine photography floats against a near-black void with no visible background plate or staged environment. Headline in `{typography.display-xl}` (condensed, 72px/700) — typically one or two words ("Pure Espresso", "Italian Heritage"). Subhead in `{typography.body-md}` at `{colors.muted}`. A `button-primary` sits below with `{spacing.lg}` clearance. The section takes `{spacing.section}` top and bottom padding.

### Badges and Seals

**`machine-badge`** — Small cobalt (#002391) label in uppercase `{typography.badge}` (11px/700, 0.8px tracking) applied to product cards and category pages to mark series lines ("CLASSIC", "SEMI-AUTO", "SUPER-AUTO"). Sits at the top-left of the product image. Radius `{rounded.xs}`.

**`award-seal`** — Circular 64px token in primary crimson (`{rounded.full}`). Used for award callouts and certifications overlaid on hero images or product detail headers. `{typography.micro-label}` (10px/700, 1px tracking, uppercase) inside.

### Spec Row

**`spec-row`** — Technical specification rows on product detail pages. Label on the left in `{typography.spec-label}` (13px/500) at `{colors.muted}`; value on the right in `{typography.body-sm}` at `{colors.ink}`. A 1px `{colors.hairline}` bottom border separates each row. 12px vertical padding, no horizontal indentation — the spec table reads like a data sheet.

### Category Filter

**`category-filter`** — Horizontally scrollable filter strip on `{colors.canvas-dark}` ground. Items in `{typography.caption}` (12px/400) at `{colors.on-dark}`. Active item gets `{colors.primary}` text and a 2px primary underline — no background pill, no rounding. The underline-only active state reads as a precision indicator rather than a soft selection chip.

### Add to Cart

**`add-to-cart`** — Full-width variant of `button-primary` at 56px height, placed below the spec summary on product detail pages. Same crimson/white/uppercase treatment as the primary button but wider for thumb-safe prominence. Never pill-shaped; `{rounded.xs}` maintains the machine-precision aesthetic at larger size.

### Footer

**`footer-bar`** — Near-black (#121212) with a 1px `{colors.surface-dark}` top rule. Footer link columns in `{typography.footer-link}` (condensed, 13px) at `{colors.muted}`. Legal copy in `{typography.caption}` at 12px. The Gaggia logo in the footer appears in `{colors.on-dark}` or muted rather than primary crimson — no red in the footer so the color hierarchy points upward toward CTAs.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to `display-md` (44px condensed); nav collapses to hamburger icon with full-screen dark overlay; category-filter horizontal scrolls in a single strip; `add-to-cart` sticks to the bottom of the viewport on product detail pages |
| Tablet | 744–1128px | Two-column product grid; hero splits headline text and machine image 50/50; nav shows partial link row with overflow or secondary menu |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; spec table supports two-column side-by-side comparison layout; hero at full `display-xl` |
| Wide | > 1440px | Four-column product grid; content blocks max-width 1440px and center; section padding scales to 96px; hero machine image gains more negative space |

### Touch Targets

- All buttons minimum 48px height
- `add-to-cart` at 56px for thumb-safe primary action
- Nav hamburger tap target minimum 44×44px
- Entire product card is tappable, not only the title or image
- `spec-row` minimum 44px height for accessible tap interaction on mobile

### Collapsing Strategy

- Navigation collapses to hamburger at < 1128px; dark full-screen overlay preserves the canvas-dark brand frame
- Hero machine image moves below the text block on mobile (text-first stacking)
- Spec table row labels may abbreviate on mobile (< 744px); full labels return at tablet breakpoint
- `category-filter` always horizontal-scrolls rather than wrapping; the single-row strip is a deliberate layout constraint
- Footer columns stack from three to two to one column as viewport narrows; condensed type holds well at narrow widths

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white (#ffffff) not present in extraction; the site likely uses it for body-level product listing backgrounds on Shopify page templates, but only the gray surface tier (#e4e5e6, #dedede) was captured
- `primary-disabled` (#7a1212) and `secondary-active` (#001a6e) are derived values, not extracted from the live site
- Exact button text-transform treatment (uppercase vs. mixed case) inferred from brand context; not confirmed by live extraction
- Icon set style (line vs. filled, stroke weight, whether cobalt or crimson tinting) not observable from color/font extraction alone
- Hover transition timing and easing curves not captured
- Mobile mega-menu or drawer structure not confirmed; hamburger overlay assumed from Shopify conventions
- Font weight availability within the Poynter Gothic Text Typekit license (whether 400/600/700 all exist or only specific cuts) not confirmed; weights assumed from common editorial gothic variants
- Promotional badge colors beyond cobalt and crimson (e.g. sale or clearance states) not extracted
