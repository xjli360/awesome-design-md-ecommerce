---
version: alpha
name: "Power Planter"
source_url: "https://powerplanter.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  FatFrank headlines land like a shovel striking soil — blocky, geometric letterforms stacked at high weights that announce tools built for weekend warriors, not boutique garden aesthetics. The system's voltage lives in a saturated nursery green (`#008e4f`) that floods primary CTAs, product badges, and the sticky add-to-cart bar, grounding every interaction in the brand promise of getting things planted faster. A secondary green (`#158251`) appears on hover and active states, barely a half-step darker but enough to register as mechanical feedback. Against a white canvas, product photography dominates the viewport while warm cream panels (`#fff1e3`) break long scroll sections with the dusty warmth of dry potting mix. Typography is aggressively simple: FatFrank handles every heading from hero banners down to collection titles, its mono-weight geometry eliminating the need for italic or light variants; body copy falls to system sans-serif at comfortable reading sizes. Corners stay sharp — buttons use `{rounded.xs}` at most, cards sit at `{rounded.sm}`, reinforcing the industrial DNA of a brand selling steel auger bits, not artisanal ceramics. The color system leans on a dark-brown ink (`#412d00`) for certain accent text, evoking turned earth alongside the expected near-black (`#121212`) for body copy. Spacing is generous vertically (`{spacing.section}` between feature blocks) but tighter horizontally on mobile, where product grids collapse to single-column with full-bleed imagery. A persistent blue (`#1199ff`) surfaces only for utility links and trust signals, kept far from the green-dominated conversion path.

colors:
  primary: "#008e4f"
  primary-active: "#158251"
  primary-disabled: "#80c7a7"
  ink: "#121212"
  body: "#412d00"
  muted: "#9e9e9e"
  muted-soft: "#bdbdbd"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-warm: "#fff1e3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#1199ff"
  earth-accent: "#412d00"

typography:
  display-xl:
    fontFamily: "'fatfrank', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'fatfrank', sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'fatfrank', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
  display-sm:
    fontFamily: "'fatfrank', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'fatfrank', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'fatfrank', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'fatfrank', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'fatfrank', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'fatfrank', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'fatfrank', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  price:
    fontFamily: "'fatfrank', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
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
  hero: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 52px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary-active}
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 2px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: 0 2px 8px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    boxShadow: 0 1px 4px rgba(0,0,0,0.06)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: 1 / 1
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.hero} {spacing.xl}"
    minHeight: 520px
  hero-banner-warm:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.hero} {spacing.xl}"
    minHeight: 520px
  feature-block:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge-bestseller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.earth-accent}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sticky-atc-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 72px
    boxShadow: 0 -2px 12px rgba(0,0,0,0.1)
    padding: "{spacing.md} {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  collection-header:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  trust-badge-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: "{spacing.base} {spacing.lg}"
    gap: "{spacing.xl}"
  size-selector-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    border: 1px solid {colors.hairline}
  size-selector-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px

---

## Components

### Buttons

**`button-primary`** — Full-green CTA with white uppercase FatFrank text, used for add-to-cart, hero actions, and checkout progression. Hover darkens to `{colors.primary-active}`, active state depresses with a 1px downward translate. Disabled state washes out to a pale mint (`{colors.primary-disabled}`) with no pointer events. Minimum width of 180px on desktop to prevent stubby buttons on short labels like "Shop" or "Buy."

**`button-secondary`** — White fill with a 2px green border and green text, reserved for secondary actions like "View All" on collection grids or "Learn More" links that need button-level prominence. Hover fills the background with `{colors.surface-soft}` while the border deepens to `{colors.primary-active}`. Never stacked directly below a primary button — always placed inline or in a separate row.

### Navigation

**`nav-bar`** — Fixed-top navigation at 72px height with the Power Planter wordmark (set in FatFrank) on the left, category links centered, and cart icon right-aligned. On scroll, height compresses to 64px (`nav-bar-scrolled`) and a subtle box-shadow appears. Background remains solid white to preserve contrast against green hero sections below. Mobile collapses to hamburger with a full-screen green overlay menu.

### Product Cards

**`product-card`** — Square product image on a light-gray background (`{colors.surface-soft}`), followed by the product title in `{typography.title-sm}`, price in `{typography.price}`, and a compact "Add to Cart" button. Cards use `{rounded.sm}` corners and a barely-there shadow to lift off white backgrounds. On hover, the image scales 1.03× with a 200ms ease and the shadow deepens slightly.

**`product-card-image`** — 1:1 aspect ratio container with the soft gray fill showing behind transparent-background product shots. The auger bit products are typically photographed at a 15° angle to show spiral depth.

### Hero

**`hero-banner`** — Full-width green block with centered white display text (`{typography.display-xl}`), a subheadline in `{typography.body-md}`, and a white secondary button. Used on the homepage to push seasonal campaigns or new product launches. Minimum height 520px ensures impact on all viewport sizes. May include a background product image at 20% opacity for texture.

**`hero-banner-warm`** — Alternate hero using the cream surface (`{colors.surface-warm}`) with dark text, typically for educational content like "How to Choose Your Auger Size" or installation guides. Same layout structure as the green hero but with a primary-green CTA button instead of the white secondary.

### Feature Blocks

**`feature-block`** — Cream-background panels (`{colors.surface-warm}`) used to break up white product grid sections. Contains a left-aligned image (60% width) and right-aligned copy stack with a `{typography.display-sm}` heading, `{typography.body-md}` paragraph, and optional CTA. Rounded to `{rounded.sm}` and padded generously at `{spacing.xxl}`.

### Badges

**`badge-bestseller`** — Small green pill overlaid on product card images, top-left corner with 8px offset from edges. White uppercase text at 11px. Used sparingly — maximum 3 per collection grid to maintain signal value.

**`badge-sale`** — Dark brown (`{colors.earth-accent}`) background with white text, same sizing as bestseller badge. Positioned top-right to avoid collision with the bestseller badge when both apply.

### Sticky Add-to-Cart Bar

**`sticky-atc-bar`** — Appears on product pages once the main add-to-cart button scrolls out of the viewport. Fixed to bottom of screen with a white background and upward shadow. Contains condensed product name, price, and a full-width primary button. Height locked at 72px with `{spacing.md}` vertical padding.

### Footer

**`footer`** — Near-black background (`{colors.ink}`) with light gray link text organized in 4 columns: Shop, Support, Company, Connect. The Power Planter logo renders in white at the top, followed by a brief tagline. Social icons sit in a row below the columns. Bottom bar contains copyright and payment icons against a slightly darker strip.

### Trust Badge Row

**`trust-badge-row`** — Horizontal strip of 3-5 trust signals (free shipping threshold, warranty, made-in-USA) on a light gray background. Each badge is an icon + caption pair. Sits between the hero and the first product grid on the homepage, full-width with generous horizontal gaps (`{spacing.xl}`).

### Size Selector

**`size-selector-chip`** — Rectangular chips with hairline borders for selecting auger diameter on product pages. Active state fills solid green with white text. Chips are arranged in a horizontal wrap layout with `{spacing.sm}` gap. Each chip displays the diameter measurement (e.g., "2 inch", "4 inch") in uppercase FatFrank at button-sm scale.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text drops to `{typography.display-md}`; nav collapses to hamburger + full-screen overlay; sticky ATC bar always visible on product pages; feature blocks stack image above copy at 100% width |
| Tablet | 744–1128px | Two-column product grid; hero text at `{typography.display-lg}`; nav links visible but condensed spacing; feature blocks maintain side-by-side at 50/50 split |
| Desktop | 1128–1440px | Three-column product grid; full nav with all category links; hero at full `{typography.display-xl}`; feature blocks at 60/40 image-to-copy ratio |
| Wide | > 1440px | Content max-width caps at 1440px and centers; four-column grid for large collections; increased section spacing to `{spacing.hero}` between major blocks |

### Touch Targets

- All interactive elements maintain minimum 44×44px touch area on mobile
- Size selector chips expand to full-width rows on viewports below 400px
- Cart icon in nav has 48px tap target despite 24px visual icon size
- Sticky ATC button spans full viewport width minus `{spacing.base}` gutters

### Collapsing Strategy

- Navigation links collapse into a hamburger menu below 744px with a slide-down green panel
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Feature block image/copy pairs stack vertically below 744px
- Trust badge row wraps to 2 rows on mobile, centered with reduced gap (`{spacing.md}`)
- Footer columns collapse from 4 across to 2×2 grid on tablet, then full-stack on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one font family (`fatfrank`) was detected; the body/system font stack is inferred from standard Shopify defaults — actual body font may differ if loaded via JavaScript or app blocks
- No meta theme-color was set, so mobile browser chrome color is unconfirmed
- Exact button border-radius could not be confirmed from extraction (assumed sharp/4px based on brand's industrial aesthetic)
- Hover transition durations and easing functions are estimated; actual CSS transitions were not captured
- Email signup / popup modal styling not captured
- Announcement bar (common on Shopify stores) styling not available in extraction
- Exact sticky-bar trigger scroll offset and animation not determined
- Product page gallery/carousel interaction patterns not captured
