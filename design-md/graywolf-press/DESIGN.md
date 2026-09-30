---
version: alpha
name: "Graywolf Press"
source_url: "https://www.graywolfpress.org"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A literary publisher whose visual identity is built on the tension between a dark, almost charcoal ink (#2e2a25) and a startlingly bright electric blue (#000cee) that appears in navigation links and accent elements, suggesting a house that values both gravitas and intellectual electricity. The palette is unusually rich for a small press — alongside the core dark and blue sit a cautionary red (#f7333f) used sparingly for sale or alert badges, a warm marigold (#efb61b) that surfaces in promotional callouts, and a deep navy (#064771) that provides a secondary dark anchor. The typography relies on Freight Sans Pro and Freight Text Pro, a pairing that gives the brand a serious, literary-modernist feel — the sans for navigation and headers, the serif for long-form body copy. White space is generous: margins feel wide, and the canvas (#ffffff) dominates, letting the dark ink and blue accents carry the weight. Buttons and cards use soft radii ({rounded.md}), avoiding both the severe square and the overly friendly pill. The overall impression is of a publisher that trusts its authors' words to do the work — the design is a quiet, confident frame, not a competing voice.

colors:
  primary: "#000cee"
  primary-active: "#000bd5"
  primary-disabled: "#c8c8c8"
  ink: "#2e2a25"
  body: "#222222"
  muted: "#6a7076"
  muted-soft: "#b3b2b3"
  hairline: "#cececc"
  hairline-soft: "#e5e5e3"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#f7333f"
  accent-marigold: "#efb61b"
  accent-navy: "#064771"
  accent-green: "#01a14b"
  accent-sky: "#5bbad5"
  accent-terracotta: "#c84700"
  accent-warm-gray: "#6f625a"

typography:
  display-xl:
    fontFamily: "'freight-text-pro', Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'freight-text-pro', Georgia, 'Times New Roman', serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'freight-text-pro', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'freight-sans-pro', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'freight-sans-pro', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'freight-sans-pro', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'freight-sans-pro', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'freight-text-pro', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'freight-text-pro', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'freight-text-pro', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'freight-sans-pro', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'freight-sans-pro', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.15px
  button-md:
    fontFamily: "'freight-sans-pro', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'freight-sans-pro', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
  link:
    fontFamily: "'freight-sans-pro', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'freight-sans-pro', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'freight-sans-pro', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    border: "2px solid {colors.hairline}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(46, 42, 37, 0.08)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    height: 44px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-lg}"
    padding: "{spacing.lg} 0"
    borderBottom: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the electric blue {colors.primary} (#000cee) and white text. Used for key actions like "Add to Cart", "Subscribe", or "Browse Books". On hover, shifts to {colors.primary-active} (#000bd5). Disabled state uses {colors.primary-disabled} (#c8c8c8) with white text, signaling the action is unavailable. Height is 44px with {rounded.sm} corners — substantial but not heavy.

**`button-secondary`** — An outlined alternative with a white fill, {colors.ink} text, and a 2px {colors.hairline} border. Used for "Learn More" or "View Details" actions alongside primary buttons. Active state darkens the border to {colors.ink} and fills with {colors.surface-soft}. Padding is slightly reduced (10px 22px) to account for the border.

**`button-tertiary-text`** — A text-only button with no background or border, using {colors.primary} for the text. Used for inline actions like "Cancel" or "Clear filters". Minimal footprint, relies on the blue to signal interactivity.

**`button-accent-red`** — A smaller, compact button using {colors.accent-red} (#f7333f) for urgent or promotional actions like "Sale" or "Limited Time". Uses {typography.button-sm} at 36px height, making it suitable for badge-like placements.

### Cards
**`product-card`** — The standard book listing card, white with a 1px {colors.hairline-soft} border and {rounded.md} corners. Contains a book cover image (top corners rounded, bottom flush), title, author, price, and optional badges. On hover, gains a subtle shadow (0 4px 12px rgba(46, 42, 37, 0.08)) and a slightly stronger border.

**`product-card-badge`** — A small marigold badge ({colors.accent-marigold}, #efb61b) overlaid on the card image for promotions like "Staff Pick" or "Featured". Uses {typography.badge} with tight padding and {rounded.xs} corners. Text is {colors.ink} for contrast against the yellow.

### Navigation
**`nav-bar`** — A fixed-height (72px) white bar with a subtle bottom border ({colors.hairline-soft}). Contains the logo, nav links, and a search icon. Links use {typography.nav-link} — uppercase, 14px, weight 600 — for a clean, editorial feel.

**`nav-link-active`** — The active page indicator: text turns {colors.primary} and a 2px bottom border in the same blue appears. No background fill — the underline is the only signal, keeping the nav clean.

**`nav-link-inactive`** — Default link state in {colors.muted} (#6a7076), providing a clear hierarchy against the active link.

### Forms
**`text-input`** — Standard text input with a white background, {colors.body} text, 1px {colors.hairline} border, and {rounded.sm} corners. Padding is generous (12px 16px) at 48px height. Focus state gains a 2px {colors.primary} border with no outline. Error state swaps to a 2px {colors.accent-red} border.

### Search
**`search-bar`** — A pill-shaped search input ({rounded.full}) with a 1px {colors.hairline} border. Used in the header for site-wide search. Height is 44px with comfortable padding (10px 20px). The rounded shape contrasts with the otherwise squared-off design system, giving search a friendly, approachable feel.

### Hero
**`hero-section`** — A full-width section with {colors.surface-soft} background, used for featured books or announcements. Contains a large serif headline ({typography.display-xl}) and a primary CTA button. Padding is {spacing.section} (64px) vertically and {spacing.xl} (32px) horizontally.

**`hero-cta`** — A larger variant of the primary button (48px height, 14px 32px padding) specifically for hero sections. Same {colors.primary} fill and white text, but with more presence to anchor the hero layout.

### Footer
**`footer-section`** — A dark footer using {colors.ink} (#2e2a25) as background, with white text. Contains links, newsletter signup, and copyright. Links default to {colors.muted-soft} (#b3b2b3) and lighten to white on hover.

**`footer-link`** — Footer navigation links in {colors.muted-soft} with {typography.link} sizing. Hover state transitions to {colors.canvas} for clear interaction feedback.

### Badges
**`badge-sale`** — A red badge ({colors.accent-red}) with white text, used to indicate discounted books. Compact at 4px 8px padding with {rounded.xs} corners.

**`badge-new`** — A green badge ({colors.accent-green}, #01a14b) with white text, used for new releases or recent arrivals. Same sizing and shape as the sale badge.

### Dividers
**`divider`** — A 1px horizontal rule in {colors.hairline-soft}, used to separate sections within a page. Minimal and unobtrusive.

### Section Headers
**`section-header`** — A section title in {typography.title-lg} with a bottom border ({colors.hairline-soft}). Used to introduce book categories, author series, or news sections. Padding is {spacing.lg} (24px) above and below the text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero padding reduces to {spacing.xl}; footer links stack; search bar moves to overlay |
| Tablet | 744–1128px | Two-column grid for product cards; nav links remain visible but reduce font size; hero uses {typography.display-lg}; footer columns at 2 |
| Desktop | 1128–1440px | Three-column product grid; full nav with uppercase links; hero at full {typography.display-xl}; footer at 4 columns |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid expands to 4 columns; hero uses larger padding |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Nav links on mobile have 48px tap targets within the hamburger menu
- Search bar remains 44px tall on all breakpoints
- Product card touch area includes the entire card surface

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; the menu overlay covers the full viewport with a white background
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 to 2 to 1 as viewport shrinks
- Hero section reduces vertical padding from {spacing.section} to {spacing.xl} on mobile
- Search bar becomes a full-width overlay on mobile, triggered by a magnifying glass icon in the nav

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for most components could not be reliably extracted from the live site; the values above are inferred from common patterns and the brand's color palette
- Error styling for forms (validation messages, error icons) is not available; the text-input error border is an assumption based on the accent-red color
- Dark mode is not present on the live site; no dark theme tokens are defined
- Sub-brand or series-specific color palettes (e.g., for Graywolf's "Art of the Novella" series) were not extractable
- The exact font weights and sizes for Freight Sans Pro and Freight Text Pro are approximated from the extracted font-family declarations and typical usage; the live site may use different weights
- Spacing values (padding, margins) are estimated from visual inspection and common design system patterns; they may not match the live site exactly
- The `product-card-hover` shadow values are an educated guess; the live site may use different shadow parameters
- No animation or transition timing data was extractable (ease curves, durations)
- The `button-tertiary-text` hover state (underline or color shift) is not documented
- Accessibility contrast ratios for some color combinations (e.g., accent-marigold on white) have not been verified against WCAG standards
- The extracted hex list includes many colors that may be from third-party widgets or images; the primary palette above is a best-guess selection of the most brand-relevant colors
