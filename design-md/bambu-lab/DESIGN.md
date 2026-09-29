---
version: alpha
name: "Bambu Lab"
source_url: "https://www.bambulab.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Precision engineering rendered in near-black and charged by a single green voltage — the Bambu Lab interface feels closer to mission-control software than to a typical e-commerce storefront. Where most consumer hardware brands lead with white-canvas layouts and lifestyle photography, Bambu Lab commits to darkness: surfaces stack from #111111 up through the extracted #313131, each tier reading as a deliberate elevation rather than an accident of default styling. Their signature green (approximately #00AE42, widely documented in brand coverage and hardware unboxing media) does not decorate — it activates. Every primary CTA, every active filter chip, every progress indicator in the cloud printing dashboard runs hot green against near-black, an unambiguous signal in a product category where print-status feedback is functionally critical, not merely aesthetic. Typography pulls entirely from the system stack — no custom typeface was detectable at crawl time, likely due to JS-loaded tokens behind anti-bot protection — but this restraint earns its keep: tight display text at 700 weight with negative letter-spacing conveys spec-sheet authority without the soft warmth of a consumer lifestyle brand. The AMS (Automatic Material System) product line introduced a genuinely novel UI problem: representing up to sixteen simultaneous filament colors in a compact dashboard widget. Bambu Lab answers with a slot-chip grid that resembles a hardware rack more than a color swatch, each 32px square carrying an active border in {colors.primary} when loaded. Product cards carry dense spec rows — print speed in mm/s, layer resolution in μm, build volume in cubic centimeters — rather than soft lifestyle copy, targeting a customer who reads a datasheet before placing an order. Corner radii hold at {rounded.xs} almost everywhere, avoiding the pill-softness of consumer lifestyle brands. Responsive collapse moves the spec strip into a horizontal scroll band on mobile and accordion-stacks comparison tables, preserving information density without burying the numbers that close the sale.

colors:
  primary: "#00AE42"
  primary-active: "#008F36"
  primary-disabled: "#4D9966"
  ink: "#FFFFFF"
  body: "#E0E0E0"
  muted: "#9A9A9A"
  hairline: "#3D3D3D"
  canvas: "#111111"
  surface-soft: "#1E1E1E"
  surface-card: "#313131"
  surface-elevated: "#3A3A3A"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  error: "#FF4D4D"
  warning: "#FFB800"
  success: "#00AE42"
  filament-chip-bg: "#252525"
  spec-label: "#6B6B6B"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  spec-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    height: 48px
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
        opacity: 0.6

  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 48px
    states:
      hover:
        borderColor: "{colors.ink}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    states:
      hover:
        textColor: "{colors.ink}"

  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    states:
      focus:
        borderColor: "{colors.primary}"
        outline: "2px solid rgba(0,174,66,0.2)"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logo:
      height: 28px
    activeIndicator:
      color: "{colors.primary}"
      height: 2px
      position: bottom

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    overflow: hidden
    border: "1px solid {colors.hairline}"
    imageAspect: 4/3
    imageBackground: "{colors.surface-soft}"
    padding: "{spacing.lg}"
    name:
      typography: "{typography.title-sm}"
      color: "{colors.ink}"
    tagline:
      typography: "{typography.body-sm}"
      color: "{colors.muted}"
    price:
      typography: "{typography.title-md}"
      color: "{colors.ink}"
    states:
      hover:
        borderColor: "{colors.primary}"
        transform: "translateY(-2px)"
        transition: "all 0.2s ease"

  hero-printer:
    backgroundColor: "{colors.canvas}"
    layout: split-screen
    minHeight: 600px
    leftColumn:
      padding: "{spacing.xxl} {spacing.xl}"
      maxWidth: 560px
      eyebrow:
        typography: "{typography.spec-label}"
        color: "{colors.primary}"
        marginBottom: "{spacing.sm}"
      headline:
        typography: "{typography.display-xl}"
        color: "{colors.ink}"
      subline:
        typography: "{typography.body-md}"
        color: "{colors.muted}"
        marginTop: "{spacing.base}"
        maxWidth: 480px
      ctaRow:
        gap: "{spacing.sm}"
        marginTop: "{spacing.xl}"
    rightColumn:
      backgroundColor: "{colors.surface-soft}"
      display: flex
      alignItems: center
      justifyContent: center
      printerImageAspect: 1/1

  spec-strip:
    backgroundColor: "{colors.surface-soft}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
    layout: horizontal
    overflowX: auto
    item:
      padding: "0 {spacing.xl}"
      borderRight: "1px solid {colors.hairline}"
      textAlign: center
      value:
        typography: "{typography.spec-value}"
        color: "{colors.ink}"
      label:
        typography: "{typography.spec-label}"
        color: "{colors.spec-label}"
        marginTop: "{spacing.xs}"

  ams-color-grid:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    gridColumns: 4
    gap: "{spacing.xs}"
    slot:
      width: 32px
      height: 32px
      rounded: "{rounded.xs}"
      border: "2px solid {colors.hairline}"
      backgroundColor: "{colors.filament-chip-bg}"
    slotActive:
      border: "2px solid {colors.primary}"
    emptySlot:
      backgroundColor: "{colors.surface-soft}"
      opacity: 0.4
    label:
      typography: "{typography.caption}"
      color: "{colors.muted}"
      marginTop: "{spacing.xs}"

  filament-badge:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    display: inline-flex
    variants:
      pla:
        borderColor: "#4CAF50"
        textColor: "#4CAF50"
      abs:
        borderColor: "#FF9800"
        textColor: "#FF9800"
      petg:
        borderColor: "#2196F3"
        textColor: "#2196F3"
      tpu:
        borderColor: "#9C27B0"
        textColor: "#9C27B0"
      support:
        borderColor: "{colors.muted}"
        textColor: "{colors.muted}"

  print-mode-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
    states:
      active:
        backgroundColor: "{colors.primary}"
        textColor: "{colors.on-primary}"
        borderColor: "{colors.primary}"
      hover:
        borderColor: "{colors.muted}"

  ecosystem-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    icon:
      size: 40px
      color: "{colors.primary}"
      marginBottom: "{spacing.md}"
    title:
      typography: "{typography.title-md}"
      color: "{colors.ink}"
    description:
      typography: "{typography.body-sm}"
      color: "{colors.muted}"
      marginTop: "{spacing.sm}"
    link:
      typography: "{typography.button-sm}"
      color: "{colors.primary}"
      marginTop: "{spacing.md}"
      display: inline-flex
      alignItems: center
      gap: "{spacing.xs}"

  comparison-table:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    overflow: hidden
    header:
      backgroundColor: "{colors.surface-soft}"
      typography: "{typography.title-sm}"
      textColor: "{colors.ink}"
      padding: "{spacing.md} {spacing.lg}"
      borderBottom: "1px solid {colors.hairline}"
    row:
      padding: "{spacing.sm} {spacing.lg}"
      borderBottom: "1px solid {colors.hairline}"
      labelTypography: "{typography.body-sm}"
      labelColor: "{colors.muted}"
      valueTypography: "{typography.body-sm}"
      valueColor: "{colors.ink}"
    highlightRow:
      backgroundColor: "rgba(0,174,66,0.07)"
      valueColor: "{colors.primary}"
      valueFontWeight: 700

  status-badge:
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    typography: "{typography.badge}"
    variants:
      new:
        backgroundColor: "{colors.primary}"
        textColor: "{colors.on-primary}"
      sale:
        backgroundColor: "#FF4D4D"
        textColor: "#FFFFFF"
      popular:
        backgroundColor: "{colors.surface-elevated}"
        textColor: "{colors.muted}"
      combo:
        backgroundColor: "{colors.surface-elevated}"
        textColor: "{colors.body}"

  print-progress-bar:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
    label:
      typography: "{typography.caption}"
      color: "{colors.muted}"
      marginTop: "{spacing.xs}"
    percentage:
      typography: "{typography.caption}"
      color: "{colors.primary}"

  search-bar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: "0 {spacing.md}"
    icon:
      color: "{colors.muted}"
      size: 18px
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    states:
      focus:
        borderColor: "{colors.primary}"

  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"
    columns: 4
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.ink}"
    copyrightTypography: "{typography.caption}"
    dividerColor: "{colors.hairline}"
    socialIcon:
      size: 20px
      color: "{colors.muted}"
      hoverColor: "{colors.ink}"

## Components

### Buttons

**`button-primary`** — The primary CTA is 48px tall with {rounded.xs} corners (4px), nearly flush-edged against the dark surface. Fill runs {colors.primary} (#00AE42) at rest and steps down to {colors.primary-active} (#008F36) on hover, a subtle darkening that communicates depression without animation overhead. Disabled state reduces opacity to 0.6 over a muted green fill so the action reads as unavailable rather than removed. Font is {typography.button-md} at 600 weight with slight positive tracking — it reads as a label, not a shout.

**`button-secondary`** — A hairline-bordered ghost on the dark canvas. At rest, the border is {colors.hairline} (#3D3D3D), nearly invisible against {colors.surface-card}; on hover it steps to full {colors.ink} (white), tightening the perceived boundary and confirming interaction without a fill change. Padding matches button-primary exactly so the two can sit in a row at identical heights.

**`button-ghost`** — Text-only for tertiary actions: filter clears, pagination links, accordion toggles. Muted gray ({colors.muted}) at rest, steps to {colors.ink} on hover. No border, no background.

### Text Input

**`text-input`** — 44px tall on {colors.surface-soft} with a 1px {colors.hairline} border. Placeholder text uses {colors.muted}. Focus state swaps the border to {colors.primary} and adds a soft 2px glow at 20% opacity — the same green that runs CTA buttons signals active state on form controls, reinforcing the single-voltage brand system. Typography is {typography.body-md}.

### Navigation

**`nav-bar`** — 64px tall, {colors.canvas} background, 1px bottom hairline. Logo sits at 28px height. Active category uses a 2px bottom-edge underline in {colors.primary}; inactive links are {typography.nav-link} at {colors.muted}. On mobile the nav collapses to a hamburger triggering a full-screen dark drawer at {colors.surface-soft}.

### Product Card

**`product-card`** — {colors.surface-card} (#313131, the only extracted color) serves as the card background, creating a single-step elevation above the #111111 canvas. A 1px {colors.hairline} border sharpens the edge. On hover the border swaps to {colors.primary} and the card lifts 2px via transform, identifying the clickable zone without relying on color alone. The image zone sits at 4:3 aspect on {colors.surface-soft} — a slightly recessed tone for the product photography to float against. Name uses {typography.title-sm}, price uses {typography.title-md}.

### Hero (Printer Spotlight)

**`hero-printer`** — Split-screen layout: the left column carries the eyebrow label in {typography.spec-label} + {colors.primary} (the green works as a category signal before the headline), followed by a {typography.display-xl} headline at 48px/700 weight, a subline in {colors.muted}, and a horizontal CTA row. The right column is {colors.surface-soft}, centered, and holds the printer render at 1:1 aspect. The dark-on-dark treatment makes the product photography the only brightness on screen.

### Spec Strip

**`spec-strip`** — A horizontal band of technical metrics directly below the hero. Each item presents a large {typography.spec-value} number (22px/700) above a {typography.spec-label} descriptor in uppercase with tracked spacing. Dividers are 1px {colors.hairline} between items. On mobile the strip becomes horizontally scrollable, keeping all specs visible without collapse.

### AMS Color Grid

**`ams-color-grid`** — A 4-column grid of 32px square slots representing filament channels. Inactive slots show {colors.filament-chip-bg} (#252525) with a {colors.hairline} border; active slots (loaded with filament) show the filament's actual hex fill and a {colors.primary} border ring. Empty future slots reduce to 40% opacity. This component is unique to Bambu Lab's multi-material ecosystem and should be treated as a brand-signature widget.

### Filament Badge

**`filament-badge`** — Inline chips that appear on product pages and print profiles to indicate compatible materials. Each material type carries a distinct border color — PLA green, ABS orange, PETG blue, TPU purple — while the chip background stays neutral. Typography is {typography.badge} (11px uppercase). These chips stack horizontally in a flex-wrap row below the product name.

### Print Mode Chip

**`print-mode-chip`** — Pill-shaped ({rounded.full}) selector chips for quality presets (Optimal, Standard, Draft, etc.). Inactive: {colors.surface-soft} fill, {colors.muted} text, hairline border. Active: full {colors.primary} fill with {colors.on-primary} text. This is one of only two places the brand uses {rounded.full} — the contrast with the otherwise square-cornered interface makes mode selection feel like a toggle rather than a button.

### Ecosystem Card

**`ecosystem-card`** — Used in sections presenting Bambu Handy (mobile app), Bambu Studio (slicer), and Makerworld (community). A 40px icon in {colors.primary} anchors the card top, followed by {typography.title-md} title, {typography.body-sm} description in {colors.muted}, and a {colors.primary} text-link with arrow. All on {colors.surface-card} with a hairline border.

### Comparison Table

**`comparison-table`** — Used side-by-side for printer model comparisons. Header row at {colors.surface-soft} holds model names in {typography.title-sm}. Data rows alternate between standard and highlighted: highlighted rows use a 7% green tint background and bold {colors.primary} values to draw attention to differentiating specs. Label column is {colors.muted}; value column is {colors.ink}.

### Status Badge

**`status-badge`** — Tight inline chips ({rounded.xs}, 4px padding vertical) in three variants: NEW in {colors.primary} fill, SALE in #FF4D4D fill, and POPULAR in {colors.surface-elevated} with {colors.muted} text. Typography is {typography.badge} throughout.

### Print Progress Bar

**`print-progress-bar`** — 4px tall, {rounded.full} track in {colors.hairline}, filled with {colors.primary}. Used in cloud dashboard and order-status contexts. The percentage label in {typography.caption} sits above the bar in {colors.primary}, echoing the fill color. Below the track, a secondary label in {colors.muted} shows estimated time remaining.

### Footer

**`footer`** — {colors.surface-soft} on a 4-column grid. Column headings in {typography.title-sm}/{colors.ink}; links in {typography.body-sm}/{colors.muted} stepping to {colors.ink} on hover. Social icons at 20px in {colors.muted}. Full-width hairline divider above the copyright row, which runs {typography.caption}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero stacks printer image above text; spec strip scrolls horizontally; nav collapses to hamburger drawer; product grid 1-column; comparison table scrolls horizontally; AMS grid reduces to 2 columns |
| Tablet | 744–1128px | 2-column product grid; hero maintains split-screen at reduced copy width; spec strip fits 3–4 items before scroll; nav may show abbreviated labels; comparison table 2-model max |
| Desktop | 1128–1440px | Full split-screen hero; 3-column product grid; spec strip shows all items inline; 4-column footer; nav fully expanded |
| Wide | > 1440px | Max content width ~1400px, centered; hero padding increases; hero copy column widens to 640px; product grid optionally 4-column |

### Touch Targets

- All interactive elements minimum 44×44px on mobile (buttons, nav items, chip selectors)
- AMS color slots expand to 40px on touch to reduce mis-tap on small filament chips
- Comparison table row tap targets extend to full row width
- Filament badges receive 8px vertical padding increase on mobile

### Collapsing Strategy

- Spec strip becomes horizontal scroll with overflow-x: auto and no scrollbar visible (webkit-scrollbar hidden)
- Comparison table with 3+ columns collapses to a paginated 2-column view with a model selector above
- AMS color grid reduces from 4 to 2 columns on mobile
- Footer collapses from 4-column to 2-column on tablet, accordion on mobile
- Hero left/right split stacks vertically: image first, then copy — printer render still visible above the fold at mobile viewport heights ≥ 667px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extractable from the live site — the page returned "Just a moment…" (Cloudflare anti-bot), indicating JS-loaded design tokens that did not survive static crawl
- Primary brand green (#00AE42 estimated) sourced from widely available brand documentation and product media, not from direct CSS extraction — actual value may differ by ±10 points in any channel
- No custom font family detected; system stack assumed throughout — Bambu Lab may use a licensed typeface loaded via JS or font-face that was blocked at crawl time
- Exact nav height, button border-radius, and card padding values are estimated from visual analysis of public product media, not extracted measurements
- Dark-mode vs. light-mode breakpoint behavior unknown — the site may have a light variant for certain subpages (store checkout, support) that follows different token values
- Bambu Studio slicer interface (desktop app) likely has a separate, more complex dark-UI design system not captured here
- Makerworld community subdomain may carry its own color overrides and card component variants not reflected in this spec
