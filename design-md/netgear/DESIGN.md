---
version: alpha
name: "Netgear"
source_url: "https://www.netgear.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The site opens on a near-black field (#1a1918), where router chassis renders and animated signal-ring graphics float against the void the same way an actual Nighthawk sits on a shelf in an unlit rack room — the display logic is borrowed from the hardware, not from a marketing playbook. The primary action color, #029ddf, is a clear-sky cyan-blue that lands between consumer-friendly and enterprise-legible without fully committing to either; it runs from full-width CTA buttons on product detail pages to the interactive ring in hero animations to the hover accent on nav links. Outfit is the sole text workhorse — a geometric rounded sans-serif whose even stroke weights let spec-dense product pages stay readable rather than compressed, while its mild letterforms soften an otherwise stark black-and-blue palette.
  Color architecture runs in two modes. Light-mode marketing and category pages sit on #ffffff canvas with #e2e8f0 surface cards and #d1d1d1 hairlines — a clean retail register. Dark-mode hero sections drop to #1a1918 or the deep navy #192f5d, a blue so saturated it reads like a signal-diagram background in a network-operations center. Accent-red #bd3d44 marks the Nighthawk sub-brand and security-alert states; #e7772f orange flags promotional tiers and bundle callouts. Spec tables on every product page embed a monospaced type treatment (SFMono-Regular, Consolas), encoding the brand's argument that publishing raw numbers — AXE6000, BE19000, port counts, coverage square footage — is itself a sales act.
  Corner geometry is deliberately controlled: primary buttons sit at {rounded.sm} (8px) rather than pill-shaped, giving CTAs a formal register that suits prosumer and enterprise buyers who distrust marketing softness. Product cards earn {rounded.md} (12px) — approachable without being consumer-toy. Badge pills and toggle chips use {rounded.full} for clear small-element click-area signaling. The persistent dark navigation bar (#181818) anchors the brand-dark aesthetic even when the page section below it switches to white canvas. Spacing steps jump from tight (4–8px within spec rows) to generous (64px section separators in hero blocks), mapping cadence to content density rather than applying a single rhythm site-wide.

colors:
  primary: "#029ddf"
  primary-active: "#016fd0"
  primary-disabled: "#52606d"
  navy: "#192f5d"
  navy-deep: "#033389"
  dark-bg: "#1a1918"
  dark-surface: "#2b3749"
  ink: "#181818"
  body: "#2b3749"
  muted: "#52606d"
  hairline: "#d1d1d1"
  hairline-soft: "#e2e8f0"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#e2e8f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#bd3d44"
  accent-orange: "#e7772f"
  accent-amber: "#f79e1b"

typography:
  display-xl:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-mono:
    fontFamily: "'SFMono-Regular', Consolas, Menlo, Monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
    padding: "14px 28px"
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "13px 27px"
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "1.5px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "13px 27px"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
    activeAccent: "{colors.primary}"
    hoverTextColor: "{colors.primary}"
  category-nav-item:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    paddingBottom: "{spacing.sm}"
    borderBottomActive: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    shadow: "0 2px 12px rgba(0,0,0,0.08)"
    shadowHover: "0 6px 24px rgba(0,0,0,0.14)"
  hero-banner:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.surface-soft}"
    paddingVertical: "{spacing.section}"
    ctaVariant: button-primary
    secondaryCtaVariant: button-ghost
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-badge-alert:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  spec-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    valueTypography: "{typography.spec-mono}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
  promo-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    accentColor: "{colors.accent-orange}"
    padding: "{spacing.lg} {spacing.xl}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.muted}"
    linkColor: "{colors.surface-soft}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.spec-label}"
    headingColor: "{colors.on-dark}"
    borderTop: "1px solid {colors.dark-surface}"
    legalTypography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — The primary CTA across product pages and checkout flows. Filled {colors.primary} (#029ddf) with white text at {typography.button-md}, sitting at {rounded.sm} (8px) rather than pill-shaped — the restrained radius gives it a formal, hardware-catalog authority. Hover transitions to {colors.primary-active} (#016fd0) over 150ms; disabled state uses {colors.primary-disabled} with 0.6 opacity. Appears at full-width on mobile and fixed minimum-width (≥160px) on desktop.

**`button-secondary`** — Outlined sibling to `button-primary`: white {colors.canvas} background, {colors.primary} border and text. Used alongside the primary for "Compare" and "Add to Wishlist" actions on product detail pages. Shares the same 48px height and {rounded.sm} radius for flush side-by-side alignment.

**`button-ghost`** — Transparent fill with white border and text ({colors.on-dark}). Appears exclusively inside dark hero banners and {colors.navy} promo bands where a solid-fill CTA would compete with the headline image. Same 48px height and {rounded.sm} radius as other button variants; inherits the parent section's background instead of painting its own.

### Text Input & Search

**`text-input`** — White {colors.canvas} field with a 1px {colors.hairline} border. Focus ring steps up to 1.5px {colors.primary}, clearly signaling active state. Placeholder in {colors.muted}; typed text in {colors.ink}. Fixed at 44px height to satisfy touch-target minimums on mobile product configurators and checkout forms.

**`search-bar`** — Sits in the top navigation on desktop and expands to a full-width overlay on mobile tap. Uses {colors.surface-soft} background rather than white to visually lift it from surrounding page canvas. Leading magnifier icon in {colors.muted}; on focus, border transitions to {colors.primary} and the icon color steps to {colors.ink}.

### Navigation

**`nav-bar`** — Persistent dark bar at 64px height in {colors.dark-bg} (#181818). Logo anchored left; primary category links and utility icons (search, account, cart) in {typography.nav-link} white; active and hover states show {colors.primary} text tint. On page scroll, a subtle drop shadow is added but the dark fill is retained — the bar never bleaches to white. Collapses to hamburger icon plus logo at breakpoints below 1128px.

**`category-nav-item`** — Horizontal tab rail below the top navigation on category and product-family pages. Inactive items render in {colors.muted}; the active item switches to {colors.ink} text with a 2px {colors.primary} bottom border. No background fill change on hover — the underline is the exclusive state indicator, keeping the rail visually flat.

### Product Card

**`product-card`** — White {colors.canvas} card with 1px {colors.hairline} border and {rounded.md} corners. Product image occupies the upper portion; below it: product name in {typography.title-sm}, a horizontal row of `spec-chip` elements (Wi-Fi generation, coverage, ports), then price in {typography.title-md}. Shadow elevates from `0 2px 12px rgba(0,0,0,0.08)` to `0 6px 24px rgba(0,0,0,0.14)` on hover. Badge overlay anchors to the top-left corner of the image region.

### Spec Chip

**`spec-chip`** — The brand's primary data-display unit and one of its most recognizable UI patterns. A small {rounded.xs} rectangle in {colors.surface-card} with a monospaced value in {typography.spec-mono} (Consolas, SFMono-Regular) and an all-caps label printed above it in {typography.spec-label} using {colors.muted}. Used inside product cards, comparison tables, and spec-callout rows embedded in hero sections. Encodes Wi-Fi tier names (AXE6000, BE19000), square-footage ranges, and port counts — the brand's position is that these numbers sell the product and they should be impossible to miss.

### Hero Banner

**`hero-banner`** — Full-bleed dark section in {colors.dark-bg}, padding {spacing.section} top and bottom. Headline in {typography.display-xl} white; subhead in {typography.body-md} using {colors.surface-soft} (slightly off-white to reduce glare against the dark ground). Product render or animated chassis illustration floats right on desktop in a roughly 55/45 text-to-image split; below 744px, the image collapses to a top-of-section banner crop and text runs below it. CTA pair: `button-primary` left, `button-ghost` right.

### Badges

**`product-badge`** — Pill-shaped chip ({rounded.full}) in {colors.primary} with {typography.spec-label} white text. Marks Wi-Fi 7 generation, "New", and bundle inclusions on product card image corners and in category-listing rows. **`product-badge-alert`** substitutes {colors.accent-red} for Nighthawk security-tier labeling (Armor, Insight) and promotional urgency signals like "Limited Stock." Both badges share the same 4px 10px padding and typographic treatment; only fill color changes.

### Promo Banner

**`promo-banner`** — Full-width band in {colors.navy} with headline in {typography.title-md} and {colors.accent-orange} used for discount amounts and countdown labels. Zero corner radius ({rounded.none}) — it bleeds edge-to-edge and reads as a system announcement rather than a floating card. Body copy in {typography.body-sm} white; CTA button uses `button-primary` which contrasts cleanly against the navy field.

### Footer

**`footer`** — Dark {colors.dark-bg} footer with a four-column link grid on desktop. Column headings in {typography.spec-label} ({colors.on-dark}); links in {typography.body-sm} ({colors.surface-soft}), transitioning to {colors.primary} on hover. Bottom row separates with a 1px {colors.dark-surface} rule, then carries legal text in {typography.caption} and {colors.muted} alongside payment-method icons and compliance certification marks.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger + logo; hero stacks image above text; product-cards in 1-column grid; spec-chips wrap vertically; search expands to full-width overlay; footer columns become accordion sections |
| Tablet | 744–1128px | 2-column product grid; nav shows logo + search + hamburger (no inline category links); hero uses side-by-side layout with display-md headline; promo-banner text allowed to wrap to two lines |
| Desktop | 1128–1440px | Full nav-bar with all primary category links visible; 3-column product grid; hero at full display-xl; spec-chip row renders horizontal inside product cards |
| Wide | > 1440px | Content max-width capped at 1440px and centered; hero sections gain additional vertical padding (section × 1.5); category pages support 4-column product grid |

### Touch Targets
- All interactive controls minimum 44×44px
- `nav-bar` hamburger carries a 44×44px hit area padded out from the visible 24px icon
- `product-card` tap target covers the full card surface including image region
- `category-nav-item` minimum 44px height including bottom padding
- `search-bar` input height fixed at 44px
- `spec-chip` is a display-only element — no minimum size constraint applies

### Collapsing Strategy
- Primary nav links and product-category links disappear behind hamburger below 1128px; search and account icons remain visible in the bar
- Category nav rail becomes horizontally scrollable on mobile — no wrapping, no truncation
- Hero product renders drop to a top-of-section banner crop below 744px; side-by-side layout is removed
- Spec-chip rows in product cards truncate to three chips plus a "view all specs" text link on mobile
- Footer four-column grid collapses to accordion expand/collapse sections below 744px; legal row stacks vertically
- Promo banner reduces to headline and CTA on a single line below 744px; body copy is hidden

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Outfit weight distribution across the live site not confirmed — weight range 100–900 assumed available but actual heading vs. body weight assignments are approximated from geometric-sans conventions
- Several extracted hex values (#0acf83, #a259ff, #f24e1e, #ff7262, #1abcfe) originate from an embedded Figma Community badge rather than Netgear brand assets — excluded from palette entirely
- Payment-method icon colors (#f79e1b Mastercard amber, #016fd0 Visa blue) and national-flag colors (#ed2939, #002395, #009246, #ce2b37, #ee1c25) appear in the crawl as incidental footer icons, not brand tokens
- No meta theme-color set — mobile browser chrome color is unconfirmed
- Dark-mode toggle or system-preference switching not observed; two-mode color architecture is inferred from coexistence of near-black hero sections and white-canvas product pages within the same layout
- Custom icon set vs. licensed library (Heroicons, Phosphor, etc.) not identifiable from static extraction
- Animation timing functions, easing curves, and motion-system tokens not extractable from a static crawl
- Exact elevation / box-shadow scale for product cards and modal overlays is approximated from common e-commerce patterns, not measured
