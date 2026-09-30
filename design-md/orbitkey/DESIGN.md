---
version: alpha
name: "Orbitkey"
source_url: "https://www.orbitkey.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A single marigold stripe (#ffcf2a) cuts through an otherwise near-monochrome system — it appears on the primary CTA, as the thin 2px underline beneath active nav links, and as the column heading color inside a dark navy footer, while every surrounding surface holds to a charcoal-to-off-white band from #373737 down to #f8f8f8. Suisse Intl, the typeface of Swiss precision manufacturing, carries all text at near-zero letter-spacing: weight 700 for the wordmark and display headings, weight 600 for product names and CTAs, weight 400 for running copy — the scale is narrow by design, letting spatial hierarchy do what weight contrast might otherwise overwork. The secondary palette adds two chromatic punctuation marks: #3c55e4 (electric blue) marks sale callouts and interactive focus rings, while #b2f9e9 (mint) surfaces on eco-material badges and success confirmations — brief flashes of color in a system that otherwise earns its chromatic restraint.

  Product imagery sits at 1:1 on a #f4f4f4 near-white field that dissolves product edges into the background. Cards have no visible stroke at rest; hover lifts them 4px with a 200ms ease shadow. The grid runs 3-up on desktop, collapsing cleanly to 2-up on tablet and single-column on mobile. Component corners apply a consistent {rounded.sm} (8px) across cards, inputs, and modals — enough to signal modernity. Buttons are squarer at {rounded.xs} (4px), a deliberate step toward industrial, tool-grade precision. Navigation sits fixed over hero video in transparent mode, switching to a #f8f8f8 solid with a 1px {colors.hairline} bottom stroke on scroll. An announcement bar above the nav runs the only UI context where marigold appears as background: {colors.primary} text reversed on a {colors.navy} field. Micro-interactions are clipped at 150ms with no spring or overshoot — the same no-flourish signal that runs through every detail.

colors:
  primary: "#ffcf2a"
  primary-active: "#ffc025"
  primary-disabled: "#e5d98a"
  ink: "#373737"
  body: "#515151"
  muted: "#9a9db1"
  ink-soft: "#676986"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#f8f8f8"
  on-primary: "#272d45"
  navy: "#272d45"
  navy-deep: "#2c3e50"
  accent-blue: "#3c55e4"
  accent-blue-vivid: "#0b02ff"
  accent-mint: "#b2f9e9"
  near-black: "#010101"
  lavender-gray: "#676986"

typography:
  display-xl:
    fontFamily: "'Suisse Intl', Montserrat, 'Instrument Sans', -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Suisse Intl', Montserrat, 'Instrument Sans', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-upper:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  wordmark:
    fontFamily: "'Suisse Intl', Montserrat, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: -0.3px

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
    padding: 14px 28px
    height: 48px
    transition: background 150ms ease
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1px solid {colors.accent-blue}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.wordmark}"
    logoColor: "{colors.ink}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    activeUnderlineColor: "{colors.primary}"
    activeUnderlineHeight: 2px
  nav-bar-transparent:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    logoColor: "{colors.canvas}"
    borderBottom: none
  announcement-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.primary}"
    typography: "{typography.label-upper}"
    height: 40px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1:1"
    imageBgColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "{spacing.base}"
    shadow: none
    shadowHover: "0 4px 16px rgba(0,0,0,0.08)"
    transition: box-shadow 200ms ease
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-card-sale-badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xxl}"
    accentRule: "{colors.primary}"
    accentRuleHeight: 3px
  hero-cta-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderActive: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.ink}"
    backgroundActive: "{colors.surface-soft}"
    padding: 8px 12px
    height: 40px
    disabledOpacity: 0.4
  eco-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.navy}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  section-heading:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
    accentUnderline: "{colors.primary}"
    underlineHeight: 3px
    marginBottom: "{spacing.xl}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: none
    focusBorder: "1px solid {colors.accent-blue}"
    padding: 10px 20px
    height: 44px
    iconColor: "{colors.muted}"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    size: 18px
  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.ink-soft}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    headingColor: "{colors.primary}"
    dividerColor: "{colors.ink-soft}"
    dividerOpacity: 0.3
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Renders in Orbitkey's marigold (#ffcf2a) with dark navy text (`{colors.on-primary}`) at 48px tall and a square-edged {rounded.xs} (4px) radius that reads as precision tooling, not consumer softness. Padding runs 14–28px to feel substantial without ballooning. Hover transitions to the deeper amber (`{colors.primary-active}`, #ffc025) in exactly 150ms with no easing curve theatrics — it snaps. Disabled state washes to `{colors.primary-disabled}` at 0.6 opacity. This is the only consistently yellow element on most product pages; its scarcity makes it unmissable.

**`button-secondary`** — White canvas with a 1px charcoal (`{colors.ink}`) border stroke, matching 48px height. Paired beside the primary CTA for secondary actions such as "Add to wishlist" or "Compare." Hover fills with `{colors.surface-soft}` at 150ms. The matching height means button pairs read as intentional equals, not hierarchy.

**`button-ghost`** — Transparent background, ink text, same 4px radius. Used for inline tertiary actions: size guide links, filter resets, "See all" anchors. Hover tints with `{colors.surface-soft}`.

**`hero-cta-primary`** — The hero-specific variant stretches to 52px tall (vs the standard 48px) with wider 32px horizontal padding, scaled to the visual weight of the full-bleed hero context. Same marigold-on-navy treatment.

### Navigation

**`nav-bar`** — Fixed at 64px. Over the hero, renders as `nav-bar-transparent` with white text against dark video. On first scroll pixel, snaps to `{colors.surface-card}` (#f8f8f8) with a 1px `{colors.hairline}` bottom stroke — no animation, a deliberate hard cut. Left: wordmark in `{typography.wordmark}` weight 700. Center: category links in `{typography.nav-link}` 14px, with a 2px `{colors.primary}` underline on the active item — the only decoration in the nav. Right: search, cart (with `cart-badge`), and account icons at 24px wrapped in 44px tap zones. Megadropdowns emerge as full-width white panels with `{rounded.sm}` on the lower two corners only.

**`announcement-bar`** — A 40px strip pinned above the nav. The only context in the UI where `{colors.primary}` is a background: here it inverts, placing white or navy text on marigold, or — more commonly — marigold `{typography.label-upper}` on `{colors.navy}`. Reserved for shipping thresholds, limited drops, and countdown messaging.

### Product Cards

**`product-card`** — 1:1 image on a `{colors.surface-soft}` field with `{rounded.sm}` corners and no border at rest. Title in `{typography.title-sm}`, price in `{typography.price}`, optional descriptor line in `{typography.caption}` at `{colors.muted}`. On hover, a 4px vertical lift appears via box-shadow in 200ms ease — the only animated effect on the card. Badges (`product-card-badge` in marigold for NEW/BEST SELLER; `product-card-sale-badge` in electric blue for SALE) anchor as flush-corner rectangles to the image top-left with zero border-radius, visually distinct from every other rounded element on the page.

### Hero Section

**`hero-section`** — Full-bleed `{colors.navy}` panel, typically housing product video or high-contrast lifestyle imagery. Heading in `{typography.display-xl}` (white), max-width 600px, left-aligned. A 3px horizontal `{colors.primary}` rule separates the heading from the subhead as a typographic anchor. Subhead runs `{typography.body-md}` at 70% opacity. The CTA uses `hero-cta-primary` — the 52px tall yellow block is the single warm pixel on an otherwise dark-navy field.

### Product Detail Selectors

**`color-swatch`** — 24px circular chips at `{rounded.full}`, spaced at `{spacing.xs}`. Inactive: 2px transparent border. Active: 2px `{colors.ink}` border with a 2px white inset gap, creating a floating-dot-in-ring that reads clearly at small size. Out-of-stock swatches carry a diagonal CSS strikethrough line.

**`size-selector`** — Rectangular pills at 40px height with `{rounded.xs}`, bordered by `{colors.hairline}`. Active switches to a 1px `{colors.ink}` border on a `{colors.surface-soft}` fill. Disabled sizes render at 0.4 opacity with pointer-events: none.

### Badges & Labels

**`eco-badge`** — Mint background (`{colors.accent-mint}`, #b2f9e9) with `{colors.navy}` text in `{typography.label-upper}`. Applied to products made from recycled or bio-sourced materials. Sits inline in the product title area or overlaid on image. The mint is the only color in the palette with no direct ancestor in the charcoal-to-yellow axis — its freshness signals environmental category without competing with the primary marigold.

**`product-card-badge`** / **`product-card-sale-badge`** — Square-corner label chips. Marigold for editorial badges (NEW, BEST SELLER). Electric blue (#3c55e4) for transactional badges (SALE, % OFF). The two never appear simultaneously on one card.

**`section-heading`** — Display heading in `{typography.display-sm}` with a 3px `{colors.primary}` underline rule anchored below the last character. The rule is short (not full-width) — approximately the width of the text — reading as a signature rather than a divider.

### Search

**`search-input`** — Pill-shaped (`{rounded.full}`), 44px, `{colors.surface-soft}` fill with no border at rest. Focus adds a 1px `{colors.accent-blue}` ring — the only moment electric blue appears in a form context rather than a badge. Used inside a full-screen overlay triggered by a nav icon; not embedded inline.

### Cart & Quantity

**`cart-badge`** — 18px circular dot at `{rounded.full}` in `{colors.primary}`, absolute-positioned top-right on the cart icon. Scales from 0.5 to 1 on item-add animation.

**`quantity-stepper`** — Inline −/+ control with `{colors.surface-soft}` background and `{colors.hairline}` border at `{rounded.xs}`, 44px tall. Stepper buttons sit at the outer edges; the count field spans the center.

### Footer

**`footer`** — Full-bleed `{colors.navy}`. Column headings in `{typography.label-upper}` at `{colors.primary}` — the marigold reappears here as the only warm note in a dark field, linking the footer's information architecture to the primary CTA color. Body links in `{typography.body-sm}` at `{colors.ink-soft}`, shifting to `{colors.canvas}` on hover. Social icons are 20px mono-white SVGs. A 1px `{colors.ink-soft}` horizontal rule at 30% opacity separates link columns from the legal strip.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart only; hero drops to 400px min-height with full-width CTA; announcement bar wraps to 2 lines at 36px; color swatch row-wraps |
| Tablet | 744–1128px | 2-column product grid; nav shows wordmark + icons, category links behind hamburger; hero text relaxes to 100% max-width; size selector pills allow horizontal scroll |
| Desktop | 1128–1440px | 3-column product grid; full nav with center category links and megadropdown; hero side-by-side text + product render; section-heading accent rule visible |
| Wide | > 1440px | Max-width container at 1400px centered; product grid stays 3-up with larger gutters ({spacing.xxl}); footer goes 5-column; hero adds decorative secondary rule element |

### Touch Targets

- Nav icons (search, cart, account, hamburger) wrapped in 44×44px tap zones regardless of visual icon size
- Color swatches are 24px visual but sit inside 36px tap zones with 6px gap between
- Size selector pills minimum 40px height, 64px minimum width on mobile
- Quantity stepper −/+ areas expand to 44×44px on mobile, 36×36px on desktop

### Collapsing Strategy

- Primary nav links collapse into a full-screen slide-in drawer: `{colors.navy}` background, white links, `{colors.primary}` active state underline preserved
- Megadropdown becomes a stacked accordion inside the drawer with `{colors.hairline}` dividers
- Product filter sidebar becomes a bottom-sheet modal on mobile (slides up from bottom, 80vh max, `{rounded.lg}` on upper corners)
- Announcement bar remains visible on mobile but reduces from 40px to 36px height; copy truncates with ellipsis if needed
- Hero video pauses and falls back to poster image on reduced-motion or low-bandwidth conditions

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font weight availability within the Suisse Intl license not confirmed — fallbacks to Montserrat at matching weights are assumed; if Suisse Intl is not licensed, Montserrat at weight 500/600/700 closely approximates the proportions
- The `oke-widget-icons` font found in the stack is a proprietary icon font (likely for the Okendo review widget) — icon naming, sizing, and usage conventions for Orbitkey's own UI icons not captured
- Megadropdown column count, imagery treatment, and featured-product placement not observed in extraction
- Dark-mode variant not detected; `{colors.navy}` panels and the footer may be the only dark surfaces intentionally used
- Hover animation easing curves (cubic-bezier values) not captured; 150ms ease used as a reasonable default throughout
- Form validation error states (color, inline message position, icon usage) not observed in extraction
- Product video player custom controls styling and brand-styled progress bar not captured
- Loyalty or rewards program UI treatment (if any) not observed
- Exact cart drawer vs. full-page cart routing behavior not confirmed
- Mobile nav drawer slide direction (left or right) not confirmed from extraction
