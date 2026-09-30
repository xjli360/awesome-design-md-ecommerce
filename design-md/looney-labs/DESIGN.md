---
version: alpha
name: "Looney Labs"
source_url: "https://www.looneylabs.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Purple hits you first — not a muted lavender or corporate violet but a saturated, slightly warm #6745a3 that reads like a tabletop wizard's cloak draped across every primary button, nav accent, and collection badge. Looney Labs sells card games (Fluxx, Chrononauts, Pyramids) to a community that skews playful-nerdy, and the digital storefront mirrors that energy through a triadic accent system: teal #22d6ce pops on hover states and promotional callouts, coral #fb8077 flags sale prices and urgency badges, and the purple anchors everything authoritative. Type is set entirely in Open Sans — a utilitarian sans-serif that stays out of the way while dense game-rule descriptions, flavor text, and product specs do the heavy lifting. Display headings run at weight 700 in the 28–32px range; body copy stays at 16px/400 with generous 1.6 line-height to keep long product descriptions scannable. Cards sit on a white #ffffff canvas with soft gray #dedede hairlines and `{rounded.md}` corners — rounded enough to feel approachable but squared enough to stack cleanly in a multi-column grid. The product card pattern dominates: a large square image (game box art does the marketing), a bold title, a teal "Add to Cart" pill or purple primary button depending on context, and a small muted price line in #777777. Navigation is minimal — a sticky top bar with the Looney Labs pyramid logo left-aligned, a handful of collection links in `{typography.nav-link}`, and a cart icon badged in coral when items are present. Footer runs dark (#121212 background, white text) with newsletter signup and social links. Spacing is generous at the section level (`{spacing.section}` between content blocks) but tight within cards (`{spacing.sm}` between title and price), creating a rhythm that lets colorful box art breathe while keeping purchase-relevant info clustered. The overall impression is a toy store's enthusiasm filtered through clean e-commerce conventions — nothing precious, nothing overwrought, just enough color and curve to signal fun without sacrificing clarity.

colors:
  primary: "#6745a3"
  primary-active: "#553892"
  primary-disabled: "#b8a7d4"
  secondary: "#22d6ce"
  secondary-active: "#1abfb8"
  accent-warm: "#fb8077"
  accent-warm-active: "#e0615a"
  ink: "#121212"
  body: "#666565"
  muted: "#777777"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-secondary: "#ffffff"
  sale: "#fb8077"
  star-rating: "#fbbc04"

typography:
  display-xl:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-compare:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.md}"
    border: 2px solid {colors.primary-active}
  button-add-to-cart:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-add-to-cart-active:
    backgroundColor: "{colors.secondary-active}"
    textColor: "{colors.on-secondary}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
  text-input-focus:
    border: 2px solid {colors.primary}
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.lg}
  nav-bar-logo:
    height: 40px
    maxWidth: 160px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: 1/1
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.md}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-compare-price:
    typography: "{typography.price-compare}"
    color: "{colors.muted}"
    textDecoration: line-through
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
  collection-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  sale-badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  cart-icon-badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    minWidth: 20px
    height: 20px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
  collection-header:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.xl} 0"
    borderBottom: 1px solid {colors.hairline}
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.on-dark}"
    marginBottom: "{spacing.base}"
  newsletter-input:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
    border: 1px solid rgba(255,255,255,0.3)
  newsletter-submit:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: 1px solid {colors.hairline}
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    separator: "/"

---

## Components

### Buttons

**`button-primary`** — The default action button uses the brand purple `{colors.primary}` with white text, `{rounded.md}` corners, and 600-weight Open Sans at 16px. On hover/active it darkens to `{colors.primary-active}`; disabled state fades to `{colors.primary-disabled}` with no cursor interaction. Minimum width of 120px on desktop; full-width on mobile within card contexts.

**`button-secondary`** — White fill with a 2px purple border and purple text. Hover fills `{colors.surface-soft}` and deepens the border to `{colors.primary-active}`. Used for secondary actions like "View Details" or "Learn the Rules" alongside a primary CTA.

**`button-add-to-cart`** — The teal pill button (`{colors.secondary}`, `{rounded.full}`) is reserved exclusively for add-to-cart actions across product cards and PDP pages. The full-radius shape and distinct color separate commerce actions from navigation. Hover darkens to `{colors.secondary-active}`.

### Navigation

**`nav-bar`** — A sticky 64px-tall white bar with a thin `{colors.hairline}` bottom border. Logo sits left at 40px height; collection links run center-aligned in `{typography.nav-link}`; cart icon with `{cart-icon-badge}` sits right. On mobile, links collapse into a hamburger drawer.

**`search-bar`** — A pill-shaped input (`{rounded.full}`) in `{colors.surface-soft}` that lives in the nav or as a hero element on the shop page. Placeholder text in `{colors.muted}`, focus ring in `{colors.primary}`.

### Product Display

**`product-card`** — Square image (1:1 aspect, `{rounded.sm}` corners) above title, price, and optional sale badge. Cards have a soft `{colors.hairline-soft}` border and `{rounded.md}` outer radius. On hover, a subtle 2px upward translate and box-shadow appear. Price displays in `{typography.price}`; compare-at price shows struck-through in `{colors.muted}`.

**`collection-header`** — A `{typography.display-md}` heading with bottom hairline, used at the top of filtered grid views. Left-aligned with `{spacing.xl}` vertical padding.

**`sale-badge`** — Coral (`{colors.accent-warm}`) pill overlaid on the top-right of product card images. Uses `{typography.badge}` (11px, 700 weight, uppercase). Typical content: "SALE" or "-20%".

**`collection-badge`** — Purple pill badge used in navigation dropdowns and promotional banners to highlight game categories (e.g., "NEW", "BEST SELLER").

### Hero & Promotional

**`hero-banner`** — Full-width purple block with white display text and a reversed CTA button (white fill, purple text, `{rounded.full}`). Minimum height of 400px ensures box-art imagery or illustrated backgrounds have room to breathe. Text overlays center-aligned on mobile, left-aligned with max-width constraint on desktop.

### Cart & Commerce

**`quantity-selector`** — A compact inline stepper with minus/plus buttons flanking a centered number. `{rounded.sm}` corners, `{colors.hairline}` border, 40px height.

**`cart-icon-badge`** — A 20px coral circle overlapping the cart icon's top-right corner, showing item count in `{typography.caption-bold}`.

### Footer

**`footer`** — Dark background (`{colors.surface-dark}`) with white text organized in 3–4 columns: About, Games, Support, Newsletter. Column headings use `{typography.title-sm}`; links use `{typography.body-sm}` with underline on hover.

**`newsletter-input`** — Semi-transparent white input field within the footer, paired with a teal `{newsletter-submit}` button. Both use `{rounded.full}` for visual consistency with the add-to-cart pill language.

### Utility

**`breadcrumb`** — Muted gray caption text with "/" separators. Appears below the nav-bar on PDP and collection pages.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav links collapse to hamburger drawer; hero text centers and shrinks to `{typography.display-md}`; buttons go full-width inside cards; footer stacks into single column accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows top 4 links with overflow into "More" dropdown; hero maintains side-by-side text/image layout; footer runs two columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav visible; hero at full 400px+ height with left-aligned copy; footer in four columns |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid holds four columns with increased card spacing; additional whitespace on flanks |

### Touch Targets

- All interactive elements maintain minimum 44×44px tap area on mobile
- Product card entire surface is tappable (link wraps the card), not just the title
- Quantity stepper buttons are 40×40px with 8px gap between them
- Nav hamburger icon is 48×48px tap target
- Cart icon tap area extends to include the badge overlay

### Collapsing Strategy

- Navigation links collapse into a full-height slide-in drawer on mobile with `{spacing.lg}` vertical rhythm between items
- Product grid collapses from 4 → 2 → 1 columns as breakpoints step down
- Footer columns collapse into expandable accordions on mobile — headings become tap targets with chevron indicators
- Hero banner stacks image below text on mobile; CTA button anchors to bottom of the text block
- Search bar moves from inline nav position to a dedicated row below the nav on mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one font family (Open Sans) was detected; the site may load additional display or decorative typefaces via JavaScript or third-party theme assets that weren't captured in static extraction
- Many of the extracted hex colors (#4285f4, #34a853, #fbbc04, #ea4335, #eb001b, #f79e1b, #ff5f00, #003087, #142688) are payment provider icons (Google Pay, Mastercard, PayPal, Visa) rather than brand tokens — these have been excluded from the palette
- No CSS custom properties or design-token variable names were captured; spacing and radius values are inferred from common Shopify theme patterns
- Illustration style, game-box photography treatment, and any animated micro-interactions (card flips, dice rolls) could not be extracted from static analysis
- The exact hover/focus shadow values and transition durations are not available — implementations should default to 0.2s ease and subtle box-shadow (0 2px 8px rgba(0,0,0,0.08))
- #5a31f4 appears in extraction and may be Shop Pay branding rather than a Looney Labs token; excluded from palette pending confirmation
