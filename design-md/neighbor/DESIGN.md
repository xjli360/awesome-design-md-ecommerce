---
version: alpha
name: "Neighbor"
source_url: "https://www.neighbor.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The outdoor furniture category tends toward either suburban-catalog beige or overly industrial brutalism — Neighbor splits the difference with a near-charcoal text system built on #313131, a dark that reads warmer than pure black on natural-light photography of concrete, teak, and woven fiber. The brand stakes its visual argument on product photography doing the heavy lifting: furniture shot in real outdoor living spaces, never isolated on white, so the UI's job is to recede. Type runs in the system stack — -apple-system, BlinkMacSystemFont, 'Helvetica Neue' — which is not a budget compromise but a deliberate choice that keeps load fast and lets photography lead rather than a branded typeface. Rounded corners sit at a restrained `{rounded.sm}` to `{rounded.md}` register — nothing too pill-shaped, nothing too sharp — matching the brand's positioning between boutique and accessible. The canvas is a warm near-white rather than pure #ffffff, softening the contrast against outdoor photography that skews toward bright natural light. Primary actions use a dark button (inheriting from the #313131 brand ink) with white text, giving CTAs authority without introducing a distracting accent hue that would compete with the lifestyle imagery. Navigation is minimal — the brand name sits at far left, a spare text link set at mid-weight, and a cart icon at right — trusting the product grid to carry the page rather than category mega-menus. An important caveat: the live site was protected by Cloudflare at extraction time ("Just a moment..."), so the full palette, custom type scale, and actual hex values beyond #313131 could not be reliably pulled. The tokens below represent a best-inference reconstruction from the single extracted color plus widely-known brand positioning; treat them as a starting scaffold and validate against the live design system before shipping.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a8a8a8"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#efefef"
  canvas: "#fafaf8"
  surface-soft: "#f5f4f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-warm: "#c8b89a"
  badge-neutral: "#eeece8"
  badge-neutral-text: "#4a4a4a"
  error: "#c0392b"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  caption-uppercase:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1px
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  label-xs:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 14px
    height: 48px
    placeholderColor: "{colors.muted}"
    focusBorder: "1px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 14px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "0 {spacing.xl}"
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    overflow: hidden
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
    productNameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    hoverEffect: subtle shadow lift
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaStyle: "{components.button-primary}"
    layout: full-bleed image with left-aligned text overlay
    padding: "0"
    minHeight: 560px
  hero-text-block:
    maxWidth: 560px
    padding: "{spacing.xxl} {spacing.xl}"
    headlineColor: "{colors.ink}"
    bodyColor: "{colors.body}"
  collection-filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-uppercase}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
    activeColor: "{colors.ink}"
  material-badge:
    backgroundColor: "{colors.badge-neutral}"
    textColor: "{colors.badge-neutral-text}"
    typography: "{typography.label-xs}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  warranty-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.primary}"
    selectedRingOffset: 2px
  product-detail-layout:
    imageAreaWidth: "55%"
    detailAreaWidth: "45%"
    padding: "{spacing.xl}"
    gap: "{spacing.xl}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-md}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    textAlign: left
    marginBottom: "{spacing.lg}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    quoteMarkColor: "{colors.accent-warm}"
    authorTypography: "{typography.caption-uppercase}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    padding: "{spacing.xxl} {spacing.xl}"
    headingTypography: "{typography.caption-uppercase}"
  sticky-add-to-cart:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
    buttonStyle: "{components.button-primary}"
    priceTypography: "{typography.price-display}"
    height: 72px

## Components

### Buttons

**`button-primary`** — Square-cornered (`{rounded.none}`) dark fill using `{colors.primary}` (#313131), 48px tall, label in `{typography.button-md}`. The absence of any radius gives CTAs a furniture-catalog authority — confident and flat, like a label on a product box. Hover darkens to `{colors.primary-active}` (#1a1a1a); disabled state pulls back to `{colors.primary-disabled}` with white text maintained. Use for Add to Cart, Checkout, primary form submit.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` border, same height and type as primary. Hover floods `{colors.surface-soft}` behind the text. Deployed for secondary browsing actions like "View All," "See Details," and filter confirmations where a filled dark button would overpower the surrounding imagery.

**`button-text`** — Bare underlined link in `{colors.primary}`, `{typography.button-sm}`. Used inline within body copy and beneath product cards for "Learn More" and material-detail expansions.

**`button-pill`** — Rounded-full small button for tags and quick-filter chips in the collection browse interface. Filled dark, white label, `{rounded.full}` at compact 8px/18px padding.

### Inputs

**`text-input`** — Off-white canvas background with a `{colors.hairline}` border, 1px, `{rounded.xs}` corners. 48px height matches button height for form-row alignment. Focus state sharpens border to `{colors.primary}`. Placeholder uses `{colors.muted}`. Used in email capture, checkout fields, and the contact form.

**`select-input`** — Matches `text-input` geometry; used for variant selectors (fabric, size, finish) on the product detail page.

### Navigation

**`nav-bar`** — 64px tall on canvas, 1px `{colors.hairline-soft}` bottom rule. Brand wordmark at far left in `{typography.display-sm}` weight. Center houses category links in `{typography.nav-link}` at regular weight — not bold — keeping the bar understated. Cart and account icons sit right. No mega-menu; navigation is flat with hover-reveal dropdowns for Collections and About. Mobile collapses to 56px with a hamburger trigger.

### Product Card

**`product-card`** — 4:3 image ratio occupying the full card width, no border-radius on the image itself. Below the break: product name in `{typography.title-sm}`, material descriptor in `{typography.caption}` at `{colors.muted}`, price in `{typography.price-display}`. Hover lifts card with a subtle box-shadow rather than color change, respecting the dark-button visual vocabulary. A `{components.material-badge}` chip may float over the image bottom-left indicating the frame material (teak, aluminum, wicker).

### Hero

**`hero`** — Full-bleed lifestyle photograph, minimum 560px tall. Text block (`{components.hero-text-block}`) anchored left, max 560px wide, with headline in `{typography.display-xl}` and subhead in `{typography.body-md}` at `{colors.body}`. A single `button-primary` CTA sits below. The image is never overlaid with a color scrim — the photography's own tonal quality is trusted to provide contrast for the text overlay.

### Collection Filter Bar

**`collection-filter-bar`** — Horizontal scroll row beneath the collection header. Each filter label uses `{typography.caption-uppercase}` — spaced, small-caps feel — in `{colors.muted}` when inactive, `{colors.ink}` when active with a 1px bottom underline. No pill or chip background on active state; the weight shift alone signals selection.

### Material Badge

**`material-badge`** — Small chip in `{colors.badge-neutral}` with `{typography.label-xs}` in `{colors.badge-neutral-text}`, rounded full. Tags like "Teak," "Aluminum," "All-Weather Wicker" float on product imagery and appear beside product titles in listing grids.

### Warranty Badge

**`warranty-badge`** — Rectangular block in `{colors.surface-soft}` with a `{colors.hairline}` border, `{rounded.xs}`. Displays icons + copy ("5-Year Warranty," "Weather-Resistant") in `{typography.caption}`. Appears in the product detail sidebar below the Add to Cart block, providing purchase-confidence signals without visual noise.

### Color Swatch

**`color-swatch`** — 24px circles with `{rounded.full}`, filled with the material/colorway sample. Selected state shows a 2px `{colors.primary}` ring with a 2px offset gap, the only place a true ring-focus pattern appears in the UI.

### Testimonial Card

**`testimonial-card`** — `{colors.surface-soft}` background, `{rounded.sm}`. Quote body in `{typography.body-md}`, author line in `{typography.caption-uppercase}` at `{colors.muted}`. An oversized quotation mark glyph in `{colors.accent-warm}` anchors the top-left corner — the single warm decorative element in an otherwise cool-neutral system.

### Sticky Add to Cart

**`sticky-add-to-cart`** — Fixed bottom bar on mobile and tablet PDP. 72px tall, `{colors.canvas}` background, 1px top border at `{colors.hairline}`. Price left-aligned in `{typography.price-display}`, `button-primary` right-aligned. Disappears on desktop where the sidebar CTA is always in viewport.

### Footer

**`footer`** — Full-bleed `{colors.primary}` (#313131) block; text in `{colors.on-primary}`. Column headers use `{typography.caption-uppercase}` for section groupings (Shop, Company, Support). Body links in `{typography.body-sm}` with no underline, underline on hover. Reversal of the page's canvas-on-dark structure anchors the page base with the same weight as the primary buttons above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark; sticky PDP bottom bar activates; hero text block full-width with reduced display-xl size (~28px); filter bar horizontally scrollable |
| Tablet | 744–1128px | Two-column product grid; nav bar keeps wordmark + cart icon, hamburger for full menu; PDP switches to stacked (image above, details below); sticky add-to-cart still active |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav; PDP uses side-by-side layout (55/45 split); sticky bar deactivates; hero at full 560px+ height |
| Wide | > 1440px | Grid remains three columns but card sizes increase; hero image crops wider; max-width container (~1400px) centered; section padding expands to keep content from feeling cramped |

### Touch Targets

- All interactive elements (buttons, swatches, filter chips) minimum 44×44px on mobile
- Color swatches expand tap area with 10px invisible padding beyond the 24px visual circle
- Nav hamburger target is 48×48px despite a 24px icon
- Cart and account nav icons maintain 44px touch width via padding

### Collapsing Strategy

- Product grid: 1 col (mobile) → 2 col (tablet) → 3 col (desktop) — no 4-col breakpoint to keep card sizes generous
- PDP: stacked on mobile/tablet, side-by-side on desktop
- Filter bar: wraps to horizontal scroll on mobile rather than dropdown collapse, keeping all options one swipe away
- Footer columns: single stacked accordion on mobile (each section header is a tap-to-expand trigger), 4-column grid on tablet+
- Hero text block: full-viewport on mobile with reduced type scale; left-constrained on tablet and above

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Site was Cloudflare-protected at extraction time** ("Just a moment..." page title) — only one hex color (#313131) was reliably extracted; the full site palette was not accessible
- **Actual primary accent color unknown** — the brand may use a warm accent (terracotta, sand, or olive) for hover states, sales banners, or seasonal promotions; none could be confirmed from extraction
- **Custom typeface unconfirmed** — the extracted font stack is pure system UI; the live site may load a custom or licensed serif/sans for display headings via web fonts not captured during extraction
- **Exact border-radius values unverified** — `{rounded.xs}` through `{rounded.md}` values are inferred from brand positioning; actual computed values not confirmed
- **Dark mode support unknown** — no `prefers-color-scheme` tokens were extractable
- **Animation/motion system not captured** — hover transitions, image lazy-load patterns, and scroll-driven animations are common in this category but unverifiable without live access
- **Specific spacing scale unconfirmed** — spacing tokens follow an 8px base-grid convention standard to the category; actual design spec may differ
- **Product photography art direction** — assumed to be lifestyle/outdoor scenes based on brand category; the specific photography style (editorial vs. studio-hybrid) was not confirmable
