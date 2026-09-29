---
version: alpha
name: "Barebones Living"
source_url: "https://barebonesliving.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Barebones Living stakes its identity on restraint as a design principle, not a budget constraint — "Beautiful. Durable. Essential." functions less like a tagline and more like an editing filter that strips every element to its minimum load-bearing form. The palette opens on a field-worn amber (#9e703c) that reads like a seasoned ash tool handle or sun-cured linseed oil, then deepens through a chain of honest browns (#8c5f27, #71491d, #58370f) before closing in near-charcoal ink (#1c1c1c). A second chromatic axis runs cool and maritime: the site's declared meta theme-color is a measured slate blue (#748cab), and the primary navigation shell settles into a dense navy-charcoal (#272d45) that carries the weight of an overcast Pacific Northwest sky rather than the warmth of the tool palette. Warm cream (#ddcfbe) and bleached field neutrals (#f4f4f6, #f8f8f8) give product photography its breathing room. The only live voltage in the system is a pair of high-energy oranges — #ff763d and #f04600 — that surface on sale callouts and promotional states, appearing like a camp lantern lit against dark canvas, which is precisely the brand's signature product category. Typography layers Futura's geometric exactness at display scale against the custom mauritius and mauritius-cond cuts for editorial headlines; brandon-grotesque handles the running body. Three families that span from precision-machined to warmly utilitarian. Buttons carry minimal rounding ({rounded.sm}), product cards hold their corners nearly flat ({rounded.xs}), and there are no decorative gradients, no illustrative flourishes, no drop shadows — only grid structure and generous spacing that lets materials photography carry the argument. The digital surface mirrors the tools: remove everything that doesn't bear a load, then trust what's left.

colors:
  primary: "#9e703c"
  primary-active: "#71491d"
  primary-disabled: "#d8c6b1"
  accent: "#ff763d"
  accent-deep: "#f04600"
  ink: "#1c1c1c"
  body: "#2a2f37"
  muted: "#5d5d5d"
  muted-soft: "#9a9db1"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#f8f8f8"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  surface-warm: "#ddcfbe"
  on-primary: "#f8f8f8"
  on-dark: "#f8f8f8"
  slate: "#748cab"
  slate-dark: "#272d45"
  slate-mid: "#676986"
  terracotta: "#94553a"
  scrim: "#171717"

typography:
  display-xl:
    fontFamily: "'mauritius', 'Futura', 'brandon-grotesque', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'mauritius', 'Futura', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'mauritius-cond', 'Futura', sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'mauritius-cond', 'Futura', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'brandon-grotesque', 'Futura', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'brandon-grotesque', 'Futura', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'brandon-grotesque', 'ITC Johnston', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'brandon-grotesque', 'ITC Johnston', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'brandon-grotesque', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  caption-label:
    fontFamily: "'brandon-grotesque', 'Futura', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'brandon-grotesque', 'Futura', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'brandon-grotesque', 'Futura', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'brandon-grotesque', 'Futura', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.8px
    textTransform: uppercase
  price:
    fontFamily: "'brandon-grotesque', 'Futura', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0
  price-sm:
    fontFamily: "'brandon-grotesque', 'Futura', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  badge:
    fontFamily: "'brandon-grotesque', 'Futura', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    border: none
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.ink}"
    hoverBackgroundColor: "{colors.ink}"
    hoverTextColor: "{colors.on-dark}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    hoverBackgroundColor: "{colors.accent-deep}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocused: "1.5px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.slate-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    logoColor: "{colors.on-dark}"
    borderBottom: none
    padding: "0 {spacing.xxl}"
    linkHoverColor: "{colors.slate}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    height: 36px
    padding: "0 {spacing.base}"
    textAlign: center
  announcement-bar-sale:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-label}"
    height: 36px
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    imageAspect: "4/5"
    imageFit: cover
    padding: "{spacing.md}"
    shadow: none
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    textColor: "{colors.ink}"
    mutedTextColor: "{colors.muted}"
    hoverImageScale: 1.04
    transition: "transform 300ms ease"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-badge-new:
    backgroundColor: "{colors.slate-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  material-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary-active}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
    border: "1px solid {colors.primary-disabled}"
  hero:
    backgroundColor: "{colors.slate-dark}"
    overlayColor: "rgba(23,23,23,0.40)"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 85vh
    contentMaxWidth: 600px
    contentPaddingLeft: "{spacing.xxl}"
    buttonStyle: "button-primary"
  hero-split:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    imageColumn: "50%"
    contentColumn: "50%"
    padding: "{spacing.section} {spacing.xxl}"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    descriptionColor: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  feature-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.title-sm}"
    iconColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
    gap: "{spacing.xxl}"
  testimonial-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    authorTypography: "{typography.caption-label}"
    authorColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    border: none
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    focusBorder: "1.5px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
    minWidth: 120px
    iconColor: "{colors.ink}"
  swatch:
    size: 28px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderUnselected: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline-soft}"
    padding: "{spacing.md} 0"
  footer:
    backgroundColor: "{colors.slate-dark}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.slate}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.slate}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: none
    dividerColor: "{colors.slate-mid}"

## Components

### Buttons
**`button-primary`** — The primary CTA carries the brand amber (#9e703c) fill on a near-white (#f8f8f8) letterpress-spaced uppercase label. On hover, it deepens to the primary-active dark brown (#71491d); disabled states render in the warm cream (#d8c6b1) with muted text so the form element stays legible without inviting interaction. Height is fixed at 48px with 28px horizontal padding and a barely-there 4px radius — substantial enough to read as a button, flat enough to look like it was made rather than designed.

**`button-secondary`** — Transparent fill with a 1.5px ink border and the same uppercase tracking as primary. On hover the button inverts to solid ink with light text, which reinforces the brand's preference for maximum contrast over intermediate states. Used for "Add to Wishlist" and secondary product actions.

**`button-ghost`** — Mirrors secondary in weight and size but uses the brand amber (#9e703c) for its border and label, filling amber on hover. Appears on warm-background sections where ink would compete with body copy.

**`button-accent`** — The lantern-orange (#ff763d) fill reserved for sale countdowns, promotional overlays, and urgency moments. Deepens to #f04600 on hover. Never used as a primary CTA outside promotional contexts — it would dilute the amber brand signal.

### Navigation
**`nav-bar`** — Deep navy-charcoal (#272d45) shell at 64px tall with 1.8px-tracked all-caps white links. The darkness of the nav bar against the lighter product content below creates immediate visual hierarchy — the shell recedes and product imagery advances. Cart icon count badge uses the accent orange. On scroll the bar remains fixed; no background blur or opacity tricks.

**`announcement-bar`** — 36px amber strip pinned above the nav for shipping promotions and site-wide messages, swapping to the accent orange (#ff763d) during sale events. All-caps caption-label type at 11px/1.5px tracking keeps it legible without overwhelming.

### Product Card
**`product-card`** — Near-square image crop at 4:5 aspect, near-flat 2px radius, no shadow. On hover the image scales 1.04× over 300ms — enough motion to confirm interactivity without theatrical zoom. Price renders in the weighted price scale (18px/700), category tag in caption-label uppercase. Sale and New badges sit flush to the top-left image corner in their respective fills with zero border radius, stamped rather than floated.

### Badges & Labels
**`material-badge`** — A surface-warm (#ddcfbe) chip with dark amber text and a hairline primary-disabled border, used on PDP pages to call out material specs: "High Carbon Steel", "FSC Certified Wood", "Powder Coated". Zero radius — these read as specification stamps, not decorative tags. The warm cream grounds them in the brand's earthy material vocabulary rather than the clinical gray most spec labels use.

### Hero
**`hero`** — Full-bleed image with a 40% dark scrim, left-anchored content column capped at 600px. Headline in mauritius display-xl (56px) at 1.05 line-height presses the typography into the image rather than floating over it. A single button-primary sits below a one-sentence subhead in body-md. On mobile, the content shifts to bottom-anchored with bottom padding for thumb reach.

**`hero-split`** — For secondary landing pages — a 50/50 split with a product photograph on one side and copy on the other on a soft canvas (#f4f4f6) background. No scrim needed; the image is full-height cropped. Headline runs display-md (36px). Used for category introductions and editorial stories.

### Feature Strip
**`feature-strip`** — A horizontal row of three to four icon + label + description cells, separated by hairline borders above and below, no outer padding. Icon set uses the brand amber. Label in title-sm (uppercase, 1.5px tracking), description in body-sm at muted text color. Common cells: "Lifetime Guarantee", "Free Shipping Over $75", "American Designed". No card background — the strip floats directly on the page canvas.

### Testimonial Card
**`testimonial-card`** — Surface-warm (#ddcfbe) fill in a 4px-radius card with no border. Quote in body-md ink, attribution in caption-label muted uppercase. The cream background pulls visually from the brand's leather and linen material world, distinct from the cooler surface-soft used for collection headers. Typically arranged in a 3-column row on desktop.

### Footer
**`footer`** — Full-width navy-charcoal (#272d45) block. Section headings in the title-sm uppercase scale at slate (#748cab) — cooler than the on-dark white of body links, creating a two-tier readability hierarchy without needing bold or size contrast. Logo reproduced in white above the column grid. The footer does not repeat the amber palette; the dark shell closes the page at the same chromatic temperature as the navigation, framing product content between two dark bands.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero content bottom-anchored with larger padding; nav collapses to hamburger with full-height drawer on slate-dark; announcement bar truncates with ellipsis; feature strip stacks vertically; buttons full-width on PDP |
| Tablet | 744–1128px | Two-column product grid; hero maintains left-anchor; nav shows abbreviated links with overflow drawer; split hero collapses to stacked image-above, text-below |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav link row visible; hero content column max 600px; feature strip horizontal row |
| Wide | > 1440px | Content max-width 1440px centered with auto margins; hero image extends edge to edge behind constrained content column; product grid remains four-column |

### Touch Targets
- All interactive controls minimum 44×44px on mobile (buttons, swatches, quantity selectors)
- Swatch tap target padded to 36px even if visual size is 28px
- Nav hamburger icon hit area 48×48px
- Footer links padded to minimum 40px vertical touch height

### Collapsing Strategy
- Nav: full bar → hamburger drawer (slate-dark fill, full viewport height, links in display-sm scale)
- Product grid: 4 → 3 → 2 → 1 columns at wide / desktop / tablet / mobile breakpoints
- Feature strip: horizontal row → 2×2 grid → vertical stack
- Hero split: side-by-side → stacked (image first, content below) at tablet
- Testimonial row: 3-col → 2-col → single scrollable carousel snap at mobile
- Footer columns: 4-col → 2-col → 1-col stacked

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted button border-radius directly observed; 4px inferred from brand's anti-ornament posture and typical Shopify theme defaults
- Font weight specifics for mauritius and mauritius-cond unavailable — weights estimated from general display-font conventions; confirm 700 availability in the mauritius font files
- No confirmed line-height or letter-spacing values from CSS extraction; all typography metrics are inferred from visual analysis of the brand category and font family conventions
- Exact nav height and padding not extracted; 64px estimated from typical Shopify header structure
- Color usage split between primary amber and the blue-slate axis not fully mapped — unclear which is dominant in primary CTA contexts without direct computed-style extraction (amber chosen as primary given "most distinctive" ranking)
- Icon library not identified; oke-widget-icons detected is a third-party review widget (OKendo), not the brand's own icon system
- Animation easing curves and durations not extracted; transition values are conventional estimates
- Mobile-specific typography scale not extracted; values represent proportional reductions from desktop scale
