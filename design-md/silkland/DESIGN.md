---
version: alpha
name: "Silkland"
source_url: "https://www.silkland.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Two gradient stops — #4e54c8 deep indigo and #8f94fb periwinkle — constitute the entire extracted chromatic identity of Silkland, a cables-and-adapters brand that chose a palette more at home in a fintech dashboard or SaaS onboarding screen than on accessory packaging. The indigo-to-lavender sweep fires across primary CTAs and hero surfaces, replacing the metallic grays and safety-red accents that crowd the cable category with something cooler and more metropolitan. Against that violet wash, white canvas (`{colors.canvas}`) and the near-ghost `{colors.surface-soft}` carry product photography and compatibility grids without competing. The font stack is purely system — Geneva leads, followed by Segoe UI, Tahoma, and Verdana — meaning renders vary by platform: slightly warmer and condensed on macOS, crisper on Windows. Rather than fighting this, the design leans on weight contrast (700 for headings, 400 for body) and conservative line-heights to maintain hierarchy across environments without a custom typeface.

  Compatibility chips are the signature micro-component: uppercase, tightly spaced labels set at `{typography.chip-label}` inside a `{rounded.full}` pill, cycling through the full language of modern connectivity — USB-C, Thunderbolt 4, MFi-certified, 240W. They appear on product cards and in the hero, functioning simultaneously as specification badges and filter handles. Product cards rest at `{rounded.md}` on `{colors.surface-card}`, soft enough to suggest approachability without erasing the precision hardware buyers expect from a spec table. The footer grounds the page in `{colors.ink}`, an indigo-tinted near-black that echoes the primary hue and closes the vertical gradient arc the hero opens at the top. Search takes a `{rounded.full}` pill form that mirrors the CTA language — a consistent rounding vocabulary that makes the interface feel single-authored even under system-font variability.

colors:
  primary: "#4e54c8"
  primary-gradient-end: "#8f94fb"
  primary-active: "#3a40b0"
  primary-disabled: "#b4b7f0"
  ink: "#1c1c3a"
  body: "#3d3d5c"
  muted: "#6b6b8f"
  hairline: "#dddde8"
  hairline-soft: "#ededf5"
  canvas: "#ffffff"
  surface-soft: "#f4f4fb"
  surface-card: "#ffffff"
  surface-strong: "#eaeaf5"
  on-primary: "#ffffff"
  success: "#2ec27e"
  warning: "#f5a623"
  error: "#e53e3e"

typography:
  display-xl:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  chip-label:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.6px
    textTransform: uppercase
  price-display:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  section-eyebrow:
    fontFamily: "Geneva, 'Segoe UI', Tahoma, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
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
    background: "linear-gradient(135deg, {colors.primary}, {colors.primary-gradient-end})"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    background: "linear-gradient(135deg, {colors.primary-active}, {colors.primary})"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoGradient: "linear-gradient(135deg, {colors.primary}, {colors.primary-gradient-end})"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageBorderRadius: "{rounded.sm}"
    hoverShadow: "0 4px 16px rgba(78,84,200,0.12)"
  hero-banner:
    background: "linear-gradient(135deg, {colors.primary}, {colors.primary-gradient-end})"
    textColor: "{colors.on-primary}"
    paddingY: "{spacing.section}"
    paddingX: "{spacing.xl}"
    titleTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
  compat-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.chip-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
    border: "1px solid {colors.hairline}"
  compat-chip-active:
    background: "linear-gradient(135deg, {colors.primary}, {colors.primary-gradient-end})"
    textColor: "{colors.on-primary}"
    typography: "{typography.chip-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  spec-row:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} 0"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.primary}"
    padding: 10px 18px
    height: 44px
  category-filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.chip-label}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
  category-filter-chip-active:
    background: "linear-gradient(135deg, {colors.primary}, {colors.primary-gradient-end})"
    textColor: "{colors.on-primary}"
    typography: "{typography.chip-label}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: none
  section-eyebrow:
    textColor: "{colors.primary}"
    typography: "{typography.section-eyebrow}"
    marginBottom: "{spacing.sm}"
  price-block:
    priceColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    originalColor: "{colors.muted}"
    originalTypography: "{typography.body-sm}"
    originalTextDecoration: line-through
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.chip-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.chip-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary-gradient-end}"
    linkHoverColor: "{colors.on-primary}"
    padding: "{spacing.xxl} 0"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — The primary action button carries the brand's defining gesture: a 135° gradient from #4e54c8 to #8f94fb, rendered on a `{rounded.sm}` 6px corner at 44px height. Hover shifts the gradient to reverse-direction `button-primary-active`, darkening the indigo anchor to #3a40b0 for clear depth cue. Disabled state washes the fill to `{colors.primary-disabled}` at 60% opacity, keeping the indigo family without suggesting interactivity. All text is `{colors.on-primary}` white at `{typography.button-md}` weight 600.

**`button-secondary`** — A white fill with a 1.5px `{colors.primary}` border and matching indigo text functions as a low-emphasis alternative that stays on-brand without gradient saturation. Active state fills to `{colors.surface-strong}` and deepens border and text to `{colors.primary-active}`. This button pairs with `button-primary` on product pages — Add to Cart primary, Compare secondary.

**`button-ghost`** — Transparent background with `{colors.primary}` text and `{typography.button-sm}` handles inline navigation actions: "View all," "See specs," category pivots. No border; hover adds a `{colors.surface-soft}` fill.

### Text Input

**`text-input`** — 44px input fields sit on `{colors.canvas}` with a 1px `{colors.hairline}` border at `{rounded.sm}`. Focus upgrades the border to 1.5px `{colors.primary}` with no box-shadow — clean and direct. Placeholder text uses `{colors.muted}` to avoid false completion cues.

### Navigation

**`nav-bar`** — The 60px bar stays `{colors.canvas}` white with a 1px `{colors.hairline}` bottom border. Links render at `{typography.nav-link}` weight 500. The logo mark uses the gradient as its fill — the only gradient element in the bar. A `{rounded.full}` search pill sits in the center or right cluster depending on breakpoint.

### Product Card

**`product-card`** — Cards are `{rounded.md}` containers on `{colors.surface-card}` with a 1px `{colors.hairline}` border that steps up to a `box-shadow: 0 4px 16px rgba(78,84,200,0.12)` on hover, pulling from the primary indigo. Product image occupies the top two-thirds with `{rounded.sm}` clipping. Below: product name at `{typography.title-sm}`, compat chips, price block, and an Add to Cart button.

### Hero Banner

**`hero-banner`** — Full-width gradient panel using the same 135° indigo-to-lavender sweep as the primary button, establishing the gradient as the brand's loudest surface rather than a UI accent. Headline at `{typography.display-xl}` and subhead at `{typography.body-md}` both render in `{colors.on-primary}`. A white `button-secondary`-styled CTA floats over the gradient, keeping contrast accessible.

### Compatibility Chips

**`compat-chip`** — Small `{rounded.full}` pills at `{typography.chip-label}` (11px, 700 weight, 0.5px tracking, uppercase) display protocol labels — USB-C, Thunderbolt 4, 240W, MFi Certified. Default state is `{colors.surface-soft}` fill with `{colors.primary}` text and a 1px `{colors.hairline}` border. When used as active filter controls (`compat-chip-active`), they flip to the brand gradient — the same vocabulary as the primary button, reading as "selected." Chips wrap across two rows on mobile before collapsing behind a "More" expander.

### Spec Row

**`spec-row`** — Alternating rows in product spec tables: an uppercase `{typography.spec-label}` label in `{colors.muted}` on the left, body value in `{colors.ink}` at `{typography.body-sm}` on the right. A 1px `{colors.hairline-soft}` bottom border separates rows. No zebra striping — the hairline is sufficient and keeps the surface clean.

### Search Bar

**`search-bar`** — A `{rounded.full}` pill on `{colors.surface-soft}` with 1px `{colors.hairline}` border, 44px tall. The pill shape echoes CTA language — both the primary button and this input speak the same rounded vocabulary. Focus border upgrades to 1.5px `{colors.primary}`. A magnifying-glass icon in `{colors.muted}` sits at the left inset; on submit, it activates in `{colors.primary}`.

### Category Filter Chips

**`category-filter-chip`** / **`category-filter-chip-active`** — Full-width filter rail on category and search pages. Inactive chips are white with `{colors.hairline}` borders; active chips fill with the gradient and drop the border. The transition between states is the most visible use of the gradient outside the hero — reinforcing that the indigo-lavender pair signals "selected/active" throughout the system.

### Badges

**`badge-new`** — 2px × 6px `{rounded.xs}` tag at `{typography.chip-label}` in `{colors.primary}` fill. Appears on product card thumbnails top-right. **`badge-sale`** — Same geometry in `{colors.error}` red, ensuring sale callouts read against the indigo-heavy palette without blending into brand color.

### Footer

**`footer`** — The `{colors.ink}` footer (#1c1c3a deep indigo-near-black) closes the gradient arc: the hero opens in bright indigo-lavender, the footer resolves it in a dark tonal echo. A 3px `{colors.primary}` top border marks the transition. Links render in `{colors.primary-gradient-end}` lavender for legibility against the dark surface, shifting to `{colors.on-primary}` white on hover.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo; hero headline drops to `{typography.display-md}`; compat chips scroll horizontally in a snap rail; search bar moves inside hamburger menu overlay |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories inline with overflow menu; hero uses 50/50 text-image split; filter chips wrap to two rows before truncating |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with search pill; hero is full-bleed with centered text column max-width 640px; spec rows display in two-column paired layout |
| Wide | > 1440px | Grid caps at 1400px max-width centered on canvas; hero text column max-width 720px; side whitespace fills with `{colors.canvas}` — gradient does not bleed to edges |

### Touch Targets

- All buttons and chips minimum 44px tall on mobile
- Compat chips in filter rail minimum 36px tall with 8px horizontal gap for tap separation
- Nav hamburger icon minimum 44×44px tap target
- Product card tap target covers full card surface, not just text or image

### Collapsing Strategy

- Primary nav: top-level labels visible at tablet+; hamburger drawer with full hierarchy on mobile
- Filter chips: horizontal scroll rail on mobile/tablet; vertical sidebar panel at desktop+
- Spec rows: single-column stacked (label above value) on mobile; inline label–value pairs at tablet+
- Product grid: 1-col mobile → 2-col tablet → 3-col desktop; no 4-col breakpoint (cable SKUs carry enough spec data that 3-col is the readable ceiling)
- Footer link columns: stacked single column on mobile; 3–4 columns at tablet+

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site is under maintenance — only 2 hex colors extracted (#4e54c8, #8f94fb); full brand palette including neutrals, error states, and surface hierarchy is inferred from the indigo family, not confirmed from live CSS
- No custom brand font detected; only system font stacks (Geneva, Segoe UI, Tahoma, Verdana) found — a custom typeface may load via JS or be hosted behind the maintenance gate
- No meta theme-color set; mobile browser chrome treatment unconfirmed
- Icon system unknown — no SVG sprite or icon font detected; icon style (line vs. filled, stroke weight) not confirmed
- Product photography art direction unknown — no images accessible through maintenance page
- Gradient angle (135°) and stop positions are inferred from the two extracted colors; actual brand gradient spec (angle, midpoint, opacity) not confirmed
- Animation and transition timing not extractable; easing curves and duration defaults are absent from this spec
- No pricing or promotional display patterns confirmed — sale badge color (#e53e3e) is inferred, not extracted
