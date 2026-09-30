---
version: alpha
name: "Leder Games"
source_url: "https://ledergames.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A board-game publisher that builds its visual identity around the deep, almost-black #231f20 — a near-ink that reads as charcoal rather than true black, giving the brand a grounded, slightly warm seriousness. This primary color appears on the site header, footer, and primary buttons, while the accent palette draws from the games themselves: a muted sage #7396a2, a forest green #116633, and a restrained red #ed1b2f that never screams. The site uses a clean white canvas (#ffffff) with soft gray surfaces (#f3f3f3, #f6f6f6) and hairline borders (#dedede, #dbdbdb) to create a calm, editorial backdrop for game art. Typography defaults to Arial and Helvetica Neue — a pragmatic, no-nonsense choice that prioritizes readability over personality, letting the elaborate game illustrations and iconography carry the emotional weight. Buttons are softly rounded ({rounded.sm}) with generous padding, and product cards use subtle shadows on white surfaces ({surface-card: #ffffff}). The overall mood is that of a serious game studio — confident in its craft, unafraid of dark backgrounds, and trusting that the fantastical worlds of Root, Oath, and Arcs need no decorative chrome from the UI.

colors:
  primary: "#231f20"
  primary-active: "#444444"
  primary-disabled: "#9a9a9a"
  ink: "#231f20"
  body: "#444444"
  muted: "#7d7d7d"
  muted-soft: "#9a9a9a"
  hairline: "#dedede"
  hairline-soft: "#ededed"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  surface-strong: "#f6f6f6"
  on-primary: "#ffffff"
  accent-sage: "#7396a2"
  accent-forest: "#116633"
  accent-red: "#ed1b2f"
  accent-red-active: "#ea2137"
  accent-deep-teal: "#5487a0"
  accent-terracotta: "#de4c39"
  badge-green: "#ddf6cf"
  badge-green-text: "#116633"
  badge-green-border: "#a9d092"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-accent-sage:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-red-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.on-primary}"
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
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.none}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    borderBottom: "2px solid {colors.primary}"
  logo-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.display-sm}"
    padding: "8px 0"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.06)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.badge-green-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    border: "1px solid {colors.badge-green-border}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: 400px
  hero-section-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: 360px
  hero-section-accent:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
    minHeight: 360px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.base} 0"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-sage}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "2px solid {colors.primary}"
  badge-default:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-success:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.badge-green-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    border: "1px solid {colors.badge-green-border}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  game-detail-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xl} {spacing.lg}"
  game-detail-meta:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  game-detail-description:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    lineHeight: 1.6
  social-icon-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  social-icon-link-hover:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px

## Components

### Buttons
**`button-primary`** — The workhorse CTA, filled with the brand's near-black {colors.primary} (#231f20) and white text. Uses {rounded.sm} (8px) corners and {typography.button-md} (15px, weight 600, 0.3px letter-spacing). On hover, the background shifts to {colors.primary-active} (#444444) for a subtle lift. Disabled state uses {colors.primary-disabled} (#9a9a9a) to signal inactivity without confusion.

**`button-secondary`** — An outlined variant with a white fill, {colors.primary} text, and a 2px solid border matching the text color. On hover, the background fills with {colors.surface-soft} (#f3f3f3) for a gentle pressed effect. Ideal for "Learn More" or "View Details" actions alongside primary buttons.

**`button-accent-sage`** — A secondary accent button using the brand's sage green {colors.accent-sage} (#7396a2). Used for game-specific calls to action or category filters. Maintains the same sizing and corner radius as the primary button for visual consistency.

**`button-accent-red`** — A high-energy accent button in {colors.accent-red} (#ed1b2f), reserved for urgent actions like "Pre-order Now" or "Limited Stock." Active state shifts to {colors.accent-red-active} (#ea2137). Use sparingly to preserve its signal value.

**`button-ghost`** — A text-only button with no background or border. Uses {colors.primary} text and the same typography as other buttons. On hover, the text may darken slightly or an underline may appear. Used for dismissible actions like "Cancel" or "Close."

### Cards
**`product-card`** — A white card ({colors.surface-card}) with a subtle box shadow (0 1px 3px rgba(0,0,0,0.08)) and {rounded.md} (12px) corners. Contains a square aspect-ratio image at the top with rounded top corners, followed by the product title in {typography.title-sm} and price in {typography.body-md}. On hover, the shadow deepens (0 4px 12px rgba(0,0,0,0.1)) for a gentle lift effect.

**`product-card-badge`** — A small green badge positioned over the product image, using {colors.badge-green} (#ddf6cf) background, {colors.badge-green-text} (#116633) text, and a {colors.badge-green-border} (#a9d092) border. Uses {typography.badge} (11px, weight 700, uppercase) with {rounded.xs} (4px) corners. Typically reads "NEW" or "IN STOCK."

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 64px height on a white background ({colors.canvas}). Uses a 1px bottom border in {colors.hairline} (#dedede). On scroll, the height reduces to 56px and a subtle box shadow appears. Navigation links use {typography.nav-link} (14px, weight 600, uppercase, 0.2px letter-spacing) for a clean, authoritative feel.

**`nav-link`** — Individual navigation items with 8px vertical and 16px horizontal padding. The active state adds a 2px bottom border in {colors.primary} to indicate the current section. Inactive links use {colors.ink} (#231f20) text.

**`logo-link`** — The brand logo or wordmark, using {typography.display-sm} (20px, weight 600) in {colors.primary}. Typically positioned at the far left of the nav bar. On the home page or game detail pages, the logo may link back to the root.

### Forms
**`text-input`** — A standard text input field with a white background, 1px {colors.hairline} border, {rounded.sm} (8px) corners, and 12px/16px padding. On focus, the border thickens to 2px and switches to {colors.primary} for clear visual feedback. Error state uses a 2px {colors.accent-red} border.

**`select-input`** — A dropdown select element matching the text input's visual style. Uses the same background, border, corner radius, and typography. The dropdown arrow may be a custom SVG in {colors.muted} (#7d7d7d).

**`textarea`** — A multi-line text input with the same styling as `text-input` but without a fixed height. Used for contact forms or game submission details.

### Hero Sections
**`hero-section`** — A full-width hero banner with a {colors.primary} (#231f20) background and white text. Uses {typography.display-xl} (32px, weight 700) for the headline, with generous padding ({spacing.xxl} vertical, {spacing.lg} horizontal). Minimum height of 400px. May include a background image or pattern overlay at low opacity.

**`hero-section-light`** — A lighter variant with a {colors.surface-soft} (#f3f3f3) background and {colors.ink} text. Used for secondary pages or content sections where a dark hero would be too heavy. Minimum height of 360px.

**`hero-section-accent`** — An accent variant using {colors.accent-sage} (#7396a2) as the background. Used for game-specific landing pages or seasonal promotions. White text maintains readability against the muted green.

### Footer
**`footer`** — A full-width footer with a {colors.primary} (#231f20) background and white text. Uses {typography.body-sm} (14px) for general content and {typography.link} (14px) for navigation links. Links shift to {colors.accent-sage} on hover for a subtle color pop against the dark background. Social icon links use a 36px circular button that fills with {colors.accent-sage} on hover.

**`social-icon-link`** — A 36px circular icon button with transparent background and white icon color. On hover, the background fills with {colors.accent-sage} (#7396a2) for a subtle, brand-appropriate highlight. Uses {rounded.full} for the perfect circle.

### Badges & Dividers
**`badge-default`** — A neutral badge with a {colors.surface-soft} background and {colors.muted} text. Used for general labels like "Category" or "Filter."

**`badge-success`** — A green badge for positive status indicators. Uses {colors.badge-green} background, {colors.badge-green-text} text, and a {colors.badge-green-border} border. Typically reads "IN STOCK" or "AVAILABLE."

**`badge-sale`** — A red badge for sale or promotion indicators. Uses {colors.accent-red} background with white text. Reserved for high-visibility discount or limited-time offers.

**`divider`** — A 1px horizontal line in {colors.hairline} (#dedede). Used between sections or content blocks. A softer variant (`divider-soft`) uses {colors.hairline-soft} (#ededed) for less visual weight.

### Accordion
**`accordion-header`** — A clickable header row with a white background, {colors.ink} text in {typography.title-sm} (16px, weight 600), and a 1px top border in {colors.hairline}. Padding of 16px on all sides. On click, the associated `accordion-content` expands below.

**`accordion-content`** — The expandable content area below an accordion header. Uses {typography.body-md} (16px) for readability, with padding of 0 on top and 16px on the bottom and sides. Content may include paragraphs, lists, or images.

### Game Detail
**`game-detail-header`** — A dark header section specific to individual game pages. Uses {colors.primary} background with white text in {typography.display-lg} (28px, weight 700). Padding of {spacing.xl} vertical and {spacing.lg} horizontal. Typically contains the game title, subtitle, and a brief tagline.

**`game-detail-meta`** — Metadata below the game header, such as player count, play time, and age range. Uses {typography.body-sm} (14px) in {colors.muted} (#7d7d7d) for a secondary, informational appearance.

**`game-detail-description`** — The main body text for a game's description. Uses {typography.body-md} (16px) in {colors.body} (#444444) with an increased line-height of 1.6 for readability. May include inline links, bold text, or bullet points.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; hero sections reduce min-height to 280px; product cards stack in single column; footer links stack vertically; game detail header reduces font size to {typography.display-md}; accordions become full-width with no side padding |
| Tablet | 744–1128px | Nav bar shows 4-5 links with "More" dropdown; hero sections at 360px min-height; product cards in 2-column grid; footer links in 2 columns; game detail header uses {typography.display-lg} |
| Desktop | 1128–1440px | Full nav bar with all links visible; hero sections at 400px min-height; product cards in 3-column grid; footer links in 3 columns; game detail header at full size with optional background image |
| Wide | > 1440px | Max-width container at 1440px; hero sections may extend full viewport width with content centered; product cards in 4-column grid; additional whitespace around content; footer links in 4 columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px on mobile and tablet
- Nav bar hamburger icon is 48x48px for easy tapping
- Accordion headers are 48px minimum height for touch interaction
- Social icon links are 36x36px with 4px padding for a 44x44px effective touch target
- Product card CTAs are at least 44px tall

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-in drawer from the left
- Product card grids collapse from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer link columns collapse from 4 to 3 to 2 to 1 as viewport narrows
- Hero section content stacks vertically on mobile, with the image or illustration moving below the text
- Game detail metadata moves from a horizontal row to a vertical stack on mobile
- Accordion behavior is consistent across all breakpoints, with no additional collapsing needed
- Search bar may collapse to an icon-only button on mobile, expanding to full width on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for most components could not be reliably extracted from static CSS. The hover behaviors described above are inferred from common patterns and the brand's visual language, but exact color shifts, shadow changes, and transition durations are unconfirmed.
- **Error and validation styling** for forms is inferred from the extracted accent-red (#ed1b2f) and standard web patterns. Specific error message typography, iconography, and animation are unknown.
- **Dark mode** is not present on the live site. No dark mode colors or behaviors could be extracted.
- **Sub-brand palettes** for individual games (Root, Oath, Arcs, etc.) are not reflected in the site's global CSS. Each game likely has its own distinct color scheme that overrides the system palette on game-specific pages.
- **Typography scale** is inferred from common Arial/Helvetica Neue usage and typical editorial sizing. The exact font sizes, weights, and line heights for every token (e.g., display-2xl, caption-sm variants) are not confirmed from the live site.
- **Animation and transition** durations, easing functions, and micro-interactions (e.g., button press, card hover lift, nav bar scroll) are not documented in the extracted data. Standard 150-300ms ease-in-out transitions are assumed.
- **Checkout and cart** components (Shopify-powered) use their own default styling that may differ from the brand's design system. The extracted hex list includes several Shopify-specific colors (#008060, #de3618, #197bbd) that are not part of the brand's primary palette.
- **Iconography** style and sizing are not documented. The brand likely uses custom game-themed icons, but no icon system could be extracted.
- **Loading states** (skeleton screens, spinners) are not present in the extracted data. Standard Shopify loading patterns may apply.
