---
version: alpha
name: "Lulu"
source_url: "https://www.lulu.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The first choice on Lulu's creation flow is not which plan to purchase but which format the finished object will take — hardcover, softcover, coil-bound, ebook — and that inversion of the standard SaaS conversion funnel defines the entire visual logic of the site. The extracted charcoal #313131 anchors all body copy at a warmth closer to an inkjet proof than an interface default; it sits roughly three-quarters of the way to black rather than at full #000000, softening tables of paper weights and ISBN steps without drifting into neutral gray. Primary CTAs fire in a mid-spectrum green that communicates "begin" rather than urgency — the exact value is inferred from brand knowledge since the live site returned a Cloudflare challenge page and extraction yielded only the charcoal (see Known Gaps), but the green-on-white logic is consistent with Lulu's documented brand direction. Typography relies entirely on the system stack — -apple-system, Segoe UI, Roboto — a choice that rewards returning authors managing multiple in-flight manuscripts: pages load instantly without a custom-font flash delaying the project dashboard. The creation wizard divides work into discrete numbered steps, each given {spacing.section} of vertical clearance to prevent a first-time publisher from conflating paper finish options with binding types. Saved project cards sit on {colors.surface-card} with a hairline border and {rounded.sm} corners rather than elevated shadows, echoing the flat, stackable quality of a manuscript pile rather than the lifted-card convention of a consumer marketplace. Format selectors — Print, Ebook, Bundle — run as {rounded.full} pill chips, scannable by shape before label text is parsed. A near-black footer pulls from the same charcoal register without requiring a separate accent color, grounding the page through tonal depth rather than hue contrast.

colors:
  primary: "#00B386"
  primary-active: "#009970"
  primary-disabled: "#99DDD1"
  ink: "#313131"
  body: "#4A4A4A"
  muted: "#767676"
  hairline: "#DDDDDD"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  footer-bg: "#1E1E1E"
  step-complete: "#313131"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
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
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  step-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px

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
    padding: "12px 24px"
    height: 48px
    hover:
      backgroundColor: "{colors.primary-active}"
    disabled:
      backgroundColor: "{colors.primary-disabled}"
      textColor: "{colors.on-primary}"

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "11px 23px"
    height: 48px
    hover:
      backgroundColor: "{colors.surface-soft}"

  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
    placeholderColor: "{colors.muted}"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    metaTypography: "{typography.body-sm}"
    metaColor: "{colors.muted}"
    shadow: none

  hero-creation:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    paddingVertical: "{spacing.section}"
    ctaComponent: "button-primary"

  format-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "none"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"

  workflow-steps:
    activeStepBackground: "{colors.primary}"
    activeStepNumberColor: "{colors.on-primary}"
    completedStepBackground: "{colors.step-complete}"
    completedStepNumberColor: "{colors.on-primary}"
    pendingStepBorder: "1px solid {colors.hairline}"
    pendingStepBackground: "{colors.canvas}"
    connectorColor: "{colors.hairline}"
    stepLabelTypography: "{typography.step-label}"
    stepLabelColor: "{colors.muted}"
    activeStepLabelColor: "{colors.ink}"

  pricing-tier:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    priceTypography: "{typography.display-md}"
    priceColor: "{colors.ink}"
    featureTypography: "{typography.body-sm}"
    featureColor: "{colors.body}"
    ctaComponent: "button-primary"

  badge-format:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"

  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    legalTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Filled {colors.primary} green at 48px height with {rounded.sm} corners and {typography.button-md} weight. Carries the three decisive moments in the Lulu workflow: "Start Creating," "Save and Continue," and "Order Now." Hover tightens to {colors.primary-active}; disabled washes to {colors.primary-disabled} while retaining the same corner radius so the affordance remains legible even when unavailable.

**`button-secondary`** — White canvas background with a 1px {colors.primary} border and matching text, used for alternatives that run alongside the primary CTA — "Preview," "Download Proof," "Save Draft." Hover fills with {colors.surface-soft} to register feedback without erasing the boundary definition. Shares the 48px height with button-primary so paired CTAs sit flush on a horizontal baseline.

**`button-ghost`** — Transparent background with {colors.ink} text, reserved for low-commitment actions like "Cancel" or "Back" within the creation wizard. Its visual silence ensures it does not pull focus from the green primary pathway.

### Text Input

**`text-input`** — 44px tall field with a 1px {colors.hairline} rest border that upgrades to a 2px {colors.primary} focus ring, giving authors a clear signal of the active field during multi-step forms. Placeholder copy in {colors.muted} distinguishes hint text from entered content. Appears across book title entry, ISBN lookup, discount code, and distribution territory fields.

### Navigation

**`nav-bar`** — 64px white bar with a 1px {colors.hairline} bottom rule separating it from page content. {typography.nav-link} at 14px/500 keeps the navigation secondary to the creation workflow below it. Logo sits at the left edge; a single button-primary CTA ("Start Creating" or "Get Started") anchors the right; product-category links (Print, Ebook, Resources, Pricing) center the bar. No mega-menu or flyout panel — the navigation surface is deliberately shallow.

### Product Cards

**`product-card`** — 1px {colors.hairline}-bordered card with {rounded.sm} corners on a {colors.surface-card} white base. Displays project thumbnail (book cover image or format placeholder), title in {typography.title-sm}/{colors.ink}, and status or format metadata in {typography.body-sm}/{colors.muted}. No drop shadow — the flat construction keeps the visual language grounded in the physical paper object rather than the glass-and-light aesthetic of consumer apps. Cards tile in a grid on the author dashboard, stacking to single-column on mobile.

### Hero

**`hero-creation`** — Full-width {colors.canvas} section leading with a {typography.display-xl} headline, {typography.body-md} sub-copy in {colors.body}, and a button-primary CTA. Vertical padding of {spacing.section} top and bottom frames the message with editorial breathing room. Typically accompanied below fold by a format-picker row of format-chip selectors, guiding new visitors immediately into the creation decision rather than a pricing comparison.

### Format Chips

**`format-chip`** — Pill-shaped selectors ({rounded.full}) for Print, Ebook, and Bundle format categories arranged in a horizontal row. Inactive state: {colors.surface-soft} fill with a 1px {colors.hairline} border and {colors.body} label text. Active state: {colors.primary} fill with {colors.on-primary} text, border removed. {typography.button-sm} at 14px/500 keeps labels compact. On mobile the row scrolls horizontally rather than wrapping to preserve the single-scan affordance.

### Workflow Steps

**`workflow-steps`** — Numbered step indicator running across the top of the book-creation wizard: Format → Upload → Cover → Distribution → Pricing. Active step: filled {colors.primary} circle with {colors.on-primary} numeral. Completed step: filled {colors.step-complete} charcoal circle with a checkmark glyph in {colors.on-primary}. Pending step: empty circle with a 1px {colors.hairline} border. Step labels below each circle use {typography.step-label} in {colors.muted}; the active step label promotes to {colors.ink}. Horizontal connector lines in {colors.hairline} link circles. On mobile, labels are hidden and only the circles and connectors remain visible.

### Pricing Tiers

**`pricing-tier`** — Card with a 1px {colors.hairline} border, {rounded.md} corners, and {spacing.lg} internal padding. Plan price in {typography.display-md}/{colors.ink}. Feature list in {typography.body-sm}/{colors.body} with a simple bullet or checkmark treatment. Each card closes with a button-primary CTA. Recommended plan receives no visual elevation beyond a slightly bolder border or a subtle badge — the layout does not use colored headers or dark-fill highlight cards.

### Format Badges

**`badge-format`** — Compact pill ({rounded.full}) labels marking physical format on project cards and catalog listings: Hardcover, Softcover, Coil-Bound, Linen Wrap. {typography.badge} at 12px/600; {colors.surface-soft} background with a 1px {colors.hairline} border. No color coding differentiates format types — the text label alone carries the distinction, keeping the badge system extensible without requiring a growing color vocabulary.

### Footer

**`footer`** — Near-black {colors.footer-bg} background with {colors.canvas} text throughout. Three to four column link grid uses {typography.body-sm}; legal copy and copyright line drop to {typography.caption}. No accent or highlight colors appear in the footer — the dark register is drawn from the same charcoal family as the brand's ink, making the transition feel like a paper edge rather than a hard brand shift. {spacing.xxl} top and bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; format chips scroll horizontally; workflow-steps show circles only, labels hidden; product-cards stack vertically; nav collapses to hamburger + logo + CTA button |
| Tablet | 744–1128px | Two-column product-card grid; hero splits headline left / format-chip row right; pricing tiers in 2-up grid; nav shows primary links, secondary links move to hamburger drawer |
| Desktop | 1128–1440px | Full three-column product-card and pricing grids; workflow-steps display full step labels; nav shows all product-category links; hero with full {spacing.section} vertical padding |
| Wide | > 1440px | Content width capped at ~1280px and centered; hero and section gutters gain additional horizontal margin; no structural layout changes beyond the cap |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Format chips extend vertical padding to 12px on small screens to reach touch-target height
- Workflow step circles minimum 40px diameter with a 44px invisible tap zone
- Nav hamburger minimum 44×44px tap area
- Product card entire surface area is tappable, not just the title text

### Collapsing Strategy
- Workflow step labels are hidden below 744px; only numbered circles and connector lines persist
- Pricing tier grid collapses 3-col → 2-col at tablet → 1-col at mobile, with the recommended tier rendered first in the stacked order
- Footer link columns collapse 4-col → 2-col at tablet → 1-col at mobile with accordion-style section expansion
- Nav secondary links (Help, Blog, API Docs) move to the hamburger drawer at < 1128px; primary product-category links move there at < 744px
- Hero layout shifts from side-by-side (text + format picker) at desktop to stacked (text above, format chips below) at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was successfully extracted — the live site returned a Cloudflare "Just a moment..." anti-bot challenge page, blocking full CSS token and palette extraction. All colors beyond the charcoal ink are inferred from brand knowledge and design convention, not site measurement.
- The primary green value (#00B386) is an estimate derived from brand context knowledge; the exact measured hex may differ. No secondary or tertiary palette colors could be confirmed.
- No custom typeface detected — the extracted font stack is entirely system fonts. It is possible Lulu loads a licensed or custom face via JavaScript after the Cloudflare challenge resolves; this could not be confirmed.
- No meta theme-color was set; mobile browser chrome color and PWA manifest accent color are unknown.
- Button corner radius, input field height, card shadow depth, and grid gutter widths could not be measured; values in this spec are design-appropriate estimates consistent with the functional, low-chrome aesthetic of a publishing workflow tool.
- Dark mode support is unknown — no prefers-color-scheme token variants were extractable.
- Illustration and photography style (book-cover mockup photography, flat vector art, or 3D product renders) not confirmed from extraction.
- Whether Lulu uses a distinct "Lulu Direct" or enterprise tier visual treatment (separate color or badge system) could not be determined.
