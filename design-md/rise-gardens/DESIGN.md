---
version: alpha
name: "Rise Gardens"
source_url: "https://risegardens.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The first signal that Rise Gardens means business is chromatic — #50de7f, an electric chlorophyll green that falls somewhere between neon and botanical, saturates every primary call-to-action against a field of white. The color is not aspirational; it is literal. The brand sells living plants growing under LED arrays in modular indoor tower systems, and the green that headlines every buy button is the same hue you would see emerging from a pod tray seventy-two hours after planting. Notably, the on-primary text runs dark (#121212) rather than white, preserving legibility across the full saturation range without washing out the primary voltage. The palette tells a four-chapter story: the electric primary for growth and action; a deep forest anchor (#008968) for hover states and secondary moments that need permanence; a harvest gold (#fec535) for promotions and seasonal callouts that carry warmth without alarm; and a cool teal (#00aba9) that surfaces in tertiary UI, consistent with browser-config assets and a secondary digital presence layer. The gray family is minimal — #dedede serves hairlines and form borders, and near-black (#121212) handles all body text with no intermediate display gray. Typography was not extractable from the live site, consistent with a Shopify theme loading font tokens via JavaScript; the scales here use a clean geometric system sans-serif as proxy, matching the restrained, utilitarian weight the page reads at — display headlines are compact rather than editorial, and buttons use weight 600 at modest letter-spacing. The rounding language leans friendly without tipping into playful: `{rounded.md}` at 12px governs product cards and inputs, while `{rounded.full}` handles grow-stage badges and the progress rings of plant-tracker UI — the organic loop of a seedling indicator. Section spacing breathes generously at `{spacing.section}` 64px, letting hero photography of lush herbs and lettuces carry the persuasion load. A subtle green-tinted surface token (`{colors.surface-soft}`) warms subscription callout panels, keeping the secondary layout layer from reading as neutral gray. Rise Gardens runs on Shopify with a product catalog structured around the garden-as-subscription model, so the component library prioritizes grow-kit cards, plant-stage progress trackers, and recurring-order callouts alongside standard e-commerce anatomy.

colors:
  primary: "#50de7f"
  primary-active: "#008968"
  primary-disabled: "#aaefc8"
  accent-harvest: "#fec535"
  accent-teal: "#00aba9"
  accent-sky: "#5bbad5"
  ink: "#121212"
  body: "#333333"
  muted: "#717171"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f2fbf5"
  surface-card: "#ffffff"
  surface-tint: "#e8f8ef"
  on-primary: "#121212"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  price:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 52px

  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    height: 52px

  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    height: 52px

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.ink}"
    padding: 12px 26px
    height: 52px

  button-secondary-active:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.md}"
    height: 52px

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    textDecoration: underline

  button-harvest:
    backgroundColor: "{colors.accent-harvest}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 52px

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary-active}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"

  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 12px rgba(0,0,0,0.08)"
    height: 64px

  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    overflow: hidden
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    textColor: "{colors.ink}"
    imagePadding: 0
    bodyPadding: 16px

  hero:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    minHeight: 560px
    contentMaxWidth: 560px
    layout: split-50-50

  grow-stage-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px

  harvest-badge:
    backgroundColor: "{colors.accent-harvest}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px

  new-badge:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px

  grow-kit-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.hairline}"
    accentBarColor: "{colors.primary}"
    accentBarWidth: 4px
    titleTypography: "{typography.title-lg}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    padding: 24px

  plant-progress-tracker:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    milestoneActiveColor: "{colors.primary-active}"
    milestoneInactiveColor: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    trackHeight: 6px
    milestoneSize: 12px
    rounded: "{rounded.full}"

  subscription-callout:
    backgroundColor: "{colors.surface-soft}"
    borderLeft: "4px solid {colors.primary}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 20px 24px

  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    textColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    captionTypography: "{typography.caption}"
    accentColor: "{colors.primary}"
    padding: 24px 28px

  category-chip:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px

  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "none"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary}"
    mutedColor: "{colors.muted}"
    headlineTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    padding: "48px 0 32px"

## Components

### Buttons

**`button-primary`** — The electric #50de7f green button with dark ink text (`{colors.on-primary}`) is Rise Gardens' main conversion surface, appearing on add-to-cart, shop-now, and subscription CTAs. At 52px tall with `{rounded.md}` corners, it reads as modern and friendly without the full pill softness. Active state drops to `{colors.primary-active}` (#008968) with white text, darkening the signal; disabled state washes to `{colors.primary-disabled}` with muted text.

**`button-secondary`** — A bordered outline button on white canvas, pairing with the primary in two-CTA hero layouts (e.g., "Shop Gardens" + "Learn More"). The 2px ink border matches `{colors.ink}` and flips on hover to `{colors.surface-tint}` background with `{colors.primary-active}` border and text.

**`button-harvest`** — A warm accent button using `{colors.accent-harvest}` (#fec535) with dark text, reserved for seasonal promotions, limited drops, and sale callouts. Same geometry as button-primary, swapped fill. Avoids the primary-green signal so users don't confuse promotional actions with standard purchase flow.

**`button-ghost`** — Text-only, underlined, in `{colors.primary-active}`, for in-context secondary links like "View growing guide" and "Compare systems" beneath product descriptions. No padding or background.

### Inputs

**`text-input`** — Standard 48px input with `{rounded.sm}` and a `{colors.hairline}` resting border that sharpens to `{colors.primary-active}` on focus, creating a green focus ring that echoes the primary brand voltage without using the full-saturation primary green.

### Navigation

**`nav-bar`** — White canvas with a 1px `{colors.hairline}` bottom border at 72px tall. On scroll, `nav-bar-scrolled` drops the border and introduces a soft box-shadow for visual lift. Navigation links use `{typography.nav-link}` at weight 500; the cart icon and primary CTA (likely "Shop Now") sit in the right rail.

### Product Cards

**`product-card`** — White card with a 1px hairline border and `{rounded.md}` corners, image bleeding edge-to-edge at top. Title in `{typography.title-sm}`, price in `{typography.price-sm}`. On hover, a subtle shadow lift surfaces; the quick-add CTA appears inline. Badges (`grow-stage-badge`, `new-badge`) stack absolute over the image top-left.

### Brand-Signature Components

**`hero`** — Split 50/50 layout at desktop: left column holds headline in `{typography.display-xl}`, 1-2 sentences of body copy in `{typography.body-md}`, and a `button-primary` CTA; right column holds a full-bleed product or lifestyle photograph. Background is plain white canvas — the photography and primary green CTA carry all the energy.

**`grow-stage-badge`** — Pill-shaped in `{colors.primary}` with dark text and uppercase `{typography.badge}` tracking, applied to product cards and grow-kit listing pages to indicate plant stage (Seedling / Growing / Harvest-Ready). `{rounded.full}` shape signals an ongoing biological cycle rather than a static label.

**`harvest-badge`** — Same geometry as `grow-stage-badge` but in `{colors.accent-harvest}` (#fec535), used for "Ready to Harvest" states, seasonal collection callouts, and promotional banners. The gold reads as warmth and reward rather than urgency.

**`grow-kit-card`** — A larger featured card (used in collection pages and how-it-works sections) with a 4px left accent bar in `{colors.primary}`, title in `{typography.title-lg}`, and supporting body copy in `{typography.body-sm}`. `{rounded.lg}` corners give it more visual weight than a standard product card, signaling it is a configurable system rather than a single-SKU item.

**`plant-progress-tracker`** — A horizontal step-progress component with a 6px fill track in `{colors.primary}`, circular milestones in `{colors.primary-active}` when passed and `{colors.hairline}` when pending, and `{typography.caption}` labels beneath each milestone (e.g., "Day 1 / Week 2 / Harvest"). Used on order detail pages and educational grow guides. All track segments use `{rounded.full}`.

**`subscription-callout`** — An informational panel in `{colors.surface-soft}` with a 4px left border in `{colors.primary}` and `{rounded.sm}` corners, used to surface subscription savings, auto-refill seed pod benefits, and referral rewards inline with product descriptions. Headline in `{typography.title-md}`, body in `{typography.body-sm}`.

**`category-chip`** / **`category-chip-active`** — Pill-shaped filter chips used in the grow category and seed-pod filters. Resting state: `{colors.surface-tint}` background, `{colors.primary}` border, `{colors.primary-active}` text. Active state: solid `{colors.primary}` fill, `{colors.on-primary}` ink text. `{rounded.full}` shape.

**`testimonial-card`** — Soft `{colors.surface-soft}` card at `{rounded.md}` with a small `{colors.primary}` accent mark (left quote glyph or decorative bar) and body copy in `{typography.body-md}`. Reviewer name and grow-kit model run in `{typography.caption}`. Used in homepage social proof rows.

**`footer`** — Dark `{colors.ink}` background with `{colors.on-dark}` body text, `{colors.primary}` links (creating a strong green-on-dark signal), and `{colors.muted}` for legal/secondary copy. Column heads in `{typography.title-sm}`. Social icons and app store badges sit in the bottom rail above the legal strip.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hero stacks vertically, image above text; nav collapses to hamburger; product grid goes 1-column or 2-column; grow-kit-card spans full width; category chips scroll horizontally |
| Tablet | 744–1128px | Hero maintains split but shifts to 45/55 text-heavy; product grid 2-column; nav retains top bar with icon-only right rail; testimonials show 2-up |
| Desktop | 1128–1440px | Hero 50/50 split; product grid 3-column; nav expands with full link labels and visible CTA button; grow-kit-cards in 2-column feature layout |
| Wide | > 1440px | Content max-width clamps at ~1320px, outer margins scale symmetrically; hero image crops to center-weighted portion; product grid stays 4-column max |

### Touch Targets

- All buttons minimum 52px tall, 44px minimum tap width
- Category chips minimum 40px tall on mobile with `{spacing.xs}` gap between chips
- Nav hamburger icon 44×44px tap target
- Product card add-to-cart tap zone extends to full card width on mobile
- Progress tracker milestones minimum 28px tap area (visual size 12px, padding extended)

### Collapsing Strategy

- Navigation: hamburger at < 744px; full horizontal link list at ≥ 1128px; icon-only middle state at 744–1128px
- Hero: image drops below text on mobile, becomes decorative secondary element; CTA button goes full-width
- Product grid: 1-col (< 480px) → 2-col (480–1128px) → 3-col (1128–1440px) → 4-col (> 1440px)
- Grow-kit-card: single-column stacked at mobile; 2-up side-by-side at tablet+
- Subscription-callout: left border drops to top border on mobile for full-width panels
- Footer: single-column accordion links on mobile; 4-column grid at desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families were extractable from the live site; the Shopify theme almost certainly loads custom or licensed fonts via JavaScript after initial parse. All typography scales here use `system-ui` as a proxy. The actual brand face should be identified via browser devtools (Fonts panel) or by inspecting the Shopify theme's `settings_data.json` / `theme.liquid` for `font_picker` values.
- The extracted blue tones (#5bbad5, #00aba9) are likely sourced from browser-config/mstile meta tags (Windows tile and Safari pinned-tab configuration) rather than live UI application. Their actual on-page usage and frequency are unconfirmed; treat `accent-sky` and `accent-teal` as secondary tokens until verified against UI screenshots.
- No shadow, motion, or animation tokens were extractable. Hover elevations, transition durations, and micro-interaction curves (e.g., button press, card lift) are inferred from Shopify Dawn/theme conventions.
- No breakpoint values were confirmed from source; widths used in Responsive Behavior follow Shopify's standard Dawn theme breakpoints and should be verified against the theme's CSS.
- Icon style and illustration system (line weight, fill style, corner radius of icons) could not be determined without authenticated site access or a full design file.
- Product photography art direction (background treatment, cropping standard, lifestyle vs. studio ratio) observed but not quantifiable without access to the full media library.
