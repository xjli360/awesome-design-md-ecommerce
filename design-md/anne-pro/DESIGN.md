---
version: alpha
name: "Anne Pro"
source_url: "https://www.obins.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The 60% layout is not a feature Anne Pro leads with — it is the product's geometry made into brand philosophy. By subtracting the numpad, the function row, and the navigation cluster, Obins returns 40% of the desk surface and ships a board that outsells full-size competitors in enthusiast forums not because it is cheaper but because it argues that constraint is the point. The visual system surrounding the Anne Pro 2 makes the same wager: near-white canvas, restrained ink-black body copy, and a warm orange on every primary CTA and "Add to Cart" trigger — a color choice drawn from the keyboard culture of amber-legend keycap sets rather than the consumer-electronics primary blues that dominate the category. Typography runs on the system sans-serif stack, trusting that a board this widely photographed in community unboxings does not need editorial font authority; display sizes reach 40px at 700 weight, but body copy stays at 13–15px with generous 1.6 line-height, closer to documentation than marketing. Product pages give the chassis 70% of the viewport at a slight overhead angle before a specification table opens below in label-over-value pairs — the layout of a datasheet, not a lifestyle lookbook. Firmware update banners, Bluetooth pairing callouts, and QMK documentation links all appear as inline info-bands with a left-border accent stroke in `{colors.primary}` rather than modal interruptions, because the Anne Pro customer follows a GitHub README as comfortably as a product page. The radius grammar nearly disappears: `{rounded.xs}` on buttons and inputs, `{rounded.sm}` on cards — no pill shapes, no soft consumer-app curves, just the milled-edge language of the keyboard's aluminum case options. The single moment of visual indulgence is a 6px RGB gradient strip on color-configuration pages, cycling the full hue wheel in a thin band that reads as a brand signature rather than decoration.

colors:
  primary: "#f07d28"
  primary-active: "#d4621a"
  primary-disabled: "#f0c4a0"
  ink: "#1a1a1a"
  body: "#3a3a3a"
  muted: "#767676"
  hairline: "#e0e0e0"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#111111"
  on-primary: "#ffffff"
  on-dark: "#f0f0f0"
  success: "#2e9e5c"
  warning: "#f5b400"
  error: "#d93025"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "system-ui, -apple-system, 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  mono:
    fontFamily: "'JetBrains Mono', 'Fira Code', 'Consolas', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0

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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.muted}"
    border: "1.5px solid {colors.hairline}"
    borderFocused: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoHeight: 28px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imagePadding: "{spacing.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    imageAspectRatio: "4/3"
    imageObjectFit: contain
  hero-band:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 520px
    padding: "{spacing.section} 0"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    rowBorder: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderUnselected: "1.5px solid {colors.hairline}"
    gap: "{spacing.xs}"
  switch-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    hoverBorder: "1px solid {colors.primary}"
  stock-badge-in:
    backgroundColor: "{colors.success}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  stock-badge-out:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  firmware-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    bodyTypography: "{typography.body-sm}"
    monoTypography: "{typography.mono}"
    border: "1px solid {colors.hairline}"
    accentLeft: "3px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base} {spacing.lg}"
  rgb-preview-strip:
    height: 6px
    rounded: "{rounded.full}"
    gradient: "linear-gradient(90deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #8b00ff)"
  product-image-viewer:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: "16/9"
    objectFit: contain
    padding: "{spacing.xl}"
  thumbnail-rail:
    gap: "{spacing.sm}"
    thumbnailSize: 64px
    thumbnailRounded: "{rounded.xs}"
    thumbnailBorderActive: "2px solid {colors.primary}"
    thumbnailBorderInactive: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid rgba(255,255,255,0.08)"
    padding: "{spacing.section} 0"
    columnGap: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Orange fill (`{colors.primary}`, #f07d28) at 44px tall with `{rounded.xs}` corners and 600-weight label. Active state darkens to `{colors.primary-active}`; disabled washes out to `{colors.primary-disabled}` with `not-allowed` cursor. The flat corner radius is deliberate: it reads like the angled edge of a keycap, not a consumer-app pill.

**`button-secondary`** — White fill with a 1.5px `{colors.hairline}` border and `{colors.ink}` label at the same 44px height as primary, so paired CTAs sit flush on the same baseline. Hover tightens the border to `{colors.primary}` without changing background.

**`button-ghost`** — Transparent background with `{colors.primary}` label text, used for secondary actions inside dark hero bands where a bordered button would compete with the photography. No border, no background fill — just the orange type.

### Text Input

**`text-input`** — 44px tall, 1.5px `{colors.hairline}` border at rest; border shifts to `{colors.primary}` on focus with no glow shadow. Placeholder in `{colors.muted}`. Used in search, login, and newsletter capture. The corner radius matches buttons (`{rounded.xs}`) so form rows feel compositionally consistent.

### Navigation

**`nav-bar`** — 60px tall white bar with a subtle `{colors.hairline-soft}` bottom rule. Logo at 28px height left-anchored; product links in `{typography.nav-link}` center or right-anchored; cart icon with numeric badge far right. On scroll, the bar adds a light box-shadow without changing background color. At < 744px, the product links collapse behind a hamburger icon.

### Product Cards

**`product-card`** — White card with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. Image occupies a 4:3 container with `contain` fit on `{colors.surface-soft}` padding so angled keyboard photos never clip. Below: product name in `{typography.title-sm}`, price in `{typography.price}`, and a color swatch rail. No hover zoom animation — the card simply lifts a box-shadow step.

### Hero Band

**`hero-band`** — Full-width dark section (`{colors.surface-dark}`) with the keyboard image right-aligned at 60% viewport width and headline/subline left at 40%. Display headline in `{typography.display-xl}` on `{colors.on-dark}`, body in `{typography.body-md}`. A single `{colors.primary}` button sits directly below body copy. No gradient overlays; the keyboard photograph provides all the visual contrast.

### Specification Table

**`spec-table`** — Two-column table (label / value) separated by a 1px `{colors.hairline-soft}` row rule. Labels in `{typography.spec-label}` all-caps muted text; values in `{typography.body-sm}` ink. Used for connectivity specs, switch type, battery life, dimensions. The table reads as documentation rather than marketing — no icon columns, no colored row alternates.

### Color & Switch Selectors

**`color-swatch`** — 28px circular swatches with 4px gap. Selected state: 2px `{colors.primary}` ring with 3px offset from the swatch edge. Unselected: 1.5px `{colors.hairline}` border. Tooltip appears on hover with color name in `{typography.caption}`.

**`switch-badge`** — Pill-less rectangular chip for switch type selection (Red / Brown / Blue). `{colors.surface-soft}` fill at rest; hover adds a 1px `{colors.primary}` border. Active state inverts to `{colors.primary}` fill with `{colors.on-primary}` label. Used in a horizontal radio-button row above the Add to Cart button.

### Stock Badges

**`stock-badge-in`** / **`stock-badge-out`** — Small `{rounded.full}` pills flanking the price display. In-stock uses `{colors.success}` fill; out-of-stock uses `{colors.surface-soft}` with `{colors.muted}` text. Both use `{typography.caption}` at 12px/500-weight. Size is deliberately small (24px tall) so it informs without alarming.

### Firmware Callout

**`firmware-callout`** — Inline info band with a 3px left accent in `{colors.primary}` and `{colors.surface-soft}` background. Body copy in `{typography.body-sm}`; any command or filename rendered in `{typography.mono}` with `{colors.surface-card}` inline chip. Used for firmware update prompts, Bluetooth pairing instructions, and QMK notes. Never modal — always inline beneath the relevant section.

### RGB Preview Strip

**`rgb-preview-strip`** — 6px tall, full-width gradient bar cycling the hue wheel from red through violet. Appears on RGB lighting configuration pages as the only purely decorative element in the system. `{rounded.full}` end caps. The strip functions as a brand signature: visible enough to delight, restrained enough not to contradict the spare aesthetic.

### Product Image Viewer

**`product-image-viewer`** — Large image container in 16:9 aspect ratio with `{colors.surface-soft}` background and `{spacing.xl}` padding so the keyboard never bleeds to the container edge. Below it, a **`thumbnail-rail`** of 64px square thumbnails with `{rounded.xs}` corners; active thumbnail receives a 2px `{colors.primary}` border.

### Footer

**`footer`** — Dark background (`{colors.surface-dark}`) mirroring the hero band to bookend the page. Links in `{colors.muted}` body-sm weight with no underline at rest; underline on hover. Column layout: product links, support, firmware downloads, community/social. A hairline rule `rgba(255,255,255,0.08)` separates footer from page content above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; hero stacks vertically with image above headline; product grid becomes single column; spec table scrolls horizontally; thumbnail rail hides, replaced by swipe gesture |
| Tablet | 744–1128px | Nav shows logo + hamburger (product links hidden); hero splits 50/50; product grid 2-column; spec table full-width; thumbnail rail visible at 48px |
| Desktop | 1128–1440px | Full nav bar; hero 40/60 split; product grid 3-column; all components at designed proportions |
| Wide | > 1440px | Content max-width 1320px centered; hero image scales up proportionally; product grid remains 3-column with wider gutters |

### Touch Targets

- All buttons and icon buttons minimum 44×44px tap target
- Color swatches 28px visual but 44px tap target via padding
- Switch-badge chips minimum 44px tall on mobile
- Thumbnail rail items expand to 56px tap height on mobile

### Collapsing Strategy

- Primary nav collapses at 744px to hamburger; drawer slides from right, full-screen overlay on `{colors.surface-dark}`
- Hero band image moves above headline on mobile; CTA button spans full width
- Spec table retains label/value layout but gains horizontal scroll wrapper; no accordion on mobile
- Firmware callouts maintain inline placement; mono code blocks gain horizontal scroll
- Product cards in 1-column mobile layout show thumbnail rail below image

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All colors are inferred** — zero hex values were extractable from obins.net (site likely JS-rendered or behind anti-bot). Primary `#f07d28` is derived from keyboard enthusiast community color associations with the brand, not confirmed brand guidelines.
- **Font family unconfirmed** — no font-family stacks were extracted. `system-ui / Inter` is a reasonable default for a lean product site; actual brand may use a licensed typeface.
- **Dark vs. light mode** — unable to confirm whether the site defaults to dark canvas or light. Design system is authored light-first with `{colors.surface-dark}` used only in hero and footer.
- **Logo mark and wordmark specifications** — color, safe-zone, and minimum-size rules unknown.
- **Icon library** — whether the site uses a custom icon set, Heroicons, or another system is unknown.
- **Animation / motion** — transition durations, easing curves, and hover/micro-interaction styles not observable.
- **Anne Pro 3 / current product lineup** — product range and page structure may have changed; spec-table and color-selector components are modeled on the Anne Pro 2 page as documented in community sources.
