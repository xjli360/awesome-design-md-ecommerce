---
version: alpha
name: "Sideshow"
source_url: "https://www.sideshow.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Near-black canvas (#0a0a0a) turns every product photograph into a light source — Sideshow's most consequential design decision is the one that disappears completely: background. A warm gold (#c9a84c) carries every primary CTA, price callout, and hover glow, behaving less like a brand color and more like a spotlight. The site is organized around a collector's taxonomy that most e-commerce platforms would flatten into categories: Sixth Scale Figure, Premium Format Figure, Statue, Diorama, and Polystone are first-class navigation concepts with their own badge language, edition-count limits, and filtering layer.

  Typography runs at heavy weight and tight letterspacing for display, producing a cinematic register that never tips into gothic excess. Body copy sits at generous contrast against the dark surfaces while a muted tier (#9e9e9e) handles secondary metadata — edition size, pre-order window, scale specification — without competing for attention. Display headings frequently uppercase-lock with expanded tracking, a convention shared across entertainment-adjacent collector brands. Franchise chips — Star Wars, Marvel, DC, Lord of the Rings, Alien — run as persistent pill navigation across category pages, signaling that the site's primary mental model is universe, not product type.

  Product cards distill to four elements on dark surface: the product photograph (portrait 3:4 ratio, zero padding), a gold-outlined edition badge, a title in white, and a price row that surfaces installment-payment copy inline. "Pre-Order Now" and "Add to Cart" states share the same gold fill; "Sold Out" drops to a ghost button in muted gray (#6b6b6b), communicating availability entirely through color and fill without needing a separate component variant. Wishlist hearts overlay product images at hover, a soft interactive layer on an otherwise dramatic static grid.

  Hero banners run full-bleed with a bottom-third dark gradient overlay, letting title and CTA float on a readable dark surface without a distinct content panel. The overall rhythm is theatrical restraint — the gold accent is rationed to action states and premium signals only, never decorative.

colors:
  primary: "#c9a84c"
  primary-active: "#b8942e"
  primary-disabled: "#5c4e24"
  ink: "#ffffff"
  body: "#e8e8e8"
  muted: "#9e9e9e"
  muted-soft: "#6b6b6b"
  hairline: "#2a2a2a"
  hairline-soft: "#1e1e1e"
  canvas: "#0a0a0a"
  surface-soft: "#141414"
  surface-card: "#1a1a1a"
  surface-raised: "#242424"
  on-primary: "#0a0a0a"
  sold-out: "#6b6b6b"
  pre-order-accent: "#4a90d9"
  sale-red: "#c41e3a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Gotham', 'Montserrat', 'Arial Narrow', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Gotham', 'Montserrat', 'Arial Narrow', Arial, sans-serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  installment-sm:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  badge-label:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  edition-meta:
    fontFamily: "'Gotham', 'Montserrat', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost-muted:
    backgroundColor: "transparent"
    textColor: "{colors.sold-out}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.sold-out}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-preorder:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    labelPrefix: "PRE-ORDER — "
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 36px
  mega-nav-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    border: "none"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
  product-card-meta:
    padding: "{spacing.sm} {spacing.base}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
  edition-badge:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sold-out-badge:
    backgroundColor: "transparent"
    textColor: "{colors.sold-out}"
    typography: "{typography.badge-label}"
    border: "1px solid {colors.sold-out}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  new-release-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sale-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  franchise-chip:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 16px
    border: "1px solid {colors.hairline}"
  franchise-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 16px
    border: "1px solid {colors.primary}"
  edition-type-tab:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 10px 0
    borderBottom: "2px solid transparent"
  edition-type-tab-active:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 10px 0
    borderBottom: "2px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    overlayGradient: "linear-gradient(to top, rgba(0,0,0,0.88) 0%, rgba(0,0,0,0.35) 45%, transparent 100%)"
    minHeight: 580px
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    ctaComponent: "button-primary"
    contentAlignment: "bottom-left"
    padding: "0 {spacing.xl} {spacing.xl}"
  price-row:
    textColor: "{colors.primary}"
    typography: "{typography.price-display}"
    installmentColor: "{colors.muted}"
    installmentTypography: "{typography.installment-sm}"
    gap: "{spacing.xs}"
  wishlist-overlay:
    backgroundColor: "transparent"
    iconColor: "{colors.muted}"
    iconColorActive: "{colors.primary}"
    position: "top-right"
    padding: "{spacing.sm}"
    trigger: hover
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    height: 44px
    iconColor: "{colors.muted}"
  search-results-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    maxHeight: 480px
  product-spotlight:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    padding: "{spacing.section}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.edition-meta}"
  edition-limit-counter:
    textColor: "{colors.muted}"
    typography: "{typography.edition-meta}"
    highlightColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.body}"
    headingTypography: "{typography.title-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"
  newsletter-row:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    inputComponent: "text-input"
    ctaComponent: "button-primary"
    padding: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — Gold fill (#c9a84c) on black canvas, uppercase tracked type at 1.5px letterSpacing, zero border-radius for a hard-edged industrial finish. Active state deepens to #b8942e; disabled degrades to a dimmed gold-brown (#5c4e24) with muted text. Used for "Add to Cart", "Buy Now", and "Pre-Order Now" — the `button-preorder` variant prepends a "PRE-ORDER — " label in the same component shell.

**`button-secondary`** — Transparent fill with 1px solid white border, matching height and typography to `button-primary`. Serves secondary actions like "Learn More" and "View Details" where the gold CTA is already present. Hover inverts to white fill with black text.

**`button-ghost-muted`** — Transparent fill, 1px solid #6b6b6b border, muted gray text. The "Sold Out" button state. Communicates unavailability entirely through color — no icon, no disabled cursor needed.

### Product Card

**`product-card`** — Portrait 3:4 image fills the card top; no rounded corners, no drop shadow. Below the image, a narrow meta strip holds the edition badge row, product title in `{typography.body-sm}`, and the price row. The `{colors.primary}` price contrasts against `{colors.surface-card}` without competing with the image. On hover, a wishlist heart appears top-right and the image scales subtly (transform: scale(1.03)) within overflow-hidden bounds.

### Edition Badge System

**`edition-badge`** — Gold-outlined pill chip using `{typography.badge-label}` for edition type (Sixth Scale, Premium Format, Statue). **`sold-out-badge`** — same shape, muted gray. **`new-release-badge`** — gold fill, black text. **`sale-badge`** — #c41e3a fill. Badges stack horizontally above the product title with `{spacing.xs}` gap, never wrapping.

### Franchise Chip Navigation

**`franchise-chip`** and **`franchise-chip-active`** — Full-radius pills running horizontally across category page headers. Inactive chips use `{colors.surface-raised}` with subtle hairline border; active inverts to gold fill. Franchise chips act as a persistent filter layer before the edition-type tabs below them — two-tier filtering with distinct visual registers.

### Hero Banner

**`hero-banner`** — Full-bleed photograph with a bottom-third gradient overlay (opacity 0 at 45%, 0.88 black at 0%). Title in `{typography.display-xl}` uppercase, subtitle in `{typography.display-sm}`, gold CTA button anchored bottom-left with `{spacing.xl}` padding. The gradient approach keeps the photograph dominant while making text legible — no frosted panel, no content box.

### Navigation

**`nav-bar`** — 64px height on `{colors.canvas}`, logo left-anchored, franchise/category links in `{typography.nav-link}` uppercase, search + wishlist + account icons right. Bottom hairline `{colors.hairline}` separates from page without lifting the nav off the dark ground. **`mega-nav-panel`** drops as a full-width dark panel on hover, organized in columns by franchise with image thumbnails and "New" badges.

### Price Row

**`price-row`** — Full price in `{typography.price-display}` at `{colors.primary}`, immediately below in `{typography.installment-sm}` at `{colors.muted}` an installment option ("or 4 payments of $X with Sezzle"). The two lines stack with `{spacing.xs}` gap, keeping payment flexibility visible without dominating the card.

### Footer

**`footer`** — `{colors.surface-soft}` background, column layout with `{typography.title-sm}` uppercase headings in `{colors.body}` and `{typography.body-sm}` links in `{colors.muted}`. Newsletter signup row sits above the column grid: full-width input + gold CTA. Social icons row at the bottom in muted gray, no fill.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces mega-menu; franchise chips scroll horizontally with snap; hero min-height drops to 380px; price row stacks vertically |
| Tablet | 744–1128px | 2-column product grid; nav collapses category links into a condensed top bar; franchise chips wrap into 2 rows or scroll; hero height 480px |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-nav on hover; franchise chips visible without scroll; hero at full 580px |
| Wide | > 1440px | Grid expands to 4–5 columns with max-width container (1440px) centered; hero image scales up, content stays left-anchored within container |

### Touch Targets

- All CTA buttons minimum 48px height
- Franchise chips minimum 36px height with 16px horizontal padding
- Wishlist heart overlay minimum 40×40px tap area
- Nav icons minimum 44×44px tap area
- Edition filter tabs 44px minimum touch height

### Collapsing Strategy

- Mega-nav collapses to hamburger drawer at tablet breakpoint; franchise filter moves inside drawer
- Edition-type tab row converts to horizontal scroll (no wrapping) below desktop
- Product card meta strip remains identical across breakpoints; image ratio preserved
- Footer column grid collapses from 4 columns → 2 → 1 accordion on mobile
- Newsletter row stacks input above CTA button on mobile (full-width both)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- All hex colors are inferred from brand knowledge; live extraction returned zero color data — the site likely loads design tokens via client-side JS or behind anti-bot protection
- Font stack unknown; "Gotham" is a reasonable inference for this market segment but may be Proxima Nova, a custom typeface, or another licensed condensed sans-serif — verify against actual CSS before implementation
- Exact border-radius values not confirmed; the brand reads as zero-radius (sharp corners) throughout but corner size on input fields and badges is an assumption
- Animation timing curves and transition durations not available
- Exact spacing scale not extracted; values above follow an 8px base grid inferred from visual inspection
- Dark-mode vs. light-mode switching behavior unknown — the site may be dark-only or offer a toggle
- Pre-order countdown timer component structure not confirmed
- Installment-payment partner (Sezzle, Afterpay, Klarna) may have changed; confirm branding rules before rendering logos inline
