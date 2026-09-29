---
version: alpha
name: "Windmill Air"
source_url: "https://windmillair.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Navy at #122940 — used so consistently it surfaces in three near-identical extracted variants (#122940, #122840, #142840) — carries all structural authority at Windmill Air, and then the rest of the palette immediately contradicts the category expectation. Warm peach (#f2a682), sage green (#b2c8a1), goldenrod (#fed31d), and coral-orange (#ec5039) are colors almost no HVAC manufacturer would claim as brand property; the visual argument is that an air conditioner belongs in the same conversation as furniture, not hidden behind a radiator cover. The blue-shifted near-whites (#f7f8fb, #f2f4f7) that fill the canvas lean cool and airy, reinforcing the product promise without resorting to clinical starkness.

  Brighton Std carries all display-weight headlines — a humanist serif with gentle swash character that reads closer to a boutique hotel welcome card than an appliance spec sheet. Montserrat handles every functional UI element. The pairing is deliberate: Brighton Std in hero and PDP headlines delivers warmth, while Montserrat in uppercase with tracked-out `{typography.button-md}` labels (1px letter-spacing, 700 weight) delivers the precision a customer needs to feel confident in an HVAC purchase. Neither font is a default choice for air care retail, which is the brand's operating premise.

  Rounding is restrained: `{rounded.sm}` (8px) governs cards, inputs, and primary CTAs, staying friendly without crossing into pill-shape softness. `{colors.surface-soft}` (#f7f8fb) floats product cards off the `{colors.canvas}` grid without requiring box shadows. `{colors.surface-warm}` (#fff2d9) isolates seasonal and promotional callouts in a warm cream zone that echoes the heating-product palette without overwhelming the cooler neutrals that dominate the base layout.

  The multi-accent system appears to function as product-line segmentation: peach and coral for heating-season SKUs, sage (#b2c8a1, #e5ede0) for air quality and purification, sky (#adc4eb, #dee3f0) for cooling, and goldenrod possibly marking smart or premium tiers. This allows the same component set to communicate seasonal context through badge and chip color swaps rather than layout-level rebrands. The footer inverts to `{colors.primary}` navy with `{colors.sky}` (#adc4eb) link treatments, closing the page in the same authority register the hero opens with.

colors:
  primary: "#122940"
  primary-active: "#1c274c"
  primary-disabled: "#adc4eb"
  ink: "#122940"
  body: "#2b3d51"
  muted: "#686868"
  hairline: "#e0e0e0"
  hairline-soft: "#edeeef"
  canvas: "#fefefe"
  surface-soft: "#f7f8fb"
  surface-card: "#f2f4f7"
  surface-warm: "#fff2d9"
  on-primary: "#fefefe"
  accent-peach: "#f2a682"
  accent-peach-soft: "#f7d1c2"
  accent-coral: "#ec5039"
  accent-yellow: "#fed31d"
  accent-sage: "#b2c8a1"
  accent-sage-soft: "#e5ede0"
  sky: "#adc4eb"
  sky-soft: "#dee3f0"
  error: "#cc0000"

typography:
  display-xl:
    fontFamily: "'Brighton Std', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Brighton Std', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Brighton Std', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Brighton Std', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "'Montserrat', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Montserrat', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Montserrat', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.5px
  badge-label:
    fontFamily: "'Montserrat', system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    hoverBackgroundColor: "{colors.primary-active}"

  button-primary-outline:
    backgroundColor: transparent
    borderColor: "{colors.primary}"
    borderWidth: 2px
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px

  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    borderColor: "{colors.on-primary}"
    borderWidth: 1px
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.primary}"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 72px
    borderBottomColor: "{colors.hairline-soft}"
    borderBottomWidth: 1px

  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    imageBorderRadius: "{rounded.sm}"

  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"

  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    paddingVertical: "{spacing.sm}"
    paddingHorizontal: "{spacing.base}"

  product-line-badge:
    backgroundColor: "{colors.sky-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px

  feature-chip:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 12px

  energy-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    selectedBorderColor: "{colors.primary}"
    selectedBorderOffset: 2px

  rating-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.full}"
    padding: 4px 10px

  section-panel:
    backgroundColor: "{colors.surface-soft}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"

  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.sky}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.xl}"

---

## Components

### Buttons

**`button-primary`** — Renders `{colors.primary}` (#122940) navy with white uppercase Montserrat text tracked at 1px; at 48px tall it meets touch targets without feeling inflated. Hover darkens to `{colors.primary-active}` (#1c274c) immediately, no delay. Disabled state uses `{colors.primary-disabled}` (#adc4eb, the sky blue), which maintains brand color continuity rather than defaulting to a generic gray — a distinctive choice that keeps even disabled states on-palette.

**`button-primary-outline`** — A 2px navy border on transparent, used for secondary-priority CTAs that sit alongside photography or light-background sections without competing. Height and type treatment match `button-primary` for optical alignment in paired layouts.

**`button-secondary`** — `{colors.surface-soft}` (#f7f8fb) background with navy text; the lowest-contrast button in the system, reserved for non-critical actions like "learn more" links or filter toggles in product listings where the visual hierarchy must stay flat.

**`button-ghost`** — White text and 1px white border on transparent, for CTAs placed directly over the navy hero or lifestyle photography with a dark overlay. When context shifts to a light surface the component must switch to `button-primary-outline` — ghost on white canvas produces inaccessible contrast.

### Text Input

**`text-input`** — White canvas container with a 1px `{colors.hairline}` border at rest; focus upgrades the border to `{colors.primary}` navy with no shadow or glow. Placeholder in `{colors.muted}` (#686868). The 48px height matches button height so form-plus-CTA row layouts stay optically flush without explicit alignment overrides.

### Navigation

**`nav-bar`** — Canvas white at 72px, separated from content by a barely-there 1px `{colors.hairline-soft}` (#edeeef) bottom rule. Logo sits left in Brighton Std; category product links run center in `{typography.nav-label}` (Montserrat 13px, 600 weight, 0.5px tracking, not uppercased at this scale); cart and account icons anchor right. The bar does not change on scroll — no sticky background color shift — trusting layout hierarchy to handle page orientation.

### Product Card

**`product-card`** — `{colors.surface-soft}` (#f7f8fb) container at `{rounded.md}` (12px) rounding; the product image fills a `{rounded.sm}` inset with a controlled aspect ratio that avoids letterboxing on the brand's taller unit photography. Product name in `{typography.title-md}` (Montserrat 18px/600) runs in ink navy; price in `{typography.price-display}` (Brighton Std 24px/400) gives the number humanist warmth that stands apart visually from the surrounding sans-serif metadata. Feature chips and product-line badges nest below the title, keeping specification data separated from editorial name text.

### Hero Section

**`hero-section`** — Full-bleed `{colors.primary}` navy with headline in `{typography.display-xl}` (Brighton Std 56px, weight 400). The display serif at a light weight on dark navy is the brand's highest-contrast brand-voice moment — wide, unhurried, unmistakably intentional. Body copy in `{typography.body-md}` white; primary CTA uses `button-ghost` so the button reads on the dark field. The hero may alternatively use lifestyle photography with a dark overlay rather than flat navy, with identical type treatment.

### Announcement Bar

**`announcement-bar`** — A 36px-tall navy strip at the very top of the viewport using `{typography.caption}` (Montserrat 12px, medium weight) in white. Used for shipping promotions, seasonal offers, or smart-home partnership callouts. The navy matches the footer inversion, framing the full page in primary color at both vertical extremes.

### Product-Line Badge

**`product-line-badge`** — Small rectangular tag at `{rounded.xs}` in `{colors.sky-soft}` (#dee3f0) with `{typography.badge-label}` navy uppercase text. Applied to product cards to signal category membership. The sky-soft default encodes the cooling category; heating-line products should override `backgroundColor` to `{colors.accent-peach}` (#f2a682); air-quality products to `{colors.accent-sage-soft}` (#e5ede0). The component spec is stable; only the fill token swaps.

### Energy Badge

**`energy-badge`** — `{colors.accent-sage}` (#b2c8a1) background with navy `{typography.badge-label}` text at `{rounded.xs}`. Used for ENERGY STAR certifications or efficiency ratings. The sage green carries environmental meaning without requiring an icon glyph, keeping the badge compact enough to sit inline on a product card without dominating.

### Feature Chip

**`feature-chip`** — `{colors.surface-warm}` (#fff2d9) pill at `{rounded.full}` with navy `{typography.caption}` text. Used on PDP pages to enumerate product specs ("Wi-Fi enabled", "2,000 sq ft", "48 dB") in a format that is scannable but warmer than a bulleted list. The warm cream background distinguishes feature chips from product-line badges and rating chips using shape and fill simultaneously.

### Rating Chip

**`rating-chip`** — Canvas white, 1px `{colors.hairline}` border, `{rounded.full}` pill, navy `{typography.caption}` text. Displays star count and review count inline. The pill shape deliberately contrasts with the square product-line badge, marking the chip as social proof rather than specification data — the shape itself communicates the information type.

### Color Swatch

**`color-swatch`** — 24px circle at `{rounded.full}` with a 1px `{colors.hairline}` border at rest. Selected state adds a 2px `{colors.primary}` ring offset by 2px, preventing the swatch fill color from bleeding into the selection indicator. Used on PDP for product finish or color options; the 24px visual size expands to a 44px tap target via invisible padding on touch devices.

### Footer

**`footer`** — Full-width `{colors.primary}` navy inversion. Column headings in `{typography.title-sm}` (Montserrat 13px, 700 weight, 0.8px tracking, uppercase) in white. Body links render in `{colors.sky}` (#adc4eb), which is legible on navy without the clinical brightness of pure white and ties the footer link treatment back to the cooling product palette. Legal and copyright text runs `{typography.caption}` in a reduced-opacity white or muted treatment at the bottom row.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark only; hero headline drops to `{typography.display-sm}` (28px); product-line badge filters in horizontal scroll row rather than wrapping |
| Tablet | 744–1128px | Two-column product grid; nav shows category links but drops utility icon labels; hero at `{typography.display-md}` (36px); announcement bar single line, truncated if overflow |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links and cart/account icons; hero at `{typography.display-xl}` (56px); `{spacing.section}` (64px) vertical padding on section panels |
| Wide | > 1440px | Layout max-width caps at 1440px and centers; side gutters expand proportionally; hero photography bleeds full viewport width but text block stays within max-width container |

### Touch Targets

- All buttons hold 48px minimum tap height including `button-ghost` on mobile
- Color swatches are 24px visual but padded to 44px tap target
- Nav category links in mobile drawer maintain 48px row height
- Rating chips and feature chips expand to 36px minimum tappable height when interactive
- Announcement bar close button (if present) minimum 44×44px

### Collapsing Strategy

- Navigation: hamburger drawer on mobile; full horizontal bar at tablet and above; no mega-menu revealed in extraction
- Product grid: 1-col → 2-col → 3-col at the two breakpoints above
- Hero: stacked (image top, text below) on mobile; side-by-side split at tablet; full-bleed with text overlay at desktop
- Feature chip rows on PDP: horizontal scroll on mobile to avoid wrapping-induced layout breaks
- Footer: 2-column stacked grid on mobile → 4-column horizontal layout at desktop; legal row always full width

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Brighton Std is not a web-standard or Google Fonts typeface — weight variants beyond 400 (regular) are unconfirmed; bold/medium variants may exist but were not enumerated in extraction
- Montserrat weights in active use on the live site could not be confirmed; 400/500/600/700 assumed from standard Shopify theme deployment patterns
- Button and card border-radius values are inferred from color extraction context, not direct CSS property reads; `{rounded.sm}` (8px) is a best-fit estimate
- The product-line color segmentation hypothesis (peach = heating, sage = air quality, sky = cooling, yellow = smart tier) is inferred from palette clustering, not confirmed by site taxonomy or navigation copy
- Meta theme-color was not set, leaving mobile browser chrome color undefined — likely defaults to white or the OS system color
- Dark mode tokens: no evidence of dark mode implementation was extracted
- Exact PDP layout (image carousel behavior, sticky add-to-cart bar, accordion specs section) could not be confirmed from extraction data
- Spacing scale is a reasonable 8px-base convention; actual Shopify theme internal spacing values were not confirmed
- `#1f3438`, `#233437` (very dark teals in the extraction) appear adjacent to product photography and may represent environmental or background image treatments rather than UI tokens — their role is unconfirmed
