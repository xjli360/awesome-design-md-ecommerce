---
version: alpha
name: "Avanti"
source_url: "https://www.avantiproducts.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bright cyan (#27c3f2) floods the header and CTA layer of a site selling refrigerators and dishwashers — an unexpectedly playful voltage for a category that defaults to stainless-steel grays and safe navy. Avanti leans into this electric aqua as a signal that compact living is energetic, not compromising. The palette backs it up with a warm orange ramp (#f48120 through #d4602c) used in promotional badges, sale callouts, and hover states, giving the page a temperature contrast that keeps product grids from feeling clinical. Typography is pure utility: Roboto at medium weights across all surfaces, set in a tight vertical rhythm that lets appliance photography — always on white or light-blue (#c6e8f9) backdrops — dominate the viewport. Card corners land at `{rounded.sm}` (8px), just enough softness to humanize the grid without competing with the cylindrical and boxy product silhouettes. Navigation is a slim 64px strip anchored by the cyan wordmark left and a monospace-styled search field right, collapsing to a hamburger icon below 744px. Product cards stack energy ratings, capacity specs, and price in a compressed vertical layout that prioritizes scannability over lifestyle storytelling — this is a spec-driven shopper's interface. The Shopify backbone delivers standard cart and collection patterns, while `{spacing.section}` (64px) separates hero banners from category grids, giving the dense catalog room to breathe. Buttons are squared-off pills (`{rounded.xs}`) in the brand cyan with white text, shifting to the darker #0c97c1 on press — a deliberate nod to physical button depression on the appliances themselves.

colors:
  primary: "#27c3f2"
  primary-active: "#0c97c1"
  primary-disabled: "#c6e8f9"
  secondary: "#006fcf"
  accent-orange: "#f48120"
  accent-orange-dark: "#d4602c"
  accent-orange-mid: "#f37521"
  success: "#008a00"
  error: "#ee0000"
  warning: "#ffbd00"
  ink: "#231f20"
  body: "#4a4a4a"
  muted: "#8c8c8c"
  muted-soft: "#8a9297"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#c6e8f9"
  surface-card: "#ffffff"
  surface-dark: "#231f20"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  promo-gradient-start: "#f58720"
  promo-gradient-end: "#e16f27"

typography:
  display-xl:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-bold:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  spec-label:
    fontFamily: "'Roboto Mono', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  price:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary-active}
  button-promo:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 64px
    boxShadow: 0 2px 8px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline}
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    boxShadow: 0 4px 16px rgba(0,0,0,0.1)
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 420px
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  sale-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-row:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    padding: "{spacing.sm} 0"
    borderBottom: 1px solid {colors.hairline}
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px 10px 40px
    height: 40px
    border: 1px solid {colors.hairline}
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  price-display:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  price-sale:
    backgroundColor: transparent
    textColor: "{colors.error}"
    typography: "{typography.price}"
  energy-rating-badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"

---

## Components

### Buttons

**`button-primary`** — Solid cyan (#27c3f2) fill with white text, `{rounded.xs}` corners (4px), producing a firm, appliance-panel feel. On hover the background deepens to `{colors.primary-active}` (#0c97c1). Disabled state washes out to the pale ice-blue `{colors.primary-disabled}` with muted gray text, clearly signaling inactivity without losing brand association.

**`button-secondary`** — White fill with a 2px cyan border and cyan text. On hover the background tints to `{colors.surface-soft}` and the border shifts to the darker active cyan. Used for "Compare" and "Add to Wishlist" actions where the primary CTA is already present.

**`button-promo`** — Warm orange (#f48120) fill with white text, deployed exclusively in promotional contexts: sale banners, limited-time offers, and clearance callouts. The warm temperature creates urgency against the cool cyan surroundings.

### Navigation

**`nav-bar`** — A 64px-tall white strip spanning full viewport width. Brand wordmark sits left at 140px width; category links ("Refrigerators", "Dishwashers", "Wine Coolers", "Freezers") center in `{typography.nav-link}`. A compact search field and cart icon anchor right. A 1px `{colors.hairline}` bottom border separates nav from content; on scroll this swaps to a subtle drop-shadow (`nav-bar-scrolled`).

**`breadcrumb`** — Muted gray links separated by "/" characters in `{typography.caption}`, with the current page in bold ink. Positioned immediately below the nav-bar with `{spacing.md}` vertical padding.

### Product Card

**`product-card`** — White card with 1px hairline border and `{rounded.sm}` corners. Interior stacks a product image (aspect 4:3, object-fit cover), a category badge (cyan), the product title in `{typography.title-sm}`, a compressed spec summary in `{typography.spec-label}` (monospace for technical readability), and the price in `{typography.price}`. On hover the border dissolves and a soft box-shadow lifts the card. Cards sit in a 3-column grid on desktop, 2-column on tablet, single stack on mobile with `{spacing.lg}` gutters.

### Hero Banner

**`hero-banner`** — Full-bleed section with the light ice-blue `{colors.surface-soft}` (#c6e8f9) background. Headline in `{typography.display-xl}` left-aligned, with a supporting subhead in `{typography.body-md}` and a primary CTA button. A large product photograph occupies the right 50% of the section on desktop. Minimum height 420px ensures visual weight even with minimal copy.

### Badges

**`category-badge`** — Small cyan pill with uppercase white text in `{typography.badge}`. Appears above product titles in cards and on collection pages to label appliance type.

**`sale-badge`** — Orange variant of the badge pattern, placed over product card images at top-right with absolute positioning. Communicates discount percentage or "SALE" text.

**`energy-rating-badge`** — Green (#008a00) mini badge for Energy Star or efficiency ratings, using `{typography.caption-bold}` for the rating letter/value.

### Spec Row

**`spec-row`** — A label-value pair rendered in monospace (`{typography.spec-label}`), separated by a hairline bottom border. Used in product detail pages to display dimensions, capacity, voltage, and noise level in a scannable vertical list.

### Search

**`search-input`** — A 40px-tall input with left-inset magnifying-glass icon (16px from left edge), hairline border, and `{rounded.xs}` corners. On focus the border transitions to `{colors.primary}`. Placeholder text in `{colors.muted}`.

### Footer

**`footer`** — Dark near-black (#231f20) background spanning full width. Content organized in 4 columns: Products, Support, Company, Connect. Links render in `{typography.body-sm}` white text with underline on hover. A bottom strip contains copyright, legal links, and payment-method icons at reduced opacity.

### Pricing

**`price-display`** — Bold 20px Roboto in ink for standard pricing. When a sale is active, the original price renders in `{colors.muted}` with line-through decoration, and the sale price renders in `{colors.error}` (#ee0000) using the same `{typography.price}` weight.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero banner stacks image below text; search hides behind icon tap; footer collapses to accordion sections |
| Tablet | 744–1128px | Two-column product grid; nav shows top 4 categories, overflow in "More" dropdown; hero image shrinks to 40% width; spec rows remain full-width |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with search field visible; hero splits 50/50 text and image; footer in 4-column layout |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid may expand to 4 columns; increased `{spacing.section}` between major blocks |

### Touch Targets
- All interactive elements maintain minimum 44px tap target on mobile
- Product cards receive full-card tap area linking to PDP
- Nav hamburger icon padded to 48×48px hit zone
- Filter chips in collection pages spaced with `{spacing.sm}` gaps to prevent mis-taps

### Collapsing Strategy
- Navigation categories collapse into hamburger drawer below 744px; drawer slides from left with scrim overlay
- Product filters move from left sidebar to a top sheet / modal on mobile, triggered by a "Filter" button
- Hero banner reverses to image-on-top, text-below on mobile for scroll priority
- Footer columns collapse into expandable accordion sections with chevron indicators
- Comparison table (if present) converts to a horizontally scrollable card strip on mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom webfont beyond Roboto detected; the site may load a proprietary display face via JavaScript or a third-party font service that wasn't captured in static extraction
- Exact border-radius values on cards and buttons are inferred from visual pattern (4px/8px) — actual CSS values may differ slightly
- Promotional gradient directions (the orange ramp from #f58720 to #e16f27) and angle degrees could not be extracted; linear-gradient assumed at 90deg
- Modal/overlay patterns (quick-view, cart drawer) are likely JS-rendered and not captured in static hints
- Icon system (size, stroke width, library) is undetermined — the site may use an inline SVG sprite or icon font not visible in extraction
- Exact spacing scale may deviate; values are based on common Shopify theme patterns rather than measured CSS custom properties
- Dark-mode support is unknown; no prefers-color-scheme media query was detected but may exist in bundled CSS
