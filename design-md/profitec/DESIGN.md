---
version: alpha
name: "Profitec"
source_url: "https://www.profitec-espresso.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Profitec stages every machine as a precision instrument rather than a kitchen appliance — each boiler housing and pressure gauge photographed dead-center against a cool #f3f3f3 ground that reads like a photographic studio backdrop rather than a design decision. The brand's German manufacturing roots manifest as restraint: no illustrative brand marks, no lifestyle photography of espresso poured over magazine-spread countertops. What carries the page is technical authority — a Pro 300 or Pro 800 earns its price through the exposed E61 grouphead, the dual PID, the hand-finished stainless steel body. The website's primary task is clearance: get the canvas clean, frame the machine, list the specifications in an order that rewards a reader who already knows what a heat exchanger does. Color extraction surfaces almost nothing beyond the near-white ground; this is intentional opacity from a brand that trusts its objects to speak without a graphic system amplifying them. Every interactive element snaps to {rounded.none}, maintaining the same hard geometry as the machines themselves — no pill shapes, no softened corners, no consumer-friendly radius. Typography likely runs thin-weight geometric sans — the default register for European precision goods — where a 300-weight display headline at large scale reads as engineer-confident rather than declarative, and all-caps spec labels with open tracking stand in for ornamentation that never arrives. Pricing sits at the prosumer tier — roughly €800 to €3,000+ — and the commerce layer reflects this: comparison tables with granular boiler-volume and pump-pressure rows, a dealer locator routing buyers to certified stockists, and product cards that lead with model number before marketing copy. The one emotional register the brand permits is its machine ladder — Pro 300 through Pro 800 signals an aspirational climb a committed home barista can follow, and the product hierarchy encodes exactly that: water tank volume and boiler type as headline specs, not lifestyle language.

colors:
  primary: "#1c1c1c"
  primary-active: "#000000"
  primary-disabled: "#aaaaaa"
  ink: "#1c1c1c"
  body: "#3a3a3a"
  muted: "#6b6b6b"
  hairline: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  chrome: "#b8b8b8"
  chrome-dark: "#888888"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.25px
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1
    letterSpacing: -0.25px
  model-number:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 2px
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  machine-series-nav:
    backgroundColor: "{colors.canvas}"
    activeTextColor: "{colors.ink}"
    inactiveTextColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    activeBorderBottom: "2px solid {colors.ink}"
    inactiveBorderBottom: "2px solid transparent"
    height: 48px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    imageBackground: "{colors.canvas}"
    modelLabelTypography: "{typography.model-number}"
    modelLabelColor: "{colors.muted}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 600px
    imagePosition: right
    padding: "{spacing.section} 0"
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline}"
    rowPadding: "14px 0"
  model-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.model-number}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerTypography: "{typography.model-number}"
    headerColor: "{colors.muted}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.ink}"
    cellBorder: "1px solid {colors.hairline}"
    highlightBackground: "{colors.surface-soft}"
    highlightHeaderColor: "{colors.ink}"
  dealer-finder:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.chrome}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.model-number}"
    headingColor: "{colors.chrome}"
    paddingVertical: "{spacing.xxl}"

---

## Components

### Buttons

**`button-primary`** — Hard-edged rectangle at 48px height, `#1c1c1c` fill, white uppercase text tracked at 1.5px and set at 13px. Hover deepens to `#000000`; disabled collapses to `#aaaaaa` fill while preserving the uppercase letter-spaced structure so the affordance reads disabled rather than absent. The zero border-radius is non-negotiable: it mirrors the machine hardware geometry.

**`button-secondary`** — Identical silhouette to primary but inverted — white fill with a 1px `#1c1c1c` border and dark ink text. Used on product pages paired with a primary "Add to Cart," typically for actions like "Compare" or "Find a Dealer." Border collapses to `{colors.hairline}` on disabled state.

**`button-ghost`** — Transparent background, muted uppercase text at 11px, no border. Used for low-priority navigation actions ("Learn More," "See All Accessories") where ink weight would compete with the machine photography. No hover fill — underline or color shift to `{colors.ink}` on hover.

### Navigation

**`nav-bar`** — White bar, 72px tall, separated from page content by a 1px `{colors.hairline}` bottom border. Links use 14px tracked navigation type. Logo anchors left; product category links and utility items (search, language, dealer) distribute right. Clean and flat — no shadow, no blur.

**`machine-series-nav`** — Secondary tab strip below the main nav on collection pages, filtering the Pro 300–800 lineup. Active tab carries a 2px solid `{colors.ink}` bottom underline; inactive tabs sit in muted color with a transparent underline placeholder. The strip sits flush with the 1px page hairline — two rules in the same visual horizontal.

### Product Display

**`product-card`** — `#f3f3f3` card body with a white image well, sharp corners, and 24px internal padding. The model number appears in 10px all-caps tracked label above the title; price displays below in the 300-weight price-display scale. The card is an image delivery vehicle — marketing copy is minimal, and interaction leads to the detail page where specs expand.

**`spec-table`** — The most content-dense component on the site: alternating rows of uppercase 10px muted label and 14px body-sm value, each row separated by a 1px hairline. Communicates pump pressure, boiler type and volume, water tank, weight, and power draw. No icons, no progress bars — value-only precision.

**`comparison-table`** — Side-by-side model grid with column headers in `{typography.model-number}` scale. A highlighted column (surface-soft background, ink-colored header) marks the selected or recommended model. Row labels sit left-aligned; cell values center. Used to navigate the Pro series range and surface the tradeoff between single boiler, heat exchanger, and dual boiler configurations.

**`model-badge`** — Small `#f3f3f3` chip with all-caps model-number typography in muted color. Appears on listing cards to label the series tier (e.g., PRO 300, PRO 800). Hard-edged, minimal vertical footprint — intended to inform rather than promote.

### Commerce & Utility

**`hero`** — Full-width band on `#f3f3f3`, minimum 600px tall. Display-xl title (52px, weight 300) followed by a short body-md description; machine image right-anchored on desktop. Primary CTA button below copy. No video, no animation — the machine photograph at rest is the brand statement.

**`dealer-finder`** — Functional block on `#f3f3f3` ground containing a title, short body-sm explanation, and a text-input for postal code or city paired with a primary CTA. Returns a list of certified stockists. The entire UI is the form — no interactive map is assumed.

**`footer`** — `#1c1c1c` ground with white body text and chrome-gray links. Column groups cover navigation, support, legal, and contact. Headings in the model-number scale (10px, uppercase, chrome-colored) provide hierarchy. No border-top — the background color change carries full separation. Padding 48px vertical.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero image stacks below copy at full width; nav collapses to drawer; spec-table scrolls horizontally; comparison-table collapses to single-focus column with swipe to compare |
| Tablet | 744–1128px | Two-column product grid; hero image remains right-anchored at reduced scale; machine-series-nav condenses to scrollable chip row if overflow occurs |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; spec-table at full content-width; hero at full 600px+ height with generous image well |
| Wide | > 1440px | Content container constrains to max-width; hero image gains lateral breathing room; footer columns spread to full grid; no layout changes beyond breathing space |

### Touch Targets
- All buttons and nav links maintain a minimum 44px tap height regardless of visual size
- Machine-series-nav tabs minimum 44px tap height even when the typographic element is shorter
- Model-badge chips are read-only labels; no minimum tap target applies
- Spec-table rows are display-only; no tap affordance unless a row expands to a tooltip

### Collapsing Strategy
- Primary nav collapses to a full-width or slide-in drawer at < 744px; drawer contains the full link hierarchy
- Machine-series-nav becomes a horizontally scrollable chip strip at < 744px with no wrapping
- Comparison-table on mobile: one focused column visible, swipe-or-tab reveals adjacent columns; row labels pin left
- Hero copy and image stack vertically at < 744px; image scales to full container width below copy block
- Footer column groups stack vertically at < 744px in order: navigation → support → legal → contact

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one color was reliably extracted (`#f3f3f3`); all other palette tokens (`{colors.primary}`, `{colors.body}`, `{colors.hairline}`, accent colors) are inferred from European precision-appliance category conventions — the live site almost certainly loads its full token set via JavaScript
- No font families were found in extractable CSS; all `{typography.*}` tokens default to Helvetica Neue system stack and must be verified against the live site before production use
- The interactive primary color (CTA button fill, active state ink) is unconfirmed as `#1c1c1c`; a warm metallic accent (copper, brass, or warm gray) reflecting machine hardware finishes is plausible and would change the entire interactive layer
- No meta theme-color tag was present, confirming that brand color is not declared at the HTML layer
- Border-radius behavior is entirely inferred as `{rounded.none}` based on German precision-engineering category norms; actual values — including whether product cards use any softening — are unverified
- Whether Profitec uses a custom typeface (common at this price tier) or a licensed geometric sans (Aktiv Grotesk, Neue Haas Grotesk, etc.) cannot be determined without font-file inspection
- The exact nav pattern on mobile (drawer vs. full-screen overlay, hamburger vs. close-button) is unconfirmed
- Presence and behavior of a search interface (icon-triggered input vs. persistent search bar) could not be confirmed
- Any promotional badge system (e.g., "NEW," "AWARD WINNER," "MADE IN GERMANY") and its color treatment is unobserved
