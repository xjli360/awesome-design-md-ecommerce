---
version: alpha
name: "Quip"
source_url: "https://getquip.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-teal canvas (#054040) and a luminous mint accent (#50fcce) define Quip's visual identity — a brand that treats oral care as a wellness ritual rather than a clinical chore. The dark, almost-black ink (#1a1a1a) sits on soft off-white surfaces (#fafafa, #f6f6f6) with generous breathing room, creating a calm, spa-like atmosphere that contrasts sharply with the bright, saturated CTA buttons and interactive elements. The brand's signature move is the mint-green (#50fcce) glow — it appears as the meta theme-color, as primary button fills, as hover states, and as the pulsing light on the electric toothbrush handle itself. Typography runs Inter at modest weights (400–600) with Poppins reserved for display moments, both set in clean, readable sizes that never compete with the product photography. Product cards float on white surfaces with soft shadows and {rounded.md} corners, while the subscription flow uses a persistent progress bar and pill-shaped buttons ({rounded.full}) that echo the ergonomic curves of the brush handles. The checkout experience is deliberately frictionless — a single-page subscription builder with toggle switches, radio-button tiers, and a mint-green "Get started" CTA that anchors every conversion point. There is no visual noise: no carousels, no pop-ups, no competing accent colors. The brand trusts its dark-teal/mint binary and the physical product photography — clean hero shots of the aluminum-handle brush against white or teal backdrops — to carry the emotional weight.

colors:
  primary: "#50fcce"
  primary-active: "#3ce0b0"
  primary-disabled: "#aaddaa"
  ink: "#1a1a1a"
  body: "#595959"
  muted: "#7b7e7e"
  muted-soft: "#b3d4fc"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  canvas: "#fafafa"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#054040"
  brand-teal: "#054040"
  brand-dark: "#141414"
  brand-charcoal: "#222222"
  brand-sage: "#9cddc0"
  brand-light-gray: "#f1f1f1"
  brand-medium-gray: "#686969"
  brand-border: "#e2e2e2"
  brand-soft-white: "#f2f2f2"
  brand-error: "#e0e0e0"

typography:
  display-xl:
    fontFamily: "'Poppins', Inter, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', Inter, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', Inter, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-lg:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.brand-teal}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
    height: 48px
  button-pill-mint:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-pill-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.brand-error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(5,64,64,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  hero-section:
    backgroundColor: "{colors.brand-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-alt:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.brand-teal}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-subscription:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.brand-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  subscription-tier-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  subscription-tier-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "2px solid {colors.primary}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    fillColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    activeColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
  radio-button:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    activeColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: 20px

## Components

### Buttons
**`button-primary`** — The brand's primary CTA, rendered as a mint-green (#50fcce) pill with dark-teal (#054040) text. Used for "Get started", "Subscribe", and "Add to cart" actions. On hover, the fill shifts to `{colors.primary-active}` (#3ce0b0). The disabled state uses a softer sage (`{colors.primary-disabled}`) with reduced opacity. The pill shape (`{rounded.full}`) echoes the ergonomic curves of Quip's brush handles.

**`button-secondary`** — An outlined pill with a white fill and dark ink text, bordered by `{colors.hairline}`. Used for "Learn more" and "Compare plans" actions. On hover, the border thickens to 2px solid `{colors.ink}`. The active state fills with `{colors.surface-soft}`.

**`button-tertiary`** — A text-only button with no background or border, used for "Skip" or "Cancel" actions in the subscription flow. Inherits `{typography.button-md}` weight for visual parity with primary buttons.

**`button-pill-mint`** — A compact, 36px-tall mint pill used for inline actions like "Shop now" on product cards or "Refill" in the subscription dashboard. Same color logic as `button-primary` but at `{typography.button-sm}` size.

**`button-pill-ghost`** — A compact outlined pill with a thin 1px border, used for secondary inline actions like "View details" or "Compare".

### Cards
**`product-card`** — A white card with a soft border and `{rounded.md}` corners. Contains a square product image (`{rounded.sm}`), the product name in `{typography.title-md}`, a price line in `{typography.body-md}`, and a `button-pill-mint` CTA. On hover, the card gains a mint border and a subtle teal-tinted shadow (`boxShadow: 0 4px 12px rgba(5,64,64,0.08)`).

**`subscription-tier-card`** — A larger card used in the subscription builder, with `{spacing.lg}` padding. Contains a tier name, price, feature list, and a radio button. The active state swaps the border to 2px solid `{colors.primary}`.

### Navigation
**`nav-bar`** — A fixed 72px-tall white bar with a thin bottom border. Contains the Quip logo (left), nav links (center: "Shop", "Learn", "Reviews"), and utility icons (right: search, cart, account). Active nav links display a 2px mint underline.

### Forms
**`text-input`** — A standard input with a white fill, 1px hairline border, and `{rounded.sm}` corners. On focus, the border becomes 2px solid `{colors.primary}`. Error state uses a 2px `{colors.brand-error}` border.

**`toggle-switch`** — A pill-shaped toggle used for subscription add-ons (e.g., "Add whitening strips"). The inactive state is `{colors.hairline}`, active is `{colors.primary}`.

**`radio-button`** — A 20px circular radio button used in the subscription tier selector. The active state fills with `{colors.primary}`.

### Badges
**`badge-new`** — A mint pill with dark-teal text, used for new product launches. `{typography.badge}` at 11px uppercase.

**`badge-sale`** — A dark-teal pill with mint text, used for promotional pricing.

**`badge-subscription`** — A neutral gray pill used for "Subscribe & save" labels.

### Footer
**`footer-section`** — A dark-teal (#054040) footer with white body text and mint links. Contains three columns: "Products", "Learn", "Support" with `{typography.body-sm}` links. Social icons appear in mint.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to `{typography.display-md}`; subscription tiers stack; CTA buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero uses `{typography.display-lg}`; subscription tiers in 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses `{typography.display-xl}`; subscription tiers in 3-column grid |
| Wide | > 1440px | Max-width container (1440px) centered; additional whitespace on sides; hero remains centered with max-width content area |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card CTAs are at least 48px tall
- Toggle switches are 24px tall with 44px touch targets
- Radio buttons are 20px with 44px touch targets

### Collapsing Strategy
- Top nav collapses to a hamburger menu below 744px
- Product grid collapses from 3 columns → 2 columns → 1 column
- Subscription tier cards collapse from 3 columns → 2 columns → 1 column
- Footer columns collapse from 3 columns → 2 columns → 1 column
- Hero section reduces font size and padding at each breakpoint

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list includes several generic grays and blues (#b3d4fc, #e0e0e0, #f2f2f2) that may be Shopify checkout-widget or social-icon colors rather than brand colors — the true brand palette is likely tighter (teal, mint, white, and 2-3 grays)
- Hover and focus states for most components were inferred from common patterns, not extracted from the live site
- Error state styling (validation messages, error icons) could not be reliably extracted
- Dark mode is not present on the live site and is not defined
- Sub-brand or seasonal color palettes (holiday, Pride, etc.) are not captured
- The exact font sizes for `display-xl`, `display-lg`, and `display-md` are estimated based on common patterns — the live site may use different values
- Animation durations and easing curves (button hover transitions, card hover shadows) are not extracted
- The `#b3d4fc` color appears to be a Shopify default or social-icon blue and should be verified against actual brand usage
- The `#aaddaa` color may be a disabled-state approximation or a stock-image tone — its role should be confirmed
- Product card shadow values are estimated — the live site may use different opacity or spread values
