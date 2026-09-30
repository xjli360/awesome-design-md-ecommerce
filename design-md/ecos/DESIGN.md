---
version: alpha
name: "Ecos"
source_url: "https://ecos.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A cleaning brand that wears its chemistry on its sleeve, Ecos builds its visual identity around a deep teal (#00587c) that reads more like a tidepool than a corporate blue, paired with a sharp cyan (#00afd7) that acts as the system's voltage — appearing on buttons, badges, and the occasional headline accent. The palette is unexpectedly broad for a cleaning brand: a warm peach (#fa9b57), a muted coral (#f7763f), and a series of pinks (#e34876, #dc327c, #c73390) that suggest the brand is comfortable with color as a wayfinding tool across product categories rather than relying on the expected green-and-white "eco" cliché. Typography leans on GT Walsheim across weights (Light, Regular, Medium, Bold) for a clean, slightly geometric sans that feels both modern and approachable, with Avenir Next and Open Sans as fallbacks. The canvas is a warm off-white (#fef6ef) rather than pure white, giving the site a softer, more tactile feel than the typical cleaning aisle. Rounded corners appear consistently — buttons and cards use {rounded.sm} to {rounded.md}, while badges and pills go to {rounded.full} — creating a friendly, non-industrial surface language. The brand's secondary palette includes a chartreuse (#cedc00) that appears in sustainability badges and callout boxes, and a deep navy (#141b38) used for footer backgrounds and heavy text, creating a clear hierarchy between the warm canvas and the cool, aquatic primary tones.

colors:
  primary: "#00587c"
  primary-active: "#004d77"
  primary-disabled: "#c3e7f4"
  ink: "#141b38"
  body: "#1c1c1a"
  muted: "#434960"
  muted-soft: "#6a6a6a"
  hairline: "#dcdde1"
  hairline-soft: "#e8e8eb"
  canvas: "#fef6ef"
  surface-soft: "#f9f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#00afd7"
  accent-peach: "#fa9b57"
  accent-coral: "#f7763f"
  accent-pink: "#e34876"
  accent-chartreuse: "#cedc00"
  badge-green: "#0093bf"
  badge-pink: "#dc327c"
  badge-purple: "#c73390"
  error: "#af2121"
  error-soft: "#841919"

typography:
  display-xl:
    fontFamily: "'GT Walsheim Bold', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GT Walsheim Bold', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT Walsheim Medium', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'GT Walsheim Medium', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'GT Walsheim Regular', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'GT Walsheim Regular', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT Walsheim Regular', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'GT Walsheim Regular', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "'GT Walsheim Medium', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'GT Walsheim Medium', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'GT Walsheim Medium', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'GT Walsheim Medium', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  link:
    fontFamily: "'GT Walsheim Regular', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'GT Walsheim Medium', 'Avenir Next', 'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.27
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-peach:
    backgroundColor: "{colors.accent-peach}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-accent:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  badge-certification:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-category:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  accordion:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  accordion-active:
    backgroundColor: "{colors.surface-card}"
    borderLeft: "3px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the deep teal {colors.primary} with white text. On hover, it shifts to {colors.primary-active} for a subtle darkening effect. Disabled state uses {colors.primary-disabled} with muted text, signaling the button is non-interactive. The {rounded.sm} corners keep the button friendly without being overly pill-shaped for standard CTAs.

**`button-secondary`** — An outlined variant with a transparent background and a 2px solid border in {colors.primary}. Used for secondary actions like "Learn More" or "View All" alongside primary buttons. The canvas background ensures it sits well on any surface.

**`button-accent-cyan`** — A high-energy alternative to the primary button, using {colors.accent-cyan} as background. Appears in promotional sections, category landing pages, and seasonal campaigns where the brand wants to signal freshness rather than authority.

**`button-accent-peach`** — A warm, approachable variant using {colors.accent-peach} with dark text. Used sparingly for special offers or limited-time calls to action, creating visual contrast against the cooler primary palette.

**`button-pill-primary`** and **`button-pill-accent`** — Fully rounded pill buttons used for subscription CTAs, newsletter signups, and mobile navigation. The {rounded.full} shape makes them feel more casual and conversational than the standard buttons.

### Cards
**`product-card`** — The standard product display card with a white surface, {rounded.md} corners, and 16px internal padding. On hover, a subtle box shadow elevates the card, creating depth without animation. The card contains product imagery, title, price, and a badge for certifications or category.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a warm off-white {colors.canvas} background. Navigation links use {typography.nav-link} at 15px with 0.2px letter spacing for readability. Active links are underlined with a 2px {colors.primary} border.

**`search-bar`** — A fully rounded search input with a white card background and subtle border. The {rounded.full} treatment makes it feel more like a discovery tool than a utility, consistent with the brand's friendly tone.

### Badges
**`badge-certification`** — Uses the chartreuse {colors.accent-chartreuse} to signal eco-certifications, sustainability claims, or third-party verifications. The uppercase, tightly tracked typography and full rounding make these badges feel like stamps of approval.

**`badge-category`** — Cyan badges for product category labels (e.g., "Laundry", "Dish", "Surface"). The cool tone differentiates category from certification without competing with the primary palette.

**`badge-sale`** — Coral badges for promotional pricing or limited-time offers. The warm accent draws immediate attention against the cooler product card backgrounds.

### Forms
**`text-input`** — Standard text inputs with a white background, 48px height, and {rounded.sm} corners. Focus state gains a 2px {colors.primary} border for clear interaction feedback. Error state uses a 2px {colors.error} border with {colors.error-soft} background tint.

### Footer
**`footer`** — A dark navy {colors.ink} footer section with white text. Links use {colors.muted-soft} for a lower visual weight, maintaining hierarchy against headings. The footer includes accordion-style sections on mobile for space efficiency.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger nav, stacked product cards, full-width hero, accordion footer |
| Tablet | 744–1128px | Two-column product grid, expanded nav with dropdowns, side-by-side hero content |
| Desktop | 1128–1440px | Three-column product grid, full top nav visible, multi-column footer, search bar in nav |
| Wide | > 1440px | Max-width container at 1440px, centered content, larger typography on display-xl |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Search bar and nav links have 48px minimum touch target
- Badges and certification labels are minimum 24px height with adequate padding
- Accordion headers have 48px touch target on mobile

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Multi-column footer collapses to accordion sections below 744px
- Product grid reduces from 3 columns to 2 at tablet, to 1 at mobile
- Hero section stacks vertically below 744px, with text above imagery
- Search bar collapses from inline to expandable icon below 744px
- Category navigation strip becomes horizontal scrollable on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted from static analysis; active states for buttons and links are inferred from common patterns
- Error state styling for forms (background tint, icon placement) is assumed based on standard accessibility patterns
- Dark mode styling is not present on the live site and has not been defined
- Sub-brand or product-line-specific palette variations (e.g., for ECOS Pro or ECOS for Business) could not be extracted
- Animation and transition timing values (durations, easing curves) are not available from the extracted data
- The exact font stack order for GT Walsheim weights is inferred; the live site may use different fallback ordering
- Iconography style (line vs. filled, stroke weights) could not be determined from the extracted data
- The extracted color list includes several pinks and purples that may belong to third-party widgets or promotional campaigns rather than the core brand palette; these have been included as accent tokens but should be validated against brand guidelines
- Spacing values are standardized tokens; actual component spacing may vary by context and should be verified against live screenshots
