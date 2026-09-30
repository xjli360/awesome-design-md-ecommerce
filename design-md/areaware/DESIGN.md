---
version: alpha
name: "Areaware"
source_url: "https://www.areaware.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A puzzle and design-object brand that uses a warm, almost domestic palette anchored on a butter-yellow #fff299 — a color that reads like afternoon light on a kitchen table, not like a brand primary. The extracted palette is unusually broad for a DTC site: alongside the yellow sit a dusty rose #fcd6d7, a sage green #d3efcd, a deep navy #3a5792, and a cherry red #c72e2f, suggesting Areaware treats color as a product language rather than a system constraint. Buttons and interactive elements take a soft pill shape (`{rounded.full}`), and the canvas is a warm off-white #f5f5f5 rather than pure white, giving the whole experience the feel of a well-loved apartment rather than a sterile gallery. The typography stack is system-native — Helvetica Neue, Arial, sans-serif — which is a deliberate choice: the brand lets the objects and their saturated colors do the talking, not a custom typeface. Product cards use generous whitespace and `{rounded.md}` corners, and the overall mood is one of gentle, curated playfulness — puzzles and home goods presented not as commodities but as objects with personality. The gray #9ca3af appears as a muted secondary text and hairline color, keeping the interface quiet so the product photography and those distinctive accent colors can sing. There is no heavy hero section; instead, the brand leads with a grid of product cards, each one a small invitation.

colors:
  primary: "#fff299"
  primary-active: "#f5e066"
  primary-disabled: "#fdf5cc"
  ink: "#1a1a1a"
  body: "#4a4a4a"
  muted: "#9ca3af"
  muted-soft: "#d1d5db"
  hairline: "#e5e7eb"
  hairline-soft: "#f0f0f0"
  canvas: "#f5f5f5"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#1a1a1a"
  accent-rose: "#fcd6d7"
  accent-sage: "#d3efcd"
  accent-navy: "#3a5792"
  accent-red: "#c72e2f"
  accent-blue: "#7bb1ff"
  accent-green: "#1b9500"

typography:
  display-xl:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
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
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.muted}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-accent-rose:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-accent-sage:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-card}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.04)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
  footer-link-hover:
    color: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  section-title:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.base}"
  filter-tag:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  add-to-cart-bar:
    backgroundColor: "{colors.surface-card}"
    padding: "{spacing.base}"
    borderTop: "1px solid {colors.hairline}"
    position: sticky
    bottom: 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and key conversion points. Rendered as a full-width or inline pill with the brand's signature butter-yellow `{colors.primary}` background. On hover, it shifts to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}` with `{colors.muted}` text to signal inactivity without visual noise. Text is uppercase with tight letter-spacing, giving it a confident, editorial weight.

**`button-secondary`** — A ghost button with a subtle hairline border, used for secondary actions like "View Details" or "Save for Later". Inherits the same pill shape and uppercase typography as the primary, but sits on the `{colors.canvas}` background with `{colors.ink}` text. On hover, the background fills with `{colors.hairline-soft}` and the border darkens to `{colors.muted}`.

**`button-tertiary`** — A text-only button with no background or border, used for low-emphasis actions like "Cancel" or "Clear Filters". Matches the primary button's typography and pill shape but remains transparent until hover, where a subtle background shift could be applied.

**`button-accent-rose` / `button-accent-sage`** — Thematic accent buttons used for limited-edition drops, seasonal collections, or promotional banners. They follow the same pill and uppercase pattern as the primary but swap the yellow for `{colors.accent-rose}` (dusty pink) or `{colors.accent-sage}` (soft green), allowing the brand to color-code campaigns without breaking the system.

### Cards
**`product-card`** — The core content unit of the site, used in grid layouts on the homepage, category pages, and search results. A white `{colors.surface-card}` background with `{rounded.md}` corners and a whisper-thin shadow. The image occupies the top portion with matching rounded top corners and a 1:1 aspect ratio. Below, the product title uses `{typography.title-sm}` and the price uses `{typography.body-sm}` in `{colors.body}`. On hover, the shadow deepens to signal interactivity. No border — the card floats on the `{colors.canvas}` page background.

### Navigation
**`nav-bar`** — A fixed-height top bar at 64px, using `{colors.canvas}` background and `{colors.ink}` text. Navigation links use `{typography.nav-link}` in uppercase with subtle letter-spacing. A thin `{colors.hairline-soft}` bottom border separates it from the page content. When scrolled, a light box-shadow replaces the border for a subtle elevation effect. The logo sits left-aligned, with category links and a search icon on the right.

### Forms
**`text-input`** — Standard input fields for email capture, search, and checkout forms. A white background with `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border becomes a 2px `{colors.primary}` stroke. Error states use a 2px `{colors.accent-red}` border. Height is 48px for comfortable touch targeting.

**`search-bar`** — A pill-shaped search input with `{rounded.full}`, used in the navigation and on search results pages. Same white background and hairline border as the text input, but with a taller pill silhouette. On focus, the border switches to `{colors.primary}`.

### Badges
**`badge-new`** — A small, pill-shaped badge with a sage green `{colors.accent-sage}` background, used to flag newly added products. Uppercase, bold, 11px type.

**`badge-sale`** — A red `{colors.accent-red}` badge with white text, used for discounted items. Same pill shape and typography as the new badge, but with higher urgency.

**`badge-limited`** — A rose `{colors.accent-rose}` badge for limited-edition or low-stock items. Follows the same pattern, adding a third color to the badge system without visual clutter.

### Footer
**`footer`** — A full-width footer with `{colors.canvas}` background, separated from the main content by a `{colors.hairline}` top border. Links use `{typography.link}` in `{colors.body}`, darkening to `{colors.ink}` on hover. Padding is generous at `{spacing.section}` top and bottom, with content arranged in a multi-column grid for desktop and a single column on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; search bar moves to full-width below nav; footer stacks vertically; buttons go full-width; hero section reduces padding |
| Tablet | 744–1128px | Two-column product grid; nav shows limited links (Shop, About) with hamburger for rest; search bar remains in nav but shrinks; footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; search bar in nav; footer uses 4-column layout; max-width container at 1128px |
| Wide | > 1440px | Four-column product grid; same nav layout; content max-width at 1440px with centered alignment; larger whitespace margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Product cards have a minimum tap area of 120px x 120px for the image region.
- Filter tags and badges are at least 32px tall with 14px horizontal padding.
- Nav links have a minimum 44px tap area, even when text is smaller.

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu at < 744px, with a slide-out drawer.
- Product grid columns reduce from 4 to 1 as viewport narrows.
- Footer multi-column layout collapses to a single column at < 744px.
- Search bar transitions from inline (desktop) to full-width below the nav (mobile).
- Hero section padding reduces from `{spacing.section}` on desktop to `{spacing.xl}` on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states:** Extracted only from static CSS; interactive hover/focus/active states for all components may differ from what's documented here. Button hover colors are inferred from the primary-active token.
- **Error styling:** Form error messages, validation states, and error page designs were not extractable from the live site. The `text-input-error` border color is an educated guess based on the red accent.
- **Dark mode:** No dark mode detected on the live site. All colors assume a light theme on `{colors.canvas}` (#f5f5f5).
- **Typography scale:** Font sizes and weights are inferred from common patterns on the site and may not match every page. The brand uses system fonts, so exact sizing may vary by browser.
- **Spacing scale:** The spacing tokens are a best-guess reconstruction from layout measurements; the actual system may use a different base unit or custom values.
- **Component variants:** Only the most common component states are documented. Missing: loading spinners, skeleton screens, toast notifications, modal dialogs, and dropdown menus.
- **Color usage:** The extracted palette includes several accent colors (rose, sage, navy, red, blue, green) that appear on the site but may have specific, undocumented usage rules. The navy `#3a5792` and blue `#7bb1ff` may be third-party widget colors rather than brand colors.
- **Animation:** No animation timing, easing curves, or transition durations were extractable. The brand likely uses subtle transitions (0.2s ease) but this is unconfirmed.
- **Checkout flow:** Shopify checkout is a separate, hosted system with its own design tokens. This document covers only the storefront.
