---
version: alpha
name: "Canyon"
source_url: "https://www.canyon.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A performance cycling brand that uses a near-black (#222222) as its primary anchor — not a vibrant brand color — letting the product photography and a single red accent (#e20000) carry all the emotional weight. The palette is overwhelmingly monochromatic: four grays (#d8d8d8, #767676, #4c4c4c, #f2f2f2) build a strict hierarchy of surfaces and text, while the red appears only on sale badges, error states, and the occasional high-voltage CTA. This is a system designed for a global catalog of carbon-fiber frames and precision components — the typography runs CanyonWeb, a proprietary sans-serif, at moderate weights and sizes that prioritize readability over personality. Buttons are sharp-cornered rectangles (`{rounded.none}`) with tight padding, communicating mechanical precision rather than friendliness. The brand's secondary palette is unusually broad — extracted from the live site are 20+ colors including a bright cyan (#2cbcff), a safety orange (#ff6b00), a deep teal (#167f45), and several pastels (#fbfec0, #f9d7d4, #ffe8c2) — but these are almost certainly product-category badges, country-specific flags, or stock-image dominant tones rather than core brand tokens. The true Canyon interface is a study in restraint: a dark header, a white canvas, and the occasional red pulse to signal urgency.

colors:
  primary: "#222222"
  primary-active: "#000000"
  primary-disabled: "#767676"
  ink: "#222222"
  body: "#4c4c4c"
  muted: "#767676"
  muted-soft: "#d8d8d8"
  hairline: "#d8d8d8"
  hairline-soft: "#f2f2f2"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#e20000"
  accent-red-hover: "#cc0000"
  accent-cyan: "#2cbcff"
  accent-orange: "#ff6b00"
  accent-green: "#167f45"
  accent-yellow: "#ffe500"

typography:
  display-xl:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'CanyonWeb', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.primary-active}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-accent-red-hover:
    backgroundColor: "{colors.accent-red-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-card-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  hero-section-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  footer-link-hover:
    color: "{colors.muted-soft}"
  badge-count:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: 0 6px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Configure," and checkout flows. Rendered as a solid near-black rectangle with white uppercase text. On hover, shifts to full black (`{colors.primary-active}`). Disabled state uses `{colors.primary-disabled}` (#767676) with white text — no opacity overlay. The `button-accent-red` variant is reserved for sale-driven CTAs and limited-time offers, using `{colors.accent-red}` (#e20000) as background. **`button-secondary`** — An outlined variant with a 2px solid border on a white background. Used for "Learn More" and secondary product actions. Active state fills the background with `{colors.surface-soft}` (#f2f2f2). **`button-tertiary-text`** — A text-only link button with no border or background, used for "View Details" and inline navigation within product cards.

### Product Cards
**`product-card`** — The core product display unit, a sharp-cornered white card with no border or shadow by default. On hover, a subtle box-shadow lifts the card. The title uses `{typography.title-sm}` in `{colors.ink}`, the price uses `{typography.body-md}` in `{colors.body}` (#4c4c4c). Badges are positioned at the top-left of the card image: sale badges use `{colors.accent-red}`, new badges use `{colors.accent-cyan}` (#2cbcff), and sold-out badges use `{colors.muted}` (#767676). All badges are uppercase 11px with tight padding and no rounding — consistent with the brand's mechanical aesthetic.

### Navigation
**`nav-bar`** — A fixed 56px dark bar (`{colors.primary}`) at the top of the page. Navigation links are uppercase 14px in white with 16px horizontal padding. The active link is underlined with a 2px white border. On scroll, the nav bar transitions to a white background with dark text — `{colors.ink}` for links, no underline for active state. The mobile nav collapses into a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — Standard form inputs use a white background with a 1px `{colors.hairline}` (#d8d8d8) border and 4px rounding (`{rounded.sm}`). On focus, the border thickens to 2px `{colors.primary}` (#222222). Error states switch to a 2px `{colors.accent-red}` (#e20000) border. Input height is 48px with 12px vertical and 16px horizontal padding.

### Search
**`search-bar`** — The site search input mirrors the text-input style: white background, 1px hairline border, 4px rounding. On focus, the border becomes 2px `{colors.primary}`. No pill shape — consistent with the brand's preference for sharp corners. The search icon is positioned inside the input on the left.

### Footer
**`footer`** — A dark footer (`{colors.primary}`) with white text in `{typography.body-sm}`. Links are 14px regular weight, turning to `{colors.muted-soft}` (#d8d8d8) on hover. The footer is divided into columns for product categories, support, company info, and legal. Social media icons appear in the bottom row, using their respective brand colors (extracted from the palette: #2cbcff for Twitter/X, #167f45 for WhatsApp, etc.).

### Badges
**`badge-count`** — A small circular badge used for cart item counts and notification numbers. Uses `{colors.accent-red}` background with white text, 20px height, and full rounding. The badge is positioned absolutely relative to its parent icon.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), nav collapses to hamburger, hero padding reduces to 32px, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav links visible but truncated (top 4 categories only), hero padding at 48px |
| Desktop | 1128–1440px | Three-column product grid, full nav with all categories, hero padding at 64px, sidebar filters visible on category pages |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero content max-width at 1200px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets are the entire card surface, not just the title/price
- Nav links have 44px minimum tap area even when text is smaller
- Filter checkboxes and radio buttons are 24px × 24px minimum

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product filters collapse into a "Filter" button that opens a slide-out panel below 744px
- Footer columns collapse to a single vertical stack below 744px, with accordion-style expandable sections
- Hero section reduces image height by 40% on mobile, with text overlay repositioned to bottom
- Product image galleries switch from thumbnail grid to horizontal swipe dots on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette includes 20+ colors that are likely product-category badges, country-specific flags, or stock-image dominant tones — the true brand palette is probably 6-8 colors centered on black, white, gray, and red. The secondary colors (cyan, orange, teal, yellow, pastels) should be validated against the brand's actual design tokens.
- Font sizes and weights are estimated based on common cycling industry standards and the extracted font-family declarations — actual type scale may differ in the live site's CSS.
- Hover and focus states for most components are inferred from common patterns — actual implementations may use different colors, transitions, or effects.
- Error state styling for forms (beyond border color) is not extracted — error message text color, icon placement, and animation are unknown.
- Dark mode is not supported or extracted — the site appears to be light-mode only.
- The `CanyonWeb` font family may have multiple weights (300, 400, 500, 600, 700) — only the most common weights are listed here.
- Button padding values (12px 24px) are estimated — actual padding may vary by button size variant.
- Product card shadow values (0 4px 12px) are estimated — actual box-shadow may use different spread or opacity.
- The nav-bar scroll transition timing and easing are unknown.
- Sub-brand or regional color variations (e.g., Canyon US vs Canyon JP) are not captured.
