---
version: alpha
name: "Aniplex+ USA"
source_url: "https://p-bandai.com/us/search?sort=relevance&text=aniplex"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A collector-grade marketplace where premium anime merchandise meets a restrained, product-forward interface. The site operates on a clean white canvas (#ffffff) with a single brand voltage — a deep, saturated crimson (#c8102e) that appears exclusively on the primary "Pre-Order" and "Add to Cart" buttons, signaling urgency without competing with the vibrant product photography. Typography runs a utilitarian sans-serif stack — likely Noto Sans JP or a system fallback — at modest weights (400–600), never exceeding 24px for display text, trusting the elaborate figure boxes and character art to carry visual weight. The navigation is a dense, two-tier system: a persistent top bar with account, cart, and search icons, and a secondary mega-menu strip of franchise categories (Demon Slayer, Fate, Gundam, etc.) that collapses into a hamburger on mobile. Product cards use a soft 8px corner radius (`{rounded.sm}`) and generous 16px padding, with price tags set in bold 16px type against the white card surface. The search bar is a full-width pill (`{rounded.full}`) with a magnifying-glass icon, sitting below the hero banner rather than in the nav, suggesting discovery is secondary to browsing known franchises. Badges — "Pre-Order", "Sold Out", "Limited Edition" — are compact 20px-tall pills in crimson or muted gray, using 11px uppercase type. The overall mood is efficient and slightly austere: no decorative flourishes, no brand illustrations, just a clean grid of product thumbnails and the crimson button as the only emotional cue.

colors:
  primary: "#c8102e"
  primary-active: "#a00d24"
  primary-disabled: "#f5c6cb"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-sold-out: "#999999"
  badge-preorder: "#c8102e"
  badge-limited: "#ff8c00"
  star-rating: "#f5a623"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-md:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  title-sm:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  price-lg:
    fontFamily: "Noto Sans JP, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
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
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
  secondary-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 44px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-price:
    typography: "{typography.price-lg}"
    textColor: "{colors.ink}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    lineClamp: 2
  badge:
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
    height: 20px
  badge-preorder:
    backgroundColor: "{colors.badge-preorder}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
    height: 20px
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
    height: 20px
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
    height: 20px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    height: 320px
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"

## Components

### Buttons
**`button-primary`** — The single call-to-action across the site, rendered in deep crimson (#c8102e) with white text. Used exclusively for "Pre-Order", "Add to Cart", and "Checkout" actions. On hover, darkens to `{colors.primary-active}` (#a00d24). When disabled, fades to a pale pink `{colors.primary-disabled}` (#f5c6cb) with white text, signaling unavailability. Height is 44px with 12px vertical padding and 24px horizontal, giving a compact but tappable footprint.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Cancel". Uses a white background with a 1px `{colors.hairline}` border and `{colors.ink}` text. On hover, the border thickens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`. Height matches the primary button at 44px for alignment in forms.

**`button-pill`** — A smaller, fully rounded variant (36px tall) used for filter tags, category chips, and "Apply" actions in search. Uses the same crimson fill as primary but with 14px type and 8px vertical padding. The pill shape (`{rounded.full}`) makes it feel like a removable tag.

### Cards
**`product-card`** — The core content unit: a white card with a 1px soft hairline border, 8px corner radius, and 16px padding. Each card contains a square product image (1:1 aspect ratio, 4px corner radius), a two-line title in 14px medium weight, and a price in 20px bold. On hover, the border darkens to `{colors.hairline}` and a subtle 2px shadow lifts the card. No gradient overlays or decorative elements — the product photography does all the work.

### Navigation
**`top-nav`** — A 56px fixed bar with the brand logo on the left, and account, cart, and search icons on the right. The background is white with a 1px soft hairline bottom border. Cart icon shows a badge count in `{colors.primary}`. The search icon toggles the full-width search bar below.

**`secondary-nav`** — A 44px strip below the top nav containing franchise category links (Demon Slayer, Fate, Gundam, Sword Art Online, etc.). Active category has a 2px crimson bottom border. On mobile, this collapses into a horizontal scrollable strip or a hamburger menu.

### Forms
**`search-bar`** — A full-width pill input with a magnifying-glass icon on the left. Background is `{colors.surface-soft}` with a 1px `{colors.hairline}` border. On focus, the border switches to `{colors.primary}` and the background turns white. Height is 40px with 10px vertical padding. Placeholder text uses `{colors.muted-soft}`.

### Badges
**`badge-preorder`** — A compact 20px-tall pill in crimson with white uppercase 11px type. Used on product cards to indicate upcoming releases. Positioned at the top-left corner of the product image with a small offset.

**`badge-sold-out`** — Same dimensions but in gray (`{colors.badge-sold-out}`). Indicates items that are no longer available. The product card remains visible but the CTA is disabled.

**`badge-limited`** — An orange variant (`{colors.badge-limited}`) for limited-edition items. Often paired with a countdown timer or "Only X left" text below the price.

### Footer
**`footer`** — A dark section (`{colors.ink}` background) with white text. Contains links to Help, About, Privacy Policy, and Terms of Service in `{colors.muted-soft}` that lighten to white on hover. Social media icons (Twitter, Instagram, YouTube) are included as 24px icons. The footer uses 48px vertical padding and 64px section padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; secondary nav collapses to hamburger; product cards stack vertically; search bar moves below hero; footer links stack |
| Tablet | 744–1128px | 2-column product grid; secondary nav scrolls horizontally; search bar remains full-width but shorter; footer in 2 columns |
| Desktop | 1128–1440px | 3-4 column product grid; full secondary nav visible; search bar in top nav area; footer in 4 columns |
| Wide | > 1440px | Max-width container at 1440px; 4-5 column grid; search bar expands to 600px max |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (WCAG 2.1 compliant)
- Icon buttons in top nav are 40x40px with 48px touch area via padding
- Product card tap targets (image, title, price) are at least 48px tall
- Badges are 20px tall but sit on 44px product card padding for tap safety

### Collapsing Strategy
- Secondary navigation collapses to a horizontal scroll strip on tablet, then to a hamburger menu on mobile
- Product grid reduces from 4 columns (desktop) to 2 (tablet) to 1 (mobile)
- Search bar moves from the top nav area on desktop to below the hero banner on mobile
- Footer links collapse from 4 columns to 2 to a single stacked column
- Cart icon badge count is hidden on mobile; cart icon remains visible

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations could be extracted from the live site; Noto Sans JP is an educated guess based on the brand's Japanese origin and typical anime e-commerce patterns. The actual font may differ.
- Only one distinctive color (crimson #c8102e) was identified as the brand primary; the extracted color list was sparse and contained mostly generic web defaults (blues, grays). The crimson was chosen as the most distinctive accent.
- Hover and active states for buttons and links are inferred from common e-commerce patterns, not extracted from the live site.
- Error states (form validation, 404 pages, empty cart) were not observed.
- Dark mode is not supported; the site uses a white canvas exclusively.
- Sub-brand palettes for individual franchises (Demon Slayer, Fate, etc.) are not captured; they may use their own accent colors within product cards.
- Loading states (skeleton screens, spinners) were not documented.
- The hero banner height (320px) is an estimate based on typical layout; actual height may vary.
- No animation or transition durations were extracted; a default 200ms ease-in-out is assumed.
