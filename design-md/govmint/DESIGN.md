---
version: alpha
name: "GovMint"
source_url: "https://www.govmint.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Coin photography drives every spatial decision at GovMint — obverse and reverse shots rendered at near-macro scale against near-black velvet force the layout to recede into deep navy scaffolding so the metal itself holds the light. The "Gov" prefix does deliberate work: it borrows the iconographic vocabulary of official mints — seals, eagles, engraved serif letterforms, the gravity of federal institutions — while operating as a fully commercial marketplace. That tension between sovereign authority and e-commerce pragmatics runs through the entire system. Primary actions fire in a muted coin-gold (#c8962e), not the electric blues common to fintech; the brand would rather suggest precious metal than urgency. Dark hero sections in near-midnight navy (#0d1f3c) give way to white product-listing surfaces, creating a strong light/dark alternation that mimics a display case — objects on felt, price tags under glass. Headlines lean on a condensed serif or slab face to invoke engraved legend text on actual coin dies; body copy drops to a neutral sans to keep long product descriptions legible. Trust signals — NGC/PCGS grade badges, mintage-limit callouts, certified-dealer banners — are treated as first-class UI components, not footnotes, because the purchase decision in numismatics is entirely dependent on provenance data. Rounded corners are conservative ({rounded.sm} at most on cards, {rounded.xs} on badges), reflecting the rectilinear precision of packaging rather than the soft consumer-app aesthetic. The overall register is authoritative and collection-minded: a site built for buyers who already know what MS-70 means and want to confirm it before they commit.

colors:
  primary: "#c8962e"
  primary-active: "#a87920"
  primary-disabled: "#e8d4a0"
  ink: "#0d1f3c"
  body: "#1e2d45"
  muted: "#5a6a80"
  hairline: "#d4d9e0"
  hairline-soft: "#eaedf1"
  canvas: "#ffffff"
  surface-soft: "#f5f6f8"
  surface-card: "#ffffff"
  surface-dark: "#0d1f3c"
  surface-dark-mid: "#14294d"
  on-primary: "#0d1f3c"
  on-dark: "#ffffff"
  accent-gold-light: "#f0d080"
  accent-red: "#b22234"
  accent-red-muted: "#8b1a26"
  grade-badge: "#1a3a6b"
  certified-green: "#2e7d4f"
  error: "#c0392b"
  star-rating: "#c8962e"

typography:
  display-xl:
    fontFamily: "'Georgia', 'Playfair Display', 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Georgia', 'Playfair Display', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Georgia', 'Playfair Display', 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge-label:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  grade-stamp:
    fontFamily: "'Georgia', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 1px
  button-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Georgia', serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  price-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  mintage-label:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.6px
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
    padding: 13px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 48px
    border: "2px solid {colors.on-dark}"
  button-add-to-cart:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 52px
  button-add-to-cart-active:
    backgroundColor: "{colors.accent-red-muted}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    topBarHeight: 36px
    topBarBackground: "{colors.ink}"
    topBarTypography: "{typography.caption}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    shadow: "0 4px 12px rgba(0,0,0,0.18)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1:1"
    padding: "{spacing.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    shadow: "0 2px 6px rgba(0,0,0,0.07)"
  product-card-hover:
    shadow: "0 6px 20px rgba(0,0,0,0.14)"
    border: "1px solid {colors.primary}"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    overlayOpacity: 0.55
  hero-gold-accent:
    accentColor: "{colors.primary}"
    accentLineHeight: 3px
    accentWidth: 60px
    accentMarginBottom: "{spacing.lg}"
  grade-badge:
    backgroundColor: "{colors.grade-badge}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    border: "1px solid {colors.primary}"
  certified-badge:
    backgroundColor: "{colors.certified-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  mintage-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.mintage-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  coin-flip-viewer:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.md}"
    shadowActive: "0 0 0 3px {colors.primary}"
    buttonSize: 32px
    buttonBackground: "{colors.surface-dark-mid}"
    buttonColor: "{colors.on-dark}"
    buttonRounded: "{rounded.full}"
  price-block:
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    premiumLabelTypography: "{typography.caption}"
    premiumLabelColor: "{colors.muted}"
    spotPriceTypography: "{typography.body-sm}"
    spotPriceColor: "{colors.muted}"
  deal-banner:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    iconColor: "{colors.primary}"
    padding: "{spacing.md} 0"
  category-tile:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    overlayGradient: "linear-gradient(to top, rgba(13,31,60,0.85) 0%, rgba(13,31,60,0.1) 100%)"
    aspectRatio: "3:2"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    height: 44px
    iconColor: "{colors.muted}"
  pagination:
    activeBackground: "{colors.primary}"
    activeColor: "{colors.on-primary}"
    inactiveBackground: "{colors.canvas}"
    inactiveColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    size: 36px
    typography: "{typography.button-sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-gold-light}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Gold-filled CTA (`{colors.primary}` background, `{colors.on-primary}` dark navy text) with uppercase letter-spacing treatment from `{typography.button-md}`. The dark text on gold is brand-intentional: it evokes an engraved coin legend rather than a high-contrast web button. Active state deepens to `{colors.primary-active}`; disabled washes out to `{colors.primary-disabled}` with muted text.

**`button-add-to-cart`** — Patriotic red (`{colors.accent-red}`) replaces gold for the decisive commerce action, creating a clear hierarchy: gold is browse/learn, red is buy. Taller than primary at 52px to emphasize purchase weight on product detail pages.

**`button-secondary`** — White fill with a 2px ink border. On dark hero surfaces, `button-secondary-dark` swaps to transparent fill with a white border so the outline reads cleanly against `{colors.surface-dark}`.

### Text Input & Search

**`text-input`** — Single-pixel `{colors.hairline}` border at rest, jumping to a 2px gold `{colors.primary}` ring on focus. This focus ring reinforces the gold brand signal even in utility contexts.

**`search-bar`** — Full-pill `{rounded.full}` form distinguishes site-search from the rectilinear product filters and form fields. Sits in the nav bar against the dark background.

### Navigation

**`nav-bar`** — Two-tier structure: a slim 36px top bar in deepest `{colors.ink}` carrying trust signals (phone number, secure-checkout copy) in `{typography.caption}`; below it, a 60px dark navy `{colors.surface-dark}` primary nav with mega-drop category columns. The distinction between the two tiers communicates "service context above, catalogue navigation below." No border-bottom separates nav from hero — the hero's own dark background creates continuity.

**`nav-dropdown`** — White surface with a strong drop shadow (`rgba(0,0,0,0.18)`) and zero border radius, snapping to rectilinear grid discipline. Column headers use `{typography.title-sm}`, links use `{typography.body-sm}`.

### Product Card

**`product-card`** — 1:1 aspect-ratio product image (coin photography benefits from square crop) above a tight data block: title in `{typography.title-sm}`, price in `{typography.price-sm}`, and an optional `grade-badge` pinned to the top-left of the image. Hover state adds a gold `{colors.primary}` border ring to signal interactivity without animation. Cards use `{rounded.sm}` (4px) — just enough to soften die-cut packaging photography.

### Coin Viewer

**`coin-flip-viewer`** — A dark `{colors.ink}` panel housing the obverse/reverse toggle UI. Two circular buttons (`{rounded.full}`, 32px) with `{colors.surface-dark-mid}` fill switch between faces. The active card gets a gold `box-shadow` ring (`0 0 0 3px {colors.primary}`) so the selected face reads immediately. This is the centrepiece interactive component — everything else in the layout defers to it.

### Pricing & Data Display

**`price-block`** — Large serif price via `{typography.price-display}` anchors the product detail sidebar. Below it, a muted `{typography.caption}` line shows spot-price premium as a percentage, giving collectors the numismatic context they expect. No sale strikethrough pattern; price changes are communicated via callout banners.

**`grade-badge`** — Navy `{colors.grade-badge}` pill with gold border and uppercase `{typography.badge-label}`. Carries grade codes like "MS-70" or "PR-70 DCAM." On light card surfaces the navy/gold pairing reads as authoritative credential rather than a promotional tag.

**`mintage-callout`** — Soft `{colors.surface-soft}` block with uppercase `{typography.mintage-label}` displaying edition size ("MINTAGE: 10,000"). The deliberate restraint — no icon, no accent color — keeps it factual. Scarcity is implied by the number, not by visual urgency.

### Hero & Category

**`hero-dark`** — Full-bleed dark navy section with coin or lifestyle photography behind a `0.55` opacity scrim. A gold accent bar (`hero-gold-accent`, 60px wide × 3px tall) precedes the display headline, functioning like a ribbon or medal stripe to introduce the brand's authoritative register before text appears.

**`category-tile`** — Dark-navy-overlaid photo tile using a top-to-bottom gradient that fades from near-opaque at bottom to near-transparent at top. Title sits at the bottom in `{typography.title-md}` white. Used in grid formations (typically 3–4 columns) to present coin categories: American Eagles, World Coins, Certified, etc.

### Trust & Footer

**`trust-bar`** — Full-width band in `{colors.surface-soft}` appearing below the nav on interior pages and above the footer on homepage. Four to five icon+label pairs (Secure Checkout, 30-Day Returns, Certified Dealer, Expert Support) in `{typography.caption}` with gold icons. Communicates legitimacy at the layout level, not as a footnote.

**`deal-banner`** — Red `{colors.accent-red}` full-width strip for time-sensitive promotions. Text in white `{typography.title-sm}`. Used sparingly — because the brand's primary vocabulary is gold, red reads as genuine urgency when it appears.

**`footer`** — Near-black `{colors.ink}` with a 3px gold top border as a closing bookend to the hero's gold accent. Link columns use `{colors.accent-gold-light}` for legibility against dark ground. Includes trust logos (NGC, PCGS, BBB) in muted white treatment.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen dark drawer; coin-flip-viewer fills 100vw; price-block moves below images; trust-bar scrolls horizontally as a chip row |
| Tablet | 744–1128px | Two-column product grid; nav retains horizontal links, drops mega-menu for single-level dropdowns; hero height reduces to 360px; category tiles shift to 2-column grid |
| Desktop | 1128–1440px | Three–four column product grid; full mega-dropdown nav; side-by-side layout on PDP (viewer left, price-block right); hero at full 480px |
| Wide | > 1440px | Content max-width caps at 1360px, centered; hero extends edge-to-edge with content constrained; six-column category tile grid available |

### Touch Targets

- All buttons minimum 44px tall; `button-add-to-cart` elevated to 52px for thumb prominence
- Nav hamburger tap target 48×48px even when icon visually smaller
- `coin-flip-viewer` face-toggle buttons 44px touch target via padding wrapper around 32px visual
- Pagination controls minimum 44px with `{spacing.sm}` gap between items
- Product card entire surface is tappable; badge overlays do not interrupt tap propagation

### Collapsing Strategy

- Mega-dropdown nav collapses to a two-level accordion inside the dark full-screen mobile drawer; top-level categories are bold, subcategories indent with `{spacing.base}` left padding
- `trust-bar` converts from a five-icon horizontal row to a horizontally scrolling single-row chip list; no vertical stacking to preserve vertical space
- `price-block` on PDP moves from right-rail sidebar to a sticky bottom bar on mobile with `button-add-to-cart` pinned at screen bottom
- Hero typography scales from `{typography.display-xl}` (42px) on desktop to `{typography.display-md}` (28px) on mobile; hero min-height reduces from 480px to 280px
- Category tile grid collapses from 4-col → 2-col → 1-col with aspect ratio shifting from 3:2 to 16:9 on mobile for better thumb browsing

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex colors are brand-knowledge estimates, not extracted values.** The site returned HTTP 405 (Not Allowed) during crawl; zero colors were captured. Actual brand primaries (navy, gold, red values) should be verified against live CSS or design files before production use.
- **All font families are estimates.** No font stacks were detected from the live site. GovMint may use a licensed custom or commercial font (e.g., a slab serif for headlines); the Georgia/Arial fallback chain used here is a safe approximation only.
- **No theme-color meta tag was found**, so the mobile browser chrome color (used in PWA/tab contexts) is unknown.
- **Component states (hover, focus, loading, error) for e-commerce flows** (checkout, address form, payment) were not observable due to the blocked crawl.
- **Specific grading-partner badge assets** (NGC slab styling, PCGS holder imagery) are proprietary and not captured; badge component specs above are structural approximations.
- **Animation and transition values** (coin-flip duration, card hover easing, drawer slide timing) are entirely unknown and not specified.
- **Mobile navigation structure** (number of top-level items, drawer vs. overlay behavior) is inferred from category conventions and not confirmed.
- **Promotional band frequency and color variants** beyond red/gold are unconfirmed; the brand may use additional accent states for special events (Presidential series, holiday sales).
