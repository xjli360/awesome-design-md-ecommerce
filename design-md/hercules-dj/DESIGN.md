---
version: alpha
name: "Hercules DJ"
source_url: "https://www.hercules.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-voltage red (#c20e1a) cuts through a near-black (#202020) and charcoal (#3e3e3e) canvas, announcing that this is DJ hardware first and software second — the brand wears its pro-audio heritage in every saturated accent. That red, paired with a magenta shock (#f70f5d) and an amber pulse (#f0d039), creates a three-stop traffic light of urgency: red for record, amber for cue, magenta for effect. The typography stack defaults to system sans (Arial, Helvetica, Segoe UI) — no custom typeface, which suggests the brand prioritizes loading speed and cross-platform legibility over typographic personality. Buttons carry {rounded.sm} corners — not pill-shaped, not square — a deliberate middle ground that feels industrial without being hostile. The product grid uses generous {spacing.lg} gutters and {rounded.md} cards on a white (#ffffff) or near-white (#f9f9f9) surface, letting the gear photography do the selling. A secondary blue (#0078d4) appears in utility links and info badges, while green (#00d084) marks "in stock" states. The overall mood is club-ready but not flashy — the reds are the headliners, the grays are the stage crew, and the gold (#c49c48) is reserved for limited-edition or pro-series callouts.

colors:
  primary: "#c20e1a"
  primary-active: "#a00c15"
  primary-disabled: "#f0a0a6"
  ink: "#202020"
  body: "#3e3e3e"
  muted: "#4d4d4d"
  muted-soft: "#6a6a6a"
  hairline: "#d0d0d7"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  surface-strong: "#efefef"
  on-primary: "#ffffff"
  accent-magenta: "#f70f5d"
  accent-amber: "#f0d039"
  accent-gold: "#c49c48"
  accent-blue: "#0078d4"
  accent-green: "#00d084"
  accent-purple: "#7030a0"
  scrim: "#0a0a0a"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
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
    padding: 12px 24px
    height: 44px
  button-accent-magenta:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 48px 24px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Buy Now," and "Find Your Gear" flows. Filled with the brand red {colors.primary} and white text, it sits on a {rounded.sm} container with 12px vertical padding. On hover, it shifts to {colors.primary-active} (#a00c15); disabled state uses {colors.primary-disabled} (#f0a0a6) to indicate inactivity without losing brand recognition.

**`button-secondary`** — An outlined or ghost variant for secondary actions like "Compare" or "Learn More." White background with {colors.ink} text, preserving the same {rounded.sm} and 44px height as the primary button so they can sit side by side in toolbars. Hover adds a thin {colors.hairline} border.

**`button-accent-magenta`** — Reserved for high-energy actions tied to DJ software downloads, effect packs, or limited-time offers. Uses {colors.accent-magenta} (#f70f5d) as fill, creating a deliberate visual break from the red-primary system. Same dimensions as `button-primary` for layout consistency.

**`button-ghost`** — A text-only button with no background, used in navigation dropdowns and filter bars. Text color is {colors.primary} with underline on hover. Maintains the 44px height for alignment with sibling buttons.

### Cards
**`product-card`** — The primary content container for DJ gear listings. A white card on {colors.surface-soft} (#f9f9f9) background with {rounded.md} corners and {spacing.base} internal padding. The product image fills the top with {rounded.md} applied to the image container. Title uses {typography.title-sm} in {colors.ink}, price uses {typography.body-md} in {colors.primary}. Badges (new, sale, stock) overlay the top-right corner of the image area.

### Navigation
**`nav-bar`** — A fixed-height (64px) top navigation bar on {colors.ink} (#202020) background. Links are white, uppercase, 14px with 0.5px letter-spacing — a club-venue marquee feel. The logo sits left-aligned; primary nav links center; utility icons (search, cart, account) right-aligned. On mobile, the nav collapses into a hamburger menu with a slide-out drawer.

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. White background, {colors.body} text, {rounded.sm} corners, 44px height. Focus state adds a {colors.primary} border ring. Placeholder text uses {colors.muted-soft}.

### Badges
**`badge-new`** — A small amber (#f0d039) pill badge reading "NEW" in uppercase 11px bold. Used on recently launched products and software versions. {rounded.xs} keeps it sharp and technical.
**`badge-sale`** — Red (#c20e1a) badge for discounted items. Same dimensions as `badge-new` but with white text.
**`badge-stock`** — Green (#00d084) badge for "In Stock" indicators. Same sizing, white text.

### Hero
**`hero-banner`** — Full-width promotional section at the top of category and landing pages. Dark background ({colors.ink}) with white display text. Large product imagery bleeds to the edges. CTA buttons sit centered or left-aligned depending on layout. Padding is {spacing.section} (64px) top and bottom.

### Footer
**`footer`** — Site-wide footer on {colors.ink} background. Links are {colors.muted-soft} (#6a6a6a) in {typography.body-sm}. Organized in a 4-column grid on desktop, collapsing to single column on mobile. Includes social icons (Font Awesome brands), newsletter signup, and legal links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero banner reduces padding to 32px; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses 48px padding |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero at 64px padding; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to 4 columns; hero imagery scales up |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility.
- Icon buttons in the nav bar are 44x44px tap targets even if the icon itself is smaller.
- Product card CTAs are at least 44px tall.

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; the slide-out drawer contains all primary links and utility icons.
- Product grid reduces columns from 3 to 2 to 1 as viewport narrows.
- Hero banner text stacks vertically on mobile instead of side-by-side.
- Footer columns collapse to a single vertical list below 744px.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site; the values above are inferred from common patterns.
- Error styling for form inputs (validation colors, error messages) was not observed.
- Dark mode is not present on the live site; no dark palette tokens are defined.
- The extracted hex list includes many generic web colors (e.g., #0073aa, #0693e3, #32373c) that likely come from third-party widgets or stock imagery. The primary palette above selects the most distinctive and frequently occurring values.
- Font weights beyond 400, 600, and 700 are assumed; the live site uses system fonts with limited weight declarations.
- Specific animation durations and easing curves were not extracted.
- Sub-brand palettes (e.g., for DJControl vs. DJUCED software) may exist but were not visible in the extracted data.
