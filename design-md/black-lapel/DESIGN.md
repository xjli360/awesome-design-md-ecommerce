---
version: alpha
name: "Black Lapel"
source_url: "https://blacklapel.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Olive (#6c7055) shows up where most menswear labels default to charcoal or navy — on the primary call-to-action, the active ring around a fabric swatch, the step indicator inside the suit configurator. It is a counterintuitive choice that reads correctly in context: the muted sage of a worsted wool window-pane weave rather than a corporate ink. Dark espresso (#372922) grounds the type, a warmer alternative to pure black that flatters the photography of finished garments against soft studio backgrounds. A secondary slate-blue (#676986) handles informational chips and secondary UI states, while a warm cream surface (#f5f0e9) lifts product cards off the main near-white canvas (#f7f7f8). Display copy runs in Wicked — a condensed, high-contrast face that belongs in a flagship tailor's fascia rather than a homepage carousel — while Asap handles sub-headings and navigation labels and Lato carries running prose, a three-level typographic hierarchy that keeps the configurator interface readable without competing with the editorial weight above. The rounded system is nearly flat throughout: inputs and cards sit at 4px or none, buttons at 4px, and there are no pill shapes anywhere in the primary UI — a discipline that mirrors the precision-made, constructed nature of the garment itself. The suit-builder flow — stepping customers through fabric, lining, lapel style, and button choice — is the functional center of the experience, and its step-indicator, swatch-grid, and option-chip components drive more design decisions than any homepage hero. Bright teal (#00eab6) appears as a narrow accent for progress pulses and notification dots, vivid against the otherwise restrained earthy palette. An espresso footer (#372922) closes every page with the same warm darkness that opens the body type — the palette wraps around itself.

colors:
  primary: "#6c7055"
  primary-active: "#525541"
  primary-disabled: "#c4c6bb"
  ink: "#372922"
  body: "#4a4a4a"
  muted: "#707070"
  muted-soft: "#888883"
  hairline: "#dbd8d5"
  hairline-cool: "#dbdde4"
  canvas: "#f7f7f8"
  canvas-white: "#ffffff"
  surface-soft: "#f5f0e9"
  surface-card: "#ffffff"
  surface-cool: "#e5e5eb"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  navy: "#272d45"
  slate: "#676986"
  slate-light: "#9a9db1"
  olive-dark: "#3f432d"
  warm-gray: "#8e8176"
  espresso: "#372922"
  accent-teal: "#00eab6"
  border-strong: "#b6b8aa"

typography:
  display-xl:
    fontFamily: "'Wicked', 'Asap', sans-serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.04
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Wicked', 'Asap', sans-serif"
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Wicked', 'Asap', sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
  title-md:
    fontFamily: "'Asap', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "'Asap', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-upper:
    fontFamily: "'Asap', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Asap', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.9px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Asap', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Asap', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  step-label:
    fontFamily: "'Asap', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  price-display:
    fontFamily: "'Asap', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas-white}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    borderWidth: 1.5px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-secondary-olive:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 1.5px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.primary}"
    focusOutline: "2px solid {colors.primary}"
  text-input-error:
    borderColor: "#c0392b"
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 36px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas-white}"
    boxShadow: "0 2px 10px rgba(55,41,34,0.09)"
  announcement-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    padding: "10px {spacing.base}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    imageFit: cover
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary-active}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    minHeight: 560px
    layout: full-bleed with centered or left-aligned text over photography
  hero-split:
    layout: "50/50 — image left, copy and CTA right"
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
  configurator-panel:
    backgroundColor: "{colors.canvas-white}"
    borderLeft: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    width: 380px
    position: sticky
    top: 72px
  step-indicator:
    inactiveBackgroundColor: "{colors.surface-cool}"
    activeBackgroundColor: "{colors.primary}"
    completedBackgroundColor: "{colors.primary-active}"
    inactiveTextColor: "{colors.muted}"
    activeTextColor: "{colors.on-primary}"
    completedTextColor: "{colors.on-primary}"
    typography: "{typography.step-label}"
    rounded: "{rounded.full}"
    size: 32px
    connectorColor: "{colors.hairline-cool}"
    connectorActiveColor: "{colors.primary}"
  fabric-swatch:
    size: 56px
    rounded: "{rounded.xs}"
    defaultBorderColor: "{colors.hairline}"
    defaultBorderWidth: 1px
    selectedBorderColor: "{colors.primary}"
    selectedBorderWidth: 2.5px
    selectedOutlineOffset: 2px
    gap: "{spacing.sm}"
  option-chip:
    backgroundColor: "{colors.surface-cool}"
    textColor: "{colors.body}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    hoverBorderColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    height: 36px
  size-input:
    backgroundColor: "{colors.canvas-white}"
    borderColor: "{colors.hairline-cool}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    focusBorderColor: "{colors.primary}"
  review-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    nameTypography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    starColor: "{colors.primary}"
  accent-dot:
    backgroundColor: "{colors.accent-teal}"
    size: 8px
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.espresso}"
    textColor: "{colors.hairline}"
    linkColor: "{colors.canvas-white}"
    linkHoverColor: "{colors.primary-disabled}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "{colors.muted-soft}"
    hoverTextColor: "{colors.canvas-white}"
    typography: "{typography.body-sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — Olive (#6c7055) background, white text, fully uppercase Asap at 14px with 0.9px tracking, 4px radius, 48px tall. On hover the background deepens to #525541; disabled state falls back to the muted sage (#c4c6bb) with white text to hold the same visual footprint while signaling inactivity.

**`button-secondary`** — Transparent background with a 1.5px espresso border and matching text. Used alongside the primary for two-up CTAs (e.g., "Start Customizing" + "Browse Suits"). Olive-variant version (`button-secondary-olive`) swaps border and text to #6c7055 for contexts where the espresso ink would be too heavy.

**`button-ghost`** — Bare uppercase label in `{colors.body}`, no border or background. Used for tertiary actions like "Learn More" within editorial sections. Padding is 8px on the y-axis only so text aligns to other inline elements.

### Navigation

**`nav-bar`** — 72px tall white bar with a 1px hairline bottom border (#dbd8d5). Links run in Asap 13px, uppercase, 600 weight, 0.6px tracking — compact enough that the full menswear category set (Suits, Shirts, Trousers, Accessories) fits on a single row without crowding. On scroll, a soft shadow replaces the hairline border. Logo sits at max 36px tall, left-aligned.

**`announcement-bar`** — 40px navy (#272d45) strip above the nav. White uppercase Asap label-upper type carries shipping promotions or seasonal offers. No close button in the primary configuration.

### Product Cards

**`product-card`** — Zero-radius, portrait-ratio (3:4) image with minimal padding below. Name in Asap 600 at 15px, price in Asap 700 at 20px rendered in olive-active (#525541). Cards sit on pure white even when the page canvas is the warm gray (#f7f7f8), creating a subtle lifted shelf effect without an explicit shadow.

**`product-card-badge`** — Flush-corner olive rectangle pinned to the image top-left. Uppercase Asap at 11px, 1.3px tracking. Used for labels like "Custom," "New," or "Sale." Zero radius matches the card edge exactly.

### Suit Configurator

**`step-indicator`** — Circular 32px nodes connected by thin hairline rules. Inactive nodes carry the cool surface color (#e5e5eb) with muted text; the active node fills olive (#6c7055); completed nodes deepen to #525541 with a checkmark glyph. The connector segment between a completed and active node also switches to olive, providing a clear progress read at a glance.

**`fabric-swatch`** — 56px square chips with 4px radius and a 1px hairline border at rest. On selection, a 2.5px olive border appears with a 2px offset outline, creating a distinct double-ring selection state that is clearly legible even on dark fabrics.

**`option-chip`** — Used for lapel style, button count, lining color, and monogram position. Cool-surface background at rest; fills olive on select. Uppercase Asap at 12px keeps the label short enough for a 36px chip height. Hover state shows an olive border before selection commits.

**`configurator-panel`** — 380px sticky right column with a 1px left hairline. Holds the running price summary, active selection summary, and the primary CTA. Top offset matches the nav height (72px) so it stays visible without overlapping the bar.

### Supporting Components

**`hero`** — Full-bleed navy (#272d45) or photography panel, 560px minimum height. Wicked display-xl at 60px carries the headline; Lato body-md handles the sub-copy below. The primary olive button is the single CTA, ensuring the sage green reads as an intentional signal rather than decoration against the dark field.

**`review-card`** — Warm cream (#f5f0e9) background, 4px radius. Star glyphs in olive. Reviewer name in Asap title-sm; review body in Lato body-sm with generous 1.55 line-height for long testimonials. Cards typically appear in a 3-column grid on desktop.

**`accent-dot`** — 8px teal (#00eab6) circle. Used as a live-notification dot (active consultation, configurator progress saved) or step-completion pulse. Its saturation is intentionally jarring against the earthy palette — the dot is meant to catch the eye exactly once.

**`footer`** — Espresso (#372922) background wrapping the full-width base. Column headings in white uppercase label-upper (11px, 1.3px tracking); links in muted warm gray (#888883) transitioning to white on hover. Mirrors the ink color used throughout the body type, so the footer reads as a natural dark anchor rather than an afterthought.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces horizontal link row; configurator panel collapses to full-width bottom drawer; swatch grid wraps to 4-per-row; hero headline drops to display-sm (26px); step indicator compresses to icon-only nodes |
| Tablet | 744–1128px | Two-column product grid; nav retains horizontal links but drops secondary utility items; configurator panel stays inline but narrows to 300px; hero switches to split layout with image left |
| Desktop | 1128–1440px | Three-column product grid; full nav with mega-dropdown panels; configurator panel 380px sticky; hero at full display-xl scale |
| Wide | > 1440px | Max-width content container (~1400px) centers; side margins expand; hero image bleeds but text column caps at 680px; product grid may expand to 4 columns |

### Touch Targets

- All interactive chips and swatches maintain a minimum 44×44px touch target even when the visible element is smaller (swatch visual is 56px, so target matches)
- Step indicator nodes are 32px visual / 44px touch target with invisible padding
- Nav links on mobile expand to full row height (min 48px) for thumb reachability
- Size inputs are 44px tall, large enough for numeric keyboard entry without zoom on iOS

### Collapsing Strategy

- Mega-nav collapses to a single hamburger icon at < 744px; sub-menus become full-screen slide-in drawers with a back-chevron pattern
- The configurator's sticky panel becomes a bottom sheet triggered by a floating "Your Selections" summary bar that appears once the user begins customizing
- Filter panels on the product listing collapse to a modal overlay on mobile rather than a sidebar
- The three-column review grid collapses to a horizontal scroll carousel on mobile, maintaining card size rather than re-flowing to single column
- Hero split layout stacks image above text at mobile, with image capped at 280px height to keep the CTA above the fold

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit border-radius values were extracted from the live site; the 4px (xs) primary radius is inferred from the flat, constructed aesthetic and Shopify theme defaults — actual values may differ
- Wicked is listed in the font stack but no specimen, weight range, or sizing scale was extractable; display sizes are estimated from visual hierarchy norms for condensed display faces
- No explicit button height or padding tokens were available; 48px tall / 14px 28px padding are inferred from standard accessible sizing
- The role of #676986 (slate-blue) versus #272d45 (navy) in the live UI could not be confirmed — both appear in the extracted palette but their specific assignment to UI zones is estimated
- Hover and focus state colors for non-primary interactive elements (chips, swatches, inputs) are inferred; no explicit state tokens were extractable
- Shadow values and elevation levels are unconfirmed; the single shadow on `nav-bar-scrolled` is an approximation
- #00eab6 (teal) placement in the live UI is uncertain — it may be a third-party widget accent (e.g., review platform, live-chat) rather than a first-party design token
- Icon set and glyph style (line weight, fill vs. stroke) could not be determined from extraction
