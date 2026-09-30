---
version: alpha
name: "Bagatiba"
source_url: "https://www.bagatiba.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Where most fine jewelry sites flood the screen with warm cream and gold-leaf gradients, Bagatiba strips back to a near-black monochrome — #121212 at the deepest anchor, #2a2a2a carrying body copy, a single quiet silver-gray at #dedede for hairlines and disabled states — and lets gold chain and stone do all the tonal work. The palette is so compressed it reads less like a jewelry store and more like an independent gallery print catalogue, which is exactly the intention. The type system doubles down on that editorial register: Newsreader, a high-contrast bracketed serif optimized for screen reading, takes every headline and display moment, while DM Sans — open apertures, even stroke, zero affectation — handles labels, navigation, price strings, and interface chrome. The two fonts never compete because they occupy completely different layers; the serif announces, the sans operates. Buttons and inputs carry very subtle rounding (`{rounded.sm}`) rather than the pill shapes common to DTC skincare or beauty, signaling precision over friendliness. Product cards sit on a near-white `{colors.surface-card}` lift against a pure `{colors.canvas}` page ground, with the product image taking the full card face and all metadata dropping below the fold in a tight DM Sans stack. The add-to-cart action is a full-width dark slab at the base of the product drawer — the only moment the near-black primary color appears at scale, making it read as a confident close rather than a promotional shout. Navigation is restrained: a centered wordmark flanked by minimal icon controls, no mega-menu, category links in low-weight DM Sans that sit flush with the page rather than demanding attention. The overall register is confident enough in its product to let silence carry weight.

colors:
  primary: "#2a2a2a"
  primary-active: "#121212"
  primary-disabled: "#626262"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#626262"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-subtle: "#fafafa"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  dark-bg: "#282828"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Newsreader', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Newsreader', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Newsreader', Georgia, serif"
    fontSize: 30px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Newsreader', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'DM Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
    textTransform: uppercase
  body-md:
    fontFamily: "'DM Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  label-upper:
    fontFamily: "'DM Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  price-display:
    fontFamily: "'DM Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'DM Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'DM Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.04em
  nav-wordmark:
    fontFamily: "'DM Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.2em
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 48px
    hoverBackgroundColor: "{colors.primary-active}"
    transition: background-color 0.2s ease
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 48px
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 15px 31px
    height: 48px
    border: "1px solid {colors.primary}"
    hoverBackgroundColor: "{colors.surface-soft}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    textDecoration: underline
    textUnderlineOffset: 3px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 14px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    padding: 0 {spacing.xl}
    wordmarkTypography: "{typography.nav-wordmark}"
    wordmarkColor: "{colors.ink}"
    iconSize: 20px
  nav-announcement:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: 1/1
    padding: 0
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.body}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    gap: "{spacing.sm}"
    hoverImageScale: 1.03
    transition: transform 0.35s ease
  hero-section:
    backgroundColor: "{colors.canvas}"
    minHeight: 90vh
    layout: split-50-50
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    ctaComponent: button-primary
    imageObjectFit: cover
    padding: "{spacing.section} {spacing.xl}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-md}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.muted}"
    textAlign: center
    paddingY: "{spacing.section}"
    maxWidth: 560px
    marginX: auto
  category-label:
    typography: "{typography.label-upper}"
    textColor: "{colors.muted}"
    backgroundColor: transparent
    display: inline-block
    marginBottom: "{spacing.sm}"
  material-badge:
    typography: "{typography.label-upper}"
    textColor: "{colors.body}"
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
    border: "1px solid {colors.hairline}"
  swatch-selector:
    size: 24px
    rounded: "{rounded.full}"
    activeBorder: "2px solid {colors.ink}"
    inactiveBorder: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  product-drawer:
    backgroundColor: "{colors.canvas}"
    width: 480px
    padding: "{spacing.xl}"
    titleTypography: "{typography.display-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.body}"
    ctaComponent: button-primary
    ctaFullWidth: true
    borderLeft: "1px solid {colors.hairline}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.label-upper}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: none
    linkHoverColor: "{colors.canvas}"
  email-signup:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.xl}"
    headlineTypography: "{typography.display-sm}"
    headlineColor: "{colors.ink}"
    inputComponent: text-input
    ctaComponent: button-primary
    layout: row-inline
    maxWidth: 480px

## Components

### Buttons
**`button-primary`** — A flat, sharp-cornered dark slab (`{rounded.none}`) filled with `{colors.primary}` (#2a2a2a) and white DM Sans uppercase text at wide tracking. No border radius means it reads as a deliberate, confident action rather than a friendly tap target. On hover it deepens to `{colors.primary-active}` (#121212) with a 0.2s ease transition. The disabled state uses `{colors.primary-disabled}` (#626262) to maintain the monochrome logic without introducing a foreign color.

**`button-secondary`** — Same sharp geometry, same uppercase DM Sans, but inverted: white fill with a 1px `{colors.primary}` border and dark text. Used for secondary choices like "Add to Wishlist" or filter resets. Hover fills with `{colors.surface-soft}` for a barely perceptible tonal shift.

**`button-text-link`** — Inline underlined body text in `{colors.body}`, used for navigational soft actions ("View all", "See details"). Underline offset of 3px keeps it legible without feeling heavy.

### Text Input
**`text-input`** — Borderless on three sides with a single 1px `{colors.hairline}` perimeter border and no radius. DM Sans at 15px, 48px tall. On focus, the border sharpens to `{colors.primary}`. Placeholder text sits in `{colors.muted}`. Used for search, email capture, and checkout fields.

### Navigation
**`nav-bar`** — White bar, 60px tall, with a 1px `{colors.hairline}` underline. The wordmark is `{typography.nav-wordmark}` — uppercase DM Sans at wide 0.2em tracking — centered or left-aligned depending on viewport. Right side holds cart icon, account icon, and search trigger at 20px. Category links in `{typography.nav-link}` sit below or inline on desktop. Above the nav, `nav-announcement` runs a full-width near-black (`{colors.dark-bg}`) strip with `{typography.label-upper}` messaging in white.

### Product Card
**`product-card`** — No border, no radius, no drop shadow: a clean image tile at 1:1 aspect ratio that scales 1.03× on hover over 0.35s. Below the image, brand name in `{typography.caption}` at `{colors.muted}`, product title in `{typography.body-sm}` at `{colors.ink}`, and price in `{typography.price-display}`. The minimalism forces visual weight back to the product photography. Collections grid runs 2-up on mobile, 3-up on tablet, 4-up on wide desktop.

### Hero
**`hero-section`** — Split 50/50 layout at 90vh minimum: editorial image on one half, headline + subhead + CTA stacked on the other. Headline in `{typography.display-xl}` Newsreader at near-black, subhead in `{typography.body-md}` DM Sans at `{colors.muted}`. The serif headline at 52px creates the gallery-catalogue moment that distinguishes the brand from mass-market jewelry sites.

### Material Badge & Swatch
**`material-badge`** — Pill-free: a flush label in `{typography.label-upper}` sitting inside a soft `{colors.surface-soft}` tile with a `{colors.hairline}` border. Used for "14K Gold", "Sterling Silver", "Gold Vermeil" callouts on the product detail. **`swatch-selector`** — 24px circular chips in `{rounded.full}` with a 2px `{colors.ink}` ring on the active state and a 1px `{colors.hairline}` ring at rest.

### Product Drawer
**`product-drawer`** — 480px side panel on desktop, full-screen modal on mobile. Title in `{typography.display-sm}` Newsreader, price in `{typography.title-md}` DM Sans. Add-to-cart CTA spans full panel width as a `button-primary` slab at the bottom. The serif title inside an otherwise sans panel reinforces the editorial/operational split that runs throughout the system.

### Footer
**`footer`** — Near-black (`{colors.dark-bg}`) ground with `{typography.label-upper}` section headings in white and `{typography.body-sm}` links in `{colors.hairline}`, lightening to `{colors.canvas}` on hover. No decorative elements — the inversion of the light-on-dark from the announcement bar creates a bookend around the page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; product grid 2-up; hero stacks image above text; nav collapses to hamburger + wordmark + cart icon; product drawer becomes full-screen modal; footer collapses to accordion |
| Tablet | 744–1128px | Product grid 3-up; hero remains split at 50/50 but at reduced font scale (display-xl → display-lg); nav shows primary category links inline; drawer remains side panel at 420px |
| Desktop | 1128–1440px | Product grid 4-up; hero at full display-xl scale; nav bar shows all category links; announcement bar visible |
| Wide | > 1440px | Content max-width caps at ~1440px with auto horizontal margins; hero image stretches edge-to-edge within the cap; grid maintains 4-up with larger gutters |

### Touch Targets
- All icon buttons in nav (cart, account, search, hamburger) minimum 44×44px tap area regardless of visual icon size
- Swatch selectors expand to 36px touch target with inset visual ring
- Product card entire tile is tappable, not just title text
- Footer accordion headers minimum 48px tall on mobile

### Collapsing Strategy
- Nav: hamburger drawer slides from left at full viewport height; categories listed at `{typography.title-md}` DM Sans; drawer background is `{colors.canvas}` with `{colors.hairline}` row dividers
- Hero: image moves above text column; headline scales from `{typography.display-xl}` to `{typography.display-md}` on mobile
- Product drawer: transitions to a bottom sheet that rises to 95vh with a drag handle; sticky add-to-cart CTA anchors to sheet bottom
- Footer: link groups collapse to tap-to-expand accordions at `{typography.title-sm}`; email signup moves above the grid

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand color beyond near-black neutrals was extracted — zero accent colors (no gold, rose, or warm tone) surfaced in the crawl; if Bagatiba uses a gold hover or active accent it was not present in top extracted colors
- White (`#ffffff`) is assumed as `canvas` and `surface-card` since it was not in the extracted color list (likely rendered as a browser default before JS paint)
- Font weights for Newsreader are inferred from editorial usage norms — exact weight values (300 vs 400 for display) not confirmed from computed styles
- No motion/animation tokens extracted (hover scale values, drawer slide duration are estimates based on category conventions)
- Icon system not observed — unclear whether Bagatiba uses a custom glyph set, Phosphor, or Feather icons
- Product page layout (single-image vs. multi-image scroll vs. thumbnail rail) not confirmed
- Dark mode or alternate color scheme not detectable from extracted tokens
