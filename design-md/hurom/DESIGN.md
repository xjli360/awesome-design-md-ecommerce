---
version: alpha
name: "Hurom"
source_url: "https://www.hurom.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Fresh-pressed celery juice in a tall glass — that saturated chlorophyll green (#78c500) anchors every primary CTA, add-to-cart button, and trust badge across hurom.com, an unmistakable signal that this brand sells the ritual of slow extraction, not just the appliance. The type system pairs geometric sans-serifs — azo-sans-web for body and UI, korolev-condensed for impact headlines — creating a clinical-yet-approachable hierarchy that borrows more from wellness editorial than consumer electronics. Product photography dominates: full-bleed hero images of juicers mid-pour against white or near-white canvases let the machinery and its produce speak without competing color noise. Cards sit at `{rounded.sm}` with barely-there shadows; buttons land at `{rounded.xs}` with firm 48px heights, favoring a squared posture over pill shapes — the message is precision engineering, not playful lifestyle. A secondary warm accent (#da532c) surfaces on sale tags, limited-edition callouts, and urgency indicators, while a deeper forest (#497900) serves as the hover and active state for primary interactions, grounding the brighter green without introducing a new hue. Spacing is generous — product grids breathe with `{spacing.xl}` gutters and `{spacing.section}` vertical rhythm between modules — reinforcing the "slow" philosophy that extends from the juicing mechanism to the shopping experience itself. Navigation is minimal: a slim sticky header with the wordmark set in azote (a display face reserved exclusively for logo lockups) collapses to a hamburger on mobile, never competing with the hero zone below. The palette stays intentionally tight — white canvas, ink-dark text, one green, one warm accent — so that lifestyle imagery of fruits, vegetables, and juice colors provides the visual variety the interface deliberately withholds.

colors:
  primary: "#78c500"
  primary-active: "#497900"
  primary-disabled: "#c8e8a0"
  accent-warm: "#da532c"
  accent-warm-active: "#b8421f"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f7f7f5"
  surface-card: "#ffffff"
  surface-warm: "#faf8f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#78c500"
  error: "#d63b2e"
  star-rating: "#f5a623"
  scrim: "rgba(0,0,0,0.5)"

typography:
  display-xl:
    fontFamily: "'korolev-condensed', 'Arial Narrow', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'korolev-condensed', 'Arial Narrow', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
    textTransform: uppercase
  display-md:
    fontFamily: "'korolev-condensed', 'Arial Narrow', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-upper:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-lg:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  logo-display:
    fontFamily: "'azote', 'azo-sans-web', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1px
  price-lg:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-compare:
    fontFamily: "'azo-sans-web', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
    textDecoration: line-through

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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    border: none
    transition: background-color 0.2s ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 1px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-accent:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    border: 1px solid {colors.error}
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 40px 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
    position: sticky
    zIndex: 100
  nav-bar-scrolled:
    boxShadow: 0 2px 8px rgba(0,0,0,0.06)
  mobile-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.lg}"
    width: 100vw
    height: 100vh
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    hoverShadow: 0 4px 16px rgba(0,0,0,0.08)
    transition: box-shadow 0.25s ease, transform 0.25s ease
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: 1/1
    objectFit: contain
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
  product-card-compare-price:
    typography: "{typography.price-compare}"
    textColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    display: flex
    alignItems: center
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 600px
  hero-subheadline:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
    maxWidth: 520px
    marginTop: "{spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 40px
    height: 52px
    marginTop: "{spacing.lg}"
  sale-badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    iconColor: "{colors.primary}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    border: 1px solid {colors.hairline}
    rounded: "{rounded.sm}"
    cellPadding: "{spacing.md} {spacing.base}"
  comparison-table-highlight:
    backgroundColor: "{colors.surface-soft}"
    borderTop: 3px solid {colors.primary}
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: 1px solid {colors.hairline}
    buttonWidth: 44px
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 48px
    height: 52px
    width: 100%
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.base}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    hoverColor: "{colors.on-dark}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg}"
    boxShadow: 0 8px 32px rgba(0,0,0,0.12)
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
    gap: "{spacing.xxs}"
  benefit-icon-row:
    iconSize: 48px
    iconColor: "{colors.primary}"
    textTypography: "{typography.body-sm}"
    textColor: "{colors.body}"
    gap: "{spacing.xl}"
    padding: "{spacing.xxl} 0"
---

## Components

### Buttons

**`button-primary`** — A solid green (#78c500) rectangle with `{rounded.xs}` corners, white text set in `{typography.button-lg}`. On hover, the background deepens to the forest active state (#497900); disabled state lightens to a washed sage (#c8e8a0) at reduced opacity. Used exclusively for primary conversions: Add to Cart, Shop Now, Subscribe.

**`button-secondary`** — White fill with a 1px ink border and dark text. On hover, inverts to a dark fill with white text, creating a firm toggle effect. Used for secondary actions like "Learn More," "Compare Models," and filter controls.

**`button-accent`** — Uses the warm orange-red (#da532c) for urgency-driven CTAs: limited-time sales, flash promotions, and clearance events. Slightly smaller at 44px height to visually subordinate to primary buttons.

**`button-text`** — An underlined green text link with no background, used inline for tertiary navigation such as "View all recipes" or "See full specs."

### Inputs

**`text-input`** — 48px-tall fields with `{rounded.xs}` corners and a light hairline border that transitions to green on focus. Error state swaps the border to the error red. Labels sit above the field in `{typography.caption}`.

**`select-input`** — Matches text-input dimensions with a custom chevron indicator positioned 16px from the right edge.

**`quantity-selector`** — A compact inline control with minus/plus buttons flanking a centered number, bordered in hairline gray. Each tap zone is 44px square for reliable touch interaction.

### Navigation

**`nav-bar`** — A 64px sticky header on white canvas with a subtle bottom hairline. The Hurom wordmark (set in azote) sits left; navigation links in `{typography.nav-link}` center or right-align on desktop. On scroll, a soft shadow appears to lift the bar from content below.

**`mobile-menu`** — Full-viewport overlay triggered by a hamburger icon. Links are stacked in `{typography.title-md}` with `{spacing.lg}` vertical gaps for comfortable thumb reach.

**`announcement-bar`** — A 40px band above the nav in solid primary green, carrying rotating promotional messages in white caption text. Dismissible via a small X on the right edge.

**`breadcrumb`** — Muted caption-sized links separated by chevrons, with the current page in ink. Appears on product and collection pages below the nav.

### Product Display

**`product-card`** — White card with a 1:1 image container (object-fit: contain on a soft-gray background), product title, and price below. On hover, a subtle shadow and 2px upward translate signal interactivity. Sale badges overlay the top-left corner of the image area.

**`product-card-price`** — Bold ink-colored price in `{typography.price-md}`. When a compare-at price exists, it renders to the right in `{typography.price-compare}` with a line-through, and the current price shifts to accent-warm to signal discount.

**`comparison-table`** — A bordered grid comparing juicer models side-by-side. The recommended model's column gets a `{colors.surface-soft}` background and a 3px green top border to draw the eye. Cell text uses `{typography.body-sm}`; headers use `{typography.title-sm}`.

### Hero & Marketing

**`hero-banner`** — A minimum 560px-tall section with a large product photograph on one side and headline copy on the other. Headlines render in condensed uppercase (`{typography.display-xl}`), subheadlines in `{typography.body-lg}`, followed by a slightly oversized CTA button (52px height).

**`sale-badge`** — Small uppercase pill in accent-warm orange with white text, positioned absolutely over product images. Conveys "SALE," "LIMITED," or percentage discounts.

**`new-badge`** — Identical shape to sale-badge but in primary green, used for new arrivals and seasonal launches.

**`trust-badge`** — A soft-background horizontal strip with a green icon (warranty shield, shipping truck, leaf) paired with short descriptive text. Typically rendered in a row of 3–4 across the product detail page.

**`benefit-icon-row`** — A horizontal sequence of 48px green icons with short labels below, communicating product benefits (quiet operation, easy clean, nutrient retention). Spaced with `{spacing.xl}` gaps and padded with `{spacing.xxl}` vertically.

### Footer

**`footer`** — Dark ink background (#1a1a1a) with white headings and muted-soft body links organized in 4-column grid on desktop. Includes newsletter signup input, social icons, and legal links at the bottom separated by a hairline.

### Utility

**`search-overlay`** — A dropdown panel anchored below the nav search icon, with a prominent text input and recent/suggested results below. Elevated with a strong box-shadow to float above page content.

**`star-rating`** — Inline SVG stars in warm gold (#f5a623) at 16px, tightly spaced with `{spacing.xxs}` gaps. Partial fills render via clip-path for fractional ratings.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks vertically (image above, copy below); nav collapses to hamburger + logo + cart icon; comparison table scrolls horizontally; benefit icons stack 2×2 |
| Tablet | 744–1128px | Two-column product grid; hero remains side-by-side at reduced image scale; nav shows top-level links, overflow into "More" dropdown; footer switches to 2-column |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at designed 560px height; comparison table renders fully; benefit row spans full width inline |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid may expand to four columns on collection pages; hero image scales proportionally with extra canvas breathing room |

### Touch Targets

- All interactive elements maintain a minimum 44×44px tap area on mobile and tablet
- Quantity selector buttons are exactly 44px square
- Nav hamburger icon has a 48px tap zone despite a 24px visual icon
- Product card entire surface is tappable, not just the title text
- Footer links have 12px vertical padding to prevent mis-taps in dense link columns

### Collapsing Strategy

- Desktop mega-menu navigation condenses to a full-screen slide-out drawer on mobile
- Product detail page tabs (Description, Specs, Reviews) become an accordion on mobile
- Comparison table locks the first column (model name) and allows horizontal scroll for feature columns
- Benefit icon row wraps from single-row to 2×2 grid below 744px
- Hero banner shifts from 50/50 side-by-side layout to stacked (image full-width, text below) at tablet breakpoint
- Footer columns collapse into expandable accordion sections on mobile, with headings as toggle triggers

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only three hex colors were extractable from static page source; additional palette values (hover states, surface tones, error colors) are inferred from the primary triad and standard UI conventions
- The `azote` font is used for the Hurom logo/wordmark but no specimen details (weights, optical sizes) could be confirmed from the extracted data
- Exact border-radius values for cards and buttons could not be measured — `{rounded.xs}` (4px) and `{rounded.sm}` (8px) are estimated from visual appearance
- Animation/transition timing curves and durations for hover states and page transitions are not captured
- Dark-mode or alternate theme tokens were not detected
- Specific box-shadow values for product card hover and nav scroll states are approximated
- Icon set details (custom SVG library vs. third-party) could not be determined from extraction
- Shopify's dynamic rendering may load additional color tokens, spacing variables, or component styles via JavaScript that static extraction missed
