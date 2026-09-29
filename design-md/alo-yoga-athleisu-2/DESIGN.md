---
version: alpha
name: "Alo Yoga"
source_url: "https://aloyoga.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Lime at the edge of neon — #dbf482 appears as a promotional banner fill and seasonal product accent against a near-black canvas (#121212), and this contrast tells the entire brand story: a yoga company that photographs like a fashion house. The type system runs arquitecta for display headings and proxima-nova for all UI text, both set at compressed weights with wide tracking and uppercase transforms; there is no decorative serif, no handwritten warmth, no nostalgic gesture — only the cool composure of a brand that trusts editorial photography to carry all the emotion. Rounded corners stay minimal to nonexistent: product cards and primary CTAs sit on {rounded.none} edges, resisting the softness that most athleisure brands deploy as a cue for approachability. The primary CTA is a flat dark rectangle — {colors.ink} on {colors.canvas} or the reverse — with no gradient, no shadow, and no softening radius. Against this monochrome skeleton, the seasonal accent palette arrives like a colorway drop: blush pink (#f9cae6), sage (#758e6d), and cool teal (#00aba9) function as deliberate editorial punctuation rather than persistent system tokens, rotating with collections rather than hardwired to UI states. Navigation is austere and mega-menu-driven, with a horizontal flyout that lists categories in small proxima-nova caps alongside imagery panels — shopping is treated as a lookbook browse rather than a hierarchy to descend. Product cards hover-reveal a second colorway image with no badge or overlay text, letting the product do the selling. The footer inverts to the deep charcoal ground ({colors.footer-bg}: #232933) with white reversed type, a structural signal marking the editorial-to-commerce boundary. Spacing is generous: hero sections breathe at {spacing.section} vertical padding, product grids hold {spacing.lg}–{spacing.xl} gutters, and the absence of decorative elements makes every unit of negative space load-bearing. The overall register is aspirational minimalism — the composed confidence of a brand certain its photography is argument enough.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#dedede"
  ink: "#121212"
  body: "#232933"
  muted: "#758e6d"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-lime: "#dbf482"
  accent-pink: "#f9cae6"
  accent-teal: "#00aba9"
  sage: "#758e6d"
  footer-bg: "#232933"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'arquitecta', 'proxima-nova', Arial, sans-serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'arquitecta', 'proxima-nova', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.25px
    textTransform: uppercase
  display-md:
    fontFamily: "'arquitecta', 'proxima-nova', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: 0.5px
    textTransform: uppercase
  display-sm:
    fontFamily: "'arquitecta', 'proxima-nova', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  title-md:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  title-sm:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 1.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  price:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  product-name:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  footer-heading:
    fontFamily: "'proxima-nova', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 1.5px
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    height: 48px
    padding: "12px {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 32px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderTop: "1px solid {colors.hairline}"
    padding: "40px {spacing.xxl}"
    columnGap: "{spacing.xxl}"
    imagePanelWidth: 220px
    imagePanelAspectRatio: "3/4"
  promotional-banner:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    height: 36px
    textAlign: center
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.product-name}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    imageObjectFit: cover
    hoverBehavior: "cross-fade to second colorway image"
    gap: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px {spacing.sm}"
    position: "absolute top-left"
  colorway-swatch:
    size: 16px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderUnselected: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    height: 44px
    minWidth: 48px
    disabledStyle: "diagonal strikethrough line"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    ctaTypography: "{typography.button-md}"
    minHeight: 600px
    padding: "{spacing.section} 0"
    imagePosition: "full-bleed or 50/50 split panel"
  hero-accent-word:
    textColor: "{colors.accent-lime}"
    typography: "{typography.display-xl}"
  editorial-label:
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    backgroundColor: transparent
    marginBottom: "{spacing.sm}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 48px
    padding: "12px {spacing.base}"
    iconColor: "{colors.ink}"
    backdropColor: "{colors.scrim}"
    backdropOpacity: 0.4
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    headingTypography: "{typography.footer-heading}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    columnGap: "{spacing.xl}"
    borderTop: none
  newsletter-input:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.on-dark}"
    rounded: "{rounded.none}"
    height: 44px
    padding: "10px {spacing.base}"
    placeholderColor: "{colors.on-dark}"
    placeholderOpacity: 0.6
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  product-grid:
    columns: 4
    gap: "{spacing.lg}"
    rowGap: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — Flat black rectangle (`{rounded.none}`) at 48px tall, proxima-nova 14px/600 weight in uppercase with 1.5px tracking. The flatness is the signal: no pill, no radius, no shadow softens the transaction. Active state shifts to `{colors.primary-active}` (#000000); disabled renders `{colors.primary-disabled}` (#dedede) with body-text color to maintain legibility.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border, identical geometry to primary. Used for alternative CTAs in product detail and size-guide drawers. Ghost variant removes the border and underlines the label instead, for tertiary actions in footer and editorial contexts.

### Navigation

**`nav-bar`** — 64px fixed bar on `{colors.canvas}` with a 1px `{colors.hairline}` bottom border. Logo centered (mobile) or left-aligned (desktop) at 32px tall. Links in `{typography.nav-link}` uppercase proxima-nova; bag icon and account icon use 24px line icons. Transparent on full-bleed hero entries, reverting to white after the fold.

**`mega-menu`** — Drops full-width below the nav on hover/focus with 40px top padding. Left column lists sub-categories in `{typography.nav-link}`; right one to three columns hold 3:4 aspect imagery panels. No background overlay — the flyout sits directly over the page content. Closes on mouse-leave with a short 150ms fade-out.

**`promotional-banner`** — 36px strip above the nav filled with `{colors.accent-lime}` (#dbf482), centered `{typography.button-sm}` uppercase text in `{colors.ink}`. The lime-on-black-text contrast is the sole moment of chromatic heat in the otherwise neutral system.

### Product Cards

**`product-card`** — Flush-edge 3:4 image with zero border radius. On desktop hover, the primary image cross-fades to a second editorial shot in the same colorway — no caption, no overlay, no badge unless marked New or Sale. Below the image: product name in `{typography.product-name}`, price in `{typography.price}`, and a row of `colorway-swatch` dots that trigger image swap on hover.

**`product-card-badge`** — Flat `{colors.ink}` rectangle with `{colors.on-primary}` badge text, positioned absolute top-left. Used only for "New" and "Sale" labels; never stacked.

**`colorway-swatch`** — 16px filled circles in `{rounded.full}`, spaced 4px apart. Selected state adds a 2px `{colors.ink}` ring. Hovered swatch previews the product image without navigation.

**`size-selector`** — Square tap targets at 44px minimum, flat border, uppercase `{typography.button-sm}`. Sold-out sizes rendered with a diagonal CSS strikethrough line overlay rather than dimming alone, making unavailability legible at a glance.

### Hero & Editorial

**`hero-section`** — Full-bleed or split-panel layout, minimum 600px tall. Heading in `{typography.display-xl}` (arquitecta uppercase, 60px); individual words may render in `{colors.accent-lime}` via `hero-accent-word` for seasonal emphasis. CTA pair stacks primary + secondary buttons left-aligned or centered depending on image layout. Padding pulls from `{spacing.section}` to breathe against product grids below.

**`editorial-label`** — Small uppercase overline in `{typography.title-sm}` and `{colors.muted}` (#758e6d sage), used above collection headings and editorial module titles to set context before the display heading.

**`search-overlay`** — Full-width input that expands beneath the nav with a 40% `{colors.scrim}` backdrop. Flat border, no radius, icon at right edge. Results surface as a product grid below the input in the same overlay layer.

### Footer

**`footer`** — Full-width `{colors.footer-bg}` (#232933) ground with all text reversed to `{colors.on-dark}`. Column headings in `{typography.footer-heading}` uppercase; links in `{typography.body-sm}`. Newsletter module contains a flat `newsletter-input` paired with an inline submit arrow button. No decorative dividers — column gap alone creates structure.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + bag; hero heading drops to display-lg (40px); mega-menu becomes fullscreen drawer with accordion sub-sections |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + collapsed menu icon + utility icons; hero switches to stacked layout; footer collapses to two columns |
| Desktop | 1128–1440px | Four-column product grid; full mega-menu on hover; hero runs 50/50 split-panel or full-bleed with overlaid text; footer runs four columns |
| Wide | > 1440px | Max content width ~1440px with symmetric side padding; hero imagery scales but type locks at display-xl caps; grid stays four columns with increased gutter |

### Touch Targets

- All interactive controls 44px minimum height (size selector tiles, swatch dots padded to 44×44 tap zone)
- Nav icons 44px touch area even if visually 24px
- Swipe-to-close on mobile mega-menu drawer
- Colorway swatches padded to 32px tap zones despite 16px visual size

### Collapsing Strategy

- Mega-menu → fullscreen accordion drawer on mobile, no hover — tap category label to expand sub-list
- Four-column grid → two-column at tablet, single-column at mobile with full-width cards
- Hero split-panel → stacked (image top, text + CTA below) at tablet and mobile
- Promotional banner text truncates to ellipsis below 360px; never wraps to two lines
- Footer four-column → two-column at tablet → single-column stacked at mobile with full-width newsletter input

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `surface-soft` (#f5f5f5) is inferred — no explicit off-white surface token was extracted from the live site; actual value may differ
- Exact arquitecta weight variants (light/regular/bold) and numeric font-weight mappings were not extractable from CSS; weights above are approximated from visual inspection
- Animation timings for image cross-fade on product card hover and mega-menu open/close not captured — 150–200ms is assumed
- Accent color usage rules (which collections use #f9cae6 vs #dbf482 vs #00aba9) follow seasonal rotation logic not encoded in static CSS
- No dark-mode palette detected; theme-color meta was absent, suggesting no adaptive color scheme
- Exact letter-spacing values for display-xl and nav-link are approximated; live site may use em units tied to font-size
- Product card hover second-image URL convention (Shopify variant images) not confirmed — behavior inferred from common Alo UX pattern
