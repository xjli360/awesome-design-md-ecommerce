---
version: alpha
name: "Tin House"
source_url: "https://www.tinhouse.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A small press publisher that wears its primary red #ee3124 like a book-cloth spine — saturated, confident, and used sparingly enough that it lands as a signature rather than a shout. The site runs on a warm off-white canvas #f7f6ff that reads as paper stock, with body text in a quiet #444444 and secondary copy in #717171, creating a reading-room hierarchy where the typography does not compete with the words. Founders Grotesk, the declared brand face, carries display and body work at moderate weights — no heavy 700+ display sizes, no uppercase shouting — trusting the literary content to hold attention. The extracted palette includes a surprising streak of blues (#0600ff, #0b0f5a, #0000ff) that may belong to social icons or checkout widgets rather than the brand itself; the true brand voice is the red-and-white editorial frame with #222222 ink for headlines. Navigation is minimal — a thin bar with the logo left and a short link set right — and the footer runs deep with columns of series, authors, and newsletter signup, all in {typography.body-sm} with {rounded.none} corners. Cards carry soft shadows and {rounded.sm} corners, but the overall feel is typographic and flat: the brand trusts its cover designs and author names, not decorative UI.

colors:
  primary: "#ee3124"
  primary-active: "#cc2a1f"
  primary-disabled: "#f5a39d"
  ink: "#222222"
  body: "#444444"
  muted: "#717171"
  muted-soft: "#a2a4c3"
  hairline: "#cccddc"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f7f6ff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#0600ff"
  accent-navy: "#0b0f5a"
  accent-muted-blue: "#616394"

typography:
  display-xl:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Founders Grotesk', 'Simula', Georgia, serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 10px 24px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 9px 23px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-item:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-item-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-author:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 32px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    color: "{colors.canvas}"
    typography: "{typography.title-sm}"
    margin-bottom: "{spacing.base}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
    height: 36px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  social-icon-link:
    color: "{colors.muted-soft}"
    height: 24px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, a flat red rectangle with no rounding. Uses Founders Grotesk at 14px/500 with 0.3px letter spacing. On hover, shifts to `button-primary-active` (#cc2a1f). Disabled state uses `button-primary-disabled` (#f5a39d) with white text. Secondary buttons use a white background with a thin #cccddc border and dark text; active state fills with the soft lavender #f7f6ff. A tertiary text-only variant exists for less prominent actions like "View all" links, styled in primary red with no background.

### Cards
**`product-card`** — A book cover card with a white background and soft 8px rounding. The image sits flush to the top with top-only rounding. Below, the title uses `title-sm` (16px/500) and the author name uses `caption` (13px/400) in muted gray #717171. No shadow by default; on hover a subtle box-shadow appears. Badges like "New" or "Sale" overlay the top-left corner of the image using `badge-new` (red) or `badge-sale` (navy).

### Navigation
**`nav-bar`** — A 64px white bar with the Tin House logo left-aligned and a short set of nav links right-aligned. Links use `nav-link` (14px/500) with 0.2px letter spacing. Active page or hover state tints the link text to primary red. No background color change on hover — the brand keeps navigation minimal and typographic.

### Forms
**`text-input`** — A flat, border-only input field with 1px #cccddc border and no rounding. On focus, the border switches to primary red. Newsletter signup fields follow the same pattern but at a smaller 36px height, paired with a red submit button of matching height. Search bars use a soft #f7f6ff background instead of white, with the same border treatment.

### Footer
**`footer-section`** — A deep navy/black footer (#222222) with white text. Columns for series, authors, events, and newsletter signup. Links use `footer-link` in muted-lavender #a2a4c3. The newsletter form sits in its own column with a white input and red submit button. Social icons appear as 24px links in the same muted-lavender tone.

### Hero
**`hero-section`** — A full-width banner using the soft lavender #f7f6ff background. Display text at 32px/500 with tight letter spacing. A single primary-red CTA button sits below the headline. No decorative imagery — the hero relies on typography and the brand color to create impact.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically at full width; hero padding reduces to 32px; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero keeps two-thirds width; footer shows 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero at max 1128px centered; footer in 4-column layout |
| Wide | > 1440px | Content max-width 1440px centered; extra whitespace on sides; no layout changes beyond spacing |

### Touch Targets
- All interactive elements minimum 40px height (buttons, inputs, links)
- Nav links padded to at least 8px on each side for tap targets
- Social icons at 24px with 8px padding minimum
- Newsletter submit button at 36px height (slightly below 40px minimum — note in gaps)

### Collapsing Strategy
- Top nav links collapse to hamburger menu below 744px
- Product grid collapses from 3 columns to 2 at tablet, to 1 at mobile
- Footer columns collapse from 4 to 2 at tablet, to 1 at mobile
- Hero section reduces padding and font size on mobile (display-xl drops to 24px)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted; only button-primary and text-input have confirmed active/focus states
- Error styling for form inputs (validation colors, error messages) not found in extracted data
- Dark mode or high-contrast mode not present on the live site
- Sub-brand or series-specific color palettes (e.g., Tin House Books vs. Tin House Workshop) not distinguishable from extracted data
- The extracted blues (#0600ff, #0b0f5a, #0000ff) may belong to social media icons, Klarna/Afterpay widgets, or stock photography — not confirmed as brand colors
- Font weights beyond 500 not confirmed in extracted CSS; display sizes may use lighter weights than assumed
- Newsletter submit button at 36px height may be below the 40px touch target minimum — needs verification
- Animation and transition durations not extracted (hover fades, menu animations, etc.)
- Box-shadow values for cards not extracted; described as "subtle" but no specific token available
