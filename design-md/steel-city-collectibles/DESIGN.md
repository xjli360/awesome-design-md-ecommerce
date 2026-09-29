---
version: alpha
name: "Steel City Collectibles"
source_url: "https://www.steelcitycollectibles.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Steel City Collectibles runs on the collector's dopamine loop — sealed wax, live breaks, and graded slabs organized around a dark charcoal canvas that lets product photography carry the visual voltage. The single confirmed extraction is #313131, a near-black charcoal that anchors surfaces, nav bars, and card backgrounds; the palette leans into this darkness rather than fighting it, giving holographic foil cards and full-bleed jersey patch images maximum contrast. Pittsburgh's sports identity sits underneath everything: the Steelers' internationally recognized gold (#ffb612) emerges as the natural accent on CTAs and price callouts, a hue so closely tied to this city that it doubles as both brand signal and cultural context. System fonts handle all typography — the stack is purely -apple-system, Roboto, Segoe UI — a pragmatic choice for a high-SKU catalogue where tens of thousands of card listings load faster without custom webfont overhead. The type hierarchy relies on weight and size contrast rather than font-family switching: heavy 700-weight headings at 28–32px drop into compact 13–14px caption lines on product cards without friction. Buttons and form inputs use {rounded.sm} at 8px, keeping the UI structured and reliable — a collector wants to trust the checkout experience, not be wowed by it. Product cards carry a subtle elevation shadow on the surface-card layer, with condition-grade badges (PSA 10, BGS 9.5) rendered in capsule chips against the card surface. Live break timers and "HOT" availability badges borrow the gold accent to signal urgency without red alarm-palette choices that would clash with the steel-dark identity. The overall register is industrial-premium: serious about the hobby, efficient in information architecture, and respectful of the collector who arrives knowing exactly what they want.

colors:
  primary: "#ffb612"
  primary-active: "#e6a310"
  primary-disabled: "#ffd98a"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#7a7a7a"
  hairline: "#3e3e3e"
  hairline-light: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-dark: "#1c1c1c"
  surface-medium: "#313131"
  on-primary: "#1a1a1a"
  on-dark: "#ffffff"
  grade-gem: "#00c853"
  grade-nm: "#2979ff"
  badge-hot: "#ffb612"
  badge-sale: "#e53935"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  break-timer:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 1px

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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-light}"
    padding: 11px 23px
    height: 44px
  button-secondary-dark:
    backgroundColor: "{colors.surface-medium}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-light}"
    padding: 10px 14px
    height: 42px
    focusBorder: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "2px solid {colors.primary}"
  nav-bar-top:
    backgroundColor: "{colors.surface-medium}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    shadow: "0 2px 8px rgba(0,0,0,0.10)"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline-light}"
  product-card-image:
    aspectRatio: "3/4"
    objectFit: cover
    rounded: "{rounded.xs}"
    backgroundColor: "{colors.surface-soft}"
  grade-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
    variants:
      gem-mt: {backgroundColor: "{colors.grade-gem}", textColor: "{colors.on-dark}"}
      nm-mt: {backgroundColor: "{colors.grade-nm}", textColor: "{colors.on-dark}"}
      hot: {backgroundColor: "{colors.badge-hot}", textColor: "{colors.on-primary}"}
  sale-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 400px
    padding: "{spacing.xxl} {spacing.lg}"
    accentColor: "{colors.primary}"
  break-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: "{spacing.base}"
  break-timer-display:
    typography: "{typography.break-timer}"
    textColor: "{colors.primary}"
    backgroundColor: "{colors.surface-dark}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline-light}"
    padding: "10px 20px"
    height: 44px
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline-light}"
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  price-tag:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  price-tag-sale:
    typography: "{typography.price-display}"
    textColor: "{colors.badge-sale}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline-light}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted}"
    accentColor: "{colors.primary}"
    padding: "{spacing.xxl} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — Gold (#ffb612) fill on a 44px-tall target with {rounded.sm} radius and heavy 700-weight label at 15px. The gold-on-dark pairing is the brand's highest-urgency action: Add to Cart, Buy Now, Join Break. Active state deepens to #e6a310 without animation delay; the collector market expects speed. Disabled state washes the gold to #ffd98a at 0.6 opacity.

**`button-secondary`** — White fill with a 1px light hairline border, mirroring button-primary in height and radius. Used for secondary actions like "Add to Wishlist" or "View Details" on light-canvas pages. The dark variant (`button-secondary-dark`) swaps in the #313131 surface and white text for use inside hero panels and break cards.

**`button-ghost`** — Transparent background with primary gold text, no border. Used for inline text-level actions — "View All," "See More Breaks," pagination — where a bordered button would overweight the layout.

### Navigation
**`nav-bar`** — Dark #1c1c1c background with a 2px gold bottom border that functions as the brand's most persistent identity mark across all pages. Links are 14px/600-weight in white. A slimmer 36px utility bar (`nav-bar-top`) at #313131 above it carries shipping threshold messaging, account, and cart links at 13px caption weight.

### Product Cards
**`product-card`** — White surface with 1px light hairline border and a soft box shadow (0 2px 8px rgba(0,0,0,0.10)) on {rounded.sm} radius. The card image fills a 3:4 portrait aspect ratio — dimensioned for trading cards — with a surface-soft grey placeholder. Grade badges float top-left on the image; sale and hot badges float top-right. Price sits below the title in price-display (20px/700). Compact {spacing.md} padding allows dense grid layouts without crowding.

### Grade Badges
**`grade-badge`** — Capsule chips in badge typography (11px uppercase 700). Three variants: gem-mt (green #00c853) for PSA 10 / BGS 9.5 pinnacle grades; nm-mt (blue #2979ff) for mid-tier grades; hot (gold #ffb612) for trending or freshly listed cards. These are the highest-information elements on a product card and must remain legible at small sizes on both light and dark surfaces.

### Hero Banner
**`hero-banner`** — Full-width dark panel (#1c1c1c) with left-aligned headline in display-xl (32px/700) and gold (#ffb612) accents on highlight words or CTA underlines. Minimum 400px height with {spacing.xxl} vertical padding. Intended for seasonal promotions, new product drops, and break event announcements where large photography bleeds edge-to-edge behind the text layer.

### Live Break Cards
**`break-card`** — Dark surface panel with a 2px gold outline, immediately differentiating break listings from standard product cards. Contains sport/team thumbnails, break format in body-sm, slot count, and a `break-timer-display` countdown block. The gold border is the single strongest urgency signal in the UI — reserved exclusively for time-bounded live events.

**`break-timer-display`** — Fixed-pitch 22px/700 numerals in primary gold (#ffb612) against the dark surface, with 1px letter-spacing to maintain digit alignment during countdown. Padded at {spacing.sm} × {spacing.md} inside a dark xs-rounded container. Never use for static informational content — countdown only.

### Search
**`search-bar`** — Full-width pill ({rounded.full}) with 1px light hairline border at 44px height. The pill silhouette distinguishes it from standard text inputs and card borders. On dark nav bars the white fill provides the contrast cue that invites entry. Autocomplete dropdown surfaces below with surface-card fill and hairline border, listing card names, sets, and player names.

### Category Pills
**`category-pill`** — Horizontal scrolling chips in caption-bold on surface-soft ground with light hairline border. Used below the search bar to scope by sport (Baseball, Football, Basketball, Hockey) or format (Singles, Sealed, Graded, Rookies). Active state flips to primary gold fill with on-primary dark text. On mobile the pill row scrolls horizontally without wrapping.

### Price Tags
**`price-tag`** — price-display typography (20px/700) in ink, sitting directly below the product title. `price-tag-sale` swaps textColor to badge-sale red (#e53935) to signal markdown. Original prices on sale cards render in muted at 14px with strikethrough.

### Trust Badges
**`trust-badge`** — Light surface-soft chip with light hairline border at {spacing.sm} × {spacing.base} padding. Carries icons for "Secure Checkout," "Authenticity Guaranteed," and "Ships Same Day." Displayed in a horizontal row beneath the add-to-cart button on product detail pages — essential in a category where condition misrepresentation is a known buyer concern.

### Footer
**`footer`** — Dark #1c1c1c panel matching the nav, gold logo lockup top-left. Links in muted grey (#7a7a7a) at body-sm, upgrading to on-dark white on hover. Section headings in caption-bold uppercase. Payment method icons and security seals sit in a hairline-bordered bottom strip at caption size.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + search icon; category pills scroll horizontally; break cards stack full-width; hero min-height drops to 260px; trust badges stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav shows primary sport categories inline; break cards in 2-column grid; hero at 340px |
| Desktop | 1128–1440px | Three–four column product grid; full horizontal nav with category dropdowns; break cards in 3-column grid; hero at full 400px |
| Wide | > 1440px | Max-width container (~1400px) centered; five-column product grid option; hero expands with wider image bleed |

### Touch Targets
- All primary and secondary buttons minimum 44px height
- Category pills minimum 36px height on mobile
- Product card tap target extends to full card surface, not image only
- Break join-CTA minimum 48px height on mobile
- Nav hamburger icon minimum 44×44px hit area

### Collapsing Strategy
- Primary nav collapses to full-screen drawer at < 744px; mega-menu categories become accordion sections
- Utility top bar hides on mobile; shipping threshold surfaces as a banner inside the drawer
- Grade badge text drops from 11px to 10px on mobile cards but badge remains visible
- Product card title truncates to 2 lines on mobile with ellipsis
- Footer columns collapse to single-column accordion on mobile; payment icon strip remains horizontal

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site was behind Cloudflare anti-bot protection ("Just a moment…") at extraction time — only one hex color (#313131) was captured; the full palette is inferred rather than observed
- Gold accent (#ffb612) is inferred from Pittsburgh Steelers brand association and collector-market conventions, not confirmed from CSS extraction — verify against live assets before shipping
- No custom brand fonts detected; typography is built entirely on the system stack, but a custom display face for the wordmark or hero headings may exist as an image asset rather than a webfont
- No confirmed border-radius values; {rounded.sm} (8px) is an educated default for this market segment
- Navigation depth, mega-menu structure, and break-calendar layout are inferred from category-type conventions, not directly observed
- Dark-mode or theme toggle presence unknown
- Actual mobile breakpoints should be confirmed via DevTools — values above are estimated
