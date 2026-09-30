---
version: alpha
name: "Sports Memorabilia"
source_url: "https://www.sportsmemorabilia.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Signed jerseys frozen under anti-reflective glass, authentication holograms catching the light — Sports Memorabilia's digital storefront treats every product image as a trophy case centerpiece, building a high-contrast grid around deep navy and championship red that mirrors the official colorways of the leagues whose artifacts it sells. The primary brand anchor is a commanding navy (#0d1f3c) drawn from the visual vocabulary of playoff programs and arena signage, set against a white canvas that lets photography — glossy 8×10s, framed prints, wax-sealed premium cuts — carry the page. Red (#c8102e) fires every primary CTA and urgency badge, reading immediately as action in a category where authenticated scarcity drives conversion. A warm gold (#c9a84c) layer surfaces for "Authenticated" seals, hologram badges, and featured-product halos, coding premium trust cues that collectors recognize from physical grading labels. Typography leans on strong serif-adjacent weight contrasts: display headings drop into bold condensed uppercase, while product titles and pricing run in a clean geometric sans at modest weights, keeping the catalog readable across dense grids of cards and memorabilia. The layout geometry is mostly orthogonal — product-card corners sit at a subtle `{rounded.xs}`, pill badges use `{rounded.full}`, and the search bar is straight-cornered, signaling a data-forward catalog experience rather than the softened lifestyle aesthetic of apparel brands. Filters and facets run down a left rail on desktop, collapsing into a drawer on mobile. Authentication is the brand's core promise: nearly every product surface carries a "Beckett" or "JSA" inline badge, and the checkout flow surfaces certificate-of-authenticity modal previews before confirming. The overall register is authoritative and collector-first — this is a site that earns trust through provenance transparency, not aspirational lifestyle photography.

colors:
  primary: "#0d1f3c"
  primary-active: "#091629"
  primary-disabled: "#8fa3be"
  accent-red: "#c8102e"
  accent-red-active: "#a80d26"
  accent-gold: "#c9a84c"
  accent-gold-soft: "#f0e0a8"
  ink: "#111111"
  body: "#2d2d2d"
  muted: "#5a5a5a"
  hairline: "#d8d8d8"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f6f8"
  surface-card: "#ffffff"
  surface-navy-tint: "#e8ecf2"
  on-primary: "#ffffff"
  on-accent-red: "#ffffff"
  on-gold: "#0d1f3c"
  badge-auth: "#c9a84c"
  badge-auth-text: "#0d1f3c"
  badge-sale: "#c8102e"
  badge-sale-text: "#ffffff"
  star-rating: "#c9a84c"
  trust-seal-bg: "#f0e0a8"

typography:
  display-xl:
    fontFamily: "'Oswald', 'Impact', 'Arial Narrow', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Oswald', 'Impact', 'Arial Narrow', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0.3px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Oswald', 'Arial Narrow', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-lg:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  category-label:
    fontFamily: "'Oswald', 'Arial Narrow', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  auth-seal:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
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
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-accent-red}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.on-accent-red}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-navy:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-add-to-cart:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-accent-red}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
    width: "100%"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "none"
  nav-bar-top-stripe:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-accent-red}"
    typography: "{typography.caption}"
    height: 32px
  nav-search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px
    border: "none"
  category-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderTop: "3px solid {colors.accent-red}"
    padding: "{spacing.lg}"
    shadow: "0 4px 16px rgba(0,0,0,0.15)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    shadow: "0 1px 4px rgba(0,0,0,0.08)"
    imageAspectRatio: "1/1"
    padding: "{spacing.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.accent-red}"
  product-card-auth-badge:
    backgroundColor: "{colors.trust-seal-bg}"
    textColor: "{colors.badge-auth-text}"
    typography: "{typography.auth-seal}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
    border: "1px solid {colors.accent-gold}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.badge-sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 7px
  badge-authenticated:
    backgroundColor: "{colors.trust-seal-bg}"
    textColor: "{colors.badge-auth-text}"
    typography: "{typography.auth-seal}"
    rounded: "{rounded.xs}"
    padding: 3px 7px
    border: "1px solid {colors.accent-gold}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 7px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 420px
    overlay: "linear-gradient(to right, rgba(13,31,60,0.85) 45%, transparent)"
  featured-strip:
    backgroundColor: "{colors.surface-navy-tint}"
    textColor: "{colors.primary}"
    labelTypography: "{typography.category-label}"
    padding: "{spacing.lg} {spacing.xl}"
  league-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.primary}"
    activeIndicator: "3px solid {colors.accent-red}"
    padding: "{spacing.sm} {spacing.base}"
  filter-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    width: 240px
    padding: "{spacing.base}"
  price-range-display:
    typography: "{typography.price-lg}"
    textColor: "{colors.accent-red}"
    strikethroughColor: "{colors.muted}"
  authentication-modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    headerBg: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    sealColor: "{colors.accent-gold}"
    padding: "{spacing.xl}"
    shadow: "0 8px 32px rgba(0,0,0,0.2)"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.surface-navy-tint}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: "3px solid {colors.accent-red}"

## Components

### Buttons

**`button-primary` / `button-add-to-cart`** — The primary action button runs in `{colors.accent-red}` (#c8102e) with full-uppercase white type at `{typography.button-md}`, reflecting the urgency register of a scarcity-driven collectibles market. The add-to-cart variant is full-width at 52px tall to maximize tap target on product detail pages. Hover deepens to `{colors.accent-red-active}`; disabled state falls back to the `{colors.hairline}` / `{colors.muted}` pair.

**`button-navy`** — Secondary actions like "View Certificate" or "Learn More" use the primary navy (`{colors.primary}`), maintaining brand authority without competing with the red purchase CTA. Same uppercase geometry as the red button; used in editorial strips and authentication callouts.

**`button-gold`** — Applied sparingly to premium tier CTAs ("Shop Premium Cuts", "View Graded Cards"), using `{colors.accent-gold}` with `{colors.on-gold}` navy text. The warm metal color signals the authentication/grading tier that commands higher price points.

### Navigation

**`nav-bar-top-stripe`** — A 32px red stripe at the very top carries shipping promotions and trust messages in small caps, mimicking the alert-bar pattern common in sports retail. It uses `{colors.accent-red}` so it reads as urgent even before the main nav.

**`nav-bar`** — The main navigation sits in deep navy `{colors.primary}` at 60px, with a centered or left-aligned logo lockup and a dominant search bar (`{typography.body-md}` on white input) that spans the center third of the viewport. League and sport category pills sit in the sub-nav row below in `{colors.surface-navy-tint}`.

**`category-mega-menu`** — Triggers on desktop hover over top-level sport/league categories. A white panel drops with a `3px solid {colors.accent-red}` top border and grid-organized sub-categories with team-icon glyphs. Shadow (`0 4px 16px rgba(0,0,0,0.15)`) lifts the panel above page content clearly.

### Product Cards

**`product-card`** — Square-cropped product image fills the top portion of a white card with a subtle 1px hairline border and minimal shadow. Title in `{typography.title-sm}` runs up to two lines; price renders in `{colors.accent-red}` at `{typography.price-md}`. The `{colors.accent-gold}` authentication badge floats over the image bottom-left corner on authenticated items, immediately encoding provenance before the buyer reads a word of copy.

**`badge-authenticated`** — Gold-tinted pill with a 1px `{colors.accent-gold}` border and uppercase micro-type in `{typography.auth-seal}`. Maps directly to the physical hologram/seal vocabulary (Beckett, JSA, PSA) that collectors trust. Used on card thumbnails, PDP headers, and cart line items.

### Product Detail

**`authentication-modal`** — Triggered by "View Certificate" links; a centered modal with a navy header panel (`{colors.primary}`) and a large gold seal icon centered below. Certificate details run in `{typography.body-sm}` on white. The modal's weight and color signal that this is the most authoritative moment in the purchase flow.

**`price-range-display`** — Large red price in `{typography.price-lg}` sits left; if a sale is active, the original price renders at `{colors.muted}` with `text-decoration: line-through` in `{typography.body-md}` immediately to the right. No badge needed — the visual contrast communicates discount.

### Hero & Merchandising

**`hero-banner`** — Full-width editorial banner with a left-to-right navy-to-transparent overlay (`{colors.primary}` at 85% opacity) preserving player/item photography on the right half. Headline in `{typography.display-xl}` uppercase white; sub-copy in `{typography.body-md}`. CTA renders as `{components.button-primary}` at bottom-left of the text block.

**`featured-strip`** — A navy-tinted `{colors.surface-navy-tint}` horizontal strip carries "Shop by League", "Trending This Week", or "New Arrivals" as horizontally scrollable category tiles, each with a league logo and `{typography.category-label}` uppercase label.

**`league-tab`** — Horizontal tab row for filtering within a sport (NFL → Team → Player hierarchy). Active tab shows a 3px red underline against `{colors.primary}` text; inactive tabs are `{colors.muted}`. No background fill change — the underline alone carries the active state.

### Search & Filters

**`nav-search-bar`** — Borderless white input inside the navy nav bar, with a red search-submit button on the right end. The contrast inversion (white in navy) makes search immediately legible without a border treatment.

**`filter-sidebar`** — Fixed left rail on desktop in `{colors.surface-soft}` with checkbox facets for sport, team, player, price range, autograph type, and authentication tier. Section headers use `{typography.category-label}` uppercase. On mobile, collapses into a bottom-sheet drawer triggered by a "Filter & Sort" button.

### Footer

**`footer`** — Full-width navy `{colors.primary}` block with a 3px red top border, four-column link grid in `{typography.body-sm}`, and secondary link text in `{colors.surface-navy-tint}` for legibility. Trust logos (Beckett, PSA, JSA partnerships) render in a dedicated row above the legal bar, reinforcing authentication credentials at the exit point of every page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar becomes bottom-sheet drawer; hero banner crops to portrait with full-overlay treatment; nav collapses to hamburger + search icon; top stripe hidden |
| Tablet | 744–1128px | Two-column product grid; filter sidebar overlays as panel rather than inline rail; sub-nav league tabs scroll horizontally; hero banner runs at 320px height |
| Desktop | 1128–1440px | Three- to four-column product grid; filter sidebar renders inline at 240px; mega-menu active; hero at full 420px with side-by-side text+image layout |
| Wide | > 1440px | Grid centers in a 1440px max-width container with side padding; hero background bleeds full-width while content stays constrained; featured strips show 6-up tile rows |

### Touch Targets

- All add-to-cart and primary CTA buttons are minimum 52px tall with full-width layout on mobile
- Authentication badge tap opens modal with 44px close target in top-right corner
- Filter checkboxes padded to 44px hit area via `{spacing.base}` vertical padding per row
- Nav hamburger icon is 48×48px with no border
- Product card entire surface is tappable (no separate "tap here" link)

### Collapsing Strategy

- Left filter rail (240px) collapses to bottom-sheet drawer triggered by sticky "Filter" pill at bottom of viewport on mobile
- Mega-menu drops down on hover (desktop) and is replaced by accordion inside hamburger drawer (mobile/tablet)
- Top promotional stripe (`nav-bar-top-stripe`) hides at < 744px to preserve vertical space
- League sub-nav tabs switch to horizontal scroll with snap-points at < 1128px
- Hero text column stacks above image at < 744px; overlay removed in favor of a flat navy panel

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All colors are estimated** — the live site returned "Access Denied" (bot protection/CDN block), so no hex values were extracted; palette is inferred from general brand knowledge of sports memorabilia retail aesthetics and may not match current production tokens
- **Font families unconfirmed** — no font-family stacks were extracted; Oswald + Open Sans is a plausible sports-retail pairing but may differ from the actual implementation
- **Exact border-radius values unknown** — `{rounded.xs}` (4px) assumed from catalog-style orthogonal aesthetic; not extracted from CSS
- **Authentication badge design** — specific Beckett/JSA/PSA inline badge dimensions, iconography, and layout are assumed based on industry convention, not extracted from live components
- **Navigation structure** — sub-nav depth, mega-menu column count, and league taxonomy ordering are inferred; actual IA may differ significantly
- **Dark mode or alternate themes** — unknown whether a dark-mode variant exists
- **Promotional/sale badge system** — exact badge shapes, colors for additional tiers (e.g., "Limited Edition", "Graded") could not be verified
- **Checkout and account flows** — no access to authenticated pages or cart/checkout UI
