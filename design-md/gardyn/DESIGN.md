---
version: alpha
name: "Gardyn"
source_url: "https://mygardyn.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The palette arrives before the product pitch: #123c2e, a near-black forest green pulled from the deepest strata of a mature canopy, faces off against #fff8f2, a cream that reads like afternoon light filtering through greenhouse film. Between them, Gardyn positions two shot-of-energy accents — #ffa763, a harvest orange that appears on primary CTAs and urgency banners, and #c6ea5f, a young-leaf lime reserved for plant-variety badges and quantity indicators. The structural contrast between dark botanical authority and fresh-produce brightness is the brand's signature voltage: it suggests both the precision of hydroponic science and the pleasure of a Tuesday-morning harvest in your own kitchen.

  Type arrives in two distinct voices. P22 Mackinac Pro — a contemporary serif with soft, ink-press curves — handles all display work: hero headlines, product names, section openers. It runs at weights 400–500 rather than the slab-heavy 700 favoured by hardware DTC brands, leaning into legibility and warmth over mechanical force. P22 Underground, Edward Johnston's geometric sans-serif lineage redrawn for digital use, takes the UI layer: navigation labels, button copy, form fields, pricing, and caption data. Proxima Nova serves as the long-form body workhorse wherever body-md prose blocks appear. The result is a magazine editorial stack operating inside a functional e-commerce chassis.

  Corner radii shift meaningfully across component scale. Primary CTAs use {rounded.full} pill shapes that echo seed pods; cards and input fields sit at {rounded.md} (12px) — approachable without signalling toy-like softness. The warm-cream canvas ({colors.canvas}) replaces the sterile white typical of device brands; pale-mint ({colors.surface-mint}) backs alternating content sections, evoking grow medium rather than a product page. The brand uses lime ({colors.lime}) almost nowhere except plant-badge backgrounds and a single "New Pod" indicator — its restraint makes each appearance land. Gardyn's visual language treats the indoor farm as a lifestyle appliance: every layout decision signals abundance, precision, and the presence of something living in your home.

colors:
  primary: "#123c2e"
  primary-active: "#0a191c"
  primary-disabled: "#3f6f5a"
  accent: "#ffa763"
  accent-active: "#f0ad4e"
  accent-disabled: "#ffe0c2"
  lime: "#c6ea5f"
  lime-strong: "#c1ed40"
  ink: "#0a191c"
  body: "#32373c"
  muted: "#69727d"
  hairline: "#edf3f0"
  hairline-strong: "#d0dbd6"
  canvas: "#fff8f2"
  surface-soft: "#ffefdf"
  surface-card: "#ffffff"
  surface-mint: "#edf3f0"
  on-primary: "#fff8f2"
  on-accent: "#0a191c"
  on-lime: "#123c2e"
  error: "#d9534f"
  success: "#5cb85c"
  info: "#5bc0de"

typography:
  display-xl:
    fontFamily: "'p22-mackinac-pro', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'p22-mackinac-pro', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'p22-mackinac-pro', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'p22-mackinac-pro', Georgia, serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-lg:
    fontFamily: "'p22-underground', 'p22-underground-pc', Futura, 'Trebuchet MS', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'p22-underground', 'p22-underground-pc', Futura, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'p22-underground', 'p22-underground-pc', Futura, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'proxima-nova', 'proforma', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', 'proforma', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', 'proforma', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-strong:
    fontFamily: "'proxima-nova', 'proforma', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'p22-underground', 'p22-underground-pc', Futura, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'p22-underground', 'p22-underground-pc', Futura, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'p22-underground', 'p22-underground-pc', Futura, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'p22-underground', 'p22-underground-sc', Futura, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'p22-underground', 'p22-underground-pc', Futura, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'p22-mackinac-pro', Georgia, serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.2px
  overline:
    fontFamily: "'p22-underground', 'p22-underground-sc', Futura, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.4
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 16px 36px
    height: 56px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    opacity: 0.5
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 16px 36px
    height: 56px
    border: none
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.hairline-strong}"
    padding: 12px 16px
    height: 52px
    focusBorder: "1.5px solid {colors.primary}"
  text-input-error:
    border: "1.5px solid {colors.error}"
    textColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 16px rgba(18,60,46,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    imageAspectRatio: "4/3"
    shadow: "0 4px 24px rgba(18,60,46,0.08)"
  product-card-featured:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xl}"
    border: "2px solid {colors.primary}"
    padding: "{spacing.xl}"
    shadow: "0 8px 40px rgba(18,60,46,0.14)"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    overlayColor: "rgba(18,60,46,0.72)"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 640px
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-lg}"
    subtitleTypography: "{typography.body-md}"
    imageColumn: "55%"
    contentColumn: "45%"
    contentPadding: "{spacing.xxl}"
  plant-variety-badge:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.on-lime}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    height: 24px
  kit-tier-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  new-pod-badge:
    backgroundColor: "{colors.lime-strong}"
    textColor: "{colors.on-lime}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  subscription-pill:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.sm}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  grow-progress-bar:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.lime}"
    height: 6px
    rounded: "{rounded.full}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    quoteTypography: "{typography.body-md}"
    attributionTypography: "{typography.caption-strong}"
    attributionColor: "{colors.primary}"
    border: none
  section-overline:
    textColor: "{colors.primary}"
    typography: "{typography.overline}"
    marginBottom: "{spacing.sm}"
  feature-icon-tile:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    iconSize: 40px
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
  pricing-tier-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
    border: "1.5px solid {colors.hairline}"
    titleTypography: "{typography.title-lg}"
    priceTypography: "{typography.price-display}"
    highlightBorder: "2px solid {colors.primary}"
    highlightBackground: "{colors.canvas}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.lime}"
    borderTop: none
    paddingY: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — The main CTA is a deep forest-green (#123c2e) pill with uppercase P22 Underground tracking (+0.5px) on warm-cream text (#fff8f2), 56px tall with generous 36px side padding. On hover it darkens to the near-black primary-active (#0a191c); the disabled state fades to the mid-range green (#3f6f5a) at 50% opacity rather than turning grey, so it stays on-brand even inactive.

**`button-accent`** — An alternate CTA in harvest orange (#ffa763) on near-black text (#0a191c), using the same pill geometry and button-lg typography. Reserved for purchase-urgency moments ("Get Yours Today", seasonal sale CTAs) and high-contrast placements over the dark primary hero background where the green button would disappear. Active state shifts to amber (#f0ad4e).

**`button-secondary`** — Transparent fill with a 2px forest-green border and matching text, same pill shape at 52px height. Converts to a filled primary button on active/hover — no intermediate outline-with-fill state.

**`button-ghost`** — Borderless, transparent, small (button-sm type) for inline low-hierarchy actions like "Learn more" or "See all pods." Uses ink text and full-radius rounding to match the button family without weight.

### Navigation Bar

**`nav-bar`** — 72px tall on the warm cream canvas (#fff8f2), with a 1px pale-mint hairline bottom border that is only visible on cream backgrounds. The Gardyn wordmark uses display-sm (p22-mackinac-pro, 24px/500) in primary ink. Navigation links in 14px P22 Underground (600 weight, +0.3px tracking, uppercase) sit right-aligned. On scroll, a soft shadow (0 2px 16px rgba(18,60,46,0.08)) lifts the bar above page content without colour change.

### Product Card

**`product-card`** — White surface-card background, {rounded.lg} (20px) corners, a single 1px hairline border (#edf3f0), and a subtle green-tinted shadow. The product title uses title-md (P22 Underground 20px/600), the price uses the standalone price-display scale (p22-mackinac-pro 28px/500). Kit-tier badges stack below the image in the upper-left corner; plant-variety badges appear as a scrolling pill row beneath the product name. The featured variant elevates to {rounded.xl} with a 2px primary border and heavier shadow.

### Hero

**`hero`** — Full-bleed image with a 72% opacity forest-green scrim layer (rgba(18,60,46,0.72)), making the background photographic but firmly on-brand. The headline runs at display-xl (p22-mackinac-pro 56px/400), sitting comfortably at line-height 1.08 — this weight choice at display size is notable; it reads as editorial magazine rather than billboard. A section-overline label (uppercase P22 Underground, +1.5px tracking, primary green) sits above the headline to name the content category.

**`hero-split`** — Two-column layout (55/45 image/content split) on a warm cream canvas for product-detail sections below the fold. The content column runs left with display-lg headline and body-md prose, the primary CTA button, and a subscription-pill showing included service tier.

### Plant Variety Badge

**`plant-variety-badge`** — Young-leaf lime (#c6ea5f) pill with dark forest text (#123c2e), uppercase P22 Underground-sc at 11px and +0.8px tracking. These are tiny — 24px tall — and appear in horizontal scroll rows on product cards and as filter chips in the plant catalog. The lime color is used almost nowhere else, making these badges pop immediately as the plant-selection affordance.

### Subscription Pill

**`subscription-pill`** — Pale mint background (#edf3f0) with a 1px hairline border, forest-green caption text, 8px corners. Used inline below product prices to flag subscription tiers ("Pods Plan Included", "Auto-Refill"). Caption-strong typography (12px/600) keeps it readable at small scale without dominating the price hierarchy.

### Grow Progress Bar

**`grow-progress-bar`** — A 6px full-radius track (hairline fill #edf3f0) with young-leaf lime fill (#c6ea5f). Paired with a caption label in muted gray showing week count or percentage. Appears inside plant-status views and post-purchase progress dashboards. The thin profile and soft colour prevent it from feeling clinical.

### Feature Icon Tile

**`feature-icon-tile`** — Pale mint (#edf3f0) background tile with {rounded.lg} corners, a 40px icon in primary green, title-sm heading, and body-sm prose. Used in grid formations (2-up on mobile, 4-up on desktop) for "Why Gardyn" content sections. No drop shadow — the tint background creates sufficient separation from the canvas.

### Pricing Tier Card

**`pricing-tier-card`** — White card with {rounded.xl} corners and 1.5px hairline border. The title uses title-lg (24px P22 Underground) and the price uses price-display (p22-mackinac-pro 28px/500). The featured tier swaps to a 2px primary border on the same white background rather than a filled background, keeping the hierarchy reading from the typography and not the container colour.

### Testimonial Card

**`testimonial-card`** — Pale peach surface (#ffefdf), {rounded.lg} corners, no border. The quote runs in body-md (proxima-nova 16px/400, line-height 1.6) and attribution in caption-strong with primary green colour. Cards sit in a horizontal scroll row or 3-column grid at desktop. The peach background gently separates this section from the cream canvas without the full contrast of a mint or green section.

### Footer

**`footer`** — Deep forest green (#123c2e) background occupying full-width, warm-cream (#fff8f2) text. Column headings use title-sm (P22 Underground 16px/600), link items use body-sm (proxima-nova 14px/400) in the hairline tone (#edf3f0) with lime hover (#c6ea5f) for interactivity signalling. The lime hover on a dark green footer is a brand-coherent detail — the same lime-on-green relationship as a leaf illuminated by grow light.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero switches to stacked (image above, content below) with display-lg (40px) headline; nav collapses to hamburger icon + wordmark; product cards go full-width; plant-variety badges become horizontally scrollable row; hero min-height reduces to 480px; padding drops from section (64px) to xl (32px) per section |
| Tablet | 744–1128px | Two-column product grid; hero-split activates at 52/48 split; nav shows top-level links only (no mega-menu); feature icon tiles switch to 2-column grid; testimonial cards become 2-up scrollable |
| Desktop | 1128–1440px | Three-column product grid; full nav with hover mega-menu; hero-split at 55/45; feature icon tiles 4-up; testimonial 3-up; pricing tier cards display inline (3-column) |
| Wide | > 1440px | Max content width 1280px centred; section padding increases to 96px; display-xl scales to 64px; hero image gains parallax depth treatment |

### Touch Targets

- All interactive pill buttons maintain minimum 52–56px height on mobile, never below 44px
- Plant-variety badge row uses horizontal scroll with -webkit-overflow-scrolling: touch and 16px side padding gutters
- Nav hamburger touch target is 48×48px with padding around a smaller visual icon
- Grow-progress-bar tap area padded to 32px tall even though the visual bar is 6px

### Collapsing Strategy

- Navigation: hamburger at < 744px; full horizontal links at ≥ 744px with CTA button visible at ≥ 1128px
- Hero: full-bleed image with overlay at all breakpoints, but text column becomes full-width on mobile with reduced font scale
- Product grid: 1-col mobile → 2-col tablet → 3-col desktop; featured card spans full row at all breakpoints
- Feature tiles: single-column list on mobile (icon left, text right inline) → 2-up grid tablet → 4-up desktop
- Footer: single-column stacked on mobile with accordion-toggle headings → 4-column grid at desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius values from the live site; {rounded.full} for buttons and {rounded.lg/xl} for cards are inferred from hydroponic-brand conventions and the general DTC softness signalled by the warm palette
- The exact font weight and size pairings for p22-mackinac-pro and p22-underground at specific breakpoints could not be extracted; values are calibrated to the editorial/precision register the palette implies
- Meta theme-color was absent, so dark-mode or mobile-chrome bar treatment is unknown
- Motion and animation tokens (hover durations, scroll transitions) are absent from extraction; no values assigned
- Icon library and exact icon style (stroke weight, filled vs. outlined) could not be determined from the extracted hints; eicons is present but custom glyph mapping is unknown
- Exact grid gutter and max-content-width values were not extracted; 1280px max-width and 24px gutters are standard estimates
- The role of `proforma` vs `proxima-nova` for body text is ambiguous; both appear in the font stack and the exact context for each is unconfirmed
- No dark-mode colour variants were extractable
