---
version: alpha
name: "Vari"
source_url: "https://www.vari.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The standing desk category has long defaulted to gray-on-gray industrial minimalism — Vari breaks from this with a saturated teal primary (#007fad) that carries every major CTA and hover state on the site, a hue specific enough to be brand-ownable without tipping into healthcare or nautical territory. Deep navy (#002543) anchors both the header and footer, wrapping the site in a dark-light contrast frame that lets large product photography — desks shown mid-lift, in real offices, with people — land without compositional competition. Type runs Lato at firm weights across the stack: display headings push to 48px at weight 700, body copy sits at 14–16px with generous 1.6 line heights so product specs and dimension tables breathe on the page rather than compressing into data grids. Corner radii stay modest throughout — {rounded.xs} to {rounded.sm} — a deliberate choice for a brand selling to facilities managers and office procurement teams as much as to individual desk buyers.

  Color does real functional work in the system. The teal primary (#007fad) drives "Shop Now" and "Add to Cart" CTAs, a vivid red (#e53c3c) marks sale badges and urgency labels, and a clean success green (#008827) confirms stock availability and form submissions. The full alert system deploys a semantic palette with Bootstrap-style tint/dark pairings — info teal (#abdde5 / #0c5460), warning amber (#ffe8a1 / #856404), danger crimson (#f5b1b1 / #771f1f) — pointing to a custom internal commerce platform rather than a theme store build. The canvas sits at a near-white #f9f9f9 rather than pure white, which softens contrast behind spec tables and product cards without drifting into the gray-heavy look of enterprise SaaS.

  Configurator pages — where buyers choose surface size, finish, and frame color — concentrate the design system's complexity into inline validation states, swatch selectors with {rounded.full} rings, and contextual spec callouts. Mobile nav collapses into a full-screen navy drawer, keeping the teal primary as the sole action color against the dark ground. Section-level spacing is generous (64px+) to give product imagery and feature-grid callouts room to register; internal component spacing stays tight at {spacing.sm} to {spacing.base} to pack comparison rows efficiently.

colors:
  primary: "#007fad"
  primary-hover: "#005474"
  primary-bright: "#00a1e0"
  primary-disabled: "#a1ddf3"
  primary-pale: "#b8e5f6"
  on-primary: "#ffffff"
  navy: "#002543"
  ink: "#1e1e1e"
  body: "#383d41"
  muted: "#818182"
  charcoal: "#444444"
  hairline: "#c8cbcf"
  hairline-soft: "#d6d8db"
  canvas: "#f9f9f9"
  surface-card: "#ffffff"
  surface-soft: "#ececf6"
  accent-red: "#e53c3c"
  accent-red-pale: "#f5b1b1"
  accent-red-dark: "#771f1f"
  success: "#008827"
  success-pale: "#a7d6b4"
  success-dark: "#004714"
  warning-text: "#856404"
  warning-pale: "#ffe8a1"
  info-dark: "#0c5460"
  info-pale: "#abdde5"
  sky: "#94e1ff"

typography:
  display-xl:
    fontFamily: "Lato, 'Lato Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  spec-value:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "Lato, 'Lato Fallback', Arial, sans-serif"
    fontSize: 22px
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    hoverBackgroundColor: "{colors.primary-hover}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
    hoverBackgroundColor: "{colors.primary-pale}"
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    border: "2px solid {colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    shadow: "0 2px 8px rgba(0,0,0,0.08)"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    overlayOpacity: 0.45
    minHeight: 560px
  spec-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.label}"
    valueTypography: "{typography.spec-value}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  alert-info:
    backgroundColor: "{colors.info-pale}"
    textColor: "{colors.info-dark}"
    border: "1px solid {colors.info-pale}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  alert-success:
    backgroundColor: "{colors.success-pale}"
    textColor: "{colors.success-dark}"
    border: "1px solid {colors.success-pale}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  alert-warning:
    backgroundColor: "{colors.warning-pale}"
    textColor: "{colors.warning-text}"
    border: "1px solid {colors.warning-pale}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  alert-danger:
    backgroundColor: "{colors.accent-red-pale}"
    textColor: "{colors.accent-red-dark}"
    border: "1px solid {colors.accent-red-pale}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  category-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.primary}"
    selectedRingOffset: 2px
  stock-badge:
    inStockBackgroundColor: "{colors.success-pale}"
    inStockTextColor: "{colors.success-dark}"
    outBackgroundColor: "{colors.accent-red-pale}"
    outTextColor: "{colors.accent-red-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  compare-tray:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    ctaTypography: "{typography.button-md}"
    padding: "{spacing.base} {spacing.xl}"
    position: fixed-bottom
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.primary-bright}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    legalTypography: "{typography.caption}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Teal (#007fad) fill with white uppercase Lato at 16px/700, 4px corner radius, 48px height. On hover it steps down to the darker #005474 immediately — no transition delay — giving a direct, confident press feel suited to a B2B procurement context. The disabled state swaps to the pale tint (#a1ddf3) and removes pointer events; opacity hacking is avoided.

**`button-secondary`** — Transparent fill with a 2px teal border and teal text; used for secondary CTAs like "Learn More," "Compare," and "Download Spec Sheet." On hover it fills with the lightest primary pale (#b8e5f6), signaling selection without the full CTA commitment.

**`button-navy`** — Navy (#002543) fill with white uppercase text; deployed on hero overlays and promotional banners where the teal primary would compete visually with large photography. Same height and type scale as `button-primary` for tap consistency.

**`button-ghost`** — White border and white text for use directly on dark or photographic backgrounds. Full 48px height preserved. Never used on light canvas.

### Navigation

**`nav-bar-strip`** — A slim 36px teal (#007fad) announcement strip above the main header, carrying shipping thresholds, promotional copy, or regional messages at `caption` scale (13px/400) in white centered text. The strip disappears on scroll past 80px and reappears on upward scroll.

**`nav-bar`** — Navy (#002543) main header, 72px tall, holding the Vari wordmark left and category mega-menus center-right in `nav-link` type (15px/700) in white. Mega-menu dropdowns open on hover with a white surface panel and product photography thumbnails. At mobile the entire bar collapses to a 60px strip with logo and hamburger icon only; tapping hamburger opens a full-screen navy drawer with accordion category links.

### Product Card

**`product-card`** — White card with 1px light-hairline border and 8px radius; lifts to a stronger directional shadow on hover. Title runs `title-md` (18px/700), price runs the `price` token (22px/700) in ink. A `product-card-badge` anchors top-left for Sale or New callouts in accent red (#e53c3c) with white uppercase label text. Layout is 3-up on desktop, 2-up on tablet, 1-up on mobile.

### Hero

**`hero`** — Full-bleed photographic section with a navy (#002543) background fallback, overlaid at 45% opacity to keep text legible against lifestyle photography. Headline runs `display-xl` (48px/700) in white; subhead at `body-md` at 80% white; a `button-primary` CTA sits below with 24px top margin. Minimum 560px height; photography consistently shows desks in-use in real office environments to communicate ergonomic range.

### Spec Callout

**`spec-callout`** — Grid of stat tiles used on PDP pages to surface key product specs: lift range, weight capacity, surface area, and warranty length. Each tile shows a `label` tag (12px/uppercase) above a large `spec-value` number (24px/700 in ink). Background is `surface-soft` (#ececf6) inside a {rounded.sm} container with hairline border. Defaults to 4-up on desktop, 2-up on tablet, stacks to 1-up on mobile. These tiles communicate product credibility with the directness of engineering datasheets rather than marketing language.

### Alert System

**`alert-info` / `alert-success` / `alert-warning` / `alert-danger`** — Full semantic alert set with Bootstrap-style tint-background/dark-text pairings: info (#abdde5 / #0c5460), success (#a7d6b4 / #004714), warning (#ffe8a1 / #856404), danger (#f5b1b1 / #771f1f). All variants use `body-sm` (14px/400), {rounded.xs}, and 16px horizontal padding. Used for cart messages, stock notifications, form validation, and order confirmation flows.

### Category Pills

**`category-pill`** — Horizontally scrolling row of pill-shaped filter tabs above product grids. Inactive: white fill, hairline border, charcoal text. Active: teal fill, white text, teal border. Used to filter by product type (Standing Desk, Monitor Arm, Chair) or feature (Height-Adjustable, Electric). Sits between the page section header and the product grid without a page reload.

### Color Swatch

**`color-swatch`** — 28px circle at {rounded.full}, used in product configurators and PDP color selectors. Selected state shows a 2px teal ring with 2px offset gap. Hover shows the ring at 50% opacity as a preview affordance. Swatches appear in horizontal runs of 4–8 representing surface finish or frame color variants.

### Compare Tray

**`compare-tray`** — Fixed bottom bar in navy (#002543) that activates when two or more products are checked for comparison. Shows small product name labels at `body-sm`, a compare CTA button at `button-md` scale in teal, and a dismiss ✕. Constrained to a single row so it does not obscure the product grid below. Disappears when comparison is cleared.

### Footer

**`footer`** — Navy background matching the nav bar, four-column link grid at desktop, collapsing to a single-column accordion on mobile. Section headings use `title-sm` (16px/700) in white. Links use `body-sm` at `primary-bright` (#00a1e0) for visual separation from static text. Bottom row carries legal text at `caption` (13px) in 60%-opacity white and social icons in solid white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to 60px bar + navy full-screen drawer; hero stacks headline above image crop; product cards go 1-up; spec callout wraps to 2-up then 1-up under 480px; compare tray shrinks to icon + count chip; category pills scroll horizontally with fade mask at edge |
| Tablet | 744–1128px | Product cards go 2-up; nav shows top-level labels with accordion dropdowns; hero image crops to portrait; spec callout stays 2-up with wider tiles; footer collapses to 2-column grid |
| Desktop | 1128–1440px | Full two-layer nav with mega-menus; product cards 3-up; hero full-bleed with text overlay; spec callout 4-up in a single row; category pills fully visible without scroll |
| Wide | > 1440px | Content max-width ~1400px centered; hero photography extends edge-to-edge behind centered content column; footer grid gains additional breathing room at section scale spacing |

### Touch Targets
- All buttons minimum 44×44px; primary and secondary CTAs at 48px height
- Category pills padded to 38px touch height on mobile with 8px horizontal gaps
- Color swatches increase from 28px to 36px on touch viewports
- Compare tray action area padded to 44px even when visually compact
- Nav hamburger icon target minimum 44×44px with centered 24px glyph

### Collapsing Strategy
- Announcement strip hides on scroll past 80px, reappears on upward scroll (sticky recovery)
- Main nav bar sticky from top: 0; collapses to 60px logo + hamburger on mobile
- Mega-menu dropdowns become full-screen accordion panels inside the mobile nav drawer
- Spec callout shifts 4-col → 2-col at tablet, 1-col at mobile under 480px
- Footer link columns collapse to tap-to-expand accordions on mobile
- Product comparison tray reduces to icon + badge count below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font confirmed from extraction — "Lato Fallback" in the font stack implies Lato is the primary web font, but the loading mechanism (Google Fonts, self-hosted, JS-injected) was not directly observable; Lato assigned as best inference
- Exact button corner radii not captured from static extraction; {rounded.xs} (4px) assigned based on professional workspace positioning
- Icon system vendor (Heroicons, Font Awesome, custom SVG set) not identifiable from extracted hints
- Motion and animation timing values (hover transitions, drawer open easing curves) not captured
- PDP configurator step count, modal vs. inline interaction model, and lift animation for standing desk preview not confirmed
- Exact grid column gutter widths not extracted; {spacing.lg} (24px) assumed as standard
- Meta theme-color is absent, so dark-mode support status is unknown; no dark surface tokens defined
- Specific font weights for Lato loading (subset vs. full 100–900 range) not confirmed; 400 and 700 assigned as minimum expected cuts
- Product photography art direction rules (aspect ratios, crop anchors, background treatment) not derivable from color extraction alone
